(function () {
  var POSTHOG_TOKEN = "phc_GP4P9O2ico9bpf1NDu9O3aSx2SFJIH6E0jn2TNX64hv";
  var POSTHOG_HOST = "https://eu.i.posthog.com";
  var SITE = "personal-website";

  if (window.location.pathname.indexOf("posthog-application.html") !== -1) {
    return;
  }

  !function (t, e) { var o, n, p, r; e.__SV || (window.posthog = e, e._i = [], e.init = function (i, s, a) { function g(t, e) { var o = e.split("."); 2 == o.length && (t = t[o[0]], e = o[1]), t[e] = function () { t.push([e].concat(Array.prototype.slice.call(arguments, 0))) } } (p = t.createElement("script")).type = "text/javascript", p.crossOrigin = "anonymous", p.async = !0, p.src = s.api_host.replace(".i.posthog.com", "-assets.i.posthog.com") + "/static/array.js", (r = t.getElementsByTagName("script")[0]).parentNode.insertBefore(p, r); var u = e; for (void 0 !== a ? u = e[a] = [] : a = "posthog", u.people = u.people || [], u.toString = function (t) { var e = "posthog"; return "posthog" !== a && (e += "." + a), t || (e += " (stub)"), e }, u.people.toString = function () { return u.toString(1) + ".people (stub)" }, o = "init capture register register_once register_for_session unregister unregister_for_session getFeatureFlag getFeatureFlagPayload isFeatureEnabled reloadFeatureFlags updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures on onFeatureFlags onSessionId getSurveys getActiveMatchingSurveys renderSurvey canRenderSurvey getNextSurveyStep identify setPersonProperties group resetGroups setPersonPropertiesForFlags resetPersonPropertiesForFlags setGroupPropertiesForFlags resetGroupPropertiesForFlags reset get_distinct_id getGroups get_session_id get_session_replay_url alias set_config startSessionRecording stopSessionRecording sessionRecordingStarted captureException loadToolbar get_property getSessionProperty createPersonProfile opt_in_capturing opt_out_capturing has_opted_in_capturing has_opted_out_capturing clear_opt_in_out_capturing debug".split(" "), n = 0; n < o.length; n++)g(u, o[n]); e._i.push([i, s, a]) }, e.__SV = 1) }(document, window.posthog || []);

  posthog.init(POSTHOG_TOKEN, {
    api_host: POSTHOG_HOST,
    defaults: "2026-01-30",
    autocapture: false,
    capture_pageview: false,
    capture_pageleave: false,
    disable_session_recording: true,
    person_profiles: "never",
    respect_dnt: true
  });

  function props(extra) {
    return Object.assign({ site: SITE }, extra || {});
  }

  function capture(name, extra) {
    if (window.posthog && typeof window.posthog.capture === "function") {
      window.posthog.capture(name, props(extra));
    }
  }

  function labelForLink(link) {
    return (
      link.getAttribute("data-analytics-label") ||
      link.getAttribute("aria-label") ||
      link.getAttribute("title") ||
      link.textContent ||
      ""
    ).trim();
  }

  function destinationForLink(link) {
    var raw = link.getAttribute("href") || "";
    if (raw.indexOf("mailto:") === 0) return "mailto";
    try {
      return new URL(raw, window.location.href).href;
    } catch (_) {
      return raw;
    }
  }

  function classifyLink(link) {
    var href = link.getAttribute("href") || "";
    var normalized = href.toLowerCase();
    var label = labelForLink(link).toLowerCase();

    if (normalized.indexOf("github.com/dragutin-oreski/pokedex") !== -1) return "pokedex_repo";
    if (normalized.indexOf("github.com") !== -1) return "github";
    if (normalized.indexOf("linkedin.com") !== -1) return "linkedin";
    if (normalized.indexOf("mailto:") === 0) return "email";
    if (normalized.indexOf("dragutin_oreski_cv.pdf") !== -1) return "cv";
    if (normalized.indexOf("courses/ui-suputnik") !== -1 || label.indexOf("ui suputnik") !== -1) return "ui_suputnik";
    if (normalized.indexOf("strategy.dragutinoreski.com") !== -1 || label.indexOf("strategy") !== -1) return "strategy_analyzer";
    return "";
  }

  function trackUsefulLinks() {
    document.querySelectorAll("a[href]").forEach(function (link) {
      var target = classifyLink(link);
      if (!target) return;

      link.addEventListener("click", function () {
        capture("website_link_clicked", {
          link_type: target,
          label: labelForLink(link),
          destination: destinationForLink(link),
          page_path: window.location.pathname
        });
      });
    });
  }

  function start() {
    capture("$pageview", { page_path: window.location.pathname });
    trackUsefulLinks();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else {
    start();
  }
})();
