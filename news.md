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
      <span>2026-10-17 23:46 抓取更新</span>
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
        <span class="channel-count">56</span>
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
        <span class="channel-count">11</span>
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
  <div class="ov-item"><span class="ov-num">7</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×18 · IT之家×10</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/10-17/10716464.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月17日电 据辽宁省纪委监委消息，日前，经辽宁省委批准，辽宁省纪委监委对本溪市政协原党组副书记、副主席邵涛严重违纪违法问题进行了立案审查调查。" data-title="辽宁省本溪市政协原党组副书记、副主席邵涛被“双开”" data-date="10-17 22:31" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-17 22:31</span>
      </div>
      <h2 class="hero-featured-title">辽宁省本溪市政协原党组副书记、副主席邵涛被“双开”</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.tomshardware.com/pc-components/gpus/quad-8-pin-mod-protects-the-usd8-500-rtx-5090-you-cant-replace-from-melting-modders-custom-power-solution-claims-to-fix-nvidia-16-pin-gpu-meltdowns" target="_blank" rel="noopener" data-cat="keji" data-summary="Redditor展示了用于Nvidia GeForce RTX显卡上16针电源连接器的全新四引脚8针电源转换套件。" data-title="Quad 8-pin mod protects the $8,500 RTX 5090 you can’t replace from melting" data-date="10-17 23:20" data-source="Tom's Hardware">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
      </div>
      <p class="hero-sub-title">Quad 8-pin mod protects the $8,500 RTX 5090 you can’t replace from melting</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/live/2026/oct/17/manchester-city-v-ipswich-brentford-v-liverpool-and-more-football-clockwatch-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="周六下午足球动作⚽现场记分牌⚽的最新消息|桌子|最佳射手|电子邮件来自Hill Dickinson的SimonAndy Hunter的比赛报告在这里，您可以在下面找到它。切尔西在国际比赛结束后带着" data-title="Manchester City v Ipswich, Brentford v Liverpool, and more: Football clockwatch" data-date="10-17 23:44" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Manchester City v Ipswich, Brentford v Liverpool, and more: Football clockwatch</p>
    </a>
    <a class="hero-sub-card" href="https://www.tomshardware.com/peripherals/gaming-headsets/hyperx-cloud-alpha-air-review" target="_blank" rel="noopener" data-cat="zonghe" data-summary="HyperX Cloud Alpha Air是该品牌首款开放式游戏耳机。它重量轻，舒适，听起来非常好。但麦克风的拾音率很低，而且似乎不适用于该品牌的外围软件（目前）。" data-title="HyperX Cloud Alpha Air Review: Open-back and budget-friendly" data-date="10-17 23:40" data-source="Tom's Hardware">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
      </div>
      <p class="hero-sub-title">HyperX Cloud Alpha Air Review: Open-back and budget-friendly</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-17/10716464.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月17日电 据辽宁省纪委监委消息，日前，经辽宁省委批准，辽宁省纪委监委对本溪市政协原党组副书记、副主席邵涛严重违纪违法问题进行了立案审查调查。" data-title="辽宁省本溪市政协原党组副书记、副主席邵涛被“双开”" data-date="10-17 22:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-17 22:31</span>
          <span class="news-item-title">辽宁省本溪市政协原党组副书记、副主席邵涛被“双开”</span>
          <span class="news-value-point">💡 中新网10月17日电 据辽宁省纪委监委消息，日前，经辽宁省委批准，辽宁省纪委监委对本溪市政协原党组副书记、副主席邵涛严重违纪违法问题进行了立案审…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-17/10716465.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月17日电 据辽宁省纪委监委消息，日前，经辽宁省委批准，辽宁省纪委监委对沈阳市委原常委、政法委原书记，沈阳市铁西区委原书记郭忠孝严重违纪违法问题进行了立案审查调查。" data-title="辽宁省沈阳市委原常委、政法委原书记郭忠孝被“双开”" data-date="10-17 22:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-17 22:30</span>
          <span class="news-item-title">辽宁省沈阳市委原常委、政法委原书记郭忠孝被“双开”</span>
          <span class="news-value-point">💡 中新网10月17日电 据辽宁省纪委监委消息，日前，经辽宁省委批准，辽宁省纪委监委对沈阳市委原常委、政法委原书记，沈阳市铁西区委原书记郭忠孝严重违…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-17/10716325.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="10月17日是国际消除贫困日。" data-title="做世界减贫事业的有力推动者" data-date="10-17 22:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-17 22:29</span>
          <span class="news-item-title">做世界减贫事业的有力推动者</span>
          <span class="news-value-point">💡 10月17日是国际消除贫困日</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-17/10716338.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="“长征中能活下来的有多少人？红军战士靠的是什么？图的是什么呢？”" data-title="学习手记｜答好“长征三问” 坚定必胜信念" data-date="10-17 22:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-17 22:27</span>
          <span class="news-item-title">学习手记｜答好“长征三问” 坚定必胜信念</span>
          <span class="news-value-point">💡 “长征中能活下来的有多少人</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-17/10716334.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="习近平总书记关切事·长征｜守护好红色传家宝" data-title="习近平总书记关切事·长征｜守护好红色传家宝" data-date="10-17 22:25" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-17 22:25</span>
          <span class="news-item-title">习近平总书记关切事·长征｜守护好红色传家宝</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-17/10716469.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月17日电 (记者 李纯 周昕 马帅莎)2026世界传统医药大会17日在北京启幕。澳门特区政府卫生局局长罗奕龙当日在接受媒体采访时表示，依托制度优势，澳门持续深化中医药守正创新，搭建传统医药国际交流桥梁，服务健康中国与粤港澳大湾区建设。" data-title="澳门卫生局局长：发挥澳门独特优势 助力中医药创新出海" data-date="10-17 22:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-17 22:21</span>
          <span class="news-item-title">澳门卫生局局长：发挥澳门独特优势 助力中医药创新出海</span>
          <span class="news-value-point">💡 中新社北京10月17日电 (记者 李纯 周昕 马帅莎)2026世界传统医药大会17日在北京启幕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-17/10716470.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月17日电 当地时间10月17日，克罗地亚总理普连科维奇在萨格勒布会见中共中央政治局委员、外交部长王毅。" data-title="克罗地亚总理普连科维奇会见王毅" data-date="10-17 21:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-17 21:52</span>
          <span class="news-item-title">克罗地亚总理普连科维奇会见王毅</span>
          <span class="news-value-point">💡 中新社北京10月17日电 当地时间10月17日，克罗地亚总理普连科维奇在萨格勒布会见中共中央政治局委员、外交部长王毅</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-17/10716460.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网南平10月17日电 (张丽君 陈悦 吴冠标)在朱子学与多元文明对话大会暨第五届考亭论坛举办期间，韩国中央大学名誉教授卢仁淑围绕《朱子家礼》的海外传播与本土化实践发表了研究观点。她以朝鲜著名学者星湖李瀷的《家礼疾书》为研究样本指出，朱子礼制在朝鲜的落地并非简单的照搬移植，而是结合时代、民生与社会条件的创造性调适，其“因时变通、普惠庶民”的礼学实践，为古今文明对话、中外文化互鉴提供重要东方智慧。" data-title="韩国学者：朱子家礼海外本土化为多元文明互鉴提供古老智慧" data-date="10-17 21:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-17 21:14</span>
          <span class="news-item-title">韩国学者：朱子家礼海外本土化为多元文明互鉴提供古老智慧</span>
          <span class="news-value-point">💡 中新网南平10月17日电 (张丽君 陈悦 吴冠标)在朱子学与多元文明对话大会暨第五届考亭论坛举办期间，韩国中央大学名誉教授卢仁淑围绕《朱子家礼》…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-17/10716454.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社首尔10月17日电 (记者 金旭)韩国外交部当地时间17日表示，韩国政府对日本高层当天向供奉二战甲级战犯的靖国神社供奉祭品及前往参拜，再次深表失望和遗憾。" data-title="韩国政府敦促日本高层正视历史反省过去" data-date="10-17 21:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-17 21:01</span>
          <span class="news-item-title">韩国政府敦促日本高层正视历史反省过去</span>
          <span class="news-value-point">💡 中新社首尔10月17日电 (记者 金旭)韩国外交部当地时间17日表示，韩国政府对日本高层当天向供奉二战甲级战犯的靖国神社供奉祭品及前往参拜，再次…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/17/us/politics/election-fraud-conspiracies-trump.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="投票权倡导者担心特朗普政府可能会利用联邦政府对选举提出质疑，阻止参与选举或试图使选举结果非法化。" data-title="Trump Revives 2020 Election Conspiracy Theories as Midterms Loom" data-date="10-17 20:58" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-17 20:58</span>
          <span class="news-item-title">特朗普在中期选举中重振2020年选举阴谋论</span>
          <span class="news-item-title-en">Trump Revives 2020 Election Conspiracy Theories as Midterms Loom</span>
          <span class="news-value-point">💡 投票权倡导者担心特朗普政府可能会利用联邦政府对选举提出质疑，阻止参与选举或试图使选举结果非法化</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-17/10716428.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社曼谷10月17日电 (王茜 李映民)泰国防灾减灾厅17日通报说，截至当天6时，泰国仍有20个府及首都曼谷部分地区受洪灾影响，共有70.5万户家庭、约214.9万人受影响。" data-title="泰国洪灾214万多人受影响" data-date="10-17 20:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-17 20:37</span>
          <span class="news-item-title">泰国洪灾214万多人受影响</span>
          <span class="news-value-point">💡 中新社曼谷10月17日电 (王茜 李映民)泰国防灾减灾厅17日通报说，截至当天6时，泰国仍有20个府及首都曼谷部分地区受洪灾影响，共有70.5万…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-17/10716350.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京10月17日电" data-title="李强在2026世界传统医药大会开幕式上的致辞（全文）" data-date="10-17 19:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-17 19:24</span>
          <span class="news-item-title">李强在2026世界传统医药大会开幕式上的致辞（全文）</span>
          <span class="news-value-point">💡 新华社北京10月17日电</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-17/10716342.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京10月17日电 10月17日上午，国务院总理李强在北京出席2026世界传统医药大会开幕式并致辞。" data-title="李强出席2026世界传统医药大会开幕式并致辞" data-date="10-17 19:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-17 19:22</span>
          <span class="news-item-title">李强出席2026世界传统医药大会开幕式并致辞</span>
          <span class="news-value-point">💡 新华社北京10月17日电 10月17日上午，国务院总理李强在北京出席2026世界传统医药大会开幕式并致辞</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-17/10716348.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社塔什干10月17日电 10月17日上午，应乌兹别克斯坦总理阿里波夫邀请，中国国务院总理李强乘包机离开北京，对乌兹别克斯坦进行正式访问。国务委员兼国务院秘书长吴政隆等陪同人员同机离京。" data-title="李强抵达塔什干开始对乌兹别克斯坦进行正式访问" data-date="10-17 19:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-17 19:11</span>
          <span class="news-item-title">李强抵达塔什干开始对乌兹别克斯坦进行正式访问</span>
          <span class="news-value-point">💡 中新社塔什干10月17日电 10月17日上午，应乌兹别克斯坦总理阿里波夫邀请，中国国务院总理李强乘包机离开北京，对乌兹别克斯坦进行正式访问</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-17/10716329.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社成都10月17日电(记者丁小溪)中共中央政治局常委、全国政协主席王沪宁10月13日至16日在四川成都市、德阳市、甘孜藏族自治州调研。他表示，要以习近平新时代中国特色社会主义思想为指导，深入贯彻落实党的二十届四中全会精神，着眼为实现“十五五”时期发展、推进中国式现代化凝心聚力，扎实抓好铸牢中华民族共同体意识、推进中华民族共同体建设工作，扎实抓好系统推进我国宗教中国化、加强宗教事务治理法治化工作，巩固和发展民族和睦、宗教和顺、社会和谐的良好局面。" data-title="王沪宁在四川调研时强调 坚持为推进中国式现代化凝心聚力 扎实做好新时代党的民族宗教工作" data-date="10-17 18:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-17 18:47</span>
          <span class="news-item-title">王沪宁在四川调研时强调 坚持为推进中国式现代化凝心聚力 扎实做好新时代党的民族宗教工作</span>
          <span class="news-value-point">💡 新华社成都10月17日电(记者丁小溪)中共中央政治局常委、全国政协主席王沪宁10月13日至16日在四川成都市、德阳市、甘孜藏族自治州调研</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/quad-8-pin-mod-protects-the-usd8-500-rtx-5090-you-cant-replace-from-melting-modders-custom-power-solution-claims-to-fix-nvidia-16-pin-gpu-meltdowns" target="_blank" rel="noopener" data-cat="keji" data-summary="Redditor展示了用于Nvidia GeForce RTX显卡上16针电源连接器的全新四引脚8针电源转换套件。" data-title="Quad 8-pin mod protects the $8,500 RTX 5090 you can’t replace from melting" data-date="10-17 23:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-17 23:20</span>
          <span class="news-item-title">四引脚8引脚模块保护您无法更换的$ 8,500 RTX 5090</span>
          <span class="news-item-title-en">Quad 8-pin mod protects the $8,500 RTX 5090 you can’t replace from melting</span>
          <span class="news-value-point">💡 Redditor展示了用于Nvidia GeForce RTX显卡上16针电源连接器的全新四引脚8针电源转换套件</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1013409/meta-removes-language-that-may-have-allowed-it-to-scrape-news-sites" target="_blank" rel="noopener" data-cat="keji" data-summary="在强烈反对之后， Meta再次更新其条款，以删除暗示它可以从包括新闻网站在内的网站上抓取内容来训练其人工智能的语言。具体而言，以下语言不再出现在商业条款页面上： …… Meta" data-title="Meta removes language that may have allowed it to scrape news sites" data-date="10-17 23:04" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-17 23:04</span>
          <span class="news-item-title">Meta删除了可能允许其抓取新闻网站的语言</span>
          <span class="news-item-title-en">Meta removes language that may have allowed it to scrape news sites</span>
          <span class="news-value-point">💡 在强烈反对之后， Meta再次更新其条款，以删除暗示它可以从包括新闻网站在内的网站上抓取内容来训练其人工智能的语言</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/410.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 17 日消息，广汽埃安刚刚宣布 Ray7 预售开启仅 2 小时，订单达 6817 单。该车于今晚开启预售，共 5 款车型，价格为 12.88 万元起。车身尺寸方面，长宽高为 4960×1900×1455mm，轴距达 2920mm，提供仲夏紫、闪电黄、月辉银、风暴红、熔岩灰、云舒白、热带蓝车色。座舱配备高通骁龙 8295P 座舱芯片 +24GB LPDDR4 运存 +128GB UFS 闪存，15.6 英寸 2.5K 高清中控屏 + 车手互联全覆盖。此外，该车搭载华为 DriveONE 多合一电驱，配合埃安全新热管理系统和 28 合一热管理模块，CLTC 百公里电耗仅为 9.7 度，CLTC 纯电续航超 700km。IT之家附预售价如下：530 后驱驾趣版 12.88 万元" data-title="12.88 万元起，广汽埃安 Ray7 预售 2 小时订单达 6817 单" data-date="10-17 23:01" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-17 23:01</span>
          <span class="news-item-title">12.88 万元起，广汽埃安 Ray7 预售 2 小时订单达 6817 单</span>
          <span class="news-value-point">💡 IT之家 10 月 17 日消息，广汽埃安刚刚宣布 Ray7 预售开启仅 2 小时，订单达 6817 单</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-insists-the-rtx-5090-isnt-dead-despite-severe-shortages-and-removed-listings-at-multiple-retailers-flagship-gpu-is-missing-from-nvidias-store-and-commands-usd8-500-on-amazon" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达表示， RTX 5090并未停产，只是供应受到限制—但该卡实际上已从店面中消失" data-title="Nvidia reportedly insists the RTX 5090 isn&#39;t dead despite severe shortages and removed listings at multiple retailers" data-date="10-17 22:38" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-17 22:38</span>
          <span class="news-item-title">据报道，英伟达坚称，尽管RTX 5090严重短缺，并在多家零售商处删除了房源，但它并没有死</span>
          <span class="news-item-title-en">Nvidia reportedly insists the RTX 5090 isn't dead despite severe shortages and removed listings at multiple retailers</span>
          <span class="news-value-point">💡 英伟达表示， RTX 5090并未停产，只是供应受到限制—但该卡实际上已从店面中消失</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-17/10716318.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="10月16日，习近平总书记在内蒙古自治区乌兰察布市考察，前往察哈尔高新技术开发区，了解内蒙古自治区推进“东数西算”工程枢纽节点建设和绿色算力产业发展等情况。" data-title="第一观察｜总书记考察绿色算力产业 指引因地制宜发展新质生产力" data-date="10-17 22:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-17 22:24</span>
          <span class="news-item-title">第一观察｜总书记考察绿色算力产业 指引因地制宜发展新质生产力</span>
          <span class="news-value-point">💡 10月16日，习近平总书记在内蒙古自治区乌兰察布市考察，前往察哈尔高新技术开发区，了解内蒙古自治区推进“东数西算”工程枢纽节点建设和绿色算力产业…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-lab-offers-free-plumbing-and-hvac-repairs-across-three-cities-to-train-ai-robots-wearable-sensors-record-video-of-repair-work-for-robotics-training-free-services-also-include-electrical-work-air-duct-cleaning-and-carpet-cleaning" target="_blank" rel="noopener" data-cat="keji" data-summary="HUMXN希望为明尼阿波利斯、芝加哥和迈阿密的房屋提供维护和维修服务，以收集数据来训练人工智能模型和机器人。" data-title="AI lab offers free plumbing and HVAC repairs across three cities to train AI robots" data-date="10-17 21:21" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-17 21:21</span>
          <span class="news-item-title">人工智能实验室在三个城市提供免费管道和HVAC维修，以培训人工智能机器人</span>
          <span class="news-item-title-en">AI lab offers free plumbing and HVAC repairs across three cities to train AI robots</span>
          <span class="news-value-point">💡 HUMXN希望为明尼阿波利斯、芝加哥和迈阿密的房屋提供维护和维修服务，以收集数据来训练人工智能模型和机器人</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-17/10716395.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网广西柳州10月17日电 (林馨)重阳节前夕，位于广西柳州市的柳州城市职业学院(简称“柳城职”)旅游与康养学院实训课上，“00后”学生正在学习人工智能(AI)舌诊、脉诊等辅助诊断手段。中国养老服务正从“传统照料”向“智慧守护”升级，越来越多年轻人开始进入这一领域。" data-title="中国养老业从“照料”转向“智慧” 年轻人成新生力量" data-date="10-17 21:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-17 21:07</span>
          <span class="news-item-title">中国养老业从“照料”转向“智慧” 年轻人成新生力量</span>
          <span class="news-value-point">💡 中新网广西柳州10月17日电 (林馨)重阳节前夕，位于广西柳州市的柳州城市职业学院(简称“柳城职”)旅游与康养学院实训课上，“00后”学生正在学…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-october-17-2026-packaging-roadmaps-chinese-dgx-spark-rival-emerges-and-digging-into-asmls-earnings" target="_blank" rel="noopener" data-cat="keji" data-summary="本周， Tom&#39;s Hardware Premium订阅者可以阅读我们的EMIB和Foveros路线图，以及中国在本地人工智能系统领域的最新竞争情况等。" data-title="This week on Tom&#39;s Hardware Premium: October 17, 2026" data-date="10-17 21:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-17 21:00</span>
          <span class="news-item-title">本周Tom's Hardware Premium ： 2026年10月17日</span>
          <span class="news-item-title-en">This week on Tom's Hardware Premium: October 17, 2026</span>
          <span class="news-value-point">💡 本周， Tom's Hardware Premium订阅者可以阅读我们的EMIB和Foveros路线图，以及中国在本地人工智能系统领域的最新竞争…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1013195/ai-agents-blocked-web" target="_blank" rel="noopener" data-cat="keji" data-summary="自主智能体是人工智能中最热门的东西。OpenAI、Meta、Google、Instinct和其他公司承诺，他们的代理可以代表您浏览互联网，从预订晚餐、清理收件箱到购买新鞋，无所不包。Bu" data-title="Websites are closing their doors to AI agents" data-date="10-17 21:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-17 21:00</span>
          <span class="news-item-title">网站正在向人工智能代理敞开大门</span>
          <span class="news-item-title-en">Websites are closing their doors to AI agents</span>
          <span class="news-value-point">💡 自主智能体是人工智能中最热门的东西</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/retro-gaming/game-decompilation-tracker-decomp-dev-shuts-its-public-leaderboard-saying-ai-has-broken-the-community-its-creator-blames-forks-that-use-ai-to-finish-other-teams-projects-and-races-to-ship-rough-pc-ports" target="_blank" rel="noopener" data-cat="keji" data-summary="decomp.dev关闭了游戏反编译项目的公开索引，称人工智能驱动的分叉和端口破坏了社区。" data-title="Game decompilation hub freezes leaderboard after AI turns progress into a hollow numbers game amid explosion of &#39;AI slop&#39;" data-date="10-17 19:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-17 19:30</span>
          <span class="news-item-title">在“AI SLOP”爆发期间， AI将进度转变为空洞的数字游戏后，游戏反编译中心冻结了排行榜</span>
          <span class="news-item-title-en">Game decompilation hub freezes leaderboard after AI turns progress into a hollow numbers game amid explosion of 'AI slop'</span>
          <span class="news-value-point">💡 decomp.dev关闭了游戏反编译项目的公开索引，称人工智能驱动的分叉和端口破坏了社区</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/377.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 17 日消息，机械革命 imini P700 迷你主机新增了一款搭载 AMD 锐龙 7 H 255 处理器、16GB DDR5 5600 内存、512GB 固态硬盘的版本，首发价 4399 元。京东机械革命 imini P700 台式迷你主机 R7 H255 16G DDR5 512G SSD 券后 4399 元领 200 元券该机搭载 AMD 锐龙 7 H 255 处理器，配备 AMD Radeon 780M 核心显卡；配备双 SODIMM 插槽，可升级至最高 128GB 内存；配备 2 个 M.2 2280 SSD 插槽。接口方面，该机支持 HDMI+DP+Type-C 四屏输出，HDMI 和 DP 均支持 4K 120Hz，USB 速率最高可达 40Gbps 且支持" data-title="机械革命 imini P700 迷你电脑主机新增 AMD R7 H255 + 16G + 512G 配置，4399 元" data-date="10-17 19:10" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-17 19:10</span>
          <span class="news-item-title">机械革命 imini P700 迷你电脑主机新增 AMD R7 H255 + 16G + 512G 配置，4399 元</span>
          <span class="news-value-point">💡 IT之家 10 月 17 日消息，机械革命 imini P700 迷你主机新增了一款搭载 AMD 锐龙 7 H 255 处理器、16GB DDR…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/employee-exclusive-asml-lego-set-now-available-on-rebrickable-custom-creation-modifies-original-version-to-add-more-details-now-requires-810-parts" target="_blank" rel="noopener" data-cat="keji" data-summary="一位乐高爱好者重新创建了罕见的ASML乐高套件，添加了他们自己的定制，并在Rebrickable上免费分享了这些计划。" data-title="ASML&#39;s employee-only High-NA EUV Lego kit gets an open 810-piece fan replica" data-date="10-17 18:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-17 18:00</span>
          <span class="news-item-title">ASML的员工专用高NA EUV乐高套件获得了一个开放的810件风扇复制品</span>
          <span class="news-item-title-en">ASML's employee-only High-NA EUV Lego kit gets an open 810-piece fan replica</span>
          <span class="news-value-point">💡 一位乐高爱好者重新创建了罕见的ASML乐高套件，添加了他们自己的定制，并在Rebrickable上免费分享了这些计划</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/283.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 17 日消息，GPU 初创企业 Bolt Graphics 当地时间本月 13 日宣布，其已完成 Zeus 架构 GPU 测试芯片的调试工作，为商用产品的 2028 年发售打下了基础。Bolt 的 Zeus 架构集成专用电磁仿真硬件，同时也能加速路径追踪图形负载，适用于物理 AI 等复杂计算场景。Bolt 在台积电 12nm 工艺上进行了小尺寸测试芯片的流片。该测试芯片仅有 6mm²，A0 步进回片未被发现任何功能问题，功耗 1.4W。Bolt 的商用 GPU 芯片则将采用台积电的 N5P 制程工艺，预计 2027Q1 开放开发者访问权限、2027 年底向早期访问计划客户提供首批产品、2028 年启动 PCIe AIC 和服务器量产、同年全面上市。" data-title="Bolt 完成 Zeus GPU 测试芯片调试，实际产品预计 2028 年发售" data-date="10-17 14:08" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-17 14:08</span>
          <span class="news-item-title">Bolt 完成 Zeus GPU 测试芯片调试，实际产品预计 2028 年发售</span>
          <span class="news-value-point">💡 IT之家 10 月 17 日消息，GPU 初创企业 Bolt Graphics 当地时间本月 13 日宣布，其已完成 Zeus 架构 GPU 测…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/274.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 17 日消息，英国当地时间 10 月 14 日在伦敦接受彭博记者 Emily Chang 采访时，英伟达首席执行官黄仁勋表示当前 AI 需求远大于供给，不认为现阶段处于“AI 泡沫”阶段，不过他也承认未来供给可能超过需求。在采访中，黄仁勋表示：“泡沫发生在供给超过需求的时候。最终供需会趋于平衡，而且在某个时候，供给可能会超过需求，但不是今天。今天，需求远远大于供给。”面对 AI 云服务商 CoreWeave 引发的市场担忧，黄仁勋表示没有必要救助该公司，其财务状况会没问题。报道说，CoreWeave 股价随后在周四扭转跌势，收涨近 6%。IT之家附上相关股价信息如下：黄仁勋认为 AI 安全不应成为减速理由，业内应该加速 AI 部署，而非放缓，想要遏制 AI 失控，需要更多" data-title="英伟达黄仁勋称 AI 现在不是泡沫，安全不应成为减速理由" data-date="10-17 13:39" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-17 13:39</span>
          <span class="news-item-title">英伟达黄仁勋称 AI 现在不是泡沫，安全不应成为减速理由</span>
          <span class="news-value-point">💡 IT之家 10 月 17 日消息，英国当地时间 10 月 14 日在伦敦接受彭博记者 Emily Chang 采访时，英伟达首席执行官黄仁勋表示…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/273.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 17 日消息，据新华社报道，国家市场监督管理总局 16 日通报，2025 年以来，市场监管总局会同公安部等部门聚焦城乡接合部、国省道沿线等加油机作弊违法行为高发频发区域，共立案查处加油机作弊案件 399 件、案值 2.7 亿元、罚没款 1.43 亿元。市场监管总局市场稽查专员嵇小灵介绍，当前加油机作弊呈现科技化、隐蔽化、链条化、双重危害性四大突出特点。一是作弊手段科技化，可以远程控制调整作弊参数。不法分子不再局限于传统机械改动，主要通过更换加油机主板、加装作弊模块、植入作弊软件等方式，破解加油机原有防作弊自锁机制。经营者可以通过电脑、手机 App、遥控发射器，一键切换作弊开关、调整偷油比例。二是作弊行为高度隐蔽，常规检查难以即时发现。不法分子利用更换外观相同的计控芯片，修" data-title="市场监管总局：立案查处加油机作弊案件 399 件、案值 2.7 亿元、罚没款 1.43 亿元" data-date="10-17 13:26" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-17 13:26</span>
          <span class="news-item-title">市场监管总局：立案查处加油机作弊案件 399 件、案值 2.7 亿元、罚没款 1.43 亿元</span>
          <span class="news-value-point">💡 IT之家 10 月 17 日消息，据新华社报道，国家市场监督管理总局 16 日通报，2025 年以来，市场监管总局会同公安部等部门聚焦城乡接合部…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">11 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/17/manchester-city-v-ipswich-brentford-v-liverpool-and-more-football-clockwatch-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="周六下午足球动作⚽现场记分牌⚽的最新消息|桌子|最佳射手|电子邮件来自Hill Dickinson的SimonAndy Hunter的比赛报告在这里，您可以在下面找到它。切尔西在国际比赛结束后带着" data-title="Manchester City v Ipswich, Brentford v Liverpool, and more: Football clockwatch" data-date="10-17 23:44" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-17 23:44</span>
          <span class="news-item-title">曼城诉伊普斯维奇、布伦特福德诉利物浦等：足球钟表</span>
          <span class="news-item-title-en">Manchester City v Ipswich, Brentford v Liverpool, and more: Football clockwatch</span>
          <span class="news-value-point">💡 周六下午足球动作⚽现场记分牌⚽的最新消息|桌子|最佳射手|电子邮件来自Hill Dickinson的SimonAndy Hunter的比赛报告在…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/17/newcastle-v-aston-villa-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="⚽ 英超联赛下午5:30 BST开球⚽现场比分更新|桌子|最佳射手|在BlueskyJoelinton上关注我们，取代纽卡斯尔队中的Jacob Murphy ，这是他们周一在考文垂4-1失利的唯一变化。这是他第一次开始" data-title="Newcastle v Aston Villa: Premier League" data-date="10-17 23:42" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-17 23:42</span>
          <span class="news-item-title">纽卡斯尔v阿斯顿维拉：英超联赛</span>
          <span class="news-item-title-en">Newcastle v Aston Villa: Premier League</span>
          <span class="news-value-point">💡 ⚽ 英超联赛下午5:30 BST开球⚽现场比分更新|桌子|最佳射手|在BlueskyJoelinton上关注我们，取代纽卡斯尔队中的Jacob …</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/17/everton-v-chelsea-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="佩德罗·内托（ Pedro Neto ）的进球在下半场结束，为切尔西赢得了埃弗顿-埃弗顿（ Everton ）开球的罕见胜利，并持续了很长时间。马丁内斯声称平底锅。在开球之前，每个人都会膝盖。这是英超联赛两周的第一周" data-title="Everton 0-2 Chelsea: Premier League – as it happened" data-date="10-17 22:13" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-17 22:13</span>
          <span class="news-item-title">埃弗顿0-2切尔西：英超联赛–事实就是这样</span>
          <span class="news-item-title-en">Everton 0-2 Chelsea: Premier League – as it happened</span>
          <span class="news-value-point">💡 佩德罗·内托（ Pedro Neto ）的进球在下半场结束，为切尔西赢得了埃弗顿-埃弗顿（ Everton ）开球的罕见胜利，并持续了很长时间</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/17/everton-chelsea-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="切尔西以一种精神、权威和韧性从国际比赛中恢复过来，这对哈比·阿隆索来说是个好兆头。他们在埃弗顿的麻烦，近年来并不是一个快乐的狩猎场，仅限于埃米·马丁内斯需要的七分钟" data-title="Neto double at Everton leads Chelsea to victory marred by Martínez head injury" data-date="10-17 21:53" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-17 21:53</span>
          <span class="news-item-title">埃弗顿的Neto双打带领切尔西取得因马丁内斯头部受伤而受损的胜利</span>
          <span class="news-item-title-en">Neto double at Everton leads Chelsea to victory marred by Martínez head injury</span>
          <span class="news-value-point">💡 切尔西以一种精神、权威和韧性从国际比赛中恢复过来，这对哈比·阿隆索来说是个好兆头</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/10/premier-league-top-scorers-2026-27-race-for-golden-boot" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="找出哪位英国顶尖射手正在向进球排行榜射击。继续阅读……" data-title="Premier League top scorers 2026-27: who is leading race for the golden boot?" data-date="10-17 21:39" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-17 21:39</span>
          <span class="news-item-title">2026-27赛季英超联赛最佳射手：谁是金靴赛的领跑者？</span>
          <span class="news-item-title-en">Premier League top scorers 2026-27: who is leading race for the golden boot?</span>
          <span class="news-value-point">💡 找出哪位英国顶尖射手正在向进球排行榜射击</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c674pzzlz8zlo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="佩德罗·内托在切尔西的两个下半场进球确保了周六在埃弗顿的重要客场胜利。" data-title="Neto stars but who was subdued? - player ratings for Everton v Chelsea" data-date="10-17 21:39" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-17 21:39</span>
          <span class="news-item-title">内托球星，但谁被征服了？ -埃弗顿对切尔西的球员评分</span>
          <span class="news-item-title-en">Neto stars but who was subdued? - player ratings for Everton v Chelsea</span>
          <span class="news-value-point">💡 佩德罗·内托在切尔西的两个下半场进球确保了周六在埃弗顿的重要客场胜利</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqn73xe5eelgo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="有些球员注定会在替补席上产生最大的影响，但谁是有史以来排名前十的英超超级球员？" data-title="Ranking the Premier League&#39;s all-time greatest super subs" data-date="10-17 05:15" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-17 05:15</span>
          <span class="news-item-title">排名英超有史以来最伟大的超级潜艇</span>
          <span class="news-item-title-en">Ranking the Premier League's all-time greatest super subs</span>
          <span class="news-value-point">💡 有些球员注定会在替补席上产生最大的影响，但谁是有史以来排名前十的英超超级球员</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/16/premier-league-team-news-predicted-lineups-for-the-weekend-action" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="In-form Everton在对阵切尔西的比赛中开局，而挣扎中的曼联则面临着前往利兹的艰难旅程周六中午12:30 TNT体育1场地Hill Dickinson体育场继续阅读..." data-title="Premier League team news: predicted lineups for the weekend action" data-date="10-17 02:07" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-17 02:07</span>
          <span class="news-item-title">英超球队新闻：周末动作的预测阵容</span>
          <span class="news-item-title-en">Premier League team news: predicted lineups for the weekend action</span>
          <span class="news-value-point">💡 In-form Everton在对阵切尔西的比赛中开局，而挣扎中的曼联则面临着前往利兹的艰难旅程周六中午12:30 TNT体育1场地Hill D…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/16/martinez-sorry-outburst-european-reaction-premier-league-latest-football-news-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）表示，曼联已经从马丁内斯盖特转会，而恩佐·马雷斯卡（ Enzo Maresca ）对曼城的场外冲突“没有压力”。切尔西今天早上证实，里斯·詹姆斯（ Reece James ）接受了轻微的膝盖手术。" data-title="Carrick includes Martínez in squad; Madrid call for Tebas to quit over Goebbels comparison: football news" data-date="10-17 01:14" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-17 01:14</span>
          <span class="news-item-title">卡里克在球队中包括马丁内斯；马德里呼吁特巴斯退出戈培尔的比较：足球新闻</span>
          <span class="news-item-title-en">Carrick includes Martínez in squad; Madrid call for Tebas to quit over Goebbels comparison: football news</span>
          <span class="news-value-point">💡 迈克尔·卡里克（ Michael Carrick ）表示，曼联已经从马丁内斯盖特转会，而恩佐·马雷斯卡（ Enzo Maresca ）对曼城的场…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6je5lwxk5l0o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="一位知名律师告诉BBC Sport ，曼城在被判犯有违反英超联赛财务规则的罪行后，如果他们有机会赢得上诉，他们将面临“重大障碍”。" data-title="Do Manchester City have any grounds to win their appeal?" data-date="10-17 00:17" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-17 00:17</span>
          <span class="news-item-title">曼城是否有任何理由赢得他们的上诉？</span>
          <span class="news-item-title-en">Do Manchester City have any grounds to win their appeal?</span>
          <span class="news-value-point">💡 一位知名律师告诉BBC Sport ，曼城在被判犯有违反英超联赛财务规则的罪行后，如果他们有机会赢得上诉，他们将面临“重大障碍”</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cwy7l5e4376no?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="刘易斯·库马斯（ Lewis Koumas ）谈到打破史蒂文·杰拉德（ Steven Gerrard ）的纪录，抓住他在安东尼·伊拉奥拉（ Andoni Iraola ）手下的机会，以及他在曼城" data-title="Feel-good Koumas story something for Liverpool to smile about" data-date="10-17 00:06" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-17 00:06</span>
          <span class="news-item-title">Koumas的美好故事，让利物浦人一笑置之</span>
          <span class="news-item-title-en">Feel-good Koumas story something for Liverpool to smile about</span>
          <span class="news-value-point">💡 刘易斯·库马斯（ Lewis Koumas ）谈到打破史蒂文·杰拉德（ Steven Gerrard ）的纪录，抓住他在安东尼·伊拉奥拉（ An…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.tomshardware.com/peripherals/gaming-headsets/hyperx-cloud-alpha-air-review" target="_blank" rel="noopener" data-cat="zonghe" data-summary="HyperX Cloud Alpha Air是该品牌首款开放式游戏耳机。它重量轻，舒适，听起来非常好。但麦克风的拾音率很低，而且似乎不适用于该品牌的外围软件（目前）。" data-title="HyperX Cloud Alpha Air Review: Open-back and budget-friendly" data-date="10-17 23:40" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-17 23:40</span>
          <span class="news-item-title">HyperX Cloud Alpha Air评测：开放且预算友好</span>
          <span class="news-item-title-en">HyperX Cloud Alpha Air Review: Open-back and budget-friendly</span>
          <span class="news-value-point">💡 HyperX Cloud Alpha Air是该品牌首款开放式游戏耳机</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/16/us/bend-shooting-hero-teacher-dad.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="俄勒冈州本德市正在赞扬那些努力阻止银轨小学枪手的人。当局正在寻找答案。" data-title="School Shooting in Bend, Ore., Has Heroes and Pain, But Few Answers" data-date="10-17 23:21" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-17 23:21</span>
          <span class="news-item-title">俄勒冈州本德市校园枪击案，有英雄和痛苦，但很少有答案</span>
          <span class="news-item-title-en">School Shooting in Bend, Ore., Has Heroes and Pain, But Few Answers</span>
          <span class="news-value-point">💡 俄勒冈州本德市正在赞扬那些努力阻止银轨小学枪手的人</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/peripherals/controllers-gamepads/moza-ay210-force-feedback-base-and-mfy-yoke-review" target="_blank" rel="noopener" data-cat="zonghe" data-summary="MOZA AY210 Force Feedback Base和MFY Yoke Bundle为桌面飞行模拟器带来了力反馈和自动驾驶功能。" data-title="MOZA AY210 Force Feedback Base and MFY Yoke review: Taking flight sim immersion to the next level" data-date="10-17 23:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-17 23:00</span>
          <span class="news-item-title">MOZA AY210 Force Feedback Base和MFY Yoke回顾：将飞行模拟沉浸式体验提升到一个新的水平</span>
          <span class="news-item-title-en">MOZA AY210 Force Feedback Base and MFY Yoke review: Taking flight sim immersion to the next level</span>
          <span class="news-value-point">💡 MOZA AY210 Force Feedback Base和MFY Yoke Bundle为桌面飞行模拟器带来了力反馈和自动驾驶功能</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1013105/pikmin-4-nintendo-switch-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="如果你想知道这个周末玩什么视频游戏，我的同事希娜·瓦萨尼（ Sheena Vasani ）发现了一款打折的Nintendo Switch游戏，可以即时数字传输。沃尔玛的Switch数字版Pikmin 4折扣为39.88 $ ，略高于20 $" data-title="Pikmin 4 is $20 off ahead of its $10 Nintendo Switch 2 update" data-date="10-17 23:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-17 23:00</span>
          <span class="news-item-title">Pikmin 4比其$ 10 Nintendo Switch 2更新提前$ 20折扣</span>
          <span class="news-item-title-en">Pikmin 4 is $20 off ahead of its $10 Nintendo Switch 2 update</span>
          <span class="news-value-point">💡 如果你想知道这个周末玩什么视频游戏，我的同事希娜·瓦萨尼（ Sheena Vasani ）发现了一款打折的Nintendo Switch游戏，可…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/17/world/europe/pope-leo-discharged-hospital.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Leo XIV在罗马的Gemelli医院接受了肺癌治疗。" data-title="Pope Leo Leaves Hospital, Days After Lung Cancer Surgery" data-date="10-17 22:59" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-17 22:59</span>
          <span class="news-item-title">教皇利奥离开医院，肺癌手术后几天</span>
          <span class="news-item-title-en">Pope Leo Leaves Hospital, Days After Lung Cancer Surgery</span>
          <span class="news-value-point">💡 Leo XIV在罗马的Gemelli医院接受了肺癌治疗</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/409.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 17 日消息，网易逆水寒官宣，10 月 30 日，《逆水寒：新世界》首个大型资料片【苗疆蛊事】正式开启，将首次采用双线更新的框架。根据官方介绍，苗寨会在月色渐显时展示出另一幅面孔。而当血月升起，刚刚流连的山水，也有了让人忍不住追问的秘密。循着蛊影深入，在【祈梦月见岭】与阿初一同直面姬玄霜；月相轮转，下一次又会遇见怎样的挑战？无更暗市里，异闻百相真假难辨，就连熟悉的菠萝农场，也被一群夜晚的不速之客找上了门……《逆水寒：新世界》首个大型资料片【苗疆蛊事】将带来全新地图【月见岭】、大理正传终章剧情、月见岭正传楔章、全新团本【祈梦月见岭】、全新月相机制。新资料片还有莫奈主题内容、星彩宠物，以及新的副本挑战、逆水侠棋第四赛季、全新种植活动【捣蛋鬼入侵】。随新资料片一同到来的还有多项" data-title="网易《逆水寒：新世界》首个大型资料片【苗疆蛊事】官宣，首次采用双线更新框架" data-date="10-17 22:43" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-17 22:43</span>
          <span class="news-item-title">网易《逆水寒：新世界》首个大型资料片【苗疆蛊事】官宣，首次采用双线更新框架</span>
          <span class="news-value-point">💡 IT之家 10 月 17 日消息，网易逆水寒官宣，10 月 30 日，《逆水寒：新世界》首个大型资料片【苗疆蛊事】正式开启，将首次采用双线更新的…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/407.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 17 日消息，英伟达个人计算业务高级副总裁 Jeff Fisher 昨日在台北出席 RTX Spark 相关活动时回应了 RTX 5090 停产相关传闻，明确表示相关消息不属实。他强调，这款显卡仍是英伟达非常重要的核心产品，后续将继续供货。但他也同时承认，当前供应链产能确实受到限制，英伟达正努力推动产品进入市场。此前，消息人士 MEGAsizeGPU (@Zed__Wang) 10 月 10 日爆料称，英伟达将不再向 GeForce RTX 50 系列游戏显卡分配 GB202，并将原本用于该卡的 GB202 芯片转向 RTX PRO 专业卡。相关传闻还提到，英伟达可能推出配备 24GB 显存的 RTX 5080，以填补高端游戏显卡市场的产品空缺。不过，这些说法当时并未获得" data-title="英伟达否认 RTX 5090 停产传闻，承认供应链产能受限" data-date="10-17 22:33" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-17 22:33</span>
          <span class="news-item-title">英伟达否认 RTX 5090 停产传闻，承认供应链产能受限</span>
          <span class="news-value-point">💡 IT之家 10 月 17 日消息，英伟达个人计算业务高级副总裁 Jeff Fisher 昨日在台北出席 RTX Spark 相关活动时回应了 R…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/entertainment/1013381/jad-abumrad-radiolab-dolly-parton-fela-kuti-podcast-interview" target="_blank" rel="noopener" data-cat="zonghe" data-summary="很难夸大Jad Abumrad对播客世界的影响。他创作并主持了多莉·帕顿（ Dolly Parton ）的《美国》（ America ）和《费拉·库蒂：无所畏惧》（ Fela Kuti: Fear No Man ） ，这是两部获得皮博迪奖（ Peabody Award ）的节目，前所未有" data-title="Jad Abumrad loves a butterfly knife and a good springy pillow" data-date="10-17 22:30" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-17 22:30</span>
          <span class="news-item-title">Jad Abumrad喜欢蝴蝶刀和弹簧枕头</span>
          <span class="news-item-title-en">Jad Abumrad loves a butterfly knife and a good springy pillow</span>
          <span class="news-value-point">💡 很难夸大Jad Abumrad对播客世界的影响</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/405.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 17 日消息，倍思现已在京东上架 2026 新国标 45W 自带双线移动电源，该产品采用 2C+1A+1Lightning 设计，匹配 20000mAh 电芯，定价为 202 元，首发价 171 元。京东倍思推出 20000mAh 45W 自带双线移动电源 171 元直达链接该移动电源整体重量 357g，尺寸为 68.2x111x32mm，采用磨砂阻燃塑料外壳，提供蓝 / 粉双色可选，机身正面顶部设计有一块粉色半透高光饰板，左侧为数显屏幕视窗，右侧为 45W 功率标识。移动电源顶部配备 1 根 USB-C 45W 及 1 根 Lightning 27W 线缆，机身配备 1 个 USB-C 45W 接口和 1 个 USB-A 33W 接口。IT之家附产品参数：" data-title="倍思推出 2026 新国标 45W 自带双线移动电源：2C+1A+1Lightning，20000mAh 电芯售 171 元" data-date="10-17 22:20" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-17 22:20</span>
          <span class="news-item-title">倍思推出 2026 新国标 45W 自带双线移动电源：2C+1A+1Lightning，20000mAh 电芯售 171 元</span>
          <span class="news-value-point">💡 IT之家 10 月 17 日消息，倍思现已在京东上架 2026 新国标 45W 自带双线移动电源，该产品采用 2C+1A+1Lightning …</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/podcast/1012416/spacex-starlink-elon-musk-cell-carrier-wireless-mobile-att-verizon-t-mobile" target="_blank" rel="noopener" data-cat="zonghe" data-summary="今天，我正在与LightShed Partners的合伙人兼分析师Walter Piecyk谈论SpaceX最近宣布的成为主要无线运营商的计划。上周， SpaceX同意购买一大块低频段" data-title="SpaceX’s ambitious, expensive gamble to replace AT&amp;T, T" data-date="10-17 22:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-17 22:00</span>
          <span class="news-item-title">SpaceX雄心勃勃，昂贵的赌博取代AT ＆ T ， T</span>
          <span class="news-item-title-en">SpaceX’s ambitious, expensive gamble to replace AT&T, T</span>
          <span class="news-value-point">💡 今天，我正在与LightShed Partners的合伙人兼分析师Walter Piecyk谈论SpaceX最近宣布的成为主要无线运营商的计划</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/sandisks-512gb-switch-2-ready-microsd-express-card-is-a-steal-for-usd98-during-sale-rare-tech-deal-arrives-to-beat-the-storage-shortage" target="_blank" rel="noopener" data-cat="zonghe" data-summary="希望下载更多游戏的任天堂Switch 2用户可以在闪迪官方授权的microSD Express卡上利用此优惠，该卡支持高达880 MB/s的读取速度，并提供512GB的容量。" data-title="Sandisk’s 512GB Switch 2-ready microSD Express card is a steal for $98 during sale" data-date="10-17 21:39" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-17 21:39</span>
          <span class="news-item-title">Sandisk的512GB Switch 2-ready microSD Express卡售价98 $</span>
          <span class="news-item-title-en">Sandisk’s 512GB Switch 2-ready microSD Express card is a steal for $98 during sale</span>
          <span class="news-value-point">💡 希望下载更多游戏的任天堂Switch 2用户可以在闪迪官方授权的microSD Express卡上利用此优惠，该卡支持高达880 MB/s的读取…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/400.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 17 日消息，今晚，2026 世界超级摩托车锦标赛（WSBK）第十二站 WorldSSP 组别首场正赛在西班牙赫雷兹赛道举行。中国摩托车制造商“张雪机车”的法国车手瓦伦丁 · 德比斯本场以第 10 名完赛，队友费德里科 · 卡里卡苏洛位列第 14 位。本站是 2026 赛季收官战。赛前，德比斯以总积分 291 分的成绩提前锁定本赛季车手年度总榜亚军。北京时间 10 月 18 日 20:00 将进行第二回合的较量，大家敬请期待。" data-title="2026 WSBK 西班牙站首回合：张雪机车德比斯获第 10 位" data-date="10-17 21:32" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-17 21:32</span>
          <span class="news-item-title">2026 WSBK 西班牙站首回合：张雪机车德比斯获第 10 位</span>
          <span class="news-value-point">💡 IT之家 10 月 17 日消息，今晚，2026 世界超级摩托车锦标赛（WSBK）第十二站 WorldSSP 组别首场正赛在西班牙赫雷兹赛道举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-17/10716400.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社贵阳10月17日电 (记者 周燕玲)17日，贵州省贵阳市观山湖区金元社区广场上，一名老人正缓缓打着太极，十多名美国青年在后面有模有样地学了起来；社区活动室内，老年合唱团排练《铃儿响叮当》，一名美国青年取出随身带的尤克里里加入伴奏，有人跟着节奏跳起舞，笑声和掌声混在一起。" data-title="美国青年贵州行：在社区看见真实中国 在抗战公路读懂合作共赢" data-date="10-17 21:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-17 21:15</span>
          <span class="news-item-title">美国青年贵州行：在社区看见真实中国 在抗战公路读懂合作共赢</span>
          <span class="news-value-point">💡 中新社贵阳10月17日电 (记者 周燕玲)17日，贵州省贵阳市观山湖区金元社区广场上，一名老人正缓缓打着太极，十多名美国青年在后面有模有样地学了…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/399.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 17 日消息，除了 6999 元的 ROG 八爪鱼 8 路由器之外，华硕本周还推出了一款配套的 ROG ZOOM 八类万兆电竞网线，提供 1.5 米和 3 米两个版本，售价分别为 299 元和 399 元。京东 ROG ZOOM CAT8 八类万兆电竞网线 / 3 米纯铜网络连接线家用电脑宽带成品网线 / 华硕 ROG 路由器适配网线 399 元直达链接华硕表示，这款网线支持 40Gbps 传输带宽、 2000MHz 载波频率，相比七类网线（10Gbps，600MHz）带宽整整提升 4 倍，slogan 为“一线之隔，高下立判”。这款网线采用 E/STP 双重屏蔽设计，拥有高隔绝性能可有效隔绝电缆串扰；网线外部采用高密度编织护套，充当铠装护体，耐磨、抗拉扯；线芯采用 26" data-title="华硕推出 ROG ZOOM 八类万兆电竞网线：1.5 米 299 元，3 米 399 元" data-date="10-17 21:15" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-17 21:15</span>
          <span class="news-item-title">华硕推出 ROG ZOOM 八类万兆电竞网线：1.5 米 299 元，3 米 399 元</span>
          <span class="news-value-point">💡 IT之家 10 月 17 日消息，除了 6999 元的 ROG 八爪鱼 8 路由器之外，华硕本周还推出了一款配套的 ROG ZOOM 八类万兆电…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-17/10716398.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京10月17日电 题：“救援先锋”王晓成：洪水中驾动力舟桥转移广西贵港被困师生" data-title="“救援先锋”王晓成：洪水中驾动力舟桥转移广西贵港被困师生" data-date="10-17 21:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-17 21:07</span>
          <span class="news-item-title">“救援先锋”王晓成：洪水中驾动力舟桥转移广西贵港被困师生</span>
          <span class="news-value-point">💡 中新网北京10月17日电 题：“救援先锋”王晓成：洪水中驾动力舟桥转移广西贵港被困师生</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-17 23:46（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
