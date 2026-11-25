---
layout: default
title: 热点新闻
---

<div class="news-header-box">
  <div class="news-title-row">
    <div>
      <h1 class="news-main-title">📰 热点新闻速览</h1>
      <p class="news-main-desc">时政国际、AI 与芯片、足球及综合资讯</p>
    </div>
    <div class="news-date-tag">
      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
      <span>2026-11-26 02:05 抓取更新</span>
    </div>
  </div>
  <div class="news-search-bar">
    <svg class="news-search-icon" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
    <input type="search" id="news-search-input" class="news-search-input" aria-label="搜索新闻" placeholder="搜索标题、摘要、人物或信源" oninput="onNewsSearch(this.value)">
    <span id="news-search-count" class="news-search-count"></span>
  </div>
  <div class="news-nav-composite">
    <div class="news-channel-bar">
      <button class="channel-btn active" onclick="filterNewsChannel('all', this)">
        <span>🌟 全部动态</span>
        <span class="channel-count">54</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('shizheng', this)">
        <span>🏛️ 时政与国际</span>
        <span class="channel-count">14</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('keji', this)">
        <span>🤖 AI模型 & 芯片算力</span>
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('zuqiu', this)">
        <span>⚽ 英超与足球风云</span>
        <span class="channel-count">10</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('zonghe', this)">
        <span>📰 综合与社会</span>
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('source', this)">
        <span>🌐 媒体信源</span>
      </button>
    </div>
    <a href="{{ "/archive" | relative_url }}" class="archive-btn-compact" title="翻阅往期历史档案">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
      <span>往期归档</span>
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
    </a>
  </div>
</div>
<div class="news-overview-bar">
  <div class="ov-item"><span class="ov-num">54</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">4</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×13 · 天空体育×13</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">按来源聚合 · 最近 24 小时精选</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.nytimes.com/2026/11/25/us/politics/van-hollen-schumer-israel-senate.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="参议员克里斯·范·霍伦表示，他取代参议员查克·舒默担任党魁的举动与以色列无关，但他对犹太国家的尖锐批评立场已成为这场竞选中的主要分歧点。" data-title="Van Hollen’s Challenge to Schumer Highlights Democratic Rift on Israel" data-date="11-26 00:41" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 11-26 00:41</span>
      </div>
      <h2 class="hero-featured-title">范·霍伦对舒默的挑战凸显了民主党内部在以色列问题上的分歧</h2>
      <div class="hero-featured-title-en">Van Hollen’s Challenge to Schumer Highlights Democratic Rift on Israel</div>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.theverge.com/science/1042278/spacex-fcc-starmind-ai-space-data-centers" target="_blank" rel="noopener" data-cat="keji" data-summary="美国联邦通信委员会（FCC）周三发布公告称，已授权SpaceX部署多达100万颗配备人工智能芯片的卫星，这是埃隆·马斯克旗下公司“Starmind”计划的一部分。还有几家公司也在致力于将人工智能数据中心" data-title="FCC signs off on SpaceX’s plan to put up to 1 million data center satellites into space" data-date="11-26 01:44" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">FCC批准了SpaceX将多达100万颗数据中心卫星送入太空的计划</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/cw20xr4d7x55o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="诺丁汉森林队主教练奥利弗·格拉斯纳（Oliver Glasner）质疑，为什么他的球队中有些人来英国多年后仍不会说英语。" data-title="Glasner criticises Forest players yet to learn English" data-date="11-26 02:00" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">格拉斯纳批评诺丁汉森林球员尚未学会英语</p>
    </a>
    <a class="hero-sub-card" href="https://www.tomshardware.com/pc-components/microsd-cards/best-nintendo-switch-2-microsd-express-card-deals-2026" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在本次黑色星期五促销活动期间，抢购一张适用于任天堂Switch 2的全新microSD Express卡。我们会不断更新此列表，提供所有大型零售商的最佳优惠。" data-title="Best Black Friday Nintendo Switch 2 microSD Express card deals 2026" data-date="11-26 02:01" data-source="Tom's Hardware">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
      </div>
      <p class="hero-sub-title">2026年黑色星期五Nintendo Switch 2 microSD Express卡超值优惠</p>
    </a>
  </div>
</div>
<div class="news-grid">
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🏛️</span>
      <span class="news-category-title">时政要闻 & 国际动态</span>
      <span class="news-category-count">14 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/11/25/us/politics/van-hollen-schumer-israel-senate.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="参议员克里斯·范·霍伦表示，他取代参议员查克·舒默担任党魁的举动与以色列无关，但他对犹太国家的尖锐批评立场已成为这场竞选中的主要分歧点。" data-title="Van Hollen’s Challenge to Schumer Highlights Democratic Rift on Israel" data-date="11-26 00:41" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-26 00:41</span>
          <span class="news-item-title">范·霍伦对舒默的挑战凸显了民主党内部在以色列问题上的分歧</span>
          <span class="news-item-title-en">Van Hollen’s Challenge to Schumer Highlights Democratic Rift on Israel</span>
          <span class="news-value-point">💡 参议员克里斯·范·霍伦表示，他取代参议员查克·舒默担任党魁的举动与以色列无关，但他对犹太国家的尖锐批评立场已成为这场竞选中的主要分歧点</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-26/10737857.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月26日电 (记者 孙自法)作为古人类演化、迁徙和扩散的关键地区之一，中国岭南是否生活过丹尼索瓦人？同期还有无其他古人类共存？这些议题一直因缺乏化石记录悬而未决，也备受关注。" data-title="中国岭南首次发现丹尼索瓦人和10.1万年前未知古人类" data-date="11-26 00:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 00:10</span>
          <span class="news-item-title">中国岭南首次发现丹尼索瓦人和10.1万年前未知古人类</span>
          <span class="news-value-point">💡 中新网北京11月26日电 (记者 孙自法)作为古人类演化、迁徙和扩散的关键地区之一，中国岭南是否生活过丹尼索瓦人</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-25/10737851.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="11月25日，搭载神舟二十四号载人飞船的长征二号F遥二十四运载火箭在酒泉卫星发射中心点火发射，任务取得圆满成功。火箭与朝霞同框画面震撼壮美，中外航天员首次“太空握手”见证历史，一起回顾神舟二十四号载人飞行任务精彩时刻！" data-title="见证历史！神舟二十四号载人飞行任务全记录" data-date="11-25 23:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-25 23:26</span>
          <span class="news-item-title">见证历史！神舟二十四号载人飞行任务全记录</span>
          <span class="news-value-point">💡 11月25日，搭载神舟二十四号载人飞船的长征二号F遥二十四运载火箭在酒泉卫星发射中心点火发射，任务取得圆满成功</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-25/10737839.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网丽水11月25日电(邵燕飞 傅飞扬 蓝倞)初冬时节，晨光洒在浙江丽水莲都万象山公园，今年74岁的青田籍华侨叶海杰缓步行至两株四五米高的山茶花下。他挺直腰板，静静看着枝繁叶茂的山茶花，期待来年春暖花开的美景。" data-title="孙中山先生赠予的山茶花里，藏着百年家国情" data-date="11-25 22:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-25 22:05</span>
          <span class="news-item-title">孙中山先生赠予的山茶花里，藏着百年家国情</span>
          <span class="news-value-point">💡 中新网丽水11月25日电(邵燕飞 傅飞扬 蓝倞)初冬时节，晨光洒在浙江丽水莲都万象山公园，今年74岁的青田籍华侨叶海杰缓步行至两株四五米高的山茶…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-25/10737835.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月25日电 (记者 周昕)中国外交部申办《海洋生物多样性协定》(以下简称《协定》)秘书处特使易先良25日在北京表示，有关国家不应把《协定》政治化，要在相关规则的前提下，友好合作、合理竞争，共同为海洋治理与发展作出贡献。" data-title="中方呼吁申办《海洋生物多样性协定》秘书处相关国家友好合作、合理竞争" data-date="11-25 22:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-25 22:03</span>
          <span class="news-item-title">中方呼吁申办《海洋生物多样性协定》秘书处相关国家友好合作、合理竞争</span>
          <span class="news-value-point">💡 中新社北京11月25日电 (记者 周昕)中国外交部申办《海洋生物多样性协定》(以下简称《协定》)秘书处特使易先良25日在北京表示，有关国家不应把…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-25/10737829.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月25日电 11月25日，中共中央政治局委员、外交部长王毅在北京同荷兰外交大臣贝伦德森举行会谈。" data-title="王毅同荷兰外交大臣贝伦德森会谈" data-date="11-25 21:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-25 21:49</span>
          <span class="news-item-title">王毅同荷兰外交大臣贝伦德森会谈</span>
          <span class="news-value-point">💡 中新社北京11月25日电 11月25日，中共中央政治局委员、外交部长王毅在北京同荷兰外交大臣贝伦德森举行会谈</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-25/10737833.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="2026年11月25日，中共中央政治局委员、外交部长王毅在北京同荷兰外交大臣贝伦德森举行会谈，就中荷关系等共同关心的问题深入交流。" data-title="中荷外长共识声明" data-date="11-25 21:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-25 21:49</span>
          <span class="news-item-title">中荷外长共识声明</span>
          <span class="news-value-point">💡 2026年11月25日，中共中央政治局委员、外交部长王毅在北京同荷兰外交大臣贝伦德森举行会谈，就中荷关系等共同关心的问题深入交流</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-25/10737826.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网广州11月25日电 (记者 方伟彬)广州互联网法院25日发布《关于涉互联网平台协助执行工作指引(试行)》(下称《工作指引》)及典型案例。2021年1月至2026年10月，该院受理执行案件54170件，其中首次执行35715件。针对涉网执行“查人找物难”、财产虚拟化查控难、失信惩戒难落实等突出问题，亟需塑造平台协助执行新格局。" data-title="广州互联网法院发布涉网平台协助执行指引及典型案例" data-date="11-25 21:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-25 21:47</span>
          <span class="news-item-title">广州互联网法院发布涉网平台协助执行指引及典型案例</span>
          <span class="news-value-point">💡 中新网广州11月25日电 (记者 方伟彬)广州互联网法院25日发布《关于涉互联网平台协助执行工作指引(试行)》(下称《工作指引》)及典型案例</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-25/10737824.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="路透社24日报道称，美国众议院民主党人杰米·拉斯金正在调查美国总统特朗普之子小唐纳德·特朗普的商业行为。" data-title="特朗普之子遭调查，民主党议员称其有“神奇预知能力”，特朗普：我为我的孩子们感到难过" data-date="11-25 21:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-25 21:44</span>
          <span class="news-item-title">特朗普之子遭调查，民主党议员称其有“神奇预知能力”，特朗普：我为我的孩子们感到难过</span>
          <span class="news-value-point">💡 路透社24日报道称，美国众议院民主党人杰米·拉斯金正在调查美国总统特朗普之子小唐纳德·特朗普的商业行为</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-25/10737815.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网东京11月25日电 (记者 朱晨曦)据日本共同社25日报道，美军已开始在其位于日本冲绳县的嘉手纳基地部署新型F-15EX战斗机，以替代老旧的F-15战斗机。这是美军首次在海外基地常态部署该型战斗机。" data-title="美军开始在日本冲绳常态部署新型战斗机" data-date="11-25 21:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-25 21:28</span>
          <span class="news-item-title">美军开始在日本冲绳常态部署新型战斗机</span>
          <span class="news-value-point">💡 中新网东京11月25日电 (记者 朱晨曦)据日本共同社25日报道，美军已开始在其位于日本冲绳县的嘉手纳基地部署新型F-15EX战斗机，以替代老旧…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-25/10737789.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月25日电 据美国全国广播公司(NBC)当地时间11月24日援引一名美国官员和一名知情人士的话称，特朗普政府内部就可能在打击行动中将伊朗政权高层领导人列为目标重新展开讨论，以清除“强硬派人物”，从而结束战事。" data-title="美媒：特朗普政府考虑将伊朗高层列为打击目标" data-date="11-25 20:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-25 20:52</span>
          <span class="news-item-title">美媒：特朗普政府考虑将伊朗高层列为打击目标</span>
          <span class="news-value-point">💡 中新网11月25日电 据美国全国广播公司(NBC)当地时间11月24日援引一名美国官员和一名知情人士的话称，特朗普政府内部就可能在打击行动中将伊…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-25/10737661.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网阿斯塔纳11月25日电 (记者 单璐)哈萨克斯坦内务部25日通报，今年前10个月，哈警方打掉40余个涉嫌实施严重或特别严重犯罪的团伙。同期，哈警方就组建、参加有组织犯罪集团的行为立案50起，其中部分案件涉及跨国犯罪集团。" data-title="哈萨克斯坦警方今年前10个月打掉40余个犯罪团伙" data-date="11-25 20:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-25 20:39</span>
          <span class="news-item-title">哈萨克斯坦警方今年前10个月打掉40余个犯罪团伙</span>
          <span class="news-value-point">💡 中新网阿斯塔纳11月25日电 (记者 单璐)哈萨克斯坦内务部25日通报，今年前10个月，哈警方打掉40余个涉嫌实施严重或特别严重犯罪的团伙</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-25/10737653.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社新加坡11月25日电 (记者 李志全)新加坡南洋理工大学传播与信息学院院长邱林川25日在于新加坡举行的2026“思想亚洲”论坛上表示，亚洲智慧不是要取代其他地区的智慧，而是要为全球治理提供独特参照，提醒世界发展的道路从来不止一条。" data-title="新加坡高校学者：亚洲智慧可为全球治理提供参照" data-date="11-25 20:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-25 20:39</span>
          <span class="news-item-title">新加坡高校学者：亚洲智慧可为全球治理提供参照</span>
          <span class="news-value-point">💡 中新社新加坡11月25日电 (记者 李志全)新加坡南洋理工大学传播与信息学院院长邱林川25日在于新加坡举行的2026“思想亚洲”论坛上表示，亚洲…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c6rmgvkp322xo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="一波与中国有关的账号用AI生成影片，攻击台湾执政党关键人物，包括总统赖清德和台北市长候选人沈伯洋。" data-title="BBC事实查核：与中国有关账号用AI生成影攻击台湾选举候选人" data-date="11-25 19:53" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-25 19:53</span>
          <span class="news-item-title">BBC事实查核：与中国有关账号用AI生成影攻击台湾选举候选人</span>
          <span class="news-value-point">💡 一波与中国有关的账号用AI生成影片，攻击台湾执政党关键人物，包括总统赖清德和台北市长候选人沈伯洋</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theverge.com/science/1042278/spacex-fcc-starmind-ai-space-data-centers" target="_blank" rel="noopener" data-cat="keji" data-summary="美国联邦通信委员会（FCC）周三发布公告称，已授权SpaceX部署多达100万颗配备人工智能芯片的卫星，这是埃隆·马斯克旗下公司“Starmind”计划的一部分。还有几家公司也在致力于将人工智能数据中心" data-title="FCC signs off on SpaceX’s plan to put up to 1 million data center satellites into space" data-date="11-26 01:44" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-26 01:44</span>
          <span class="news-item-title">FCC批准了SpaceX将多达100万颗数据中心卫星送入太空的计划</span>
          <span class="news-item-title-en">FCC signs off on SpaceX’s plan to put up to 1 million data center satellites into space</span>
          <span class="news-value-point">💡 美国联邦通信委员会（FCC）周三发布公告称，已授权SpaceX部署多达100万颗配备人工智能芯片的卫星，这是埃隆·马斯克旗下公司“Starmin…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/laptops/save-usd200-with-surprising-deals-on-new-nvidia-rtx-spark-powered-asus-proart-p14-laptops-both-24gb-and-32gb-configurations-are-already-on-sale" target="_blank" rel="noopener" data-cat="keji" data-summary="在发布仅一个月后，搭载 RTX Spark 的华硕 ProArt P14 现正以 200 美元的优惠价格发售，包括 24GB 和 32GB 两种配置。" data-title="Save $200 with surprising deals on new Nvidia RTX Spark-powered Asus ProArt P14 laptops" data-date="11-26 00:58" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-26 00:58</span>
          <span class="news-item-title">享受惊喜优惠，购买搭载全新Nvidia RTX Spark的华硕ProArt P14笔记本电脑，立省200美元</span>
          <span class="news-item-title-en">Save $200 with surprising deals on new Nvidia RTX Spark-powered Asus ProArt P14 laptops</span>
          <span class="news-value-point">💡 在发布仅一个月后，搭载 RTX Spark 的华硕 ProArt P14 现正以 200 美元的优惠价格发售，包括 24GB 和 32GB 两种…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/policy/lawsuit-reveals-trumps-alleged-strong-arming-of-intel-troubled-chipmaker-allegedly-forced-to-give-white-house-10-percent-stake-for-release-of-chips-act-funds" target="_blank" rel="noopener" data-cat="keji" data-summary="显然，总统曾威胁英特尔董事会，如果他们不接受他提出的获得该公司10%股份的要求，将面临“后果”。" data-title="Lawsuit alleges Trump strong" data-date="11-26 00:39" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-26 00:39</span>
          <span class="news-item-title">诉讼指控特朗普强行</span>
          <span class="news-item-title-en">Lawsuit alleges Trump strong</span>
          <span class="news-value-point">💡 显然，总统曾威胁英特尔董事会，如果他们不接受他提出的获得该公司10%股份的要求，将面临“后果”</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/512748.html" target="_blank" rel="noopener" data-cat="keji" data-summary="商汤SenseNova U1.6" data-title="我以为这是摄影作品，你告诉我这是最新的国产AI？！" data-date="11-26 00:34" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-26 00:34</span>
          <span class="news-item-title">我以为这是摄影作品，你告诉我这是最新的国产AI？！</span>
          <span class="news-value-point">💡 商汤SenseNova U1.6</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/podcast/ai-data-centers-are-becoming-harder-to-build-and-neoclouds-are-feeling-it/" target="_blank" rel="noopener" data-cat="keji" data-summary="⁠Nvidia 已明确表示，在人工智能数据中心即将投入运行之前，它不会提供支持，而此时正值新云公司报告建设延期和债务成本上升。向开发商传达的信息是，土地、电力和竣工的建筑物" data-title="AI data centers are becoming harder to build, and neoclouds are feeling it" data-date="11-25 23:41" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-25 23:41</span>
          <span class="news-item-title">人工智能数据中心越来越难建，新云正在感受到这一点</span>
          <span class="news-item-title-en">AI data centers are becoming harder to build, and neoclouds are feeling it</span>
          <span class="news-value-point">💡 ⁠Nvidia 已明确表示，在人工智能数据中心即将投入运行之前，它不会提供支持，而此时正值新云公司报告建设延期和债务成本上升</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/512727.html" target="_blank" rel="noopener" data-cat="keji" data-summary="丢个故事就行！直出15分钟AI短片，家里二舅也能上手" data-title="丢个故事就行！直出15分钟AI短片，家里二舅也能上手" data-date="11-25 22:51" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-25 22:51</span>
          <span class="news-item-title">丢个故事就行！直出15分钟AI短片，家里二舅也能上手</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/512715.html" target="_blank" rel="noopener" data-cat="keji" data-summary="智元推出行业首个开放且完整的具身智能生态技术体系AIMA" data-title="零基础也能做开发，智元灵心平台一年孵化超3万个机器人智能体" data-date="11-25 22:32" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-25 22:32</span>
          <span class="news-item-title">零基础也能做开发，智元灵心平台一年孵化超3万个机器人智能体</span>
          <span class="news-value-point">💡 智元推出行业首个开放且完整的具身智能生态技术体系AIMA</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/512582.html" target="_blank" rel="noopener" data-cat="keji" data-summary="11月25日，以“算力唤醒真实世界”为主题的2026物理AI行业峰会暨九章云极智算生态大会在深圳举行。" data-title="算力唤醒真实世界：九章云极发布物理AI工厂与生态开放计划" data-date="11-25 22:21" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-25 22:21</span>
          <span class="news-item-title">算力唤醒真实世界：九章云极发布物理AI工厂与生态开放计划</span>
          <span class="news-value-point">💡 11月25日，以“算力唤醒真实世界”为主题的2026物理AI行业峰会暨九章云极智算生态大会在深圳举行</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/512683.html" target="_blank" rel="noopener" data-cat="keji" data-summary="贯通具⾝智能研发流程" data-title="逐际动⼒与商汤⼤装置达成合作，以高质量算力全⾯⽀撑机器⼈仿真训练与测试" data-date="11-25 22:20" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-25 22:20</span>
          <span class="news-item-title">逐际动⼒与商汤⼤装置达成合作，以高质量算力全⾯⽀撑机器⼈仿真训练与测试</span>
          <span class="news-value-point">💡 贯通具⾝智能研发流程</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/25/amazon-and-meta-reportedly-in-talks-to-lift-blockade-on-ai-agent-muse/" target="_blank" rel="noopener" data-cat="keji" data-summary="亚马逊和Meta正在讨论一项潜在的交易，该交易将结束对Muse长达两个月的封锁。" data-title="Amazon and Meta reportedly in talks to lift blockade on AI agent Muse" data-date="11-25 22:10" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-25 22:10</span>
          <span class="news-item-title">据报道，亚马逊和Meta正在就解除对AI代理Muse的封锁进行谈判</span>
          <span class="news-item-title-en">Amazon and Meta reportedly in talks to lift blockade on AI agent Muse</span>
          <span class="news-value-point">💡 亚马逊和Meta正在讨论一项潜在的交易，该交易将结束对Muse长达两个月的封锁</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-25/10737796.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网杭州11月25日电(鲍梦妮)具身智能走向真实场景的难点、瓶颈在哪里？11月25日，“科学咖啡馆·未来产业专场”在杭州举行，来自政府部门、高校科研平台、具身智能相关企业以及投资机构齐聚，共同探讨真实场景如何“喂养”具身大脑、整机与场景如何协同验证，为浙江具身智能产业加速落地真实场景提供路径。" data-title="浙江“科学咖啡馆”推动具身智能走向真实场景" data-date="11-25 21:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-25 21:22</span>
          <span class="news-item-title">浙江“科学咖啡馆”推动具身智能走向真实场景</span>
          <span class="news-value-point">💡 中新网杭州11月25日电(鲍梦妮)具身智能走向真实场景的难点、瓶颈在哪里</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/25/the-questions-jensen-huang-and-nvidia-will-still-have-to-answer-about-megaspeed/" target="_blank" rel="noopener" data-cat="keji" data-summary="调查人员的核心问题是，Nvidia对这些芯片的最终去向了解多少，以及黄仁勋与Megaspeed高管的私情是否让该公司有理由怀疑Megaspeed的保证。" data-title="The questions Jensen Huang and Nvidia will still have to answer about Megaspeed" data-date="11-25 21:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-25 21:00</span>
          <span class="news-item-title">黄仁勋和英伟达仍需回答的有关Megaspeed的问题</span>
          <span class="news-item-title-en">The questions Jensen Huang and Nvidia will still have to answer about Megaspeed</span>
          <span class="news-value-point">💡 调查人员的核心问题是，Nvidia对这些芯片的最终去向了解多少，以及黄仁勋与Megaspeed高管的私情是否让该公司有理由怀疑Megaspeed…</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/512538.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Fable5.2已经很旧了。" data-title="Anthropic还藏着2个最强模型…" data-date="11-25 16:23" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-25 16:23</span>
          <span class="news-item-title">Anthropic还藏着2个最强模型…</span>
          <span class="news-value-point">💡 Fable5.2已经很旧了</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/24/yales-sonnenfeld-nvidia-is-a-detriment-to-u-s-industrial-might-not-a-champion/" target="_blank" rel="noopener" data-cat="keji" data-summary="耶鲁大学的杰弗里·索南菲尔德（Jeffrey Sonnenfeld）警告称，市场周一欢呼雀跃的事件——即黄仁勋在白宫的支持下重返英伟达担任首席执行官和董事会成员——可能会被证明是一个巨大的错误，使董事们面临因日益增加的诉讼而产生的“历史性”个人责任。" data-title="Yale’s Sonnenfeld: Nvidia is a ‘detriment’ to US industrial might" data-date="11-25 08:12" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-25 08:12</span>
          <span class="news-item-title">耶鲁大学的索南菲尔德：英伟达对美国工业实力“有害”</span>
          <span class="news-item-title-en">Yale’s Sonnenfeld: Nvidia is a ‘detriment’ to US industrial might</span>
          <span class="news-value-point">💡 耶鲁大学的杰弗里·索南菲尔德（Jeffrey Sonnenfeld）警告称，市场周一欢呼雀跃的事件——即黄仁勋在白宫的支持下重返英伟达担任首席执…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/24/in-all-hands-meeting-jensen-huang-thanks-white-house-and-says-hes-in-therapy/" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达创始人周二向员工道歉，并表示感谢大家给他第二次领导公司的机会。" data-title="In all-hands meeting, Jensen Huang thanks White House and says he’s in therapy" data-date="11-25 05:48" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-25 05:48</span>
          <span class="news-item-title">在全体员工大会上，黄仁勋感谢白宫，并表示他正在接受心理治疗</span>
          <span class="news-item-title-en">In all-hands meeting, Jensen Huang thanks White House and says he’s in therapy</span>
          <span class="news-value-point">💡 英伟达创始人周二向员工道歉，并表示感谢大家给他第二次领导公司的机会</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">10 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cw20xr4d7x55o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="诺丁汉森林队主教练奥利弗·格拉斯纳（Oliver Glasner）质疑，为什么他的球队中有些人来英国多年后仍不会说英语。" data-title="Glasner criticises Forest players yet to learn English" data-date="11-26 02:00" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-26 02:00</span>
          <span class="news-item-title">格拉斯纳批评诺丁汉森林球员尚未学会英语</span>
          <span class="news-item-title-en">Glasner criticises Forest players yet to learn English</span>
          <span class="news-value-point">💡 诺丁汉森林队主教练奥利弗·格拉斯纳（Oliver Glasner）质疑，为什么他的球队中有些人来英国多年后仍不会说英语</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13616388/dominik-szoboszlai-free-kick-for-liverpool-vs-man-utd-reveals-grey-area-as-mauricio-pochettino-questions-decision" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在曼联输给利物浦的比赛中，毛里西奥·波切蒂诺对勒尼·约罗被罚红牌感到愤怒，但也认为多米尼克·索博斯洛伊的开场进球不应被判有效——他说的对吗？" data-title="Why wasn&#39;t Szoboszlai&#39;s free-kick ruled out vs Man Utd?" data-date="11-25 23:15" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 23:15</span>
          <span class="news-item-title">为什么索博斯洛伊对曼联的任意球没有被判无效？</span>
          <span class="news-item-title-en">Why wasn't Szoboszlai's free-kick ruled out vs Man Utd?</span>
          <span class="news-value-point">💡 在曼联输给利物浦的比赛中，毛里西奥·波切蒂诺对勒尼·约罗被罚红牌感到愤怒，但也认为多米尼克·索博斯洛伊的开场进球不应被判有效——他说的对吗</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025486/arsenal-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Arsenal latest: Merson accuses Gunners of second" data-title="Arsenal latest: Merson accuses Gunners of second" data-date="11-25 21:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 21:00</span>
          <span class="news-item-title">阿森纳最新消息：默森指责枪手屈居第二</span>
          <span class="news-item-title-en">Arsenal latest: Merson accuses Gunners of second</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13616290/raheem-sterling-former-england-international-given-suspended-12-month-jail-sentence-for-dangerous-driving" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="前英格兰球员拉希姆·斯特林（Raheem Sterling）因在高速公路上发生涉及兰博基尼的撞车事故，被判处12个月的缓刑，罪名是危险驾驶和持有氧化亚氮。" data-title="Sterling given suspended jail sentence for dangerous driving" data-date="11-25 19:30" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 19:30</span>
          <span class="news-item-title">斯特林因危险驾驶被判缓刑</span>
          <span class="news-item-title-en">Sterling given suspended jail sentence for dangerous driving</span>
          <span class="news-value-point">💡 前英格兰球员拉希姆·斯特林（Raheem Sterling）因在高速公路上发生涉及兰博基尼的撞车事故，被判处12个月的缓刑，罪名是危险驾驶和持有…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13616028/raheem-sterling-enjoyed-a-wonderful-premier-league-career-but-regularly-attracted-controversy-is-there-any-way-back" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="拉希姆·斯特林曾有过一段势不可挡的时期。这位球员的奔跑风格独具抽象美，但带球时却总能给人一种游刃有余的稳健感。像滑翔机般在球场上飞驰。" data-title="Sterling&#39;s career was defined by comebacks - this could be one too many" data-date="11-25 19:30" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 19:30</span>
          <span class="news-item-title">斯特林的职业生涯以东山再起为标志——这次可能有点过分了</span>
          <span class="news-item-title-en">Sterling's career was defined by comebacks - this could be one too many</span>
          <span class="news-value-point">💡 拉希姆·斯特林曾有过一段势不可挡的时期</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13616234/arsenal-and-manchester-citys-problems-analysed-as-both-set-to-meet-in-bumper-premier-league-clash-this-weekend" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳本周末将在英超联赛中迎战曼城，这是一场备受瞩目的比赛，但在最近几天和几个月里，两支球队都有一些问题需要克服。" data-title="Arsenal punished for bluntness in attack - but Man City also have problems" data-date="11-25 06:54" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 06:54</span>
          <span class="news-item-title">阿森纳因进攻乏力而受到惩罚，但曼城也存在问题</span>
          <span class="news-item-title-en">Arsenal punished for bluntness in attack - but Man City also have problems</span>
          <span class="news-value-point">💡 阿森纳本周末将在英超联赛中迎战曼城，这是一场备受瞩目的比赛，但在最近几天和几个月里，两支球队都有一些问题需要克服</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqzr5ylmeerlo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联和毛里西奥·波切蒂诺对VAR裁判约翰·布鲁克斯和裁判主管霍华德·韦伯处理莱尼·约罗红牌的方式感到愤怒。" data-title="Pochettino leads Man Utd fury at Yoro red card ruling" data-date="11-25 06:05" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-25 06:05</span>
          <span class="news-item-title">波切蒂诺带头对尤罗的红牌判罚表示不满</span>
          <span class="news-item-title-en">Pochettino leads Man Utd fury at Yoro red card ruling</span>
          <span class="news-value-point">💡 曼联和毛里西奥·波切蒂诺对VAR裁判约翰·布鲁克斯和裁判主管霍华德·韦伯处理莱尼·约罗红牌的方式感到愤怒</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13616134/mauricio-pochettino-man-utd-boss-fumes-at-var-in-liverpool-loss-over-leny-yoro-and-dominik-szoboszlai-calls" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在曼联输给利物浦的比赛中，莱尼·约罗的红牌被撤销，毛里西奥·波切蒂诺对此严厉批评了VAR。这位阿根廷人认为，多米尼克·索博斯洛伊的开场进球本不应算作有效。" data-title="Poch fumes at Yoro red and thinks Szoboszlai goal shouldn&#39;t have stood" data-date="11-25 05:50" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 05:50</span>
          <span class="news-item-title">波切蒂诺对约罗的红牌感到愤怒，并认为索博斯洛伊的进球不应有效</span>
          <span class="news-item-title-en">Poch fumes at Yoro red and thinks Szoboszlai goal shouldn't have stood</span>
          <span class="news-value-point">💡 在曼联输给利物浦的比赛中，莱尼·约罗的红牌被撤销，毛里西奥·波切蒂诺对此严厉批评了VAR</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025492/man-utd-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Man Utd latest: Should Szoboszlai&#39;s goal have stood? Vote!" data-title="Man Utd latest: Should Szoboszlai&#39;s goal have stood? Vote!" data-date="11-25 03:43" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 03:43</span>
          <span class="news-item-title">曼联最新消息：索博斯洛伊的进球是否应该有效？请投票！</span>
          <span class="news-item-title-en">Man Utd latest: Should Szoboszlai's goal have stood? Vote!</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025501/liverpool-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Liverpool latest: Wirtz enjoying life after finding top form" data-title="Liverpool latest: Wirtz enjoying life after finding top form" data-date="11-25 02:15" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 02:15</span>
          <span class="news-item-title">利物浦最新消息：维尔茨在找回最佳状态后享受生活</span>
          <span class="news-item-title-en">Liverpool latest: Wirtz enjoying life after finding top form</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/microsd-cards/best-nintendo-switch-2-microsd-express-card-deals-2026" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在本次黑色星期五促销活动期间，抢购一张适用于任天堂Switch 2的全新microSD Express卡。我们会不断更新此列表，提供所有大型零售商的最佳优惠。" data-title="Best Black Friday Nintendo Switch 2 microSD Express card deals 2026" data-date="11-26 02:01" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-26 02:01</span>
          <span class="news-item-title">2026年黑色星期五Nintendo Switch 2 microSD Express卡超值优惠</span>
          <span class="news-item-title-en">Best Black Friday Nintendo Switch 2 microSD Express card deals 2026</span>
          <span class="news-value-point">💡 在本次黑色星期五促销活动期间，抢购一张适用于任天堂Switch 2的全新microSD Express卡</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1041460/fairphone-6-plus-repairable-phone-black-friday-2026-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="与大多数智能手机不同，Fairphone 6 Plus专为在家维修而设计，其零部件易于更换，有助于延长其使用寿命。这使得其中端价位更容易被接受，特别是在现在降价的情况下。" data-title="The Fairphone 6 Plus is modular, repairable, and $100 off right now" data-date="11-26 02:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-26 02:00</span>
          <span class="news-item-title">Fairphone 6 Plus 采用模块化设计，可维修，现正优惠 100 美元</span>
          <span class="news-item-title-en">The Fairphone 6 Plus is modular, repairable, and $100 off right now</span>
          <span class="news-value-point">💡 与大多数智能手机不同，Fairphone 6 Plus专为在家维修而设计，其零部件易于更换，有助于延长其使用寿命</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/column/1041761/optimizer-peptide-parties-afterglow" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这是Optimizer，由Verge高级评论员Victoria Song发出的每周通讯，深入剖析和讨论那些宣称将改变您生活的最新小玩意和灵丹妙药。请在此订阅Optimizer。在一个秋雨绵绵的夜晚，一位体验者" data-title="The loneliest peptide party in New York" data-date="11-26 02:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-26 02:00</span>
          <span class="news-item-title">纽约最寂寞的肽派对</span>
          <span class="news-item-title-en">The loneliest peptide party in New York</span>
          <span class="news-value-point">💡 这是Optimizer，由Verge高级评论员Victoria Song发出的每周通讯，深入剖析和讨论那些宣称将改变您生活的最新小玩意和灵丹妙药</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/save-usd2600-on-the-cheapest-rtx-5090-prebuilt-pc-weve-found-so-far-in-the-black-friday-rush-corsair-vengeance-i7600-features-ultra-9-285k-cpu-64gb-ram-and-the-ultimate-gaming-gpu" target="_blank" rel="noopener" data-cat="zonghe" data-summary="TKTK" data-title="Save $2600 on the cheapest RTX 5090 prebuilt PC we&#39;ve found so far in the Black Friday rush" data-date="11-26 01:45" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-26 01:45</span>
          <span class="news-item-title">在黑色星期五购物狂潮中，我们迄今为止发现的最便宜的RTX 5090预装电脑可节省2600美元</span>
          <span class="news-item-title-en">Save $2600 on the cheapest RTX 5090 prebuilt PC we've found so far in the Black Friday rush</span>
          <span class="news-value-point">💡 TKTK</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/25/state-ags-fight-character-ais-plan-to-auction-off-users-private-chats/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="州总检察长表示，拟议的Character.ai破产拍卖包括来自超过2100万个美国账户的敏感个人数据，其中210万个账户由未成年人注册。" data-title="State AGs fight Character AI’s plan to auction off users’ private chats" data-date="11-26 01:35" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-26 01:35</span>
          <span class="news-item-title">各州总检察长反对Character AI拍卖用户私人聊天的计划</span>
          <span class="news-item-title-en">State AGs fight Character AI’s plan to auction off users’ private chats</span>
          <span class="news-value-point">💡 州总检察长表示，拟议的Character.ai破产拍卖包括来自超过2100万个美国账户的敏感个人数据，其中210万个账户由未成年人注册</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/desktops/gaming-pcs/the-best-prebuilt-gaming-pcs-weve-seen-on-sale-so-far-the-four-best-rtx-5090-5070-and-5060-gaming-pcs" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这些是我们在这个黑色星期五看到的预组装游戏电脑的最佳优惠。" data-title="The best prebuilt gaming PCs we&#39;ve seen on sale so far" data-date="11-26 01:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-26 01:20</span>
          <span class="news-item-title">迄今为止我们见过的最棒的预装游戏电脑特惠</span>
          <span class="news-item-title-en">The best prebuilt gaming PCs we've seen on sale so far</span>
          <span class="news-value-point">💡 这些是我们在这个黑色星期五看到的预组装游戏电脑的最佳优惠</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/peripherals/gaming-chairs/best-gaming-chair-deals-2026" target="_blank" rel="noopener" data-cat="zonghe" data-summary="适合各种预算、风格和舒适度的游戏椅，尽享黑色星期五超值优惠。用高品质的产品升级您的游戏椅。" data-title="Best Black Friday gaming chair deals 2026" data-date="11-26 01:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-26 01:00</span>
          <span class="news-item-title">2026年黑色星期五最佳游戏椅优惠</span>
          <span class="news-item-title-en">Best Black Friday gaming chair deals 2026</span>
          <span class="news-value-point">💡 适合各种预算、风格和舒适度的游戏椅，尽享黑色星期五超值优惠</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/racing/news/12040/13616389/newburys-coral-gold-cup-jamie-lynchs-horse-by-horse-guide-to-saturdays-feature-handicap-chase-live-on-sky-sports-racing" target="_blank" rel="noopener" data-cat="zonghe" data-summary="杰米·林奇（Jamie Lynch）对参赛马匹进行了评估，并为本周六本赛季最负盛名的让赛之一提供了他的最佳建议，比赛将在天空体育赛马频道（Sky Sports Racing）现场直播。" data-title="Newbury&#39;s Coral Gold Cup: Jamie Lynch&#39;s horse" data-date="11-26 01:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 01:00</span>
          <span class="news-item-title">纽伯里珊瑚金杯赛：杰米·林奇的马</span>
          <span class="news-item-title-en">Newbury's Coral Gold Cup: Jamie Lynch's horse</span>
          <span class="news-value-point">💡 杰米·林奇（Jamie Lynch）对参赛马匹进行了评估，并为本周六本赛季最负盛名的让赛之一提供了他的最佳建议，比赛将在天空体育赛马频道（Sky…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/rugby-league/news/12040/13616443/super-league-london-broncos-confirmed-as-15th-team-for-2027-season-after-clubs-voted-in-favour-of-motion" target="_blank" rel="noopener" data-cat="zonghe" data-summary="伦敦野牛队已确认成为2027赛季超级联赛的第15支球队。" data-title="London Broncos confirmed as Super League&#39;s 15th team for 2027 season" data-date="11-26 01:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 01:00</span>
          <span class="news-item-title">伦敦野牛队确认成为2027赛季超级联赛的第15支球队</span>
          <span class="news-item-title-en">London Broncos confirmed as Super League's 15th team for 2027 season</span>
          <span class="news-value-point">💡 伦敦野牛队已确认成为2027赛季超级联赛的第15支球队</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/boxing/news/12040/13616397/fight-back-promotions-a-new-venture-to-support-women-affected-by-domestic-violence-begins-its-triumph-over-trauma" target="_blank" rel="noopener" data-cat="zonghe" data-summary="一项旨在支持遭受家庭暴力和基于性别的暴力的女性的新拳击推广活动将于周六在伦敦的拉德布鲁克大厅（Ladbroke Hall）举行首场赛事。" data-title="&#39;Triumph over trauma&#39; - new women&#39;s boxing promotion begins" data-date="11-26 01:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 01:00</span>
          <span class="news-item-title">“战胜创伤”——新的女子拳击推广活动拉开帷幕</span>
          <span class="news-item-title-en">'Triumph over trauma' - new women's boxing promotion begins</span>
          <span class="news-value-point">💡 一项旨在支持遭受家庭暴力和基于性别的暴力的女性的新拳击推广活动将于周六在伦敦的拉德布鲁克大厅（Ladbroke Hall）举行首场赛事</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/hdds/best-hard-drive-hdd-deals-2026" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这些是2026年黑色星期五最超值的硬盘优惠，保证让您在不掏空钱包的情况下扩展电脑的存储空间。我们会不断更新此列表，为您提供所有零售商的最佳优惠。" data-title="Best Black Friday hard drive deals 2026" data-date="11-26 00:32" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-26 00:32</span>
          <span class="news-item-title">2026年黑色星期五最佳硬盘优惠</span>
          <span class="news-item-title-en">Best Black Friday hard drive deals 2026</span>
          <span class="news-value-point">💡 这些是2026年黑色星期五最超值的硬盘优惠，保证让您在不掏空钱包的情况下扩展电脑的存储空间</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/f1/news/12040/13616434/williams-in-minor-breach-of-f1-cost-cap-and-take-financial-and-wind-tunnel-time-penalties" target="_blank" rel="noopener" data-cat="zonghe" data-summary="威廉姆斯车队因在2025赛季略微超出F1的成本上限，而被处以财务和空气动力学测试处罚。" data-title="Williams handed penalties after minor breach of cost cap" data-date="11-26 00:17" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 00:17</span>
          <span class="news-item-title">威廉姆斯车队因轻微违反成本上限而被处以罚款</span>
          <span class="news-item-title-en">Williams handed penalties after minor breach of cost cap</span>
          <span class="news-value-point">💡 威廉姆斯车队因在2025赛季略微超出F1的成本上限，而被处以财务和空气动力学测试处罚</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/rugby-union/news/12040/13616405/ireland-vs-australia-mack-hansen-out-with-injury-as-nick-timoney-replaces-suspended-dan-sheehan-for-nations-championship-clash" target="_blank" rel="noopener" data-cat="zonghe" data-summary="马克·汉森（Mack Hansen）已确定无缘爱尔兰队本周五在安联体育场与澳大利亚队进行的国家锦标赛决赛首发阵容。" data-title="Hansen ruled out of Ireland&#39;s clash with Australia due to injury" data-date="11-26 00:10" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 00:10</span>
          <span class="news-item-title">汉森因伤缺席爱尔兰与澳大利亚的比赛</span>
          <span class="news-item-title-en">Hansen ruled out of Ireland's clash with Australia due to injury</span>
          <span class="news-value-point">💡 马克·汉森（Mack Hansen）已确定无缘爱尔兰队本周五在安联体育场与澳大利亚队进行的国家锦标赛决赛首发阵容</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1042162/nothing-ear-note-ai-earbuds-reveal" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在即将于12月8日发布之前，Nothing展示了其即将推出的AI耳机的更多细节。Ear Note耳机可以录制您的通话，而其充电盒可以录制、转录和总结您的对话。与Ear" data-title="Nothing offers a full look at its AI earbuds and charging case" data-date="11-26 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-26 00:00</span>
          <span class="news-item-title">Nothing全面展示其AI耳机和充电盒</span>
          <span class="news-item-title-en">Nothing offers a full look at its AI earbuds and charging case</span>
          <span class="news-value-point">💡 在即将于12月8日发布之前，Nothing展示了其即将推出的AI耳机的更多细节</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/032/534.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 26 日消息，由《碧蓝航线》开发商蛮啾网络打造的幻想大世界 RPG《蓝色星原：旅谣》将于 11 月 26 日 10:00 正式开启公测，登陆 PC、iOS、安卓、鸿蒙与 PS5 平台。该作由上海蛮啾网络科技有限公司研发并运营，采用 Unity 引擎开发，背景音乐有川井宪次、西木康智等作曲家参与。海外发行方面，日服由蛮啾网络与悠星联合发行，韩服由 NEXON 代理，东南亚地区由 PlayPark 负责。故事舞台为幻想大陆普罗米利亚。玩家扮演“星临者”重返这片土地，在灾变后秩序失衡的世界中游历，追寻散落于天地间的星光传说。与常见的开放世界产品不同，本作不设强制线性流程，探索解谜、动作战斗与家园经营之间的切换由玩家自行安排。核心玩法围绕幻想生物“奇波”展开（IT之家注：奇波为本" data-title="蛮啾《蓝色星原：旅谣》今日公测：两百余种奇波可捕捉骑乘，登陆 PC、iOS、安卓、鸿蒙与 PS5" data-date="11-26 00:00" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-26 00:00</span>
          <span class="news-item-title">蛮啾《蓝色星原：旅谣》今日公测：两百余种奇波可捕捉骑乘，登陆 PC、iOS、安卓、鸿蒙与 PS5</span>
          <span class="news-value-point">💡 IT之家 11 月 26 日消息，由《碧蓝航线》开发商蛮啾网络打造的幻想大世界 RPG《蓝色星原：旅谣》将于 11 月 26 日 10:00 正…</span>
        </a>
  </div>
</div>
<script defer src="{{ "/assets/js/news-feed.js" | relative_url }}"></script>


<p class="news-updated">🕐 抓取更新于 2026-11-26 02:05（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
