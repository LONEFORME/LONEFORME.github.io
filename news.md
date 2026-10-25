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
      <span>2026-10-26 00:37 抓取更新</span>
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
        <span class="channel-count">52</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('shizheng', this)">
        <span>🏛️ 时政与国际</span>
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('keji', this)">
        <span>🤖 AI模型 & 芯片算力</span>
        <span class="channel-count">7</span>
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
  <div class="ov-item"><span class="ov-num">52</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×14 · 天空体育×7</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.nytimes.com/2026/10/25/world/middleeast/saudi-arabia-riyadh-airport-reopens.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="伊朗支持的也门民兵胡塞武装本月在机场发动了几次致命袭击。" data-title="Saudi Arabia Reopens Riyadh Airport Even as Houthis Threaten Further Strikes" data-date="10-25 23:50" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 10-25 23:50</span>
      </div>
      <h2 class="hero-featured-title">沙特阿拉伯重新开放利雅得机场，尽管胡塞武装威胁要进一步罢工</h2>
      <div class="hero-featured-title-en">Saudi Arabia Reopens Riyadh Airport Even as Houthis Threaten Further Strikes</div>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/big-tech-is-cashing-in-on-ai-while-the-rest-of-corporate-america-sees-no-financial-returns-report-outlines-how-rising-token-costs-threaten-to-squeeze-corporate-profit-margins" target="_blank" rel="noopener" data-cat="keji" data-summary="Magnificent Seven的每名员工收入已超过标准普尔493指数，一项新的比较凸显了美国最大的科技公司与标准普尔500指数其他公司之间的财富差距日益扩大。" data-title="Big Tech is cashing in on AI while the rest of corporate America sees no financial returns" data-date="10-25 23:25" data-source="Tom's Hardware">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
      </div>
      <p class="hero-sub-title">Big Tech is cashing in on AI while the rest of corporate America sees no financial returns</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/live/2026/oct/25/sunderland-v-leeds-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英超联赛现场更新从英国夏令时下午4:30开始欧洲对桑德兰的诅咒多于祝福报名参加足球每日1分钟窥视！当我们观看时，利兹在他们的黄色换衣带中从左到右开球。普罗科菲耶夫在体育场的单簧管上" data-title="Sunderland v Leeds: Premier League" data-date="10-26 00:37" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Sunderland v Leeds: Premier League</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/darts/live-blog/12040/13603407/european-championship-darts-commentary-updates-scores-analysis-with-luke-littler-in-finals-day-in-dortmund" target="_blank" rel="noopener" data-cat="zonghe" data-summary="&#39;It was my chance and I took it!&#39; - Ratajski savours shock Littler win" data-title="&#39;It was my chance and I took it!&#39; - Ratajski savours shock Littler win" data-date="10-26 00:00" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">'It was my chance and I took it!' - Ratajski savours shock Littler win</p>
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
        <a class="news-item" href="https://www.nytimes.com/2026/10/25/world/middleeast/saudi-arabia-riyadh-airport-reopens.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="伊朗支持的也门民兵胡塞武装本月在机场发动了几次致命袭击。" data-title="Saudi Arabia Reopens Riyadh Airport Even as Houthis Threaten Further Strikes" data-date="10-25 23:50" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-25 23:50</span>
          <span class="news-item-title">沙特阿拉伯重新开放利雅得机场，尽管胡塞武装威胁要进一步罢工</span>
          <span class="news-item-title-en">Saudi Arabia Reopens Riyadh Airport Even as Houthis Threaten Further Strikes</span>
          <span class="news-value-point">💡 伊朗支持的也门民兵胡塞武装本月在机场发动了几次致命袭击</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-25/10720855.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社安徽六安10月25日电 题：两岸同忆台静农：渡海传薪续文脉 “歇脚庵”里话古今" data-title="两岸同忆台静农：渡海传薪续文脉 “歇脚庵”里话古今" data-date="10-25 22:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 22:09</span>
          <span class="news-item-title">两岸同忆台静农：渡海传薪续文脉 “歇脚庵”里话古今</span>
          <span class="news-value-point">💡 中新社安徽六安10月25日电 题：两岸同忆台静农：渡海传薪续文脉 “歇脚庵”里话古今</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/ukrainian-drone-attacks-hammer-russias-finance-ministry-data-center-damaged-facility-reportedly-holds-tax-databases-facility-also-holds-other-important-state-registry-data" target="_blank" rel="noopener" data-cat="shizheng" data-summary="据报道，这是俄罗斯财政部运营的三个数据中心之一。" data-title="Ukrainian drone attacks hammer Russia&#39;s finance ministry data center, damaged facility reportedly holds tax databases" data-date="10-25 22:05" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-25 22:05</span>
          <span class="news-item-title">乌克兰无人机袭击锤击俄罗斯财政部数据中心，据报道受损设施持有税务数据库</span>
          <span class="news-item-title-en">Ukrainian drone attacks hammer Russia's finance ministry data center, damaged facility reportedly holds tax databases</span>
          <span class="news-value-point">💡 据报道，这是俄罗斯财政部运营的三个数据中心之一</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-25/10720840.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网福州10月25日电 (叶秋云)由福建省文化和旅游厅主办，福建省闽台文化交流中心承办的“周末戏相逢”2026年闽台青少年街舞展演25日晚在福建博物院则徐广场周末戏相逢大舞台举办。" data-title="2026年闽台青少年街舞展演在福州举办" data-date="10-25 21:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 21:01</span>
          <span class="news-item-title">2026年闽台青少年街舞展演在福州举办</span>
          <span class="news-value-point">💡 中新网福州10月25日电 (叶秋云)由福建省文化和旅游厅主办，福建省闽台文化交流中心承办的“周末戏相逢”2026年闽台青少年街舞展演25日晚在福…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-25/10720822.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网福州10月25日电 题：台湾专家：从“养老”到“享老”为两岸康养融合提供新机遇" data-title="台湾专家：从“养老”到“享老”为两岸康养融合提供新机遇" data-date="10-25 20:51" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 20:51</span>
          <span class="news-item-title">台湾专家：从“养老”到“享老”为两岸康养融合提供新机遇</span>
          <span class="news-value-point">💡 中新网福州10月25日电 题：台湾专家：从“养老”到“享老”为两岸康养融合提供新机遇</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-25/10720828.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网银川10月25日电 (记者 于晶)25日，记者从宁夏回族自治区市场监督管理厅(知识产权局)获悉，宁夏政府常务会议审议通过《宁夏回族自治区知识产权保护和运用“十五五”规划》，为未来五年宁夏知识产权治理体系完善、保护运用效能提升划定路线图。" data-title="宁夏知识产权保护和运用“十五五”规划获批 锚定2030年知识产权强区建设目标" data-date="10-25 20:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 20:48</span>
          <span class="news-item-title">宁夏知识产权保护和运用“十五五”规划获批 锚定2030年知识产权强区建设目标</span>
          <span class="news-value-point">💡 中新网银川10月25日电 (记者 于晶)25日，记者从宁夏回族自治区市场监督管理厅(知识产权局)获悉，宁夏政府常务会议审议通过《宁夏回族自治区知…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-25/10720823.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网福建武平10月25日电 (李源杰 王展雄 邱靖)10月23日至25日，2026年武台定光文化交流活动在福建省龙岩市武平县举办。活动以“武台同源，两岸共福”为主题，助推海峡两岸文化交流样板建设，增进两岸同胞心灵契合。" data-title="2026年武台定光文化交流活动在福建武平举办" data-date="10-25 20:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 20:45</span>
          <span class="news-item-title">2026年武台定光文化交流活动在福建武平举办</span>
          <span class="news-value-point">💡 中新网福建武平10月25日电 (李源杰 王展雄 邱靖)10月23日至25日，2026年武台定光文化交流活动在福建省龙岩市武平县举办</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-25/10720832.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="河北省第十四届人民代表大会常务委员会公告" data-title="河北省第十四届人民代表大会常务委员会公告" data-date="10-25 20:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 20:42</span>
          <span class="news-item-title">河北省第十四届人民代表大会常务委员会公告</span>
          <span class="news-value-point">💡 河北省第十四届人民代表大会常务委员会公告</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-25/10720807.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间10月25日上午8时，巴西总统选举开始第二轮投票，选民将在劳工党候选人、现任总统卢拉和自由党候选人、前总统雅伊尔·博索纳罗之子弗拉维奥·博索纳罗之间选出下任总统。" data-title="巴西总统选举第二轮投票开始" data-date="10-25 20:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 20:08</span>
          <span class="news-item-title">巴西总统选举第二轮投票开始</span>
          <span class="news-value-point">💡 当地时间10月25日上午8时，巴西总统选举开始第二轮投票，选民将在劳工党候选人、现任总统卢拉和自由党候选人、前总统雅伊尔·博索纳罗之子弗拉维奥·…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-25/10720739.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月25日电 综合消息：也门胡塞武装25日发布警告称，位于沙特阿拉伯首都利雅得的哈立德国王国际机场仍是其军事打击目标，禁止前往和使用。该机场24日晚发布通知，宣布25日恢复开放部分航站楼。" data-title="沙特首都机场拟恢复运营 也门胡塞武装紧急警告" data-date="10-25 19:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 19:27</span>
          <span class="news-item-title">沙特首都机场拟恢复运营 也门胡塞武装紧急警告</span>
          <span class="news-value-point">💡 中新社北京10月25日电 综合消息：也门胡塞武装25日发布警告称，位于沙特阿拉伯首都利雅得的哈立德国王国际机场仍是其军事打击目标，禁止前往和使用</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/25/world/middleeast/israels-high-stakes-election-what-to-know.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="以色列人将于周二前往投票站进行选举，以决定该国的下一任总理。但组建新政府可能需要数周、数月或更长时间。" data-title="Israel’s High-Stakes Election: What to Know" data-date="10-25 17:01" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-25 17:01</span>
          <span class="news-item-title">以色列高风险选举：须知</span>
          <span class="news-item-title-en">Israel’s High-Stakes Election: What to Know</span>
          <span class="news-value-point">💡 以色列人将于周二前往投票站进行选举，以决定该国的下一任总理</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-25/10720710.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月25日电 综合外媒报道，美国将于11月3日迎来中期选举，共和党和民主党两大阵营加大造势和拉票力度。" data-title="隔空互怼！奥巴马批评：现任美国政府造成混乱局面 特朗普回击：“你的集会现场空荡荡”" data-date="10-25 15:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 15:42</span>
          <span class="news-item-title">隔空互怼！奥巴马批评：现任美国政府造成混乱局面 特朗普回击：“你的集会现场空荡荡”</span>
          <span class="news-value-point">💡 中新网10月25日电 综合外媒报道，美国将于11月3日迎来中期选举，共和党和民主党两大阵营加大造势和拉票力度</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-25/10720701.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社巴黎10月25日电 (记者 李洋)法国当地时间24日出现新一轮全国性抗议示威活动，仍有数十万人参与。法国官方称，已有近千人被捕。" data-title="法国新一轮抗议示威活动有近千人被捕" data-date="10-25 15:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 15:37</span>
          <span class="news-item-title">法国新一轮抗议示威活动有近千人被捕</span>
          <span class="news-value-point">💡 中新社巴黎10月25日电 (记者 李洋)法国当地时间24日出现新一轮全国性抗议示威活动，仍有数十万人参与</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-25/10720698.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社悉尼10月25日电 (记者 薄雯雯)澳大利亚昆士兰州洛根市24日晚发生枪击事件，造成4人受伤，其中1人伤势危重。当地警方25日表示，至少3名涉案嫌疑人仍在逃。" data-title="澳大利亚昆州发生枪击事件致4人受伤" data-date="10-25 15:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 15:36</span>
          <span class="news-item-title">澳大利亚昆州发生枪击事件致4人受伤</span>
          <span class="news-value-point">💡 中新社悉尼10月25日电 (记者 薄雯雯)澳大利亚昆士兰州洛根市24日晚发生枪击事件，造成4人受伤，其中1人伤势危重</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-25/10720679.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社河北雄安10月25日电 题：专访英国48家集团俱乐部副主席：全球治理倡议维护国际关系积极成果" data-title="专访英国48家集团俱乐部副主席：全球治理倡议维护国际关系积极成果" data-date="10-25 15:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 15:35</span>
          <span class="news-item-title">专访英国48家集团俱乐部副主席：全球治理倡议维护国际关系积极成果</span>
          <span class="news-value-point">💡 中新社河北雄安10月25日电 题：专访英国48家集团俱乐部副主席：全球治理倡议维护国际关系积极成果</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">7 条</span>
    </div>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/big-tech-is-cashing-in-on-ai-while-the-rest-of-corporate-america-sees-no-financial-returns-report-outlines-how-rising-token-costs-threaten-to-squeeze-corporate-profit-margins" target="_blank" rel="noopener" data-cat="keji" data-summary="Magnificent Seven的每名员工收入已超过标准普尔493指数，一项新的比较凸显了美国最大的科技公司与标准普尔500指数其他公司之间的财富差距日益扩大。" data-title="Big Tech is cashing in on AI while the rest of corporate America sees no financial returns" data-date="10-25 23:25" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-25 23:25</span>
          <span class="news-item-title">大型科技公司正在利用人工智能赚钱，而美国其他企业则看不到财务回报</span>
          <span class="news-item-title-en">Big Tech is cashing in on AI while the rest of corporate America sees no financial returns</span>
          <span class="news-value-point">💡 Magnificent Seven的每名员工收入已超过标准普尔493指数，一项新的比较凸显了美国最大的科技公司与标准普尔500指数其他公司之间的…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1018217/reddit-opensource-ai-ban" target="_blank" rel="noopener" data-cat="keji" data-summary="R/opensource的mod发布了新的提交规则，其中包括禁止使用人工智能的项目。周六晚上发布的帖子开头说： “如果您的项目使用人工智能，由人工智能制作，或打算用于人工智能，则不欢迎使用r/opensour" data-title="r/opensource just banned AI, non-English speakers, and more" data-date="10-25 21:25" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-25 21:25</span>
          <span class="news-item-title">r/opensource刚刚禁止了人工智能、非英语人士等</span>
          <span class="news-item-title-en">r/opensource just banned AI, non-English speakers, and more</span>
          <span class="news-value-point">💡 R/opensource的mod发布了新的提交规则，其中包括禁止使用人工智能的项目</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/nvidia-discusses-usd2-000-per-gpu-annual-software-fee-for-running-agents-on-ai-infrastructure-firm-already-charges-more-than-twice-that-amount-for-its-ai-enterprise-software-platform" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道，英伟达首席执行官黄延森（ Jensen Huang ）正在权衡企业AI的每个GPU约2,000美元的年度软件费用，如果售出500万个许可证，这一模式每年可以产生100亿美元的收入。定价和发布时间表仍未确认，" data-title="Nvidia discusses $2,000-per-GPU annual fee for software that &#39;runs agents on AI factories&#39;" data-date="10-25 21:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-25 21:00</span>
          <span class="news-item-title">英伟达讨论了“在人工智能工厂上运行代理”软件的每GPU年费$ 2,000</span>
          <span class="news-item-title-en">Nvidia discusses $2,000-per-GPU annual fee for software that 'runs agents on AI factories'</span>
          <span class="news-value-point">💡 据报道，英伟达首席执行官黄延森（ Jensen Huang ）正在权衡企业AI的每个GPU约2,000美元的年度软件费用，如果售出500万个许可…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/column/1017983/google-ai-search-online-publishing" target="_blank" rel="noopener" data-cat="keji" data-summary="The Stepback是一份每周时事通讯，详细介绍了科技界的一个重要故事。有关人工智能对网络影响的更多信息，请关注Emma Roth。Stepback将于美国东部时间周日上午8点到达订阅者的收件箱。选择加入The Stepback he" data-title="Google’s AI search changes upended online publishing" data-date="10-25 20:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-25 20:00</span>
          <span class="news-item-title">谷歌的人工智能搜索变革颠覆了在线发布</span>
          <span class="news-item-title-en">Google’s AI search changes upended online publishing</span>
          <span class="news-value-point">💡 The Stepback是一份每周时事通讯，详细介绍了科技界的一个重要故事</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1018205/blue-planet-iii-authentic-organic-ai" target="_blank" rel="noopener" data-cat="keji" data-summary="英国广播公司的蓝色星球III希望通过拍摄不那么完美的照片来证明其真实性。以前的自然系列的化身是由他们华丽，水晶般清晰的镜头定义的，这些镜头看起来几乎太好了，不可能是真实的。但" data-title="Blue Planet III is keeping the rough edges in the age of AI" data-date="10-25 05:29" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-25 05:29</span>
          <span class="news-item-title">蓝色星球III在人工智能时代保持着粗糙的边缘</span>
          <span class="news-item-title-en">Blue Planet III is keeping the rough edges in the age of AI</span>
          <span class="news-value-point">💡 英国广播公司的蓝色星球III希望通过拍摄不那么完美的照片来证明其真实性</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/24/the-ai-graveyard-a-running-list-of-projects-and-startups-that-didnt-make-it/" target="_blank" rel="noopener" data-cat="keji" data-summary="从苹果一再推迟Siri AI到OpenAI凌乱的“超级应用”发布，以下是关闭或未达到预期的人工智能项目。" data-title="The AI graveyard: a running list of projects and startups that didn’t make it" data-date="10-25 03:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-25 03:00</span>
          <span class="news-item-title">人工智能墓地：未成功完成的项目和初创公司的运行列表</span>
          <span class="news-item-title-en">The AI graveyard: a running list of projects and startups that didn’t make it</span>
          <span class="news-value-point">💡 从苹果一再推迟Siri AI到OpenAI凌乱的“超级应用”发布，以下是关闭或未达到预期的人工智能项目</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1018187/pennsylvania-ai-deceptive-advertising-act" target="_blank" rel="noopener" data-cat="keji" data-summary="周四，宾夕法尼亚州州长乔希·夏皮罗（ Josh Shapiro ）签署了《人工智能欺骗性广告法》（ Artificial Intelligence Deceptive Advertising Act ） ，要求披露人工智能生成的广告。法律要求任何广告-无论是静止图像，视频，音频还是文本- “" data-title="Pennsylvania will require labels on AI" data-date="10-25 02:32" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-25 02:32</span>
          <span class="news-item-title">宾夕法尼亚州将要求在人工智能上贴标签</span>
          <span class="news-item-title-en">Pennsylvania will require labels on AI</span>
          <span class="news-value-point">💡 周四，宾夕法尼亚州州长乔希·夏皮罗（ Josh Shapiro ）签署了《人工智能欺骗性广告法》（ Artificial Intelligenc…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/25/sunderland-v-leeds-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英超联赛现场更新从英国夏令时下午4:30开始欧洲对桑德兰的诅咒多于祝福报名参加足球每日1分钟窥视！当我们观看时，利兹在他们的黄色换衣带中从左到右开球。普罗科菲耶夫在体育场的单簧管上" data-title="Sunderland v Leeds: Premier League" data-date="10-26 00:37" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-26 00:37</span>
          <span class="news-item-title">桑德兰v利兹：英超联赛</span>
          <span class="news-item-title-en">Sunderland v Leeds: Premier League</span>
          <span class="news-value-point">💡 英超联赛现场更新从英国夏令时下午4:30开始欧洲对桑德兰的诅咒多于祝福报名参加足球每日1分钟窥视</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/25/manchester-united-v-bournemouth-liverpool-v-brighton-and-more-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="伯恩茅斯羞辱曼联将迈克尔·卡里克留在边缘，而利物浦击败布莱顿，纽卡斯尔赢得皇宫，赫尔与布伦特福德平局。否则，卡里克将与安德烈·桑托斯和卡洛斯·巴尔在中场争夺压舱物。" data-title="Manchester United 0-3 Bournemouth, Liverpool 2-0 Brighton and more: clockwatch – as it happened" data-date="10-26 00:32" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-26 00:32</span>
          <span class="news-item-title">曼联0-3伯恩茅斯，利物浦2-0布莱顿和更多：钟表–它发生了</span>
          <span class="news-item-title-en">Manchester United 0-3 Bournemouth, Liverpool 2-0 Brighton and more: clockwatch – as it happened</span>
          <span class="news-value-point">💡 伯恩茅斯羞辱曼联将迈克尔·卡里克留在边缘，而利物浦击败布莱顿，纽卡斯尔赢得皇宫，赫尔与布伦特福德平局</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/25/crystal-palace-newcastle-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="上半场是英超历史上最糟糕的45分钟之一。通过率虽然感觉较低，但只有微不足道的72.8%。只有两发子弹命中目标。太阳不停地从云层后面蹦出来，" data-title="Osula and Barnes’ second-half burst sees Newcastle pile pressure on lacklustre Palace" data-date="10-26 00:29" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-26 00:29</span>
          <span class="news-item-title">奥苏拉（ Osula ）和巴恩斯（ Barnes ）的下半场爆发看到纽卡斯尔（ Newcastle ）桩对平淡无奇的宫殿</span>
          <span class="news-item-title-en">Osula and Barnes’ second-half burst sees Newcastle pile pressure on lacklustre Palace</span>
          <span class="news-value-point">💡 上半场是英超历史上最糟糕的45分钟之一</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/25/manchester-united-bournemouth-premier-league-match-report-michael-carrick" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="根据迈克尔·卡里克（ Michael Carrick ）的说法，在布鲁诺·费尔南德斯（ Bruno Fernandes ）因“纯粹的足球”原因被淘汰后，曼联真的能答案，同样，是一个响亮的，羞辱性的否定，如果经理的工作仍然处于真正的危险之中" data-title="Michael Carrick on the brink after Manchester United are humiliated by Bournemouth" data-date="10-26 00:19" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-26 00:19</span>
          <span class="news-item-title">在曼联被伯恩茅斯羞辱后，迈克尔卡里克处于边缘</span>
          <span class="news-item-title-en">Michael Carrick on the brink after Manchester United are humiliated by Bournemouth</span>
          <span class="news-value-point">💡 根据迈克尔·卡里克（ Michael Carrick ）的说法，在布鲁诺·费尔南德斯（ Bruno Fernandes ）因“纯粹的足球”原因被…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/25/liverpool-brighton-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="布莱顿的强势跑步在安菲尔德被击败，因为利物浦在球场两端的胃口和紧迫感上升到第四位，这表明安东尼·伊拉奥拉（ Andoni Iraola ）的方法扎根了。这是利物浦，令人信服的本土优胜者" data-title="Isak applies finishing touch as Liverpool bring Brighton’s winning run to an end" data-date="10-26 00:12" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-26 00:12</span>
          <span class="news-item-title">伊萨克在利物浦结束布莱顿的胜利时进行了最后的润色</span>
          <span class="news-item-title-en">Isak applies finishing touch as Liverpool bring Brighton’s winning run to an end</span>
          <span class="news-value-point">💡 布莱顿的强势跑步在安菲尔德被击败，因为利物浦在球场两端的胃口和紧迫感上升到第四位，这表明安东尼·伊拉奥拉（ Andoni Iraola ）的方法…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13603616/manchester-united-michael-carrick-head-coach-on-brink-of-losing-job-after-bournemouth-defeat" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="根据加里·内维尔（ Gary Neville ）和杰米·卡拉格（ Jamie Carragher ）的说法，迈克尔·卡里克（ Michael Carrick ）在主场以3比0击败伯恩茅斯后，看起来有望失去曼联主教练" data-title="Neville fears Carrick on the brink as Carra calls for decision tonight" data-date="10-26 00:10" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-26 00:10</span>
          <span class="news-item-title">内维尔担心卡里克濒临灭绝，因为卡拉今晚呼吁做出决定</span>
          <span class="news-item-title-en">Neville fears Carrick on the brink as Carra calls for decision tonight</span>
          <span class="news-value-point">💡 根据加里·内维尔（ Gary Neville ）和杰米·卡拉格（ Jamie Carragher ）的说法，迈克尔·卡里克（ Michael C…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13603616/manchester-united-michael-carrick-head-coach-on-brink-of-losing-job-after-bournemouth-defeat" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="根据加里·内维尔（ Gary Neville ）和杰米·卡拉格（ Jamie Carragher ）的说法，迈克尔·卡里克（ Michael Carrick ）在主场以3比0击败伯恩茅斯后，看起来有望失去曼联主教练" data-title="Neville fears Carrick on the brink as Carra calls for decision tonight" data-date="10-26 00:10" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-26 00:10</span>
          <span class="news-item-title">内维尔担心卡里克濒临灭绝，因为卡拉今晚呼吁做出决定</span>
          <span class="news-item-title-en">Neville fears Carrick on the brink as Carra calls for decision tonight</span>
          <span class="news-value-point">💡 根据加里·内维尔（ Gary Neville ）和杰米·卡拉格（ Jamie Carragher ）的说法，迈克尔·卡里克（ Michael C…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/manchester-united-vs-bournemouth/report/559522" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）放弃了布鲁诺·费尔南德斯（ Bruno Fernandes ） ，只看到他的问题加剧，因为曼联在老特拉福德（ Old Trafford ）以3比0击败伯恩茅斯（ Bournem" data-title="Carrick drops Fernandes only to see Man Utd humbled by Bournemouth" data-date="10-26 00:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-26 00:00</span>
          <span class="news-item-title">卡里克放弃了费尔南德斯，却看到曼联在伯恩茅斯谦卑</span>
          <span class="news-item-title-en">Carrick drops Fernandes only to see Man Utd humbled by Bournemouth</span>
          <span class="news-value-point">💡 迈克尔·卡里克（ Michael Carrick ）放弃了布鲁诺·费尔南德斯（ Bruno Fernandes ） ，只看到他的问题加剧，因为曼…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/10/premier-league-top-scorers-2026-27-race-for-golden-boot" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="找出哪位英国顶尖射手正在向进球排行榜射击。继续阅读……" data-title="Premier League top scorers 2026-27: who is leading race for the golden boot?" data-date="10-25 23:56" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-25 23:56</span>
          <span class="news-item-title">2026-27赛季英超联赛最佳射手：谁是金靴赛的领跑者？</span>
          <span class="news-item-title-en">Premier League top scorers 2026-27: who is leading race for the golden boot?</span>
          <span class="news-value-point">💡 找出哪位英国顶尖射手正在向进球排行榜射击</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13603522/gary-neville-on-bruno-fernandes-and-michael-carrick-at-man-utd" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="加里·内维尔（ Gary Neville ）认为，在布鲁诺·费尔南德斯（ Bruno Fernandes ）公开“直接攻击”迈克尔·卡里克（ Michael Carrick ）之后，曼联的更衣室将是有毒的，并想知道闭门造车会说些什么。" data-title="&#39;Players have completely gone&#39; - Nev dissects &#39;toxic&#39; atmosphere at Man Utd" data-date="10-25 20:12" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-25 20:12</span>
          <span class="news-item-title">“玩家完全消失了” - NEV解剖曼联的“有毒”气氛</span>
          <span class="news-item-title-en">'Players have completely gone' - Nev dissects 'toxic' atmosphere at Man Utd</span>
          <span class="news-value-point">💡 加里·内维尔（ Gary Neville ）认为，在布鲁诺·费尔南德斯（ Bruno Fernandes ）公开“直接攻击”迈克尔·卡里克（ M…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13603513/bruno-fernandes-manchester-united-captain-dropped-for-crucial-premier-league-game-against-bournemouth" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="布鲁诺·费尔南德斯（ Bruno Fernandes ）因在主场对阵伯恩茅斯的英超联赛失利而被曼联队淘汰。" data-title="Fernandes dropped and an unused sub in Man Utd&#39;s heavy defeat" data-date="10-25 19:33" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-25 19:33</span>
          <span class="news-item-title">费尔南德斯和未使用的潜艇在曼联的沉重失败</span>
          <span class="news-item-title-en">Fernandes dropped and an unused sub in Man Utd's heavy defeat</span>
          <span class="news-value-point">💡 布鲁诺·费尔南德斯（ Bruno Fernandes ）因在主场对阵伯恩茅斯的英超联赛失利而被曼联队淘汰</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ck78p37y5508o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育专栏作家托尼·普利斯（ Tony Pulis ）解释了为什么布鲁诺·费尔南德斯（ Bruno Fernandes ）在曼联被科莫击败后的评论表明，目前管理俱乐部是多么困难。" data-title="What Man Utd need now is stability, not more changes" data-date="10-25 14:34" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-25 14:34</span>
          <span class="news-item-title">曼联现在需要的是稳定性，而不是更多的变化</span>
          <span class="news-item-title-en">What Man Utd need now is stability, not more changes</span>
          <span class="news-value-point">💡 英国广播公司体育专栏作家托尼·普利斯（ Tony Pulis ）解释了为什么布鲁诺·费尔南德斯（ Bruno Fernandes ）在曼联被科莫…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmy83vg66zngo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="随着曼联主教练迈克尔·卡里克（ Michael Carrick ）的压力越来越大，英国广播公司体育台（ BBC Sport ）关注英超联赛的“裁员赛季”何时开始。" data-title="When is Premier League &#39;sacking season&#39; - and who should be worried?" data-date="10-25 14:17" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-25 14:17</span>
          <span class="news-item-title">英超联赛的“裁员季”是什么时候？谁应该担心？</span>
          <span class="news-item-title-en">When is Premier League 'sacking season' - and who should be worried?</span>
          <span class="news-value-point">💡 随着曼联主教练迈克尔·卡里克（ Michael Carrick ）的压力越来越大，英国广播公司体育台（ BBC Sport ）关注英超联赛的“裁…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c9ly0dxxgp7lo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）表示，在伯恩茅斯周日访问老特拉福德时，他有可能有效地管理曼联。" data-title="Man Utd not an unmanageable club" data-date="10-25 05:34" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-25 05:34</span>
          <span class="news-item-title">曼联不是一个难以管理的俱乐部</span>
          <span class="news-item-title-en">Man Utd not an unmanageable club</span>
          <span class="news-value-point">💡 迈克尔·卡里克（ Michael Carrick ）表示，在伯恩茅斯周日访问老特拉福德时，他有可能有效地管理曼联</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqev38dz34vxo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="托特纳姆热刺在周六的英超联赛中排名第12 ，这是他们自1月2日以来的最高联赛位置。他们终于要回来了？" data-title="The candid meeting that &#39;changed&#39; Spurs - are they finally on way back?" data-date="10-25 05:14" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-25 05:14</span>
          <span class="news-item-title">“改变”马刺的坦率会议-他们终于回来了吗？</span>
          <span class="news-item-title-en">The candid meeting that 'changed' Spurs - are they finally on way back?</span>
          <span class="news-value-point">💡 托特纳姆热刺在周六的英超联赛中排名第12 ，这是他们自1月2日以来的最高联赛位置</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/darts/live-blog/12040/13603407/european-championship-darts-commentary-updates-scores-analysis-with-luke-littler-in-finals-day-in-dortmund" target="_blank" rel="noopener" data-cat="zonghe" data-summary="&#39;It was my chance and I took it!&#39; - Ratajski savours shock Littler win" data-title="&#39;It was my chance and I took it!&#39; - Ratajski savours shock Littler win" data-date="10-26 00:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-26 00:00</span>
          <span class="news-item-title">（这是我的机会，我抓住了！ '- Ratajski品尝震撼Littler的胜利</span>
          <span class="news-item-title-en">'It was my chance and I took it!' - Ratajski savours shock Littler win</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/719.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 25 日消息，猫眼专业版数据显示，《三星堆：未来往事》电影票房已达到 116.2 万。据IT之家了解，《三星堆：未来往事》是国内首部获得国家电影局公映许可证的 AI 全流程院线长片，上映于 10 月 23 日。本片片长 100 分钟，所有角色均为原创数字形象，不含对真实演员的数字复制。同时，本片故事设定在未来人类将一切决策交给算法而引发全球危机，破解困局的线索指向三星堆七个古老刻符，形成“答案在过去，危机在未来”的叙事结构。这部影片的制作方式决定了它“首部”标签的实质含义。全片依托博纳自研的“博卡电影云片场”完成，创作团队历时两年，产出 120 余万张底图，完成上百次全片迭代。据官方介绍，AI 主要承担生成与执行，创意构思、剧本、镜头设计与审美判断由博纳 AIGMS 团队" data-title="国内首部 AI 院线长片《三星堆：未来往事》，票房过百万" data-date="10-25 23:36" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-25 23:36</span>
          <span class="news-item-title">国内首部 AI 院线长片《三星堆：未来往事》，票房过百万</span>
          <span class="news-value-point">💡 IT之家 10 月 25 日消息，猫眼专业版数据显示，《三星堆：未来往事》电影票房已达到 116.2 万</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/peripherals/mechanical-keyboards/iqunix-mq80-low-profile-mechanical-keyboard-review" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IQUNIX MQ80做工精良，超级时尚，但它不像以前那么畅销。如果您不喜欢磁性开关，请抓住这个，否则等待促销。" data-title="IQUNIX MQ80 low profile mechanical keyboard review" data-date="10-25 23:08" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-25 23:08</span>
          <span class="news-item-title">IQUNIX MQ80低调机械键盘评测</span>
          <span class="news-item-title-en">IQUNIX MQ80 low profile mechanical keyboard review</span>
          <span class="news-value-point">💡 IQUNIX MQ80做工精良，超级时尚，但它不像以前那么畅销</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/sunderland-vs-leeds-united/live/559523" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Sunderland vs Leeds LIVE!" data-title="Sunderland vs Leeds LIVE!" data-date="10-25 23:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-25 23:00</span>
          <span class="news-item-title">桑德兰vs利兹现场直播！</span>
          <span class="news-item-title-en">Sunderland vs Leeds LIVE!</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/716.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 25 日消息，国产武侠游戏《影之刃零》今晚宣布将于 10 月 27 日 10:00 开启预下载，并公布官方配置要求。官方提醒，为保障良好的游戏体验，请将游戏安装在固态硬盘 (SSD) 中；游戏本体约 145G，由于预下载机制，请预留至少 300G 可用磁盘空间；请务必将显卡驱动更新至最新版本。IT之家注意到，《影之刃零》将于 10 月 29 日 10 点正式解锁，登陆 PS5 与 PC 平台，国区数字标准版售价 268 元，数字豪华版售价 328 元。PS5 实体光碟将于 2027 年推出。《影之刃零》由灵游坊自主研发发行，采用虚幻引擎 5 打造，定位黑暗武侠题材第三人称动作冒险与单机动作 RPG，把中国武术与蒸汽朋克融合为功夫朋克风格，美术深沉黑暗，主打快节奏高速战斗。" data-title="国产武侠游戏《影之刃零》10 月 27 日 10:00 开启预下载，游戏本体约 145G" data-date="10-25 22:53" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-25 22:53</span>
          <span class="news-item-title">国产武侠游戏《影之刃零》10 月 27 日 10:00 开启预下载，游戏本体约 145G</span>
          <span class="news-value-point">💡 IT之家 10 月 25 日消息，国产武侠游戏《影之刃零》今晚宣布将于 10 月 27 日 10:00 开启预下载，并公布官方配置要求</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/715.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 25 日消息，开源智能家居平台 Home Assistant 现已在最新测试版安装程序 0.0.0-alpha.4 中，新增 x86-64 架构的 Live USB 安装选项。未来该功能实装后，有望简化迷你主机安装 Home Assistant OS 的流程。IT之家了解到，Home Assistant OS 目前已经支持 x86-64 硬件，但现有安装流程要求用户先制作启动盘，再将系统镜像写入到目标磁盘。而 Live USB 则是可以将系统直接运行在 U 盘上，不需要安装到电脑硬盘。同时，本次更新还为 Live USB 带来了全屏界面，并新增校验功能，可验证系统镜像完整性。其他改进还包括更清晰地显示硬盘信息，以及在擦除存储设备之前显示更明确的警告。不过，上述改进目前还处" data-title="Home Assistant 将新增 Live USB 安装选项，利好迷你主机用户" data-date="10-25 22:52" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-25 22:52</span>
          <span class="news-item-title">Home Assistant 将新增 Live USB 安装选项，利好迷你主机用户</span>
          <span class="news-value-point">💡 IT之家 10 月 25 日消息，开源智能家居平台 Home Assistant 现已在最新测试版安装程序 0.0.0-alpha.4 中，新增…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/714.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 25 日消息，彭博社记者马克・古尔曼发文，透露今年早些时候，苹果对硬件工程和硬件技术部门进行了大规模调整，将团队交由新任首席硬件官 Johny Srouji 负责。此外，苹果两名资深显示技术高管 Wei Chen 和 John Zhong 在公司工作约 30 年后，正逐步转向规模更小、偏顾问性质的岗位。这一安排被视为两人未来退休前的过渡步骤。多年来接受两人指导的 Victor Yin，目前已经负责公司相当一部分屏幕相关工作。苹果还按照每年 10 月通常进行的晋升安排，任命 Rajesh Ambati、Louie Sanguinetti 和 Derek Shaeffer 为工程领域的新任副总裁。三人的工作主要涉及帮助苹果设备连接互联网的软件或硬件技术。其中，Sanguine" data-title="苹果硬件技术部门再迎人事调整：两名显示技术高管退休临近，转任顾问角色" data-date="10-25 22:52" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-25 22:52</span>
          <span class="news-item-title">苹果硬件技术部门再迎人事调整：两名显示技术高管退休临近，转任顾问角色</span>
          <span class="news-value-point">💡 IT之家 10 月 25 日消息，彭博社记者马克・古尔曼发文，透露今年早些时候，苹果对硬件工程和硬件技术部门进行了大规模调整，将团队交由新任首席…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/713.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 25 日消息，彭博社记者马克・古尔曼发文，透露苹果正在为 iPhone Duo 开发新的“便捷访问”（Reachability）模式，可以将外屏“主要内容”移动至左侧或右侧，方便用户根据自己的持机习惯调整界面。IT之家获悉，此前有不少用户吐槽左撇子用户难以操作 iPhone Duo，不过古尔曼指出，相关担忧可能被夸大。一些左撇子用户表示，外屏交互逻辑并未对他们的日常使用造成太大影响。至于内屏，由于用户经常需要双手操作，左右手习惯的差异也不那么明显。行业研究机构 IDC 此前预计，苹果首款折叠屏 iPhone 首年出货量将超过 1000 万部，并可能在 2027 年拿下全球折叠屏手机市场约 40% 的份额。高盛则维持对 iPhone Duo 的乐观判断，预计其 2026 年" data-title="古尔曼：苹果正为 iPhone Duo 开发全新“便捷访问”模式，方便左撇子用户根据持机习惯调整界面" data-date="10-25 22:46" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-25 22:46</span>
          <span class="news-item-title">古尔曼：苹果正为 iPhone Duo 开发全新“便捷访问”模式，方便左撇子用户根据持机习惯调整界面</span>
          <span class="news-value-point">💡 IT之家 10 月 25 日消息，彭博社记者马克・古尔曼发文，透露苹果正在为 iPhone Duo 开发新的“便捷访问”（Reachabilit…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/712.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 25 日消息，彭博社记者马克・古尔曼发文，透露苹果 Apple Store 零售门店近年来面临一种棘手问题：部分顾客购买 iPhone 或其他产品后，会将包装盒里的设备拿走，再利用配重块调整包装重量，之后将其后封伪装成“未开封”产品进行退款。为了应对这一问题，苹果曾要求零售店员工仔细检查退货商品，即使包装看起来没有被动过的痕迹，也需要员工亲自打开包装确认设备是否完整。但在大多数正常退货案例中，消费者并没有恶意，这一流程却会造成额外的库存损耗。如今，苹果开发了一种新的检测设备，可以扫描包装内的 iPhone 并运行诊断程序，确认设备是否完整，同时保持包装密封，使商品能够重新进入库存。该设备采用了苹果 Presto 设备所使用的相关技术。Presto 此前主要用于在不拆开包装" data-title="遏制退货欺诈：苹果开发新型检测设备，可帮助 Apple Store 员工扫描密封包装盒内 iPhone 完整性" data-date="10-25 22:43" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-25 22:43</span>
          <span class="news-item-title">遏制退货欺诈：苹果开发新型检测设备，可帮助 Apple Store 员工扫描密封包装盒内 iPhone 完整性</span>
          <span class="news-value-point">💡 IT之家 10 月 25 日消息，彭博社记者马克・古尔曼发文，透露苹果 Apple Store 零售门店近年来面临一种棘手问题：部分顾客购买 i…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/711.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 25 日消息，彭博社记者马克・古尔曼发文，透露苹果首款触屏 MacBook Pro 即将于北京时间 10 月 29 日凌晨 1 点正式亮相。这款产品不仅将为 Mac 产品线引入触控操作，还将采用 OLED 屏幕和全新的交互界面，成为苹果近年来产品策略转变的又一例证。苹果高管过去曾多次在相关产品正式推出前否认公司有意进入某些市场。无论是智能手机、平板电脑，还是近年来的低价笔记本、折叠屏手机和智能家居显示设备，苹果最终都陆续推出了相应产品。但与这些品类不同，触屏笔记本长期以来一直是苹果明确表示不看好的方向。事实上，乔布斯曾将触屏笔记本形容为“在人体工程学上糟糕透顶”的设计。蒂姆 · 库克出任 CEO 后，也曾将平板电脑与 PC 融合比作“把烤面包机和冰箱合二为一”。前营销主管" data-title="古尔曼：苹果首款触屏 MacBook Pro 北京时间 10 月 29 日发布，标志公司产品策略迎来重大转变" data-date="10-25 22:37" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-25 22:37</span>
          <span class="news-item-title">古尔曼：苹果首款触屏 MacBook Pro 北京时间 10 月 29 日发布，标志公司产品策略迎来重大转变</span>
          <span class="news-value-point">💡 IT之家 10 月 25 日消息，彭博社记者马克・古尔曼发文，透露苹果首款触屏 MacBook Pro 即将于北京时间 10 月 29 日凌晨 …</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-25/10720856.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="10月25日20时，经过连续8小时奋战，西藏那曲巴青县玛如乡二村受灾群众安置点活动板房顺利通电。" data-title="西藏那曲巴青7.0级地震震区玛如乡二村受灾群众安置点活动板房顺利通电" data-date="10-25 22:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 22:16</span>
          <span class="news-item-title">西藏那曲巴青7.0级地震震区玛如乡二村受灾群众安置点活动板房顺利通电</span>
          <span class="news-value-point">💡 10月25日20时，经过连续8小时奋战，西藏那曲巴青县玛如乡二村受灾群众安置点活动板房顺利通电</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/25/the-hottest-ai-wearables-and-gadgets-you-should-know-about/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="我们编制了所有最热门的AI可穿戴设备列表，包括Muse Charm、Bee、Friend、Plaud等。" data-title="The hottest AI wearables and gadgets you should know about" data-date="10-25 22:10" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-25 22:10</span>
          <span class="news-item-title">您应该了解的最热门的AI可穿戴设备和小工具</span>
          <span class="news-item-title-en">The hottest AI wearables and gadgets you should know about</span>
          <span class="news-value-point">💡 我们编制了所有最热门的AI可穿戴设备列表，包括Muse Charm、Bee、Friend、Plaud等</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/ssds/samsungs-new-2tb-990-ssd-is-38-percent-off-at-amazon-today-get-usd200-off-this-pcie-4-0-all-rounder-drive-for-a-limited-time" target="_blank" rel="noopener" data-cat="zonghe" data-summary="全新Samsung 990 2TB固态硬盘立减38% ，节省$ 200。" data-title="Samsung&#39;s new 2TB 990 SSD is 38% off at Amazon today" data-date="10-25 21:43" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-25 21:43</span>
          <span class="news-item-title">三星的新款2TB 990固态硬盘今天在亚马逊上可享38%的折扣</span>
          <span class="news-item-title-en">Samsung's new 2TB 990 SSD is 38% off at Amazon today</span>
          <span class="news-value-point">💡 全新Samsung 990 2TB固态硬盘立减38% ，节省$ 200</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/24/us/politics/trump-netanyahu-iran-new-phase-of-war.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="随着新的情报和各方寻找行动借口的可能性，伊朗的战争正进入美国和以色列选举前的危险阶段。" data-title="A New Level of Threat and Fear Risks Pushing the U.S. and Iran Back to Full War" data-date="10-25 21:38" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-25 21:38</span>
          <span class="news-item-title">新的威胁和恐惧风险将美国和伊朗推回全面战争</span>
          <span class="news-item-title-en">A New Level of Threat and Fear Risks Pushing the U.S. and Iran Back to Full War</span>
          <span class="news-value-point">💡 随着新的情报和各方寻找行动借口的可能性，伊朗的战争正进入美国和以色列选举前的危险阶段</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-25/10720843.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网福州10月25日电 (郑江洛)25日，“新媒传情·华裳漆韵”新媒体技能培训与非遗交流体验活动在福州举行，30名在榕高校台青代表相聚于此，在技艺学习与沉浸式体验中，共品闽都文化魅力，缔结两岸青年情谊。" data-title="在榕台青于非遗与新媒体碰撞中感悟闽都文脉" data-date="10-25 21:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-25 21:13</span>
          <span class="news-item-title">在榕台青于非遗与新媒体碰撞中感悟闽都文脉</span>
          <span class="news-value-point">💡 中新网福州10月25日电 (郑江洛)25日，“新媒传情·华裳漆韵”新媒体技能培训与非遗交流体验活动在福州举行，30名在榕高校台青代表相聚于此，在…</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-26 00:37（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
