---
layout: default
title: 股票财经
---

<h1>📈 股票与宏观财经看板</h1>
<p class="page-subtitle">全球市场快照 · A 股与港股 K 线 · 宏观财经资讯</p>

{% include market-chart.html %}

<!-- ================= 1. 全球核心指数行情看板 ================= -->
<div class="section-header" style="margin-top: 24px;">
  <h2 style="font-size: 18px; margin: 0; display: flex; align-items: center; gap: 8px;">
    <span>🌍 全球核心股指 & 宏观资产快照</span>
  </h2>
  <span style="font-size: 12px; color: var(--color-muted);">覆盖 15 项市场指标 · 行情按源时间展示，可能存在延迟</span>
</div>

<!-- QUOTES:BEGIN -->
<div class="finance-ticker-grid">
  <div class="ticker-card" data-tcode="sh000001" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇨🇳 上证指数</span>
      <span class="ticker-code">000001.SH</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">3,476.47</span>
      <span class="ticker-change down">▼ -2.03%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="sh000001" aria-label="查看上证指数 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>上海证券市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-25 15:35:57（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="sz399001" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇨🇳 深证成指</span>
      <span class="ticker-code">399001.SZ</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">10,086.35</span>
      <span class="ticker-change down">▼ -3.24%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="sz399001" aria-label="查看深证成指 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>深圳证券市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-25 15:00:03（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="sz399006" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇨🇳 创业板指</span>
      <span class="ticker-code">399006.SZ</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">2,183.58</span>
      <span class="ticker-change down">▼ -4.19%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="sz399006" aria-label="查看创业板指 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>创业板市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-25 15:00:03（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="sh000688" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇨🇳 科创50</span>
      <span class="ticker-code">000688.SH</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">1,186.14</span>
      <span class="ticker-change down">▼ -5.12%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="sh000688" aria-label="查看科创50 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>科创板核心指数</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-25 15:35:39（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="hkHSTECH" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇭🇰 恒生科技</span>
      <span class="ticker-code">HSTECH</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">3,378.26</span>
      <span class="ticker-change down">▼ -2.56%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="hkHSTECH" aria-label="查看恒生科技 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>香港科技股指数</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 · 源时间未提供</div>
  </div>
  <div class="ticker-card" data-tcode="usNDX" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇺🇸 纳斯达克100</span>
      <span class="ticker-code">NDX</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">26,214.17</span>
      <span class="ticker-change down">▼ -1.99%</span>
    </div>
    <div class="ticker-footer">
      <span>纳斯达克市场</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 2026-11-25 09:18:36（非实时）</div>
  </div>
  <div class="ticker-card">
    <div class="ticker-header">
      <span class="ticker-name">💱 美元/离岸人民币</span>
      <span class="ticker-code">USD/CNH</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-up">6.6768</span>
      <span class="ticker-change up">▲ +0 bp</span>
    </div>
    <div class="ticker-footer">
      <span>美元兑离岸人民币</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 18:38:56（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="hf_XAU" data-fmt="usd" data-unit="/盎司">
    <div class="ticker-header">
      <span class="ticker-name">🪙 伦敦现货黄金</span>
      <span class="ticker-code">XAU/USD</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">$3,531.36 <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/盎司</span></span>
      <span class="ticker-change down">▼ -24.47 (-0.69%)</span>
    </div>
    <div class="ticker-footer">
      <span>美元 / 金衡盎司</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 18:38:00（非实时）</div>
  </div>
  <div class="ticker-card">
    <div class="ticker-header">
      <span class="ticker-name">🪙 国内现货黄金</span>
      <span class="ticker-code">Au(T+D)</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">¥756.80 <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/克</span></span>
      <span class="ticker-change down">▼ -20.41 (-2.63%)</span>
    </div>
    <div class="ticker-footer">
      <span>上海黄金交易所基准</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 15:30:01（非实时）</div>
  </div>
  <div class="ticker-card" data-tcode="hkHSI" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇭🇰 恒生指数</span>
      <span class="ticker-code">HSI</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">21,966.01</span>
      <span class="ticker-change down">▼ -1.14%</span>
    </div>
    <button type="button" class="ticker-select" data-symbol="hkHSI" aria-label="查看恒生指数 K 线" aria-pressed="false">查看 K 线 →</button>
    <div class="ticker-footer">
      <span>港股基准大盘</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 · 源时间未提供</div>
  </div>
  <div class="ticker-card" data-tcode="usDJI" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇺🇸 道琼斯工业指数</span>
      <span class="ticker-code">DJIA</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-up">46,247.29</span>
      <span class="ticker-change up">▲ +0.65%</span>
    </div>
    <div class="ticker-footer">
      <span>美股蓝筹风向标</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 · 源时间未提供</div>
  </div>
  <div class="ticker-card" data-tcode="ukUKX" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇬🇧 富时100</span>
      <span class="ticker-code">FTSE</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-up">9,284.83</span>
      <span class="ticker-change up">▲ +0.77%</span>
    </div>
    <div class="ticker-footer">
      <span>欧洲市场开盘参照</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 · 源时间未提供</div>
  </div>
  <div class="ticker-card">
    <div class="ticker-header">
      <span class="ticker-name">🇯🇵 日经225</span>
      <span class="ticker-code">N225</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">44,946.64</span>
      <span class="ticker-change down">▼ -0.90%</span>
    </div>
    <div class="ticker-footer">
      <span>亚太早盘情绪指标</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 · 源时间未提供</div>
  </div>
  <div class="ticker-card" data-tcode="usINX" data-fmt="idx" data-unit="">
    <div class="ticker-header">
      <span class="ticker-name">🇺🇸 标普500</span>
      <span class="ticker-code">SPX</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-up">6,643.70</span>
      <span class="ticker-change up">▲ +0.59%</span>
    </div>
    <div class="ticker-footer">
      <span>美股大盘核心基准</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 · 源时间未提供</div>
  </div>
  <div class="ticker-card" data-tcode="hf_OIL" data-fmt="usd" data-unit="/桶">
    <div class="ticker-header">
      <span class="ticker-name">🛢️ 布伦特原油</span>
      <span class="ticker-code">OIL/USD</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price ticker-down">$88.03 <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/桶</span></span>
      <span class="ticker-change down">▼ -0.75 (-0.85%)</span>
    </div>
    <div class="ticker-footer">
      <span>美元 / 桶</span>
    </div>
    <div class="ticker-quote-time">🕒 快照 18:39:06（非实时）</div>
  </div>
</div>



<style>
.ticker-card[data-live="1"] .ticker-quote-time { color: #00b86b; }
</style>
<script>
(function () {
  var cards = Array.prototype.slice.call(document.querySelectorAll('.ticker-card[data-tcode]'));
  if (!cards.length) return;
  var REFRESH_MS = 60000;
  var API = 'https://qt.gtimg.cn/q=';

  function pad(n) { return n < 10 ? '0' + n : '' + n; }
  function comma(v, d) {
    var s = v.toFixed(d), p = s.split('.');
    p[0] = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    return p.join('.');
  }
  function unitSpan(unit) {
    return unit ? ' <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">' + unit + '</span>' : '';
  }

  // 指数格式：1~名称~代码~现价~昨收~今开~...~YYYYMMDDHHMMSS~
  function parseIdx(raw) {
    var f = raw.split('~');
    if (f.length < 6) return null;
    var price = parseFloat(f[3]), prev = parseFloat(f[4]);
    if (!isFinite(price)) return null;
    // Field 30 is the timestamp. Other numeric fields can resemble a date.
    var t = f[30] || '';
    if (!/^20\d{12}$/.test(t) && !/^20\d{2}[-/]\d{2}[-/]\d{2} \d{2}:\d{2}:\d{2}$/.test(t)) t = '';
    if (price <= 0 || !isFinite(prev) || prev <= 0) return null;
    return { price: price, pct: (price - prev) / prev * 100, chg: price - prev, time: t };
  }

  // 外盘现货/期货格式：现价,涨跌幅%,买,卖,最高,最低,HH:MM:SS,昨收,今开,...
  function parseHf(raw) {
    var f = raw.split(',');
    if (f.length < 8) return null;
    var price = parseFloat(f[0]), pct = parseFloat(f[1]), prev = parseFloat(f[7]);
    if (!isFinite(price) || price <= 0) return null;
    return { price: price, pct: isFinite(pct) ? pct : 0, chg: isFinite(prev) ? price - prev : 0, time: f[6] || '' };
  }

  function paint(card, q) {
    var up = q.pct >= 0;
    var fmt = card.getAttribute('data-fmt') || 'idx';
    var unit = card.getAttribute('data-unit') || '';
    var priceHTML, chgText;

    if (fmt === 'fx') {
      priceHTML = q.price.toFixed(4);
      chgText = (q.chg >= 0 ? '+' : '') + Math.round(q.chg * 10000) + ' bp';
    } else if (fmt === 'usd' || fmt === 'cny') {
      priceHTML = (fmt === 'usd' ? '$' : '¥') + comma(q.price, 2) + unitSpan(unit);
      chgText = (q.chg >= 0 ? '+' : '') + q.chg.toFixed(2) + ' (' + (up ? '+' : '') + q.pct.toFixed(2) + '%)';
    } else {
      priceHTML = comma(q.price, 2);
      chgText = (up ? '+' : '') + q.pct.toFixed(2) + '%';
    }

    var pEl = card.querySelector('.ticker-price');
    var cEl = card.querySelector('.ticker-change');
    var tEl = card.querySelector('.ticker-quote-time');
    if (pEl) { pEl.innerHTML = priceHTML; pEl.className = 'ticker-price ' + (up ? 'ticker-up' : 'ticker-down'); }
    if (cEl) { cEl.innerHTML = (up ? '\u25b2 ' : '\u25bc ') + chgText; cEl.className = 'ticker-change ' + (up ? 'up' : 'down'); }
    if (tEl) {
      var hhmmss = '';
      if (/^20\d{12}$/.test(q.time)) {
        hhmmss = q.time.slice(0, 4) + '-' + q.time.slice(4, 6) + '-' + q.time.slice(6, 8) + ' '
               + q.time.slice(8, 10) + ':' + q.time.slice(10, 12) + ':' + q.time.slice(12, 14);
      } else if (q.time) {
        hhmmss = q.time;
      }
      if (hhmmss) {
        // 数据源时间按北京时间换算，超过 3 分钟就说明已收盘或延迟
        var stale = true;
        if (/^20\d{12}$/.test(q.time)) {
          var t = Date.UTC(+q.time.slice(0, 4), +q.time.slice(4, 6) - 1, +q.time.slice(6, 8),
                           +q.time.slice(8, 10) - 8, +q.time.slice(10, 12), +q.time.slice(12, 14)) / 1000;
          stale = (Date.now() / 1000 - t) > 180;
        } else if (/^\d{2}:\d{2}:\d{2}$/.test(q.time)) {
          // 外盘只给 HH:MM:SS，按北京时间拼今天再比较
          var n = new Date(Date.now() + (new Date().getTimezoneOffset() + 480) * 60000);
          var hh = +q.time.slice(0, 2), mi = +q.time.slice(3, 5), se = +q.time.slice(6, 8);
          var t2 = Date.UTC(n.getUTCFullYear(), n.getUTCMonth(), n.getUTCDate(), hh - 8, mi, se) / 1000;
          stale = Math.abs(Date.now() / 1000 - t2) > 600;
        }
        tEl.textContent = '\ud83d\udd52 行情时间 ' + hhmmss
          + (/^20\d{12}$/.test(q.time) ? (stale ? '（延迟/已收盘）' : '') : '（源时区）');
      } else {
        tEl.textContent = '\ud83d\udd52 已获取行情，源时间未知';
      }
    }
    card.setAttribute('data-live', q.time && !stale ? '1' : '0');
  }

  function apply() {
    cards.forEach(function (c) {
      var code = c.getAttribute('data-tcode');
      var raw = window['v_' + code];
      if (!raw) return;
      var q = code.indexOf('hf_') === 0 ? parseHf(raw) : parseIdx(raw);
      if (q) paint(c, q);
    });
  }

  function refresh() {
    if (document.visibilityState === 'hidden') return;
    var el = document.createElement('script');
    el.charset = 'gbk';
    el.src = API + cards.map(function (c) { return c.getAttribute('data-tcode'); }).join(',')
           + '&_=' + Date.now();
    el.onload = function () { apply(); el.remove(); };
    el.onerror = function () { el.remove(); };
    document.head.appendChild(el);
  }

  refresh();
  setInterval(refresh, REFRESH_MS);
  document.addEventListener('visibilitychange', function () {
    if (document.visibilityState === 'visible') refresh();
  });
})();
</script>

<!-- QUOTES:END -->

<!-- ================= 2. 热门核心赛道与主力资金流向 ================= -->
<div class="section-header" style="margin-top: 32px;">
  <h2 style="font-size: 18px; margin: 0; display: flex; align-items: center; gap: 8px;">
    <span>产业主题观察</span>
  </h2>
  <span style="font-size: 12px; color: var(--color-muted);">关注领域</span>
</div>

<div class="finance-sector-grid">
  <div class="sector-card">
    <div class="sector-title-row">
      <span class="sector-title">🤖 人工智能 & 先进算力链</span>
    </div>
    <p class="sector-desc">产业主题观察</p>
    <div class="sector-tags">
      <span class="sector-tag-chip">CPO 光模块</span>
      <span class="sector-tag-chip">GPU 服务器</span>
      <span class="sector-tag-chip">先进制程封装</span>
      <span class="sector-tag-chip">PCB 算力板</span>
    </div>
  </div>
  <div class="sector-card">
    <div class="sector-title-row">
      <span class="sector-title">⚡ 新能源出海 & 特高压电网</span>
    </div>
    <p class="sector-desc">产业主题观察</p>
    <div class="sector-tags">
      <span class="sector-tag-chip">特高压直流</span>
      <span class="sector-tag-chip">固态锂电</span>
      <span class="sector-tag-chip">工商业储能</span>
      <span class="sector-tag-chip">核电核岛</span>
    </div>
  </div>
  <div class="sector-card">
    <div class="sector-title-row">
      <span class="sector-title">🚗 具身智能 & 智能网联车</span>
    </div>
    <p class="sector-desc">产业主题观察</p>
    <div class="sector-tags">
      <span class="sector-tag-chip">端到端智驾</span>
      <span class="sector-tag-chip">激光雷达</span>
      <span class="sector-tag-chip">行星滚柱丝杠</span>
      <span class="sector-tag-chip">六维力传感器</span>
    </div>
  </div>
  <div class="sector-card">
    <div class="sector-title-row">
      <span class="sector-title">🛡️ 高股息红利与底仓资产</span>
    </div>
    <p class="sector-desc">产业主题观察</p>
    <div class="sector-tags">
      <span class="sector-tag-chip">国有大行</span>
      <span class="sector-tag-chip">水电公用</span>
      <span class="sector-tag-chip">高股息煤炭</span>
      <span class="sector-tag-chip">中字头基建</span>
    </div>
  </div>
</div>


<!-- ================= 3. 每日财经资讯 ================= -->
<div class="section-header" style="margin-top: 36px;">
  <h2 style="font-size: 18px; margin: 0; display: flex; align-items: center; gap: 8px;">
    <span>📰 每日宏观财经 & 资本市场资讯聚合</span>
  </h2>
  <span style="font-size: 12px; color: var(--color-muted);">宏观经济与资本市场</span>
</div>

<div class="news-grid">
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">💰</span>
      <span class="news-category-title">宏观经济 · 汇率 · 证券 · 产业深度</span>
      <span class="news-category-count">11 条精选资讯</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-25/10737671.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新网广西柳州11月25日电(韦新娜)眼下，在广西柳州市柳江区进德镇龙新村，一场椒香与果香交织的甜蜜邂逅在田间上演，架上收葡萄、架下摘彩椒，让一亩田地收获两份收益，为乡村产业增收开辟新路径。" data-title="（乡村行·看振兴）广西柳江“一棚双收”：葡萄架下彩椒香 立体套种助增收" data-date="11-25 18:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-25 18:15</span>
          <span class="news-item-title">（乡村行·看振兴）广西柳江“一棚双收”：葡萄架下彩椒香 立体套种助增收</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/032/379.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 25 日消息，在昨天下午的 HUAWEI Mate X8 及全场景新品发布会上，华为 Mate X8 大折旗舰机正式发布。华为官方还为这款新机推出了云晰柔光膜，用户在华为授权服务中心可购买更换。关于为何不标配“云晰柔光膜”，华为常务董事、产品投资评审委员会主任、终端 BG 董事长余承东也给出了解释：大多数人不太喜欢这种柔光膜，因为它（IT之家注：此处预计指 Mate X8）不像平板和 PC，尺寸大、人离得远。手机拿得离人近，柔光这一块牺牲一定的（少量）分辨率，有些人不是很接受，因此我们（华为）没有把它做成标配，只让大家可选。根据规划，云晰柔光膜预计 2027 年 1 月下旬正式上线，支持 HUAWEI Mate X8、Pura X Max（内屏贴膜）。上线后，用户可以前往" data-title="华为余承东解释为何 Mate X8 不标配“云晰柔光膜”：大多数人不喜欢，会少量牺牲分辨率" data-date="11-25 18:02" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-25 18:02</span>
          <span class="news-item-title">华为余承东解释为何 Mate X8 不标配“云晰柔光膜”：大多数人不喜欢，会少量牺牲分辨率</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-25/10737512.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新社悉尼11月25日电 (记者 薄雯雯)澳大利亚统计局25日公布的数据显示，该国10月消费者价格指数(CPI)同比上涨4.9%，高于9月的4.3%，并超出市场预期。" data-title="澳大利亚10月CPI同比上涨4.9%" data-date="11-25 16:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-25 16:44</span>
          <span class="news-item-title">澳大利亚10月CPI同比上涨4.9%</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/512532.html" target="_blank" rel="noopener" data-cat="caijing" data-summary="第二十一届中国IDC产业年度大典（IDCC2026）暨2026全球数字基础设施科技展即将举办" data-title="完整议程！第二十一届中国IDC产业年度大典（IDCC2026）" data-date="11-25 16:18" data-source="量子位">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-25 16:18</span>
          <span class="news-item-title">完整议程！第二十一届中国IDC产业年度大典（IDCC2026）</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1041820/huawei-guilty-trade-secrets-trial" target="_blank" rel="noopener" data-cat="caijing" data-summary="正如NBC新闻和彭博社此前报道的那样，陪审团已裁定华为犯有窃取美国商业秘密的罪行。该判决在纽约的一家联邦法院作出，结束了长达数年的法律诉讼，该诉讼指控这家中国电信巨头窃取商业机密。" data-title="Huawei found guilty of stealing trade secrets" data-date="11-25 06:23" data-source="The Verge">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-25 06:23</span>
          <span class="news-item-title">Huawei found guilty of stealing trade secrets</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-25/10737277.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="中新社莫斯科11月24日电 俄罗斯总统普京24日主持召开能源发展战略和环境安全委员会会议时表示，针对乌克兰对俄能源基础设施的袭击，俄方必然作出回应。" data-title="普京：乌方袭击俄能源设施必招致俄方回应" data-date="11-25 06:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-25 06:17</span>
          <span class="news-item-title">普京：乌方袭击俄能源设施必招致俄方回应</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/031/901.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 25 日消息，惠普今日发布 2026 财年（2025 年 11 月 1 日～2026 年 10 月 31 日）全年及第四财季（2026 年 8 月 1 日～2026 年 10 月 31 日）报告：2026 财年全年营业总收入：605.27 亿美元（IT之家注：现汇率约合 4042.78 亿元人民币），同比增长 9.5%毛利润：115.96 亿美元（现汇率约合 774.53 亿元人民币）毛利率：19.16%归母净利润：24.25 亿美元（现汇率约合 161.97 亿元人民币），同比下降 4.1%经营现金流：39.76 亿美元（现汇率约合 265.57 亿元人民币），同比增长 7.5%自由现金流：33.3 亿美元（现汇率约合 222.42 亿元人民币），同比增长 13.5%基" data-title="惠普 2026 财年全年归母净利润 24.25 亿美元，同比下降 4.1%" data-date="11-25 05:23" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-25 05:23</span>
          <span class="news-item-title">惠普 2026 财年全年归母净利润 24.25 亿美元，同比下降 4.1%</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/031/900.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 25 日消息，戴尔今日发布 2027 财年（2026 年 1 月 31 日～2027 年 1 月 29 日）前三季度（2026 年 2 月 1 日～2026 年 10 月 30 日）及第三财季（2026 年 8 月 1 日～2026 年 10 月 30 日）报告：2027 财年前三季度营业总收入：1457.5 亿美元，同比增长 82%毛利润：291.71 亿美元，同比增长 83%毛利率：20%，同比增长 0.1 个百分点归母净利润：132.44 亿美元，同比增长 260%经营现金流：107.65 亿美元，同比增长 65%自由现金流：75.78 亿美元，同比增长 65%基本每股收益：20.6 美元，同比增长 281%稀释每股收益：20.38 美元，同比增长 282%资产负债" data-title="戴尔 2027 财年前三季度归母净利润 132.44 亿美元，同比增长 260%" data-date="11-25 05:13" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-25 05:13</span>
          <span class="news-item-title">戴尔 2027 财年前三季度归母净利润 132.44 亿美元，同比增长 260%</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/031/895.htm" target="_blank" rel="noopener" data-cat="caijing" data-summary="IT之家 11 月 25 日消息，在昨天下午的 HUAWEI Mate X8 及全场景新品发布会上，华为 Mate X8 大折旗舰机正式发布，全系搭载麒麟 9050 Pro 处理器，售价 12,999 元起。此次华为 Mate X8 在屏幕上又有新技术突破。其中，大家最关心的就是折痕水平。根据此前曝光的视频来看，Mate X8 内屏在采用“亮面”设计的情况下，折痕多角度查看处于几乎不可见的状态。而据华为官方数据，Mate X8 内屏平整度对比前代 X7 提升了 90%。华为常务董事、产品投资评审委员会主任、终端 BG 董事长余承东也在发布会现场揭秘了新机“超平整”内屏的实现原理，总结为四个字 ——“削峰填谷”。余承东表示，传统折叠屏幕，在开合使用时会产生凹凸形变。而华为 Mate X8 首创" data-title="削峰填谷！余承东揭秘华为 Mate X8“超平整”内屏原理，首创磁控展平技术定向修复" data-date="11-25 00:47" data-source="IT之家">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-25 00:47</span>
          <span class="news-item-title">削峰填谷！余承东揭秘华为 Mate X8“超平整”内屏原理，首创磁控展平技术定向修复</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/crp3eqg9l8eeo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="caijing" data-summary="黄仁勋在美国总统特朗普介入下重掌辉达，台湾股民在台股涨停板的气氛大喊“爸爸回来了”。但“台湾干爹”会再一次变成黑天鹅吗？" data-title="“不能没有你”：黄仁勋回归，台湾股市的狂欢与半导体“ 黑天鹅”风险" data-date="11-24 22:35" data-source="BBC">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-24 22:35</span>
          <span class="news-item-title">“不能没有你”：黄仁勋回归，台湾股市的狂欢与半导体“ 黑天鹅”风险</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-24/10737227.shtml" target="_blank" rel="noopener" data-cat="caijing" data-summary="11月的深圳，绿意盎然，鲜花盛放。一架架航班降落在深圳宝安国际机场，亚太经济体的领导人、代表共赴“深圳之约”，参加亚太经合组织(APEC)第三十三次领导人非正式会议。" data-title="聚焦APEC·记者手记｜亚太合作的“深圳印记”" data-date="11-24 21:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 21:11</span>
          <span class="news-item-title">聚焦APEC·记者手记｜亚太合作的“深圳印记”</span>
        </a>
  </div>
</div>


<div style="text-align: center; margin: 36px 0 20px;">
  <a href="{{ "/news" | relative_url }}" class="card-link" style="display: inline-flex; align-items: center; gap: 6px; padding: 10px 24px; font-size: 14px;">
    <span>📰 返回综合热点新闻专区</span>
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
  </a>
</div>

---

<p class="news-updated">🕐 页面生成于 2026-11-25 18:36（北京时间）· 行情每 60 秒尝试刷新，失败时保留页面快照 · K 线按数据源交易周期展示，最新一根可能尚未收盘 · 仅供参考</p>
