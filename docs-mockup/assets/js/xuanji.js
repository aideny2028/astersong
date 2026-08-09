/* Xuanji docs, small progressive-enhancement helpers. No dependencies. */
(function () {
  "use strict";

  /* install / code tabs */
  document.querySelectorAll("[data-tabs]").forEach(function (group) {
    var tabs = group.querySelectorAll(".codecard__tab");
    var panes = group.querySelectorAll("[data-pane]");
    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        var name = tab.getAttribute("data-tab");
        tabs.forEach(function (t) { t.classList.toggle("is-active", t === tab); });
        panes.forEach(function (p) {
          p.hidden = p.getAttribute("data-pane") !== name;
        });
      });
    });
  });

  /* click-to-copy pip chip (and any [data-copy]) */
  document.querySelectorAll("[data-copy]").forEach(function (el) {
    el.addEventListener("click", function () {
      var text = el.getAttribute("data-copy");
      if (navigator.clipboard) {
        navigator.clipboard.writeText(text).then(function () {
          var prev = el.getAttribute("data-label") || "";
          el.classList.add("copied");
          setTimeout(function () { el.classList.remove("copied"); }, 1200);
        });
      }
    });
  });

  /* mobile docs sidebar toggle */
  var toggle = document.querySelector(".menu-toggle");
  var side = document.querySelector(".docs__side");
  if (toggle && side) {
    toggle.addEventListener("click", function () {
      side.classList.toggle("is-open");
    });
  }

  /* scrollspy for the on-this-page TOC */
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll(".toc-list a"));
  if (tocLinks.length && "IntersectionObserver" in window) {
    var map = {};
    tocLinks.forEach(function (a) {
      var id = a.getAttribute("href").slice(1);
      var target = document.getElementById(id);
      if (target) map[id] = a;
    });
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          tocLinks.forEach(function (a) { a.classList.remove("is-active"); });
          var a = map[e.target.id];
          if (a) a.classList.add("is-active");
        }
      });
    }, { rootMargin: "-70px 0px -70% 0px", threshold: 0 });
    Object.keys(map).forEach(function (id) {
      var t = document.getElementById(id);
      if (t) obs.observe(t);
    });
  }
})();
