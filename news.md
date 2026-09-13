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
      <span>2026-09-13 20:48 抓取更新</span>
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
        <span class="channel-count">60</span>
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
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('zonghe', this)">
        <span>📰 综合与社会</span>
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('meimei', this)">
        <span>🌍 西方媒体视角</span>
        <span class="channel-count">0</span>
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
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/09-13/10695812.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网漳州9月13日电 (刘晨欣)12 日，福建漳州举办“侨批连两岸·家国共团圆”——在漳台胞台属迎中秋、庆国庆活动。在漳台胞、两岸婚姻家庭代表等近30人参会，活动旨为增进两岸亲情、促进漳台同胞心灵契合。" data-title="福建漳州举办台胞台属迎中秋、庆国庆活动" data-date="09-13 20:49" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 09-13 20:49</span>
      </div>
      <h2 class="hero-featured-title">福建漳州举办台胞台属迎中秋、庆国庆活动</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.nytimes.com/2026/09/13/us/politics/ai-catastrophe-fears-washington.html" target="_blank" rel="noopener" data-cat="keji" data-summary="特朗普总统一直走在“我担心什么”人群的最前沿，拒绝参与如何平衡人工智能的风险和回报。" data-title="随着对人工智能灾难的恐惧放大，华盛顿搅拌，但主要是沉睡" data-date="09-13 20:45" data-source="纽约时报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
      </div>
      <p class="hero-sub-title">随着对人工智能灾难的恐惧放大，华盛顿搅拌，但主要是沉睡</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/2026/sep/13/how-to-watch-premier-league-manchester-united-manchester-city" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联和曼城今天的表现如何？以下是需要了解的内容，包括开球时间、电视频道和直播选项本赛季的第一场曼彻斯特德比对两家俱乐部来说都是一个有趣的时刻。曼城在新任经理恩佐·马雷斯卡（ Enzo Maresca ）的领导下正在建立势头，而曼联正试图从一个对他们的转会市场策略提出质疑的夏天继续前进。在他们的三场比赛中每场都承认了两个进球" data-title="今日英超赛程：如何观看、收看电视频道和直播" data-date="09-13 19:00" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">今日英超赛程：如何观看、收看电视频道和直播</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/001/845.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 13 日消息，在稍早前结束的《CS2》裂变天地 S3 苏州站决赛中，巴西战队 Legacy 以 3:0 的大比分横扫 G2 Esports 赢得冠军荣誉。IT之家注意到，Legacy 此前已在中国拿下 2025、2026 两年的《CS》亚洲邀请赛 (CAC) 头名。中国无疑是这支战队福地，甚至队伍官方也将中国视为其“第二主场”。" data-title="实乃福地！Legacy 赢得《CS2》裂变天地 S3 苏州站冠军" data-date="09-13 20:44" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">实乃福地！Legacy 赢得《CS2》裂变天地 S3 苏州站冠军</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-13/10695812.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网漳州9月13日电 (刘晨欣)12 日，福建漳州举办“侨批连两岸·家国共团圆”——在漳台胞台属迎中秋、庆国庆活动。在漳台胞、两岸婚姻家庭代表等近30人参会，活动旨为增进两岸亲情、促进漳台同胞心灵契合。" data-title="福建漳州举办台胞台属迎中秋、庆国庆活动" data-date="09-13 20:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-13 20:49</span>
          <span class="news-item-title">福建漳州举办台胞台属迎中秋、庆国庆活动</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-13/10695808.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月13日电 据重庆市纪委监委消息：重庆市政府办公厅副主任陶晓锋涉嫌严重违纪违法，目前正接受重庆市纪委监委纪律审查和监察调查。" data-title="重庆市政府办公厅副主任陶晓锋接受审查调查" data-date="09-13 20:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-13 20:44</span>
          <span class="news-item-title">重庆市政府办公厅副主任陶晓锋接受审查调查</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/13/us/politics/paxton-corruption-impeachment-trial.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="现在竞选美国参议院议员的德克萨斯州总检察长帕克斯顿被指控滥用其办公室的权力来保护竞选捐赠者。他在所有罪名上都被宣告无罪。" data-title="威胁结束肯·帕克斯顿政治生涯的弹劾审判内幕" data-date="09-13 20:39" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-13 20:39</span>
          <span class="news-item-title">威胁结束肯·帕克斯顿政治生涯的弹劾审判内幕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-13/10695800.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京9月13日电 (记者 陈杭)北京市第十六届人民代表大会常务委员会第二十六次会议近日通过《北京市人民代表大会常务委员会关于进一步促进民族团结进步的决定》(下称决定)。决定自公布之日起施行。" data-title="北京立法促进民族团结进步 以首善标准建设示范城市" data-date="09-13 20:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-13 20:39</span>
          <span class="news-item-title">北京立法促进民族团结进步 以首善标准建设示范城市</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-13/10695731.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间9月13日，国家主席习近平在印度新德里出席金砖国家领导人第十八次会晤第二阶段会议，并发表题为《筑牢金砖合作根基 壮大全球南方力量》的重要讲话。习近平指出——" data-title="习言道｜“强权即公理”的逻辑行不通、早就应该摒弃" data-date="09-13 19:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-13 19:12</span>
          <span class="news-item-title">习言道｜“强权即公理”的逻辑行不通、早就应该摒弃</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cg7knkpjr39o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="金砖峰会《新德里宣言》呼吁对伊朗战争“最大克制”却不点名美国。而习近平七年首访印度，中印关系解冻了吗？" data-title="习近平七年再访印度：金砖峰会握手背后，中印关系破冰？" data-date="09-13 18:56" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-13 18:56</span>
          <span class="news-item-title">习近平七年再访印度：金砖峰会握手背后，中印关系破冰？</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-13/10695732.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="伊朗外长阿拉格齐13日在接受采访时表示，14日在阿曼举行的会议将重点讨论霍尔木兹海峡内一条新的海上通道。伊朗届时将向与会国家介绍伊朗与阿曼达成的相关协议细节及新通道路线图。" data-title="伊朗将与相关国家讨论霍尔木兹海峡内新通道" data-date="09-13 18:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-13 18:54</span>
          <span class="news-item-title">伊朗将与相关国家讨论霍尔木兹海峡内新通道</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-13/10695720.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间9月13日上午，国家主席习近平在新德里出席金砖国家领导人第十八次会晤第二阶段会议，并发表题为《筑牢金砖合作根基#8195;壮大全球南方力量》的重要讲话。他指出——" data-title="习近平：共同书写全球南方团结自强新篇章" data-date="09-13 17:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-13 17:56</span>
          <span class="news-item-title">习近平：共同书写全球南方团结自强新篇章</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-13/10695678.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月13日电 德黑兰消息：当地时间9月13日，伊朗一艘商船在南部格什姆岛附近遭袭，造成1人死亡、3人受伤。" data-title="伊朗一商船在南部格什姆岛遭袭致1死3伤" data-date="09-13 17:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-13 17:12</span>
          <span class="news-item-title">伊朗一商船在南部格什姆岛遭袭致1死3伤</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/13/us/politics/angie-nixon-florida-senate.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="民主党参议院候选人在一个明显倾向于共和党的州面临强大阻力。多年来，她一直是一名斗士，也是一名失败者。" data-title="安吉·尼克松（ Angie Nixon ） ，参议院候选人，风暴夺取佛罗里达州" data-date="09-13 17:03" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-13 17:03</span>
          <span class="news-item-title">安吉·尼克松（ Angie Nixon ） ，参议院候选人，风暴夺取佛罗里达州</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/13/world/middleeast/iran-hard-liners-sabotaged-peace-deal.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="政权内部人士说，反对者秘密袭击霍尔木兹海峡的船只，破坏了协议。伊朗总统在发现此事时非常愤怒。" data-title="伊朗的强硬派如何破坏与特朗普的和平协议" data-date="09-13 17:02" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-13 17:02</span>
          <span class="news-item-title">伊朗的强硬派如何破坏与特朗普的和平协议</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-13/10695651.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网苏州9月13日电 (记者 薛凌桥)“在走访上海市和江苏省后，我深刻感悟了城市发展、公共空间与生活质量之间的内在联系。同时，此次行程也帮助我们进一步理解了城市应当如何在应对变化的同时保持自身特色、回应社区需求。”" data-title="从“polis”到“市民”：塞浦路斯驻华大使感悟中西城市治理理念共鸣" data-date="09-13 16:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-13 16:05</span>
          <span class="news-item-title">从“polis”到“市民”：塞浦路斯驻华大使感悟中西城市治理理念共鸣</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-13/10695585.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社雅加达9月13日电 (记者 李志全)印度尼西亚一艘载有243人的客轮13日在爪哇海海域失联。" data-title="印尼一艘载有243人的客轮在爪哇海失联" data-date="09-13 14:58" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-13 14:58</span>
          <span class="news-item-title">印尼一艘载有243人的客轮在爪哇海失联</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-13/10695629.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社新德里9月13日电" data-title="习近平在金砖国家领导人第十八次会晤第二阶段会议的讲话（全文）" data-date="09-13 14:38" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-13 14:38</span>
          <span class="news-item-title">习近平在金砖国家领导人第十八次会晤第二阶段会议的讲话（全文）</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-13/10695627.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社新德里9月13日电(记者李忠发#8195;韩墨)当地时间9月13日上午，国家主席习近平在新德里出席金砖国家领导人第十八次会晤第二阶段会议，并发表题为《筑牢金砖合作根基#8195;壮大全球南方力量》的重要讲话。" data-title="习近平出席金砖国家领导人第十八次会晤第二阶段会议并发表重要讲话" data-date="09-13 14:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-13 14:24</span>
          <span class="news-item-title">习近平出席金砖国家领导人第十八次会晤第二阶段会议并发表重要讲话</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/09/13/us/politics/ai-catastrophe-fears-washington.html" target="_blank" rel="noopener" data-cat="keji" data-summary="特朗普总统一直走在“我担心什么”人群的最前沿，拒绝参与如何平衡人工智能的风险和回报。" data-title="随着对人工智能灾难的恐惧放大，华盛顿搅拌，但主要是沉睡" data-date="09-13 20:45" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-13 20:45</span>
          <span class="news-item-title">随着对人工智能灾难的恐惧放大，华盛顿搅拌，但主要是沉睡</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/843.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 13 日消息，谷歌 DeepMind 研究员乔希 · 恩格尔斯（Josh Engels）已离开公司的通用人工智能安全团队，加入独立 AI 评估机构 METR。他表示，自己认为未来五年内 AI 系统造成巨大危害的概率“高得吓人”。此事进一步加剧了外界对 AI 研发速度的担忧。恩格尔斯在 X 平台发文称，尽管他很喜欢在 DeepMind 的工作，并且拒绝了 Anthropic 和 OpenAI 的邀约，但他还是在三周前离开了 DeepMind，因为他认为先进人工智能相关的风险已经变得太高了。“所有 AI 企业都在致力于打造超级智能。”他写道。他警告，递归自我提升（RSI）—— 也就是 AI 系统辅助迭代出能力更强的下一代 AI 模型，如果对齐技术跟不上模型能力的增长，就会产生危" data-title="谷歌 DeepMind 安全研究员离职，称 AI 五年内造成巨大危害的概率高得吓人" data-date="09-13 20:21" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-13 20:21</span>
          <span class="news-item-title">谷歌 DeepMind 安全研究员离职，称 AI 五年内造成巨大危害的概率高得吓人</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/841.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 13 日消息，当地时间 9 月 13 日，适用于 macOS 和 Linux 的开源包管理器 Homebrew 发布了 7.0.0 大版本更新。Homebrew 是一个免费且开源的工具，能通过终端（Terminal）输入简单的指令，来快速安装、卸载、更新和管理电脑上的各种软件及开发工具。IT之家整理 Homebrew 7.0.0 主要升级内容如下：进一步提升了安装与升级速度强化了沙箱隔离机制推出原生 macOS 应用程序（brew install homebrew-app）内置安全漏洞检查功能与安全通告数据库正式终止对 macOS 10.15 及更早版本的支持基于 Intel 处理器的 Mac 机型降级至 Tier 3 等级支持（计划支持截止时间为 2027 年 9 月 1" data-title="开源包管理器 Homebrew 7.0.0 发布，推出原生苹果 macOS App" data-date="09-13 20:10" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-13 20:10</span>
          <span class="news-item-title">开源包管理器 Homebrew 7.0.0 发布，推出原生苹果 macOS App</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/838.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 13 日消息，9 月 10 日，在 2026 年中国国际服务贸易交易会“服务贸易发展论坛”上，中国信息通信研究院（简称“中国信通院”）与国务院发展研究中心对外经济研究部联合发布《数字贸易发展与合作报告（2026 年）》，由中国信通院副院长王志勤进行解读，这是双方联合推出的第六期报告。报告指出，当前百年未有之大变局加速演进，以人工智能为代表的数智技术加速突破、深度渗透，数字贸易作为数智化与全球化融合的新型贸易形态，展现出较强发展韧性，持续发挥全球贸易“稳定器”作用。2025 年全球数字服务贸易规模达 5.26 万亿美元（IT之家注：现汇率约合 35.4 万亿元人民币），同比增长 10%，较 2019 年增长 86.2%，远超同期货物贸易（38.1%）和传统服务贸易（51.1%" data-title="中国信通院：2025 年我国跨境电商进出口总额约 2.84 万亿元，连续五年位居全球首位" data-date="09-13 19:58" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-13 19:58</span>
          <span class="news-item-title">中国信通院：2025 年我国跨境电商进出口总额约 2.84 万亿元，连续五年位居全球首位</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/cryptomining/mexican-cartel-crypto-farm-seized-in-mountain-raid-300-gpus-satellite-links-and-industrial-transformers-tapped-hydroelectric-power" target="_blank" rel="noopener" data-cat="keji" data-summary="越来越多的证据表明，墨西哥贩毒集团正在向加密货币挖矿领域发展，并利用加密平台洗钱。" data-title="墨西哥卡特尔的加密货币农场在山区突袭中被查封— 300个GPU、卫星链路和工业变压器利用了水力发电" data-date="09-13 19:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-13 19:30</span>
          <span class="news-item-title">墨西哥卡特尔的加密货币农场在山区突袭中被查封— 300个GPU、卫星链路和工业变压器利用了水力发电</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/software/programming/playable-tomb-raider-runs-on-a-humble-1-watt-chip-usd25-board-with-dual-core-400-mhz-esp32-p4-mcu-scales-openlara-up-to-1-024-x-600-playable-pixels" target="_blank" rel="noopener" data-cat="keji" data-summary="一位复古视频游戏爱好者展示了Lara Croft在一个不起眼的ESP32-P4微控制器上在古墓中冒险。" data-title="可播放的古墓丽影在一个不起眼的1瓦芯片上运行— 25 $板，双核400 MHz ESP32-P4 MCU可将OpenLara扩展到1,024 x 600可播放像素" data-date="09-13 19:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-13 19:00</span>
          <span class="news-item-title">可播放的古墓丽影在一个不起眼的1瓦芯片上运行— 25 $板，双核400 MHz ESP32-P4 MCU可将OpenLara扩展到1,024 x 600可播放像素</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/488672.html" target="_blank" rel="noopener" data-cat="keji" data-summary="亮源新创的Physical Al路线清晰了" data-title="2000+真实场景搬进仿真！一个导航模型零样本“通吃”四种机器人本体" data-date="09-13 15:38" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-13 15:38</span>
          <span class="news-item-title">2000+真实场景搬进仿真！一个导航模型零样本“通吃”四种机器人本体</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/755.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 13 日消息，特斯拉借助 Grok，持续把车载语音控制从基础关键词指令，升级成一套完整的对话助手。自从 SpaceX AI 的聊天程序登陆特斯拉车机屏幕后，工程师不断拓展其功能，让驾驶员双手不用离开方向盘就能完成更多操作。如今官方文档披露，下一步将要上线短信收发功能。网友在特斯拉 Model Y 新版车主手册里发现了这项待上线功能。更新后的介绍页面说明了 Grok 切换为助手模式后可实现的操作。在功能列表中，特斯拉明确写道：短信功能：可以让 Grok 给联系人或手机号发送短信（例如，跟它说“给妈妈发消息，说我在路上了”）。目前 Grok 已经可以控制大量车辆功能，还能拨打电话，但尚不支持发短信。作为参考，车主手册里标注的 Grok 现有能力如下：导航：让 Grok 搜索地点" data-title="车主手册披露：特斯拉 Grok 将支持语音收发短信功能" data-date="09-13 14:43" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-13 14:43</span>
          <span class="news-item-title">车主手册披露：特斯拉 Grok 将支持语音收发短信功能</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/488447.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Agent的下一步是关系型生产力" data-title="今年外滩最特别Agent：能干活，能陪聊，还会朋友圈拉黑你" data-date="09-13 14:40" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-13 14:40</span>
          <span class="news-item-title">今年外滩最特别Agent：能干活，能陪聊，还会朋友圈拉黑你</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/752.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 13 日消息，据新浪财经报道，图灵量子今日正式发布“TuringQ Gen3 大规模芯片级可扩展光量子计算机”。该产品采用标准 IDC 机柜形态，拥有全芯片化、模块化、可扩展的整机架构和全栈软硬件体系，支持量子算力节点按需扩展。IT之家从原报道获悉，TuringQ Gen3 基于高速可编程薄膜铌酸锂光量子芯片打造，集成量子光源、可编程光量子处理芯片、单光子探测及量子-经典异构计算等核心模块。该系统采用空时复用架构，将空间光路、时间循环和高速电光调控纳入统一可编程网络，使同一组物理器件能够在不同时间模式中重复参与量子演化，并与空间模式共同形成大规模时空计算网络，可支持单芯片 10000 光子级、1000000 模式数的计算资源扩展。同时，该系统在量子光源、片上传输、器件调控、" data-title="图灵量子发布 TuringQ Gen3 第三代光量子计算机：标准 IDC 机柜形态，采用自研 XLink 低延迟互联架构" data-date="09-13 14:25" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-13 14:25</span>
          <span class="news-item-title">图灵量子发布 TuringQ Gen3 第三代光量子计算机：标准 IDC 机柜形态，采用自研 XLink 低延迟互联架构</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-13/10695620.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="新华社新德里9月13日电#8195;当地时间9月13日上午，国家主席习近平在新德里出席金砖国家领导人第十八次会晤第二阶段会议时就深化金砖合作提出5项倡议：一是人工智能开源普惠倡议，二是贸易投资便利化倡议，三是数字产业合作倡议，四是智能制造合作倡议，五是科技育才倡议。" data-title="习近平：让新兴技术照亮共同繁荣之路" data-date="09-13 14:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-13 14:13</span>
          <span class="news-item-title">习近平：让新兴技术照亮共同繁荣之路</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/749.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 13 日消息，磐镭现已为旗下 WO5 迷你主机新增 R5-3500U + 8GB RAM + 256GB SSD 规格，定价为 1549 元。京东磐镭 WO5 迷你主机 1549 元直达链接该机采用黑色外观设计，造型方正，机身正面有 2 个 USB-A 3.2 Gen2 接口，背面有 2 个 HDMI 2.0 接口、1 个千兆 RJ45 网口、2 个 USB-A 2.0 接口、1 个全功能 USB-C 接口。该机搭载 4 核 8 线程 AMD 锐龙 5 3500U 处理器，至高睿频可达 3.7GHz，TDP 为 15W，搭载了 2 个 SO-DIMM DDR4 2666MHz 内存插槽，匹配 8GB RAM。硬盘方面配备了 1 个 PCIe 3.0 x4 2280 M.2" data-title="磐镭 WO5 迷你主机新增 R5-3500U + 8G + 256G 规格，1549 元" data-date="09-13 13:37" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-13 13:37</span>
          <span class="news-item-title">磐镭 WO5 迷你主机新增 R5-3500U + 8G + 256G 规格，1549 元</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c0qxpyw20q7o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="雅各布·考克森（Jacob Coxon）向BBC表示，如果不遏制人工智能的发展速度，人工智能有很大机会导致人类灭绝。" data-title="AI巨头前雇员：同业“真诚恐惧”人类遭灭绝，西方必须与中国协调" data-date="09-13 13:30" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-13 13:30</span>
          <span class="news-item-title">AI巨头前雇员：同业“真诚恐惧”人类遭灭绝，西方必须与中国协调</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/13/us/politics/obama-democrats-ai.html" target="_blank" rel="noopener" data-cat="keji" data-summary="在一次私人筹款活动中，这位前总统警告说，如果不紧急管理并制定明确的计划，这项技术可能会“危险”。" data-title="奥巴马敦促民主党人将人工智能转移到美国对其议程中心的监督" data-date="09-13 12:03" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-13 12:03</span>
          <span class="news-item-title">奥巴马敦促民主党人将人工智能转移到美国对其议程中心的监督</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/13/us/politics/obama-democrats-ai.html" target="_blank" rel="noopener" data-cat="keji" data-summary="在一次私人筹款活动中，这位前总统警告说，如果不紧急管理并制定明确的计划，这项技术可能会“危险”。" data-title="奥巴马敦促民主党人将人工智能监督转移到他们议程的中心" data-date="09-13 12:03" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-13 12:03</span>
          <span class="news-item-title">奥巴马敦促民主党人将人工智能监督转移到他们议程的中心</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/13/how-to-watch-premier-league-manchester-united-manchester-city" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联和曼城今天的表现如何？以下是需要了解的内容，包括开球时间、电视频道和直播选项本赛季的第一场曼彻斯特德比对两家俱乐部来说都是一个有趣的时刻。曼城在新任经理恩佐·马雷斯卡（ Enzo Maresca ）的领导下正在建立势头，而曼联正试图从一个对他们的转会市场策略提出质疑的夏天继续前进。在他们的三场比赛中每场都承认了两个进球" data-title="今日英超赛程：如何观看、收看电视频道和直播" data-date="09-13 19:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-13 19:00</span>
          <span class="news-item-title">今日英超赛程：如何观看、收看电视频道和直播</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c5ym4384rezo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳以2-0击败桑德兰，取得了坚韧不拔的胜利，但米克尔·阿尔特塔（ Mikel Arteta ）对可能让他的球队付出代价的点球感到愤怒。" data-title="“今天的比赛没有受到保护”——阿尔特塔怒不可遏，但阿森纳幸存下来" data-date="09-13 06:57" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-13 06:57</span>
          <span class="news-item-title">“今天的比赛没有受到保护”——阿尔特塔怒不可遏，但阿森纳幸存下来</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c5ym4384rezo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳以2-0击败桑德兰，取得了坚韧不拔的胜利，但米克尔·阿尔特塔（ Mikel Arteta ）对可能让他的球队付出代价的点球感到愤怒。" data-title="“今天比赛没有受到保护” - Arteta烟雾但阿森纳幸存下来" data-date="09-13 06:57" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-13 06:57</span>
          <span class="news-item-title">“今天比赛没有受到保护” - Arteta烟雾但阿森纳幸存下来</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/sep/12/sunderland-v-arsenal-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Bruno Guimarães, Bukayo Saka and David Raya all had a hand in maintaining Arsenal’s 100% record against SunderlandSunderland parade new striker Juan Angulo, signed from Independiente del Valle last week, before kick-off at the Stadium of Light. That one had passed me by – and I’ve spent all summer writing down hundreds of transfers for this …JD ema" data-title="桑德兰 0-2 阿森纳：英超联赛——事实如此" data-date="09-13 05:15" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-13 05:15</span>
          <span class="news-item-title">桑德兰 0-2 阿森纳：英超联赛——事实如此</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/sep/12/sunderland-v-arsenal-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Bruno Guimarães, Bukayo Saka and David Raya all had a hand in maintaining Arsenal’s 100% record against SunderlandSunderland parade new striker Juan Angulo, signed from Independiente del Valle last week, before kick-off at the Stadium of Light. That one had passed me by – and I’ve spent all summer writing down hundreds of transfers for this …JD ema" data-title="桑德兰0-2阿森纳：英超联赛–事实如此" data-date="09-13 05:15" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-13 05:15</span>
          <span class="news-item-title">桑德兰0-2阿森纳：英超联赛–事实如此</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/12/sunderland-arsenal-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="当终场哨声吹响时，布鲁诺·吉马良斯脸上挂着顽皮的微笑，恩佐·勒菲则郁郁寡欢，阿森纳本赛季的完美开局依然没有受到任何影响。在大卫·拉亚相当威严地扑出勒菲下半场的点球两分钟后，吉马良斯从禁区边缘射出一记弧线球，绕过罗宾·罗夫斯，让他的北伦敦新球迷和纽卡斯尔的许多老朋友们高兴不已。继续阅读..." data-title="吉马良斯和萨卡带领阿森纳在拉亚比赛后击败桑德兰" data-date="09-13 05:14" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-13 05:14</span>
          <span class="news-item-title">吉马良斯和萨卡带领阿森纳在拉亚比赛后击败桑德兰</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/12/sunderland-arsenal-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="As the final whistle blew Bruno Guimarães wore a mischievous smile, Enzo Le Fée was a study in dejection and Arsenal’s immaculate start to the season remained unblemished.Two minutes after David Raya had rather majestically saved Le Fée’s second-half penalty, Guimarães delighted his new north London public and plenty of old friends in Newcastle by" data-title="吉马良斯和萨卡射击阿森纳，在拉亚现场之后在桑德兰获胜" data-date="09-13 05:14" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-13 05:14</span>
          <span class="news-item-title">吉马良斯和萨卡射击阿森纳，在拉亚现场之后在桑德兰获胜</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/10/premier-league-top-scorers-2026-27-race-for-golden-boot" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="了解哪些英格兰顶级联赛的神射手正在进球榜上一路高歌猛进 继续阅读..." data-title="2026-27赛季英超最佳射手：谁在金靴争夺战中领先？" data-date="09-13 05:04" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-13 05:04</span>
          <span class="news-item-title">2026-27赛季英超最佳射手：谁在金靴争夺战中领先？</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/10/premier-league-top-scorers-2026-27-race-for-golden-boot" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="找出哪位英国顶尖射手正在向进球排行榜射击。继续阅读……" data-title="2026-27赛季英超联赛最佳射手：谁是金靴赛的领跑者？" data-date="09-13 05:04" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-13 05:04</span>
          <span class="news-item-title">2026-27赛季英超联赛最佳射手：谁是金靴赛的领跑者？</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/czjzpvxy0vko?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="桑德兰和阿森纳球员在英超比赛后的评价。" data-title="吉马良斯和拉亚至关重要 - 桑德兰对阵阿森纳球员评分" data-date="09-13 04:56" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-13 04:56</span>
          <span class="news-item-title">吉马良斯和拉亚至关重要 - 桑德兰对阵阿森纳球员评分</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/czjzpvxy0vko?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="桑德兰和阿森纳球员在英超比赛后的评分。" data-title="Guimaraes和Raya至关重要-桑德兰v阿森纳球员评分" data-date="09-13 04:56" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-13 04:56</span>
          <span class="news-item-title">Guimaraes和Raya至关重要-桑德兰v阿森纳球员评分</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cvgydkv0yxdo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="首席足球作家菲尔·麦克纳尔蒂（ Phil McNulty ）说，无牙马刺再次画了一片空白，现在面临着看到一个勇敢的新时代变成一个虚假的黎明的危险。" data-title="无牙马刺再次空白，因为新时代变成了一个虚假的黎明" data-date="09-13 04:38" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-13 04:38</span>
          <span class="news-item-title">无牙马刺再次空白，因为新时代变成了一个虚假的黎明</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/12/roberto-de-zerbi-tottenham-everton-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="“没有胜利，没有进球……这对球员来说是艰难的”马刺队在对阵埃弗顿·罗伯托·德·泽比的0-0平局后排名第17位，他说他的托特纳姆热刺球员仍然缺乏身体素质，在与埃弗顿主场0-0取得最新的英超联赛空白后，他们必须在心理上“解开”自己。自本赛季开始以来，比赛已经进行了四场比赛，没有马刺的进球；他们在两场比赛中排名第17" data-title="德泽尔比表示热刺在继续等待联赛胜利后出现了“精神障碍”" data-date="09-13 04:36" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-13 04:36</span>
          <span class="news-item-title">德泽尔比表示热刺在继续等待联赛胜利后出现了“精神障碍”</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/12/roberto-de-zerbi-tottenham-everton-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="“没有胜利，没有进球……这对球员来说是艰难的”马刺队在对阵埃弗顿·罗伯托·德·泽比的0-0平局后排名第17位，他说他的托特纳姆热刺球员仍然缺乏身体素质，在与埃弗顿主场0-0取得最新的英超联赛空白后，他们必须在心理上“解开”自己。自本赛季开始以来，比赛已经进行了四场比赛，没有马刺的进球；他们在两场比赛中排名第17" data-title="德泽尔比说，马刺队在等待联赛胜利后仍有“精神障碍”" data-date="09-13 04:36" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-13 04:36</span>
          <span class="news-item-title">德泽尔比说，马刺队在等待联赛胜利后仍有“精神障碍”</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c62j0lr1rzmo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦未能在安菲尔德赢得前两场英超比赛中的任何一场。但现在担心还为时过早吗？" data-title="安菲尔德丢分更多——利物浦现在担心还为时过早吗？" data-date="09-13 03:30" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-13 03:30</span>
          <span class="news-item-title">安菲尔德丢分更多——利物浦现在担心还为时过早吗？</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/001/845.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 13 日消息，在稍早前结束的《CS2》裂变天地 S3 苏州站决赛中，巴西战队 Legacy 以 3:0 的大比分横扫 G2 Esports 赢得冠军荣誉。IT之家注意到，Legacy 此前已在中国拿下 2025、2026 两年的《CS》亚洲邀请赛 (CAC) 头名。中国无疑是这支战队福地，甚至队伍官方也将中国视为其“第二主场”。" data-title="实乃福地！Legacy 赢得《CS2》裂变天地 S3 苏州站冠军" data-date="09-13 20:44" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-13 20:44</span>
          <span class="news-item-title">实乃福地！Legacy 赢得《CS2》裂变天地 S3 苏州站冠军</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-13/10695791.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社台北9月13日电 (记者 朱贺)“树上的鸟儿成双对，绿水青山带笑颜……”13日，台北文山剧场响起《天仙配》的经典旋律，演员观众齐声合唱，将安徽省黄梅戏剧院带来的演出推向高潮。" data-title="安徽省黄梅戏剧院圈粉台北观众" data-date="09-13 20:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-13 20:34</span>
          <span class="news-item-title">安徽省黄梅戏剧院圈粉台北观众</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/842.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 13 日消息，奕境汽车今日宣布，奕境安全技术讲解会将于 9 月 14 日 19:30-20:30 在武汉举行，华为干昆智驾 ADS 5 × 奕境“天穹智盾”。据IT之家此前报道，奕境 X9 旗舰大六座 SUV 已于 8 月 18 日正式开启预售，号称满配华为干昆全栈智能，拥有华为干昆智驾、鸿蒙座舱、干昆赤兔平台、干昆车载光、干昆车云、鲸鳍通信等，预售价 29.98 万-37.98 万元。增程 四驱 Ultra+ 旗舰 长续航版：37.98 万元增程 四驱 Ultra+ 长续航版：33.98 万元增程 Max 长续航版：29.98 万元奕境 X9 长 5301mm、宽 2015mm、高 1820mm，轴距为 3120mm；搭载鸿蒙座舱 HarmonySpace 6，配备双 1" data-title="华为干昆智驾 ADS 5 加持，东风奕境安全技术讲解会明日举行" data-date="09-13 20:16" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-13 20:16</span>
          <span class="news-item-title">华为干昆智驾 ADS 5 加持，东风奕境安全技术讲解会明日举行</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/840.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 13 日消息，为纪念《塞尔达传说》诞生 40 周年，任天堂推出了 Switch 2 特别版主机、Switch 2 Pro 手柄以及 Switch 2 收纳包。不过并非只有任天堂在推出限定产品来庆祝这一里程碑。知名第三方游戏配件厂商 Hori 也推出了塞尔达主题系列产品，一同参与这次周年纪念。单从观感来说，这套配件甚至比任天堂官方产品更吸睛，可选配件品类也比官方更多。Hori 的《塞尔达传说》系列一共包含五款产品，全部将于 11 月上市。这套产品分别是：适配 Switch 2 的塞尔达主题无线 Horipad Turbo 手柄、Switch 2 Hori 冒险套装、Switch 2 轻薄硬保护包、Switch 2 便携多功能收纳包，以及 Hori 弹压式游戏卡盒。这款 Swi" data-title="Hori 推出《塞尔达传说》40 周年 Switch 2 周边配件，11 月日本发售" data-date="09-13 20:05" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-13 20:05</span>
          <span class="news-item-title">Hori 推出《塞尔达传说》40 周年 Switch 2 周边配件，11 月日本发售</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-13/10695747.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网福建诏安9月13日电 题：古法杉木闸板显奇效 福建诏安大水门“土办法”挡洪护城" data-title="古法杉木闸板显奇效 福建诏安大水门“土办法”挡洪护城" data-date="09-13 20:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-13 20:00</span>
          <span class="news-item-title">古法杉木闸板显奇效 福建诏安大水门“土办法”挡洪护城</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/994218/apple-iphone-18-pro-airpods-5-meta-muse-ai-sony-headphones" target="_blank" rel="noopener" data-cat="zonghe" data-summary="嗨，朋友们！欢迎来到143号安装商，这是世界上最好、最边缘的东西的指南。（如果您是新手，欢迎光临，新技术季即将到来，您还可以在安装程序主页上阅读所有旧版本。）本周，我一直在吞噬我能找到的每一个iPhone Duo视频，点击[…]" data-title="苹果的新手机在这里" data-date="09-13 20:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-13 20:00</span>
          <span class="news-item-title">苹果的新手机在这里</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/837.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 13 日消息，当地时间 9 月 10 日，模块化电脑厂商 Framework 宣布，由于无法将材料成本、组装成本以及制造良率控制在具备商业可行性的水平，最终决定终止单键模块（One Key Module）个性化键盘项目。IT之家获悉，Framework 于去年正式对外公布了单键模块，该项目允许独立开发者和硬件爱好者利用单个按键模块在载板 PCB 上随意排列，从而打破笔记本键盘的固化布局，为笔记本打造专属于自己的超薄人体工学键盘或输入控制模块。官方表示，单键成本过高导致其收支平衡售价超出合理范围，难以拉动规模化销量；Framework 和供应商均无法承受小批量生产此类高复杂度部件所带来的高昂开销。Framework 还透露，即便是开发者计划中经验丰富的 DIY 高手与电子发烧" data-title="因制造与成本问题，模块化电脑厂商 Framework 宣布终止“单键模块”个性化键盘项目" data-date="09-13 19:52" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-13 19:52</span>
          <span class="news-item-title">因制造与成本问题，模块化电脑厂商 Framework 宣布终止“单键模块”个性化键盘项目</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/13/world/middleeast/iran-meeting-gulf-arab-states.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="官员们表示，预计明天将举行会谈。结束与美国战争的外交陷入僵局，伊朗盟军在也门取得了进展。" data-title="伊朗将与海湾阿拉伯国家会晤，扩大中东冲突" data-date="09-13 19:52" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-13 19:52</span>
          <span class="news-item-title">伊朗将与海湾阿拉伯国家会晤，扩大中东冲突</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-13/10695745.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网海口9月13日电 (记者 王子谦)记者13日下午从气象等相关部门获悉，南海热带低压已于当日17时前后在越南广治省沿海登陆，但强降雨仍在持续，多个预警仍维持。" data-title="南海热带低压登陆越南 海南继续维持多项预警" data-date="09-13 19:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-13 19:37</span>
          <span class="news-item-title">南海热带低压登陆越南 海南继续维持多项预警</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-13/10695744.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网海口9月13日电 (钟坚 卓欣欣)受热带低压和冷空气共同影响，海南多地持续强降雨。海南省消防救援总队表示，目前全省消防救援队伍已按二级响应要求全面进入备勤状态，各项防汛准备工作有序展开。" data-title="海南全省消防救援队伍进入二级响应 全力应对强降雨" data-date="09-13 19:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-13 19:28</span>
          <span class="news-item-title">海南全省消防救援队伍进入二级响应 全力应对强降雨</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-13/10695739.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京9月13日电 (记者 孙自法)全球首座翼龙主题科学博物馆——哈密翼龙博物馆，9月13日在中国新疆哈密翼龙—雅丹国家地质公园正式开馆，备受关注。" data-title="专家解读全球首座翼龙博物馆：打造世界级翼龙研究与科普中心" data-date="09-13 19:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-13 19:23</span>
          <span class="news-item-title">专家解读全球首座翼龙博物馆：打造世界级翼龙研究与科普中心</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/drones/waymo-robotaxi-calls-cops-on-riders-handling-loaded-ar-style-ghost-gun-waymo-alerted-san-francisco-police-then-juvenile-riders-were-stopped-and-arrested" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在机器人出租车公司Waymo告密后，旧金山警方进行了“高风险停车” ，并逮捕了两名非法持有枪支的青少年。" data-title="Waymo机器人出租车在处理装有AR风格幽灵枪的乘客时报警— Waymo通知了旧金山警方，然后青少年乘客被拦截并被捕" data-date="09-13 19:16" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-13 19:16</span>
          <span class="news-item-title">Waymo机器人出租车在处理装有AR风格幽灵枪的乘客时报警— Waymo通知了旧金山警方，然后青少年乘客被拦截并被捕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-13/10695736.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京9月13日电 题：“魔豆”长成大树 促更多困境女性从“救助”到“赋能”" data-title="“魔豆”长成大树 促更多困境女性从“救助”到“赋能”" data-date="09-13 19:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-13 19:10</span>
          <span class="news-item-title">“魔豆”长成大树 促更多困境女性从“救助”到“赋能”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-13/10695730.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="新华社雅加达9月13日电(记者高竹)印度尼西亚国家搜救局13日说，此前在爪哇海海域失联的一艘客轮已经沉没。目前已确认有1人遇难、约110人获救，另有约130人仍在搜寻中。" data-title="印尼失联客轮已确认沉没 船上无中国公民" data-date="09-13 18:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-13 18:53</span>
          <span class="news-item-title">印尼失联客轮已确认沉没 船上无中国公民</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-13/10695727.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网南宁9月13日电(张广权)9月12日至10月11日，南宁园博园举办第五届“粉黛季·遇见你”粉黛花海生活节。本次活动以3.1万平方米粉黛花海为核心，设置花海区、花镜区、童话区和休憩区，让市民游客沉浸式欣赏花海美景，体验生态休闲乐趣。" data-title="秋日粉黛花开 南宁园博园3.1万平方米花海迎客" data-date="09-13 18:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-13 18:44</span>
          <span class="news-item-title">秋日粉黛花开 南宁园博园3.1万平方米花海迎客</span>
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


<p class="news-updated">🕐 抓取更新于 2026-09-13 20:48（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
