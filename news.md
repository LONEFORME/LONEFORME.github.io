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
      <span>2026-11-02 01:59 抓取更新</span>
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
        <span class="channel-count">59</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('shizheng', this)">
        <span>🏛️ 时政与国际</span>
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('keji', this)">
        <span>🤖 AI模型 & 芯片算力</span>
        <span class="channel-count">14</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('zuqiu', this)">
        <span>⚽ 英超与足球风云</span>
        <span class="channel-count">15</span>
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
  <div class="ov-item"><span class="ov-num">59</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">10</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×10 · 天空体育×9</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.nytimes.com/2026/11/01/us/politics/election-mood-affordability.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在全国范围内，许多选民在特朗普总统的政策和通货膨胀之间划出了一条直线。" data-title="A Midterm Campaign Dominated by Concerns Over High Prices Nears Its End" data-date="11-02 01:42" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 11-02 01:42</span>
      </div>
      <h2 class="hero-featured-title">对高价担忧的中期竞选活动即将结束</h2>
      <div class="hero-featured-title-en">A Midterm Campaign Dominated by Concerns Over High Prices Nears Its End</div>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/brazilian-lawyers-busted-for-attempting-to-manipulate-courts-ai-with-prompt-injection-hidden-in-filing-courts-ai-flags-hidden-text-that-demanded-superficial-legal-scrutiny-lawyers-fined-usd16-000" target="_blank" rel="noopener" data-cat="keji" data-summary="在一起劳工案件中，原告的律师试图使用即时注入来影响法院的人工智能，但被抓获。无论如何，他们都赢了，因为被告没有回应，这使得此举完全没有必要。" data-title="Brazilian lawyers busted for attempting to manipulate court&#39;s AI with prompt injection hidden in filing" data-date="11-01 23:05" data-source="Tom's Hardware">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
      </div>
      <p class="hero-sub-title">Brazilian lawyers busted for attempting to manipulate court's AI with prompt injection hidden in filing</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/live/2026/nov/01/liverpool-v-arsenal-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="安菲尔德比赛（格林威治标准时间下午4:30 ）的最新消息桌|最佳射手|在这里给丹尼尔发电子邮件比赛在哪里？当阿森纳拥有球时，利物浦将寻求让球员围绕球，如果他们赢得控球权，就会为球员打开球场。当他们d" data-title="Liverpool v Arsenal: Premier League" data-date="11-02 02:00" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Liverpool v Arsenal: Premier League</p>
    </a>
    <a class="hero-sub-card" href="https://www.theverge.com/tech/1024219/apples-homeview-could-add-security-camera-features" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Reddit用户pdfu发现了隐藏在HomeView 27.2代码中的提示，即苹果可能会在其智能家居中心添加监控摄像头功能。字符串描述了具有运动检测、实时流式传输和录制选项的安全摄像头模式" data-title="Apple’s HomeView could add security camera features" data-date="11-02 01:16" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">Apple’s HomeView could add security camera features</p>
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
        <a class="news-item" href="https://www.nytimes.com/2026/11/01/us/politics/election-mood-affordability.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在全国范围内，许多选民在特朗普总统的政策和通货膨胀之间划出了一条直线。" data-title="A Midterm Campaign Dominated by Concerns Over High Prices Nears Its End" data-date="11-02 01:42" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-02 01:42</span>
          <span class="news-item-title">对高价担忧的中期竞选活动即将结束</span>
          <span class="news-item-title-en">A Midterm Campaign Dominated by Concerns Over High Prices Nears Its End</span>
          <span class="news-value-point">💡 在全国范围内，许多选民在特朗普总统的政策和通货膨胀之间划出了一条直线</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/01/us/alaska-ranked-choice-voting-peltola.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="除了激烈争议的参议院和州长竞选之外，阿拉斯加人将于周二决定是否取消该州的独特选票。玛丽·佩尔托拉（ Mary Peltola ）的竞选活动可能支持了对该系统的批评。" data-title="Did the Peltola Campaign Seal the Fate of Alaska’s Ranked Choice Vote?" data-date="11-01 23:21" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-01 23:21</span>
          <span class="news-item-title">佩尔托拉战役是否决定了阿拉斯加排名投票的命运？</span>
          <span class="news-item-title-en">Did the Peltola Campaign Seal the Fate of Alaska’s Ranked Choice Vote?</span>
          <span class="news-value-point">💡 除了激烈争议的参议院和州长竞选之外，阿拉斯加人将于周二决定是否取消该州的独特选票</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-01/10724519.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间11月1日，国际移民组织发布的最新数据显示，也门冲突导致超过30万人流离失所，这些人几乎都是过去两个月内流离失所的。战乱导致基本生活用品价格飙升，许多家庭难以找到住所，也难以负担基本生活必需品，而准入限制导致援助机构更难接触到需要帮助的人。" data-title="国际移民组织：也门流离失所者已超30万人" data-date="11-01 23:19" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-01 23:19</span>
          <span class="news-item-title">国际移民组织：也门流离失所者已超30万人</span>
          <span class="news-value-point">💡 当地时间11月1日，国际移民组织发布的最新数据显示，也门冲突导致超过30万人流离失所，这些人几乎都是过去两个月内流离失所的</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-01/10724518.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间1日，在谈及伊朗代表团访问卡塔尔事宜时，伊朗外长阿拉格齐表示，此次访问由副外长率领，目的是继续与卡塔尔调解方进行磋商。" data-title="伊朗外长：磋商是否能取得成果取决于美国的答复" data-date="11-01 23:18" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-01 23:18</span>
          <span class="news-item-title">伊朗外长：磋商是否能取得成果取决于美国的答复</span>
          <span class="news-value-point">💡 当地时间1日，在谈及伊朗代表团访问卡塔尔事宜时，伊朗外长阿拉格齐表示，此次访问由副外长率领，目的是继续与卡塔尔调解方进行磋商</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-01/10724511.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="【欧洲专线】中欧班列沿线国家代表在敦煌共话丝路交融与当代合作" data-title="中欧班列沿线国家代表在敦煌共话丝路交融与当代合作" data-date="11-01 22:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-01 22:12</span>
          <span class="news-item-title">中欧班列沿线国家代表在敦煌共话丝路交融与当代合作</span>
          <span class="news-value-point">💡 【欧洲专线】中欧班列沿线国家代表在敦煌共话丝路交融与当代合作</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-01/10724501.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网福建莆田11月1日电 (叶秋云)“妈祖文化倡导的‘立德、行善、大爱’精神，与中华民族优秀传统美德一脉相承，将其与海洋防灾减灾、海洋生态文明、海洋科技创新有机融合，有助于大力提升海洋防灾减灾能力。”中国海洋大学教授王海涛1日在福建莆田湄洲岛参加第十一届世界妈祖文化论坛时如是表示。" data-title="海内外专家聚首“妈祖故里”谈妈祖文化减灾智慧" data-date="11-01 21:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-01 21:43</span>
          <span class="news-item-title">海内外专家聚首“妈祖故里”谈妈祖文化减灾智慧</span>
          <span class="news-value-point">💡 中新网福建莆田11月1日电 (叶秋云)“妈祖文化倡导的‘立德、行善、大爱’精神，与中华民族优秀传统美德一脉相承，将其与海洋防灾减灾、海洋生态文明…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-01/10724507.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间10月31日，法国爆发近三周以来第三轮全国性大规模抗议示威活动。据法国内政部统计，截至11月1日，法国全国已有779人在31日的示威游行中被拘留。" data-title="法国新一轮示威活动中已有779人被捕" data-date="11-01 21:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-01 21:42</span>
          <span class="news-item-title">法国新一轮示威活动中已有779人被捕</span>
          <span class="news-value-point">💡 当地时间10月31日，法国爆发近三周以来第三轮全国性大规模抗议示威活动</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-01/10724499.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京11月1日电 新华社11月1日受权全文播发《中共中央关于持之以恒推进全面从严治党若干重大问题的决定》和中共中央总书记习近平所作的《关于〈中共中央关于持之以恒推进全面从严治党若干重大问题的决定〉的说明》。" data-title="新华社受权全文播发《中共中央关于持之以恒推进全面从严治党若干重大问题的决定》和习近平总书记所作的《关于〈中共中央关于持之以恒推进全面从严治党若干重大问题的决定〉的说明》" data-date="11-01 21:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-01 21:10</span>
          <span class="news-item-title">新华社受权全文播发《中共中央关于持之以恒推进全面从严治党若干重大问题的决定》和习近平总书记所作的《关于〈中共中央关于持之以恒推进全面从严治党若干重大问题的决定〉的说明》</span>
          <span class="news-value-point">💡 新华社北京11月1日电 新华社11月1日受权全文播发《中共中央关于持之以恒推进全面从严治党若干重大问题的决定》和中共中央总书记习近平所作的《关于…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-01/10724414.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社福州11月1日电 (记者 闫旭)新时代城市高质量发展市长论坛11月1日在福州举行。作为2026年世界城市日全球主场活动的主论坛，该论坛吸引了海内外百余名城市市长、国际组织代表、专家学者参加。" data-title="多国市长福州共话高质量推进城市更新" data-date="11-01 20:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-01 20:44</span>
          <span class="news-item-title">多国市长福州共话高质量推进城市更新</span>
          <span class="news-value-point">💡 中新社福州11月1日电 (记者 闫旭)新时代城市高质量发展市长论坛11月1日在福州举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-01/10724487.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京11月1日电(记者赵瀚泽)应国家主席习近平邀请，阿曼苏丹海赛姆11月1日抵达北京，开始对中国进行为期两天的国事访问。" data-title="阿曼苏丹海赛姆抵达北京开始访华" data-date="11-01 20:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-01 20:42</span>
          <span class="news-item-title">阿曼苏丹海赛姆抵达北京开始访华</span>
          <span class="news-value-point">💡 新华社北京11月1日电(记者赵瀚泽)应国家主席习近平邀请，阿曼苏丹海赛姆11月1日抵达北京，开始对中国进行为期两天的国事访问</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-01/10724474.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月1日电 综合塔斯社、俄罗斯卫星通讯社11月1日报道，俄罗斯总统助理乌沙科夫在接受采访时表示，俄罗斯总统普京从未拒绝与乌克兰总统泽连斯基对话。" data-title="俄总统助理：普京从未拒绝与泽连斯基对话，泽连斯基可以来莫斯科" data-date="11-01 20:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-01 20:09</span>
          <span class="news-item-title">俄总统助理：普京从未拒绝与泽连斯基对话，泽连斯基可以来莫斯科</span>
          <span class="news-value-point">💡 中新网11月1日电 综合塔斯社、俄罗斯卫星通讯社11月1日报道，俄罗斯总统助理乌沙科夫在接受采访时表示，俄罗斯总统普京从未拒绝与乌克兰总统泽连斯…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/01/world/middleeast/netanyahu-coalition-building-tests-political-skills.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在以色列大选中失利后，总理本雅明·内塔尼亚胡（ Benjamin Netanyahu ）必须利用数十年的政治资本，并与老对手打交道，才能建立执政联盟。" data-title="Netanyahu’s Bid to Stay in Power Will Test His Political Savvy" data-date="11-01 18:20" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-01 18:20</span>
          <span class="news-item-title">内塔尼亚胡继续执政的举动将考验他的政治智慧</span>
          <span class="news-item-title-en">Netanyahu’s Bid to Stay in Power Will Test His Political Savvy</span>
          <span class="news-value-point">💡 在以色列大选中失利后，总理本雅明·内塔尼亚胡（ Benjamin Netanyahu ）必须利用数十年的政治资本，并与老对手打交道，才能建立执政…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/01/world/middleeast/israel-arab-parties.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="这两个阿拉伯人领导的政党在以色列议会赢得了创纪录的19个席位，他们表示希望与反对派合作，推翻内塔尼亚胡政府。" data-title="Where Do Israel’s Arab Parties Stand?" data-date="11-01 18:03" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-01 18:03</span>
          <span class="news-item-title">以色列的阿拉伯政党的立场如何？</span>
          <span class="news-item-title-en">Where Do Israel’s Arab Parties Stand?</span>
          <span class="news-value-point">💡 这两个阿拉伯人领导的政党在以色列议会赢得了创纪录的19个席位，他们表示希望与反对派合作，推翻内塔尼亚胡政府</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/01/us/politics/trump-speeches-rallies-age.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="《泰晤士报》对总统公开演讲的评论发现，他比2016年更亵渎、更专制、更长篇大论、更缺乏连贯性。" data-title="Gaffes and Men’s Bodies: Analysis of Trump’s Speeches at Age 80" data-date="11-01 18:01" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-01 18:01</span>
          <span class="news-item-title">失言与男人的身体：对特朗普80岁演讲的分析</span>
          <span class="news-item-title-en">Gaffes and Men’s Bodies: Analysis of Trump’s Speeches at Age 80</span>
          <span class="news-value-point">💡 《泰晤士报》对总统公开演讲的评论发现，他比2016年更亵渎、更专制、更长篇大论、更缺乏连贯性</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cwn8dkzrm8lvo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="由美国第一夫人梅拉尼娅·特朗普（Melania Trump）斡旋达成的人道停火在赫尔松（Kherson）地区生效，令当地四年来首次出现数天和平时段，并让奥列什基（Oleshky）居民得以撤离。" data-title="“我们从地狱回来”" data-date="11-01 12:24" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-01 12:24</span>
          <span class="news-item-title">“我们从地狱回来”</span>
          <span class="news-value-point">💡 由美国第一夫人梅拉尼娅·特朗普（Melania Trump）斡旋达成的人道停火在赫尔松（Kherson）地区生效，令当地四年来首次出现数天和平时…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">14 条</span>
    </div>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/brazilian-lawyers-busted-for-attempting-to-manipulate-courts-ai-with-prompt-injection-hidden-in-filing-courts-ai-flags-hidden-text-that-demanded-superficial-legal-scrutiny-lawyers-fined-usd16-000" target="_blank" rel="noopener" data-cat="keji" data-summary="在一起劳工案件中，原告的律师试图使用即时注入来影响法院的人工智能，但被抓获。无论如何，他们都赢了，因为被告没有回应，这使得此举完全没有必要。" data-title="Brazilian lawyers busted for attempting to manipulate court&#39;s AI with prompt injection hidden in filing" data-date="11-01 23:05" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-01 23:05</span>
          <span class="news-item-title">巴西律师因试图操纵法院的人工智能而被捕，提示注入隐藏在文件中</span>
          <span class="news-item-title-en">Brazilian lawyers busted for attempting to manipulate court's AI with prompt injection hidden in filing</span>
          <span class="news-value-point">💡 在一起劳工案件中，原告的律师试图使用即时注入来影响法院的人工智能，但被抓获</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/sam-altman-travels-to-south-korea-to-meet-samsung-leadership-to-secure-more-ram-for-data-centers-amid-crushing-shortages-openai-ceo-meets-samsung-leadership-to-discuss-future-ai-data-centers" target="_blank" rel="noopener" data-cat="keji" data-summary="10月31日， OpenAI首席执行官Sam Altman在韩国会见了大约50名三星高管，讨论了人工智能的未来、商业机会以及该技术对企业运营的影响。会议召开之际，对内存芯片的需求也随之增长" data-title="Sam Altman meets with Samsung leadership to secure more RAM for data centers amid crushing shortages" data-date="11-01 22:21" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-01 22:21</span>
          <span class="news-item-title">Sam Altman与三星领导层会面，在严重短缺的情况下为数据中心提供更多RAM</span>
          <span class="news-item-title-en">Sam Altman meets with Samsung leadership to secure more RAM for data centers amid crushing shortages</span>
          <span class="news-value-point">💡 10月31日， OpenAI首席执行官Sam Altman在韩国会见了大约50名三星高管，讨论了人工智能的未来、商业机会以及该技术对企业运营的影…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/020/837.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 1 日消息，OpenAI、谷歌、微软以及 Anthropic 近日宣布将采用一项新标准，内容发布方可以借助该标准选择拒绝 AI 抓取自家网站内容。借助这项管控机制，内容发布方可以一次性向多家 AI 企业统一申明自身针对 AI 模型训练的内容使用偏好，而不必为每家企业单独设置规则。该标准由 Anthropic 技术负责人 Kevin Kelley 向互联网工程任务组（IETF）提出，并将集成在网站的 robots.txt 文件中。长期以来，robots.txt 文件用于告知网络爬虫哪些网站内容允许抓取、哪些禁止抓取，适用场景包含搜索索引、网页归档以及 AI 模型训练。目前，网站必须向每一家 AI 企业分别单独声明自己的 AI 训练相关内容使用偏好。在此背景下，各类 AI 爬" data-title="OpenAI、谷歌、微软和 Anthropic 联手推行 AI 数据抓取退出标准" data-date="11-01 22:19" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-01 22:19</span>
          <span class="news-item-title">OpenAI、谷歌、微软和 Anthropic 联手推行 AI 数据抓取退出标准</span>
          <span class="news-value-point">💡 IT之家 11 月 1 日消息，OpenAI、谷歌、微软以及 Anthropic 近日宣布将采用一项新标准，内容发布方可以借助该标准选择拒绝 A…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/020/836.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 1 日消息，海贝宣布推出一款 HiBy R6III SE 便携 Hi-Fi 播放器，定价为 1798 元。该机整体尺寸为 129.4 x 73.1 x 15.6 mm，重量为 250 g。提供黑色和海军蓝两种颜色选择，正面配备了一块 5 英寸 1280x720 分辨率 IPS 面板，背部搭配了钻石切割纹理的玻璃背板。该机采用 4 颗 CS43198 DAC 芯片，支持 8 路独立输出。耳放部分支持 A 类和 AB 类模式切换，其中 A 类耳放由 OPA1652 运放、晶体管及 ELNA 音频电容组成。硬件搭载 45.158MHz 和 49.152MHz 两颗专用音频晶振。该机搭载骁龙 665 处理器，配备 3GB RAM 与 32GB 存储空间，机身底部配备 3.5mm" data-title="海贝推出 HiBy R6III SE 便携 Hi-Fi 播放器：4 颗 CS43198 DAC 芯片，1798 元" data-date="11-01 22:01" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-01 22:01</span>
          <span class="news-item-title">海贝推出 HiBy R6III SE 便携 Hi-Fi 播放器：4 颗 CS43198 DAC 芯片，1798 元</span>
          <span class="news-value-point">💡 IT之家 11 月 1 日消息，海贝宣布推出一款 HiBy R6III SE 便携 Hi-Fi 播放器，定价为 1798 元</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/open-source-usb-tool-unlocks-nvidias-half-speed-gpu-ai-limiter-on-windows-lifts-gpus-fp16-math-performance-up-to-65-percent-uefi-unlocker-covers-rtx-20-30-and-40-series-desktops-and-laptops" target="_blank" rel="noopener" data-cat="keji" data-summary="开源UEFI工具nv-uefi-unlocker提升了Nvidia在Windows下RTX 20、30和40系列GPU上的张量速率上限。" data-title="Open-source USB tool unlocks Nvidia&#39;s half-speed GPU AI limiter on Windows" data-date="11-01 22:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-01 22:00</span>
          <span class="news-item-title">开源USB工具在Windows上解锁Nvidia的半速GPU AI限制器</span>
          <span class="news-item-title-en">Open-source USB tool unlocks Nvidia's half-speed GPU AI limiter on Windows</span>
          <span class="news-value-point">💡 开源UEFI工具nv-uefi-unlocker提升了Nvidia在Windows下RTX 20、30和40系列GPU上的张量速率上限</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1024108/homepod-mini-2-hands-on-siri-smart-home-mac-speaker" target="_blank" rel="noopener" data-cat="keji" data-summary="当我上个月在苹果的欢迎回家活动上第一次听说新的$ 149 HomePod Mini 2时，我感到很失望。苹果推出入门级智能音箱已经六年了，它在第二代中得到的只是一个芯片凸起，一些颜色" data-title="HomePod Mini 2 first look: Three things I love and one disappointment" data-date="11-01 22:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-01 22:00</span>
          <span class="news-item-title">HomePod Mini 2首次亮相：三件我喜欢的事情和一件令人失望的事情</span>
          <span class="news-item-title-en">HomePod Mini 2 first look: Three things I love and one disappointment</span>
          <span class="news-value-point">💡 当我上个月在苹果的欢迎回家活动上第一次听说新的$ 149 HomePod Mini 2时，我感到很失望</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/020/834.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 1 日消息，消息源 smashx_60 现已曝光了 HMD 旗下诺基亚 2360 Flip 翻盖功能机，该机据称为 ODM 产品。该机提供深灰色、酒红色、蓝绿色三种配色可选，配备 1.8 英寸外屏和 2.8 英寸 LCD 内屏，搭载 1Mp 摄像头。该机搭载紫光展锐 T127 芯片，搭载 4MB RAM，内置 4MB 存储空间，同时支持 32GB microSD 卡扩展。手机内置 1450mAh 电池，使用 USB-C 接口。" data-title="HMD 诺基亚 2360 Flip 翻盖功能机曝光：紫光展锐 T127 芯片，1.8 英寸外屏" data-date="11-01 21:45" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-01 21:45</span>
          <span class="news-item-title">HMD 诺基亚 2360 Flip 翻盖功能机曝光：紫光展锐 T127 芯片，1.8 英寸外屏</span>
          <span class="news-value-point">💡 IT之家 11 月 1 日消息，消息源 smashx_60 现已曝光了 HMD 旗下诺基亚 2360 Flip 翻盖功能机，该机据称为 ODM …</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/507076.html" target="_blank" rel="noopener" data-cat="keji" data-summary="西湖世界模型研究中心成立" data-title="三年前布局，今年爆火丨西湖大学成立新中心" data-date="11-01 21:28" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-01 21:28</span>
          <span class="news-item-title">三年前布局，今年爆火丨西湖大学成立新中心</span>
          <span class="news-value-point">💡 西湖世界模型研究中心成立</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/507038.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Claude紧急叫停！暗改Harness禁止逆向游戏" data-title="Claude紧急叫停！暗改Harness禁止逆向游戏" data-date="11-01 21:09" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-01 21:09</span>
          <span class="news-item-title">Claude紧急叫停！暗改Harness禁止逆向游戏</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/507031.html" target="_blank" rel="noopener" data-cat="keji" data-summary="让AI像牛顿一样思考" data-title="清华姚期智团队新作：代数世界模型，让AI像牛顿一样思考" data-date="11-01 16:02" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-01 16:02</span>
          <span class="news-item-title">清华姚期智团队新作：代数世界模型，让AI像牛顿一样思考</span>
          <span class="news-value-point">💡 让AI像牛顿一样思考</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/506990.html" target="_blank" rel="noopener" data-cat="keji" data-summary="这事还是想得太简单了" data-title="老牌便利店机器人售货折戟：实验室锤炼上万次，货架前还是摔瓶子" data-date="11-01 15:50" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-01 15:50</span>
          <span class="news-item-title">老牌便利店机器人售货折戟：实验室锤炼上万次，货架前还是摔瓶子</span>
          <span class="news-value-point">💡 这事还是想得太简单了</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/506922.html" target="_blank" rel="noopener" data-cat="keji" data-summary="再次“性价比屠夫”" data-title="Jev新成果，再次引爆开源" data-date="11-01 12:18" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-01 12:18</span>
          <span class="news-item-title">Jev新成果，再次引爆开源</span>
          <span class="news-value-point">💡 再次“性价比屠夫”</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/31/apple-ceo-says-the-company-doesnt-want-to-ship-ai-for-ais-sake/" target="_blank" rel="noopener" data-cat="keji" data-summary="苹果新任首席执行官为公司目前在人工智能领域的地位辩护。" data-title="Apple CEO says the company doesn’t ‘want to ship AI for AI’s sake’" data-date="11-01 05:41" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-01 05:41</span>
          <span class="news-item-title">苹果首席执行官表示，该公司“不想为人工智能出货”</span>
          <span class="news-item-title-en">Apple CEO says the company doesn’t ‘want to ship AI for AI’s sake’</span>
          <span class="news-value-point">💡 苹果新任首席执行官为公司目前在人工智能领域的地位辩护</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/31/judge-allows-naacp-lawsuit-over-xai-data-center-pollution-to-move-forward/" target="_blank" rel="noopener" data-cat="keji" data-summary="全国有色人种协进会（ NAACP ）的一起诉讼指控SpaceX拥有的人工智能公司违反了《清洁空气法》。" data-title="Judge allows NAACP lawsuit over xAI data center pollution to move forward" data-date="11-01 05:17" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-01 05:17</span>
          <span class="news-item-title">法官允许NAACP就xAI数据中心污染提起诉讼</span>
          <span class="news-item-title-en">Judge allows NAACP lawsuit over xAI data center pollution to move forward</span>
          <span class="news-value-point">💡 全国有色人种协进会（ NAACP ）的一起诉讼指控SpaceX拥有的人工智能公司违反了《清洁空气法》</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/nov/01/liverpool-v-arsenal-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="安菲尔德比赛（格林威治标准时间下午4:30 ）的最新消息桌|最佳射手|在这里给丹尼尔发电子邮件比赛在哪里？当阿森纳拥有球时，利物浦将寻求让球员围绕球，如果他们赢得控球权，就会为球员打开球场。当他们d" data-title="Liverpool v Arsenal: Premier League" data-date="11-02 02:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-02 02:00</span>
          <span class="news-item-title">利物浦v阿森纳：英超</span>
          <span class="news-item-title-en">Liverpool v Arsenal: Premier League</span>
          <span class="news-value-point">💡 安菲尔德比赛（格林威治标准时间下午4:30 ）的最新消息桌|最佳射手|在这里给丹尼尔发电子邮件比赛在哪里</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/01/michael-carrick-manchester-united-favourite-premier-league-sack-race" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="不同寻常的是，顶级联赛中的所有俱乐部都有同一位经理，他们本赛季的开局经理是同一个人–但第一次解雇可能并不遥远本赛季还没有英超经理丢掉工作。在过去的10次活动中，只有三次是11月份的" data-title="Michael Carrick remains favourite in the Premier League sack race | Andrew Beasley" data-date="11-02 02:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-02 02:00</span>
          <span class="news-item-title">迈克尔·卡里克（ Michael Carrick ）仍然是英超麻袋赛的最爱|安德鲁·比斯利（ Andrew</span>
          <span class="news-item-title-en">Michael Carrick remains favourite in the Premier League sack race | Andrew Beasley</span>
          <span class="news-value-point">💡 不同寻常的是，顶级联赛中的所有俱乐部都有同一位经理，他们本赛季的开局经理是同一个人–但第一次解雇可能并不遥远本赛季还没有英超经理丢掉工作</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13606752/asia-pacific-amateur-championship-day-four-highlights" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="亚太业余锦标赛第四天的亮点， FIFA Laopakdee赢得了大师赛和公开锦标赛的邀请。" data-title="Laopakdee earns major invites after winning Asia-Pacific Amateur Championship" data-date="11-02 01:21" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-02 01:21</span>
          <span class="news-item-title">Laopakdee在赢得亚太业余锦标赛后赢得了重要的邀请</span>
          <span class="news-item-title-en">Laopakdee earns major invites after winning Asia-Pacific Amateur Championship</span>
          <span class="news-value-point">💡 亚太业余锦标赛第四天的亮点， FIFA Laopakdee赢得了大师赛和公开锦标赛的邀请</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13606708/manchester-united-gary-neville-says-club-are-in-a-rut-and-is-unimpressed-with-lisandro-martinez-amid-tough-run-of-games-for-michael-carricks-side" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="加里·内维尔（ Gary Neville ）表示，曼联陷入了困境，未来艰难的比赛将导致老特拉福德“非常令人担忧”。" data-title="Neville: Man Utd stuck in a rut - and it&#39;s really worrying" data-date="11-02 00:45" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-02 00:45</span>
          <span class="news-item-title">内维尔：曼联陷入困境-这真的令人担忧</span>
          <span class="news-item-title-en">Neville: Man Utd stuck in a rut - and it's really worrying</span>
          <span class="news-value-point">💡 加里·内维尔（ Gary Neville ）表示，曼联陷入了困境，未来艰难的比赛将导致老特拉福德“非常令人担忧”</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13606708/manchester-united-gary-neville-says-club-are-in-a-rut-and-is-unimpressed-with-lisandro-martinez-amid-tough-run-of-games-for-michael-carricks-side" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="加里·内维尔（ Gary Neville ）表示，曼联陷入了困境，未来艰难的比赛将导致老特拉福德“非常令人担忧”。" data-title="Neville: Man Utd stuck in a rut - and it&#39;s really worrying" data-date="11-02 00:45" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-02 00:45</span>
          <span class="news-item-title">内维尔：曼联陷入困境-这真的令人担忧</span>
          <span class="news-item-title-en">Neville: Man Utd stuck in a rut - and it's really worrying</span>
          <span class="news-value-point">💡 加里·内维尔（ Gary Neville ）表示，曼联陷入了困境，未来艰难的比赛将导致老特拉福德“非常令人担忧”</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/rugby-union/news/12040/13606709/steve-borthwick-england-must-quickly-adjust-from-prem-to-test-rugby-for-nations-championship" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="史蒂夫·博思维克（ Steve Borthwick ）承认，英格兰需要迅速弥合英超和测试橄榄球之间的差距，才能在秋季取得成功。" data-title="Borthwick: England must quickly adjust from Prem to Test rugby for Nations Championship" data-date="11-02 00:17" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-02 00:17</span>
          <span class="news-item-title">Borthwick ：英格兰必须迅速从Prem调整到国家锦标赛的测试橄榄球</span>
          <span class="news-item-title-en">Borthwick: England must quickly adjust from Prem to Test rugby for Nations Championship</span>
          <span class="news-value-point">💡 史蒂夫·博思维克（ Steve Borthwick ）承认，英格兰需要迅速弥合英超和测试橄榄球之间的差距，才能在秋季取得成功</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/liverpool-vs-arsenal/live/559530" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Liverpool still hunting for equaliser in entertaining Arsenal encounter LIVE!" data-title="Liverpool still hunting for equaliser in entertaining Arsenal encounter LIVE!" data-date="11-01 22:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-01 22:00</span>
          <span class="news-item-title">利物浦仍在寻找阿森纳现场娱乐遭遇战的均衡器！</span>
          <span class="news-item-title-en">Liverpool still hunting for equaliser in entertaining Arsenal encounter LIVE!</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/nov/01/carrick-defiant-after-latest-defeat-liverpool-v-arsenal-buildup-wsl-and-more-matchday-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="为周日的比赛做准备，利物浦在英超联赛中主办阿森纳之前获得了一份丰厚的WSL比赛名单至少可以说，诺丁汉森林的奥利弗·格拉斯纳（ Oliver Glasner ）表现不佳。“对我来说，我回家和家人一起吃早餐，所以" data-title="Carrick to stay in charge for Roma game; Challinor in at Sheffield Wednesday; Liverpool v Arsenal buildup" data-date="11-01 20:03" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-01 20:03</span>
          <span class="news-item-title">卡里克将继续负责罗马比赛;周三在谢菲尔德的Challinor;利物浦对阿森纳的积累</span>
          <span class="news-item-title-en">Carrick to stay in charge for Roma game; Challinor in at Sheffield Wednesday; Liverpool v Arsenal buildup</span>
          <span class="news-value-point">💡 为周日的比赛做准备，利物浦在英超联赛中主办阿森纳之前获得了一份丰厚的WSL比赛名单至少可以说，诺丁汉森林的奥利弗·格拉斯纳（ Oliver Gl…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/01/how-to-watch-premier-league-liverpool-arsenal" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦和阿森纳今天的表现如何？以下是需要了解的内容，包括开球时间、电视频道和直播选项连续五场胜利，包括周三的卡拉宝杯点球大战战胜切尔西，给人的印象是安东尼" data-title="Premier League today: How to watch, TV channels &amp; live stream" data-date="11-01 19:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-01 19:30</span>
          <span class="news-item-title">今日英超联赛：如何观看、收看电视频道和直播</span>
          <span class="news-item-title-en">Premier League today: How to watch, TV channels & live stream</span>
          <span class="news-value-point">💡 利物浦和阿森纳今天的表现如何</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ckzd6217j7pgo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在周日卫冕冠军阿森纳访问之前，利物浦球迷再次在安菲尔德寻找快乐，在俱乐部周围有一个感觉良好的因素。" data-title="Anfield, intensity, rotation - how Iraola is improving Liverpool" data-date="11-01 15:38" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-01 15:38</span>
          <span class="news-item-title">安菲尔德，强度，旋转- Iraola如何改善利物浦</span>
          <span class="news-item-title-en">Anfield, intensity, rotation - how Iraola is improving Liverpool</span>
          <span class="news-value-point">💡 在周日卫冕冠军阿森纳访问之前，利物浦球迷再次在安菲尔德寻找快乐，在俱乐部周围有一个感觉良好的因素</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c8g47wl06vkqo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="如果整个赛季继续下去，曼联目前在9场比赛中得到的7分甚至不会得到30分。" data-title="Are Manchester United really at risk of a relegation scrap?" data-date="11-01 07:52" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-01 07:52</span>
          <span class="news-item-title">曼联真的有降级的风险吗？</span>
          <span class="news-item-title-en">Are Manchester United really at risk of a relegation scrap?</span>
          <span class="news-value-point">💡 如果整个赛季继续下去，曼联目前在9场比赛中得到的7分甚至不会得到30分</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/10/premier-league-top-scorers-2026-27-race-for-golden-boot" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="找出哪位英国顶尖射手正在向进球排行榜射击。继续阅读……" data-title="Premier League top scorers 2026-27: who is leading race for the golden boot?" data-date="11-01 06:42" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-01 06:42</span>
          <span class="news-item-title">2026-27赛季英超联赛最佳射手：谁是金靴赛的领跑者？</span>
          <span class="news-item-title-en">Premier League top scorers 2026-27: who is leading race for the golden boot?</span>
          <span class="news-value-point">💡 找出哪位英国顶尖射手正在向进球排行榜射击</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/31/aston-villa-fulham-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="富勒姆帮助巩固了杰米·卡拉格（ Jamie Carragher ）的论点，即阿斯顿维拉永远不会成为曼联。不，他们知道如何在糟糕的一天磨出一分，周二可以放心地去巴塞罗那。别墅的守门员锡安·铃木（ Zion Suzuki ）放弃了亚历克斯" data-title="Zion Suzuki horror own goal haunts Aston Villa to hand Fulham a point" data-date="11-01 06:15" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-01 06:15</span>
          <span class="news-item-title">锡安铃木恐怖自己的进球困扰着阿斯顿维拉给富勒姆一分</span>
          <span class="news-item-title-en">Zion Suzuki horror own goal haunts Aston Villa to hand Fulham a point</span>
          <span class="news-value-point">💡 富勒姆帮助巩固了杰米·卡拉格（ Jamie Carragher ）的论点，即阿斯顿维拉永远不会成为曼联</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/aston-villa-vs-fulham/report/559524" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="尼古拉斯·杰克逊（ Nicolas Jackson ）在10场比赛中打入第八个进球，但守门员锡安·铃木（ Zion Suzuki ）的失误意味着阿斯顿维拉（ Aston Villa ）不得不在主场对阵富勒姆（" data-title="Suzuki makes string of saves before conceding own goal in draw with Fulham" data-date="11-01 05:45" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-01 05:45</span>
          <span class="news-item-title">铃木在与富勒姆的平局中放弃自己的进球之前进行了一连串的扑救</span>
          <span class="news-item-title-en">Suzuki makes string of saves before conceding own goal in draw with Fulham</span>
          <span class="news-value-point">💡 尼古拉斯·杰克逊（ Nicolas Jackson ）在10场比赛中打入第八个进球，但守门员锡安·铃木（ Zion Suzuki ）的失误意味着…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6n04v897qe4o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="首席足球作家菲尔·麦克纳尔蒂（ Phil McNulty ）问道，在连续第三次赢得英超联赛冠军后，马刺终于在罗伯托·德·泽比（ Roberto de Zerbi" data-title="Are De Zerbi&#39;s Spurs finding elusive consistency?" data-date="11-01 05:16" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-01 05:16</span>
          <span class="news-item-title">De Zerbi的马刺队是否发现难以捉摸的一致性？</span>
          <span class="news-item-title-en">Are De Zerbi's Spurs finding elusive consistency?</span>
          <span class="news-value-point">💡 首席足球作家菲尔·麦克纳尔蒂（ Phil McNulty ）问道，在连续第三次赢得英超联赛冠军后，马刺终于在罗伯托·德·泽比（ Roberto …</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theverge.com/tech/1024219/apples-homeview-could-add-security-camera-features" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Reddit用户pdfu发现了隐藏在HomeView 27.2代码中的提示，即苹果可能会在其智能家居中心添加监控摄像头功能。字符串描述了具有运动检测、实时流式传输和录制选项的安全摄像头模式" data-title="Apple’s HomeView could add security camera features" data-date="11-02 01:16" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-02 01:16</span>
          <span class="news-item-title">苹果的HomeView可以添加监控摄像头功能</span>
          <span class="news-item-title-en">Apple’s HomeView could add security camera features</span>
          <span class="news-value-point">💡 Reddit用户pdfu发现了隐藏在HomeView 27.2代码中的提示，即苹果可能会在其智能家居中心添加监控摄像头功能</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13606749/maybank-championship-day-four-highlights" target="_blank" rel="noopener" data-cat="zonghe" data-summary="吉隆坡LPGA马来亚银行锦标赛第四轮比赛的亮点。" data-title="Yamashita comes out on top at Maybank Championship" data-date="11-02 01:14" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-02 01:14</span>
          <span class="news-item-title">Yamashita在Maybank锦标赛中名列前茅</span>
          <span class="news-item-title-en">Yamashita comes out on top at Maybank Championship</span>
          <span class="news-value-point">💡 吉隆坡LPGA马来亚银行锦标赛第四轮比赛的亮点</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/31/world/asia/congress-cjp-protest-delhi-india-modi.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="成千上万的人聚集在印度首都，喧闹的鼓声，吟唱和摇曳的旗帜，来自全国各地的参与者。" data-title="India’s Congress Party Holds Mass Protest in New Delhi" data-date="11-02 00:51" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-02 00:51</span>
          <span class="news-item-title">印度国大党在新德里举行大规模抗议活动</span>
          <span class="news-item-title-en">India’s Congress Party Holds Mass Protest in New Delhi</span>
          <span class="news-value-point">💡 成千上万的人聚集在印度首都，喧闹的鼓声，吟唱和摇曳的旗帜，来自全国各地的参与者</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/desktops/gaming-pcs/lucky-pc-buyer-gets-usd1-200-discount-on-9900x3d-gaming-pc-walmart-honors-usd1-099-shelf-price-on-usd2-299-unit" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Redditor在实体沃尔玛零售店以超过50%的折扣获得一台游戏PC。" data-title="Walmart honors massive shelf price mistake, lucky buyer gets two $2,299 CyberPowerPC gaming rigs for $1,099 each" data-date="11-01 23:53" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-01 23:53</span>
          <span class="news-item-title">沃尔玛尊重巨大的货架价格错误，幸运的买家以每台$ 1,099的价格获得两个$ 2,299的CyberPowerPC游戏钻机</span>
          <span class="news-item-title-en">Walmart honors massive shelf price mistake, lucky buyer gets two $2,299 CyberPowerPC gaming rigs for $1,099 each</span>
          <span class="news-value-point">💡 Redditor在实体沃尔玛零售店以超过50%的折扣获得一台游戏PC</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/020/841.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 1 日消息，米哈游生活模拟游戏《星布谷地》今日官宣，将于 2027 年登陆 Switch2 平台。IT之家注意到，《星布谷地》已经确认推出 PC / iOS / Android 版，将于 12 月 4 日开启全球公测。这款游戏以星际田园为主题，玩家在游戏中将可以赶海、钓鱼、种田等，期待理想生活自然发生，拥有自定义系统，可随心装点天空、海岸与每一片土地，三五好友可相聚在星空街市，使善意、共鸣、友谊在星空下交汇。目前，官方公布的游戏角色有云果、伊佐奇、绵朵莉、幻雪等，它们的造型都类似小动物，各自拥有不同的身份，玩家可以在游戏中与这些性格各异的角色缔结友谊。" data-title="米哈游生活模拟游戏《星布谷地》官宣 2027 年登陆任天堂 Switch 2" data-date="11-01 23:37" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-01 23:37</span>
          <span class="news-item-title">米哈游生活模拟游戏《星布谷地》官宣 2027 年登陆任天堂 Switch 2</span>
          <span class="news-value-point">💡 IT之家 11 月 1 日消息，米哈游生活模拟游戏《星布谷地》今日官宣，将于 2027 年登陆 Switch2 平台</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13606700/celtic-team-in-regression-under-martin-oneill-and-manager-to-blame-says-chris-sutton" target="_blank" rel="noopener" data-cat="zonghe" data-summary="“这是一个等待凯尔特人队的彩票。谁知道马丁会选哪支球队？”" data-title="&#39;This is on Martin&#39; - Sutton blames O&#39;Neill for Celtic struggles" data-date="11-01 23:37" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-01 23:37</span>
          <span class="news-item-title">“这是在马丁身上” -萨顿将凯尔特人的挣扎归咎于奥尼尔</span>
          <span class="news-item-title-en">'This is on Martin' - Sutton blames O'Neill for Celtic struggles</span>
          <span class="news-value-point">💡 “这是一个等待凯尔特人队的彩票</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/01/nyregion/new-york-city-marathon-celebrities-running.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="演员、真人秀明星和运动员是众多跑步者中的一员。喜剧演员特蕾西·摩根（ Tracy Morgan ）是该活动的大警长。" data-title="Here Are Some of the Celebrities Running in the NYC Marathon" data-date="11-01 23:18" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-01 23:18</span>
          <span class="news-item-title">以下是参加纽约马拉松比赛的一些名人</span>
          <span class="news-item-title-en">Here Are Some of the Celebrities Running in the NYC Marathon</span>
          <span class="news-value-point">💡 演员、真人秀明星和运动员是众多跑步者中的一员</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/tennis/news/12040/13606593/carlos-alcaraz-spaniard-seals-erste-bank-open-victory-in-vienna-as-he-defeats-alex-de-minaur" target="_blank" rel="noopener" data-cat="zonghe" data-summary="卡洛斯·阿尔卡拉斯（ Carlos Alcaraz ）在维也纳的埃尔斯特银行公开赛决赛中击败亚历克斯·德米诺尔（ Alex de Minaur ） ，赢得了伤病中断赛季的第四个冠军。" data-title="Alcaraz waltzes past De Minaur to win Vienna title for first time" data-date="11-01 23:15" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-01 23:15</span>
          <span class="news-item-title">阿尔卡拉兹跳过德米诺尔，首次赢得维也纳冠军</span>
          <span class="news-item-title-en">Alcaraz waltzes past De Minaur to win Vienna title for first time</span>
          <span class="news-value-point">💡 卡洛斯·阿尔卡拉斯（ Carlos Alcaraz ）在维也纳的埃尔斯特银行公开赛决赛中击败亚历克斯·德米诺尔（ Alex de Minaur …</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/020/840.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 1 日消息，SteamDB 平台显示，《影之刃零》Steam 峰值在线玩家数达到 83 万创下新高，这部国产武侠游戏在线人数连续四天走高。IT之家注意到，国产 3A 游戏《影之刃零》现已正式发售，登陆 PS5 与 PC 平台，国区数字标准版售价 268 元，数字豪华版售价 328 元。PS5 实体光碟将于 2027 年推出。该作由灵游坊自主研发发行，采用虚幻引擎 5 打造，定位黑暗武侠题材第三人称动作冒险与单机动作 RPG，把中国武术与蒸汽朋克融合为功夫朋克风格，美术深沉黑暗，主打快节奏高速战斗。在《影之刃零》中，玩家将化身心脏遭受重创的剑客，在仅余六十六天的生命里，逃亡于刀光剑影和腥风血雨之间，并粉碎一桩笼罩在整个武林上方的惊天阴谋。在失序末法的武林中以身证道，以命寻心" data-title="国产武侠游戏《影之刃零》Steam 峰值在线玩家 83 万创新高，连续四天走高" data-date="11-01 23:01" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-01 23:01</span>
          <span class="news-item-title">国产武侠游戏《影之刃零》Steam 峰值在线玩家 83 万创新高，连续四天走高</span>
          <span class="news-value-point">💡 IT之家 11 月 1 日消息，SteamDB 平台显示，《影之刃零》Steam 峰值在线玩家数达到 83 万创下新高，这部国产武侠游戏在线人数…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/3d-printing/anycubic-and-thingiverse-announce-exclusive-3d-printing-partnership-makeronline-platform-to-offer-1-click-multicolor-3mf-models" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Thingiverse与Anycubic合作，将模型直接带入3D打印机。" data-title="Anycubic and Thingiverse announce exclusive 3D printing partnership" data-date="11-01 23:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-01 23:00</span>
          <span class="news-item-title">Anycubic和Thingiverse宣布独家3D打印合作伙伴关系</span>
          <span class="news-item-title-en">Anycubic and Thingiverse announce exclusive 3D printing partnership</span>
          <span class="news-value-point">💡 Thingiverse与Anycubic合作，将模型直接带入3D打印机</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/ssds/biwin-m560-2tb-ssd-review" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Biwin M560将SMI的SM2504XT带入零售业，具有顶级的响应速度和卓越的效率，但不是最快的post-cache写入速度。" data-title="Biwin M560 2TB SSD Review: The DRAM" data-date="11-01 23:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-01 23:00</span>
          <span class="news-item-title">Biwin M560 2TB SSD回顾： DRAM</span>
          <span class="news-item-title-en">Biwin M560 2TB SSD Review: The DRAM</span>
          <span class="news-value-point">💡 Biwin M560将SMI的SM2504XT带入零售业，具有顶级的响应速度和卓越的效率，但不是最快的post-cache写入速度</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1024176/north-korea-binance-crypto-heist" target="_blank" rel="noopener" data-cat="zonghe" data-summary="联邦调查局表示，朝鲜是10月29日袭击币安的大规模63亿美元加密货币抢劫案的幕后黑手。联邦调查局将该活动标记为“TraderTraitor” ，并表示已观察到与黑客有关的演员将令牌转换为以太坊" data-title="North Korea linked to massive Binance crypto heist" data-date="11-01 22:33" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-01 22:33</span>
          <span class="news-item-title">朝鲜与大规模币安加密货币抢劫有关</span>
          <span class="news-item-title-en">North Korea linked to massive Binance crypto heist</span>
          <span class="news-value-point">💡 联邦调查局表示，朝鲜是10月29日袭击币安的大规模63亿美元加密货币抢劫案的幕后黑手</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/3d-printing/bambu-labs-black-friday-sale-cuts-up-to-usd300-on-the-flagship-h2c-printer-and-more-deep-cuts-across-companys-3d-printer-and-filament-lineup" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在Bambu Lab的黑色星期五促销中尽早达成协议。直至12月1日，他们的旗舰3D打印机最高可节省$ 300。" data-title="Bambu Lab&#39;s Black Friday sale cuts up to $300 on the flagship H2C printer and more" data-date="11-01 22:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-01 22:30</span>
          <span class="news-item-title">Bambu Lab的黑色星期五促销活动在旗舰H2C打印机等产品上削减了高达300 $</span>
          <span class="news-item-title-en">Bambu Lab's Black Friday sale cuts up to $300 on the flagship H2C printer and more</span>
          <span class="news-value-point">💡 在Bambu Lab的黑色星期五促销中尽早达成协议</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-01/10724513.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="出国探亲，有人把签证交给中介代办。可钱花了、办下来的却不是约定的签证类型，中介该不该担责？消费者能否索赔全部损失？近日，北京市西城区人民法院就审结了这样一起案件。" data-title="代办“超级签”落地后发现竟是旅游签 中介该如何赔偿？" data-date="11-01 22:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-01 22:20</span>
          <span class="news-item-title">代办“超级签”落地后发现竟是旅游签 中介该如何赔偿？</span>
          <span class="news-value-point">💡 出国探亲，有人把签证交给中介代办</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/020/835.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 1 日消息，2026 年 10 月汽车销量 / 交付数据现已陆续公布。比亚迪拿出单月交付 490,168 辆的答卷，继续稳坐头把交椅。上汽集团凭销售 430,018 辆的成绩位居亚军。吉利以 310,183 辆的销量超越奇瑞（282,458 辆）拿下第三。另外，零跑汽车实现连续 4 个月月销超 10 万台（10 月销量为 106,127 辆）。小米汽车交付量在 10 月重回 50,000 辆（小米汽车 2025 年 12 月交付量超过 5 万辆）。“蔚小理”9 月分别交出 34,246 辆、50,237 辆、29,025 辆成绩。鸿蒙智行 10 月交付新车 33,537 辆，均价超过 40 万元。IT之家汇总 2026 年 10 月汽车销量 / 交付榜单如下（包含目前已公" data-title="2026 年 10 月汽车销量 / 交付榜出炉：比亚迪超 49 万辆稳居榜首，小米月销重回 5 万辆" data-date="11-01 21:53" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-01 21:53</span>
          <span class="news-item-title">2026 年 10 月汽车销量 / 交付榜出炉：比亚迪超 49 万辆稳居榜首，小米月销重回 5 万辆</span>
          <span class="news-value-point">💡 IT之家 11 月 1 日消息，2026 年 10 月汽车销量 / 交付数据现已陆续公布</span>
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


<p class="news-updated">🕐 抓取更新于 2026-11-02 01:59（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
