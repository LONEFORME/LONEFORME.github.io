---
layout: default
title: 热点新闻
---

# 📰 热点新闻速览

> AI 精选 · 来源可溯 · 每日更新

---

<div class="news-tabs">
  <input type="radio" name="news-tab" id="tab-all" checked>
  <input type="radio" name="news-tab" id="tab-shizheng">
  <input type="radio" name="news-tab" id="tab-keji">
  <input type="radio" name="news-tab" id="tab-caijing">
  <input type="radio" name="news-tab" id="tab-guoji">
  <input type="radio" name="news-tab" id="tab-shehui">
  <div class="tab-bar" id="newsTabBar">
    <label for="tab-all" class="tab-label">📋 全部 <span class="tab-count">20</span></label>
    <label for="tab-shizheng" class="tab-label">🏛️ 时政 <span class="tab-count">4</span></label>
    <label for="tab-keji" class="tab-label">🤖 科技 AI <span class="tab-count">4</span></label>
    <label for="tab-caijing" class="tab-label">💰 财经 <span class="tab-count">3</span></label>
    <label for="tab-guoji" class="tab-label">🌍 国际 <span class="tab-count">4</span></label>
    <label for="tab-shehui" class="tab-label">🔬 社会·科学 <span class="tab-count">5</span></label>
  </div>

  <div class="tab-nav">
    <button class="tab-nav-btn tab-prev" onclick="switchTab(-1)" title="上一个分类" aria-label="Previous">‹</button>
    <div class="tab-nav-indicator" id="tabIndicator">全部</div>
    <button class="tab-nav-btn tab-next" onclick="switchTab(1)" title="下一个分类" aria-label="Next">›</button>
  </div>

  <div class="news-summary-line">🕐 更新于 2026-07-05 · 共 20 条新闻 · 点击标签或 ← → 键切换</div>

  <div class="tab-panel" id="panel-all">
<div class="news-card">
  <div class="news-date-badge">2026-07-05</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-05</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-05</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-05</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-04</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-04</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-04</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-05</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-03</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-03</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-03</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-03</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-03</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-05</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-03</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-05</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-04</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-04</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-03</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-05</div>
  </div>

  <div class="tab-panel" id="panel-shizheng">
<div class="news-card">
  <div class="news-date-badge">2026-07-05</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-05</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-05</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-05</div>
  </div>

  <div class="tab-panel" id="panel-keji">
<div class="news-card">
  <div class="news-date-badge">2026-07-04</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-04</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-04</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-05</div>
  </div>

  <div class="tab-panel" id="panel-caijing">
<div class="news-card">
  <div class="news-date-badge">2026-07-03</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-03</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-03</div>
  </div>

  <div class="tab-panel" id="panel-guoji">
<div class="news-card">
  <div class="news-date-badge">2026-07-03</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-03</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-05</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-03</div>
  </div>

  <div class="tab-panel" id="panel-shehui">
<div class="news-card">
  <div class="news-date-badge">2026-07-05</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-04</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-04</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-03</div>
<div class="news-card">
  <div class="news-date-badge">2026-07-05</div>
  </div>

</div>

<script>
(function() {
  const tabIds = ["all", "shizheng", "keji", "caijing", "guoji", "shehui"];
  let currentIdx = 0;

  window.switchTab = function(dir) {
    currentIdx = (currentIdx + dir + tabIds.length) % tabIds.length;
    const id = tabIds[currentIdx];
    const radio = document.getElementById("tab-" + id);
    if (radio) {
      radio.checked = true;
      radio.dispatchEvent(new Event("change", { bubbles: true }));
    }
    updateIndicator();
    scrollTabIntoView(id);
  };

  function updateIndicator() {
    const id = tabIds[currentIdx];
    const indicator = document.getElementById("tabIndicator");
    const label = document.querySelector("label[for='tab-" + id + "']");
    if (label && indicator) {
      let text = label.textContent.trim();
      // Remove trailing number count
      text = text.replace(/\s*\d+\s*$/, "").trim();
      indicator.textContent = text;
    }
  }

  function scrollTabIntoView(id) {
    const label = document.querySelector("label[for='tab-" + id + "']");
    if (label) {
      label.scrollIntoView({ behavior: "smooth", block: "nearest", inline: "center" });
    }
  }

  // Click on tab labels updates indicator
  document.querySelectorAll(".tab-label").forEach(function(label) {
    label.addEventListener("click", function() {
      const forId = this.getAttribute("for").replace("tab-", "");
      currentIdx = tabIds.indexOf(forId);
      if (currentIdx === -1) currentIdx = 0;
      updateIndicator();
    });
  });

  // Keyboard navigation
  document.addEventListener("keydown", function(e) {
    if (e.key === "ArrowLeft") { switchTab(-1); e.preventDefault(); }
    if (e.key === "ArrowRight") { switchTab(1); e.preventDefault(); }
  });

  updateIndicator();
})();
</script>


---

<p class="news-updated">🕐 更新于 2026-07-05</p>
