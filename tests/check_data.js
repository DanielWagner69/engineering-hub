// Static data checks: node tests/check_data.js
const fs = require("fs"), vm = require("vm"), path = require("path");
const ctx = { window: {} }; vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(__dirname, "../data/hub.js"), "utf8"), ctx);
const D = ctx.window.HUB_DATA, errs = [], byId = {};
D.pages.forEach(p => { if (byId[p.id]) errs.push("Duplicate ID " + p.id); byId[p.id] = p; });
const facets = D.facets.map(f => f.key);
D.pages.forEach(p => {
  Object.entries(p.tags || {}).forEach(([k, ids]) => {
    if (!facets.includes(k)) errs.push(p.id + ": unknown facet " + k);
    ids.forEach(id => { if (!byId[id]) errs.push(p.id + ": tag " + id + " not in taxonomy"); else if (byId[id].type !== k) errs.push(p.id + ": " + id + " is a " + byId[id].type + " not a " + k); });
  });
  const txt = [p.summary || ""].concat((p.sections || []).map(s => s.body)).join("\n");
  (txt.match(/\[\[([A-Z]{2,4}-[A-Z0-9]+)\]\]/g) || []).forEach(m => { const id = m.slice(2, -2); if (!byId[id]) errs.push(p.id + ": inline link " + id + " does not exist"); });
});
// Agreed-facet structure checks
D.pages.filter(p => p.type === "system").forEach(p => { if (!byId[p.group] || byId[p.group].type !== "sysgroup") errs.push(p.id + ": bad System Group " + p.group); });
D.pages.filter(p => p.type === "sysgroup").forEach(g => g.members.forEach(m => { if (!byId[m] || byId[m].group !== g.id) errs.push(g.id + ": member " + m + " inconsistent"); }));
D.pages.filter(p => p.type === "srcsystem").forEach(p => {
  const m = p.mapsTo || {}; if (!Object.keys(m).length) errs.push(p.id + ": tracker entry not mapped");
  Object.entries(m).forEach(([k, ids]) => ids.forEach(id => { if (!byId[id] || byId[id].type !== k) errs.push(p.id + ": maps to bad " + k + " " + id); }));
});
D.pages.forEach(p => (p.sources || []).forEach(id => { if (!byId[id] || byId[id].type !== "srcsystem") errs.push(p.id + ": bad source " + id); }));
D.pages.forEach(p => Object.keys(p.derived || {}).forEach(k => { if (!(p.tags || {})[k]) errs.push(p.id + ": derived note for untagged facet " + k); }));
D.pages.filter(p => p.type === "lesson" || p.type === "content").forEach(p => { if (!(p.tags.stage || []).length || !(p.tags.system || []).length) errs.push(p.id + ": mandatory stage/system tag missing"); if ((p.tags.sysgroup || []).length) errs.push(p.id + ": System Group must be derived, not stored"); });
// Facet levels: every facet has a level; views offered together share the level of their top facet
D.facets.forEach(f => { if (!f.level || !f.levelLabel) errs.push("facet " + f.key + " has no level"); });
const fl = Object.fromEntries(D.facets.map(f => [f.key, f.level])), grp = {};
D.views.forEach(v => { (grp[v.group] = grp[v.group] || []).push(fl[v.levels[0]]); });
Object.entries(grp).forEach(([g, ls]) => { if (new Set(ls).size > 1) errs.push("view group '" + g + "' mixes facet levels " + ls.join(",")); });
const srcCount = D.pages.filter(p => p.type === "srcsystem").length; if (srcCount !== 28) errs.push("expected 28 tracker Aircraft System entries, got " + srcCount);
D.issues.forEach(i => i.refs.forEach(id => { if (!byId[id]) errs.push(i.id + ": ref " + id + " missing"); }));
D.views.forEach(v => v.levels.forEach(l => { if (!facets.includes(l)) errs.push("view " + v.key + " level " + l); }));
const counts = {}; D.pages.forEach(p => counts[p.type] = (counts[p.type] || 0) + 1);
console.log("Pages:", JSON.stringify(counts), "Issues:", D.issues.length);
if (errs.length) { console.log("ERRORS:\n" + errs.join("\n")); process.exit(1); } else console.log("Data checks passed: all IDs unique, all tags and links resolve.");
