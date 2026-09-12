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
      <span>2026-09-12 19:41 抓取更新</span>
    </div>
  </div>

  <div class="news-search-bar" style="margin: 12px 0 8px; display: flex; align-items: center; gap: 8px; background: rgba(127,127,127,0.08); border: 1px solid rgba(127,127,127,0.2); border-radius: 8px; padding: 7px 14px;">
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="opacity: 0.65;"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
    <input type="text" id="news-search-input" placeholder="🔍 实时搜索今日全天新闻（输入关键词、球队、公司、人物、信源）..." oninput="onNewsSearch(this.value)" style="flex: 1; background: transparent; border: none; outline: none; color: inherit; font-size: 13px;">
    <span id="news-search-count" style="font-size: 12px; opacity: 0.7; font-weight: 500;"></span>
  </div>

  <div class="news-nav-composite">
    <div class="news-channel-bar">
      <button class="channel-btn active" onclick="filterNewsChannel('all', this)">
        <span>🌟 全部动态</span>
        <span class="channel-count">58</span>
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
        <span class="channel-count">13</span>
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
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/09-12/10695326.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网兴安盟9月12日电 (记者 张玮)记者12日从兴安盟袁隆平院士工作站获悉，2026年耐盐碱水稻测产活动在内蒙古自治区兴安盟科右中旗举行。经专家团现场实收测定，耐盐碱水稻平均亩产达552.67公斤，再创历史新高。" data-title="兴安盟袁隆平院士工作站耐盐碱水稻亩产超552公斤" data-date="09-12 19:35" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 09-12 19:35</span>
      </div>
      <h2 class="hero-featured-title">兴安盟袁隆平院士工作站耐盐碱水稻亩产超552公斤</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.theverge.com/ai-artificial-intelligence/994255/openai-millennium-prize-problem-tristan-buckmaster-competition" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI在过去几年中一直在日益困难的数学领域种植旗帜。本周，它获得了迄今为止最大的奖项之一：解决传奇的千年奖问题。在正常情况下，这被认为是一项历史性的成就。相反，许多数学家已经看到了OpenAI在[…]方面的不懈进步。" data-title="OpenAI只想赢" data-date="09-12 19:00" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">OpenAI只想赢</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/2026/sep/12/how-to-watch-spurs-everton-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="马刺队和埃弗顿队今天的表现如何？以下是需要了解的信息，包括开球时间、电视频道和直播选项热刺在经历了一个几乎被英超联赛淘汰的赛季之后的复苏尚未实现。事实上，罗伯托·德·泽比的球队仍在寻找他们在联赛赛季的第一场胜利，对周六的比赛给予一定的重视。任何低于马刺的胜利都可能改变气氛" data-title="今日英超联赛：如何观看马刺对埃弗顿，电视频道和直播" data-date="09-12 19:30" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">今日英超联赛：如何观看马刺对埃弗顿，电视频道和直播</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/001/627.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 12 日消息，据中国载人航天工程办公室，近期，神二十三乘组圆满完成了约 5.5 小时的出舱活动。中国空间站要实现长期在轨可靠、安全稳定运行，必须具备在轨组装及维修维护能力。因此，需要航天员出舱完成舱外载荷和设备的维修、安装等一系列舱外操作任务。那么，在出舱活动期间，空间站是如何调控姿态，为航天员提供稳定的舱外作业环境呢？IT之家从官方介绍获悉，中国空间站的姿态控制方式分为两种：发动机喷气控制和 CMG 控制。发动机喷气控制时，向外喷射推进剂，通过反作用力实现空间站姿态控制；CMG 控制时，由 CMG 与空间站舱体之间进行角动量交换，实现空间站姿态控制。CMG 是什么？CMG 全称控制力矩陀螺（Control Moment Gyroscope），是航天器姿态控制的关键执行机构" data-title="航天员出舱时空间站如何稳姿？官方详解 CMG 与喷气控制" data-date="09-12 19:27" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">航天员出舱时空间站如何稳姿？官方详解 CMG 与喷气控制</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-12/10695326.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网兴安盟9月12日电 (记者 张玮)记者12日从兴安盟袁隆平院士工作站获悉，2026年耐盐碱水稻测产活动在内蒙古自治区兴安盟科右中旗举行。经专家团现场实收测定，耐盐碱水稻平均亩产达552.67公斤，再创历史新高。" data-title="兴安盟袁隆平院士工作站耐盐碱水稻亩产超552公斤" data-date="09-12 19:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 19:35</span>
          <span class="news-item-title">兴安盟袁隆平院士工作站耐盐碱水稻亩产超552公斤</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-12/10695325.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网上海9月12日电 (记者 孙自法 郑莹莹)2026浦江创新论坛开幕式9月12日在上海举行，国家自然科学基金长三角基础研究联合基金重大专项正式启动。" data-title="2026浦江创新论坛开幕 长三角基础研究联合基金重大专项正式启动" data-date="09-12 19:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 19:35</span>
          <span class="news-item-title">2026浦江创新论坛开幕 长三角基础研究联合基金重大专项正式启动</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/drones/iran-could-potentially-reverse-engineer-captured-u-s-underwater-drone-several-iranian-embassies-mock-us-over-capture-as-u-s-military-downplays-the-situation" target="_blank" rel="noopener" data-cat="shizheng" data-summary="伊朗可能会对被俘的美国海军Anduril Dive-LD水下无人机进行逆向工程，因为德黑兰嘲笑损失，而华盛顿则淡化其军事价值。" data-title="伊朗可能对捕获的美国水下无人机进行逆向工程—几个伊朗大使馆嘲笑美国捕获，海军声称丢失的Anduril车辆有缺陷且未分类" data-date="09-12 19:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-12 19:30</span>
          <span class="news-item-title">伊朗可能对捕获的美国水下无人机进行逆向工程—几个伊朗大使馆嘲笑美国捕获，海军声称丢失的Anduril车辆有缺陷且未分类</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-12/10695324.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网甘肃天水9月12日电 (记者 应妮)“东方微笑 跨越千年——麦积山雕塑论坛·2026”11日在甘肃省天水市开幕。来自全国40余家文博单位、高校和科研院所的百余位专家学者齐聚一堂。" data-title="“麦积山雕塑论坛·2026”探索构建中国雕塑自主知识体系" data-date="09-12 19:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 19:22</span>
          <span class="news-item-title">“麦积山雕塑论坛·2026”探索构建中国雕塑自主知识体系</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-12/10695372.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间9月12日下午，国家主席习近平在新德里出席金砖国家领导人第十八次会晤第一阶段会议。" data-title="新华图讯丨习近平出席金砖国家领导人第十八次会晤第一阶段会议并发表重要讲话" data-date="09-12 19:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 19:14</span>
          <span class="news-item-title">新华图讯丨习近平出席金砖国家领导人第十八次会晤第一阶段会议并发表重要讲话</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-12/10695294.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社乌鲁木齐9月12日电 题：台湾人士：青年乐于走进大陆、看见真实、讲述所见" data-title="台湾人士：青年乐于走进大陆、看见真实、讲述所见" data-date="09-12 19:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 19:01</span>
          <span class="news-item-title">台湾人士：青年乐于走进大陆、看见真实、讲述所见</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-12/10695356.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月12日 综合俄媒报道，俄罗斯总统普京11日表示，俄罗斯没有威胁欧洲国家，也不打算威胁欧洲国家，俄方没有任何理由同欧洲发生冲突。" data-title="普京：欧洲在乌克兰部署军队意味着“与俄罗斯开战”" data-date="09-12 18:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 18:53</span>
          <span class="news-item-title">普京：欧洲在乌克兰部署军队意味着“与俄罗斯开战”</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/12/world/americas/us-brazil-crime-police-visas-ice.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="官员们表示，特朗普政府正在阻止巴西在打击跨国犯罪方面扩大合作的一些努力。" data-title="签证问题威胁到美国和巴西在犯罪问题上的合作" data-date="09-12 18:48" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-12 18:48</span>
          <span class="news-item-title">签证问题威胁到美国和巴西在犯罪问题上的合作</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-12/10695347.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="视频：新思想引领新征程丨大力弘扬教育家精神 书写教育强国时代新篇来源：央视新闻客户端" data-title="新思想引领新征程丨大力弘扬教育家精神 书写教育强国时代新篇" data-date="09-12 18:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 18:40</span>
          <span class="news-item-title">新思想引领新征程丨大力弘扬教育家精神 书写教育强国时代新篇</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-12/10695327.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="视频丨国际人士热切期待习近平主席出席金砖国家领导人第十八次会晤" data-title="国际人士热切期待习近平主席出席金砖国家领导人第十八次会晤" data-date="09-12 18:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 18:20</span>
          <span class="news-item-title">国际人士热切期待习近平主席出席金砖国家领导人第十八次会晤</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/621.htm" target="_blank" rel="noopener" data-cat="shizheng" data-summary="IT之家 9 月 12 日消息，乘联分会秘书长崔东树今天（12 日）在个人公众号发文称，2026 年 8 月车市零售环比回升 5.5%，是油价高位压制、宏观景气偏弱、政策预期升温、成都车展带动等多重因素交织共振的结果。崔东树表示，地缘冲突持续困扰霍尔木兹海峡的通航，推动国际油价维持高位震荡，2026 年国内汽油价格累计上调已超 1720 元 / 吨，尤其 7 月底以来上涨了 180 元，大幅抬高了燃油车用车成本，国内燃油乘用车消费需求持续剧烈萎缩。数据显示，8 月制造业 PMI 环比回升 0.6% 至 49.8%，仍处于荣枯线之下，终端内需边际虽回暖但力度有限。IT之家从文中获悉，当月上中旬高温假抑制终端到店客流、下旬成都车展带动市场热度回升、月末冲量拉动日均零售修复，终端订单与客流呈现前低" data-title="乘联分会崔东树：本轮乘用车市场下行属于阶段性结构性波动" data-date="09-12 18:07" data-source="IT之家">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-12 18:07</span>
          <span class="news-item-title">乘联分会崔东树：本轮乘用车市场下行属于阶段性结构性波动</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-12/10695307.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月12日电 中国官方12日通报，近日，在中央反腐败协调小组国际追逃追赃工作办公室统筹协调下，经国际执法司法合作，“红通人员”、外逃职务犯罪嫌疑人曾能贵被引渡回国。" data-title="“红通人员”、外逃职务犯罪嫌疑人曾能贵被引渡回中国" data-date="09-12 18:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 18:01</span>
          <span class="news-item-title">“红通人员”、外逃职务犯罪嫌疑人曾能贵被引渡回中国</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/12/world/middleeast/yemen-iran-war-houthis.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="多年来，饥饿和疾病一直折磨着也门。现在，沙特支持的政府与伊朗支持的胡塞武装之间的战斗正在将其推向边缘。" data-title="“我们穿着我们穿的衣服离开了” ：也门人逃离新的战斗" data-date="09-12 17:03" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-12 17:03</span>
          <span class="news-item-title">“我们穿着我们穿的衣服离开了” ：也门人逃离新的战斗</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/12/us/politics/trump-free-speech.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="特朗普总统利用政府各部门限制新闻自由，言论自由倡导者表示，这将产生持久影响。" data-title="特朗普如何利用权力扼杀言论" data-date="09-12 17:02" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-12 17:02</span>
          <span class="news-item-title">特朗普如何利用权力扼杀言论</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/12/us/politics/trump-democrats-communism-midterms.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="用总统的夸张说法，共产主义对国家的威胁比珍珠港事件或9/11袭击事件更严重。这种中期策略是否有效是一个悬而未决的问题。" data-title="面临中期风险的共和党人试图将民主党人打上共产党人的烙印" data-date="09-12 17:00" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-12 17:00</span>
          <span class="news-item-title">面临中期风险的共和党人试图将民主党人打上共产党人的烙印</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/994255/openai-millennium-prize-problem-tristan-buckmaster-competition" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI在过去几年中一直在日益困难的数学领域种植旗帜。本周，它获得了迄今为止最大的奖项之一：解决传奇的千年奖问题。在正常情况下，这被认为是一项历史性的成就。相反，许多数学家已经看到了OpenAI在[…]方面的不懈进步。" data-title="OpenAI只想赢" data-date="09-12 19:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-12 19:00</span>
          <span class="news-item-title">OpenAI只想赢</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/487796.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Claude越界攻击真实系统，并非只是测试系统的设置问题，模型本身的安全问题也出了问题。" data-title="A社承认Claude安全对齐存在缺陷，但“尚无解决方案”" data-date="09-12 16:49" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-12 16:49</span>
          <span class="news-item-title">A社承认Claude安全对齐存在缺陷，但“尚无解决方案”</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/487752.html" target="_blank" rel="noopener" data-cat="keji" data-summary="触觉、记忆、Ego数据、自进化……这个世界模型全都有" data-title="探索RSI，生数新世界模型让机器人开始自我进化" data-date="09-12 16:15" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-12 16:15</span>
          <span class="news-item-title">探索RSI，生数新世界模型让机器人开始自我进化</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/487701.html" target="_blank" rel="noopener" data-cat="keji" data-summary="FrontierMath Tier 4，饱和了" data-title="AI数学的最后一道高墙，塌了！GPT-6 Astra刷穿FrontierMath Tier 4" data-date="09-12 15:33" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-12 15:33</span>
          <span class="news-item-title">AI数学的最后一道高墙，塌了！GPT-6 Astra刷穿FrontierMath Tier 4</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/487688.html" target="_blank" rel="noopener" data-cat="keji" data-summary="冲刺港股IPO" data-title="Kimi突发K2.8：性能逼近K3，百万上下文全员开放" data-date="09-12 13:58" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-12 13:58</span>
          <span class="news-item-title">Kimi突发K2.8：性能逼近K3，百万上下文全员开放</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/562.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 12 日消息，阿里宣布旗下企业级通用 Agent 智能体产品千问办公已上架麒麟软件商店，即日起，银河麒麟操作系统用户在软件商店搜索千问办公，即可一键下载安装体验。目前，千问办公已全面支持 Windows、macOS、HarmonyOS、银河麒麟、统信 UOS 等全部主流操作系统。阿里表示，千问办公和麒麟软件团队此前进行了联合攻坚，在系统登录联动、设备互联、技能调用等核心链路展开了深度协作，并针对办公全场景适配优化，实现了千问办公在银河麒麟操作系统上的原生级运行效果，可为用户提供稳定、流畅的 AI 办公体验。例如，银河麒麟操作系统用户不仅可以体验通用办公 Agent 的能力，还可以使用千问办公发送钉钉消息、总结群聊内容、生成周报、预定日程会议、总结会议纪要、创建钉钉文档和 A" data-title="阿里千问办公上架麒麟软件商店，已原生适配全部主流操作系统" data-date="09-12 13:47" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-12 13:47</span>
          <span class="news-item-title">阿里千问办公上架麒麟软件商店，已原生适配全部主流操作系统</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/487653.html" target="_blank" rel="noopener" data-cat="keji" data-summary="25位菲尔兹奖得主联名吹哨" data-title="陶哲轩邓煜究竟在反对什么：AI暴力解题摧毁人类数学精神" data-date="09-12 12:53" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-12 12:53</span>
          <span class="news-item-title">陶哲轩邓煜究竟在反对什么：AI暴力解题摧毁人类数学精神</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/11/mecka-ai-nears-500m-valuation-in-sequoia-led-deal-amid-rush-for-robot-training-data/" target="_blank" rel="noopener" data-cat="keji" data-summary="这家成立两年的初创公司的融资是在Mecka宣布其A轮融资的几个月后进行的。" data-title="在急于获取机器人训练数据之际， Mecka AI对红杉领导的交易的估值接近5亿美元" data-date="09-12 06:58" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-12 06:58</span>
          <span class="news-item-title">在急于获取机器人训练数据之际， Mecka AI对红杉领导的交易的估值接近5亿美元</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/11/y-combinators-garry-tan-wants-u-s-open-weight-ai-labs-to-distill-frontier-models-too/" target="_blank" rel="noopener" data-cat="keji" data-summary="Tan希望规模较小的美国开放式人工智能实验室在美国前沿人工智能实验室中使用相同的训练技术，为美国提供一套更强大的非中国开放式权重选择。" data-title="Y Combinator的Garry Tan希望美国开放式人工智能实验室也能“提炼”前沿模型" data-date="09-12 04:59" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-12 04:59</span>
          <span class="news-item-title">Y Combinator的Garry Tan希望美国开放式人工智能实验室也能“提炼”前沿模型</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/11/openais-feud-with-mathematicians-is-only-escalating/" target="_blank" rel="noopener" data-cat="keji" data-summary="25位领先的数学家签署了一封公开信，声称人工智能实验室正在威胁他们的智力工作。" data-title="OpenAI与数学家的不和只会升级" data-date="09-12 04:57" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-12 04:57</span>
          <span class="news-item-title">OpenAI与数学家的不和只会升级</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/994207/chatgpt-new-mexico-lawyer-fined-murder-appeal" target="_blank" rel="noopener" data-cat="keji" data-summary="据路透社报道，新墨西哥州最高法院正在惩罚一名律师，因为他将人工智能捏造的证人和伪造的警方证词纳入其客户谋杀罪的上诉。在周三提交的一份文件中，法院对Stephen Aarons处以5000 $的罚款，并判定他藐视法庭，因为他未能“核实事实主张和法律[…]" data-title="律师在一起谋杀案中因人工智能幻觉证人被罚款5000 $" data-date="09-12 04:44" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-12 04:44</span>
          <span class="news-item-title">律师在一起谋杀案中因人工智能幻觉证人被罚款5000 $</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/11/kimi-maker-moonshot-ai-targets-2-billion-in-annual-revenue/" target="_blank" rel="noopener" data-cat="keji" data-summary="虽然K3的使用数据在最近几个月略有下降，但OpenRouter数据目前显示，系统上的K3模型每天生成的代币多达3000亿个。" data-title="Kimi制造商Moonshot AI的年收入目标为$ 2B" data-date="09-12 03:35" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-12 03:35</span>
          <span class="news-item-title">Kimi制造商Moonshot AI的年收入目标为$ 2B</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/podcast/an-anthropic-researchers-doomsday-warning-comes-at-a-very-interesting-time/" target="_blank" rel="noopener" data-cat="keji" data-summary="一位人类学研究人员本周辞职，他在X上的一篇帖子中警告说，该公司正在“直奔自我提升的超级智能，用我们的生命赌博”。该公司自己的对齐领导甚至共同签署了信息，而不是把它带回去。这是人工智能行业以前曾经发出的末日警告，但据报道， Anthropic准备首次公开募股的时机使它以不同的方式落地。在[…]" data-title="人类学研究者的世界末日警告发生在一个非常有趣的时刻" data-date="09-12 02:41" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-12 02:41</span>
          <span class="news-item-title">人类学研究者的世界末日警告发生在一个非常有趣的时刻</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/487631.html" target="_blank" rel="noopener" data-cat="keji" data-summary="看清“一个真正的人”" data-title="银行Agent上岗：4200万小微经营者可用，信贷、票据、财税一把梭" data-date="09-12 02:02" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-12 02:02</span>
          <span class="news-item-title">银行Agent上岗：4200万小微经营者可用，信贷、票据、财税一把梭</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/11/nscale-adds-former-openai-exec-fidji-simo-to-its-board-ahead-of-potential-ipo/" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI排名第二的高管也在2023年带领Instacart完成了首次公开募股。" data-title="Nscale在潜在的IPO之前将前OpenAI高管Fidji Simo加入其董事会" data-date="09-12 00:46" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-12 00:46</span>
          <span class="news-item-title">Nscale在潜在的IPO之前将前OpenAI高管Fidji Simo加入其董事会</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">13 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/12/how-to-watch-spurs-everton-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="马刺队和埃弗顿队今天的表现如何？以下是需要了解的信息，包括开球时间、电视频道和直播选项热刺在经历了一个几乎被英超联赛淘汰的赛季之后的复苏尚未实现。事实上，罗伯托·德·泽比的球队仍在寻找他们在联赛赛季的第一场胜利，对周六的比赛给予一定的重视。任何低于马刺的胜利都可能改变气氛" data-title="今日英超联赛：如何观看马刺对埃弗顿，电视频道和直播" data-date="09-12 19:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-12 19:30</span>
          <span class="news-item-title">今日英超联赛：如何观看马刺对埃弗顿，电视频道和直播</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-12/10695391.shtml" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="中新网9月12日 据英国《卫报》当地时间12日报道，本周早些时候导致英国数千趟航班停飞的空中交通管制系统故障，据称是由一架军用飞机向系统输入虚假飞行数据所引发的。" data-title="英国超2000架次航班突然被取消 英媒：一军机输入虚假飞行数据所致" data-date="09-12 19:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 19:29</span>
          <span class="news-item-title">英国超2000架次航班突然被取消 英媒：一军机输入虚假飞行数据所致</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cj9x7e40gr2o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="摩纳哥和塞内加尔中场球员拉明·卡马拉（ Lamine Camara ）表示，他正在从失败的4710万英镑转会切尔西。" data-title="“我已经翻开了一页” -卡马拉对切尔西的交易崩溃" data-date="09-12 18:07" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-12 18:07</span>
          <span class="news-item-title">“我已经翻开了一页” -卡马拉对切尔西的交易崩溃</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/12/how-to-watch-liverpool-fulham-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦和富勒姆今天的表现如何？以下是需要了解的内容，包括开球时间、电视频道和直播选项2026-27赛季英超联赛的积分榜已经开始成形，利物浦的目标是在上个赛季的压倒性竞选之后更接近积分榜榜首，安菲尔德队获得了第五名。对于富勒姆来说，本赛季可能是关于生存的。山寨队已经失去了他们的三个开场赛程，" data-title="今日英超联赛：如何观看利物浦对富勒姆、电视频道和直播" data-date="09-12 17:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-12 17:00</span>
          <span class="news-item-title">今日英超联赛：如何观看利物浦对富勒姆、电视频道和直播</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cy5zp9llp3ro?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="新任队长鲁本·迪亚斯（ Ruben Dias ）表示，曼城带来了“渴望获胜”的夏季签约球员，整个球队正在“接受”新任经理恩佐·马雷斯卡（ Enzo Maresca ）的“想法”。" data-title="新曼城签约迫切希望获胜" data-date="09-12 13:24" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-12 13:24</span>
          <span class="news-item-title">新曼城签约迫切希望获胜</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c1j4z1ry29jo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="切尔西主教练哈比·阿隆索表示，前锋若昂·佩德罗在风格上与他的前皇家马德里队友卡里姆·本泽马相似，与曼城的埃尔林·哈兰德相当。" data-title="像本泽马和哈兰德一样好-阿隆索和若昂·佩德罗" data-date="09-12 05:30" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-12 05:30</span>
          <span class="news-item-title">像本泽马和哈兰德一样好-阿隆索和若昂·佩德罗</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/11/premier-league-news-iraola-values-wirtzs-work-ethic-moyes-backs-senior-citizen-grealish" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦主教练坚持认为，中场球员应该以他的影响力而不是数字来评判。继续阅读……" data-title="英超新闻： Iraola重视Wirtz的职业道德； Moyes支持“老年人” Grealish" data-date="09-12 05:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-12 05:30</span>
          <span class="news-item-title">英超新闻： Iraola重视Wirtz的职业道德； Moyes支持“老年人” Grealish</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cr50q58vqggo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="托特纳姆热刺前锋理查利森提议搬到瓦斯科达伽马，但在巴西未来的不确定性中失败了。" data-title="Richarlison搬到Vasco da Gama" data-date="09-12 04:49" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-12 04:49</span>
          <span class="news-item-title">Richarlison搬到Vasco da Gama</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/11/ballon-dor-shortlist-shows-up-premier-leagues-attacking-failings-but-tide-could-be-turning" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="English top flight’s forwards are not well represented on the list, reflecting a season of set-piece grapple, but 2026-27 already looks brighterPremier League representation is low when it comes to the 16 attacking players on this year’s Ballon d’Or shortlist. Manchester United’s Bruno Fernandes and Manchester City’s Erling Haaland are there but Co" data-title="Ballon d &#39;Or入围名单显示了英超联赛的进攻失败–但潮流可能正在转变" data-date="09-12 03:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-12 03:00</span>
          <span class="news-item-title">Ballon d 'Or入围名单显示了英超联赛的进攻失败–但潮流可能正在转变</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/11/premier-league-team-news-predicted-lineups-for-the-weekend-action" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="周日，在桑德兰主办阿森纳之后，曼城前往曼联参加一场有趣的德比比赛周六下午3点场地别墅公园继续阅读..." data-title="英超球队新闻：周末动作的预测阵容" data-date="09-12 01:16" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-12 01:16</span>
          <span class="news-item-title">英超球队新闻：周末动作的预测阵容</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/11/arts/television/republican-midterm-convention-trump-notebook.html" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="漫长而奇怪的两晚电视节目希望能够接触到精选的顽固派选民（如果足球没有拦截他们的话）。" data-title="特朗普的“中期大会”试图接触顽固的共和党选民，但缺乏机会" data-date="09-11 22:25" data-source="纽约时报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-11 22:25</span>
          <span class="news-item-title">特朗普的“中期大会”试图接触顽固的共和党选民，但缺乏机会</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c624l1v9853o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="赫尔城因歧视性吟唱被罚款£ 30,000 ，俱乐部在2月份被切尔西击败足总杯后发布了三次支持者禁令。" data-title="船体被罚款£ 30K ，并在切尔西颂歌上发布禁令" data-date="09-11 21:43" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-11 21:43</span>
          <span class="news-item-title">船体被罚款£ 30K ，并在切尔西颂歌上发布禁令</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c5y48zdxv0ko?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="米克尔·阿尔特塔表示，阿森纳已经为周中欧冠航班延误做好了准备——因为他故意扰乱了他们季前赛的训练和旅行计划，让他们做好准备。" data-title="我打乱了季前旅行计划，为球员做好准备- Arteta" data-date="09-11 20:32" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-11 20:32</span>
          <span class="news-item-title">我打乱了季前旅行计划，为球员做好准备- Arteta</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/001/627.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 12 日消息，据中国载人航天工程办公室，近期，神二十三乘组圆满完成了约 5.5 小时的出舱活动。中国空间站要实现长期在轨可靠、安全稳定运行，必须具备在轨组装及维修维护能力。因此，需要航天员出舱完成舱外载荷和设备的维修、安装等一系列舱外操作任务。那么，在出舱活动期间，空间站是如何调控姿态，为航天员提供稳定的舱外作业环境呢？IT之家从官方介绍获悉，中国空间站的姿态控制方式分为两种：发动机喷气控制和 CMG 控制。发动机喷气控制时，向外喷射推进剂，通过反作用力实现空间站姿态控制；CMG 控制时，由 CMG 与空间站舱体之间进行角动量交换，实现空间站姿态控制。CMG 是什么？CMG 全称控制力矩陀螺（Control Moment Gyroscope），是航天器姿态控制的关键执行机构" data-title="航天员出舱时空间站如何稳姿？官方详解 CMG 与喷气控制" data-date="09-12 19:27" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-12 19:27</span>
          <span class="news-item-title">航天员出舱时空间站如何稳姿？官方详解 CMG 与喷气控制</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-12/10695311.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网沈阳9月12日电 (记者 赵桂华)9月12日，2026第二届北方芯谷生态伙伴大会暨东北亚半导体装备、零部件、材料展(NAS展)在沈阳市浑南区浑河外滩赛艇中心9号码头启幕。" data-title="南北共链“芯”动沈阳 第二届北方芯谷生态伙伴大会启幕" data-date="09-12 19:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 19:15</span>
          <span class="news-item-title">南北共链“芯”动沈阳 第二届北方芯谷生态伙伴大会启幕</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/ssds/kioxia-exceria-pro-g2-2tb-ssd-review" target="_blank" rel="noopener" data-cat="zonghe" data-summary="铠侠的Exceria Pro G2将SM2508和BiCS8 TLC闪存配对，实现快速、高效的PCIe 5.0存储。它不是最快的PCIe 5.0固态硬盘，但它是可靠的黑色SN8100替代品。" data-title="铠侠Exceria Pro G2 2TB SSD评测" data-date="09-12 19:05" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-12 19:05</span>
          <span class="news-item-title">铠侠Exceria Pro G2 2TB SSD评测</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/626.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 12 日消息，网易《逆水寒：新世界》今日官宣，开服史上真 · 含金量最高的版本，将于 9 月 24 日开启，带来盗墓笔记联动、新玩法、新剧情等。IT之家附《逆水寒：新世界》4.1.4 双节版本概念性前瞻：新版本将有白发加速 300 次，更多出金福利，还有真黄金掉落，扭蛋机额外获得寻珍抽奖道具 * 3。盗墓笔记联动，将带来吴邪、张起灵、霍秀秀三位经典人物，与玩家共探迷局。军工文创联动，带来全新小镇建筑皮肤、限定配饰等免费内容，还有部分 BOSS 免战机制。你画我猜玩法迎来底层焕新，带来新优化、新玩法、新互动等。新华章“且倾人间月”上线，还有中秋“真金喜”活动，联动淘宝闪购等。" data-title="网易《逆水寒：新世界》“含金量最高版本”9 月 24 日上线，联动盗墓笔记" data-date="09-12 19:04" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-12 19:04</span>
          <span class="news-item-title">网易《逆水寒：新世界》“含金量最高版本”9 月 24 日上线，联动盗墓笔记</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/lucky-pc-scavenger-discovers-12-rtx-3070-gpus-from-the-crypto-mining-era-cards-survived-years-of-basement-storage-with-only-minor-signs-of-wear" target="_blank" rel="noopener" data-cat="zonghe" data-summary="看起来像几个被遗忘的采矿钻机，结果是一个令人惊讶的有价值的运输，有12个RTX 3070显卡可能仍然可以执行游戏任务。" data-title="Lucky PC Scavenger发现了加密货币挖矿时代的12个腾讯通3070显卡—卡片在地下室多年的存储中幸存下来，只有轻微的磨损迹象" data-date="09-12 19:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-12 19:00</span>
          <span class="news-item-title">Lucky PC Scavenger发现了加密货币挖矿时代的12个腾讯通3070显卡—卡片在地下室多年的存储中幸存下来，只有轻微的磨损迹象</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/625.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 12 日消息，绿联今日发布了 AI NAS iDX6011 Pro，日常价 19999 元，首发到手价 15999 元。这款新品搭载英特尔酷睿 Ultra 7 255H 处理器（16 核心 16 线程），64GB LPDDR5X 8533MT/s 内存，独立系统盘存储为 128GB。该机配备 2 个 PCIe 4.0×4 M.2 固态硬盘位，单盘上限支持 8TB；支持安装 6 块 2.5/3.5 英寸 SATA 硬盘，单盘位最高支持 32TB。接口方面，这款 NAS 搭载双雷电 4、双万兆网口、OCuLink、HDMI 2.1、SD 4.0 插槽、2 个 USB-A 3.2 Gen2 和 2 个 USB-A 2.0；此外，新品还有一个 PCIe 4.0×8 插槽。这款产品内" data-title="绿联发布 AI NAS iDX6011 Pro：酷睿 Ultra 7 255H、内存 64GB，首发价 15999 元" data-date="09-12 18:50" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-12 18:50</span>
          <span class="news-item-title">绿联发布 AI NAS iDX6011 Pro：酷睿 Ultra 7 255H、内存 64GB，首发价 15999 元</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/cpus/apples-a20-pro-shatters-geekbench-7-single-core-record-2nm-chip-beats-desktop-intel-core-i9-and-amd-ryzen-9-by-up-to-32-percent" target="_blank" rel="noopener" data-cat="zonghe" data-summary="苹果A20 Pro智能手机SoC的性能远远优于所有智能手机处理器，并设法抛弃了最新的笔记本电脑处理器。" data-title="苹果A20 Pro打破Geekbench 7单核记录--2nm芯片比台式机英特尔酷睿i9和AMD锐龙9高出32%" data-date="09-12 18:48" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-12 18:48</span>
          <span class="news-item-title">苹果A20 Pro打破Geekbench 7单核记录--2nm芯片比台式机英特尔酷睿i9和AMD锐龙9高出32%</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/12/world/europe/trump-irish-open-ireland-doonbeg.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="当美国总统前往他的Doonbeg酒店参加爱尔兰公开赛时，当地人既表示赞赏度假村的经济利益，也反对他的政治。" data-title="在Doonbeg ，特朗普的爱尔兰公开访问引发了抗议和赞扬" data-date="09-12 18:36" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-12 18:36</span>
          <span class="news-item-title">在Doonbeg ，特朗普的爱尔兰公开访问引发了抗议和赞扬</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/playstation/consumer-rights-wiki-documents-at-least-44-instances-in-which-sony-says-you-own-your-games-project-is-direct-assault-on-sonys-claim-in-recent-ownership-lawsuit" target="_blank" rel="noopener" data-cat="zonghe" data-summary="详细的采购直接驳斥了索尼的法律主张，即一个理智的人不会期望在PlayStation Store上拥有他们的数字购物。" data-title="Wiki记录了至少44起索尼在数字游戏所有权诉讼中声称您拥有游戏的案例—该项目直接攻击了索尼在最近的所有权诉讼中的主张" data-date="09-12 18:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-12 18:30</span>
          <span class="news-item-title">Wiki记录了至少44起索尼在数字游戏所有权诉讼中声称您拥有游戏的案例—该项目直接攻击了索尼在最近的所有权诉讼中的主张</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/622.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 12 日消息，新大洲本田今日推出 NS125FX 摩托车，可选自由高达联名限量版，售价 8080 元起：碟刹版：8080 元碟刹尾箱版：8380 元ABS 版：8980 元自由高达联名限量版（限量 1000 台）：9980 元NS125FX 搭载 Honda eSP 125cc 发动机，最大扭矩 10N·m/5750rpm，最大功率 7kW/7500rpm，综合油耗 2.0L/100km。NS125FX 搭载全车 LED 灯组（透镜大灯搭配独立日间行车灯），尾部采用立体式造型设计；拥有高清 VA 全贴合液晶仪表、铝合金后扶手、前置储物格、20W 双口（Type A + C）快充、独立铝合金后脚蹬、驻车开关、3/4 座桶空间等配置。NS125FX 搭载五段可调后减震，座高 7" data-title="8080 元起：新大洲本田推出 NS125FX 摩托车，含自由高达联名限量版" data-date="09-12 18:15" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-12 18:15</span>
          <span class="news-item-title">8080 元起：新大洲本田推出 NS125FX 摩托车，含自由高达联名限量版</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/engineer-turns-simulated-fly-brain-into-a-crypto-day-trader-posts-downloadable-sim-to-github-166-700-virtual-neurons-read-candlestick-charts-for-dopamine-hits" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Coinbase工程师将苍蝇大脑变成加密货币日内交易者— Stonkfly拥有116,700个模拟神经元，尚未亏损" data-title="工程师将模拟的苍蝇大脑变成加密货币日内交易者，将可下载的SIM发布到GitHub — 166,700个虚拟神经元阅读多巴胺命中的烛台图表" data-date="09-12 18:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-12 18:00</span>
          <span class="news-item-title">工程师将模拟的苍蝇大脑变成加密货币日内交易者，将可下载的SIM发布到GitHub — 166,700个虚拟神经元阅读多巴胺命中的烛台图表</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/609.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 12 日消息，据外媒 Neowin 今天（11 日）下午报道，此前消息称，微软确认 Windows 11 最新“补丁星期二”更新引发了两个新问题。数小时后，微软又确认了一项新的故障，导致 USB Audio Class 1.0 设备无法正常工作。安装更新后，部分设备会在设备管理器中出现“代码 10”错误，并在多个 Windows 11 版本中完全失去声音输出。故障影响 Windows 11 26H1、25H2 和 24H2，仅涉及客户端设备，服务器版本不受影响。微软承认，受影响用户可能遇到完全无声、音量控制失灵，以及多声道或 3D 音频功能无法使用等情况。IT之家从报道中获悉，微软回应称，目前正调查“永久修复方案”。正式修复推出前，Microsoft Learn 上的部分用" data-title="微软承认 Win11 更新引发“代码 10”错误，部分 USB 音频设备无法正常工作" data-date="09-12 17:55" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-12 17:55</span>
          <span class="news-item-title">微软承认 Win11 更新引发“代码 10”错误，部分 USB 音频设备无法正常工作</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-12/10695304.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="9月11日至13日，" data-title="人这一辈子，一定要去一趟廊坊！" data-date="09-12 17:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 17:33</span>
          <span class="news-item-title">人这一辈子，一定要去一趟廊坊！</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-12/10695278.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网银川9月12日电 (记者 李佩珊)9月12日，2026“举杯贺兰山”青年艺术季系列活动——宁夏银川“中国之路 塞上湖城”主题自驾游在横城旅游集散中心正式启程。来自北京、江苏、甘肃、新疆等8个省份的62辆自驾车、近200名游客及文旅达人集结银川，开启为期三天的山水人文深度自驾旅程。" data-title="银川“中国之路 塞上湖城”主题自驾游活动启幕 游客深度畅游塞上风光" data-date="09-12 17:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 17:14</span>
          <span class="news-item-title">银川“中国之路 塞上湖城”主题自驾游活动启幕 游客深度畅游塞上风光</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-12/10695300.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="“今晚又失眠了……”这句话，你是不是也常说？" data-title="一粒小树籽，竟能缓解失眠！这个小村庄找到了睡眠“解药”" data-date="09-12 17:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-12 17:00</span>
          <span class="news-item-title">一粒小树籽，竟能缓解失眠！这个小村庄找到了睡眠“解药”</span>
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
    el.style.display = isMatch ? (el.classList.contains('news-item') ? 'flex' : 'block') : 'none';
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


---

<p class="news-updated">🕐 抓取更新于 2026-09-12 19:41（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
