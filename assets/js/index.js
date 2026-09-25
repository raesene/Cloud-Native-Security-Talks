// Filters the talk index by search text, series, year and event.
// State lives in the query string (?q=&series=&year=&event=) so filtered views can be linked.
(function () {
  const q = document.getElementById("q");
  const year = document.getElementById("year");
  const seriesButtons = [...document.querySelectorAll("#series button")];
  const groups = [...document.querySelectorAll(".event-group")];
  const rows = [...document.querySelectorAll(".talk-row")];
  const count = document.getElementById("count");
  const empty = document.getElementById("empty");
  const activeEvent = document.getElementById("active-event");
  const activeEventName = document.getElementById("active-event-name");
  const total = rows.length;

  const state = { q: "", series: "", year: "", event: "" };
  let abstracts = null;
  let loading = null;

  function loadAbstracts() {
    if (!loading) {
      loading = fetch(document.documentElement.dataset.searchUrl || "/search.json")
        .then((r) => r.json())
        .then((data) => { abstracts = data; })
        .catch(() => { abstracts = {}; });
    }
    return loading;
  }

  function matches(row, terms) {
    if (!terms.length) return true;
    const href = row.querySelector("a").getAttribute("href");
    const hay = row.dataset.text + " " + (abstracts ? abstracts[href] || "" : "");
    return terms.every((t) => hay.includes(t));
  }

  function setCount(n) {
    const text = String(n);
    const flap = count.closest(".flap");
    const cells = [...count.children];
    while (cells.length < text.length) {
      const c = document.createElement("span");
      c.className = "flap-cell";
      c.setAttribute("aria-hidden", "true");
      count.appendChild(c);
      cells.push(c);
    }
    cells.forEach((c, i) => {
      const ch = text[i];
      c.hidden = ch === undefined;
      if (ch !== undefined && c.textContent !== ch) {
        c.textContent = ch;
        c.classList.remove("is-turning");
        void c.offsetWidth;
        c.classList.add("is-turning");
      }
    });
    count.setAttribute("aria-label", text + " talks");
    flap.classList.toggle("flap--transit", n !== total);
  }

  function apply() {
    const terms = state.q.toLowerCase().split(/\s+/).filter(Boolean);
    let shown = 0;
    groups.forEach((g) => {
      const groupOk =
        (!state.series || g.dataset.series === state.series) &&
        (!state.year || g.dataset.year === state.year) &&
        (!state.event || g.dataset.event === state.event);
      let n = 0;
      g.querySelectorAll(".talk-row").forEach((row) => {
        const ok = groupOk && matches(row, terms);
        row.hidden = !ok;
        if (ok) n++;
      });
      g.hidden = n === 0;
      g.querySelector(".js-shown").textContent = n;
      shown += n;
    });
    setCount(shown);
    empty.hidden = shown !== 0;

    seriesButtons.forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.series === state.series)));
    if (state.event) {
      const g = groups.find((x) => x.dataset.event === state.event);
      activeEventName.textContent = g ? g.querySelector(".event-name").textContent : state.event.toUpperCase();
    }
    activeEvent.hidden = !state.event;
  }

  function writeUrl() {
    const params = new URLSearchParams();
    Object.entries(state).forEach(([k, v]) => { if (v) params.set(k, v); });
    const qs = params.toString();
    history.replaceState(null, "", location.pathname + (qs ? "?" + qs : "") + location.hash);
  }

  function update() {
    apply();
    writeUrl();
  }

  function readUrl() {
    const params = new URLSearchParams(location.search);
    Object.keys(state).forEach((k) => { state[k] = params.get(k) || ""; });
    q.value = state.q;
    year.value = state.year;
  }

  let timer;
  q.addEventListener("input", () => {
    state.q = q.value.trim();
    clearTimeout(timer);
    timer = setTimeout(() => {
      if (state.q && !abstracts) loadAbstracts().then(update);
      update();
    }, 120);
  });
  year.addEventListener("change", () => { state.year = year.value; update(); });
  seriesButtons.forEach((b) => b.addEventListener("click", () => {
    state.series = b.dataset.series;
    state.event = "";
    update();
  }));
  document.getElementById("clear-event").addEventListener("click", () => { state.event = ""; update(); });

  readUrl();
  if (state.q) loadAbstracts().then(apply);
  apply();
})();
