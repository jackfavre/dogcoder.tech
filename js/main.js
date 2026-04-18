(function () {
  const stage = document.getElementById("stage");
  const replayBtn = document.getElementById("replay-btn");
  const caption = document.getElementById("stage-caption");
  const yearEl = document.getElementById("year");

  if (yearEl) {
    yearEl.textContent = String(new Date().getFullYear());
  }

  const captions = [
    { t: 0, text: "Here we go…" },
    { t: 2200, text: "Jump! Nice." },
    { t: 5200, text: "Wait—" },
    { t: 6800, text: "CAUGHT IN 4K" },
  ];

  let captionTimerIds = [];

  function clearCaptionTimers() {
    captionTimerIds.forEach(function (id) {
      clearTimeout(id);
    });
    captionTimerIds = [];
  }

  function scheduleCaptions() {
    clearCaptionTimers();
    if (!caption) return;
    captions.forEach(function (item) {
      const id = setTimeout(function () {
        caption.textContent = item.text;
      }, item.t);
      captionTimerIds.push(id);
    });
  }

  var prefersReducedMotion =
    typeof window.matchMedia === "function" &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function play() {
    if (!stage) return;
    stage.classList.remove("playing");
    if (caption) {
      caption.textContent = prefersReducedMotion
        ? "CAUGHT IN 4K (static)"
        : "Here we go…";
    }
    clearCaptionTimers();
    void stage.offsetWidth;
    stage.classList.add("playing");
    if (!prefersReducedMotion) {
      scheduleCaptions();
    }
  }

  if (replayBtn && stage) {
    replayBtn.addEventListener("click", play);
  }

  if (stage) {
    play();
  }
})();
