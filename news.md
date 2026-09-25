---
layout: default
title: 热点新闻
---

<div class="news-header-box">
  <div class="news-title-row">
    <div>
      <h1 class="news-main-title">📰 热点新闻速览</h1>
      <p class="news-main-desc">每日聚合全球英超足球、前沿科技与国际时政焦点（电脑端悬浮即览深度特稿 · 手机端自适应浏览）</p>
    </div>
    <div class="news-date-tag">
      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
      <span>2026-09-25 14:46 抓取更新</span>
    </div>
  </div>

  <div class="news-search-bar">
    <svg class="news-search-icon" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
    <input type="text" id="news-search-input" class="news-search-input" placeholder="🔍 实时搜索今日全天新闻（输入关键词、球队、公司、人物、信源）..." oninput="onNewsSearch(this.value)">
    <span id="news-search-count" class="news-search-count"></span>
  </div>

  <div class="news-nav-composite">
    <div class="news-channel-bar">
      <button class="channel-btn active" onclick="filterNewsChannel('all', this)">
        <span>🌟 全部动态</span>
        <span class="channel-count">53</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('shizheng', this)">
        <span>🏛️ 时政与国际</span>
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('keji', this)">
        <span>🤖 AI模型 & 芯片算力</span>
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('zuqiu', this)">
        <span>⚽ 英超与足球风云</span>
        <span class="channel-count">7</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('zonghe', this)">
        <span>📰 综合与社会</span>
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('meimei', this)">
        <span>🌍 西方媒体视角</span>
        <span class="channel-count">1</span>
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
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.nytimes.com/2026/09/24/us/politics/trump-xi-state-dinner-menu.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="白宫表示，包括海鲈鱼和白菜在内的三道菜菜单以美国食材为特色，具有“微妙的中国影响”。" data-title="在特朗普主持纪念习近平的国宴之际，请参阅菜单" data-date="09-25 14:41" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 09-25 14:41</span>
      </div>
      <h2 class="hero-featured-title">在特朗普主持纪念习近平的国宴之际，请参阅菜单</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/007/137.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 25 日消息，海贝本周三发布了 RS2 便携无损音乐播放器，标准版（铝合金 / 墨绿色）定价 2798 元，限量版（黄铜） 3498 元。据介绍，这款播放器采用旗舰型号 RS8 二代同款第三代达尔文架构 (DARWIN III)，由 HiBy 全程自主研发，重构底层核心处理架构，重塑高清音频处理全流程。第三代达尔文架构采用全新 FPGA 数字引擎，逻辑单元数量突破 35K，拥有 40 个高速、高性能 DSP，为可调纯 FIR 滤波算法、多样 DARWIN 滤波器、谐波控制器等特色功能提供强大算力基础，实现全柔性架构、全流程自主可控。第三代达尔文架构配备两颗飞秒级低相噪音频专用晶振，分别为 45.158MHz、 49.152MHz，可有效降低相位噪声以及时钟抖动，低至 -14" data-title="海贝 RS2 音乐播放器发售：R2R 技术达尔文三代架构，2798 元起" data-date="09-25 14:43" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">海贝 RS2 音乐播放器发售：R2R 技术达尔文三代架构，2798 元起</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/ckeq8vq7rwe7o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育频道探讨了为什么英格兰足球顶级俱乐部越来越多地交易学院球员，以及对年轻人本身的影响。" data-title="为什么青少年已经成为足球转会市场的重要组成部分" data-date="09-25 14:32" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">为什么青少年已经成为足球转会市场的重要组成部分</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/007/135.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 25 日消息，据央视新闻报道，24 日，民航局相关负责人表示，中秋、国庆假期也是民航旅客出行的高峰，环线游、出境游增速非常明显。假日出行还呈现出去程渐次达峰、回程集中抵离的特点。民航的旅客量有望再创历史同期新高。中国民航局副局长马兵表示，整体来看，从 9 月 25 日到 10 月 7 日，全国民航预计运输旅客量 3119 万人次，日均 240 万人次，增长率 3.6%。单日峰值有望突破 260 万人次，超过去年同期水平。据介绍，大城市航空客流保持高位，特色旅游城市客流快速增长。十大航空枢纽（IT之家注：中国民航 10 个国际航空枢纽为北京、上海、广州、成都、昆明、深圳、重庆、西安、乌鲁木齐、哈尔滨）目前日均机票预订量已超过了 49 万张，同比增长了 3.9%。截至目前，“双" data-title="日均 240 万人次，中秋、国庆假期民航旅客量有望再创同期新高" data-date="09-25 14:31" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">日均 240 万人次，中秋、国庆假期民航旅客量有望再创同期新高</p>
    </a>
  </div>
</div>
<div class="news-grid">
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🏛️</span>
      <span class="news-category-title">时政要闻 & 国际动态</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/09/24/us/politics/trump-xi-state-dinner-menu.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="白宫表示，包括海鲈鱼和白菜在内的三道菜菜单以美国食材为特色，具有“微妙的中国影响”。" data-title="在特朗普主持纪念习近平的国宴之际，请参阅菜单" data-date="09-25 14:41" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-25 14:41</span>
          <span class="news-item-title">在特朗普主持纪念习近平的国宴之际，请参阅菜单</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-25/10703664.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间9月24日晚，国家主席习近平和夫人彭丽媛在白宫出席美国总统特朗普和夫人梅拉尼娅举行的欢迎宴会。习近平主席发表致辞。他指出——" data-title="习言道｜中美关系又站在新的历史起点上" data-date="09-25 13:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-25 13:43</span>
          <span class="news-item-title">习言道｜中美关系又站在新的历史起点上</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-25/10703647.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网成都9月25日电 (记者 岳依桐)由马来西亚国会上议院副议长努尔·贾兹兰为团长，17国国际和平组织与安全智库领导人组成的研修班一行25日结束了对四川为期4天的访问。" data-title="17国研修班结束四川访问 盼深化交流合作" data-date="09-25 13:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-25 13:41</span>
          <span class="news-item-title">17国研修班结束四川访问 盼深化交流合作</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-25/10703669.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间9月24日晚，国家主席习近平和夫人彭丽媛出席美国总统特朗普和夫人梅拉尼娅在白宫举行的欢迎宴会。习近平在祝酒辞中说——" data-title="习近平：共同浇灌中美友谊的美丽花朵" data-date="09-25 13:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-25 13:33</span>
          <span class="news-item-title">习近平：共同浇灌中美友谊的美丽花朵</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-25/10703633.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社纽约9月24日电 当地时间9月24日，中国国家副主席韩正在纽约出席联合国大会期间会见保加利亚总统约托娃。" data-title="韩正会见保加利亚总统约托娃" data-date="09-25 13:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-25 13:32</span>
          <span class="news-item-title">韩正会见保加利亚总统约托娃</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-25/10703631.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社纽约9月24日电 当地时间9月24日，中国国家副主席韩正在纽约出席联合国大会期间会见塞尔维亚总统武契奇。" data-title="韩正会见塞尔维亚总统武契奇" data-date="09-25 13:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-25 13:32</span>
          <span class="news-item-title">韩正会见塞尔维亚总统武契奇</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c3qjkx1wdyyxo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="从红杉木长椅到DVD，馈赠礼物一直是外交艺术的重要一环。" data-title="为何特朗普在国宴上送习近平一座华丽的白头海雕雕像？" data-date="09-25 12:56" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-25 12:56</span>
          <span class="news-item-title">为何特朗普在国宴上送习近平一座华丽的白头海雕雕像？</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-25/10703651.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社华盛顿9月24日电 题：走进美国希望中文学校：做美中文化民间交流的桥梁" data-title="走进美国希望中文学校：做美中文化民间交流的桥梁" data-date="09-25 12:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-25 12:42</span>
          <span class="news-item-title">走进美国希望中文学校：做美中文化民间交流的桥梁</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-25/10703632.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社华盛顿9月24日电 (记者 郭金超 黄钰钦 郭超凯)当地时间9月24日晚，美国总统特朗普和夫人梅拉尼娅为中国国家主席习近平和夫人彭丽媛在白宫举行欢迎国宴。" data-title="习近平和彭丽媛出席特朗普总统夫妇举行的欢迎国宴" data-date="09-25 12:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-25 12:40</span>
          <span class="news-item-title">习近平和彭丽媛出席特朗普总统夫妇举行的欢迎国宴</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-25/10703635.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网悉尼9月25日电 中国驻墨尔本总领馆近日举行庆祝中华人民共和国成立77周年招待会。" data-title="中国驻墨尔本总领馆举办庆祝中华人民共和国成立77周年招待会" data-date="09-25 12:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-25 12:39</span>
          <span class="news-item-title">中国驻墨尔本总领馆举办庆祝中华人民共和国成立77周年招待会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-25/10703614.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月25日电 综合消息：也门胡塞武装方面当地时间24日表示，该组织武装部队对沙特阿拉伯首都利雅得一处“敏感地点”、西部城市延布的沙特阿美石油公司设施，以及西南部吉赞地区多处军事目标发动袭击。" data-title="也门胡塞武装称袭击沙特多地目标" data-date="09-25 12:38" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-25 12:38</span>
          <span class="news-item-title">也门胡塞武装称袭击沙特多地目标</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/24/us/politics/trump-xi-summit-china.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="随着中国国家主席习近平十多年来首次访问白宫，特朗普总统推出了他个人的外交品牌。" data-title="特朗普和习近平在美国的飞越和熊猫掩盖了分歧" data-date="09-25 11:10" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-25 11:10</span>
          <span class="news-item-title">特朗普和习近平在美国的飞越和熊猫掩盖了分歧</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-25/10703567.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网布鲁塞尔9月25日电 (记者 德永健)案发3年半后，比利时知名艺术品收藏家米莉亚姆·尤伦斯遭枪杀案24日开审，嫌疑人米莉亚姆·尤伦斯的继子尼古拉·尤伦斯将接受法庭审判。" data-title="比利时知名艺术品收藏家“尤伦斯夫人”遭枪杀案开审" data-date="09-25 09:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-25 09:13</span>
          <span class="news-item-title">比利时知名艺术品收藏家“尤伦斯夫人”遭枪杀案开审</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/24/nyregion/un-protest-netanyahu-israel-gaza.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="Large groups gathered in Midtown Manhattan to demonstrate as the Israeli prime minister spoke to the General Assembly." data-title="About 100 Are Arrested in Protests Against Netanyahu" data-date="09-25 08:03" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-25 08:03</span>
          <span class="news-item-title">About 100 Are Arrested in Protests Against Netanyahu</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cqpvew870ezko/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="有分析人士表示，峰会至今主要着眼于营造“正面气氛”，但仍有多项迫切议题有待讨论。" data-title="习近平访美排场十足，但迄今进展甚微" data-date="09-25 07:51" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-25 07:51</span>
          <span class="news-item-title">习近平访美排场十足，但迄今进展甚微</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/007/137.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 25 日消息，海贝本周三发布了 RS2 便携无损音乐播放器，标准版（铝合金 / 墨绿色）定价 2798 元，限量版（黄铜） 3498 元。据介绍，这款播放器采用旗舰型号 RS8 二代同款第三代达尔文架构 (DARWIN III)，由 HiBy 全程自主研发，重构底层核心处理架构，重塑高清音频处理全流程。第三代达尔文架构采用全新 FPGA 数字引擎，逻辑单元数量突破 35K，拥有 40 个高速、高性能 DSP，为可调纯 FIR 滤波算法、多样 DARWIN 滤波器、谐波控制器等特色功能提供强大算力基础，实现全柔性架构、全流程自主可控。第三代达尔文架构配备两颗飞秒级低相噪音频专用晶振，分别为 45.158MHz、 49.152MHz，可有效降低相位噪声以及时钟抖动，低至 -14" data-title="海贝 RS2 音乐播放器发售：R2R 技术达尔文三代架构，2798 元起" data-date="09-25 14:43" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-25 14:43</span>
          <span class="news-item-title">海贝 RS2 音乐播放器发售：R2R 技术达尔文三代架构，2798 元起</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-25/10703709.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="日本政府及执政党相关人士近日透露，日本政府已着手探讨启动将人形机器人用于防卫领域的相关研究。详情显示，日本政府计划年底修改“安保三文件”，全面运用人工智能(AI)将成为强化防卫力的核心。" data-title="“温水煮青蛙” 日本渐进式布局军用AI暗藏多重风险" data-date="09-25 14:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-25 14:26</span>
          <span class="news-item-title">“温水煮青蛙” 日本渐进式布局军用AI暗藏多重风险</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c5zjzl8n2epxo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="多名美国科技和金融界巨头有份出席，部分人士更与两国领导人同桌。但近日高调警告人工智能风险的企业Anthropic代表未有出席。" data-title="习近平访美：白宫国宴谁出席、谁缺席？意味了什么？" data-date="09-25 14:00" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-25 14:00</span>
          <span class="news-item-title">习近平访美：白宫国宴谁出席、谁缺席？意味了什么？</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/497012.html" target="_blank" rel="noopener" data-cat="keji" data-summary="给机器人当老师，还能赚外快？“中国版Index”觅蜂派来了" data-title="给机器人当老师，还能赚外快？“中国版Index”觅蜂派来了" data-date="09-25 13:52" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-25 13:52</span>
          <span class="news-item-title">给机器人当老师，还能赚外快？“中国版Index”觅蜂派来了</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1000495/microsoft-is-killing-off-the-copilot-plus-pc-brand" target="_blank" rel="noopener" data-cat="keji" data-summary="还记得微软希望每个人都知道“Copilot Plus PC”是可以获得的，因为这些PC具有足够的内置AI功能来完成任务？两年半后，微软和高通似乎承认该品牌已经死亡。Windows Central的Zac Bowden报告[…]" data-title="微软正在淘汰“Copilot Plus PC”品牌" data-date="09-25 09:25" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-25 09:25</span>
          <span class="news-item-title">微软正在淘汰“Copilot Plus PC”品牌</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/24/nyregion/netanyahu-mamdani-un-speech.html" target="_blank" rel="noopener" data-cat="keji" data-summary="The Israeli prime minister accused Mayor Zohran Mamdani, an outspoken critic of Israel, of antisemitism. The mayor has become a political foil for the prime minister." data-title="马姆达尼指责内塔尼亚胡在联合国演讲后散布“毫无根据的谎言”" data-date="09-25 08:57" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-25 08:57</span>
          <span class="news-item-title">马姆达尼指责内塔尼亚胡在联合国演讲后散布“毫无根据的谎言”</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/24/world/middleeast/netanyahu-israel-un.html" target="_blank" rel="noopener" data-cat="keji" data-summary="总理本雅明·内塔尼亚胡（ Benjamin Netanyahu ）也对接待他的市长佐赫兰·马姆达尼（ Zohran Mamdani ）感到愤怒。" data-title="内塔尼亚胡在联合国发言时谴责以色列的批评者是“道德懦夫”" data-date="09-25 08:40" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-25 08:40</span>
          <span class="news-item-title">内塔尼亚胡在联合国发言时谴责以色列的批评者是“道德懦夫”</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/australian-pm-says-openai-took-84-days-to-email-agency-after-agent-hacked-its-national-health-care-portal-incident-is-believed-to-be-the-first-known-case-of-ai-breaching-a-government-site" target="_blank" rel="noopener" data-cat="keji" data-summary="澳大利亚表示， OpenAI代理商在6月份通过了Medicare统计门户网站的屏蔽。OpenAI的通知于9月到达。" data-title="OpenAI专员进入澳大利亚的Medicare STATS门户网站，通知延迟了84天" data-date="09-25 04:34" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-25 04:34</span>
          <span class="news-item-title">OpenAI专员进入澳大利亚的Medicare STATS门户网站，通知延迟了84天</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1000328/google-gemini-ai-live-avatar-face" target="_blank" rel="noopener" data-cat="keji" data-summary="谷歌的新Gemini 3.8实时更新允许用户在观看动画AI角色实时响应的同时与模型进行对话。“Live Avatar”将在对话期间同步并显示不同的面部表情，但目前仅适用于Gemini Enterprise客户。正如谷歌所指出的， Live Avatar可以在97 […]之间转换" data-title="Gemini 3.8 Live with Live Avatar为谷歌的人工智能提供了一张脸" data-date="09-25 03:59" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-25 03:59</span>
          <span class="news-item-title">Gemini 3.8 Live with Live Avatar为谷歌的人工智能提供了一张脸</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/24/prismml-brings-its-tiny-llms-to-qualcomm-powered-smart-glasses/" target="_blank" rel="noopener" data-cat="keji" data-summary="Prism更大的目标是在设备上运行的开放式人工智能，并更好地利用他们已经拥有的计算能力。" data-title="PrismML将其微小的LLM带入高通驱动的智能眼镜" data-date="09-25 03:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-25 03:00</span>
          <span class="news-item-title">PrismML将其微小的LLM带入高通驱动的智能眼镜</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1000122/cyberpowerpc-gaming-prebuilt-rtx-5070-core-i7-asrock-oled-monitor-deal-sale" target="_blank" rel="noopener" data-cat="keji" data-summary="虽然PC组件价格仍然很高，但通过购买预建的台式机，您可以在系统上节省大量资金。沃尔玛有一台设备齐全的CyberPowerPC游戏PC ，售价为1,549美元，比原价2,139美元低近600美元。它由英特尔酷睿i7-14700KF处理器提供动力，并与32GB的6000MHz […]" data-title="遗憾的是，这款配备$ 1,549 RTX 5070的游戏电脑非常划算" data-date="09-25 02:19" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-25 02:19</span>
          <span class="news-item-title">遗憾的是，这款配备$ 1,549 RTX 5070的游戏电脑非常划算</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1000140/jensen-huang-nvidia-ai-energy-climate-change-supervillain" target="_blank" rel="noopener" data-cat="keji" data-summary="正如Jensen Huang所说，人工智能可以帮助应对气候变化--但前提是它首先造成“巨大的痛苦和苦难”。这位英伟达首席执行官在最新一期的《以斯拉·克莱因秀》中讨论了能源的未来和人工智能对我们星球的影响。但他的评论可以归结为[…]" data-title="Jensen Huang像超级恶棍一样谈论人工智能和气候变化" data-date="09-25 02:04" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-25 02:04</span>
          <span class="news-item-title">Jensen Huang像超级恶棍一样谈论人工智能和气候变化</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1000222/meta-muse-ai-filesystem" target="_blank" rel="noopener" data-cat="keji" data-summary="一对开发人员表示，在很少提示的情况下， Meta的Muse将与您共享其整个文件系统。彼得·詹姆斯（ Peter James ）和乔尼·桑德斯（ Jonny L. Saunders ）表示，他们都独立地诱使Muse压缩并共享其根文件系统、Ubuntu系统文件、应用程序模板和内部文档的全部内容。桑德斯于[…]发布" data-title="Muse显然会让您下载其整个文件系统" data-date="09-25 01:14" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-25 01:14</span>
          <span class="news-item-title">Muse显然会让您下载其整个文件系统</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/report/1000180/muse-openclaw-instinct-lookalike" target="_blank" rel="noopener" data-cat="keji" data-summary="我们似乎正在进入人工智能特工的复兴。据Apptopia估计， Meta新的面向消费者的人工智能代理商Muse在发布后不久就登上了App Store排行榜的榜首，并在美国拥有60万日活跃用户。而人工智能代理平台Instinct ，其同名创作者正在以25亿美元的估值筹集资金，已经[…]" data-title="Muse看起来很像OpenClaw" data-date="09-25 01:10" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-25 01:10</span>
          <span class="news-item-title">Muse看起来很像OpenClaw</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/24/google-photos-clueless-inspired-virtual-closet-is-now-available-on-android-and-ios/" target="_blank" rel="noopener" data-cat="keji" data-summary="人工智能功能从您的照片中构建了一个虚拟衣柜，在6月首次向Android用户推出后，现在可以广泛使用。" data-title="Google相册“Clueless”风格的虚拟衣柜现已在Android和iOS上推出" data-date="09-25 01:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-25 01:00</span>
          <span class="news-item-title">Google相册“Clueless”风格的虚拟衣柜现已在Android和iOS上推出</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">7 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ckeq8vq7rwe7o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育频道探讨了为什么英格兰足球顶级俱乐部越来越多地交易学院球员，以及对年轻人本身的影响。" data-title="为什么青少年已经成为足球转会市场的重要组成部分" data-date="09-25 14:32" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-25 14:32</span>
          <span class="news-item-title">为什么青少年已经成为足球转会市场的重要组成部分</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-25/10703636.shtml" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="中新网北京9月25日电 (记者 徐婧)第四届北京国际运河艺术周24日开幕。活动开展文艺演出、主题市集、多地快闪等，联动德国多特蒙德-埃姆斯运河、罗马尼亚多瑙-黑海运河等全球13条运河，让古老运河焕发时代新貌。" data-title="联动全球13条运河 第四届北京国际运河艺术周开幕" data-date="09-25 13:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-25 13:32</span>
          <span class="news-item-title">联动全球13条运河 第四届北京国际运河艺术周开幕</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmx2zv4e320do?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联证实，自6月30日以来，他们又借了9000万£ ，使他们的总债务超过11亿£。" data-title="曼联再借入9000万£ ，债务超过11亿£" data-date="09-25 06:22" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-25 06:22</span>
          <span class="news-item-title">曼联再借入9000万£ ，债务超过11亿£</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c639merx84jno?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="欧足联认为，由于今年夏天英超俱乐部的巨额支出， “明确的双速系统”正在转会市场出现。" data-title="欧足联担心英超联赛支出对转会市场的影响" data-date="09-25 06:09" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-25 06:09</span>
          <span class="news-item-title">欧足联担心英超联赛支出对转会市场的影响</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmly4qkly434o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英超联赛希望“尽快”与EFL就其资助模式达成协议。" data-title="英超热衷于解决EFL资金僵局" data-date="09-25 01:52" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-25 01:52</span>
          <span class="news-item-title">英超热衷于解决EFL资金僵局</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/sport/2026/sep/24/arsenal-brighton-premier-league-questions" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="本周，我们将围绕英超联赛周末最令人惊讶的结果深入探讨重大问题。在上个周末之前，阿森纳自4月以来没有在英超联赛中输过。连续九场联赛的胜利足以在上赛季结束时加冕枪手为冠军，并坚定地确立他们为本赛季初击败的球队。尽管如此，周六再次击败布莱顿，要击败的球队被击败了。彻底。继续rea" data-title="阿森纳被发现了吗？布莱顿沮丧之后的三大问题" data-date="09-24 18:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-24 18:00</span>
          <span class="news-item-title">阿森纳被发现了吗？布莱顿沮丧之后的三大问题</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cm1wx51gyly5o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育频道进入曼城的数据团队，该团队在过去18个月中一直是其重建工作的关键部分。" data-title="曼城如何彻底改造他们的球队，从65万" data-date="09-24 17:31" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-24 17:31</span>
          <span class="news-item-title">曼城如何彻底改造他们的球队，从65万</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/007/135.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 25 日消息，据央视新闻报道，24 日，民航局相关负责人表示，中秋、国庆假期也是民航旅客出行的高峰，环线游、出境游增速非常明显。假日出行还呈现出去程渐次达峰、回程集中抵离的特点。民航的旅客量有望再创历史同期新高。中国民航局副局长马兵表示，整体来看，从 9 月 25 日到 10 月 7 日，全国民航预计运输旅客量 3119 万人次，日均 240 万人次，增长率 3.6%。单日峰值有望突破 260 万人次，超过去年同期水平。据介绍，大城市航空客流保持高位，特色旅游城市客流快速增长。十大航空枢纽（IT之家注：中国民航 10 个国际航空枢纽为北京、上海、广州、成都、昆明、深圳、重庆、西安、乌鲁木齐、哈尔滨）目前日均机票预订量已超过了 49 万张，同比增长了 3.9%。截至目前，“双" data-title="日均 240 万人次，中秋、国庆假期民航旅客量有望再创同期新高" data-date="09-25 14:31" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-25 14:31</span>
          <span class="news-item-title">日均 240 万人次，中秋、国庆假期民航旅客量有望再创同期新高</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/007/134.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 25 日消息，北京驭风飞行科技有限公司宣布，全球首台全天候浮空器 —— 云哨 M1000-CNS 首发仪式于 9 月 22 日在四川自贡荣县云哨浮空器产教融合总部基地举行。这一可连续驻空五年、通导监气一体化的空基平台直径 21 米、总长 24 米，集成风电、光伏与储能一体化供电系统，能够抵御风雨、冰雪、雷电等复杂天气条件，具备全天候作业能力。与传统柔式浮空器不同，该产品将柔性升力体蒙皮与刚性载荷舱、能源及系留系统进行一体化承载与姿态控制，外蒙皮仅负责耐耗，内部设置多个浮力囊体负责气密，从而降低了整体制造成本。IT之家注：浮空器是指利用轻于空气的气体提供升力、可长时间驻留空中的飞行器，常见形式包括系留气球和飞艇。驭风飞行董事长兼 CEO 史智广在现场介绍称，云哨 M1000-" data-title="全球首台全天候浮空器在川首发：可连续驻空五年，覆盖面积约 2000 平方公里" data-date="09-25 14:31" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-25 14:31</span>
          <span class="news-item-title">全球首台全天候浮空器在川首发：可连续驻空五年，覆盖面积约 2000 平方公里</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/007/133.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 25 日消息，蔚来今日宣布，蔚来“Cedar S 雪松”智能系统 1.6.0 版本已全量推送。为 ES6、EC6、ET5、ET5T 带来全维度智能的智能座舱、更全能的得力助手 NOMI、专属驾乘体验、智能辅助驾驶四大板块，超 30 项功能体验新增与升级。IT之家附本次更新内容如下：中控屏交互体验新增桌面随挡位自动切换：P 挡进入艺境桌面，D 挡进入地图桌面手势切换主题：支持五指抓握屏幕手势，便捷进入艺境主题切换页优化无限画布布局：进入后保留底部导航栏底部导航栏自定义：优化操作交互快捷控制卡片交互：点击儿童座椅卡片可直跳对应设置页HUD 交互体验新增HUD 极简模式：仅保留车速、限速、车道指引等核心信息，支持显示转向盲点影像挡位数值直观显示：调节高度与角度时实时显示挡位数值地" data-title="蔚来“Cedar S 雪松”智能系统 1.6.0 版本全量推送，智能座舱、NOMI、驾乘体验、辅助驾驶升级" data-date="09-25 14:24" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-25 14:24</span>
          <span class="news-item-title">蔚来“Cedar S 雪松”智能系统 1.6.0 版本全量推送，智能座舱、NOMI、驾乘体验、辅助驾驶升级</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/007/132.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 25 日消息，国铁集团今日宣布，哈尔滨至伊春高速铁路将于 9 月 28 日开通运营。IT之家注意到，相关车次已上架铁路 12306，但目前处于暂停发售状态。哈伊高铁开通后，哈尔滨至伊春间最快 1 小时 46 分钟可达，绥化、伊春等地市接入全国高铁网。为满足旅客不同出行需求，铁路部门在哈伊高铁实施灵活折扣、差异化的市场化票价机制，为旅客出行提供更多选择，具体票价可通过铁路 12306 查询。哈伊高铁起自哈尔滨站，途经黑龙江省哈尔滨市、绥化市、铁力市，终至伊春市，线路全长 318 公里，设计时速 250 公里。全线共设哈尔滨、哈尔滨北、呼兰北、兴隆镇西、绥化南、庆安南、铁力、日月峡、伊春西 9 座车站。其中哈尔滨站、哈尔滨北站为既有车站，铁力站为既有车站改建站，其余均为新建车站" data-title="哈伊高铁 9 月 28 日开通运营：哈尔滨至伊春最快 1 小时 46 分钟，实施市场化票价机制" data-date="09-25 14:16" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-25 14:16</span>
          <span class="news-item-title">哈伊高铁 9 月 28 日开通运营：哈尔滨至伊春最快 1 小时 46 分钟，实施市场化票价机制</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-25/10703705.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="记者从国铁集团获悉，哈尔滨至伊春高速铁路(以下简称哈伊高铁)将于9月28日开通运营，哈尔滨至伊春间最快1小时46分钟可达，绥化、伊春等地市接入全国高铁网，为新时代东北全面振兴注入新动能。" data-title="哈尔滨至伊春高铁9月28日开通运营 将实施市场化票价机制" data-date="09-25 14:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-25 14:16</span>
          <span class="news-item-title">哈尔滨至伊春高铁9月28日开通运营 将实施市场化票价机制</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/007/131.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 25 日消息，科技媒体 Android Authority 今天（9 月 25 日）发布博文，报道称谷歌调整网页版 Gmail 的星标和“重要”标记，默认统一变成蓝色，这引发了用户的广泛抱怨。谷歌于 9 月 17 日通过 X 平台发布推文，表示为了符合现代无障碍标准，将默认的星标和“重要”标签颜色从黄色更新为蓝色。此项更改确保收件箱更清晰、更易读，并且对所有人都更友好。IT之家附上相关图片如下：报道指出 Gmail 长期使用黄色图标，帮助用户快速识别邮件状态。本次更新将默认黄色星标和黄色重要性箭头，均改为高饱和度蓝色，引发不少用户吐槽。部分用户认为，相同的饱和蓝色削弱了收件箱的视觉层级。用户还表示，新图标在邮件列表中更加醒目，增加了界面杂乱感。谷歌暂未提供恢复经典黄色配色的" data-title="谷歌网页版 Gmail 星标和“重要”标签默认设为蓝色，用户抱怨导致收件箱杂乱无章" data-date="09-25 14:15" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-25 14:15</span>
          <span class="news-item-title">谷歌网页版 Gmail 星标和“重要”标签默认设为蓝色，用户抱怨导致收件箱杂乱无章</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-25/10703663.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网丽水9月25日电(黄彦君)瓯江流淌，青山如黛，入秋的浙江省丽水市莲都区古堰画乡，宛如一幅风景画。" data-title="瓯江之畔，浙江丽水“巴比松”探讨数字时代“新可能”" data-date="09-25 13:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-25 13:55</span>
          <span class="news-item-title">瓯江之畔，浙江丽水“巴比松”探讨数字时代“新可能”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-25/10703650.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网抚顺9月25日电 “传承红色薪火，争做党和人民的红孩子”主题汇报展示暨“青少年党史学习月”推进会近日在抚顺市雷锋纪念馆雷锋讲坛隆重举行。" data-title="辽宁抚顺举办主题活动传承红色薪火" data-date="09-25 13:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-25 13:50</span>
          <span class="news-item-title">辽宁抚顺举办主题活动传承红色薪火</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-25/10703690.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="铁路中秋国庆假期运输9月23日启动，至10月8日结束，为期16天，全国铁路预计发送旅客2.84亿人次，日均计划开行旅客列车约1.3万列，10月1日将迎来客流最高峰。" data-title="通途畅行，满载“欣悦”赴远方" data-date="09-25 13:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-25 13:49</span>
          <span class="news-item-title">通途畅行，满载“欣悦”赴远方</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-25/10703670.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网杭州9月25日电 题：五千年良渚古城里的“共建”故事" data-title="五千年良渚古城里的“共建”故事" data-date="09-25 13:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-25 13:32</span>
          <span class="news-item-title">五千年良渚古城里的“共建”故事</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/24/world/middleeast/iran-proposal.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Under the offer, the Strait of Hormuz would reopen and nuclear talks would be revived." data-title="Iran Proposes 7" data-date="09-25 13:27" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-25 13:27</span>
          <span class="news-item-title">Iran Proposes 7</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cqx2z782j7y7o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="倡议人士希望，这些新词语能减少对身体的羞辱，并推动更正向的性观念。" data-title="“让女性感到被看见”：为何荷兰人为阴唇创造了一个新词？" data-date="09-25 08:03" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-25 08:03</span>
          <span class="news-item-title">“让女性感到被看见”：为何荷兰人为阴唇创造了一个新词？</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1000370/meta-instagram-attorney-client-privilege-hats" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Meta的律师辩称，在针对涉嫌伤害青少年安全和心理健康的诉讼中，以律师-客户特权为由，某些证据应从公众视野中隐瞒。起诉该公司的律师本周表示，该标签的适用范围过于广泛，同时指出最近未密封的文件[…]" data-title="Meta员工在打击儿童安全披露的同时订购了“律师/客户特权”帽子" data-date="09-25 07:50" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-25 07:50</span>
          <span class="news-item-title">Meta员工在打击儿童安全披露的同时订购了“律师/客户特权”帽子</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1000443/qualcomms-new-elite-sound-chip-might-finally-deliver-the-wi-fi-earbud-dream" target="_blank" rel="noopener" data-cat="zonghe" data-summary="如果您的无线耳机（或音频眼镜）可以传输高质量的无损音频，而当您将手机放在床边充电器上或埋在沙发上时，这些音频不会中断，该怎么办？高通公司的新款Snapdragon Sound Elite Gen 2是其首款将“微功率Wi-Fi 6E”直接集成到芯片中的产品，因此它们可以[…]" data-title="高通公司的新“Elite”声音芯片可能最终提供Wi" data-date="09-25 07:42" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-25 07:42</span>
          <span class="news-item-title">高通公司的新“Elite”声音芯片可能最终提供Wi</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/news/1000374/microsoft-comms-pr-brad-smith-cela" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Microsoft正在将其通信部门从营销部门转移到公司、外部和法律事务(CELA)部门。出人意料的变化是，微软副董事长兼总裁布拉德·史密斯（ Brad Smith ）将负责通信，而该公司正在寻找首席通信官弗兰克·肖（ Frank Shaw ）的替代人选，后者将于今年晚些时候离微软首席执行官Satya […]" data-title="微软让布拉德·史密斯负责沟通" data-date="09-25 06:08" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-25 06:08</span>
          <span class="news-item-title">微软让布拉德·史密斯负责沟通</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🌍</span>
      <span class="news-category-title">西方媒体视角 (外媒看中国 · 奇葩言论集锦)</span>
      <span class="news-category-count">1 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/09/24/us/politics/trump-xi-press-pool-boycott-media.html" target="_blank" rel="noopener" data-cat="meimei" data-summary="特朗普总统部分媒体禁令的摊牌在他欢迎习近平主席的同时进行，习近平政府是世界上最具压制性的政府之一。" data-title="在特朗普的白宫，中国的独裁者受到欢迎。美国媒体，不是这样。" data-date="09-25 08:38" data-source="纽约时报">
          <span class="news-cat-tag cat-meimei">🌍 外媒视角</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-25 08:38</span>
          <span class="news-item-title">在特朗普的白宫，中国的独裁者受到欢迎。美国媒体，不是这样。</span>
        </a>
  </div>
</div>

<script>
const NEWS_COLLAPSE_LIMIT = 10;

function applyNewsCollapse(forceExpand) {
  document.querySelectorAll('.news-category').forEach(cat => {
    const items = cat.querySelectorAll('.news-item');
    let btn = cat.querySelector('.news-expand-btn');
    if (items.length <= NEWS_COLLAPSE_LIMIT) {
      cat.removeAttribute('data-collapse');
      if (btn) btn.remove();
      return;
    }
    if (!btn) {
      btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'news-expand-btn';
      cat.appendChild(btn);
      btn.addEventListener('click', () => {
        const collapsed = cat.getAttribute('data-collapse') === '1';
        const next = collapsed ? '0' : '1';
        cat.setAttribute('data-collapse', next);
        const total = cat.querySelectorAll('.news-item').length;
        btn.textContent = next === '1'
          ? `展开其余 ${total - NEWS_COLLAPSE_LIMIT} 条（共 ${total} 条）`
          : '收起列表';
      });
    }
    if (forceExpand) {
      cat.setAttribute('data-collapse', '0');
      btn.style.display = 'none';
      btn.textContent = '收起列表';
    } else {
      if (cat.getAttribute('data-collapse') !== '0') {
        cat.setAttribute('data-collapse', '1');
      }
      btn.style.display = '';
      const total = items.length;
      const collapsed = cat.getAttribute('data-collapse') === '1';
      btn.textContent = collapsed
        ? `展开其余 ${total - NEWS_COLLAPSE_LIMIT} 条（共 ${total} 条）`
        : '收起列表';
    }
  });
}

function restoreNewsCollapse() {
  applyNewsCollapse(false);
}

function onNewsSearch(query) {
  query = (query || '').trim().toLowerCase();
  const terms = query.split(/\s+/).filter(Boolean);
  const items = document.querySelectorAll('.news-item, .hero-featured-card, .hero-sub-card');
  let matched = 0;

  if (!terms.length) {
    if (typeof filterNewsChannel === 'function') {
      const activeBtn = document.querySelector('.channel-btn.active');
      const channel = activeBtn ? (activeBtn.getAttribute('onclick') || '').match(/'([^']+)'/)?.[1] || 'all' : 'all';
      filterNewsChannel(channel, activeBtn);
    } else {
      items.forEach(el => el.style.display = '');
      document.querySelectorAll('.news-category').forEach(cat => cat.style.display = '');
    }
    restoreNewsCollapse();
    const countEl = document.getElementById('news-search-count');
    if (countEl) countEl.innerText = '';
    return;
  }

  applyNewsCollapse(true);
  items.forEach(el => {
    const title = (el.getAttribute('data-title') || el.innerText || '').toLowerCase();
    const summary = (el.getAttribute('data-summary') || '').toLowerCase();
    const source = (el.getAttribute('data-source') || '').toLowerCase();
    const cat = (el.getAttribute('data-cat') || '').toLowerCase();
    const date = (el.getAttribute('data-date') || '').toLowerCase();
    const searchTarget = title + ' ' + summary + ' ' + source + ' ' + cat + ' ' + date;
    const isMatch = terms.every(t => searchTarget.includes(t));
    el.style.display = isMatch ? (el.classList.contains('news-item') ? 'grid' : 'block') : 'none';
    if (isMatch) matched++;
  });

  document.querySelectorAll('.news-category').forEach(cat => {
    const visibleChildren = cat.querySelectorAll('.news-item:not([style*="display: none"])');
    cat.style.display = visibleChildren.length > 0 ? 'block' : 'none';
  });

  const countEl = document.getElementById('news-search-count');
  if (countEl) {
    countEl.innerText = `🔍 找到 ${matched} 条`;
  }
}

document.addEventListener('DOMContentLoaded', () => {
  applyNewsCollapse(false);
  const readKey = 'loneforme_read_news';
  let readLinks = [];
  try {
    readLinks = JSON.parse(localStorage.getItem(readKey) || '[]');
  } catch(e) {}

  document.querySelectorAll('.news-item, .hero-featured-card, .hero-sub-card').forEach(el => {
    const link = el.getAttribute('href');
    if (readLinks.includes(link)) {
      el.classList.add('news-read-card');
    }
    el.addEventListener('click', () => {
      if (link && !readLinks.includes(link)) {
        readLinks.push(link);
        if (readLinks.length > 300) readLinks = readLinks.slice(-300);
        try { localStorage.setItem(readKey, JSON.stringify(readLinks)); } catch(e) {}
        el.classList.add('news-read-card');
      }
    });
  });
});
</script>
<style>
.news-read-card {
  opacity: 0.62 !important;
}
.news-read-card .news-item-title, .news-read-card .hero-featured-title, .news-read-card .hero-sub-title {
  color: var(--color-muted, #888) !important;
}
</style>


<p class="news-updated">🕐 抓取更新于 2026-09-25 14:46（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
