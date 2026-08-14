document.addEventListener('DOMContentLoaded', () => {
  const base = window.location.href.split('#')[0];
  document.querySelectorAll('.pl-water path[stroke^="url(#"]').forEach(el => {
    const id = el.getAttribute('stroke').match(/url\(['"]?#([^)'"]+)['"]?\)/)[1];
    el.setAttribute('stroke', `url(${base}#${id})`);
  });
  document.querySelectorAll('.pl-water g[filter^="url(#"]').forEach(el => {
    const id = el.getAttribute('filter').match(/url\(['"]?#([^)'"]+)['"]?\)/)[1];
    el.setAttribute('filter', `url(${base}#${id})`);
  });
  document.querySelectorAll('.pl-water [fill^="url(#"]').forEach(el => {
    const id = el.getAttribute('fill').match(/url\(['"]?#([^)'"]+)['"]?\)/)[1];
    el.setAttribute('fill', `url(${base}#${id})`);
  });
});
