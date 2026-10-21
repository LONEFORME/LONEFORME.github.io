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
      <span>2026-10-21 14:41 抓取更新</span>
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
        <span class="channel-count">50</span>
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
        <span class="channel-count">5</span>
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
  <div class="ov-item"><span class="ov-num">50</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">10</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×19 · TechCrunch×8</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/10-21/10718463.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月21日电 (张素 马广志)近日发布的《中国慈善联合会慈善行业标准化建设三年行动方案》提出，到2029年底，慈善团体标准体系、行业组织网络、贯标协同机制和人才队伍基本建成，研制发布多批次团体标准，分层分类开展慈善组织试点建设，组建包括指导专家、宣贯员等的专业队伍。" data-title="中国慈善联合会：到2029年底慈善团体标准体系等基本建成" data-date="10-21 14:35" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-21 14:35</span>
      </div>
      <h2 class="hero-featured-title">中国慈善联合会：到2029年底慈善团体标准体系等基本建成</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/gn/2026/10-21/10718471.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网北京10月21日电 (记者 黄钰钦)记者21日从中国社会科学院获悉，中国—乌兹别克斯坦专家委员会第二次会议日前在乌兹别克斯坦世界经济与外交大学举行。会议以“数字伙伴关系：人工智能与新一代数据经济”为主题，聚焦数字化转型、人工智能治理与务实合作，探讨以科技创新赋能两国现代化建设新路径。" data-title="中国—乌兹别克斯坦专家委员会第二次会议举行 共商数字技术合作前景" data-date="10-21 14:34" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">中国—乌兹别克斯坦专家委员会第二次会议举行 共商数字技术合作前景</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/ck4g10n56jzqo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="切尔西的行动首次与他们希望留住青训后卫乔希·阿奇庞（ Josh Acheampong ）的言论相吻合。" data-title="How England hopeful Acheampong is giving Chelsea a big decision to make" data-date="10-21 14:26" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">How England hopeful Acheampong is giving Chelsea a big decision to make</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/015/853.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 21 日消息，三星钱包昨日宣布，三星钱包数字车钥匙已支持吉利银河。据介绍，无需打开车企 App、无需设置后台常驻，即可完成无感解闭锁。IT之家附支持的吉利银河车型如下：吉利星愿2026 款星愿翼真 L3802025 款熊猫 mini2025 款熊猫卡丁2025 款熊猫骑士吉利星愿 Ultra吉利银河 L6吉利银河 L7熊猫 MINI熊猫卡丁熊猫骑士熊猫勇士吉利银河 E8吉利银河 E5战舰 700参考三星钱包数字车钥匙支持型号" data-title="三星钱包数字车钥匙支持吉利银河，可无感开关车门、启动车辆" data-date="10-21 14:40" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">三星钱包数字车钥匙支持吉利银河，可无感开关车门、启动车辆</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-21/10718463.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月21日电 (张素 马广志)近日发布的《中国慈善联合会慈善行业标准化建设三年行动方案》提出，到2029年底，慈善团体标准体系、行业组织网络、贯标协同机制和人才队伍基本建成，研制发布多批次团体标准，分层分类开展慈善组织试点建设，组建包括指导专家、宣贯员等的专业队伍。" data-title="中国慈善联合会：到2029年底慈善团体标准体系等基本建成" data-date="10-21 14:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-21 14:35</span>
          <span class="news-item-title">中国慈善联合会：到2029年底慈善团体标准体系等基本建成</span>
          <span class="news-value-point">💡 中新网北京10月21日电 (张素 马广志)近日发布的《中国慈善联合会慈善行业标准化建设三年行动方案》提出，到2029年底，慈善团体标准体系、行业…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-21/10718453.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社石家庄10月21日电 题：从新兵到“排爆兵王” 彝族战士普有飞的“长征”" data-title="（长征胜利90周年）从新兵到“排爆兵王”  彝族战士普有飞的“长征”" data-date="10-21 14:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-21 14:32</span>
          <span class="news-item-title">（长征胜利90周年）从新兵到“排爆兵王”  彝族战士普有飞的“长征”</span>
          <span class="news-value-point">💡 中新社石家庄10月21日电 题：从新兵到“排爆兵王” 彝族战士普有飞的“长征”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-21/10718445.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="直播海报：挑战机车水上漂纪录 17年后张雪为梦再冲锋！" data-title="直播海报：挑战机车水上漂纪录 17年后张雪为梦再冲锋！" data-date="10-21 14:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-21 14:09</span>
          <span class="news-item-title">直播海报：挑战机车水上漂纪录 17年后张雪为梦再冲锋！</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-21/10718429.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月21日电 (记者 阮煜琳)中国温室气体自愿减排交易市场加速扩容、加速发展。中国生态环境部副部长李高21日在北京透露，将持续扩大自愿减排交易市场支持领域，到2027年实现重点领域全覆盖。" data-title="中国自愿减排交易市场加速发展 累计成交额近20亿元" data-date="10-21 13:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-21 13:54</span>
          <span class="news-item-title">中国自愿减排交易市场加速发展 累计成交额近20亿元</span>
          <span class="news-value-point">💡 中新社北京10月21日电 (记者 阮煜琳)中国温室气体自愿减排交易市场加速扩容、加速发展</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-21/10718425.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月21日电 (记者 孙自法)作为2026国际科学理事会中期会员大会暨北京科学对话的重要卫星会议之一，空间科学国际论坛10月20日在北京举行，推动空间科学领域跨国界、跨学科的开放合作与可持续发展。" data-title="如何应对空间研究当前挑战？国际组织和中外专家共商全球合作之策" data-date="10-21 13:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-21 13:53</span>
          <span class="news-item-title">如何应对空间研究当前挑战？国际组织和中外专家共商全球合作之策</span>
          <span class="news-value-point">💡 中新网北京10月21日电 (记者 孙自法)作为2026国际科学理事会中期会员大会暨北京科学对话的重要卫星会议之一，空间科学国际论坛10月20日在…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-21/10718404.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月21日电 综合外媒20日报道，美国司法部堪萨斯州联邦检察官办公室当地时间19日表示，一名涉嫌威胁刺杀美国总统特朗普的男子已被逮捕。" data-title="晚宴、球场、集会……特朗普屡遭刺杀威胁，美国政治暴力阴影难消" data-date="10-21 13:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-21 13:17</span>
          <span class="news-item-title">晚宴、球场、集会……特朗普屡遭刺杀威胁，美国政治暴力阴影难消</span>
          <span class="news-value-point">💡 中新网10月21日电 综合外媒20日报道，美国司法部堪萨斯州联邦检察官办公室当地时间19日表示，一名涉嫌威胁刺杀美国总统特朗普的男子已被逮捕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-21/10718402.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月21日电 综合消息：伊朗多名官员20日会见到访的巴基斯坦陆军参谋长穆尼尔，赞赏巴方斡旋努力，强调重启谈判的前提是美国采取措施建立信任。伊方明确表示，所有核材料都将留在伊朗国内。" data-title="伊朗强调所有核材料将留在国内 建立信任是谈判前提" data-date="10-21 13:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-21 13:16</span>
          <span class="news-item-title">伊朗强调所有核材料将留在国内 建立信任是谈判前提</span>
          <span class="news-value-point">💡 中新社北京10月21日电 综合消息：伊朗多名官员20日会见到访的巴基斯坦陆军参谋长穆尼尔，赞赏巴方斡旋努力，强调重启谈判的前提是美国采取措施建立…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-21/10718391.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月21日电 综合消息：也门战事20日多线持续交火，也门政府军称过去24小时内消灭约200名也门胡塞武装人员；胡塞方面则指责沙特阿拉伯空袭致平民死亡。同时，联合国机构20日警告，也门新一轮战事已迫使超25万人流离失所，当地人道主义危机加剧。" data-title="也门多线交火致人道主义危机加剧  超25万人流离失所" data-date="10-21 13:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-21 13:16</span>
          <span class="news-item-title">也门多线交火致人道主义危机加剧  超25万人流离失所</span>
          <span class="news-value-point">💡 中新社北京10月21日电 综合消息：也门战事20日多线持续交火，也门政府军称过去24小时内消灭约200名也门胡塞武装人员</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-21/10718367.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月21日电 综合消息：当地时间10月20日，乌克兰问题会谈在挪威奥斯陆举行。在会后记者会上，泽连斯基说：“我们做好了谈判的准备，任何缓和局势的信号都十分重要。”他还表示愿意同美国总统特朗普、俄罗斯总统普京举行三方会晤。" data-title="乌克兰总统表示愿意同美俄举行三方会晤" data-date="10-21 12:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-21 12:00</span>
          <span class="news-item-title">乌克兰总统表示愿意同美俄举行三方会晤</span>
          <span class="news-value-point">💡 中新网北京10月21日电 综合消息：当地时间10月20日，乌克兰问题会谈在挪威奥斯陆举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-21/10718362.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月21日电 阿布贾消息：尼日利亚卫生和社会福利部当地时间20日发布公告称，经实验室检测，该国联邦首都区发现一例埃博拉确诊病例。" data-title="尼日利亚报告一例埃博拉确诊病例" data-date="10-21 11:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-21 11:59</span>
          <span class="news-item-title">尼日利亚报告一例埃博拉确诊病例</span>
          <span class="news-value-point">💡 中新社北京10月21日电 阿布贾消息：尼日利亚卫生和社会福利部当地时间20日发布公告称，经实验室检测，该国联邦首都区发现一例埃博拉确诊病例</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-21/10718263.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月21日电(记者 刁炜)据路透社报道，近日，伊朗议会批准现年68岁的迈赫达德·阿赫拉基，出任伊朗国防部长兼武装部队后勤部长。" data-title="曾研发“会跳舞的导弹”，伊朗新防长警告美国别动武" data-date="10-21 11:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-21 11:59</span>
          <span class="news-item-title">曾研发“会跳舞的导弹”，伊朗新防长警告美国别动武</span>
          <span class="news-value-point">💡 中新网10月21日电(记者 刁炜)据路透社报道，近日，伊朗议会批准现年68岁的迈赫达德·阿赫拉基，出任伊朗国防部长兼武装部队后勤部长</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/20/us/politics/julio-herrera-pardon-alina-habba.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="委内瑞拉著名人物胡里奥·埃雷拉·韦卢蒂尼（ Julio Herrera Velutini ）正在寻求宽大处理。在他的女儿给哈巴这位与特朗普总统关系密切的律师一份利润丰厚的工作后不久，他就得到了这份工作。" data-title="A Billionaire Wanted a Trump Pardon. His Family Gave Alina Habba a $50 Million Deal." data-date="10-21 11:58" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-21 11:58</span>
          <span class="news-item-title">亿万富翁要求特朗普赦免。他的家人给了Alina Habba 5000万$的交易。</span>
          <span class="news-item-title-en">A Billionaire Wanted a Trump Pardon. His Family Gave Alina Habba a $50 Million Deal.</span>
          <span class="news-value-point">💡 委内瑞拉著名人物胡里奥·埃雷拉·韦卢蒂尼（ Julio Herrera Velutini ）正在寻求宽大处理</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-21/10718330.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月21日电 综合报道，以色列国防部长卡茨20日在社交媒体发文称，以色列国防军正在组建一支太空部队，此举将提高以军在太空领域的作战能力，目标是使以色列成为“太空安全领域的世界领先国家之一”。" data-title="以色列宣布组建太空部队 提高太空领域作战能力" data-date="10-21 11:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-21 11:26</span>
          <span class="news-item-title">以色列宣布组建太空部队 提高太空领域作战能力</span>
          <span class="news-value-point">💡 中新网10月21日电 综合报道，以色列国防部长卡茨20日在社交媒体发文称，以色列国防军正在组建一支太空部队，此举将提高以军在太空领域的作战能力，…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/20/us/politics/trump-maga-inc-midterms.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="这位任期有限的总统的超级政治行动委员会的巨额支出在美国历史上是前所未有的，可以为陷入困境的共和党候选人提供生命线。" data-title="Trump Wields an Unprecedented $277 Million in Final Midterm Stretch" data-date="10-21 11:14" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-21 11:14</span>
          <span class="news-item-title">特朗普在最后的中期计划中挥舞着前所未有的2.77亿美元$</span>
          <span class="news-item-title-en">Trump Wields an Unprecedented $277 Million in Final Midterm Stretch</span>
          <span class="news-value-point">💡 这位任期有限的总统的超级政治行动委员会的巨额支出在美国历史上是前所未有的，可以为陷入困境的共和党候选人提供生命线</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/news/1014989/trump-fraud-tips-program-nick-shirley-influencers" target="_blank" rel="noopener" data-cat="shizheng" data-summary="唐纳德·特朗普(Donald Trump)和副总统JD ·万斯(JD Vance)周二表示，特朗普政府将向右翼YouTube用户尼克·雪莉(Nick Shirley)提供1万美元，并启动一项2500万美元的赏金计划，让公众举报欺诈行为。2025年12月， Shirley" data-title="Trump is giving Nick Shirley $10,000 and launching a $25 million fraud bounty program" data-date="10-21 06:20" data-source="The Verge">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-21 06:20</span>
          <span class="news-item-title">特朗普将向尼克·雪莉（ Nick Shirley ）提供1万美元，并推出2500万美元的欺诈奖金计划</span>
          <span class="news-item-title-en">Trump is giving Nick Shirley $10,000 and launching a $25 million fraud bounty program</span>
          <span class="news-value-point">💡 唐纳德·特朗普(Donald Trump)和副总统JD ·万斯(JD Vance)周二表示，特朗普政府将向右翼YouTube用户尼克·雪莉(Ni…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-21/10718471.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网北京10月21日电 (记者 黄钰钦)记者21日从中国社会科学院获悉，中国—乌兹别克斯坦专家委员会第二次会议日前在乌兹别克斯坦世界经济与外交大学举行。会议以“数字伙伴关系：人工智能与新一代数据经济”为主题，聚焦数字化转型、人工智能治理与务实合作，探讨以科技创新赋能两国现代化建设新路径。" data-title="中国—乌兹别克斯坦专家委员会第二次会议举行 共商数字技术合作前景" data-date="10-21 14:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-21 14:34</span>
          <span class="news-item-title">中国—乌兹别克斯坦专家委员会第二次会议举行 共商数字技术合作前景</span>
          <span class="news-value-point">💡 中新网北京10月21日电 (记者 黄钰钦)记者21日从中国社会科学院获悉，中国—乌兹别克斯坦专家委员会第二次会议日前在乌兹别克斯坦世界经济与外交…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/015/847.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 21 日消息，据湖北日报报道，10 月 19 日，2026 年全球光纤光缆大会在武汉光谷开幕，来自 30 多个国家的行业组织与产业链代表参会。会上，由亚太光纤光缆产业协会（APC）技术委员会牵头，烽火通信、上海大学等单位联合编制的《通信用弱耦合单模多芯光纤技术要求第 1 部分：截止波长位移弱耦合单模多芯光纤》正式发布，这是全球首个多芯光纤国际标准。该标准填补了弱耦合单模多芯光纤产业化的标准空白，为其在人工智能数据中心（AIDC）高速光互联、大容量海底光缆系统、多维复用光纤通信系统等场景的规模化商用提供支撑。IT之家注：多芯光纤是一种在一根光纤包层内集成多个独立纤芯的新型光纤，能通过空分复用技术将单纤传输容量提升数倍至数十倍。" data-title="全球首个多芯光纤国际标准在武汉发布" data-date="10-21 14:29" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-21 14:29</span>
          <span class="news-item-title">全球首个多芯光纤国际标准在武汉发布</span>
          <span class="news-value-point">💡 IT之家 10 月 21 日消息，据湖北日报报道，10 月 19 日，2026 年全球光纤光缆大会在武汉光谷开幕，来自 30 多个国家的行业组织…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-21/10718436.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新社南宁10月21日电 (记者 蒋雪林 黄艳梅)“平陆运河通航为企业带来发展利好，既大幅降低从东南亚进口大宗原材料的运输成本，也让产品出海物流更高效。我们将利用广西的区位与政策优势，持续深化桂台产学研协同，助力广西打造面向东盟的新能源新材料产业集群。”在桂台商、华徽(广西)新材料科技有限公司总经理陈闵富21日接受中新社记者采访时说。" data-title="聚焦向海经济与人工智能 桂台携手拓“蓝海”" data-date="10-21 14:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-21 14:02</span>
          <span class="news-item-title">聚焦向海经济与人工智能 桂台携手拓“蓝海”</span>
          <span class="news-value-point">💡 中新社南宁10月21日电 (记者 蒋雪林 黄艳梅)“平陆运河通航为企业带来发展利好，既大幅降低从东南亚进口大宗原材料的运输成本，也让产品出海物流…</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/504608.html" target="_blank" rel="noopener" data-cat="keji" data-summary="先看真实问题解决力" data-title="飞书豆包工作AI先锋未来人才大赛：企业正在争抢会用AI做成事的人" data-date="10-21 10:37" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-21 10:37</span>
          <span class="news-item-title">飞书豆包工作AI先锋未来人才大赛：企业正在争抢会用AI做成事的人</span>
          <span class="news-value-point">💡 先看真实问题解决力</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/20/anthropic-pitches-ai-safety-bill-that-may-block-a-model-if-50-people-could-be-killed/" target="_blank" rel="noopener" data-cat="keji" data-summary="拟议的政策似乎提供了防止人工智能疯狂运行的保护措施，但实际上禁止联邦机构在未经法官许可的情况下阻止模型的发布。" data-title="Anthropic pitches AI safety bill that may block a model if 50+ people could be killed" data-date="10-21 07:01" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-21 07:01</span>
          <span class="news-item-title">Anthropic提出人工智能安全法案，如果超过50人可能被杀，可能会阻止模型</span>
          <span class="news-item-title-en">Anthropic pitches AI safety bill that may block a model if 50+ people could be killed</span>
          <span class="news-value-point">💡 拟议的政策似乎提供了防止人工智能疯狂运行的保护措施，但实际上禁止联邦机构在未经法官许可的情况下阻止模型的发布</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1014999/google-gemini-ai-cars-android-auto" target="_blank" rel="noopener" data-cat="keji" data-summary="谷歌正在将个人智能引入您的车中的Gemini AI。借助此次更新， Android Auto中的Gemini和内置Google的汽车可以在Google应用程序（包括Gmail、日历、地图、照片、YouTube和搜索）中挖掘您的信息。" data-title="Google’s more personalized Gemini AI is heading to your car" data-date="10-21 06:11" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-21 06:11</span>
          <span class="news-item-title">谷歌更个性化的双子座人工智能正走向您的汽车</span>
          <span class="news-item-title-en">Google’s more personalized Gemini AI is heading to your car</span>
          <span class="news-value-point">💡 谷歌正在将个人智能引入您的车中的Gemini AI</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/20/anthropics-cloud-partnerships-are-getting-messy/" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道， Anthropic正在努力从云提供商那里获得足够的计算，这些提供商越来越多地将其视为竞争对手，尽管其基础设施支出在计划于11月进行的首次公开募股之前激增。" data-title="Anthropic’s cloud partnerships are getting messy" data-date="10-21 05:25" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-21 05:25</span>
          <span class="news-item-title">Anthropic的云合作伙伴关系变得混乱</span>
          <span class="news-item-title-en">Anthropic’s cloud partnerships are getting messy</span>
          <span class="news-value-point">💡 据报道， Anthropic正在努力从云提供商那里获得足够的计算，这些提供商越来越多地将其视为竞争对手，尽管其基础设施支出在计划于11月进行的首…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/20/spacexs-ai-business-is-beating-expectations/" target="_blank" rel="noopener" data-cat="keji" data-summary="SpaceX在第三季度实现了盈利，净利润为44亿美元（ $ ）。人工智能是引擎。" data-title="SpaceX’s AI business is beating expectations" data-date="10-21 04:40" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-21 04:40</span>
          <span class="news-item-title">SpaceX的人工智能业务超出预期</span>
          <span class="news-item-title-en">SpaceX’s AI business is beating expectations</span>
          <span class="news-value-point">💡 SpaceX在第三季度实现了盈利，净利润为44亿美元（ $ ）</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/20/openai-acquires-startup-orchestra-bio%e2%81%a0-to-beef-up-its-biotech-business/" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI表示，它正在增加Orchestra的团队和技术，以开发其用于生命科学研究的人工智能模型Rosalind ，以及其相关的Rosalind Workbench工具，该工具旨在帮助研究人员计划实验和分析结果。" data-title="OpenAI acquires startup Orchestra Bio⁠ to beef up its biotech business" data-date="10-21 04:35" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-21 04:35</span>
          <span class="news-item-title">OpenAI收购创业公司Orchestra Bio ，以加强其生物技术业务</span>
          <span class="news-item-title-en">OpenAI acquires startup Orchestra Bio⁠ to beef up its biotech business</span>
          <span class="news-value-point">💡 OpenAI表示，它正在增加Orchestra的团队和技术，以开发其用于生命科学研究的人工智能模型Rosalind ，以及其相关的Rosalin…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/20/google-has-joined-amazon-in-attacking-nvidias-stronghold-with-ai-app-developers/" target="_blank" rel="noopener" data-cat="keji" data-summary="谷歌与亚马逊一起发布了一个开发人员工具，使PyTorch用户可以轻松地将其应用程序从Nvidia GPU上移除。" data-title="Google has joined Amazon in attacking Nvidia’s stronghold with AI app developers" data-date="10-21 02:38" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-21 02:38</span>
          <span class="news-item-title">谷歌已加入亚马逊，通过AI应用程序开发人员攻击Nvidia的据点</span>
          <span class="news-item-title-en">Google has joined Amazon in attacking Nvidia’s stronghold with AI app developers</span>
          <span class="news-value-point">💡 谷歌与亚马逊一起发布了一个开发人员工具，使PyTorch用户可以轻松地将其应用程序从Nvidia GPU上移除</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/20/chatgpt-now-lets-you-lock-your-chats/" target="_blank" rel="noopener" data-cat="keji" data-summary="该公司表示，该功能专为用户可能正在讨论个人或计划惊喜的情况而设计，并且在将设备交给朋友或家人以向他们展示" data-title="ChatGPT now lets you lock your chats" data-date="10-21 02:36" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-21 02:36</span>
          <span class="news-item-title">ChatGPT现在可以锁定您的聊天</span>
          <span class="news-item-title-en">ChatGPT now lets you lock your chats</span>
          <span class="news-value-point">💡 该公司表示，该功能专为用户可能正在讨论个人或计划惊喜的情况而设计，并且在将设备交给朋友或家人以向他们展示</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/20/eric-schmidt-reportedly-owns-about-half-as-much-of-anthropic-as-ceo-dario-amodei/" target="_blank" rel="noopener" data-cat="keji" data-summary="埃里克·施密特（ Eric Schmidt ）的财富即将变得更大。" data-title="Eric Schmidt reportedly owns about half as much of Anthropic as CEO Dario Amodei" data-date="10-21 01:55" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-21 01:55</span>
          <span class="news-item-title">据报道， Eric Schmidt拥有的Anthropic股份约为首席执行官Dario Amodei的一半</span>
          <span class="news-item-title-en">Eric Schmidt reportedly owns about half as much of Anthropic as CEO Dario Amodei</span>
          <span class="news-value-point">💡 埃里克·施密特（ Eric Schmidt ）的财富即将变得更大</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpu-drivers/amds-fsr-4-1-now-works-on-radeon-rx-6000-gpus-xbox-series-x-and-s-and-ryzen-ai-max-ai-9-and-z2-socs-new-release-brings-cutting-edge-tech-to-older-hardware-with-a-small-performance-cost" target="_blank" rel="noopener" data-cat="keji" data-summary="AMD发布了其尖端的FSR 4.1升级版，现在适用于Radeon RX 6000 GPU、Xbox Series X和Series S游戏机，以及Ryzen AI Max、AI 9和Z2芯片。" data-title="AMD&#39;s FSR 4.1 now works on Radeon RX 6000 cards, Xbox Series X and S, and Ryzen AI Max, AI 9, and Z2 SoCs" data-date="10-21 01:47" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-21 01:47</span>
          <span class="news-item-title">AMD的FSR 4.1现在适用于Radeon RX 6000卡、Xbox系列X和S以及Ryzen AI Max、AI 9和Z2 SoC</span>
          <span class="news-item-title-en">AMD's FSR 4.1 now works on Radeon RX 6000 cards, Xbox Series X and S, and Ryzen AI Max, AI 9, and Z2 SoCs</span>
          <span class="news-value-point">💡 AMD发布了其尖端的FSR 4.1升级版，现在适用于Radeon RX 6000 GPU、Xbox Series X和Series S游戏机，以…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/20/metas-muse-hits-10m-u-s-downloads-in-40-days-a-milestone-reached-by-only-11-other-apps/" target="_blank" rel="noopener" data-cat="keji" data-summary="Meta的人工智能伴侣Muse在前40天内在美国的下载量超过了1000万次，加入了包括Threads在内的独家应用程序组。新数据还显示， Muse保留用户的比率高于其人工智能竞争对手。" data-title="Meta’s Muse hits 10M U.S. downloads in 40 days, a milestone reached by only 11 other apps" data-date="10-21 01:12" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-21 01:12</span>
          <span class="news-item-title">Meta的Muse在40天内在美国下载量达到1000万次，这是其他11个应用程序达到的里程碑</span>
          <span class="news-item-title-en">Meta’s Muse hits 10M U.S. downloads in 40 days, a milestone reached by only 11 other apps</span>
          <span class="news-value-point">💡 Meta的人工智能伴侣Muse在前40天内在美国的下载量超过了1000万次，加入了包括Threads在内的独家应用程序组</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/news/1014455/amd-fsr-4-1-xbox-consoles-handhelds-laptops" target="_blank" rel="noopener" data-cat="keji" data-summary="AMD刚刚透露，它正在将其最新的升级技术FSR 4.1引入Xbox Series S和X游戏机，以及笔记本电脑、6000系列GPU和Xbox Ally X设备等手持设备。FSR 4.1将开始出现在Radeon RX 6000上-" data-title="AMD is bringing FSR 4.1 to Xbox consoles and handhelds" data-date="10-21 00:21" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-21 00:21</span>
          <span class="news-item-title">AMD将FSR 4.1引入Xbox游戏机和手持设备</span>
          <span class="news-item-title-en">AMD is bringing FSR 4.1 to Xbox consoles and handhelds</span>
          <span class="news-value-point">💡 AMD刚刚透露，它正在将其最新的升级技术FSR 4.1引入Xbox Series S和X游戏机，以及笔记本电脑、6000系列GPU和Xbox A…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">5 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ck4g10n56jzqo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="切尔西的行动首次与他们希望留住青训后卫乔希·阿奇庞（ Josh Acheampong ）的言论相吻合。" data-title="How England hopeful Acheampong is giving Chelsea a big decision to make" data-date="10-21 14:26" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-21 14:26</span>
          <span class="news-item-title">英格兰充满希望的Acheampong如何让切尔西做出重大决定</span>
          <span class="news-item-title-en">How England hopeful Acheampong is giving Chelsea a big decision to make</span>
          <span class="news-value-point">💡 切尔西的行动首次与他们希望留住青训后卫乔希·阿奇庞（ Josh Acheampong ）的言论相吻合</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/21/manchester-city-david-kogan-independent-football-regulator" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="IFR主席大卫·科根（ David Kogan ）坚称监管机构有权采取行动曼城已对英超联赛的指控提出上诉独立足球监管机构（ IFR ）将拥有“绝对权力” ，如果他们最终被发现" data-title="Football regulator has ‘absolute power’ to force Manchester City sale if verdict upheld" data-date="10-21 07:34" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-21 07:34</span>
          <span class="news-item-title">如果判决维持，足球监管机构有“绝对权力”迫使曼城出售</span>
          <span class="news-item-title-en">Football regulator has ‘absolute power’ to force Manchester City sale if verdict upheld</span>
          <span class="news-value-point">💡 IFR主席大卫·科根（ David Kogan ）坚称监管机构有权采取行动曼城已对英超联赛的指控提出上诉独立足球监管机构（ IFR ）将拥有“绝…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1014976/sam-altman-ann-altman-lawsuit-dismissed" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="周二，美国地区法官扎卡里·布鲁斯通（ Zachary Bluestone ）驳回了安·奥尔特曼（ Ann Altman ）去年提起的诉讼，指控她的兄弟、OpenAI首席执行官萨姆·奥尔特曼（ Sam Altman ）在她的整个童年时期对她进行了性虐待正如《卫报》早些时候报道的那样，法官写道" data-title="Judge dismisses Sam Altman’s sister’s sexual abuse lawsuit" data-date="10-21 07:04" data-source="The Verge">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-21 07:04</span>
          <span class="news-item-title">法官驳回Sam Altman姐姐的性虐待诉讼</span>
          <span class="news-item-title-en">Judge dismisses Sam Altman’s sister’s sexual abuse lawsuit</span>
          <span class="news-value-point">💡 周二，美国地区法官扎卡里·布鲁斯通（ Zachary Bluestone ）驳回了安·奥尔特曼（ Ann Altman ）去年提起的诉讼，指控她…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/news/articles/cm93z1xlgqxqo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="尚未开始正式调查，但监管机构正在对此案进行调查。" data-title="Audit regulator looking into Manchester City accounting" data-date="10-21 04:56" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-21 04:56</span>
          <span class="news-item-title">审计监管机构调查曼彻斯特城的会计</span>
          <span class="news-item-title-en">Audit regulator looking into Manchester City accounting</span>
          <span class="news-value-point">💡 尚未开始正式调查，但监管机构正在对此案进行调查</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cm3vqz1de9lro?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英超联赛裁判长霍华德·韦伯（ Howard Webb ）表示，斯文·博特曼（ Sven Botman ）对尼古拉斯·杰克逊（ Nicolas Jackson ）的挑战是一项“高端鲁莽的挑战” ，但支持视频助理裁判不干预红牌的决定。" data-title="Webb backs VAR over Botman challenge on Jackson" data-date="10-21 00:56" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-21 00:56</span>
          <span class="news-item-title">韦伯支持VAR对杰克逊的博特曼挑战</span>
          <span class="news-item-title-en">Webb backs VAR over Botman challenge on Jackson</span>
          <span class="news-value-point">💡 英超联赛裁判长霍华德·韦伯（ Howard Webb ）表示，斯文·博特曼（ Sven Botman ）对尼古拉斯·杰克逊（ Nicolas J…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/015/853.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 21 日消息，三星钱包昨日宣布，三星钱包数字车钥匙已支持吉利银河。据介绍，无需打开车企 App、无需设置后台常驻，即可完成无感解闭锁。IT之家附支持的吉利银河车型如下：吉利星愿2026 款星愿翼真 L3802025 款熊猫 mini2025 款熊猫卡丁2025 款熊猫骑士吉利星愿 Ultra吉利银河 L6吉利银河 L7熊猫 MINI熊猫卡丁熊猫骑士熊猫勇士吉利银河 E8吉利银河 E5战舰 700参考三星钱包数字车钥匙支持型号" data-title="三星钱包数字车钥匙支持吉利银河，可无感开关车门、启动车辆" data-date="10-21 14:40" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-21 14:40</span>
          <span class="news-item-title">三星钱包数字车钥匙支持吉利银河，可无感开关车门、启动车辆</span>
          <span class="news-value-point">💡 IT之家 10 月 21 日消息，三星钱包昨日宣布，三星钱包数字车钥匙已支持吉利银河</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/015/850.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 21 日消息，比亚迪王朝网销售事业部总经理路天刚刚公布了第三代秦 PLUS 全新海岛蓝车色的外观。据路天介绍，这一代新车设计，是科技美学的具象表达：前脸横向舒展，飒爽利落；流畅的溜背车身，优雅动感；加宽的车尾，气场更足；贯穿式中国结尾灯，一眼可辨。全新的海岛蓝车色，灵感来自海风拂过海面的清透质感。据IT之家此前报道，该车已经公布官图并完成工信部申报，预计 10 月下旬上市。申报信息显示，比亚迪秦 PLUS EV 为纯电动轿车，由比亚迪汽车工业有限公司申报，车身外形尺寸为长 4840mm、宽 1900mm、高 1498mm，轴距达到 2800mm。动力方面，该车搭载永磁同步驱动电机，型号为 TZ164XYD，由抚州比亚迪实业有限公司生产，峰值功率 100kW、额定功率 40" data-title="比亚迪第三代秦 PLUS 全新海岛蓝车色亮相：溜背车身、贯穿式中国结尾灯，预计 10 月下旬上市" data-date="10-21 14:38" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-21 14:38</span>
          <span class="news-item-title">比亚迪第三代秦 PLUS 全新海岛蓝车色亮相：溜背车身、贯穿式中国结尾灯，预计 10 月下旬上市</span>
          <span class="news-value-point">💡 IT之家 10 月 21 日消息，比亚迪王朝网销售事业部总经理路天刚刚公布了第三代秦 PLUS 全新海岛蓝车色的外观</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/015/849.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 21 日消息，印度证书颁发机构 eMudhra 的 8 个中间证书私钥被发现在生成时存在严重缺陷，Mozilla、谷歌、苹果、微软以及多个开发工具链已紧急吊销相关证书或发布更新。此次事件源于 eMudhra 旗下 emSign 的 8 张中间 CA（证书颁发机构）证书在私钥生成环节存在严重缺陷，正常情况下应具备 384 位随机性的 P-384 私钥实际取值却仅相当于个位数或两位数的整数，这导致相关私钥可被轻易推算。攻击者理论上能够在毫秒级时间内通过穷举还原，并利用这些密钥为任意域名签发伪造的 HTTPS 证书，从而冒充目标网站并拦截或篡改通信。Mozilla 安全团队 10 月 20 日发布公告称，该团队于 10 月 17 日 20:06 UTC 收到报告，获悉与 8 张" data-title="印度 eMudhra 中间证书私钥存在严重缺陷：Chrome、Firefox 迅速阻断，Go、Python、Rust 均需更新" data-date="10-21 14:32" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-21 14:32</span>
          <span class="news-item-title">印度 eMudhra 中间证书私钥存在严重缺陷：Chrome、Firefox 迅速阻断，Go、Python、Rust 均需更新</span>
          <span class="news-value-point">💡 IT之家 10 月 21 日消息，印度证书颁发机构 eMudhra 的 8 个中间证书私钥被发现在生成时存在严重缺陷，Mozilla、谷歌、苹果…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-21/10718455.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网巴中10月21日电 题：四川巴中：石刻未老，陵园常青" data-title="（长征胜利90周年）四川巴中：石刻未老，陵园常青" data-date="10-21 14:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-21 14:32</span>
          <span class="news-item-title">（长征胜利90周年）四川巴中：石刻未老，陵园常青</span>
          <span class="news-value-point">💡 中新网巴中10月21日电 题：四川巴中：石刻未老，陵园常青</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/015/848.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 21 日消息，美国宇航局（NASA）于 10 月 14 日发布博文，宣布“罗曼太空望远镜”（Nancy Grace Roman Space Telescope）在轨测试表现优于预期，其主相机“宽视场仪器”（Wide Field Instrument）的光学性能比原定指标高出近 30%，未来对宇宙的大范围巡天观测有望获得更锐利的图像。IT之家注：“罗曼太空望远镜”以美国宇航局首位女性高管南希 · 格雷斯 · 罗曼（她被誉为“哈勃太空望远镜之母”）命名，于 2026 年 8 月 30 日由 SpaceX“猎鹰重型”火箭发射，核心目标是快速扫描大片天空，研究暗能量、暗物质和系外行星。图源：美国宇航局按照原定设计要求，“宽视场仪器”的光学误差应控制在约 90 纳米均方根（RMS）" data-title="美国罗曼太空望远镜“视力”超常发挥，成像精度提升近 30%" data-date="10-21 14:30" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-21 14:30</span>
          <span class="news-item-title">美国罗曼太空望远镜“视力”超常发挥，成像精度提升近 30%</span>
          <span class="news-value-point">💡 IT之家 10 月 21 日消息，美国宇航局（NASA）于 10 月 14 日发布博文，宣布“罗曼太空望远镜”（Nancy Grace Roma…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/015/845.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 21 日消息，联合国表示，全球现已无法将升温控制在较工业化前水平上升 1.5℃ 以内；按照当前排放趋势，本世纪末全球升温将达到 2.8℃。尽管科学家不断发出愈发紧迫的警示，阐述升温突破 1.5℃ 所带来的各类风险，但全球排放量至今仍未下降，世界各国政府所采取的脱碳行动远远不足。联合国在最新的《排放差距报告》中指出，如今想要实现 1.5℃ 目标，唯一途径是短期内突破该阈值，然后依靠直接空气捕获等技术在本世纪下半叶大规模实施全球降温。这一“最低幅度超调”情景下，全球气温上升峰值将达到 1.7℃ 至 1.8℃，有 50% 概率在 2100 年回落至 1.5℃。要达成该情景，全球需要以 2025 年排放水平为基准，在 2030 年前减排 18%，2035 年前减排 45%，204" data-title="联合国最新报告：1.5℃ 控温目标已难守住，本世纪末全球升温将达 2.8℃" data-date="10-21 14:26" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-21 14:26</span>
          <span class="news-item-title">联合国最新报告：1.5℃ 控温目标已难守住，本世纪末全球升温将达 2.8℃</span>
          <span class="news-value-point">💡 IT之家 10 月 21 日消息，联合国表示，全球现已无法将升温控制在较工业化前水平上升 1.5℃ 以内</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-21/10718461.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网天津10月21日电 (孙翼飞)记者21日从天津市宁河区获悉，七里海湿地候鸟迁徙已进入高峰期，目前累计监测记录过境水鸟总量超5万只。" data-title="天津七里海湿地过境水鸟累计超5万只" data-date="10-21 14:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-21 14:23</span>
          <span class="news-item-title">天津七里海湿地过境水鸟累计超5万只</span>
          <span class="news-value-point">💡 中新网天津10月21日电 (孙翼飞)记者21日从天津市宁河区获悉，七里海湿地候鸟迁徙已进入高峰期，目前累计监测记录过境水鸟总量超5万只</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/015/844.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 21 日消息，Marshall（马歇尔）便携派对音箱 BROMLEY 150 现已在国行渠道上市。其拥有 IP54 防护，配备提手，可更换电池提供约 40hr 无线续航，集成舞台灯效，售价 3,999 元。BROMLEY 150 搭载 True Stereophonic 360° Sound 环绕立体声场技术，配备 1× 6.5&quot; 40W 低音单元（90W D 类功放）、2× 2&quot; 6W 全频单元（55W D 类功放）、1× 7.5&quot; 无源辐射器，频率响应范围 40~20000Hz，声压级达到 97dB。其具备 3.5mm AUX、XLR / 6.35mm、USB-C、蓝牙 5.3 输入，可接入麦克风或乐器，支持 SBC、AAC、LC3 编解码器。京东 Marshall" data-title="Marshall BROMLEY 150 便携派对音箱国行上市，3999 元" data-date="10-21 14:19" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-21 14:19</span>
          <span class="news-item-title">Marshall BROMLEY 150 便携派对音箱国行上市，3999 元</span>
          <span class="news-value-point">💡 IT之家 10 月 21 日消息，Marshall（马歇尔）便携派对音箱 BROMLEY 150 现已在国行渠道上市</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-21/10718431.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="重回聚光灯下，千万粉丝的关注让75岁老人“演奏拖堂”" data-title="“萨克斯大爷”：音乐漫湖岸,热爱抵流年" data-date="10-21 13:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-21 13:45</span>
          <span class="news-item-title">“萨克斯大爷”：音乐漫湖岸,热爱抵流年</span>
          <span class="news-value-point">💡 重回聚光灯下，千万粉丝的关注让75岁老人“演奏拖堂”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-21/10718393.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网10月21日电 据国家能源局网站消息，9月份，全社会用电量8997亿千瓦时，同比增长1.2%。从分产业用电看，第一产业用电量135亿千瓦时，同比增长4.1%。第二产业用电量5800亿千瓦时，同比增长1.7%；其中，工业用电量5751亿千瓦时，同比增长1.8%，高技术及装备制造业用电量1167亿千瓦时，同比增长4.6%。第三产业用电量1852亿千瓦时，同比增长4.9%；其中，充换电服务业、互联网数据服务用电量分别为168亿、98亿千瓦时，增速分别达到57.0%、35.4%。城乡居民生活用电量1210亿千瓦时，同比下降6.0%，主要原因是受“沙德尔”台风等极端天气影响，9月上中旬华中、华东、南方等高负荷区域降温用电需求下降。" data-title="9月份全社会用电量8997亿千瓦时 同比增长1.2%" data-date="10-21 13:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-21 13:39</span>
          <span class="news-item-title">9月份全社会用电量8997亿千瓦时 同比增长1.2%</span>
          <span class="news-value-point">💡 中新网10月21日电 据国家能源局网站消息，9月份，全社会用电量8997亿千瓦时，同比增长1.2%</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-21/10718403.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网杭州10月21日电 (钱晨菲)21日，根据《浙江省防汛防台抗旱应急预案》，经会商研判，浙江省防指决定于10月21日9时启动海上防台风应急响应。" data-title="台风“蔷琵”逼近 浙江启动海上防台风应急响应" data-date="10-21 13:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-21 13:29</span>
          <span class="news-item-title">台风“蔷琵”逼近 浙江启动海上防台风应急响应</span>
          <span class="news-value-point">💡 中新网杭州10月21日电 (钱晨菲)21日，根据《浙江省防汛防台抗旱应急预案》，经会商研判，浙江省防指决定于10月21日9时启动海上防台风应急响…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cw0k0n6x4k4eo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在不信任投票即将到来之际，康奈尔表示，Jane Doe 对校长反应的描述是“不正确的”。" data-title="康奈尔大学 Jane Doe 称，校长质疑她遭多人轮奸的指控" data-date="10-21 13:07" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-21 13:07</span>
          <span class="news-item-title">康奈尔大学 Jane Doe 称，校长质疑她遭多人轮奸的指控</span>
          <span class="news-value-point">💡 在不信任投票即将到来之际，康奈尔表示，Jane Doe 对校长反应的描述是“不正确的”</span>
        </a>
        <a class="news-item" href="https://arstechnica.com/security/2026/10/php-maintainers-tell-web-devs-to-prepare-themselves-for-critical-security-patches/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="未经确认的报告声称PHP2Shell利用在PHP站点上远程执行代码。" data-title="PHP warns it plans to release 2 emergency patches imminently" data-date="10-21 10:12" data-source="Ars Technica">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-arstechnica">🔬 Ars Technica</span>
          <span class="news-item-date">10-21 10:12</span>
          <span class="news-item-title">PHP警告它计划立即发布2个紧急补丁</span>
          <span class="news-item-title-en">PHP warns it plans to release 2 emergency patches imminently</span>
          <span class="news-value-point">💡 未经确认的报告声称PHP2Shell利用在PHP站点上远程执行代码</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/504551.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="电池、电驱、超充一把梭，冬天多跑30公里" data-title="理想宣布：电池自燃报废赔新车！自研6年后有底气了" data-date="10-21 09:04" data-source="量子位">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-21 09:04</span>
          <span class="news-item-title">理想宣布：电池自燃报废赔新车！自研6年后有底气了</span>
          <span class="news-value-point">💡 电池、电驱、超充一把梭，冬天多跑30公里</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cmp3gepg90x6o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="根据英国国家统计局（ONS）数据，目前有超过100万名电子烟使用者过去从未吸烟。" data-title="翻看英国统计 为何从未吸烟的人也开始对电子烟上瘾？" data-date="10-21 08:17" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-21 08:17</span>
          <span class="news-item-title">翻看英国统计 为何从未吸烟的人也开始对电子烟上瘾？</span>
          <span class="news-value-point">💡 根据英国国家统计局（ONS）数据，目前有超过100万名电子烟使用者过去从未吸烟</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-21 14:41（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
