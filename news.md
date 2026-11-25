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
      <span>2026-11-26 05:52 抓取更新</span>
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
        <span class="channel-count">56</span>
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
        <span class="channel-count">12</span>
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
  <div class="ov-item"><span class="ov-num">56</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">4</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×12 · Tom's Hardware×10</span><span class="ov-label">TOP 信源</span></div>
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
    <a class="hero-sub-card" href="https://www.nytimes.com/2026/11/25/business/stocks-sp500-nvidia-ai.html" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达和其他科技公司股价下跌，原因是投资者权衡了全球贸易的发展和利率走势。" data-title="Stocks Slump Again as Investors Fret About A.I., Tariffs and Inflation" data-date="11-26 05:32" data-source="纽约时报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
      </div>
      <p class="hero-sub-title">投资者对人工智能、关税和通胀感到担忧，股市再次暴跌</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/c65y10z8k59jo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英格兰足球独立监管机构主席向议员表示，他“有胆量”对曼城采取潜在的行动。" data-title="Regulator chief &#39;has stomach&#39; to face Man City" data-date="11-26 05:27" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">监管机构负责人“有胆量”面对曼城</p>
    </a>
    <a class="hero-sub-card" href="https://www.nytimes.com/2026/11/25/weather/thanksgiving-weather-storm-rain-flooding.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这场风暴正在海上形成，预计将向内陆移动，穿过北卡罗来纳州，并在感恩节期间向东北方向推进。" data-title="Thanksgiving Storm Is Expected to Hit East Coast With Heavy Rain and Flooding" data-date="11-26 05:47" data-source="纽约时报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
      </div>
      <p class="hero-sub-title">感恩节风暴预计将袭击东海岸，带来大雨和洪涝</p>
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
        <a class="news-item" href="https://www.nytimes.com/2026/11/25/business/stocks-sp500-nvidia-ai.html" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达和其他科技公司股价下跌，原因是投资者权衡了全球贸易的发展和利率走势。" data-title="Stocks Slump Again as Investors Fret About A.I., Tariffs and Inflation" data-date="11-26 05:32" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-26 05:32</span>
          <span class="news-item-title">投资者对人工智能、关税和通胀感到担忧，股市再次暴跌</span>
          <span class="news-item-title-en">Stocks Slump Again as Investors Fret About A.I., Tariffs and Inflation</span>
          <span class="news-value-point">💡 英伟达和其他科技公司股价下跌，原因是投资者权衡了全球贸易的发展和利率走势</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/25/nyregion/mamdani-rent-freeze-legal-challenge-apartments.html" target="_blank" rel="noopener" data-cat="keji" data-summary="曼哈顿的一名法官驳回了房东就租金稳定公寓的租金冻结提起的诉讼，从而使市议员Zohran Mamdani胜诉。" data-title="Mamdani Wins Against Landlords in Rent Freeze Lawsuit" data-date="11-26 05:16" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-26 05:16</span>
          <span class="news-item-title">Mamdani在租金冻结诉讼中胜诉房东</span>
          <span class="news-item-title-en">Mamdani Wins Against Landlords in Rent Freeze Lawsuit</span>
          <span class="news-value-point">💡 曼哈顿的一名法官驳回了房东就租金稳定公寓的租金冻结提起的诉讼，从而使市议员Zohran Mamdani胜诉</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/25/openai-says-heavy-chatgpt-users-may-hit-limits-sooner-as-it-merges-chat-and-work/" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI 将在整个 ChatGPT 中引入一个统一的使用量仪表，因为它将聊天和工作体验结合在一起。" data-title="OpenAI says heavy ChatGPT users may hit limits sooner as it merges Chat and Work" data-date="11-26 04:03" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-26 04:03</span>
          <span class="news-item-title">OpenAI表示，随着ChatGPT将聊天和工作功能合并，重度用户可能更快达到使用上限。</span>
          <span class="news-item-title-en">OpenAI says heavy ChatGPT users may hit limits sooner as it merges Chat and Work</span>
          <span class="news-value-point">💡 OpenAI 将在整个 ChatGPT 中引入一个统一的使用量仪表，因为它将聊天和工作体验结合在一起</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/25/jensen-huang-broke-nvidias-code-of-conduct-and-his-employees-may-not-forget-it/" target="_blank" rel="noopener" data-cat="keji" data-summary="大多数行为准则都反映了企业文化。就英伟达而言，这可能会产生后果。" data-title="Jensen Huang broke Nvidia’s code of conduct, and his employees may not forget it" data-date="11-26 03:54" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-26 03:54</span>
          <span class="news-item-title">黄仁勋违反了英伟达的行为准则，他的员工可能不会忘记这一点</span>
          <span class="news-item-title-en">Jensen Huang broke Nvidia’s code of conduct, and his employees may not forget it</span>
          <span class="news-value-point">💡 大多数行为准则都反映了企业文化</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/25/anthropics-dario-amodei-calls-accusations-of-surrendering-human-control-to-ai-absurd/" target="_blank" rel="noopener" data-cat="keji" data-summary="尽管领先的人工智能公司正日益实现其自身研究和模型开发的自动化，但Anthropic首席执行官Dario Amodei仍对竞争对手的指责予以回击，后者指责他倾向于将人类的自主权拱手让与人工智能。" data-title="Anthropic’s Dario Amodei calls accusations of surrendering human control to AI ‘absurd’" data-date="11-26 03:44" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-26 03:44</span>
          <span class="news-item-title">Anthropic的Dario Amodei称，将人类控制权拱手让给人工智能的指控“荒谬”</span>
          <span class="news-item-title-en">Anthropic’s Dario Amodei calls accusations of surrendering human control to AI ‘absurd’</span>
          <span class="news-value-point">💡 尽管领先的人工智能公司正日益实现其自身研究和模型开发的自动化，但Anthropic首席执行官Dario Amodei仍对竞争对手的指责予以回击，…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/25/want-to-buy-your-kid-an-ai-toy-this-christmas-not-in-new-york/" target="_blank" rel="noopener" data-cat="keji" data-summary="纽约已禁止人工智能聊天机器人玩具五年，因为Common Sense Media的新研究揭示了令人担忧的安全缺陷，包括接触不当内容和对情绪发展的风险。" data-title="Want to buy your kid an AI toy this Christmas? Not in New York" data-date="11-26 02:11" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-26 02:11</span>
          <span class="news-item-title">想在这个圣诞节给孩子买一个人工智能玩具吗？在纽约不行</span>
          <span class="news-item-title-en">Want to buy your kid an AI toy this Christmas? Not in New York</span>
          <span class="news-value-point">💡 纽约已禁止人工智能聊天机器人玩具五年，因为Common Sense Media的新研究揭示了令人担忧的安全缺陷，包括接触不当内容和对情绪发展的风…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/save-usd2600-on-the-cheapest-rtx-5090-prebuilt-pc-weve-found-so-far-in-the-black-friday-rush-corsair-vengeance-i7600-features-ultra-9-285k-cpu-64gb-ram-and-the-ultimate-gaming-gpu" target="_blank" rel="noopener" data-cat="keji" data-summary="这款 Corsair Vengeance 预组装游戏电脑将 RTX 5090 与英特尔最强大的 Arrow Lake 处理器和 64GB 内存相结合，可满足最苛刻的工作或游戏需求。" data-title="Save $2600 on the cheapest RTX 5090 prebuilt PC we&#39;ve found so far in the Black Friday rush" data-date="11-26 01:45" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-26 01:45</span>
          <span class="news-item-title">在黑色星期五购物狂潮中，我们迄今为止发现的最便宜的RTX 5090预装电脑可节省2600美元</span>
          <span class="news-item-title-en">Save $2600 on the cheapest RTX 5090 prebuilt PC we've found so far in the Black Friday rush</span>
          <span class="news-value-point">💡 这款 Corsair Vengeance 预组装游戏电脑将 RTX 5090 与英特尔最强大的 Arrow Lake 处理器和 64GB 内存相…</span>
        </a>
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
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">12 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c65y10z8k59jo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英格兰足球独立监管机构主席向议员表示，他“有胆量”对曼城采取潜在的行动。" data-title="Regulator chief &#39;has stomach&#39; to face Man City" data-date="11-26 05:27" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-26 05:27</span>
          <span class="news-item-title">监管机构负责人“有胆量”面对曼城</span>
          <span class="news-item-title-en">Regulator chief 'has stomach' to face Man City</span>
          <span class="news-value-point">💡 英格兰足球独立监管机构主席向议员表示，他“有胆量”对曼城采取潜在的行动</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13616555/porting-lisbon-vs-manchester-united-clinton-morrison-reacts-to-bizarre-bruno-fernandes-goal" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="克林顿·莫里森观看了曼联凭借布鲁诺·费尔南德斯的诡异进球以 2-1 战胜里斯本竞技的比赛。" data-title="Strangest goal ever?! Morrison reacts to BIZARRE Bruno goal!" data-date="11-26 05:14" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 05:14</span>
          <span class="news-item-title">有史以来最奇怪的进球？！莫里森对布鲁诺的离奇进球做出反应！</span>
          <span class="news-item-title-en">Strangest goal ever?! Morrison reacts to BIZARRE Bruno goal!</span>
          <span class="news-value-point">💡 克林顿·莫里森观看了曼联凭借布鲁诺·费尔南德斯的诡异进球以 2-1 战胜里斯本竞技的比赛</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13616547/sporing-lisbon-vs-manchester-united-clinton-morrison-reacts-to-double-penalty-drama" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="克林顿·莫里森对曼联在欧冠与里斯本竞技的比赛中被判的两粒点球发表了看法。" data-title="&#39;Where&#39;s he going?!&#39; - Morrison reacts to Man Utd double penalty drama!" data-date="11-26 04:43" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 04:43</span>
          <span class="news-item-title">“他要去哪里？！“- 莫里森对曼联的两粒点球戏剧性事件做出反应！</span>
          <span class="news-item-title-en">'Where's he going?!' - Morrison reacts to Man Utd double penalty drama!</span>
          <span class="news-value-point">💡 克林顿·莫里森对曼联在欧冠与里斯本竞技的比赛中被判的两粒点球发表了看法</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/burnley-vs-birmingham-city/live/560699" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Birmingham ease to victory at troubled Burnley LIVE!" data-title="Birmingham ease to victory at troubled Burnley LIVE!" data-date="11-26 03:15" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 03:15</span>
          <span class="news-item-title">伯明翰轻松战胜陷入困境的伯恩利，直播！</span>
          <span class="news-item-title-en">Birmingham ease to victory at troubled Burnley LIVE!</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cw20xr4d7x55o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="诺丁汉森林队主教练奥利弗·格拉斯纳（Oliver Glasner）质疑，为什么他的球队中有些人来英国多年后仍不会说英语。" data-title="Glasner criticises Forest players yet to learn English" data-date="11-26 02:32" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-26 02:32</span>
          <span class="news-item-title">格拉斯纳批评诺丁汉森林球员尚未学会英语</span>
          <span class="news-item-title-en">Glasner criticises Forest players yet to learn English</span>
          <span class="news-value-point">💡 诺丁汉森林队主教练奥利弗·格拉斯纳（Oliver Glasner）质疑，为什么他的球队中有些人来英国多年后仍不会说英语</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/club-brugge-vs-liverpool/live/577679" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Game over? Liverpool three up at Club Brugge LIVE!" data-title="Game over? Liverpool three up at Club Brugge LIVE!" data-date="11-26 01:58" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 01:58</span>
          <span class="news-item-title">比赛结束？利物浦在布鲁日俱乐部以三球领先！</span>
          <span class="news-item-title-en">Game over? Liverpool three up at Club Brugge LIVE!</span>
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
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/11/25/weather/thanksgiving-weather-storm-rain-flooding.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这场风暴正在海上形成，预计将向内陆移动，穿过北卡罗来纳州，并在感恩节期间向东北方向推进。" data-title="Thanksgiving Storm Is Expected to Hit East Coast With Heavy Rain and Flooding" data-date="11-26 05:47" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-26 05:47</span>
          <span class="news-item-title">感恩节风暴预计将袭击东海岸，带来大雨和洪涝</span>
          <span class="news-item-title-en">Thanksgiving Storm Is Expected to Hit East Coast With Heavy Rain and Flooding</span>
          <span class="news-value-point">💡 这场风暴正在海上形成，预计将向内陆移动，穿过北卡罗来纳州，并在感恩节期间向东北方向推进</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/25/us/iowa-army-ammunition-blast.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="军方和民政当局表示，陆军的行动取得了成功。但检测工作将继续进行，以确保居民免受污染。" data-title="After Extraordinary Iowa Explosion, Officials and Scientists Assess Fallout Risks" data-date="11-26 05:17" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-26 05:17</span>
          <span class="news-item-title">爱荷华州发生罕见爆炸后，官员和科学家评估放射性尘埃风险</span>
          <span class="news-item-title-en">After Extraordinary Iowa Explosion, Officials and Scientists Assess Fallout Risks</span>
          <span class="news-value-point">💡 军方和民政当局表示，陆军的行动取得了成功</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/25/us/iowa-detonation-lead-what-next.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="官员们需要一些时间来检测空气、水和土壤样本是否受到污染。" data-title="Iowa Awaits All-Clear as Tests for Lead Continue" data-date="11-26 05:16" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-26 05:16</span>
          <span class="news-item-title">随着铅含量检测的继续进行，爱荷华州正等待全面解除警报</span>
          <span class="news-item-title-en">Iowa Awaits All-Clear as Tests for Lead Continue</span>
          <span class="news-value-point">💡 官员们需要一些时间来检测空气、水和土壤样本是否受到污染</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/peripherals/razer-china-partners-up-with-durex-for-a-limited-edition-kit-with-a-mousepad-and-condoms-long-lasting-battle-armor-meets-heavy-armored-beetle" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Razer中国与杜蕾斯合作推出限量版鼠标垫和避孕套套装——持久战斗盔甲邂逅重装甲虫" data-title="Razer China partners up with Durex for a limited-edition kit of mousepad and condoms" data-date="11-26 05:07" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-26 05:07</span>
          <span class="news-item-title">雷蛇中国与杜蕾斯合作推出限量版鼠标垫和避孕套套装</span>
          <span class="news-item-title-en">Razer China partners up with Durex for a limited-edition kit of mousepad and condoms</span>
          <span class="news-value-point">💡 Razer中国与杜蕾斯合作推出限量版鼠标垫和避孕套套装——持久战斗盔甲邂逅重装甲虫</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/peripherals/usb/best-usb-charger-and-power-bank-deals-for-black-friday-2026-from-tiny-single-port-smartphone-chargers-to-large-power-banks-for-laptops-weve-found-the-best-deals" target="_blank" rel="noopener" data-cat="zonghe" data-summary="从单端口15W充电器到25000mAh 220W移动电源，我们找到了一些超值优惠，让您的电子设备始终充满电，随时待命。" data-title="Best USB charger and power bank deals 2026" data-date="11-26 05:05" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-26 05:05</span>
          <span class="news-item-title">2026年USB充电器和充电宝超值优惠</span>
          <span class="news-item-title-en">Best USB charger and power bank deals 2026</span>
          <span class="news-value-point">💡 从单端口15W充电器到25000mAh 220W移动电源，我们找到了一些超值优惠，让您的电子设备始终充满电，随时待命</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1042532/whatsapp-scheduled-messages" target="_blank" rel="noopener" data-cat="zonghe" data-summary="WhatsApp的30亿用户将获得一项Meta称之为最受期待的功能之一，即能够提前为私人对话和群聊安排消息发送。大多数消息平台很早就有这项功能了。" data-title="WhatsApp’s new scheduled messages let you choose the right time to send" data-date="11-26 04:31" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-26 04:31</span>
          <span class="news-item-title">WhatsApp 的新定时消息功能让您选择合适的发送时间</span>
          <span class="news-item-title-en">WhatsApp’s new scheduled messages let you choose the right time to send</span>
          <span class="news-value-point">💡 WhatsApp的30亿用户将获得一项Meta称之为最受期待的功能之一，即能够提前为私人对话和群聊安排消息发送</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/speakers/save-up-to-36-percent-on-a-some-of-the-best-pc-speakers-weve-reviewed-deals-starting-at-just-usd26-from-audioengine-creative-edifier-and-more" target="_blank" rel="noopener" data-cat="zonghe" data-summary="我们在黑色星期五促销期间测试了一些最出色的电脑音箱，其中包括来自AudioEngine、创新和安桥的音箱。" data-title="Save up to 36% on a some of the best PC speakers we&#39;ve reviewed" data-date="11-26 04:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-26 04:30</span>
          <span class="news-item-title">我们评测过的一些顶级电脑音箱，现可享高达36%的优惠</span>
          <span class="news-item-title-en">Save up to 36% on a some of the best PC speakers we've reviewed</span>
          <span class="news-value-point">💡 我们在黑色星期五促销期间测试了一些最出色的电脑音箱，其中包括来自AudioEngine、创新和安桥的音箱</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/gift-guides-seasonal-sales/the-lowest-priced-ram-in-2026-price-tracking-on-ddr5-and-ddr4-memory-of-all-capacities" target="_blank" rel="noopener" data-cat="zonghe" data-summary="查看不同容量的 DDR5 和 DDR4 内存套件的最佳价格。" data-title="RAM price tracking 2026" data-date="11-26 04:09" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-26 04:09</span>
          <span class="news-item-title">2026 年内存价格跟踪</span>
          <span class="news-item-title-en">RAM price tracking 2026</span>
          <span class="news-value-point">💡 查看不同容量的 DDR5 和 DDR4 内存套件的最佳价格</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/boxing/news/12040/13614342/daniel-dubois-to-fight-joseph-parker-in-wbo-heavyweight-world-championship-clash-in-manchester-on-january-30" target="_blank" rel="noopener" data-cat="zonghe" data-summary="丹尼尔·杜布瓦将于 1 月 30 日在曼彻斯特的 Co-op Live 体育馆与约瑟夫·帕克争夺 WBO 重量级世界冠军头衔。" data-title="Dubois vs Parker announced for WBO heavyweight title clash" data-date="11-26 04:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 04:00</span>
          <span class="news-item-title">杜博瓦与帕克将争夺WBO重量级冠军头衔</span>
          <span class="news-item-title-en">Dubois vs Parker announced for WBO heavyweight title clash</span>
          <span class="news-value-point">💡 丹尼尔·杜布瓦将于 1 月 30 日在曼彻斯特的 Co-op Live 体育馆与约瑟夫·帕克争夺 WBO 重量级世界冠军头衔</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/science/1042109/us-army-detonation-lead-azide-explosives-iowa-ammunition-plant" target="_blank" rel="noopener" data-cat="zonghe" data-summary="美国陆军表示，为防止用于引爆器和雷管的材料储存发生自燃爆炸，今天在爱荷华州陆军弹药厂对超过9,700磅的叠氮化铅进行了受控引爆。" data-title="EPA reports ‘zero’ airborne lead following controlled Army detonation in Iowa" data-date="11-26 03:45" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-26 03:45</span>
          <span class="news-item-title">美国环保署报告称，在爱荷华州进行的陆军受控爆破后，空气中铅含量为“零”</span>
          <span class="news-item-title-en">EPA reports ‘zero’ airborne lead following controlled Army detonation in Iowa</span>
          <span class="news-value-point">💡 美国陆军表示，为防止用于引爆器和雷管的材料储存发生自燃爆炸，今天在爱荷华州陆军弹药厂对超过9,700磅的叠氮化铅进行了受控引爆</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1042409/1password-data-breach-leak" target="_blank" rel="noopener" data-cat="zonghe" data-summary="1Password表示，黑客在获得其后端系统的访问权限后窃取了客户姓名和电子邮件地址。据称，此次数据泄露并未导致存储在客户保管库中的密码或其他信息被泄露，但可能会让用户面临网络钓鱼攻击的风险。" data-title="1Password breach leaked customer names and emails, but not passwords" data-date="11-26 03:10" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-26 03:10</span>
          <span class="news-item-title">1Password 数据泄露事件导致客户姓名和电子邮件地址泄露，但未泄露密码</span>
          <span class="news-item-title-en">1Password breach leaked customer names and emails, but not passwords</span>
          <span class="news-value-point">💡 1Password表示，黑客在获得其后端系统的访问权限后窃取了客户姓名和电子邮件地址</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/monitors/gaming-monitors/here-are-the-best-oled-gaming-monitor-deals-you-can-snag-for-black-friday-beautiful-monitors-up-to-39-percent-off" target="_blank" rel="noopener" data-cat="zonghe" data-summary="OLED游戏显示器目前非常热门，黑色星期五是入手的绝佳时机。" data-title="Here are the best OLED gaming monitor deals you can snag for Black Friday 2026" data-date="11-26 03:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-26 03:00</span>
          <span class="news-item-title">以下是您在2026年黑色星期五可以抢购的最佳OLED游戏显示器优惠</span>
          <span class="news-item-title-en">Here are the best OLED gaming monitor deals you can snag for Black Friday 2026</span>
          <span class="news-value-point">💡 OLED游戏显示器目前非常热门，黑色星期五是入手的绝佳时机</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/networking/routers/save-on-a-budget-router-with-prices-starting-at-just-usd39-tp-link-archer-ax1450-and-netgear-rax5-wi-fi-6-routers-go-on-low-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="TP-Link Archer AX1450现价仅为39美元" data-title="Save on a budget router with prices starting at just $39 — TP-Link Archer AX1450 and Netgear RAX5 Wi-Fi 6 routers go on low sale" data-date="11-26 02:54" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-26 02:54</span>
          <span class="news-item-title">超值优惠路由器，价格低至 39 美元起——TP-Link Archer AX1450 和 Netgear RAX5 Wi-Fi 6 路由器特价促销</span>
          <span class="news-item-title-en">Save on a budget router with prices starting at just $39 — TP-Link Archer AX1450 and Netgear RAX5 Wi-Fi 6 routers go on low sale</span>
          <span class="news-value-point">💡 TP-Link Archer AX1450现价仅为39美元</span>
        </a>
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
  </div>
</div>
<script defer src="{{ "/assets/js/news-feed.js" | relative_url }}"></script>


<p class="news-updated">🕐 抓取更新于 2026-11-26 05:52（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
