/* Engineering Hub prototype v0.2 - vanilla JS, hash routing, no external dependencies.
   All content lives once in window.HUB_DATA.pages (flat). Trees are views generated from tags. */
(function () {
  "use strict";
  var D = window.HUB_DATA;
  if (!D) { document.getElementById("page").innerHTML = "<p>Data file data/hub.js not loaded.</p>"; return; }

  // ---------- indexes ----------
  var byId = {}, facetByKey = {}, viewByKey = {};
  D.pages.forEach(function (p) { byId[p.id] = p; });
  D.facets.forEach(function (f) { facetByKey[f.key] = f; });
  D.views.forEach(function (v) { viewByKey[v.key] = v; });
  var TYPE_LABEL = { stage: "Lifecycle Stage", sysgroup: "System Group", system: "System", designtype: "Design Type", productscope: "Product Scope",
    discipline: "Discipline", skill: "Skill", trait: "Trait", srcsystem: "Tracker source entry", content: "Topic (example)", lesson: "Lesson Learned", special: "Hub page" };
  var TYPE_COLOUR = {};
  Object.keys(TYPE_LABEL).forEach(function (k) { TYPE_COLOUR[k] = "var(--" + k + ")"; });
  var TAG_FACETS = ["stage", "system", "designtype", "productscope", "discipline", "skill", "trait"]; // stored tags
  var SHOW_FACETS = ["stage", "sysgroup", "system", "designtype", "productscope", "discipline", "skill", "trait"]; // incl. derived
  var LL_FACETS = ["stage", "system", "designtype", "discipline"];

  function valuesOf(facet) { return D.pages.filter(function (p) { return p.type === facet; }).sort(function (a, b) { return a.order - b.order; }); }
  var contents = D.pages.filter(function (p) { return p.type === "content"; });
  var lessons = D.pages.filter(function (p) { return p.type === "lesson"; });
  var items = contents.concat(lessons);

  function refsInText(t) { var out = [], re = /\[\[([A-Z]{2,4}-[A-Z0-9]+)\]\]/g, m; while ((m = re.exec(t || ""))) out.push(m[1]); return out; }
  function storedTags(p) { var o = []; TAG_FACETS.forEach(function (k) { (p.tags && p.tags[k] || []).forEach(function (id) { o.push(id); }); }); return o; }
  // Derived tags: System Group comes from the System tag(s); never stored.
  function derivedGroups(p) { var g = []; (p.tags && p.tags.system || []).forEach(function (s) { var grp = byId[s] && byId[s].group; if (grp && g.indexOf(grp) < 0) g.push(grp); }); return g; }
  function tagsOf(p, k) { return k === "sysgroup" ? derivedGroups(p) : (p.tags && p.tags[k]) || []; }
  function allTags(p) { return storedTags(p).concat(derivedGroups(p)); }

  // Explicit outgoing links (tags, inline references, structural links), used for backlinks
  var outLinks = {};
  D.pages.forEach(function (p) {
    var s = storedTags(p).concat(refsInText(p.summary));
    (p.sections || []).forEach(function (sec) { s = s.concat(refsInText(sec.body)); });
    if (p.group) s.push(p.group);
    (p.members || []).forEach(function (m) { s.push(m); });
    (p.sources || []).forEach(function (m) { s.push(m); });
    Object.keys(p.mapsTo || {}).forEach(function (k) { s = s.concat(p.mapsTo[k]); });
    outLinks[p.id] = s;
  });
  outLinks["HUB-ISSUES"] = [].concat.apply([], D.issues.map(function (i) { return i.refs; }));
  var backlinks = {};
  Object.keys(outLinks).forEach(function (src) { outLinks[src].forEach(function (t) { if (t !== src) (backlinks[t] = backlinks[t] || {})[src] = true; }); });

  function taggedWith(id) { return items.filter(function (c) { return allTags(c).indexOf(id) >= 0; }); }

  // ---------- helpers ----------
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function scopeOn() { return state.scope && viewByKey[state.view].scopeSelectable; }
  function href(id, ctx) { var h = "#/p/" + encodeURIComponent(id) + "?v=" + state.view + (scopeOn() ? "&s=" + state.scope : ""); if (ctx && ctx.length) h += "&c=" + ctx.map(encodeURIComponent).join(","); return h; }
  function link(id, ctx) { var p = byId[id]; if (!p) return '<span class="warn">Broken link: ' + esc(id) + "</span>"; return '<a href="' + href(id, ctx) + '">' + esc(p.title) + "</a>"; }
  function chip(id, extraCls) { var p = byId[id]; if (!p) return '<span class="chip c-special">missing ' + esc(id) + "</span>"; return '<a class="chip c-' + p.type + (extraCls ? " " + extraCls : "") + '" href="' + href(id) + '" title="' + esc(TYPE_LABEL[p.type]) + '"><span class="cid">' + esc(p.id) + "</span>" + esc(p.title) + "</a>"; }
  function rich(t) {
    var html = "", list = false;
    String(t || "").split("\n").forEach(function (line) {
      var l = esc(line).replace(/\[\[([A-Z]{2,4}-[A-Z0-9]+)\]\]/g, function (_, id) { return link(id); });
      if (/^- /.test(line)) { if (!list) { html += "<ul>"; list = true; } html += "<li>" + l.slice(2) + "</li>"; }
      else { if (list) { html += "</ul>"; list = false; } if (line.trim()) html += "<p>" + l + "</p>"; }
    });
    if (list) html += "</ul>";
    return html;
  }
  function ph(text) { return '<div class="ph"><span class="ph-tag">PLACEHOLDER</span>' + esc(text) + "</div>"; }

  // ---------- state & routing ----------
  var state = { view: "lifecycle", route: "home", id: null, ctx: [], query: "", filter: [], scope: "" };
  try { var saved = window.localStorage && localStorage.getItem("eh-view"); if (saved && viewByKey[saved]) state.view = saved; } catch (e) {}

  function parseHash() {
    var h = (location.hash || "#/home").slice(1), q = {}, path = h, i = h.indexOf("?");
    if (i >= 0) { path = h.slice(0, i); h.slice(i + 1).split("&").forEach(function (kv) { var a = kv.split("="); q[a[0]] = decodeURIComponent(a[1] || ""); }); }
    if (q.v && viewByKey[q.v]) state.view = q.v;
    var parts = path.split("/").filter(Boolean);
    state.scope = q.s && byId[q.s] && byId[q.s].type === "productscope" ? q.s : "";
    state.filter = q.f ? q.f.split(",").filter(function (x) { return byId[x]; }) : [];
    state.ctx = q.c ? q.c.split(",").filter(function (x) { return byId[x]; }) : [];
    if (parts[0] === "p" && parts[1]) { state.route = "page"; state.id = decodeURIComponent(parts[1]); }
    else if (parts[0] === "f" && parts[1]) { state.route = "facet"; state.id = parts[1]; }
    else { state.route = "home"; state.id = null; }
    try { localStorage.setItem("eh-view", state.view); } catch (e) {}
  }
  function setView(v) {
    state.view = v;
    var h = location.hash || "#/home";
    h = h.replace(/([?&])v=[a-z]+/, "$1v=" + v).replace(/[?&]c=[^&]*/, "");
    if (!/[?&]v=/.test(h)) h += (h.indexOf("?") >= 0 ? "&" : "?") + "v=" + v;
    location.hash = h;
  }

  // ---------- tree (generated from tags, any number of levels) ----------
  var expanded = {};
  function buildLevel(levels, pool, ctx) {
    if (!levels.length) return pool.map(function (c) { return { id: c.id, ctx: ctx, key: ctx.concat([c.id]).join("/"), children: [] }; });
    var facet = levels[0], rest = levels.slice(1), vals = valuesOf(facet);
    if (facet === "system") { // under a System Group, show only its member Systems
      var g = ctx.filter(function (id) { return byId[id].type === "sysgroup"; })[0];
      if (g) vals = vals.filter(function (s) { return s.group === g; });
    }
    var nodes = vals.map(function (v) {
      var sub = pool.filter(function (c) { return allTags(c).indexOf(v.id) >= 0; });
      return { id: v.id, ctx: ctx, key: ctx.concat([v.id]).join("/"), count: sub.length, children: buildLevel(rest, sub, ctx.concat([v.id])) };
    });
    pool.filter(function (c) { return !tagsOf(c, facet).length; }).forEach(function (c) { nodes.push({ id: c.id, ctx: ctx, key: ctx.concat([c.id]).join("/"), children: [] }); });
    return nodes;
  }
  // Product Scope (Level 0) is selectable at the top of views whose top facet sits at Level 1
  function buildTree(viewKey, scope) {
    var v = viewByKey[viewKey], sc = scope === undefined ? (v.scopeSelectable ? state.scope : "") : scope;
    var pool = sc ? items.filter(function (c) { return tagsOf(c, "productscope").indexOf(sc) >= 0; }) : items;
    return buildLevel(v.levels, pool, []);
  }
  function registerTree() {
    var cats = {}, order = [];
    valuesOf("trait").forEach(function (t) { if (!cats[t.category]) { cats[t.category] = []; order.push(t.category); } cats[t.category].push(t); });
    function leaf(p) { return { id: p.id, ctx: [], key: "reg/" + p.id, children: [] }; }
    return [
      { label: "Product Scope", facet: "productscope", key: "reg/ps", children: valuesOf("productscope").map(leaf) },
      { label: "Skills Register", facet: "skill", key: "reg/skill", children: valuesOf("skill").map(leaf) },
      { label: "Traits Register", facet: "trait", key: "reg/trait", children: order.map(function (c) { return { label: c, key: "reg/trait/" + c, children: cats[c].map(leaf) }; }) },
      { label: "Tracker Aircraft Systems (source)", facet: "srcsystem", key: "reg/src", children: valuesOf("srcsystem").map(leaf) }
    ];
  }
  function sameCtx(a, b) { return a.join(",") === b.join(","); }
  function markExpanded(nodes, parents) {
    nodes.forEach(function (n) {
      if (n.id && n.id === state.id && (sameCtx(n.ctx || [], state.ctx) || !state.ctx.length)) { parents.forEach(function (k) { expanded[k] = true; }); if (sameCtx(n.ctx || [], state.ctx)) expanded[n.key] = true; }
      if (n.children && n.children.length) markExpanded(n.children, parents.concat([n.key]));
    });
  }
  function renderNodes(nodes) {
    return "<ul>" + nodes.map(function (n) {
      var has = n.children && n.children.length, open = expanded[n.key];
      var p = n.id ? byId[n.id] : null;
      var cur = p && p.id === state.id && sameCtx(n.ctx || [], state.ctx) ? " current" : "";
      var label = p ? '<span class="dot t-' + p.type + '"></span><a href="' + href(p.id, n.ctx) + '" title="' + esc(p.id + " " + p.title) + '">' + esc(p.title) + "</a>"
                    : '<span class="dot t-' + (n.facet || "trait") + '"></span><a href="' + (n.facet ? "#/f/" + n.facet + "?v=" + state.view : "javascript:void 0") + '" data-toggle="' + esc(n.key) + '">' + esc(n.label) + "</a>";
      var badge = n.count != null ? '<span class="badge' + (n.count ? " has" : "") + '" title="topic pages and lessons tagged here">' + n.count + "</span>" : "";
      return '<li><div class="node' + cur + '"><button class="twisty' + (has ? "" : " leaf") + '" data-toggle="' + esc(n.key) + '" aria-label="expand">' + (open ? "\u25BC" : "\u25B6") + "</button>" + label + badge + "</div>" +
             (has && open ? renderNodes(n.children) : "") + "</li>";
    }).join("") + "</ul>";
  }
  function simpleNode(hrefStr, dot, text, current) { return '<li><div class="node' + (current ? " current" : "") + '"><button class="twisty leaf"></button><span class="dot t-' + dot + '"></span><a href="' + hrefStr + '">' + text + "</a></div></li>"; }
  function renderTree() {
    var el = document.getElementById("tree");
    // Views are only offered as alternatives within the same facet level
    var groups = [];
    D.views.forEach(function (v) { var g = groups.filter(function (x) { return x.name === v.group; })[0]; if (!g) { g = { name: v.group, views: [] }; groups.push(g); } g.views.push(v); });
    document.getElementById("view-buttons").innerHTML = groups.map(function (g) {
      var sel = g.views.some(function (v) { return v.scopeSelectable; }) ? (function () {
        var enabled = viewByKey[state.view].scopeSelectable;
        return '<div class="scope-select"><label for="scope-select">Product Scope (Level 0)</label><select id="scope-select"' + (enabled ? "" : ' disabled title="Product Scope applies to the System and Design Type views"') + '><option value="">All scopes</option>' +
          valuesOf("productscope").map(function (ps) { return '<option value="' + ps.id + '"' + (enabled && state.scope === ps.id ? " selected" : "") + ">" + esc(ps.title) + "</option>"; }).join("") + "</select></div>";
      })() : "";
      return '<div class="view-group' + (g.views.some(function (v) { return v.key === state.view; }) ? " has-active" : "") + '"><div class="view-group-label">' + esc(g.name) + "</div>" + sel + '<div class="view-row">' + g.views.map(function (v) {
        return '<button role="tab" data-view="' + v.key + '" class="' + (v.key === state.view ? "active" : "") + '" aria-selected="' + (v.key === state.view) + '" title="' + esc(v.description) + '">' + esc(v.label) + "</button>";
      }).join("") + "</div></div>";
    }).join("");
    document.getElementById("view-desc").textContent = viewByKey[state.view].description;
    if (state.query) { el.innerHTML = renderSearch(state.query); return; }
    var main = buildTree(state.view), reg = registerTree(), v = viewByKey[state.view];
    markExpanded(main, []); markExpanded(reg, []);
    el.innerHTML =
      '<div class="tree-section">Home</div><ul>' + simpleNode("#/home?v=" + state.view, "special", "Engineering Hub home", state.route === "home") + "</ul>" +
      '<div class="tree-section">' + esc(v.label) + " view: " + esc(facetByKey[v.levels[0]].plural) + (scopeOn() ? " \u00b7 " + esc(byId[state.scope].title) : "") + "</div>" + renderNodes(main) +
      '<div class="tree-section">Registers</div>' + renderNodes(reg) +
      '<div class="tree-section">Hub pages</div><ul>' +
      simpleNode(href("HUB-LESSONS"), "lesson", "Lessons Learned (" + lessons.length + ")", state.id === "HUB-LESSONS") +
      simpleNode(href("HUB-ISSUES"), "special", "Framework issues (" + D.issues.length + ")", state.id === "HUB-ISSUES") + "</ul>";
  }
  function renderSearch(q) {
    var s = q.toLowerCase();
    var hits = D.pages.filter(function (p) { return p.id.toLowerCase().indexOf(s) >= 0 || p.title.toLowerCase().indexOf(s) >= 0; });
    if (!hits.length) return '<p class="empty" style="padding:8px">No pages match \u201c' + esc(q) + "\u201d.</p>";
    return '<div class="tree-section">' + hits.length + " result" + (hits.length === 1 ? "" : "s") + '</div><ul class="search-results">' + hits.slice(0, 100).map(function (p) {
      return '<li><div class="node"><span class="dot t-' + p.type + '"></span><a href="' + href(p.id) + '">' + esc(p.title) + '</a><span class="nid">' + esc(p.id) + "</span></div></li>";
    }).join("") + "</ul>";
  }

  // ---------- breadcrumbs (reflect current view) ----------
  function facetLink(k) { return '<a href="#/f/' + k + "?v=" + state.view + '">' + esc(facetByKey[k].plural) + "</a>"; }
  function crumbs() {
    var v = viewByKey[state.view], out = ['<a href="#/home?v=' + state.view + '">Home</a>', '<span class="view-crumb">' + esc(v.label) + " view</span>"];
    if (scopeOn()) out.push('<a href="' + href(state.scope) + '">' + esc(byId[state.scope].title) + "</a>");
    if (state.route === "home") return out;
    if (state.route === "facet") { out.push(esc(facetByKey[state.id] ? facetByKey[state.id].plural : state.id)); return out; }
    var p = byId[state.id]; if (!p) return out;
    var L = v.levels, path = state.ctx.slice();
    if (!path.length) {
      if (p.type === "content" || p.type === "lesson") {
        L.forEach(function (k) { var t = tagsOf(p, k).filter(function (id) { return k !== "system" || !path.length || byId[path[0]].type !== "sysgroup" || byId[id].group === path[0]; })[0]; if (t) path.push(t); });
      } else if (p.type === "system" && L[0] === "sysgroup") path = [p.group];
      else if (p.type !== L[0]) {
        if (["skill", "trait", "srcsystem", "productscope"].indexOf(p.type) >= 0) out.push("Registers");
        if (facetByKey[p.type]) out.push(facetLink(p.type));
        if (p.type === "trait") out.push(esc(p.category));
      }
    }
    path.forEach(function (id, i) { out.push('<a href="' + href(id, path.slice(0, i)) + '">' + esc(byId[id].title) + "</a>"); });
    out.push("<b>" + esc(p.title) + "</b>");
    return out;
  }

  // ---------- page templates ----------
  function verificationPanel(p) {
    return '<div class="panel"><h4>Verification &amp; validation</h4><div class="kv">' +
      '<span class="k">Status</span><span><span class="vstatus">Not verified</span> <span class="ph-tag">PLACEHOLDER</span></span>' +
      '<span class="k">Owner</span><span class="empty">To be assigned (placeholder)</span>' +
      '<span class="k">Last reviewed</span><span class="empty">Not yet reviewed (placeholder)</span>' +
      '<span class="k">Next review</span><span class="empty">To be set (placeholder)</span></div></div>';
  }
  function metaPanel(p) {
    var f = facetByKey[p.type];
    var rows = '<span class="k">Permanent ID</span><span class="mono">' + esc(p.id) + "</span>" + '<span class="k">Page type</span><span>' + esc(TYPE_LABEL[p.type]) + "</span>";
    if (f) rows += '<span class="k">Facet</span><span><a href="#/f/' + f.key + "?v=" + state.view + '">' + esc(f.label) + "</a></span>" + '<span class="k">Source</span><span>' + esc(f.source) + "</span>" +
      '<span class="k">Hierarchy level</span><span>' + esc(f.levelLabel) + "</span>";
    if (p.status) rows += '<span class="k">Status</span><span>' + esc(p.status) + "</span>";
    if (p.group) rows += '<span class="k">System Group</span><span>' + chip(p.group) + "</span>";
    if (p.sourceCategory && p.type !== "trait") rows += '<span class="k">Source category</span><span>' + esc(p.sourceCategory) + "</span>";
    if (p.category) rows += '<span class="k">Trait category</span><span>' + esc(p.category) + "</span>";
    if (p.sources) rows += '<span class="k">Source</span><span><div class="chips">' + p.sources.map(function (id) { return chip(id); }).join("") + "</div></span>";
    if (p.origin) rows += '<span class="k">Origin</span><span>' + (p.origin.url ? '<a href="' + esc(p.origin.url) + '">' + esc(p.origin.document) + "</a>" : esc(p.origin.document)) + ", issue: " + esc(p.origin.issue) + "</span>";
    var html = '<div class="panel"><h4>Metadata</h4><div class="kv">' + rows + "</div>";
    if (storedTags(p).length) {
      html += '<h4 style="margin-top:12px">Tags</h4>' + SHOW_FACETS.filter(function (k) { return tagsOf(p, k).length; }).map(function (k) {
        var der = k === "sysgroup" ? "derived from System" : (p.derived && p.derived[k] ? "derived from components" : "");
        return '<div style="margin:6px 0"><div style="color:var(--muted);font-size:.78rem">' + esc(facetByKey[k].label) + (der ? ' <span class="derived-tag" title="' + esc(k === "sysgroup" ? "System Group is derived from the System tag(s); it is never stored." : p.derived[k]) + '">' + der + "</span>" : "") +
          '</div><div class="chips">' + tagsOf(p, k).map(function (id) { return chip(id, der ? "derived" : ""); }).join("") + "</div>" +
          (p.derived && p.derived[k] ? '<div class="derived-note">' + esc(p.derived[k]) + "</div>" : "") + "</div>";
      }).join("");
    }
    return html + "</div>";
  }
  function backlinkSection(p) {
    var b = Object.keys(backlinks[p.id] || {});
    return "<h2>Pages that link here</h2>" + (b.length ? '<ul class="linklist">' + b.map(function (id) { return "<li>" + link(id) + ' <span class="mono" style="color:var(--muted)">' + esc(id) + "</span></li>"; }).join("") + "</ul>" : '<p class="empty">No pages link here yet.</p>');
  }
  function head(p) {
    return '<div class="page-head"><span class="type-pill" style="background:' + TYPE_COLOUR[p.type] + '">' + esc(TYPE_LABEL[p.type]) + '</span><div><div class="page-id">' + esc(p.id) + "</div><h1>" + esc(p.title) + "</h1></div></div>";
  }
  function relatedSection(p) {
    var html = "<h2>Related pages</h2>";
    if (p.members) html += '<h3>Systems in this group</h3><div class="chips">' + p.members.map(function (id) { return chip(id); }).join("") + "</div>";
    var tagged = taggedWith(p.id), topics = tagged.filter(function (c) { return c.type === "content"; });
    if (topics.length) html += "<h3>Topic pages tagged with this " + esc(TYPE_LABEL[p.type].toLowerCase()) + '</h3><div class="chips">' + topics.map(function (c) { return chip(c.id); }).join("") + "</div>";
    var co = {};
    tagged.forEach(function (c) { allTags(c).forEach(function (id) { var t = byId[id].type; if (id !== p.id && t !== p.type && !(p.type === "system" && t === "sysgroup") && !(p.type === "sysgroup" && t === "system")) (co[t] = co[t] || {})[id] = true; }); });
    SHOW_FACETS.forEach(function (k) { if (co[k]) html += "<h3>Linked " + esc(facetByKey[k].plural) + ' (via shared topics and lessons)</h3><div class="chips">' + Object.keys(co[k]).map(function (id) { return chip(id); }).join("") + "</div>"; });
    var sibs = valuesOf(p.type).filter(function (x) { return (p.type !== "trait" || x.category === p.category) && (p.type !== "system" || x.group === p.group); });
    var i = sibs.map(function (x) { return x.id; }).indexOf(p.id), nb = [];
    if (i > 0) nb.push("\u2190 Previous: " + link(sibs[i - 1].id));
    if (i >= 0 && i < sibs.length - 1) nb.push("Next: " + link(sibs[i + 1].id) + " \u2192");
    if (nb.length) html += "<h3>" + (p.type === "stage" ? "Adjacent lifecycle stages" : "Neighbouring entries in the " + esc(p.type === "trait" ? p.category + " category" : p.type === "system" ? byId[p.group].title + " group" : facetByKey[p.type].label + " list")) + "</h3><p>" + nb.join(" &nbsp;|&nbsp; ") + "</p>";
    if (!tagged.length && p.type !== "srcsystem") html += ph("Cross-links to related values in other facets will appear automatically when topic pages or lessons are tagged with this value.");
    return html;
  }
  function contextBox(p) {
    if (!state.ctx.length || p.type === "content" || p.type === "lesson") return "";
    var ctxIds = state.ctx.concat([p.id]);
    var its = items.filter(function (c) { var t = allTags(c); return ctxIds.every(function (id) { return t.indexOf(id) >= 0; }); });
    return '<div class="ctx"><b>In this view context:</b> ' + ctxIds.map(function (id) { return esc(byId[id].title); }).join(" \u203a ") + ". " +
      (its.length ? "Topic pages and lessons tagged with all of these: " + its.map(function (c) { return link(c.id, ctxIds); }).join(", ") : "No topic pages or lessons are tagged with this combination yet.") + "</div>";
  }
  function lessonsSection(p) {
    var ls = lessons.filter(function (l) { return allTags(l).indexOf(p.id) >= 0; });
    var canFilter = LL_FACETS.indexOf(p.type) >= 0;
    return "<h2>Lessons learned</h2>" + (ls.length
      ? '<ul class="linklist">' + ls.map(function (l) { return "<li>" + link(l.id) + ' <span class="mono" style="color:var(--muted)">' + esc(l.id) + "</span> \u2013 " + esc(l.summary) + "</li>"; }).join("") + "</ul>"
      : '<p class="empty">No lessons are tagged with this value yet.</p>') +
      (canFilter ? '<p><a href="' + href("HUB-LESSONS") + "&f=" + encodeURIComponent(p.id) + '">Open Lessons Learned filtered to \u201c' + esc(p.title) + "\u201d \u2192</a></p>" : "");
  }
  function mappingBox(p) {
    var m = p.mapsTo || {};
    return '<div class="' + (p.mappingClean ? "ctx" : "warn") + '"><b>Tracker source entry, kept as a source reference.</b> It is no longer used for tagging. Maps to: ' +
      Object.keys(m).map(function (k) { return esc(facetByKey[k].label) + " " + m[k].map(function (id) { return chip(id); }).join(" "); }).join(" + ") +
      (p.mappingClean ? " (one-to-one)." : "<br><b>Not a clean mapping:</b> " + esc(p.mappingNote) + " See " + link("HUB-ISSUES") + ".") +
      (p.mappingClean && p.mappingNote ? "<br>" + esc(p.mappingNote) : "") + "</div>";
  }
  function renderValuePage(p) {
    var desc;
    if (p.description) desc = "<p>" + esc(p.description) + "</p>";
    else if (p.agreed) desc = ph("Description of this " + TYPE_LABEL[p.type].toLowerCase() + "'s function and boundary to be written (agreed by name and rule only).");
    else desc = '<div class="warn"><b>No description in the source register.</b> The tracker has no description for this entry, so it is shown here as a gap rather than invented. See ' + link("HUB-ISSUES") + ".</div>";
    var f = facetByKey[p.type];
    var rule = f && f.note && ["system", "sysgroup", "designtype", "productscope"].indexOf(p.type) >= 0 ? '<p class="facet-rule"><b>' + esc(f.label) + ":</b> " + esc(f.note) + "</p>" : "";
    var taggable = ["stage", "sysgroup", "system", "designtype", "productscope", "discipline"].indexOf(p.type) >= 0;
    return head(p) + '<div class="grid"><div>' + (p.type === "srcsystem" ? mappingBox(p) : "") + contextBox(p) + "<h2>Description</h2>" + desc + rule +
      "<h2>Key considerations</h2>" + ph("Key considerations for \u201c" + p.title + "\u201d to be written and verified by a nominated owner.") +
      (taggable ? lessonsSection(p) : "") +
      relatedSection(p) +
      "<h2>Learning resources</h2>" + ph("Links to courses, standards, handbooks and internal guidance to be added.") +
      backlinkSection(p) + "</div><div>" + metaPanel(p) + verificationPanel(p) + "</div></div>";
  }
  function lessonMatches(l, filter) {
    return LL_FACETS.every(function (k) {
      var sel = filter.filter(function (id) { return byId[id].type === k; });
      return !sel.length || sel.some(function (id) { return tagsOf(l, k).indexOf(id) >= 0; });
    });
  }
  function renderLessonsIndex(p) {
    var f = state.filter, res = lessons.filter(function (l) { return lessonMatches(l, f); });
    function opt(v, k) {
      var n = lessons.filter(function (l) { return tagsOf(l, k).indexOf(v.id) >= 0; }).length;
      return '<label class="' + (n ? "" : "zero") + '"><input type="checkbox" data-filter="' + v.id + '"' + (f.indexOf(v.id) >= 0 ? " checked" : "") + "> " + esc(v.title) + ' <span class="badge' + (n ? " has" : "") + '">' + n + "</span></label>";
    }
    var boxes = LL_FACETS.map(function (k) {
      var body = k === "system" ? valuesOf("sysgroup").map(function (g) { return '<div class="opt-group">' + esc(g.title) + "</div>" + valuesOf("system").filter(function (s) { return s.group === g.id; }).map(function (v) { return opt(v, k); }).join(""); }).join("")
                                : valuesOf(k).map(function (v) { return opt(v, k); }).join("");
      return '<div class="facet-box"><h4>' + esc(facetByKey[k].label) + '</h4><div class="facet-opts">' + body + "</div></div>";
    }).join("");
    return head(p) + "<p>" + esc(p.summary) + " Tick any combination: lessons must match at least one ticked value in <b>every</b> facet where something is ticked (OR within a facet, AND across facets), so you see all applicable and only applicable lessons.</p>" +
      '<div class="example-banner"><b>Example content.</b> All ' + lessons.length + " lessons in this prototype are fictional examples written to demonstrate the template and filtering; none is authoritative engineering guidance.</div>" +
      '<div class="facet-filters">' + boxes + "</div>" +
      "<p><b>" + res.length + " of " + lessons.length + " lessons match</b>" + (f.length ? ' \u00b7 filters: <span class="chips" style="display:inline-flex">' + f.map(function (id) { return chip(id); }).join("") + '</span> \u00b7 <a href="' + href("HUB-LESSONS") + '">Clear all</a>' : " (no filters applied)") + "</p>" +
      '<table class="list"><thead><tr><th>ID</th><th>Lesson</th><th>Summary</th><th>Tags</th></tr></thead><tbody>' +
      (res.length ? res.map(function (l) { return '<tr><td class="mono">' + esc(l.id) + "</td><td>" + link(l.id) + "</td><td>" + esc(l.summary) + '</td><td><div class="chips">' + storedTags(l).filter(function (id) { return LL_FACETS.indexOf(byId[id].type) >= 0; }).map(function (id) { return chip(id); }).join("") + "</div></td></tr>"; }).join("")
                  : '<tr><td colspan="4" class="empty">No lessons match this combination.</td></tr>') + "</tbody></table>" + backlinkSection(p);
  }
  function renderLessonPage(p) {
    var others = lessons.filter(function (c) { return c.id !== p.id && storedTags(c).some(function (id) { return storedTags(p).indexOf(id) >= 0; }); });
    var o = p.origin || {};
    return head(p) + '<div class="example-banner"><b>EXAMPLE lesson.</b> ' + esc(p.exampleNote) + "</div>" +
      '<div class="grid"><div><h2>Summary</h2><p>' + esc(p.summary) + "</p>" +
      "<h2>What happened</h2><p>" + esc(p.whatHappened) + "</p>" +
      "<h2>Root cause</h2><p>" + esc(p.rootCause) + "</p>" +
      "<h2>Recommendation</h2><p>" + esc(p.recommendation) + "</p>" +
      "<h2>Applicability</h2><p>" + esc(p.applicability) + "</p>" +
      "<h2>Source / origin</h2><p><b>Origin:</b> " + (o.url ? '<a href="' + esc(o.url) + '">' + esc(o.document) + "</a>" : esc(o.document || "Not recorded")) + ", issue " + esc(o.issue || "not recorded") + "</p>" +
      (o.url ? "" : ph("Link to the originating document, with its issue/revision and references, to be added. Once verified, this structured record is the authoritative (master) source; the original document is kept as its linked origin only.")) +
      "<h2>Related pages</h2>" + (others.length ? '<h3>Other lessons sharing a tag</h3><div class="chips">' + others.map(function (c) { return chip(c.id); }).join("") + "</div>" : '<p class="empty">No other lessons share a tag.</p>') +
      "<p>See all lessons: " + link("HUB-LESSONS") + ".</p>" +
      backlinkSection(p) + "</div><div>" + metaPanel(p) + verificationPanel(p) + "</div></div>";
  }
  function renderContentPage(p) {
    var others = contents.filter(function (c) { return c.id !== p.id && storedTags(c).some(function (id) { return storedTags(p).indexOf(id) >= 0; }); });
    return head(p) + '<div class="example-banner"><b>Example content.</b> ' + esc(p.exampleNote) + "</div>" +
      '<div class="grid"><div><p><i>' + rich(p.summary).replace(/^<p>|<\/p>$/g, "") + "</i></p>" +
      p.sections.map(function (s) { return "<h2>" + esc(s.heading) + "</h2>" + rich(s.body); }).join("") +
      "<h2>Related pages</h2><p>Every tag in the metadata panel is a link to that value's page. This page is stored once and appears under each of its tags in every view.</p>" +
      (others.length ? '<h3>Other topics sharing a tag</h3><div class="chips">' + others.map(function (c) { return chip(c.id); }).join("") + "</div>" : "") +
      "<h2>Learning resources</h2>" + ph("Links to courses, standards and guidance to be added.") +
      backlinkSection(p) + "</div><div>" + metaPanel(p) + verificationPanel(p) + "</div></div>";
  }
  function renderIssues(p) {
    var counts = {}; D.issues.forEach(function (i) { counts[i.status] = (counts[i.status] || 0) + 1; });
    return head(p) + "<p>" + esc(p.summary) + "</p>" +
      "<p>" + Object.keys(counts).map(function (k) { return '<span class="status s-' + k.replace(/\s/g, "") + '">' + esc(k) + "</span> " + counts[k]; }).join(" &nbsp; ") + "</p>" +
      '<p style="font-size:.85rem;color:var(--muted)">Source: ' + esc(D.meta.source) + ". Generated " + esc(D.meta.generated) + ". Checks marked \u2018Auto-detected\u2019 are produced by scripts/build_data.py each time the data is regenerated.</p>" +
      D.issues.map(function (i) {
        return '<div class="issue i-' + i.status.replace(/\s/g, "") + '" id="' + i.id + '"><div class="kind">' + esc(i.id) + " \u00b7 " + esc(i.kind) + ' \u00b7 <span class="status s-' + i.status.replace(/\s/g, "") + '">' + esc(i.status) + "</span></div><h3>" + esc(i.title) + "</h3>" + (i.detail ? "<p>" + esc(i.detail) + "</p>" : "") +
          (i.resolution ? '<p class="resolution"><b>' + esc(i.status) + ":</b> " + esc(i.resolution.replace(/^(Resolved|Partly resolved|For review):\s*/i, "")) + "</p>" : "") +
          (i.refs.length ? '<div class="chips">' + i.refs.map(function (id) { return chip(id); }).join("") + "</div>" : "") + "</div>";
      }).join("") + backlinkSection(p);
  }
  function renderFacet(key) {
    var f = facetByKey[key]; if (!f) return "<p>Unknown facet.</p>";
    var vals = valuesOf(key), extra = key === "trait" ? "Category" : key === "system" ? "System Group" : key === "srcsystem" ? "Maps to" : key === "sysgroup" ? "Systems" : null;
    function extraCell(v) {
      if (key === "trait") return esc(v.category);
      if (key === "system") return link(v.group);
      if (key === "sysgroup") return v.members.length;
      if (key === "srcsystem") return '<div class="chips">' + Object.keys(v.mapsTo).map(function (k) { return v.mapsTo[k].map(function (id) { return chip(id); }).join(""); }).join("") + "</div>" + (v.mappingClean ? "" : '<span class="status s-Open">not clean</span>');
      return "";
    }
    return '<div class="page-head"><span class="type-pill" style="background:' + TYPE_COLOUR[key] + '">Facet</span><div><div class="page-id">' + esc(f.source) + "</div><h1>" + esc(f.plural) + "</h1></div></div>" +
      (f.note ? '<p class="facet-rule">' + esc(f.note) + "</p>" : "") + "<p><b>Hierarchy level:</b> " + esc(f.levelLabel) + "</p><p>" + vals.length + " values. Each is a page with a permanent ID.</p>" +
      '<table class="list"><thead><tr><th>ID</th><th>' + esc(f.label) + "</th>" + (extra ? "<th>" + extra + "</th>" : "") + "<th>Description</th><th>Tagged items</th></tr></thead><tbody>" +
      vals.map(function (v) { return '<tr><td class="mono">' + esc(v.id) + "</td><td>" + link(v.id) + "</td>" + (extra ? "<td>" + extraCell(v) + "</td>" : "") + "<td>" + (v.description ? esc(v.description) : '<span class="empty">No description yet</span>') + "</td><td>" + taggedWith(v.id).length + "</td></tr>"; }).join("") + "</tbody></table>";
  }
  function renderHome() {
    var v = viewByKey[state.view];
    var cardFacets = ["stage", "sysgroup", "system", "designtype", "productscope", "discipline", "skill", "trait"];
    var cards = cardFacets.map(function (k) { return '<a class="card" style="border-top-color:' + TYPE_COLOUR[k] + '" href="#/f/' + k + "?v=" + state.view + '"><div class="n">' + valuesOf(k).length + '</div><div class="l">' + esc(facetByKey[k].plural) + "</div></a>"; }).join("") +
      '<a class="card" style="border-top-color:var(--content)" href="' + href(contents[0].id) + '"><div class="n">' + contents.length + '</div><div class="l">Example topic pages</div></a>' +
      '<a class="card" style="border-top-color:var(--lesson)" href="' + href("HUB-LESSONS") + '"><div class="n">' + lessons.length + '</div><div class="l">Example lessons learned</div></a>' +
      '<a class="card" style="border-top-color:var(--srcsystem)" href="#/f/srcsystem?v=' + state.view + '"><div class="n">' + valuesOf("srcsystem").length + '</div><div class="l">Tracker source entries (mapped)</div></a>' +
      '<a class="card" style="border-top-color:var(--special)" href="' + href("HUB-ISSUES") + '"><div class="n">' + D.issues.length + '</div><div class="l">Framework issues</div></a>';
    return '<div class="page-head"><span class="type-pill" style="background:var(--primary)">Home</span><div><div class="page-id">' + esc(D.meta.version) + "</div><h1>Engineering Hub</h1></div></div>" +
      "<p>An interactive, linked knowledge site for the <b>education</b> of engineers, the <b>verification and validation</b> of information, and <b>navigation</b> of engineering knowledge across the Air System Engineering Lifecycle. The former Design Hub becomes one part of it.</p>" +
      "<h2>How it works: one store, many views</h2>" +
      "<ul><li>Every page is stored <b>once</b>, in a flat list, with a <b>permanent ID</b> (e.g. <span class=\"mono\">SYS-0007</span>, <span class=\"mono\">KN-0005</span>).</li>" +
      "<li>Pages are <b>tagged</b> with values from controlled facets: Lifecycle Stage, System (two levels: System Group \u203a System), Design Type, Product Scope and Discipline, plus the Skills and Traits registers.</li>" +
      "<li>There is no fixed tree. The navigation tree on the left is a <b>view generated from the tags</b>. Switch between <b>Lifecycle</b>, <b>System</b>, <b>Design Type</b> and <b>Discipline</b> views; the same page is reached by different routes, never duplicated.</li>" +
      "<li><b>Facet levels:</b> every facet is assigned to a defined level. Product Scope (Aircraft, Ground Equipment, Test Equipment, Facilities) is Level 0 and can be selected at the top of the System and Design Type views. System and Design Type both sit at Level 1, directly below any Product Scope item (e.g. Full Aircraft), so either can structure that level; the view switcher only offers alternatives at the same level. Lifecycle and Discipline are cross-cutting. Each facet's level is shown in its metadata panel.</li>" +
      "<li><b>Systems span scopes:</b> the System facet applies to every Product Scope, and interfaces between items in different scopes within the same System are links, not parent levels (see " + link("EX-0005") + ").</li>" +
      "<li><b>Derived tags:</b> an assembly takes its System tag(s) from its components (a loom shows the Systems of its wires), and System Group is always derived from System.</li>" +
      "<li><b>Lessons Learned</b> use one standard template and the same tags, so " + link("HUB-LESSONS") + " can be filtered by any combination of stage, system, design type and discipline.</li>" +
      "<li>Every page carries verification status, owner and last-reviewed fields (placeholders in this prototype).</li></ul>" +
      "<p>Current view: <b>" + esc(v.label) + "</b> (" + esc(v.description) + ").</p>" +
      '<div class="cards">' + cards + "</div>" +
      "<h2>Example topic pages (intersections)</h2><p>These demonstrate a single page tagged with several facets. Open one, then switch views: it stays the same page while the tree and breadcrumbs change.</p>" +
      '<table class="list"><thead><tr><th>ID</th><th>Topic</th><th>Tags</th></tr></thead><tbody>' +
      contents.map(function (c) { return '<tr><td class="mono">' + esc(c.id) + "</td><td>" + link(c.id) + '</td><td><div class="chips">' + storedTags(c).filter(function (id) { return ["stage", "system", "designtype"].indexOf(byId[id].type) >= 0; }).map(function (id) { return chip(id); }).join("") + "</div></td></tr>"; }).join("") + "</tbody></table>" +
      '<div class="warn" style="margin-top:18px"><b>Prototype.</b> Lifecycle Stage, Discipline, Skill and Trait names and IDs come from the tracker registers; System, Design Type and Product Scope are the facets agreed on 2 Oct 2026, with the tracker\'s Aircraft System entries kept as mapped source references. All guidance text, owners and review dates are placeholders or clearly labelled examples. ' + D.issues.length + " framework issues are listed on " + link("HUB-ISSUES") + ".</div>";
  }

  // ---------- render ----------
  var keepScroll = false;
  function render() {
    parseHash();
    var el = document.getElementById("page"), html;
    if (state.route === "home") { html = renderHome(); document.title = "Engineering Hub"; }
    else if (state.route === "facet") { html = renderFacet(state.id); document.title = (facetByKey[state.id] ? facetByKey[state.id].plural + " \u2013 " : "") + "Engineering Hub"; }
    else {
      var p = byId[state.id];
      if (!p) html = '<h1>Page not found</h1><p>No page has ID <span class="mono">' + esc(state.id) + "</span>.</p>";
      else if (p.type === "content") html = renderContentPage(p);
      else if (p.id === "HUB-ISSUES") html = renderIssues(p);
      else if (p.id === "HUB-LESSONS") html = renderLessonsIndex(p);
      else if (p.type === "lesson") html = renderLessonPage(p);
      else html = renderValuePage(p);
      document.title = (p ? p.id + " " + p.title + " \u2013 " : "") + "Engineering Hub";
    }
    el.innerHTML = html;
    document.getElementById("breadcrumbs").innerHTML = crumbs().join('<span class="sep">\u203a</span>');
    document.getElementById("footer").textContent = "Engineering Hub " + D.meta.version + " \u00b7 data generated " + D.meta.generated + " \u00b7 " + D.pages.length + " pages \u00b7 " + D.meta.source;
    renderTree();
    var cur = document.querySelector(".tree .node.current"); if (cur && cur.scrollIntoView) cur.scrollIntoView({ block: "nearest" });
    if (state.id !== "HUB-LESSONS" || !keepScroll) document.querySelector(".main").scrollTop = 0;
    keepScroll = state.id === "HUB-LESSONS";
  }

  // ---------- events ----------
  document.getElementById("view-buttons").addEventListener("click", function (e) { var b = e.target.closest("button[data-view]"); if (b) setView(b.getAttribute("data-view")); });
  document.getElementById("view-buttons").addEventListener("change", function (e) {
    if (e.target.id !== "scope-select") return;
    var h = (location.hash || "#/home").replace(/[?&]s=[^&]*/, "").replace(/[?&]c=[^&]*/, "");
    if (e.target.value) h += (h.indexOf("?") >= 0 ? "&" : "?") + "s=" + e.target.value;
    location.hash = h;
  });
  document.getElementById("tree").addEventListener("click", function (e) {
    var t = e.target.closest("[data-toggle]");
    if (t && (t.tagName === "BUTTON" || t.getAttribute("href") === "javascript:void 0")) { e.preventDefault(); var k = t.getAttribute("data-toggle"); expanded[k] = !expanded[k]; renderTree(); }
  });
  document.getElementById("page").addEventListener("change", function (e) {
    var cb = e.target.closest("input[data-filter]"); if (!cb) return;
    var f = state.filter.slice(), id = cb.getAttribute("data-filter"), i = f.indexOf(id);
    if (cb.checked && i < 0) f.push(id); if (!cb.checked && i >= 0) f.splice(i, 1);
    location.hash = href("HUB-LESSONS") + (f.length ? "&f=" + f.map(encodeURIComponent).join(",") : "");
  });
  var search = document.getElementById("search");
  search.addEventListener("input", function () { state.query = search.value.trim(); renderTree(); });
  search.addEventListener("keydown", function (e) {
    if (e.key === "Escape") { search.value = ""; state.query = ""; renderTree(); }
    if (e.key === "Enter") { var a = document.querySelector(".search-results a"); if (a) location.hash = a.getAttribute("href"); }
  });
  window.addEventListener("hashchange", render);
  window.EH = { data: D, byId: byId, backlinks: backlinks, outLinks: outLinks, buildTree: buildTree, render: render, allTags: allTags };
  render();
})();
