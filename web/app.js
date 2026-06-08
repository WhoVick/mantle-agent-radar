(function () {
  const data = window.SIGNAL_DATA || { signals: [], sources: [] };
  let activeFilter = "all";
  let activeId = data.signals[0] ? data.signals[0].id : null;

  const signalList = document.getElementById("signalList");
  const detail = document.getElementById("signalDetail");
  const metricSignals = document.getElementById("metricSignals");
  const metricConfidence = document.getElementById("metricConfidence");
  const metricSources = document.getElementById("metricSources");
  const copyButton = document.getElementById("copyTopSignal");

  function filteredSignals() {
    if (activeFilter === "all") return data.signals;
    return data.signals.filter((signal) => signal.signal_type === activeFilter);
  }

  function renderMetrics() {
    const signals = filteredSignals();
    const average = signals.length
      ? Math.round(signals.reduce((sum, signal) => sum + signal.confidence, 0) / signals.length)
      : 0;
    metricSignals.textContent = String(signals.length);
    metricConfidence.textContent = `${average}%`;
    metricSources.textContent = String(data.sources.length);
  }

  function truncate(text, limit) {
    if (text.length <= limit) return text;
    return `${text.slice(0, limit - 1)}...`;
  }

  function tagHtml(tags) {
    return tags.slice(0, 5).map((tag) => `<span class="tag">${escapeHtml(tag)}</span>`).join("");
  }

  function renderList() {
    const signals = filteredSignals();
    if (!signals.some((signal) => signal.id === activeId)) {
      activeId = signals[0] ? signals[0].id : null;
    }
    signalList.innerHTML = signals.map((signal) => `
      <button class="signal-item ${signal.id === activeId ? "active" : ""}" data-id="${signal.id}">
        <span class="signal-head">
          <span class="signal-title">${escapeHtml(signal.title)}</span>
          <span class="confidence">${signal.confidence}%</span>
        </span>
        <span class="signal-summary">${escapeHtml(truncate(signal.summary, 170))}</span>
        <span class="tags">${tagHtml(signal.tags)}</span>
      </button>
    `).join("");

    signalList.querySelectorAll(".signal-item").forEach((button) => {
      button.addEventListener("click", () => {
        activeId = button.dataset.id;
        render();
      });
    });
  }

  function renderDetail() {
    const signal = data.signals.find((item) => item.id === activeId);
    if (!signal) {
      detail.innerHTML = `
        <div class="empty-state">
          <h3>No signals</h3>
          <p>Change the filter or rebuild the data set.</p>
        </div>
      `;
      return;
    }

    detail.innerHTML = `
      <div class="detail-grid">
        <span class="type-badge">${escapeHtml(signal.signal_type)}</span>
        <h3>${escapeHtml(signal.title)}</h3>
        <p class="detail-summary">${escapeHtml(signal.summary)}</p>
        <div class="action">${escapeHtml(signal.action)}</div>
        <section>
          <h4>Score rationale</h4>
          <div class="score-bars">
            ${Object.entries(signal.scores).map(([name, value]) => `
              <div class="bar-row">
                <span>${escapeHtml(labelize(name))}</span>
                <span class="bar-track"><span class="bar-fill" style="width:${value}%"></span></span>
                <strong>${value}</strong>
              </div>
            `).join("")}
          </div>
        </section>
        <section>
          <h4>Evidence</h4>
          <div class="evidence">
            ${signal.evidence.map((item) => `
              <a href="${escapeHtml(item.url)}" target="_blank" rel="noreferrer">
                ${escapeHtml(item.source)} / ${escapeHtml(item.type)} / ${escapeHtml(item.observed_at)}
              </a>
            `).join("")}
          </div>
        </section>
        <section>
          <h4>Tags</h4>
          <div class="tags">${tagHtml(signal.tags)}</div>
        </section>
      </div>
    `;
  }

  function labelize(value) {
    return value.replaceAll("_", " ");
  }

  function escapeHtml(value) {
    return String(value)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  function render() {
    renderMetrics();
    renderList();
    renderDetail();
  }

  document.querySelectorAll(".filter").forEach((button) => {
    button.addEventListener("click", () => {
      activeFilter = button.dataset.filter;
      document.querySelectorAll(".filter").forEach((item) => item.classList.remove("active"));
      button.classList.add("active");
      render();
    });
  });

  copyButton.addEventListener("click", async () => {
    const signal = data.signals.find((item) => item.id === activeId) || data.signals[0];
    if (!signal) return;
    const text = `${signal.title}\nConfidence: ${signal.confidence}%\nAction: ${signal.action}`;
    try {
      await navigator.clipboard.writeText(text);
      copyButton.textContent = "Copied";
      setTimeout(() => {
        copyButton.textContent = "Copy";
      }, 1300);
    } catch (error) {
      copyButton.textContent = "Blocked";
      setTimeout(() => {
        copyButton.textContent = "Copy";
      }, 1300);
    }
  });

  render();
})();

