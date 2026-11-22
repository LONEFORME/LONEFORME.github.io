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
      <span>2026-11-22 16:56 抓取更新</span>
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
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('keji', this)">
        <span>🤖 AI模型 & 芯片算力</span>
        <span class="channel-count">11</span>
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
  <div class="ov-item"><span class="ov-num">56</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">4</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×18 · BBC×8</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">按来源聚合 · 最近 24 小时精选</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gj/2026/11-22/10736067.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网金边11月22日电 (张堰林 杨强)柬埔寨卫生部当地时间22日发布通报称，该国近日发现1例猴痘确诊病例，目前患者正在医院接受治疗。" data-title="柬埔寨时隔两年多再现猴痘确诊病例" data-date="11-22 16:13" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 11-22 16:13</span>
      </div>
      <h2 class="hero-featured-title">柬埔寨时隔两年多再现猴痘确诊病例</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.nytimes.com/2026/11/21/world/asia/china-nvidia-spy-chips-state-security.html" target="_blank" rel="noopener" data-cat="keji" data-summary="官员们表示，中国的间谍机构一直在开展一项秘密行动，以帮助该国的公司获取先进的人工智能芯片，并收集该领域的情报。" data-title="China’s Spies Set Sights on A.I. Chips Years Before Nvidia Scandal" data-date="11-22 12:28" data-source="纽约时报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
      </div>
      <p class="hero-sub-title">早在英伟达丑闻发生数年前，中国间谍就已将目光瞄准人工智能芯片</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/football/news/11661/13614990/bruno-fernandes-man-utd-captain-confirms-contract-offer-but-says-negotiations-are-on-hold" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="布鲁诺·费尔南德斯在接受天空体育独家采访时表示，曼联已向他提供了一份新合同，但他已暂停谈判，因为他坚持认为俱乐部的首要任务必须是重返胜利轨道。" data-title="Fernandes: Man Utd have offered new deal but now is not time for talks" data-date="11-22 15:00" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">费尔南德斯：曼联已提出新合同，但现在不是谈判的时候</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/11-22/10736094.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网黑河11月22日电 (王琳 胡心玥)黑河红河谷国际滑雪场于22日开板迎客，作为该市唯一SSS级滑雪场，经过全方位升级改造，以全新设施、多元业态，为广大游客营造高品质冰雪游玩体验。" data-title="黑河红河谷国际滑雪场开板迎客" data-date="11-22 16:44" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">黑河红河谷国际滑雪场开板迎客</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-22/10736067.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网金边11月22日电 (张堰林 杨强)柬埔寨卫生部当地时间22日发布通报称，该国近日发现1例猴痘确诊病例，目前患者正在医院接受治疗。" data-title="柬埔寨时隔两年多再现猴痘确诊病例" data-date="11-22 16:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-22 16:13</span>
          <span class="news-item-title">柬埔寨时隔两年多再现猴痘确诊病例</span>
          <span class="news-value-point">💡 中新网金边11月22日电 (张堰林 杨强)柬埔寨卫生部当地时间22日发布通报称，该国近日发现1例猴痘确诊病例，目前患者正在医院接受治疗</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-22/10736082.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月22日电 综合报道，在从中国深圳返回美国后，美国总统特朗普在过去数小时内，在其社交平台“真实社交”(Truth Social)上，连发30多张APEC会议相关照片。" data-title="特朗普连发30多张照片盛赞APEC会议，照片配文“GOAT”（有史以来最伟大的）" data-date="11-22 16:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-22 16:11</span>
          <span class="news-item-title">特朗普连发30多张照片盛赞APEC会议，照片配文“GOAT”（有史以来最伟大的）</span>
          <span class="news-value-point">💡 中新网11月22日电 综合报道，在从中国深圳返回美国后，美国总统特朗普在过去数小时内，在其社交平台“真实社交”(Truth Social)上，连…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-22/10736077.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月22日电 中国外交部发言人22日宣布：应中共中央政治局委员、外交部长王毅邀请，瑞士联邦副主席兼外长卡西斯将于11月23日至24日访华并举行中瑞第五轮外长级战略对话。(完)" data-title="瑞士联邦副主席兼外长卡西斯将访华" data-date="11-22 15:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-22 15:49</span>
          <span class="news-item-title">瑞士联邦副主席兼外长卡西斯将访华</span>
          <span class="news-value-point">💡 中新社北京11月22日电 中国外交部发言人22日宣布：应中共中央政治局委员、外交部长王毅邀请，瑞士联邦副主席兼外长卡西斯将于11月23日至24日…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-22/10736053.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网曼谷11月22日电 (李映民 梁峻祥 王茜)古老佛塔静静矗立，斑驳砖墙诉说历史，树根环抱的佛像头像引人驻足……11月22日，记者随泰国国家旅游局工作人员走进泰国大城府，探访历史遗迹、体验传统美食、感受地方文化，领略这座千年古都独特的旅游魅力。" data-title="泰国大城府：千年古都展现历史文化魅力" data-date="11-22 15:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-22 15:35</span>
          <span class="news-item-title">泰国大城府：千年古都展现历史文化魅力</span>
          <span class="news-value-point">💡 中新网曼谷11月22日电 (李映民 梁峻祥 王茜)古老佛塔静静矗立，斑驳砖墙诉说历史，树根环抱的佛像头像引人驻足……11月22日，记者随泰国国家…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-22/10736069.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月22日电 综合印度媒体报道，11月21日，印度总理莫迪在公开讲话中表示，民众响应了其避免购买黄金的号召，这帮助降低了黄金价格。" data-title="莫迪：“印度民众响应我的号召，帮助降低了黄金价格”" data-date="11-22 15:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-22 15:34</span>
          <span class="news-item-title">莫迪：“印度民众响应我的号召，帮助降低了黄金价格”</span>
          <span class="news-value-point">💡 中新网11月22日电 综合印度媒体报道，11月21日，印度总理莫迪在公开讲话中表示，民众响应了其避免购买黄金的号召，这帮助降低了黄金价格</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-22/10736064.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="外交部发言人宣布：" data-title="瑞士联邦副主席兼外长卡西斯将访华" data-date="11-22 15:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-22 15:07</span>
          <span class="news-item-title">瑞士联邦副主席兼外长卡西斯将访华</span>
          <span class="news-value-point">💡 外交部发言人宣布：</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-22/10736048.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月22日电 中国外交部发言人22日宣布：中共中央政治局委员、中央政法委书记陈文清将于11月22日至28日赴德国出席第六次中德高级别安全对话并访问德国、奥地利。(完)" data-title="陈文清将赴德国出席第六次中德高级别安全对话并访问德国、奥地利" data-date="11-22 14:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-22 14:30</span>
          <span class="news-item-title">陈文清将赴德国出席第六次中德高级别安全对话并访问德国、奥地利</span>
          <span class="news-value-point">💡 中新社北京11月22日电 中国外交部发言人22日宣布：中共中央政治局委员、中央政法委书记陈文清将于11月22日至28日赴德国出席第六次中德高级别…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-22/10736034.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月22日电 题：历史性会晤里的历史与未来" data-title="【和合共生】习言道｜历史性会晤里的历史与未来" data-date="11-22 14:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-22 14:02</span>
          <span class="news-item-title">【和合共生】习言道｜历史性会晤里的历史与未来</span>
          <span class="news-value-point">💡 中新网11月22日电 题：历史性会晤里的历史与未来</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-22/10736036.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月22日电 据韩联社报道，韩国总统李在明22日受理教育部长官崔教振提交的辞呈。" data-title="韩国总统李在明受理教育部长官崔教振辞呈" data-date="11-22 13:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-22 13:42</span>
          <span class="news-item-title">韩国总统李在明受理教育部长官崔教振辞呈</span>
          <span class="news-value-point">💡 中新网11月22日电 据韩联社报道，韩国总统李在明22日受理教育部长官崔教振提交的辞呈</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-22/10736022.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月22日电 中国官方22日通报，中国石油天然气集团有限公司党组成员、副总经理谢军涉嫌严重违纪违法，目前正接受中央纪委国家监委纪律审查和监察调查。" data-title="中国石油天然气集团有限公司副总经理谢军被查" data-date="11-22 13:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-22 13:24</span>
          <span class="news-item-title">中国石油天然气集团有限公司副总经理谢军被查</span>
          <span class="news-value-point">💡 中新社北京11月22日电 中国官方22日通报，中国石油天然气集团有限公司党组成员、副总经理谢军涉嫌严重违纪违法，目前正接受中央纪委国家监委纪律审…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-22/10736011.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="蓝厅观察丨APEC“中国年” 亚太合作启新航" data-title="APEC“中国年” 亚太合作启新航" data-date="11-22 12:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-22 12:28</span>
          <span class="news-item-title">APEC“中国年” 亚太合作启新航</span>
          <span class="news-value-point">💡 蓝厅观察丨APEC“中国年” 亚太合作启新航</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-22/10735990.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网曼谷11月22日电(李映民 王茜 梁峻祥)古老佛塔在灯光映照下熠熠生辉，五彩水灯点亮水面，传统舞蹈与烟花表演交相辉映。当地时间21日晚，泰国2026年“水之色彩”水灯节庆典在泰国大城府举行，通过传统祈福仪式、文化演出和现代光影展示，为这座历史古都增添浓厚节日氛围。" data-title="泰国大城府水灯节璀璨上演 古都历史遗址焕发节庆魅力" data-date="11-22 11:51" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-22 11:51</span>
          <span class="news-item-title">泰国大城府水灯节璀璨上演 古都历史遗址焕发节庆魅力</span>
          <span class="news-value-point">💡 中新网曼谷11月22日电(李映民 王茜 梁峻祥)古老佛塔在灯光映照下熠熠生辉，五彩水灯点亮水面，传统舞蹈与烟花表演交相辉映</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cq702kdw845ro/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="周四美国、中国和俄罗斯领导人的会晤将为普京（普丁）提供一个重要的舞台——但这并不会让他离赢得乌克兰战争更近一步。" data-title="分析：APEC上与习近平、特朗普历史性会晤，对普京是一场重大胜利" data-date="11-22 11:46" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-22 11:46</span>
          <span class="news-item-title">分析：APEC上与习近平、特朗普历史性会晤，对普京是一场重大胜利</span>
          <span class="news-value-point">💡 周四美国、中国和俄罗斯领导人的会晤将为普京（普丁）提供一个重要的舞台——但这并不会让他离赢得乌克兰战争更近一步</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/21/us/politics/trump-congressional-oversight-contractors.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="总统的行政命令是削弱民主党调查政府行为计划的最新举措。" data-title="Trump Moves to Restrict Congressional Oversight of Contractors" data-date="11-22 09:29" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-22 09:29</span>
          <span class="news-item-title">特朗普采取行动限制国会对承包商的监督</span>
          <span class="news-item-title-en">Trump Moves to Restrict Congressional Oversight of Contractors</span>
          <span class="news-value-point">💡 总统的行政命令是削弱民主党调查政府行为计划的最新举措</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/trump-wants-to-ban-us-companies-from-building-overseas-data-centers-as-bans-slow-development-also-considers-putting-a-tremendous-tax-in-lieu-of-prohibition" target="_blank" rel="noopener" data-cat="shizheng" data-summary="总统希望美国的数据中心公司留在美国境内，如果它们想在国外建数据中心，则需要支付高额费用。" data-title="Trump wants to ban US companies from building overseas data centers as bans slow development" data-date="11-22 00:29" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-22 00:29</span>
          <span class="news-item-title">特朗普希望禁止美国公司在海外建设数据中心，因为禁令会拖慢发展速度</span>
          <span class="news-item-title-en">Trump wants to ban US companies from building overseas data centers as bans slow development</span>
          <span class="news-value-point">💡 总统希望美国的数据中心公司留在美国境内，如果它们想在国外建数据中心，则需要支付高额费用</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">11 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/11/21/world/asia/china-nvidia-spy-chips-state-security.html" target="_blank" rel="noopener" data-cat="keji" data-summary="官员们表示，中国的间谍机构一直在开展一项秘密行动，以帮助该国的公司获取先进的人工智能芯片，并收集该领域的情报。" data-title="China’s Spies Set Sights on A.I. Chips Years Before Nvidia Scandal" data-date="11-22 12:28" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-22 12:28</span>
          <span class="news-item-title">早在英伟达丑闻发生数年前，中国间谍就已将目光瞄准人工智能芯片</span>
          <span class="news-item-title-en">China’s Spies Set Sights on A.I. Chips Years Before Nvidia Scandal</span>
          <span class="news-value-point">💡 官员们表示，中国的间谍机构一直在开展一项秘密行动，以帮助该国的公司获取先进的人工智能芯片，并收集该领域的情报</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/21/a-tale-of-two-nvidias/" target="_blank" rel="noopener" data-cat="keji" data-summary="我们看到了有关英伟达的两种截然不同的景象——该公司最新的财报，以及科技高管们大声疾呼黄仁勋回归。" data-title="A tale of two Nvidias" data-date="11-22 05:07" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-22 05:07</span>
          <span class="news-item-title">两个英伟达的故事</span>
          <span class="news-item-title-en">A tale of two Nvidias</span>
          <span class="news-value-point">💡 我们看到了有关英伟达的两种截然不同的景象——该公司最新的财报，以及科技高管们大声疾呼黄仁勋回归</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/cpus/act-fast-to-score-intels-core-i7-14700k-for-its-lowest-price-ever-at-usd249-99-raptor-lake-refresh-cpu-is-a-bargain-that-supports-ddr5-and-ddr4-motherboards" target="_blank" rel="noopener" data-cat="keji" data-summary="经过数月的价格波动，英特尔酷睿 i7-14700K 的价格降至历史最低的 249.99 美元，该处理器支持 LGA 1700 主板，主板可支持 DDR4 或 DDR5 内存。" data-title="Act fast to score Intel&#39;s Core i7-14700K for its lowest price ever at $249.99" data-date="11-22 04:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-22 04:00</span>
          <span class="news-item-title">抓紧行动，以有史以来最低的249.99美元价格拿下英特尔酷睿i7-14700K</span>
          <span class="news-item-title-en">Act fast to score Intel's Core i7-14700K for its lowest price ever at $249.99</span>
          <span class="news-value-point">💡 经过数月的价格波动，英特尔酷睿 i7-14700K 的价格降至历史最低的 249.99 美元，该处理器支持 LGA 1700 主板，主板可支持 …</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/21/us/politics/tech-outages-ai-disruptions.html" target="_blank" rel="noopener" data-cat="keji" data-summary="自互联网诞生之初，网络安全就一直被忽视。如今，人工智能正在揭示潜藏的问题，使几十年来易受攻击的代码终于要付出代价。" data-title="Tech Outages Are Only the Beginning. A.I. Will Bring More Disruptions." data-date="11-22 03:11" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-22 03:11</span>
          <span class="news-item-title">技术中断只是一个开始。人工智能将带来更多颠覆。</span>
          <span class="news-item-title-en">Tech Outages Are Only the Beginning. A.I. Will Bring More Disruptions.</span>
          <span class="news-value-point">💡 自互联网诞生之初，网络安全就一直被忽视</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/21/all-the-ai-agents-that-can-live-in-your-text-messages/" target="_blank" rel="noopener" data-cat="keji" data-summary="我们创建了一个列表，列出了可以在短信中出现的最著名的人工智能客服代表，从一般助理到专为家庭、旅行和工作而设计的客服代表。" data-title="Here are the top AI agents that can live in your text messages" data-date="11-22 01:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-22 01:00</span>
          <span class="news-item-title">以下是可以存在于您的短信中的顶级AI代理</span>
          <span class="news-item-title-en">Here are the top AI agents that can live in your text messages</span>
          <span class="news-value-point">💡 我们创建了一个列表，列出了可以在短信中出现的最著名的人工智能客服代表，从一般助理到专为家庭、旅行和工作而设计的客服代表</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/supercomputers/this-week-on-toms-hardware-premium-21-november-2026-amd-nvidia-and-more-show-off-the-future-of-high-performance-computing-at-sc26" target="_blank" rel="noopener" data-cat="keji" data-summary="我们将详细介绍我们在SC26上涵盖的所有内容，其中包括AMD、Nvidia、Intel等公司的全新设备和最新动态。" data-title="This week on Tom&#39;s Hardware Premium: 21 November 2026" data-date="11-22 00:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-22 00:00</span>
          <span class="news-item-title">本周Tom's Hardware Premium：2026年11月21日</span>
          <span class="news-item-title-en">This week on Tom's Hardware Premium: 21 November 2026</span>
          <span class="news-value-point">💡 我们将详细介绍我们在SC26上涵盖的所有内容，其中包括AMD、Nvidia、Intel等公司的全新设备和最新动态</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/rapidus-reportedly-struggles-to-produce-working-sram-on-its-2nm-node-putting-2027-mass-production-at-risk-company-faces-significant-challenges-using-euv-to-develop-gaa-transistors" target="_blank" rel="noopener" data-cat="keji" data-summary="日本的半导体初创公司已经展示了GAA晶体管的运作情况，但要将它们集成到工作内存单元中似乎是一项更为艰巨的挑战。" data-title="Rapidus reportedly struggles to produce working SRAM on its 2nm node, putting 2027 mass production at risk" data-date="11-21 23:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-21 23:30</span>
          <span class="news-item-title">据报道，Rapidus 在其 2 纳米工艺节点上生产可正常工作的 SRAM 存在困难，这使 2027 年的量产计划面临风险。</span>
          <span class="news-item-title-en">Rapidus reportedly struggles to produce working SRAM on its 2nm node, putting 2027 mass production at risk</span>
          <span class="news-value-point">💡 日本的半导体初创公司已经展示了GAA晶体管的运作情况，但要将它们集成到工作内存单元中似乎是一项更为艰巨的挑战</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/35-year-old-snes-runs-chatgpt-accelerated-with-a-super-fx-2-chip-21-mhz-of-risc-muscle-speeds-2-2m-parameter-chatbot-replies" target="_blank" rel="noopener" data-cat="keji" data-summary="任天堂的经典 SNES 游戏机现在有了自己的 ChatGPT 客户端，并由 Super FX 2 芯片提供加速。" data-title="35-year-old SNES runs ChatGPT, accelerated with a Super FX 2 chip — 21 MHz of RISC muscle speeds 2.2M parameter chatbot replies" data-date="11-21 23:02" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-21 23:02</span>
          <span class="news-item-title">35岁的SNES运行ChatGPT，由Super FX 2芯片加速——21 MHz的RISC性能可加速220万参数的聊天机器人回复</span>
          <span class="news-item-title-en">35-year-old SNES runs ChatGPT, accelerated with a Super FX 2 chip — 21 MHz of RISC muscle speeds 2.2M parameter chatbot replies</span>
          <span class="news-value-point">💡 任天堂的经典 SNES 游戏机现在有了自己的 ChatGPT 客户端，并由 Super FX 2 芯片提供加速</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/podcast/1038701/anthropic-ipo-ai-safety-openai-nvidia-structure" target="_blank" rel="noopener" data-cat="keji" data-summary="今天，我将与《The Verge》的高级人工智能记者Hayden Field就Anthropic的IPO进行探讨，这是我们关于人工智能在现实生活中的系列节目的第三期，也是最后一期。Claude背后的这家人工智能实验室于上周四在纳斯达克上市。这些数字非常庞大。" data-title="Can Anthropic afford to put safety first?" data-date="11-21 23:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-21 23:00</span>
          <span class="news-item-title">Anthropic 是否有能力将安全放在首位？</span>
          <span class="news-item-title-en">Can Anthropic afford to put safety first?</span>
          <span class="news-value-point">💡 今天，我将与《The Verge》的高级人工智能记者Hayden Field就Anthropic的IPO进行探讨，这是我们关于人工智能在现实生活…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/506.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 21 日消息，据路透社报道，当地时间 21 日，韩国总统李在明前往韩国东南部城市蔚山，视察当地一座在建数据中心，并敦促韩国加快在全球 AI 竞赛中的步伐。“全世界都在竞相角逐，速度至关重要。”数据中心是芯片需求的重要来源。李在明希望，SK 建设的蔚山项目能够取得成功，进而吸引全球 AI 企业加大投资。蔚山数据中心由 SK 集团与亚马逊云科技共同开发。韩国科学技术信息通信部去年公布的估算显示，项目到 2029 年的总投资额预计为 7 万亿韩元（IT之家注：现汇率约合 351.26 亿元人民币），计划于 2027 年下半年投入运营。SK 集团会长崔泰源 9 月介绍，在建数据中心首期容量预计到 2029 年达到 103MW，未来还计划在此基础上扩容近 900MW。随着项目推进，" data-title="韩国总统李在明：速度在 AI 竞赛中至关重要" data-date="11-21 22:26" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-21 22:26</span>
          <span class="news-item-title">韩国总统李在明：速度在 AI 竞赛中至关重要</span>
          <span class="news-value-point">💡 IT之家 11 月 21 日消息，据路透社报道，当地时间 21 日，韩国总统李在明前往韩国东南部城市蔚山，视察当地一座在建数据中心，并敦促韩国加…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/21/business/anthropic-stock-wall-street-silicon-valley.html" target="_blank" rel="noopener" data-cat="keji" data-summary="本周，这家人工智能巨头在首次公开募股中创下纪录，但在首个完整交易日却遭遇波折，原因是市场对人工智能支出的担忧导致市场大跌。" data-title="Anthropic’s Debut Shows the Disconnect Between Wall Street and Silicon Valley" data-date="11-21 18:03" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-21 18:03</span>
          <span class="news-item-title">Anthropic的首次亮相凸显了华尔街与硅谷之间的脱节</span>
          <span class="news-item-title-en">Anthropic’s Debut Shows the Disconnect Between Wall Street and Silicon Valley</span>
          <span class="news-value-point">💡 本周，这家人工智能巨头在首次公开募股中创下纪录，但在首个完整交易日却遭遇波折，原因是市场对人工智能支出的担忧导致市场大跌</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13614990/bruno-fernandes-man-utd-captain-confirms-contract-offer-but-says-negotiations-are-on-hold" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="布鲁诺·费尔南德斯在接受天空体育独家采访时表示，曼联已向他提供了一份新合同，但他已暂停谈判，因为他坚持认为俱乐部的首要任务必须是重返胜利轨道。" data-title="Fernandes: Man Utd have offered new deal but now is not time for talks" data-date="11-22 15:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-22 15:00</span>
          <span class="news-item-title">费尔南德斯：曼联已提出新合同，但现在不是谈判的时候</span>
          <span class="news-item-title-en">Fernandes: Man Utd have offered new deal but now is not time for talks</span>
          <span class="news-value-point">💡 布鲁诺·费尔南德斯在接受天空体育独家采访时表示，曼联已向他提供了一份新合同，但他已暂停谈判，因为他坚持认为俱乐部的首要任务必须是重返胜利轨道</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ckqx5w58dgv7o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="BBC体育专栏作家托尼·普利斯（Tony Pulis）解释了曼联新帅毛里西奥·波切蒂诺（Mauricio Pochettino）如何在与球队共事仅几天后为周日对阵利物浦的比赛做好准备。" data-title="&#39;He will see what Man Utd are made of&#39; - Pulis on Pochettino&#39;s first game" data-date="11-22 14:21" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-22 14:21</span>
          <span class="news-item-title">“他将看到曼联的实力”——普利斯谈波切蒂诺的首场比赛</span>
          <span class="news-item-title-en">'He will see what Man Utd are made of' - Pulis on Pochettino's first game</span>
          <span class="news-value-point">💡 BBC体育专栏作家托尼·普利斯（Tony Pulis）解释了曼联新帅毛里西奥·波切蒂诺（Mauricio Pochettino）如何在与球队共事…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ckx28w9ree9vo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳门将大卫·拉亚（David Raya）在周六与纽卡斯尔2-2战平的比赛中因伤下场，他将接受肩部扫描检查。" data-title="Raya set to have scan on injury - how much would Arsenal miss him?" data-date="11-22 05:14" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-22 05:14</span>
          <span class="news-item-title">拉亚将接受伤情扫描——阿森纳会多么想念他？</span>
          <span class="news-item-title-en">Raya set to have scan on injury - how much would Arsenal miss him?</span>
          <span class="news-value-point">💡 阿森纳门将大卫·拉亚（David Raya）在周六与纽卡斯尔2-2战平的比赛中因伤下场，他将接受肩部扫描检查</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025486/arsenal-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Arsenal latest: Arteta gives update on Raya injury" data-title="Arsenal latest: Arteta gives update on Raya injury" data-date="11-22 04:33" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-22 04:33</span>
          <span class="news-item-title">阿森纳最新消息：阿尔特塔通报拉亚的伤情</span>
          <span class="news-item-title-en">Arsenal latest: Arteta gives update on Raya injury</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13615040/arsenal-escape-with-2-2-draw-at-newcastle-after-complacent-second-half-almost-proves-costly-for-defending-champions" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="从“出色”到“自满”——阿森纳在纽卡斯尔客场下半场的表现急转直下，令人咋舌。" data-title="How &#39;complacent&#39; Arsenal unravelled at Newcastle - and their key lesson" data-date="11-22 04:21" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-22 04:21</span>
          <span class="news-item-title">“自满”的阿森纳如何在纽卡斯尔队面前溃不成军——以及他们吸取的重要教训</span>
          <span class="news-item-title-en">How 'complacent' Arsenal unravelled at Newcastle - and their key lesson</span>
          <span class="news-value-point">💡 从“出色”到“自满”——阿森纳在纽卡斯尔客场下半场的表现急转直下，令人咋舌</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6p9d102k4mdo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在取得九连胜后，伯恩茅斯在新任主教练马尔科·罗斯的带领下继续书写历史。" data-title="Nine wins in a row - Bournemouth &amp; Evanilson continue to make history" data-date="11-22 04:07" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-22 04:07</span>
          <span class="news-item-title">九连胜——伯恩茅斯和埃瓦尼尔森继续书写历史</span>
          <span class="news-item-title-en">Nine wins in a row - Bournemouth & Evanilson continue to make history</span>
          <span class="news-value-point">💡 在取得九连胜后，伯恩茅斯在新任主教练马尔科·罗斯的带领下继续书写历史</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/nov/21/newcastle-united-v-arsenal-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="纽卡斯尔在下半场强势反扑，上演了一场精彩的对攻大战，最终诺尼·马杜埃克的进球为阿森纳扳平比分，帮助球队拿到一分。“阿森纳的前锋三人组有起有落，不是吗？”查尔斯·安塔基写道。“埃泽、哈弗茨、马杜埃克——在任何一场比赛中，总有一个人" data-title="Newcastle United 2-2 Arsenal: Premier League – as it happened" data-date="11-22 03:48" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-22 03:48</span>
          <span class="news-item-title">纽卡斯尔联 2-2 阿森纳：英超联赛 – 赛况回顾</span>
          <span class="news-item-title-en">Newcastle United 2-2 Arsenal: Premier League – as it happened</span>
          <span class="news-value-point">💡 纽卡斯尔在下半场强势反扑，上演了一场精彩的对攻大战，最终诺尼·马杜埃克的进球为阿森纳扳平比分，帮助球队拿到一分</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/21/newcastle-arsenal-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="如果米克尔·阿尔特塔很高兴看到埃迪·豪不再担任纽卡斯尔的主教练，那么坏消息是，圣詹姆斯公园球场又迎来了一位同样令人头疼的场边对手。阿森纳的主教练似乎从来都不喜欢前往客场对阵" data-title="Raya injured but Madueke rescues point for Arsenal in seesaw Newcastle draw" data-date="11-22 03:47" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-22 03:47</span>
          <span class="news-item-title">拉亚受伤，但马杜埃克在与纽卡斯尔的势均力敌的平局中为阿森纳扳平比分</span>
          <span class="news-item-title-en">Raya injured but Madueke rescues point for Arsenal in seesaw Newcastle draw</span>
          <span class="news-value-point">💡 如果米克尔·阿尔特塔很高兴看到埃迪·豪不再担任纽卡斯尔的主教练，那么坏消息是，圣詹姆斯公园球场又迎来了一位同样令人头疼的场边对手</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/10/premier-league-top-scorers-2026-27-race-for-golden-boot" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="找出哪位英国顶尖射手正在向进球排行榜射击。继续阅读……" data-title="Premier League top scorers 2026-27: who is leading race for the golden boot?" data-date="11-22 03:42" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-22 03:42</span>
          <span class="news-item-title">2026-27赛季英超联赛最佳射手：谁是金靴赛的领跑者？</span>
          <span class="news-item-title-en">Premier League top scorers 2026-27: who is leading race for the golden boot?</span>
          <span class="news-value-point">💡 找出哪位英国顶尖射手正在向进球排行榜射击</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cq4gn97e8ee4o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="BBC体育的Alex Howell分享了他对纽卡斯尔联与阿森纳在英超联赛中2-2平局的球员评分，您也可以为球员评分。" data-title="Madueke &#39;a consistent threat&#39; - Newcastle v Arsenal player ratings" data-date="11-22 03:29" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-22 03:29</span>
          <span class="news-item-title">马杜埃凯“持续构成威胁”——纽卡斯尔对阵阿森纳球员评分</span>
          <span class="news-item-title-en">Madueke 'a consistent threat' - Newcastle v Arsenal player ratings</span>
          <span class="news-value-point">💡 BBC体育的Alex Howell分享了他对纽卡斯尔联与阿森纳在英超联赛中2-2平局的球员评分，您也可以为球员评分</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cm9d7jg50e12o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在卢卡·威廉姆斯-巴内特为热刺上演精彩的英超首秀后，BBC体育聚焦于热刺这位新晋少年球星。" data-title="&#39;The world got to see today&#39; - Williams-Barnett announces himself as Spurs star" data-date="11-22 03:21" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-22 03:21</span>
          <span class="news-item-title">“今天全世界都看到了”——威廉姆斯-巴内特宣布自己是热刺明星</span>
          <span class="news-item-title-en">'The world got to see today' - Williams-Barnett announces himself as Spurs star</span>
          <span class="news-value-point">💡 在卢卡·威廉姆斯-巴内特为热刺上演精彩的英超首秀后，BBC体育聚焦于热刺这位新晋少年球星</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/21/chelsea-leeds-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="哈维·阿隆索正步入危机边缘。这是一项令人难以置信的统计数据：切尔西排名第八，但目前在联赛中输掉的比赛比曼联还多。他们被气势汹汹的利兹联队压制，后者完全有理由在斯坦福桥取得首场胜利。" data-title="‘Fragile’ Chelsea must toughen up after Leeds humiliation, admits Xabi Alonso" data-date="11-22 03:20" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-22 03:20</span>
          <span class="news-item-title">哈维·阿隆索承认，在利兹联的羞辱之后，‘脆弱’的切尔西必须变得坚韧</span>
          <span class="news-item-title-en">‘Fragile’ Chelsea must toughen up after Leeds humiliation, admits Xabi Alonso</span>
          <span class="news-value-point">💡 哈维·阿隆索正步入危机边缘</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cwe8944d004yo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="切尔西主教练哈维·阿隆索的蜜月期已经结束，在斯坦福桥以 1-4 输给利兹联后，他现在正处于救火模式。" data-title="&#39;Fragile&#39; and &#39;miles off it&#39; - Alonso&#39;s Chelsea honeymoon is over" data-date="11-22 03:04" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-22 03:04</span>
          <span class="news-item-title">“脆弱”且“相去甚远”——阿隆索在切尔西的蜜月期结束了</span>
          <span class="news-item-title-en">'Fragile' and 'miles off it' - Alonso's Chelsea honeymoon is over</span>
          <span class="news-value-point">💡 切尔西主教练哈维·阿隆索的蜜月期已经结束，在斯坦福桥以 1-4 输给利兹联后，他现在正处于救火模式</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c50md981n277o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在利兹联客场战胜切尔西的比赛中，裁判判给利兹联一个关键的点球，这再次引发了英超联赛关于手球是否故意的争论。" data-title="&#39;Officials can&#39;t use common sense&#39; - was Rogers handball correct?" data-date="11-22 02:30" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-22 02:30</span>
          <span class="news-item-title">“裁判不会用常识”——罗杰斯的手球判罚正确吗？</span>
          <span class="news-item-title-en">'Officials can't use common sense' - was Rogers handball correct?</span>
          <span class="news-value-point">💡 在利兹联客场战胜切尔西的比赛中，裁判判给利兹联一个关键的点球，这再次引发了英超联赛关于手球是否故意的争论</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/newcastle-united-vs-arsenal/report/559552" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳在英超联赛中四连胜且未失一球的势头被纽卡斯尔以一场激烈的 2-2 平局终结。" data-title="Arsenal&#39;s winning run ended by Newcastle in thrilling draw" data-date="11-22 02:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-22 02:00</span>
          <span class="news-item-title">阿森纳的连胜势头被纽卡斯尔终结，双方上演激动人心的平局</span>
          <span class="news-item-title-en">Arsenal's winning run ended by Newcastle in thrilling draw</span>
          <span class="news-value-point">💡 阿森纳在英超联赛中四连胜且未失一球的势头被纽卡斯尔以一场激烈的 2-2 平局终结</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-22/10736094.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网黑河11月22日电 (王琳 胡心玥)黑河红河谷国际滑雪场于22日开板迎客，作为该市唯一SSS级滑雪场，经过全方位升级改造，以全新设施、多元业态，为广大游客营造高品质冰雪游玩体验。" data-title="黑河红河谷国际滑雪场开板迎客" data-date="11-22 16:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-22 16:44</span>
          <span class="news-item-title">黑河红河谷国际滑雪场开板迎客</span>
          <span class="news-value-point">💡 中新网黑河11月22日电 (王琳 胡心玥)黑河红河谷国际滑雪场于22日开板迎客，作为该市唯一SSS级滑雪场，经过全方位升级改造，以全新设施、多元…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-22/10736089.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网福建永春11月22日电 题：“中国芦柑之乡”福建永春果香越山海" data-title="（乡村行·看振兴）“中国芦柑之乡”福建永春果香越山海" data-date="11-22 16:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-22 16:43</span>
          <span class="news-item-title">（乡村行·看振兴）“中国芦柑之乡”福建永春果香越山海</span>
          <span class="news-value-point">💡 中新网福建永春11月22日电 题：“中国芦柑之乡”福建永春果香越山海</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/622.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 22 日消息，天津大学脑机海河实验室团队近日在国际权威期刊《科学 · 进展》（Science Advances）发表最新研究成果。团队提出了一种高鲁棒性（稳健性，Robustness）的超声调制脑电信号解码技术，首次实现人体被试数据层面的稳态视觉诱发电位（Steady-State Visual Evoked Potentials，SSVEP）脑电源信号高精度解码。该技术可在多种复杂、极端场景下高保真无创重建颅内脑电源波形，为高时空分辨率超声脑机接口的广泛应用提供关键支撑。据介绍，脑机接口通过在大脑与计算机之间建立直接的信息通路，有望实现最高形态的人机混合智能。但传统无创脑机接口受限于头皮脑电的低空间分辨率瓶颈导致脑信息读取量受限，严重制约系统性能。超声调制脑电技术是一种基" data-title="首次：天津大学脑机海河实验室实现人体超声脑机接口高时空分辨解码" data-date="11-22 16:36" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-22 16:36</span>
          <span class="news-item-title">首次：天津大学脑机海河实验室实现人体超声脑机接口高时空分辨解码</span>
          <span class="news-value-point">💡 IT之家 11 月 22 日消息，天津大学脑机海河实验室团队近日在国际权威期刊《科学 · 进展》（Science Advances）发表最新研究…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/620.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 22 日消息，《GTA 6》已经成为迄今为止全球规模最大的游戏首发作品，以前所未有的声势席卷整个游戏行业，过去没有任何一款游戏的发售盛况能够与之相提并论。《GTA 6》发售首日销量超过 3000 万份，在 PS5 和 Xbox Series S|X 两大主机平台上均表现强势。事实上，知名行业分析师公布的一组数据更为惊人：超过半数的 PS5 用户都在首发期间体验了这款游戏。IT之家注意到，Circana 分析师马特 · 皮斯卡特拉（Matt Piscatella）在 BlueSky 上分享的数据显示，美国 PS5 玩家中，有 61% 在《GTA 6》发售当天启动并游玩了这款游戏。需要注意的是，这一数据仅统计了发售当天实际进入游戏的玩家，并未将那些因为工作、上学或其他事务而无" data-title="《GTA 6》首发统治力惊人：美国超六成 PS5 玩家首日涌入游戏" data-date="11-22 16:35" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-22 16:35</span>
          <span class="news-item-title">《GTA 6》首发统治力惊人：美国超六成 PS5 玩家首日涌入游戏</span>
          <span class="news-value-point">💡 IT之家 11 月 22 日消息，《GTA 6》已经成为迄今为止全球规模最大的游戏首发作品，以前所未有的声势席卷整个游戏行业，过去没有任何一款游…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-22/10736088.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="进入小雪节气，松花江还没有完全封冻，但是江畔的造雪机已经开始工作了，在新的冰雪季向人们发出邀请。" data-title="冰雪大世界建设进行时 哈尔滨今年还有这些亮点" data-date="11-22 16:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-22 16:28</span>
          <span class="news-item-title">冰雪大世界建设进行时 哈尔滨今年还有这些亮点</span>
          <span class="news-value-point">💡 进入小雪节气，松花江还没有完全封冻，但是江畔的造雪机已经开始工作了，在新的冰雪季向人们发出邀请</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/618.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 22 日消息，Rockstar Games 近日公开了《GTA 6》中 NPC 的设计过程，介绍了开发团队通过角色背景、个性特征及全新的内部技术，让游戏中的 NPC 更加贴合游戏世界。Rockstar Games 艺术视觉开发副总裁 Miriam Bellard 透露，团队在设计每个角色时，都会尝试站在角色本人的角度思考，了解他们在莱昂尼达州（Leonida）所处的环境和社会地位，并据此塑造完整的人物形象。Bellard 举例称，团队会考虑角色是否会聘请建筑师设计住所，还是选择自己动手装修；他们是否希望通过外观彰显身份和地位，还是更注重舒适性与实用性；他们平时是否整洁，以及具体的审美偏好。这些细节都会影响最终的视觉设计。她表示，开发团队很享受为不同人物和场景进行设计的过程" data-title="Rockstar 介绍《GTA6》人物设计细节：NPC 设计精度与主角标准统一、设身处地打造居家环境" data-date="11-22 16:26" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-22 16:26</span>
          <span class="news-item-title">Rockstar 介绍《GTA6》人物设计细节：NPC 设计精度与主角标准统一、设身处地打造居家环境</span>
          <span class="news-value-point">💡 IT之家 11 月 22 日消息，Rockstar Games 近日公开了《GTA 6》中 NPC 的设计过程，介绍了开发团队通过角色背景、个性…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/617.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 22 日消息，“迪粉之家”公众号昨日曝光了一组比亚迪全新一代汉的实车照片。据IT之家此前报道，11 月 2 日，比亚迪王朝网销售事业部总经理路天宣布，11 月广州车展将推出一款“用户呼声很高的车型”，预计为全新一代比亚迪汉。全新一代比亚迪汉已在工信部第 412 批新车申报目录中完成申报，共涉及四款车型，包括三款纯电版本与一款插混版本。新车车身长宽高为 5156/1969/1507（1492）mm，轴距 3030mm。对比现款汉，车长增加 161mm，宽度增加 59mm，轴距增加 110mm。车头造型饱满圆润，配备贯穿式前大灯，车头顶端搭载激光雷达。纯电版本提供三种动力配置：245kW 后驱入门版搭载型号 TZ205QYS 永磁同步单电机，峰值功率 245kW，最高车速 2" data-title="全新一代比亚迪汉新款配色实车曝光" data-date="11-22 16:19" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-22 16:19</span>
          <span class="news-item-title">全新一代比亚迪汉新款配色实车曝光</span>
          <span class="news-value-point">💡 IT之家 11 月 22 日消息，“迪粉之家”公众号昨日曝光了一组比亚迪全新一代汉的实车照片</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/616.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 22 日消息，Clicks 宣布，受“全球特种玻璃纤维织物供应短缺”影响，旗下配备实体键盘的 Communicator 手机交付时间将从原定的 2026 年 12 月推迟至 2027 年 1 月下旬至 2 月。Clicks 表示，Communicator 手机的硬件设计已经完成，FCC 认证也在按计划推进。目前影响生产进度的主要问题，是制造 12 层 PCB 所需的特殊玻璃纤维编织布。全球只有 6 家独立工厂能够生产这种材料，其中 4 家无法承接 Clicks 所需的订单规模，导致原材料采购耗时远超预期。按照最新计划，Communicator 手机将于 2027 年 1 月初启动组装，首批产品预计在 1 月下旬送达消费者手中。不过，由于中国农历新年前后工厂将于 2 月初停" data-title="Clicks Communicator 实体键盘手机因零部件供应短缺推迟交付，2027 年 1 月下旬发货" data-date="11-22 16:18" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-22 16:18</span>
          <span class="news-item-title">Clicks Communicator 实体键盘手机因零部件供应短缺推迟交付，2027 年 1 月下旬发货</span>
          <span class="news-value-point">💡 IT之家 11 月 22 日消息，Clicks 宣布，受“全球特种玻璃纤维织物供应短缺”影响，旗下配备实体键盘的 Communicator 手机…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/615.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 22 日消息，特斯拉 Cybertruck 现在可以更轻松地通过狭窄空间了。特斯拉官方 Cybertruck 账号在 X 平台宣布，车辆正在通过 OTA 方式获得一项新升级，进一步缩小转弯半径，让车辆能够完成“更小半径的转弯”。不过，这项升级有一定限制：车辆必须安装 2026.44 或更高版本的软件，而且只有 2027 款 Cybertruck 才能使用这项转向优化功能。大块头皮卡也能灵活转弯特斯拉没有公布优化后的具体转弯半径数据，但官方展示的升级前后对比画面显示，Cybertruck 转弯时所需的空间明显缩小。对于一辆重量超过 6000 磅（约 2722 千克）的皮卡而言，这一改进相当实用。此前，Cybertruck 就已经是同级全尺寸皮卡中较容易操控的车型之一。这在很" data-title="即将停产的特斯拉 Cybertruck 迎来 OTA 更新：2027 款转弯半径缩小" data-date="11-22 16:14" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-22 16:14</span>
          <span class="news-item-title">即将停产的特斯拉 Cybertruck 迎来 OTA 更新：2027 款转弯半径缩小</span>
          <span class="news-value-point">💡 IT之家 11 月 22 日消息，特斯拉 Cybertruck 现在可以更轻松地通过狭窄空间了</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/desktops/gaming-pcs/alienware-aurora-pc-with-rtx-5070-32gb-of-ram-drops-to-usd1-899-in-amazon-black-friday-offer-core-ultra-7-equipped-pc-is-one-of-the-best-value-prebuilt-deals-weve-seen-so-far" target="_blank" rel="noopener" data-cat="zonghe" data-summary="今年黑色星期五，选购这款搭载RTX 5070的Alienware Aurora游戏电脑，还配备32GB DDR5内存，仅售1899美元。" data-title="Alienware Aurora PC with RTX 5070, 32GB of RAM drops to $1,899 in Amazon Black Friday offer — Core Ultra 7 equipped PC is one of the best value prebuilt deals we’ve seen so far" data-date="11-22 16:08" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-22 16:08</span>
          <span class="news-item-title">配备RTX 5070、32GB内存的Alienware Aurora电脑在亚马逊黑色星期五优惠中降至1899美元——这款配备酷睿Ultra 7的电脑是我们迄今为止看到的性价比最高的预装电脑优惠之一</span>
          <span class="news-item-title-en">Alienware Aurora PC with RTX 5070, 32GB of RAM drops to $1,899 in Amazon Black Friday offer — Core Ultra 7 equipped PC is one of the best value prebuilt deals we’ve seen so far</span>
          <span class="news-value-point">💡 今年黑色星期五，选购这款搭载RTX 5070的Alienware Aurora游戏电脑，还配备32GB DDR5内存，仅售1899美元</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-22/10736076.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网扬州11月22日电 (徐珊珊 崔佳明)在2026年亚太经合组织(APEC)第三十三次领导人非正式会议主场馆深圳国际交流中心，一对红雕漆《锦绣万年春》花瓶庄重陈列，向来自亚太各国的重要嘉宾讲述匠心传承之美、和合共生的中国故事。22日，扬州运河文投集团相关负责人介绍，这对花瓶由所属扬州漆器厂创作。" data-title="扬州红雕漆对瓶亮相深圳APEC会议 “锦绣万年”传和合" data-date="11-22 15:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-22 15:50</span>
          <span class="news-item-title">扬州红雕漆对瓶亮相深圳APEC会议 “锦绣万年”传和合</span>
          <span class="news-value-point">💡 中新网扬州11月22日电 (徐珊珊 崔佳明)在2026年亚太经合组织(APEC)第三十三次领导人非正式会议主场馆深圳国际交流中心，一对红雕漆《锦…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/f1/news/12040/13615085/ferrari-boss-frederic-vasseur-blames-charles-leclerc-for-unacceptable-collision-with-lewis-hamilton-in-las-vegas-gp" target="_blank" rel="noopener" data-cat="zonghe" data-summary="法拉利车队领队弗雷德里克·瓦塞尔（Frederic Vasseur）指责夏尔·勒克莱尔（Charles Leclerc）在拉斯维加斯大奖赛中与队友刘易斯·汉密尔顿（Lewis Hamilton）发生“完全不可接受”的碰撞。" data-title="&#39;Completely unacceptable! - Vasseur slams Leclerc for Hamilton collision" data-date="11-22 15:50" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-22 15:50</span>
          <span class="news-item-title">“完全不能接受！”——瓦塞尔抨击勒克莱尔与汉密尔顿的碰撞</span>
          <span class="news-item-title-en">'Completely unacceptable! - Vasseur slams Leclerc for Hamilton collision</span>
          <span class="news-value-point">💡 法拉利车队领队弗雷德里克·瓦塞尔（Frederic Vasseur）指责夏尔·勒克莱尔（Charles Leclerc）在拉斯维加斯大奖赛中与队…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/f1/news/12040/13615084/max-verstappen-says-george-russell-so-far-below-his-level-after-poking-fun-at-rival-for-major-error-during-las-vegas-gp" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在赢得拉斯维加斯大奖赛后，马克斯·维斯塔潘（Max Verstappen）对梅赛德斯车手乔治·拉塞尔（George Russell）进行了尖锐的回应，称他“远远低于我的水平”。" data-title="&#39;He&#39;s so far below my level&#39; - Verstappen taunts Russell over Las Vegas GP error" data-date="11-22 15:45" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-22 15:45</span>
          <span class="news-item-title">“他远远达不到我的水平”——维斯塔潘嘲笑拉塞尔在拉斯维加斯大奖赛上的失误</span>
          <span class="news-item-title-en">'He's so far below my level' - Verstappen taunts Russell over Las Vegas GP error</span>
          <span class="news-value-point">💡 在赢得拉斯维加斯大奖赛后，马克斯·维斯塔潘（Max Verstappen）对梅赛德斯车手乔治·拉塞尔（George Russell）进行了尖锐的…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-22/10736071.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社湖南益阳11月22日电 题：湖南安化茶企抱团出海 “黑茶之乡”加速拓展全球市场" data-title="（走进中国乡村）湖南安化茶企抱团出海  “黑茶之乡”加速拓展全球市场" data-date="11-22 15:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-22 15:41</span>
          <span class="news-item-title">（走进中国乡村）湖南安化茶企抱团出海  “黑茶之乡”加速拓展全球市场</span>
          <span class="news-value-point">💡 中新社湖南益阳11月22日电 题：湖南安化茶企抱团出海 “黑茶之乡”加速拓展全球市场</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-22/10736070.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社成都11月22日电 题：4000元、96集、一个人 AI短剧《重生螳螂》的爆款样本" data-title="4000元、96集、一个人  AI短剧《重生螳螂》的爆款样本" data-date="11-22 15:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-22 15:40</span>
          <span class="news-item-title">4000元、96集、一个人  AI短剧《重生螳螂》的爆款样本</span>
          <span class="news-value-point">💡 中新社成都11月22日电 题：4000元、96集、一个人 AI短剧《重生螳螂》的爆款样本</span>
        </a>
  </div>
</div>
<script defer src="{{ "/assets/js/news-feed.js" | relative_url }}"></script>


<p class="news-updated">🕐 抓取更新于 2026-11-22 16:56（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
