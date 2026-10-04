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
      <span>2026-10-04 21:22 抓取更新</span>
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
        <span class="channel-count">47</span>
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
        <span class="channel-count">2</span>
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
  <div class="ov-item"><span class="ov-num">47</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×22 · IT之家×8</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/10-04/10707970.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="原标题：永不磨灭的印记 | 一张借谷证：见证红色政权的铮铮诺言" data-title="一张借谷证：见证红色政权的铮铮诺言" data-date="10-04 21:05" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-04 21:05</span>
      </div>
      <h2 class="hero-featured-title">一张借谷证：见证红色政权的铮铮诺言</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.tomshardware.com/tech-industry/robotics/ai-robot-company-decommissioned-its-robots-terminator-style-in-a-75-ton-vat-of-molten-steel-arnold-schwarzenegger-suggested-melting-them-one-robot-held-up-a-thumbs-up-sign-as-it-sank-into-molten-metal" target="_blank" rel="noopener" data-cat="keji" data-summary="人工智能机器人公司Figure找到了一种创新的方法，可以将其旧的F.02机队退役，而无需分配资源进行困难而耗时的拆卸。" data-title="AI robot company decommissioned its robots ‘Terminator-style’ in a 75-ton vat of molten steel" data-date="10-04 21:20" data-source="Tom's Hardware">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
      </div>
      <p class="hero-sub-title">AI robot company decommissioned its robots ‘Terminator-style’ in a 75-ton vat of molten steel</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/2026/oct/03/blank-instead-manchester-city-name-trophies-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="这些空间既是对贪婪时代的谴责，也是对英超联赛追求正义的致敬在2014年联赛杯决赛中场休息时，桑德兰以1比0领先曼城。Yaya Touré与休闲明亮的30码相媲美" data-title="Let there be blanks instead of Manchester City’s name on trophies: there was no honour there | Jonathan Wilson" data-date="10-04 03:00" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Let there be blanks instead of Manchester City’s name on trophies: there was no honour there | Jonathan Wilson</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/009/728.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 4 日消息，近期网络上流传一段所谓“乐山大佛开展养护作业”短视频，其中显示文保工人正在给大佛“掏耳朵”，佛耳里掏出鸽子和腐叶，鼻孔里清理出大量腐叶等物质，旁边还有一只猴子在佛身上上蹿下跳，猴子还抢工人的安全帽戴在自己头上。对此，乐山大佛文物保护（景区）管委会回应媒体“四川观察”，称相应视频不实，系他人 AI 生成，不是乐山大佛景区里的真实场景。希望广大网友不信谣、不传谣。乐山大佛文物保护（景区）管委会数字化信息中心副主任陈芮透露，“2026 年以来乐山大佛总计开展 5 次保养维护，其中第 5 次是 9 月 20 日至 25 日，主要内容包含岩体表面微损伤修复、微生物清理、表层植被清除等，与视频内容无关。同时，大佛耳鼻内并无杂物需要清理，乐山大佛所在的凌云山片区目前没有猴子" data-title="乐山大佛景区回应网传“掏耳朵”养护作业视频：系 AI 合成，佛耳内并无所谓“杂物”" data-date="10-04 21:20" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">乐山大佛景区回应网传“掏耳朵”养护作业视频：系 AI 合成，佛耳内并无所谓“杂物”</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707970.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="原标题：永不磨灭的印记 | 一张借谷证：见证红色政权的铮铮诺言" data-title="一张借谷证：见证红色政权的铮铮诺言" data-date="10-04 21:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 21:05</span>
          <span class="news-item-title">一张借谷证：见证红色政权的铮铮诺言</span>
          <span class="news-value-point">💡 原标题：永不磨灭的印记 | 一张借谷证：见证红色政权的铮铮诺言</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707941.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社伦敦10月4日电 (记者 欧阳开宇)英国政府4日发布消息称，英国皇家刑事法院待审积压案件创下历史新高，总量约8.1万宗，其中近三分之一案件等待审理时长超过一年。" data-title="英皇家刑事法院积压案件约8.1万宗" data-date="10-04 20:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 20:55</span>
          <span class="news-item-title">英皇家刑事法院积压案件约8.1万宗</span>
          <span class="news-value-point">💡 中新社伦敦10月4日电 (记者 欧阳开宇)英国政府4日发布消息称，英国皇家刑事法院待审积压案件创下历史新高，总量约8.1万宗，其中近三分之一案件…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707960.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月4日电 据路透社报道，当地时间10月4日，也门总统领导委员会主席、武装部队最高统帅拉沙德·穆罕默德·阿里米宣布启动大规模军事行动。" data-title="也门总统领导委员会主席宣布启动军事行动" data-date="10-04 20:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 20:49</span>
          <span class="news-item-title">也门总统领导委员会主席宣布启动军事行动</span>
          <span class="news-value-point">💡 中新网10月4日电 据路透社报道，当地时间10月4日，也门总统领导委员会主席、武装部队最高统帅拉沙德·穆罕默德·阿里米宣布启动大规模军事行动</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707956.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="视频：听英雄后代讲长征故事丨开国上将朱良才之子讲述长征路上的鱼水深情来源：新华网" data-title="听英雄后代讲长征故事丨开国上将朱良才之子讲述长征路上的鱼水深情" data-date="10-04 20:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 20:48</span>
          <span class="news-item-title">听英雄后代讲长征故事丨开国上将朱良才之子讲述长征路上的鱼水深情</span>
          <span class="news-value-point">💡 视频：听英雄后代讲长征故事丨开国上将朱良才之子讲述长征路上的鱼水深情来源：新华网</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/725.htm" target="_blank" rel="noopener" data-cat="shizheng" data-summary="IT之家 10 月 4 日消息，据新华社报道，记者 4 日从商务部获悉，国庆假期过半，全国消费市场平稳有序，生活必需品货足价稳。商务部商务大数据显示，国庆假期前三天（10 月 1 至 3 日），商务部重点监测的 78 个步行街（商圈）客流量、营业额同比分别增长 3.4%、5.3%。消费品以旧换新带动销售额 196.3 亿元，惠及 348.3 万人次。其中，汽车以旧换新 4.6 万辆，带动新车销售额 74.5 亿元；家电以旧换新 151.1 万台，带动销售额 65.0 亿元；数码和智能产品购新 170.9 万件，带动销售额 49.0 亿元。IT之家注意到，近日，国家发展改革委会同财政部，向地方下达了今年第四批 625 亿元超长期特别国债支持消费品以旧换新资金。至此，全年 2500 亿元消费品以" data-title="国庆假期前三天：汽车以旧换新 4.6 万辆、数码和智能产品购新 170.9 万件" data-date="10-04 20:46" data-source="IT之家">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-04 20:46</span>
          <span class="news-item-title">国庆假期前三天：汽车以旧换新 4.6 万辆、数码和智能产品购新 170.9 万件</span>
          <span class="news-value-point">💡 IT之家 10 月 4 日消息，据新华社报道，记者 4 日从商务部获悉，国庆假期过半，全国消费市场平稳有序，生活必需品货足价稳</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707899.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="爱国主义是中华民族精神的核心，是中国人民和中华民族同心同德、自强不息的精神纽带。党的十八大以来，习近平总书记在不同场合发表一系列重要讲话，生动阐述爱国主义的丰富内涵。一起学习感悟。" data-title="学习新语·家国同心｜怀爱国之心 立报国之志" data-date="10-04 20:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 20:28</span>
          <span class="news-item-title">学习新语·家国同心｜怀爱国之心 立报国之志</span>
          <span class="news-value-point">💡 爱国主义是中华民族精神的核心，是中国人民和中华民族同心同德、自强不息的精神纽带</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707939.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月4日电 美国内政部当地时间2日在社交媒体平台X发布照片并配文称，夏威夷火山国家公园标志性的霍莱海蚀拱门已坍塌并沉入太平洋，这标志着该公园偏远崎岖海岸线的又一次自然演变。" data-title="夏威夷标志性景观霍莱海蚀拱门“坍塌并沉入太平洋”" data-date="10-04 20:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 20:26</span>
          <span class="news-item-title">夏威夷标志性景观霍莱海蚀拱门“坍塌并沉入太平洋”</span>
          <span class="news-value-point">💡 中新网10月4日电 美国内政部当地时间2日在社交媒体平台X发布照片并配文称，夏威夷火山国家公园标志性的霍莱海蚀拱门已坍塌并沉入太平洋，这标志着该…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cr89zllz31wdo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="加拿大总理马克‧卡尼表示，军方正在制定应对方案，以防美国入侵加拿大这种不太可能发生的情况。" data-title="加拿大为何要为（概率极小的）美国入侵做准备" data-date="10-04 19:51" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-04 19:51</span>
          <span class="news-item-title">加拿大为何要为（概率极小的）美国入侵做准备</span>
          <span class="news-value-point">💡 加拿大总理马克‧卡尼表示，军方正在制定应对方案，以防美国入侵加拿大这种不太可能发生的情况</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707900.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月4日电 巴西2026年总统选举首轮投票于巴西利亚时间10月4日8时(北京时间19时)开始。" data-title="巴西2026年总统选举首轮投票开始" data-date="10-04 19:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 19:16</span>
          <span class="news-item-title">巴西2026年总统选举首轮投票开始</span>
          <span class="news-value-point">💡 中新网10月4日电 巴西2026年总统选举首轮投票于巴西利亚时间10月4日8时(北京时间19时)开始</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707895.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社快讯：巴西2026年总统选举首轮投票于巴西利亚时间4日8时(北京时间19时)开始。" data-title="巴西总统选举首轮投票开始" data-date="10-04 19:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 19:04</span>
          <span class="news-item-title">巴西总统选举首轮投票开始</span>
          <span class="news-value-point">💡 新华社快讯：巴西2026年总统选举首轮投票于巴西利亚时间4日8时(北京时间19时)开始</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707894.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="今天(10月4日)，我国喜马拉雅“8·26”极端地质灾害应急跨境科学考察队从成都启程赴尼泊尔，开展冰冻圈与岩石圈巨灾应急联合科考。本次科考共有十余家高校与科研院所50余名科研人员参加。" data-title="我国科学家赴尼泊尔开展联合科考 研判喜马拉雅冰冻灾害" data-date="10-04 18:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 18:52</span>
          <span class="news-item-title">我国科学家赴尼泊尔开展联合科考 研判喜马拉雅冰冻灾害</span>
          <span class="news-value-point">💡 今天(10月4日)，我国喜马拉雅“8·26”极端地质灾害应急跨境科学考察队从成都启程赴尼泊尔，开展冰冻圈与岩石圈巨灾应急联合科考</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707880.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="视频：跟着课本走长征丨90多年前，他们爬过这座老山界来源：新华社" data-title="跟着课本走长征丨90多年前，他们爬过这座老山界" data-date="10-04 18:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 18:04</span>
          <span class="news-item-title">跟着课本走长征丨90多年前，他们爬过这座老山界</span>
          <span class="news-value-point">💡 视频：跟着课本走长征丨90多年前，他们爬过这座老山界来源：新华社</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707841.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月4日电 综合消息：中东媒体4日报道称，也门政府军和胡塞武装在该国塔伊兹省持续激烈交火。" data-title="也门政府军与胡塞武装持续激烈交火" data-date="10-04 17:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 17:30</span>
          <span class="news-item-title">也门政府军与胡塞武装持续激烈交火</span>
          <span class="news-value-point">💡 中新社北京10月4日电 综合消息：中东媒体4日报道称，也门政府军和胡塞武装在该国塔伊兹省持续激烈交火</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707866.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月4日电 据俄罗斯媒体当地时间10月4日报道，俄罗斯联邦安全会议副主席梅德韦杰夫在个人社交账号上发文警告美方，不要应乌方要求“封锁”俄方“黎明”低轨卫星通信系统。" data-title="梅德韦杰夫警告美方勿封锁俄版“星链”系统" data-date="10-04 17:25" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 17:25</span>
          <span class="news-item-title">梅德韦杰夫警告美方勿封锁俄版“星链”系统</span>
          <span class="news-value-point">💡 中新网10月4日电 据俄罗斯媒体当地时间10月4日报道，俄罗斯联邦安全会议副主席梅德韦杰夫在个人社交账号上发文警告美方，不要应乌方要求“封锁”俄…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707863.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="拉丁美洲民调机构“拉丁美洲晴雨表”(Latinobarómetro)当地时间10月2日发布《2026年度报告》。调查显示，65%的拉美受访者认为中国对该地区的影响是积极的；相比之下，57%的受访者对美国的影响持积极评价。" data-title="全球媒体聚焦 | 拉美民众缘何对中国影响力的评价更积极" data-date="10-04 17:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 17:16</span>
          <span class="news-item-title">全球媒体聚焦 | 拉美民众缘何对中国影响力的评价更积极</span>
          <span class="news-value-point">💡 拉丁美洲民调机构“拉丁美洲晴雨表”(Latinobarómetro)当地时间10月2日发布《2026年度报告》</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/robotics/ai-robot-company-decommissioned-its-robots-terminator-style-in-a-75-ton-vat-of-molten-steel-arnold-schwarzenegger-suggested-melting-them-one-robot-held-up-a-thumbs-up-sign-as-it-sank-into-molten-metal" target="_blank" rel="noopener" data-cat="keji" data-summary="人工智能机器人公司Figure找到了一种创新的方法，可以将其旧的F.02机队退役，而无需分配资源进行困难而耗时的拆卸。" data-title="AI robot company decommissioned its robots ‘Terminator-style’ in a 75-ton vat of molten steel" data-date="10-04 21:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-04 21:20</span>
          <span class="news-item-title">人工智能机器人公司在75吨钢水桶中退役其机器人“终结者式”</span>
          <span class="news-item-title-en">AI robot company decommissioned its robots ‘Terminator-style’ in a 75-ton vat of molten steel</span>
          <span class="news-value-point">💡 人工智能机器人公司Figure找到了一种创新的方法，可以将其旧的F.02机队退役，而无需分配资源进行困难而耗时的拆卸</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/chatgpt-6-astra-cracks-217-year-old-napoleonic-code-in-just-six-hours-single-prompt-ai-run-solves-24-rows-of-custom-symbols-from-a-single-image-reveals-lost-troop-orders" target="_blank" rel="noopener" data-cat="keji" data-summary="一位人工智能工程师使用GPT-6 Astra揭示了自拿破仑战争以来从未被读取的密码的内容。这项任务是用一张图片和提示发起的，从开始到结束只花了六个小时。" data-title="ChatGPT-6 Astra cracks 217-year-old Napoleonic code in just six hours" data-date="10-04 21:08" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-04 21:08</span>
          <span class="news-item-title">ChatGPT-6 Astra在短短六小时内破解了217年前的拿破仑密码</span>
          <span class="news-item-title-en">ChatGPT-6 Astra cracks 217-year-old Napoleonic code in just six hours</span>
          <span class="news-value-point">💡 一位人工智能工程师使用GPT-6 Astra揭示了自拿破仑战争以来从未被读取的密码的内容</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/701.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 4 日消息，DeepSeek Harness 组成员崔添翼今日回应了“如何看待 DeepSeek Harness 在新版本中加入 Claude Code Mods 兼容？”，他本人是这次 v0.2.1-alpha.1 版本中加入 Claude Code Mods 兼容层的作者。目前 DeepSeek Harness 中的“Claude Code Mods 兼容层”属于“alpha 版本”中的“实验性功能”。做这个兼容层的主要目的，是验证 Claude Code Mods 向插件作者提供的扩展能力，是否大致是 DSH“一切皆插件”架构所提供能力的一个子集。目前还无法让所有 Claude Code Mods 在 DeepSeek Harness 中无缝运行；如果认为这是一个值" data-title="DeepSeek Harness 崔添翼：产品核心理念是“一切皆插件”，可扩展性是初心" data-date="10-04 20:27" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-04 20:27</span>
          <span class="news-item-title">DeepSeek Harness 崔添翼：产品核心理念是“一切皆插件”，可扩展性是初心</span>
          <span class="news-value-point">💡 IT之家 10 月 4 日消息，DeepSeek Harness 组成员崔添翼今日回应了“如何看待 DeepSeek Harness 在新版本中…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-torture-chamber-triggers-massive-backlash-for-putting-chatbots-in-simulated-pain-critics-issue-death-threats-while-anthropomorphizing-text-predictors-demand-github-remove-the-repository-over-unethical-treatment" target="_blank" rel="noopener" data-cat="keji" data-summary="人工智能“酷刑室”在网上招致大量批评和相应的嘲笑--科技新手和人工智能传道者疯狂地将法学硕士拟人化" data-title="&#39;AI Torture Chamber&#39; triggers massive backlash for putting chatbots in simulated pain" data-date="10-04 20:05" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-04 20:05</span>
          <span class="news-item-title">“人工智能酷刑室”引发强烈反对，将聊天机器人置于模拟的痛苦之中</span>
          <span class="news-item-title-en">'AI Torture Chamber' triggers massive backlash for putting chatbots in simulated pain</span>
          <span class="news-value-point">💡 人工智能“酷刑室”在网上招致大量批评和相应的嘲笑--科技新手和人工智能传道者疯狂地将法学硕士拟人化</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/501605.html" target="_blank" rel="noopener" data-cat="keji" data-summary="一种混搭的可能：英特尔继续供先进工艺，即前端用14A；后端再接台积电，来补工厂运营、良率、封装这些能力。" data-title="AI算力硬合作，马斯克还是更相信中国制造" data-date="10-04 14:12" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-04 14:12</span>
          <span class="news-item-title">AI算力硬合作，马斯克还是更相信中国制造</span>
          <span class="news-value-point">💡 一种混搭的可能：英特尔继续供先进工艺，即前端用14A</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/501506.html" target="_blank" rel="noopener" data-cat="keji" data-summary="什么是FDE？它会一直存在吗？" data-title="最火AI岗位FDE：月薪5万，都干这些…" data-date="10-04 14:05" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-04 14:05</span>
          <span class="news-item-title">最火AI岗位FDE：月薪5万，都干这些…</span>
          <span class="news-value-point">💡 什么是FDE</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/501451.html" target="_blank" rel="noopener" data-cat="keji" data-summary="专业3D模型反而更稀缺了" data-title="GPT-6要“吃掉”3D公司？这家公司不到2年ARR翻百倍，破1亿美元" data-date="10-04 08:53" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-04 08:53</span>
          <span class="news-item-title">GPT-6要“吃掉”3D公司？这家公司不到2年ARR翻百倍，破1亿美元</span>
          <span class="news-value-point">💡 专业3D模型反而更稀缺了</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/service-providers/streaming/7-year-old-nvidia-shield-tv-pro-gets-shocking-50-percent-price-hike-driven-by-ai-memory-shortage-chipmaker-axes-entry-level-shield-tv-as-component-prices-soar" target="_blank" rel="noopener" data-cat="keji" data-summary="Shield TV Pro仍然是英伟达运行时间最长的消费设备之一，但其299.99 $的价格标签现在使流媒体盒比推出时贵得多。" data-title="7-year-old Nvidia Shield TV Pro gets shocking 50% price hike driven by AI memory shortage" data-date="10-04 00:59" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-04 00:59</span>
          <span class="news-item-title">7年历史的Nvidia Shield TV Pro在人工智能内存短缺的推动下，价格上涨了50% ，令人震惊</span>
          <span class="news-item-title-en">7-year-old Nvidia Shield TV Pro gets shocking 50% price hike driven by AI memory shortage</span>
          <span class="news-value-point">💡 Shield TV Pro仍然是英伟达运行时间最长的消费设备之一，但其299.99 $的价格标签现在使流媒体盒比推出时贵得多</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/games/1004418/capcom-ai-game-development" target="_blank" rel="noopener" data-cat="keji" data-summary="Capcom的Pragmata可能完全是关于人工智能的恐怖，但在实践中，工作室似乎并不那么低调。在CAPCOM公开会议RE: 2026期间，程序员Satoshi Ishida发表了一篇演讲，题目是： “The Outlook a" data-title="Capcom is preparing for a ‘future where we create games together with AI’" data-date="10-04 00:49" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-04 00:49</span>
          <span class="news-item-title">Capcom正在为“我们与人工智能一起创造游戏的未来”做准备</span>
          <span class="news-item-title-en">Capcom is preparing for a ‘future where we create games together with AI’</span>
          <span class="news-value-point">💡 Capcom的Pragmata可能完全是关于人工智能的恐怖，但在实践中，工作室似乎并不那么低调</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/03/openai-safety-employee-resigns-claiming-the-companys-culture-is-broken/" target="_blank" rel="noopener" data-cat="keji" data-summary="大卫·罗宾逊（ David Robinson ）自己承认，他“有些陈词滥调” ：一家领先的人工智能公司的员工在辞职时发出可怕的警告。" data-title="OpenAI safety employee resigns, claiming the company’s ‘culture is broken’" data-date="10-04 00:30" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-04 00:30</span>
          <span class="news-item-title">OpenAI安全员工辞职，声称公司的“文化被打破”</span>
          <span class="news-item-title-en">OpenAI safety employee resigns, claiming the company’s ‘culture is broken’</span>
          <span class="news-value-point">💡 大卫·罗宾逊（ David Robinson ）自己承认，他“有些陈词滥调” ：一家领先的人工智能公司的员工在辞职时发出可怕的警告</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/580.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 4 日消息，在 10 月 1 日的华为 Mate 90 系列及全场景新品发布会上，华为年度旗舰 Mate 90 系列手机正式发布。其中，Mate 90 Pro Max / RS 非凡大师搭载的是首款逻辑折叠 τ 芯片 —— 麒麟 9050 Pro。根据华为官方介绍，麒麟 9050 Pro 是麒麟性能新巅峰，通过软硬芯云垂直整合，整机性能提升 31%。这枚芯片 CPU 还支持 9 核 16 线程超线程技术，多核性能提升 23%、GPU 渲染性能提升 40%、NPU 性能提升 140%。极客湾发布了一期针对华为 Mate 90 Pro Max 的性能分析报告，讲解了麒麟 9050 Pro 的逻辑折叠是如何实现，并公开了 Mate 90 Pro Max 的实际性能续航表现。需要" data-title="华为 Mate 90 Pro Max 性能解禁：搭载麒麟 9050 Pro，部分游戏能效优于第五代骁龙 8 至尊版机型" data-date="10-04 00:20" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-04 00:20</span>
          <span class="news-item-title">华为 Mate 90 Pro Max 性能解禁：搭载麒麟 9050 Pro，部分游戏能效优于第五代骁龙 8 至尊版机型</span>
          <span class="news-value-point">💡 IT之家 10 月 4 日消息，在 10 月 1 日的华为 Mate 90 系列及全场景新品发布会上，华为年度旗舰 Mate 90 系列手机正式…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/elon-musk-confirms-discussions-with-tsmc-about-terafab-chipmaking-collaboration-intel-is-the-only-other-named-partner-terafab-to-exclusively-supply-tesla-spacex-and-xai" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道， Elon Musk和台积电讨论了Terafab项目中的多个合作机会。" data-title="Elon Musk confirms discussions with TSMC about Terafab chipmaking collaboration" data-date="10-03 22:50" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-03 22:50</span>
          <span class="news-item-title">Elon Musk确认与台积电就Terafab芯片制造合作进行讨论</span>
          <span class="news-item-title-en">Elon Musk confirms discussions with TSMC about Terafab chipmaking collaboration</span>
          <span class="news-value-point">💡 据报道， Elon Musk和台积电讨论了Terafab项目中的多个合作机会</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/576.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 3 日消息，海马云 (haimacloud) 近日推出了 haimacloud GEAR 端云混合掌机。其本地采用高通骁龙 865 移动平台，运行 Android 13 操作系统，支持海马云的云游戏服务。该掌机拥有 8GB + 128GB 的存储器组合，搭配 7&quot; FHD 144Hz 2ms 800nits OLED 屏幕，内置 8000mAh 电池，具备主动散热、TMR 摇杆、霍尔扳机、机械微动按键、六轴体感，ABXY 为模块化设计，支持 Wi-Fi 6 &amp; BT 5.1，质量 450g。IT之家获悉，配套的云游戏服务基于英特尔酷睿 i7-12700KF 处理器、&quot;70&quot; 级 NVIDIA GeForce RTX 显卡，支持 1080p 144FPS。haimaclou" data-title="海马云推出 haimacloud GEAR 端云混合掌机：高通骁龙 865，硬件首发价 3149 元" data-date="10-03 22:47" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-03 22:47</span>
          <span class="news-item-title">海马云推出 haimacloud GEAR 端云混合掌机：高通骁龙 865，硬件首发价 3149 元</span>
          <span class="news-value-point">💡 IT之家 10 月 3 日消息，海马云 (haimacloud) 近日推出了 haimacloud GEAR 端云混合掌机</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1004408/openai-safety-quits-sounding-the-alarm" target="_blank" rel="noopener" data-cat="keji" data-summary="大卫·罗宾逊（ David Robinson ）曾在OpenAI的每个主要模型版本中撰写安全报告。本周，他辞去了职务，现在正在《大西洋月刊》的一篇社论中发表讲话。如果你觉得有点愤世嫉俗是可以理解的" data-title="An OpenAI safety employee has quit and is sounding the alarm" data-date="10-03 22:31" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-03 22:31</span>
          <span class="news-item-title">OpenAI安全员工已辞职并正在敲响警钟</span>
          <span class="news-item-title-en">An OpenAI safety employee has quit and is sounding the alarm</span>
          <span class="news-value-point">💡 大卫·罗宾逊（ David Robinson ）曾在OpenAI的每个主要模型版本中撰写安全报告</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/03/all-the-ai-agents-that-can-live-in-your-text-messages/" target="_blank" rel="noopener" data-cat="keji" data-summary="我们创建了一个列表，列出了可以在短信中出现的最著名的人工智能客服代表，从一般助理到专为家庭、旅行和工作而设计的客服代表。" data-title="All the AI agents that can live in your text messages" data-date="10-03 22:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-03 22:00</span>
          <span class="news-item-title">所有可以存在于您的短信中的人工智能代理</span>
          <span class="news-item-title-en">All the AI agents that can live in your text messages</span>
          <span class="news-value-point">💡 我们创建了一个列表，列出了可以在短信中出现的最著名的人工智能客服代表，从一般助理到专为家庭、旅行和工作而设计的客服代表</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">2 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/03/blank-instead-manchester-city-name-trophies-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="这些空间既是对贪婪时代的谴责，也是对英超联赛追求正义的致敬在2014年联赛杯决赛中场休息时，桑德兰以1比0领先曼城。Yaya Touré与休闲明亮的30码相媲美" data-title="Let there be blanks instead of Manchester City’s name on trophies: there was no honour there | Jonathan Wilson" data-date="10-04 03:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-04 03:00</span>
          <span class="news-item-title">让奖杯上有空白而不是曼城的名字：那里没有荣誉|乔纳森·威尔逊</span>
          <span class="news-item-title-en">Let there be blanks instead of Manchester City’s name on trophies: there was no honour there | Jonathan Wilson</span>
          <span class="news-value-point">💡 这些空间既是对贪婪时代的谴责，也是对英超联赛追求正义的致敬在2014年联赛杯决赛中场休息时，桑德兰以1比0领先曼城</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/577.htm" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="IT之家 10 月 3 日消息，2026 爱知-名古屋亚运会男足三四名决赛，中国队在常规时间内 2 比 2 战平乌兹别克斯坦队。点球大战中，中国队 4 比 3 取胜，获得本次亚运会男足比赛铜牌。上半场，中国队胡荷韬破门。半场结束，中国男足与对手 1-1 战平。下半场，中国队王钰栋破门。90 分钟双方战成 2-2。这也是中国队时隔 28 年再次获得亚运会男足比赛铜牌！也是亚运会男足项目实行 U23 年龄限制后，中国队首次获得奖牌。IT之家查询获悉，中国男足曾在 1994 年广岛亚运会上获得银牌，并于 1978 年、1998 年两次获得铜牌。本届比赛，中国队时隔 28 年再次闯入亚运会男足四强，并最终登上领奖台。另外，今年 1 月，在 2026 年 U23 亚洲杯半决赛中，中国 U23 男足以" data-title="点球大战制胜！国足击败乌兹别克斯坦队，时隔 28 年再夺亚运会男足比赛铜牌" data-date="10-03 22:51" data-source="IT之家">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-03 22:51</span>
          <span class="news-item-title">点球大战制胜！国足击败乌兹别克斯坦队，时隔 28 年再夺亚运会男足比赛铜牌</span>
          <span class="news-value-point">💡 IT之家 10 月 3 日消息，2026 爱知-名古屋亚运会男足三四名决赛，中国队在常规时间内 2 比 2 战平乌兹别克斯坦队</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/009/728.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 4 日消息，近期网络上流传一段所谓“乐山大佛开展养护作业”短视频，其中显示文保工人正在给大佛“掏耳朵”，佛耳里掏出鸽子和腐叶，鼻孔里清理出大量腐叶等物质，旁边还有一只猴子在佛身上上蹿下跳，猴子还抢工人的安全帽戴在自己头上。对此，乐山大佛文物保护（景区）管委会回应媒体“四川观察”，称相应视频不实，系他人 AI 生成，不是乐山大佛景区里的真实场景。希望广大网友不信谣、不传谣。乐山大佛文物保护（景区）管委会数字化信息中心副主任陈芮透露，“2026 年以来乐山大佛总计开展 5 次保养维护，其中第 5 次是 9 月 20 日至 25 日，主要内容包含岩体表面微损伤修复、微生物清理、表层植被清除等，与视频内容无关。同时，大佛耳鼻内并无杂物需要清理，乐山大佛所在的凌云山片区目前没有猴子" data-title="乐山大佛景区回应网传“掏耳朵”养护作业视频：系 AI 合成，佛耳内并无所谓“杂物”" data-date="10-04 21:20" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-04 21:20</span>
          <span class="news-item-title">乐山大佛景区回应网传“掏耳朵”养护作业视频：系 AI 合成，佛耳内并无所谓“杂物”</span>
          <span class="news-value-point">💡 IT之家 10 月 4 日消息，近期网络上流传一段所谓“乐山大佛开展养护作业”短视频，其中显示文保工人正在给大佛“掏耳朵”，佛耳里掏出鸽子和腐叶…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707973.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="新华社重庆10月3日电 题：重庆：焕新历史街巷唤醒城市记忆" data-title="重庆：焕新历史街巷唤醒城市记忆" data-date="10-04 21:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 21:10</span>
          <span class="news-item-title">重庆：焕新历史街巷唤醒城市记忆</span>
          <span class="news-value-point">💡 新华社重庆10月3日电 题：重庆：焕新历史街巷唤醒城市记忆</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/727.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 4 日消息，开发商 Fuse Games 旗下《星球大战》IP 竞速游戏《星球大战：银河赛车手（STAR WARS：Galactic Racer）》将于 10 月 6 日正式发售，目前本作全球媒体评分已解禁。截至IT之家发稿，本作 PC 版在 Metacritic 上获 84 分（基于 16 家媒体评分）、XBOX Series X 版获 96 分（基于 12 家媒体评分）、PS5 版获 88 分（基于 60 家媒体评分）。IGN 给予本作 8 分，认为游戏机制较有特色，但长时间游玩后容易厌倦：《星球大战：银河赛车手》最大的特色是融合 Roguelite 元素的赛季式玩法。比赛过程中无法重新开始或倒带，失误和失败都需要自行承担后果，一旦在赛季中途落败，就必须重新进行当前阶" data-title="竞速游戏《星球大战：银河赛车手》获 IGN 8 分评价，10 月 6 日发售" data-date="10-04 21:09" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-04 21:09</span>
          <span class="news-item-title">竞速游戏《星球大战：银河赛车手》获 IGN 8 分评价，10 月 6 日发售</span>
          <span class="news-value-point">💡 IT之家 10 月 4 日消息，开发商 Fuse Games 旗下《星球大战》IP 竞速游戏《星球大战：银河赛车手（STAR WARS：Gala…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707971.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网三亚10月4日电 (张月和)“我很喜欢舞狮和画中国画。”三亚之行给新西兰奥克兰派恩赫斯特学校学生多里安(Dorian)留下了深刻印象，“画中国画十分有趣且别具特色，在新西兰我们体验不到这类活动；舞狮也特别酷，对我们而言这算是一种全新的体验”。" data-title="新西兰青少年的三亚之行：文化体验中感知中国" data-date="10-04 21:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 21:09</span>
          <span class="news-item-title">新西兰青少年的三亚之行：文化体验中感知中国</span>
          <span class="news-value-point">💡 中新网三亚10月4日电 (张月和)“我很喜欢舞狮和画中国画</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707967.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="原标题：我的铁路风景｜候车室里搭“文化集市”，将赣西三地风光送到旅客身边！" data-title="候车室里搭“文化集市”，将赣西三地风光送到旅客身边！" data-date="10-04 21:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 21:02</span>
          <span class="news-item-title">候车室里搭“文化集市”，将赣西三地风光送到旅客身边！</span>
          <span class="news-value-point">💡 原标题：我的铁路风景｜候车室里搭“文化集市”，将赣西三地风光送到旅客身边</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1004242/airpods-pro-3-amazon-october-prime-day-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="我们已经有一段时间没有在Apple AirPods Pro 3上看到很好的折扣了，但就像最新的iPad Mini和M5 MacBook Airs一样， 10月Prime Day现在正在发生一个很棒的折扣。您可以抢购一对降噪耳机，其中包括" data-title="The AirPods Pro 3 are a fantastic deal at $179" data-date="10-04 21:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-04 21:00</span>
          <span class="news-item-title">AirPods Pro 3非常划算，售价179 $</span>
          <span class="news-item-title-en">The AirPods Pro 3 are a fantastic deal at $179</span>
          <span class="news-value-point">💡 我们已经有一段时间没有在Apple AirPods Pro 3上看到很好的折扣了，但就像最新的iPad Mini和M5 MacBook Airs…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707936.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网宁波10月4日电(林波)10月4日，宁波辣味海鲜争霸赛预热展示活动在浙江宁波举行，16家旅游饭店同台亮相，名厨现场掌勺展演辣味海鲜烹制技艺，首期《宁波辣味海鲜美食地图》同步对外发布。" data-title="浙江宁波举办辣味海鲜争霸赛 开辟鲜辣美食赛道" data-date="10-04 21:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 21:00</span>
          <span class="news-item-title">浙江宁波举办辣味海鲜争霸赛 开辟鲜辣美食赛道</span>
          <span class="news-value-point">💡 中新网宁波10月4日电(林波)10月4日，宁波辣味海鲜争霸赛预热展示活动在浙江宁波举行，16家旅游饭店同台亮相，名厨现场掌勺展演辣味海鲜烹制技艺…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/726.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 4 日消息，拉瑞安工作室宣布，为了感谢中国玩家一直以来的支持，《博德之门 3》将在本次 10 月促销活动结束后降价。游戏基础版从 298 元下调至 268 元。目前，《博德之门 3》正在 Steam 秋季特卖中进行促销，7 折后到手价为 208.6 元，活动预计将于 10 月 9 日结束。IT之家附游戏商品页（https://store.steampowered.com/app/1086940/3/）。游戏图赏：" data-title="拉瑞安工作室：《博德之门 3》Steam 国区即将永久降价：298 元起 → 268 元起" data-date="10-04 20:58" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-04 20:58</span>
          <span class="news-item-title">拉瑞安工作室：《博德之门 3》Steam 国区即将永久降价：298 元起 → 268 元起</span>
          <span class="news-value-point">💡 IT之家 10 月 4 日消息，拉瑞安工作室宣布，为了感谢中国玩家一直以来的支持，《博德之门 3》将在本次 10 月促销活动结束后降价</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707965.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="原标题：追光的你丨百姓的“小确幸”绘就城市幸福底色" data-title="百姓的“小确幸”绘就城市幸福底色" data-date="10-04 20:58" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 20:58</span>
          <span class="news-item-title">百姓的“小确幸”绘就城市幸福底色</span>
          <span class="news-value-point">💡 原标题：追光的你丨百姓的“小确幸”绘就城市幸福底色</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/cyber-security/iranian-national-extradited-to-us-over-alleged-usd3-4-billion-state-backed-hacking-campaign-in-rare-legal-win-for-law-enforcement-operative-helped-steal-31-terabytes-of-data-from-over-300-universities" target="_blank" rel="noopener" data-cat="zonghe" data-summary="一名伊朗-土耳其男子因涉嫌参与针对数百所大学、公司和政府机构的黑客活动并窃取了超过31 TB的学术数据而被从黑山引渡到美国。" data-title="Iranian national extradited to US over alleged $3.4 billion state-backed hacking campaign in rare legal win for law enforcement" data-date="10-04 20:55" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-04 20:55</span>
          <span class="news-item-title">伊朗国民因涉嫌$ 34亿国家支持的黑客活动而被引渡到美国，这是执法部门罕见的合法胜利</span>
          <span class="news-item-title-en">Iranian national extradited to US over alleged $3.4 billion state-backed hacking campaign in rare legal win for law enforcement</span>
          <span class="news-value-point">💡 一名伊朗-土耳其男子因涉嫌参与针对数百所大学、公司和政府机构的黑客活动并窃取了超过31 TB的学术数据而被从黑山引渡到美国</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707959.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="如果说馆藏典籍是读懂中国的钥匙，那么中央民族大学图书馆的万千文献，就藏着中华民族多元一体、交融共生的历史密码，实证着各民族休戚与共、同心报国的千年脉络。" data-title="校馆弦歌丨中央民族大学图书馆：万卷藏珍 同心报国" data-date="10-04 20:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 20:50</span>
          <span class="news-item-title">校馆弦歌丨中央民族大学图书馆：万卷藏珍 同心报国</span>
          <span class="news-value-point">💡 如果说馆藏典籍是读懂中国的钥匙，那么中央民族大学图书馆的万千文献，就藏着中华民族多元一体、交融共生的历史密码，实证着各民族休戚与共、同心报国的千…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707947.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京10月4日电 (记者 贾天勇)记者从北京站获悉：2026年中秋节、国庆节运输期自9月23日起至10月8日止，共计16天。在此期间北京站全站预计发送旅客203.5万人。" data-title="北京站便民服务提质升级助力国庆铁路运输" data-date="10-04 20:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 20:49</span>
          <span class="news-item-title">北京站便民服务提质升级助力国庆铁路运输</span>
          <span class="news-value-point">💡 中新网北京10月4日电 (记者 贾天勇)记者从北京站获悉：2026年中秋节、国庆节运输期自9月23日起至10月8日止，共计16天</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707923.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社南京10月4日电 (记者 徐珊珊)一股冷空气4日自北向南影响长三角地区，带来降温、大风和降雨。随着气温持续走低，沪苏浙皖多地正式迈入秋天门槛，浙江杭州、宁波等地相继官宣入秋，江苏也有望在近期全面入秋。" data-title="长三角多地官宣入秋 冷空气携降温大风登场" data-date="10-04 20:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 20:47</span>
          <span class="news-item-title">长三角多地官宣入秋 冷空气携降温大风登场</span>
          <span class="news-value-point">💡 中新社南京10月4日电 (记者 徐珊珊)一股冷空气4日自北向南影响长三角地区，带来降温、大风和降雨</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707919.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社福建宁德10月4日电 (叶茂 秦红丽)“宁台一家亲”乒乓球邀请赛4日在福建省宁德福安市举行，闽台两地10支队伍同台竞技，以球会友。" data-title="闽台乒乓球选手以球会友促交融" data-date="10-04 20:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 20:44</span>
          <span class="news-item-title">闽台乒乓球选手以球会友促交融</span>
          <span class="news-value-point">💡 中新社福建宁德10月4日电 (叶茂 秦红丽)“宁台一家亲”乒乓球邀请赛4日在福建省宁德福安市举行，闽台两地10支队伍同台竞技，以球会友</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1000832/macbook-air-m5-amazon-prime-big-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="亚马逊的10月黄金日有效地遏制了苹果6月份的价格上涨。配备M5芯片和512GB存储空间的13英寸MacBook Air通常售价为1,299美元，在亚马逊上以1,099美元的价格出售。对于具有sig的机器来说，这是一个更可口的价格" data-title="The MacBook Air M5 is $200 off for the first time in months" data-date="10-04 20:34" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-04 20:34</span>
          <span class="news-item-title">MacBook Air M5几个月来首次折扣$ 200</span>
          <span class="news-item-title-en">The MacBook Air M5 is $200 off for the first time in months</span>
          <span class="news-value-point">💡 亚马逊的10月黄金日有效地遏制了苹果6月份的价格上涨</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-04 21:22（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
