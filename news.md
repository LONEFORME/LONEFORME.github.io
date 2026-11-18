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
      <span>2026-11-19 04:45 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num">60</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">4</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">天空体育×16 · 中国新闻网×10</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">按来源聚合 · 最近 24 小时精选</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.theverge.com/policy/1036935/congress-forced-arbitration-deepfakes-defiance-act" target="_blank" rel="noopener" data-cat="shizheng" data-summary="距离2026年底仅剩数周时间，立法者正努力通过针对深伪创作者和阻止用户提起诉讼的在线平台的新法律，为在线侵害受害者提供保护。周二，参议院司法委员会的成员" data-title="Tech lawsuits defined 2026 — and lawmakers want more" data-date="11-19 03:07" data-source="The Verge">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
        <span class="hero-featured-date">🕒 11-19 03:07</span>
      </div>
      <h2 class="hero-featured-title">科技诉讼成为2026年的标志性事件——立法者希望有更多此类诉讼</h2>
      <div class="hero-featured-title-en">Tech lawsuits defined 2026 — and lawmakers want more</div>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://techcrunch.com/2026/11/18/snapchat-now-lets-developers-build-ar-lenses-with-ai-coding-assistants-like-claude-code-and-cursor/" target="_blank" rel="noopener" data-cat="keji" data-summary="Snapchat表示，Lens创作者可以用通俗易懂的语言描述他们想要的Lens，而他们的AI助手将从头到尾处理整个过程。" data-title="Snapchat now lets developers build AR Lenses with AI assistants like Claude Code and Cursor" data-date="11-19 03:56" data-source="TechCrunch">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
      </div>
      <p class="hero-sub-title">Snapchat现允许开发者使用Claude Code和Cursor等AI助手来构建AR滤镜</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/football/live-blog/12040/13176154/scottish-premiership-news-transfers-rumours-gossip-and-more" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Scottish football latest: Dumbarton appoint youngest manager in SPFL history" data-title="Scottish football latest: Dumbarton appoint youngest manager in SPFL history" data-date="11-19 03:00" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">苏格兰足球最新消息：邓巴顿任命苏超联赛历史上最年轻的主教练</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/f1/news/12040/13611531/valtteri-bottas-cadillac-confirm-finnish-driver-to-stay-with-team-for-2027-formula-1-season-ahead-of-las-vegas-grand-prix" target="_blank" rel="noopener" data-cat="zonghe" data-summary="凯迪拉克已确认瓦尔特里·博塔斯将在2027年F1赛季继续留在车队，结束了外界对这位芬兰车手未来的猜测。" data-title="Cadillac confirm Bottas to stay with team for 2027" data-date="11-19 04:11" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">凯迪拉克确认博塔斯将在 2027 年继续留在车队</p>
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
        <a class="news-item" href="https://www.theverge.com/policy/1036935/congress-forced-arbitration-deepfakes-defiance-act" target="_blank" rel="noopener" data-cat="shizheng" data-summary="距离2026年底仅剩数周时间，立法者正努力通过针对深伪创作者和阻止用户提起诉讼的在线平台的新法律，为在线侵害受害者提供保护。周二，参议院司法委员会的成员" data-title="Tech lawsuits defined 2026 — and lawmakers want more" data-date="11-19 03:07" data-source="The Verge">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-19 03:07</span>
          <span class="news-item-title">科技诉讼成为2026年的标志性事件——立法者希望有更多此类诉讼</span>
          <span class="news-item-title-en">Tech lawsuits defined 2026 — and lawmakers want more</span>
          <span class="news-value-point">💡 距离2026年底仅剩数周时间，立法者正努力通过针对深伪创作者和阻止用户提起诉讼的在线平台的新法律，为在线侵害受害者提供保护</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/18/us/politics/vance-trump-iran-2028-election-rubio.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="这场紧张局势发生在副总统的一个关键时刻，她正在考虑是否在2028年竞选总统。" data-title="Trump Grows Frustrated With Vance Over Iran War Critique" data-date="11-19 01:15" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-19 01:15</span>
          <span class="news-item-title">特朗普因万斯对伊朗战争的批评而感到沮丧</span>
          <span class="news-item-title-en">Trump Grows Frustrated With Vance Over Iran War Critique</span>
          <span class="news-value-point">💡 这场紧张局势发生在副总统的一个关键时刻，她正在考虑是否在2028年竞选总统</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/18/us/politics/hakeem-jeffries-speaker-of-the-house-democrats.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="经过投票，纽约州众议员哈基姆·杰弗里斯有望成为首位赢得总统继任第二顺位职位的黑人议员。" data-title="Democrats Nominate Hakeem Jeffries for Speaker of the House, Making History" data-date="11-19 00:42" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-19 00:42</span>
          <span class="news-item-title">民主党提名哈基姆·杰弗里斯为众议院议长，创造历史</span>
          <span class="news-item-title-en">Democrats Nominate Hakeem Jeffries for Speaker of the House, Making History</span>
          <span class="news-value-point">💡 经过投票，纽约州众议员哈基姆·杰弗里斯有望成为首位赢得总统继任第二顺位职位的黑人议员</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-19/10734432.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月19日电 (记者 孙自法)直立人是生存年代最长的古人类物种之一，已知在约190万年到10.8万年前分布在整个非洲到欧亚大陆东部。不过，由于此前中国特别是华南地区相关化石记录存在空白，成为古人类演化关键谜题之一，备受关注。" data-title="中国广西新发现直立人化石 将助力破解古人类演化关键谜题" data-date="11-19 00:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-19 00:07</span>
          <span class="news-item-title">中国广西新发现直立人化石 将助力破解古人类演化关键谜题</span>
          <span class="news-value-point">💡 中新网北京11月19日电 (记者 孙自法)直立人是生存年代最长的古人类物种之一，已知在约190万年到10.8万年前分布在整个非洲到欧亚大陆东部</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-18/10734423.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="去餐馆吃家乡菜、进小店给本国车厘子、龙虾“带货”、到大学演讲、和学生互动……" data-title="到大学演讲、给车厘子“带货”、打卡家乡菜……各国领导人在深圳忙不停" data-date="11-18 22:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 22:55</span>
          <span class="news-item-title">到大学演讲、给车厘子“带货”、打卡家乡菜……各国领导人在深圳忙不停</span>
          <span class="news-value-point">💡 去餐馆吃家乡菜、进小店给本国车厘子、龙虾“带货”、到大学演讲、和学生互动……</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-18/10734415.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社深圳11月18日电 (记者 黄钰钦)11月18日晚，中国国家主席习近平和夫人彭丽媛在深圳国际交流中心举行宴会，欢迎出席亚太经合组织第三十三次领导人非正式会议的来宾。" data-title="（深圳APEC）详讯：习近平和彭丽媛为出席亚太经合组织第三十三次领导人非正式会议的来宾举行欢迎宴会" data-date="11-18 22:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 22:42</span>
          <span class="news-item-title">（深圳APEC）详讯：习近平和彭丽媛为出席亚太经合组织第三十三次领导人非正式会议的来宾举行欢迎宴会</span>
          <span class="news-value-point">💡 中新社深圳11月18日电 (记者 黄钰钦)11月18日晚，中国国家主席习近平和夫人彭丽媛在深圳国际交流中心举行宴会，欢迎出席亚太经合组织第三十三…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-18/10734419.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网云南大理11月18日电 (记者 韩帅南)记者18日从大理州委宣传部获悉，近日，在云南省大理白族自治州成立70周年之际，一封跨越重洋的贺信从南半球传来。澳大利亚米尔迪拉市市长海伦·希利议员致信，向大理州送上祝贺。" data-title="从墨累河畔到苍山洱海：一封越洋贺信里的大理开放故事" data-date="11-18 22:38" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 22:38</span>
          <span class="news-item-title">从墨累河畔到苍山洱海：一封越洋贺信里的大理开放故事</span>
          <span class="news-value-point">💡 中新网云南大理11月18日电 (记者 韩帅南)记者18日从大理州委宣传部获悉，近日，在云南省大理白族自治州成立70周年之际，一封跨越重洋的贺信从…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-18/10734411.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="11月18日晚，国家主席习近平和夫人彭丽媛在深圳国际交流中心举行宴会，欢迎出席亚太经合组织第三十三次领导人非正式会议的来宾。习近平在祝酒辞中说——" data-title="习近平：看五十年的中国就来深圳" data-date="11-18 22:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 22:33</span>
          <span class="news-item-title">习近平：看五十年的中国就来深圳</span>
          <span class="news-value-point">💡 11月18日晚，国家主席习近平和夫人彭丽媛在深圳国际交流中心举行宴会，欢迎出席亚太经合组织第三十三次领导人非正式会议的来宾</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-18/10734403.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="11月18日晚，国家主席习近平和夫人彭丽媛在深圳国际交流中心举行宴会，欢迎出席亚太经合组织第三十三次领导人非正式会议的来宾。习近平发表祝酒辞指出——" data-title="【和合共生】习言道丨为了建设亚太共同体，我们跨越山海走到一起" data-date="11-18 22:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 22:32</span>
          <span class="news-item-title">【和合共生】习言道丨为了建设亚太共同体，我们跨越山海走到一起</span>
          <span class="news-value-point">💡 11月18日晚，国家主席习近平和夫人彭丽媛在深圳国际交流中心举行宴会，欢迎出席亚太经合组织第三十三次领导人非正式会议的来宾</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-18/10734405.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="11月18日晚，国家主席习近平和夫人彭丽媛在深圳国际交流中心举行宴会，欢迎出席亚太经合组织第三十三次领导人非正式会议的来宾。" data-title="新华图讯丨习近平和彭丽媛为出席亚太经合组织第三十三次领导人非正式会议的来宾举行欢迎宴会" data-date="11-18 22:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 22:31</span>
          <span class="news-item-title">新华图讯丨习近平和彭丽媛为出席亚太经合组织第三十三次领导人非正式会议的来宾举行欢迎宴会</span>
          <span class="news-value-point">💡 11月18日晚，国家主席习近平和夫人彭丽媛在深圳国际交流中心举行宴会，欢迎出席亚太经合组织第三十三次领导人非正式会议的来宾</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-18/10734388.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社深圳11月18日电 (记者 尹倩芸)11月18日，在深圳举行的2026年亚太经合组织(APEC)工商领导人峰会开幕式上，中国向全球工商界发出一份合作“邀请函”。" data-title="（深圳APEC）中国向全球工商界发出合作“邀请函”" data-date="11-18 22:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 22:30</span>
          <span class="news-item-title">（深圳APEC）中国向全球工商界发出合作“邀请函”</span>
          <span class="news-value-point">💡 中新社深圳11月18日电 (记者 尹倩芸)11月18日，在深圳举行的2026年亚太经合组织(APEC)工商领导人峰会开幕式上，中国向全球工商界发…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cjy5xkw9g1zpo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="这是中国自1980年以来，首次有最高领导人亲赴机场迎接外国元首。1980年前，华国锋、毛泽东都有多次赴机场迎接外国领袖的历史。" data-title="APEC深圳峰会：习近平亲赴机场迎接特朗普，46年来首次中国元首接机" data-date="11-18 21:21" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-18 21:21</span>
          <span class="news-item-title">APEC深圳峰会：习近平亲赴机场迎接特朗普，46年来首次中国元首接机</span>
          <span class="news-value-point">💡 这是中国自1980年以来，首次有最高领导人亲赴机场迎接外国元首</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-18/10734335.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网布里斯班11月18日电 (记者 薄雯雯)中昆“旅游+”对话会17日在澳大利亚昆士兰州首府布里斯班举行。与会嘉宾围绕中国与昆士兰州在旅游、教育、体育等领域的合作展开交流。" data-title="中国驻布里斯班总领馆举办中昆“旅游+”对话会" data-date="11-18 20:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 20:33</span>
          <span class="news-item-title">中国驻布里斯班总领馆举办中昆“旅游+”对话会</span>
          <span class="news-value-point">💡 中新网布里斯班11月18日电 (记者 薄雯雯)中昆“旅游+”对话会17日在澳大利亚昆士兰州首府布里斯班举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-18/10734268.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月18日电 阿布扎比消息：当地时间18日，阿联酋阿布扎比国家石油公司旗下的物流与服务公司表示，该公司一艘船只17日晚途经霍尔木兹海峡时遭到袭击，造成11人受伤、1人失踪。" data-title="阿联酋方面称一船只在霍尔木兹海峡遇袭  致11人伤、1人失踪" data-date="11-18 18:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 18:53</span>
          <span class="news-item-title">阿联酋方面称一船只在霍尔木兹海峡遇袭  致11人伤、1人失踪</span>
          <span class="news-value-point">💡 中新社北京11月18日电 阿布扎比消息：当地时间18日，阿联酋阿布扎比国家石油公司旗下的物流与服务公司表示，该公司一艘船只17日晚途经霍尔木兹海…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/18/world/asia/trump-imelda-marcos.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="菲律宾总统表示，特朗普总统和菲律宾前第一夫人彼此非常熟悉。" data-title="Trump Briefly Met an Old Friend in Manila: Imelda Marcos" data-date="11-18 17:52" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-18 17:52</span>
          <span class="news-item-title">特朗普在马尼拉与老友伊梅尔达·马科斯短暂会面</span>
          <span class="news-item-title-en">Trump Briefly Met an Old Friend in Manila: Imelda Marcos</span>
          <span class="news-value-point">💡 菲律宾总统表示，特朗普总统和菲律宾前第一夫人彼此非常熟悉</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://techcrunch.com/2026/11/18/snapchat-now-lets-developers-build-ar-lenses-with-ai-coding-assistants-like-claude-code-and-cursor/" target="_blank" rel="noopener" data-cat="keji" data-summary="Snapchat表示，Lens创作者可以用通俗易懂的语言描述他们想要的Lens，而他们的AI助手将从头到尾处理整个过程。" data-title="Snapchat now lets developers build AR Lenses with AI assistants like Claude Code and Cursor" data-date="11-19 03:56" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-19 03:56</span>
          <span class="news-item-title">Snapchat现允许开发者使用Claude Code和Cursor等AI助手来构建AR滤镜</span>
          <span class="news-item-title-en">Snapchat now lets developers build AR Lenses with AI assistants like Claude Code and Cursor</span>
          <span class="news-value-point">💡 Snapchat表示，Lens创作者可以用通俗易懂的语言描述他们想要的Lens，而他们的AI助手将从头到尾处理整个过程</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/18/technology/google-gemini-ai-search-schools-nyc-la-chicago.html" target="_blank" rel="noopener" data-cat="keji" data-summary="谷歌拒绝将人工智能功能与面向学生的搜索功能分拆，引发了强烈反弹。现在，学校正在寻找替代方案。" data-title="NYC, LA and Chicago School Districts Weigh Breaking Up With Google Search Over A.I." data-date="11-19 03:51" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-19 03:51</span>
          <span class="news-item-title">纽约市、洛杉矶和芝加哥的学区正考虑因人工智能而放弃使用Google搜索</span>
          <span class="news-item-title-en">NYC, LA and Chicago School Districts Weigh Breaking Up With Google Search Over A.I.</span>
          <span class="news-value-point">💡 谷歌拒绝将人工智能功能与面向学生的搜索功能分拆，引发了强烈反弹</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1035924/nvidia-visualized-revenue-profit-earnings-after-huang" target="_blank" rel="noopener" data-cat="keji" data-summary="如果有人每秒钟给你 8300 美元，你会怎么做？这就是英伟达现在赚取的纯利润。等您读完这段话时，英伟达很可能已经赚到了4.5万美元多一点。Nvidia是一家……的公司，看待它很容易。" data-title="What’s next for Nvidia? Whatever doesn’t rock the mind-bogglingly profitable boat" data-date="11-19 03:30" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-19 03:30</span>
          <span class="news-item-title">英伟达的下一步是什么？任何不会动摇这艘令人难以置信的盈利之船的事情</span>
          <span class="news-item-title-en">What’s next for Nvidia? Whatever doesn’t rock the mind-bogglingly profitable boat</span>
          <span class="news-value-point">💡 如果有人每秒钟给你 8300 美元，你会怎么做</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/big-tech/nvidia-promises-employee-pay-raises-equity-before-december-to-quell-unrest-in-wake-of-jensen-huang-scandal-at-first-all-hands-meeting-since-ceos-departure-staff-offered-perks-told-were-going-to-be-fine" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道，在黄仁勋辞职后举行的公司首次全体员工大会上，临时首席执行官科莱特·克雷斯（Collete Kress）向员工承诺提前加薪并增加股权。" data-title="Nvidia promises employee pay raises, equity before December to quell unrest in wake of Jensen Huang scandal" data-date="11-19 02:40" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-19 02:40</span>
          <span class="news-item-title">Nvidia承诺为员工加薪，并在12月前发放股权，以平息黄仁勋丑闻引发的不满情绪</span>
          <span class="news-item-title-en">Nvidia promises employee pay raises, equity before December to quell unrest in wake of Jensen Huang scandal</span>
          <span class="news-value-point">💡 据报道，在黄仁勋辞职后举行的公司首次全体员工大会上，临时首席执行官科莱特·克雷斯（Collete Kress）向员工承诺提前加薪并增加股权</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1036880/nvidia-rtx-spark-ai-mini-pc-desktops" target="_blank" rel="noopener" data-cat="keji" data-summary="继今年早些时候首批 RTX Spark 笔记本电脑上市之后，Nvidia 的 RTX Spark N1X 芯片现已应用于华硕、戴尔和微星的台式机。宏碁、技嘉和惠普的更多 RTX Spark 台式机也即将推出，而微软的 Surface RTX" data-title="The first Nvidia RTX Spark mini PCs launch today from Asus, Dell, and MSI" data-date="11-19 02:34" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-19 02:34</span>
          <span class="news-item-title">华硕、戴尔和微星今日首发搭载英伟达 RTX Spark 的迷你电脑</span>
          <span class="news-item-title-en">The first Nvidia RTX Spark mini PCs launch today from Asus, Dell, and MSI</span>
          <span class="news-value-point">💡 继今年早些时候首批 RTX Spark 笔记本电脑上市之后，Nvidia 的 RTX Spark N1X 芯片现已应用于华硕、戴尔和微星的台式机</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/18/more-banks-says-customers-using-ai-agents-are-on-their-own-even-if-they-get-hacked/" target="_blank" rel="noopener" data-cat="keji" data-summary="花旗是最新一家叫停个人理财AI代理的大型金融机构。" data-title="More banks say customers using AI agents are on their own — even if they get hacked" data-date="11-19 01:32" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-19 01:32</span>
          <span class="news-item-title">更多银行表示，使用人工智能代理的客户需自行承担风险——即使他们遭到黑客攻击</span>
          <span class="news-item-title-en">More banks say customers using AI agents are on their own — even if they get hacked</span>
          <span class="news-value-point">💡 花旗是最新一家叫停个人理财AI代理的大型金融机构</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/18/sam-altman-warns-against-a-future-where-ai-not-humans-calls-the-shots/" target="_blank" rel="noopener" data-cat="keji" data-summary="Sam Altman和Greg Brockman对硅谷日益加剧的关于人工智能接管的争论表示反对，同时承认让人类掌控先进模型所面临的挑战。" data-title="Sam Altman warns against a future where AI, not humans, calls the shots" data-date="11-19 00:59" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-19 00:59</span>
          <span class="news-item-title">萨姆·阿尔特曼警告称，未来将由人工智能而非人类掌控大局</span>
          <span class="news-item-title-en">Sam Altman warns against a future where AI, not humans, calls the shots</span>
          <span class="news-value-point">💡 Sam Altman和Greg Brockman对硅谷日益加剧的关于人工智能接管的争论表示反对，同时承认让人类掌控先进模型所面临的挑战</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/029/124.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 19 日消息，腾讯昨日发布第三季度财报。财报显示，其第三季度实现营收 2073.36 亿元，同比增长 8%；毛利 1159.11 亿元，同比增长 7%；归母净利润为 636.12 亿元，同比增长 0.8%。据《科创板日报》报道，对于持续增加的 AI 投入，腾讯管理层在业绩会上表示，公司当前资本开支主要用于 AI 基础设施建设。这类投入并非一次性消耗，建成后的基础设施可以持续用于模型训练和 Token 生成。随着 2026 年、2027 年建设的基础设施在后续年份发挥作用，预计到 2028 年相关投入带来的经营压力有望逐步缓解。管理层同时提到，AI 基础设施的投入成本未来有望出现积极变化。其认为，目前设备采购价格相对较高，预计到 2028 年，同类设备采购价格将明显下降；此" data-title="腾讯：更多企业转向国产芯片，将助推国内供应链建设提速" data-date="11-19 00:40" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-19 00:40</span>
          <span class="news-item-title">腾讯：更多企业转向国产芯片，将助推国内供应链建设提速</span>
          <span class="news-value-point">💡 IT之家 11 月 19 日消息，腾讯昨日发布第三季度财报</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/18/us/anti-ai-protests-petitions-colleges.html" target="_blank" rel="noopener" data-cat="keji" data-summary="一些学生拒绝使用人工智能，还有一些学生开始发起请愿，要求在整个校园范围内限制人工智能的使用。高校已经注意到了这一点。" data-title="The Anti-A.I. Campus Movement Is Growing" data-date="11-19 00:16" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-19 00:16</span>
          <span class="news-item-title">反人工智能校园运动正在蓬勃发展</span>
          <span class="news-item-title-en">The Anti-A.I. Campus Movement Is Growing</span>
          <span class="news-value-point">💡 一些学生拒绝使用人工智能，还有一些学生开始发起请愿，要求在整个校园范围内限制人工智能的使用</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/18/openai-ceo-sam-altman-says-its-hard-to-imagine-the-ai-industry-without-jensen/" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达创始人兼前首席执行官黄仁勋上周因多起丑闻而辞职，其中包括与一名涉嫌为中国间谍的女子有染。" data-title="OpenAI CEO Sam Altman says it’s ‘hard to imagine the AI industry without Jensen’" data-date="11-19 00:14" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-19 00:14</span>
          <span class="news-item-title">OpenAI首席执行官萨姆·阿尔特曼表示，“很难想象没有黄仁勋的AI行业”。</span>
          <span class="news-item-title-en">OpenAI CEO Sam Altman says it’s ‘hard to imagine the AI industry without Jensen’</span>
          <span class="news-value-point">💡 英伟达创始人兼前首席执行官黄仁勋上周因多起丑闻而辞职，其中包括与一名涉嫌为中国间谍的女子有染</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/console-gaming/gta-vi-runs-at-1440p-on-ps5-and-xbox-series-x-but-just-720p-with-upscaling-on-series-s-rockstar-details-upscaling-technologies-for-launch" target="_blank" rel="noopener" data-cat="keji" data-summary="《GTA VI》将在PlayStation和Xbox主机上以30FPS为目标帧率，Rockstar将在PS5和Xbox Series X上使用其自研的时间抗锯齿解决方案，在PS5 Pro上使用索尼的PSSR 2，在Xbox Series S上使用AMD的FSR 4。" data-title="GTA VI runs at 1440p on PS5 and Xbox Series X, but just 720p with upscaling on Series S" data-date="11-19 00:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-19 00:00</span>
          <span class="news-item-title">《GTA VI》在PS5和Xbox Series X上以1440p运行，但在Series S上仅以720p运行并进行上采样。</span>
          <span class="news-item-title-en">GTA VI runs at 1440p on PS5 and Xbox Series X, but just 720p with upscaling on Series S</span>
          <span class="news-value-point">💡 《GTA VI》将在PlayStation和Xbox主机上以30FPS为目标帧率，Rockstar将在PS5和Xbox Series X上使用其…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1036549/nvidia-amd-earnings-fall-2026-chips-pause-frontier-models" target="_blank" rel="noopener" data-cat="keji" data-summary="今年夏天，OpenAI的AI代理意外黑进了Hugging Face，且早期证据表明其下一代模型能够独立发现并利用安全漏洞，因此OpenAI暂停了其计划中规模最大的前沿训练。9月，Anthropic首席执行官" data-title="Remember the frontier AI pause? Chip companies don’t either" data-date="11-18 23:44" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-18 23:44</span>
          <span class="news-item-title">还记得尖端人工智能暂停吗？芯片公司也不记得了</span>
          <span class="news-item-title-en">Remember the frontier AI pause? Chip companies don’t either</span>
          <span class="news-value-point">💡 今年夏天，OpenAI的AI代理意外黑进了Hugging Face，且早期证据表明其下一代模型能够独立发现并利用安全漏洞，因此OpenAI暂停了…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/029/121.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 18 日消息，北京时间今天（18 日）晚间，据美国 CNBC 援引知情人士消息称，Anthropic 考虑扩大 IPO 发行规模，并可能将发行价定在远高于 80 美元（IT之家注：现汇率约合 534.4 元人民币）的水平。当地时间 17 日，Anthropic 结束了认购意向征集，汇总了投资者需求，为登陆纳斯达克做准备。知情人士称，机构投资者的认购意向总额约为 4,000 亿美元（现汇率约合 2.67 万亿元人民币），散户认购意向也接近 1,000 亿美元（现汇率约合 6,679.86 亿元人民币）。不过，这些认购意向并不具有约束力，发行方案仍可能调整。知情人士透露，Anthropic 将在当地时间 18 日下午作出最终决定，预计在当天美股收盘后敲定 IPO 发行价。An" data-title="消息称 Anthropic 考虑扩大 IPO 规模，散户认购意向接近千亿美元" data-date="11-18 23:35" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-18 23:35</span>
          <span class="news-item-title">消息称 Anthropic 考虑扩大 IPO 规模，散户认购意向接近千亿美元</span>
          <span class="news-value-point">💡 IT之家 11 月 18 日消息，北京时间今天（18 日）晚间，据美国 CNBC 援引知情人士消息称，Anthropic 考虑扩大 IPO 发行…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/leaked-ohio-bill-could-allow-ai-data-center-companies-to-seize-private-land-for-their-buildouts-using-eminent-domain-law-proposed-law-would-expand-list-of-beneficiaries" target="_blank" rel="noopener" data-cat="keji" data-summary="一份泄露的俄亥俄州法案可能允许数据中心被认定为公共事业，以适用征用权法，从而使公司能够征用私人土地来建造新设施。" data-title="Leaked Ohio bill could allow AI data center companies to seize private land for their buildouts using eminent domain law" data-date="11-18 23:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-18 23:30</span>
          <span class="news-item-title">一份泄露的俄亥俄州法案显示，人工智能数据中心公司可能利用征用权法为其扩建项目征用私人土地。</span>
          <span class="news-item-title-en">Leaked Ohio bill could allow AI data center companies to seize private land for their buildouts using eminent domain law</span>
          <span class="news-value-point">💡 一份泄露的俄亥俄州法案可能允许数据中心被认定为公共事业，以适用征用权法，从而使公司能够征用私人土地来建造新设施</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/18/business/hospitals-java-artificial-intelligence.html" target="_blank" rel="noopener" data-cat="keji" data-summary="人工智能正在加剧医疗卫生系统所面临的威胁，这些系统多年来一直受到黑客的攻击。" data-title="Hospitals Rush to Patch Java Vulnerabilities" data-date="11-18 23:27" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-18 23:27</span>
          <span class="news-item-title">医院争相修补Java漏洞</span>
          <span class="news-item-title-en">Hospitals Rush to Patch Java Vulnerabilities</span>
          <span class="news-value-point">💡 人工智能正在加剧医疗卫生系统所面临的威胁，这些系统多年来一直受到黑客的攻击</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/12040/13176154/scottish-premiership-news-transfers-rumours-gossip-and-more" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Scottish football latest: Dumbarton appoint youngest manager in SPFL history" data-title="Scottish football latest: Dumbarton appoint youngest manager in SPFL history" data-date="11-19 03:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-19 03:00</span>
          <span class="news-item-title">苏格兰足球最新消息：邓巴顿任命苏超联赛历史上最年轻的主教练</span>
          <span class="news-item-title-en">Scottish football latest: Dumbarton appoint youngest manager in SPFL history</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/12476234/transfer-centre-live-football-transfer-news-updates-and-rumours" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Transfer Centre LIVE! Time for Man Utd to sell Fernandes? Vote here!" data-title="Transfer Centre LIVE! Time for Man Utd to sell Fernandes? Vote here!" data-date="11-19 03:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-19 03:00</span>
          <span class="news-item-title">转会中心直播！是时候让曼联出售费尔南德斯了吗？在此投票！</span>
          <span class="news-item-title-en">Transfer Centre LIVE! Time for Man Utd to sell Fernandes? Vote here!</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13613662/free-stream-watch-special-unfinished-business-transfer-show-on-sky-sports-news-with-guest-alan-pardew" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="FREE STREAM: Watch &#39;Unfinished Business&#39; Transfer Show on Sky Sports News" data-title="FREE STREAM: Watch &#39;Unfinished Business&#39; Transfer Show on Sky Sports News" data-date="11-19 02:55" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-19 02:55</span>
          <span class="news-item-title">免费直播：在Sky Sports News观看“未完成的交易”转会节目</span>
          <span class="news-item-title-en">FREE STREAM: Watch 'Unfinished Business' Transfer Show on Sky Sports News</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/029/127.htm" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="IT之家 11 月 19 日消息，华为 WATCH Air 真机谍照已在各大平台曝光。画面显示，新表至少提供两种表带款式可选，包括运动硅胶表带和金属米兰尼斯表带。据博主 @搞机王腾霄 透露，华为 WATCH Air 主打轻薄，采用方形设计，配备有钛金属表体。新表还有望内置高硅叠片异形电池，续航可达 5 天。已曝光的海报显示，华为 WATCH Air 采用超轻薄设计，拥有圆润的弧面机身，侧边配有一枚旋转表冠按钮和一枚多功能按键。此外，这款手表还预装了鸿蒙 HarmonyOS 系统。目前，华为官方暂未公布这款手表的具体配置信息，但爆料提到，这款手表将采用高亮钛一体化设计，提供黑、银、金三种配色。IT之家也将持续关注这款智能手表新品，并在第一时间带来最新情报。" data-title="华为 WATCH Air 真机曝光：方形设计、钛金属表体，消息称续航可达 5 天" data-date="11-19 01:20" data-source="IT之家">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-19 01:20</span>
          <span class="news-item-title">华为 WATCH Air 真机曝光：方形设计、钛金属表体，消息称续航可达 5 天</span>
          <span class="news-value-point">💡 IT之家 11 月 19 日消息，华为 WATCH Air 真机谍照已在各大平台曝光</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13613154/bruno-fernandes-tumbles-as-new-no-1-is-crowned-sky-sports-ranks-the-premier-leagues-top-25-players-right-now" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在英超联赛前25名球员的重大洗牌中，布鲁诺·费尔南德斯被拉下英超联赛之王的宝座。" data-title="Fernandes tumbles as new No 1 is crowned: Sky Sports&#39; top 25 Premier League players" data-date="11-19 01:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-19 01:00</span>
          <span class="news-item-title">费尔南德斯跌落榜单，新晋头号球员加冕：天空体育英超联赛25大球员榜单</span>
          <span class="news-item-title-en">Fernandes tumbles as new No 1 is crowned: Sky Sports' top 25 Premier League players</span>
          <span class="news-value-point">💡 在英超联赛前25名球员的重大洗牌中，布鲁诺·费尔南德斯被拉下英超联赛之王的宝座</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13613629/sky-sports-writers-give-their-hot-takes-on-the-premier-leagues-top-25-players" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育数字团队对英超联赛的25大球员发表了热门观点……" data-title="Premier League Top 25 - Sky Sports writers give their HOT TAKES" data-date="11-19 01:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-19 01:00</span>
          <span class="news-item-title">英超联赛前25名——天空体育记者发表热门观点</span>
          <span class="news-item-title-en">Premier League Top 25 - Sky Sports writers give their HOT TAKES</span>
          <span class="news-value-point">💡 天空体育数字团队对英超联赛的25大球员发表了热门观点……</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cj3vgp36z063o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英超联赛将于周六恢复，水晶宫、桑德兰和曼联目前处于降级区。但现在担心还为时过早吗？" data-title="The tightest survival scrap for years? Why it&#39;s not too early to worry" data-date="11-19 00:09" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-19 00:09</span>
          <span class="news-item-title">多年来最激烈的保级大战？为什么现在担心并不为时过早</span>
          <span class="news-item-title-en">The tightest survival scrap for years? Why it's not too early to worry</span>
          <span class="news-value-point">💡 英超联赛将于周六恢复，水晶宫、桑德兰和曼联目前处于降级区</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13612918/premier-league-predictor-predict-the-fixtures-each-gameweek-generate-your-table-and-share-results" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Premier League predictor - play our new game each week!" data-title="Premier League predictor - play our new game each week!" data-date="11-19 00:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-19 00:00</span>
          <span class="news-item-title">英超联赛预测器 - 每周玩我们的新游戏！</span>
          <span class="news-item-title-en">Premier League predictor - play our new game each week!</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13613285/alex-scott-arsenal-keen-on-chelsea-and-liverpool-target-with-bournemouth-softening-stance-over-potential-sale" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳是英超联赛中对签约伯恩茅斯和英格兰中场球员亚历克斯·斯科特感兴趣的三大俱乐部之一。" data-title="Arsenal willing to make sales to beat Chelsea and Liverpool to Scott signing" data-date="11-18 23:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 23:00</span>
          <span class="news-item-title">阿森纳愿意出售球员，以期在斯科特签约方面击败切尔西和利物浦</span>
          <span class="news-item-title-en">Arsenal willing to make sales to beat Chelsea and Liverpool to Scott signing</span>
          <span class="news-value-point">💡 阿森纳是英超联赛中对签约伯恩茅斯和英格兰中场球员亚历克斯·斯科特感兴趣的三大俱乐部之一</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025492/man-utd-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Man Utd latest: Pochettino&#39;s first words as he arrives at Carrington for first time" data-title="Man Utd latest: Pochettino&#39;s first words as he arrives at Carrington for first time" data-date="11-18 23:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 23:00</span>
          <span class="news-item-title">曼联最新消息：波切蒂诺首次抵达卡灵顿训练基地后的首批言论</span>
          <span class="news-item-title-en">Man Utd latest: Pochettino's first words as he arrives at Carrington for first time</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13613290/transfer-news-your-premier-league-clubs-unfinished-business-ahead-of-january-window" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Your PL club&#39;s &#39;Unfinished Business&#39; revealed ahead of January window" data-title="Your PL club&#39;s &#39;Unfinished Business&#39; revealed ahead of January window" data-date="11-18 20:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 20:00</span>
          <span class="news-item-title">英超俱乐部“未竟之事”在1月转会窗口开启前揭晓</span>
          <span class="news-item-title-en">Your PL club's 'Unfinished Business' revealed ahead of January window</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13613260/man-utd-transfer-news-calvin-bassey-and-jarrad-branthwaite-among-targets-with-mauricio-pochettino-set-to-be-backed-in-january" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联主教练毛里西奥·波切蒂诺预计将在 1 月转会窗口获得支持，因为俱乐部希望扭转本赛季令人失望的开局。" data-title="Man Utd expected to back Poch in January transfer window" data-date="11-18 20:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 20:00</span>
          <span class="news-item-title">曼联预计将在 1 月转会窗口为波切蒂诺提供支持</span>
          <span class="news-item-title-en">Man Utd expected to back Poch in January transfer window</span>
          <span class="news-value-point">💡 曼联主教练毛里西奥·波切蒂诺预计将在 1 月转会窗口获得支持，因为俱乐部希望扭转本赛季令人失望的开局</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13613260/man-utd-transfer-news-calvin-bassey-and-jarrad-branthwaite-among-targets-with-mauricio-pochettino-set-to-be-backed-in-january" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联主教练毛里西奥·波切蒂诺预计将在 1 月转会窗口获得支持，因为俱乐部希望扭转本赛季令人失望的开局。" data-title="Man Utd expected to back Poch in January transfer window" data-date="11-18 20:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 20:00</span>
          <span class="news-item-title">曼联预计将在 1 月转会窗口为波切蒂诺提供支持</span>
          <span class="news-item-title-en">Man Utd expected to back Poch in January transfer window</span>
          <span class="news-value-point">💡 曼联主教练毛里西奥·波切蒂诺预计将在 1 月转会窗口获得支持，因为俱乐部希望扭转本赛季令人失望的开局</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025489/tottenham-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Spurs latest: &#39;Tottenham were one of three clubs in Poch&#39;s USA exit clause&#39;" data-title="Spurs latest: &#39;Tottenham were one of three clubs in Poch&#39;s USA exit clause&#39;" data-date="11-18 17:47" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 17:47</span>
          <span class="news-item-title">热刺最新消息：“热刺是波切蒂诺美国解约条款中提及的三家俱乐部之一”</span>
          <span class="news-item-title-en">Spurs latest: 'Tottenham were one of three clubs in Poch's USA exit clause'</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13613499/mauricio-pochettino-incoming-manchester-united-head-coach-calls-for-time-to-topple-manchester-city-ahead-of-old-trafford-arrival" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="当被问及曼城的主导地位时，毛里西奥·波切蒂诺（Mauricio Pochettino）承诺将让曼联再次成为这座城市的霸主，并坚持表示“你们会看到的”。" data-title="Pochettino vows to make Manchester red again" data-date="11-18 17:21" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 17:21</span>
          <span class="news-item-title">波切蒂诺誓言让曼彻斯特再次变红</span>
          <span class="news-item-title-en">Pochettino vows to make Manchester red again</span>
          <span class="news-value-point">💡 当被问及曼城的主导地位时，毛里西奥·波切蒂诺（Mauricio Pochettino）承诺将让曼联再次成为这座城市的霸主，并坚持表示“你们会看到…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/f1/news/12040/13611531/valtteri-bottas-cadillac-confirm-finnish-driver-to-stay-with-team-for-2027-formula-1-season-ahead-of-las-vegas-grand-prix" target="_blank" rel="noopener" data-cat="zonghe" data-summary="凯迪拉克已确认瓦尔特里·博塔斯将在2027年F1赛季继续留在车队，结束了外界对这位芬兰车手未来的猜测。" data-title="Cadillac confirm Bottas to stay with team for 2027" data-date="11-19 04:11" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-19 04:11</span>
          <span class="news-item-title">凯迪拉克确认博塔斯将在 2027 年继续留在车队</span>
          <span class="news-item-title-en">Cadillac confirm Bottas to stay with team for 2027</span>
          <span class="news-value-point">💡 凯迪拉克已确认瓦尔特里·博塔斯将在2027年F1赛季继续留在车队，结束了外界对这位芬兰车手未来的猜测</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/18/sam-altman-says-his-life-is-so-weird-that-hes-unfazed-by-andrew-garfield-portraying-him-in-upcoming-movie/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="“这感觉并不像是我人生中最奇怪的十件事之一。”奥特曼说。" data-title="Sam Altman says his life is so weird that he’s unfazed by Andrew Garfield portraying him in upcoming movie" data-date="11-19 04:07" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-19 04:07</span>
          <span class="news-item-title">Sam Altman表示，他的生活如此离奇，以至于他对安德鲁·加菲尔德（Andrew Garfield）在即将上映的电影中扮演他的角色并不感到意外。</span>
          <span class="news-item-title-en">Sam Altman says his life is so weird that he’s unfazed by Andrew Garfield portraying him in upcoming movie</span>
          <span class="news-value-point">💡 “这感觉并不像是我人生中最奇怪的十件事之一</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/golf/news/12040/13613712/brooks-koepka-american-labels-his-2026-pga-tour-season-a-disappointment-and-targets-2027-ryder-cup-spot" target="_blank" rel="noopener" data-cat="zonghe" data-summary="布鲁克斯·科普卡将他的2026赛季称为“令人失望的”，但他坚持认为自己渴望在2027年莱德杯中获得美国队的一席之地。" data-title="Koepka &#39;disappointed&#39; with PGA Tour season but &#39;beyond happy&#39; to be back" data-date="11-19 03:43" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-19 03:43</span>
          <span class="news-item-title">科普卡对 PGA 巡回赛赛季感到“失望”，但对回归赛场“非常高兴”</span>
          <span class="news-item-title-en">Koepka 'disappointed' with PGA Tour season but 'beyond happy' to be back</span>
          <span class="news-value-point">💡 布鲁克斯·科普卡将他的2026赛季称为“令人失望的”，但他坚持认为自己渴望在2027年莱德杯中获得美国队的一席之地</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/policy/1036749/trump-ai-chip-data-center-us-philippines-pax-silica" target="_blank" rel="noopener" data-cat="zonghe" data-summary="据当地新闻媒体Rappler报道，周二，唐纳德·特朗普总统在抵达菲律宾时，受到了不下五位选美皇后的迎接。当他踏上停机坪时，一个孩子递给他一面小小的美国国旗和一面菲律宾国旗。一支乐队奏起了乐曲。" data-title="Trump’s latest land grab is an AI hub in the Philippines" data-date="11-19 03:40" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-19 03:40</span>
          <span class="news-item-title">特朗普的最新土地掠夺是一处位于菲律宾的人工智能中心</span>
          <span class="news-item-title-en">Trump’s latest land grab is an AI hub in the Philippines</span>
          <span class="news-value-point">💡 据当地新闻媒体Rappler报道，周二，唐纳德·特朗普总统在抵达菲律宾时，受到了不下五位选美皇后的迎接</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1036693/sony-bravia-8-ii-oled-black-friday-2026-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="黑色星期五是为您的冬季电影之夜选购新款OLED电视并享受优惠的绝佳时机。不过，事实证明，您现在已经可以以超值价格买到65英寸的索尼Bravia 8 II，这是我们最喜爱的OLED电视之一。目前该产品正在享受" data-title="Sony’s impressive Bravia 8 II OLED hits a new low price ahead of Black Friday" data-date="11-19 03:30" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-19 03:30</span>
          <span class="news-item-title">索尼令人印象深刻的Bravia 8 II OLED电视在黑色星期五前创下新低价</span>
          <span class="news-item-title-en">Sony’s impressive Bravia 8 II OLED hits a new low price ahead of Black Friday</span>
          <span class="news-value-point">💡 黑色星期五是为您的冬季电影之夜选购新款OLED电视并享受优惠的绝佳时机</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1036941/instagram-now-lets-you-edit-your-stories-after-you-post-them" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Instagram 的最新更新将允许您编辑您的“故事”，而不会丢失您的浏览量、点赞数或回复。Instagram负责人Adam Mosseri宣布，现在，您在分享故事后最多有15分钟的时间来编辑文字、音乐、贴纸和涂鸦。" data-title="Instagram now lets you edit your stories after you post them" data-date="11-19 03:29" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-19 03:29</span>
          <span class="news-item-title">Instagram 现在允许您在发布故事后对其进行编辑</span>
          <span class="news-item-title-en">Instagram now lets you edit your stories after you post them</span>
          <span class="news-value-point">💡 Instagram 的最新更新将允许您编辑您的“故事”，而不会丢失您的浏览量、点赞数或回复</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/games/1036819/the-leaked-lenovo-legion-go-beam-could-be-the-affordable-handheld-we-need" target="_blank" rel="noopener" data-cat="zonghe" data-summary="有一段时间，联想似乎放弃了销售掌上游戏电脑，将其Legion Go 2和Legion Go S的价格抬高到远远高于其他内存不足的竞争对手。现在，一款像样的产品很容易就要花掉 1000 美元，甚至 2000 美元。但它看起来" data-title="The leaked Lenovo Legion Go Beam could be the affordable handheld we need" data-date="11-19 03:11" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-19 03:11</span>
          <span class="news-item-title">曝光的联想Legion Go Beam可能是我们需要的实惠掌机</span>
          <span class="news-item-title-en">The leaked Lenovo Legion Go Beam could be the affordable handheld we need</span>
          <span class="news-value-point">💡 有一段时间，联想似乎放弃了销售掌上游戏电脑，将其Legion Go 2和Legion Go S的价格抬高到远远高于其他内存不足的竞争对手</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1028991/black-friday-best-early-deals-2026" target="_blank" rel="noopener" data-cat="zonghe" data-summary="黑色星期五的倒计时已经开始，各种折扣也开始陆续登场。虽然购物节要到11月27日才正式开始，但零售商已经开始对我们喜爱的一些科技产品推出提前优惠。当然，随着价格上涨，" data-title="The best early Black Friday deals you can already shop" data-date="11-19 02:44" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-19 02:44</span>
          <span class="news-item-title">您已经可以购买的最佳黑色星期五提前优惠</span>
          <span class="news-item-title-en">The best early Black Friday deals you can already shop</span>
          <span class="news-value-point">💡 黑色星期五的倒计时已经开始，各种折扣也开始陆续登场</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/darts/live-blog/12040/13613592/grand-slam-of-darts-live-commentary-updates-scores-analysis-with-luke-littler-gerwyn-price-rob-cross-in-action" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Grand Slam of Darts LIVE! Price in action after Cross loses out to Springer" data-title="Grand Slam of Darts LIVE! Price in action after Cross loses out to Springer" data-date="11-19 02:30" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-19 02:30</span>
          <span class="news-item-title">飞镖大满贯直播！克罗斯输给斯普林格后，普莱斯上场比赛</span>
          <span class="news-item-title-en">Grand Slam of Darts LIVE! Price in action after Cross loses out to Springer</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/18/well/rfk-jr-uspstf-health-care.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="15名曾任成员和联邦雇员向《纽约时报》透露，在过去两年里，政府阻碍了他们的工作，并终结了美国预防服务工作组的科学独立性。" data-title="How RFK Jr. Upended a Group Guiding Health Care for All Americans" data-date="11-19 02:04" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-19 02:04</span>
          <span class="news-item-title">罗伯特·肯尼迪·肯尼迪二世如何颠覆一个为所有美国人提供医疗保健指导的组织</span>
          <span class="news-item-title-en">How RFK Jr. Upended a Group Guiding Health Care for All Americans</span>
          <span class="news-value-point">💡 15名曾任成员和联邦雇员向《纽约时报》透露，在过去两年里，政府阻碍了他们的工作，并终结了美国预防服务工作组的科学独立性</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/18/googles-ai-feature-in-search-gets-its-own-incognito-mode/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="谷歌的新临时会话让用户可以在AI模式下进行对话，而不会将这些对话添加到他们的搜索历史记录中，也不会影响未来的推荐。" data-title="Google’s AI feature in Search gets its own incognito mode" data-date="11-19 02:04" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-19 02:04</span>
          <span class="news-item-title">谷歌搜索的AI功能将拥有自己的无痕模式</span>
          <span class="news-item-title-en">Google’s AI feature in Search gets its own incognito mode</span>
          <span class="news-value-point">💡 谷歌的新临时会话让用户可以在AI模式下进行对话，而不会将这些对话添加到他们的搜索历史记录中，也不会影响未来的推荐</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/18/us/politics/amazon-delivery-drones-massachusetts.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="亚马逊希望提供更快的配送服务。居民希望天空宁静。马萨诸塞州的一个郊区正在为争夺其领空控制权而展开一场史诗般的斗争。" data-title="A Massachusetts Town Revolts Against Amazon’s Delivery Drones" data-date="11-19 01:48" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-19 01:48</span>
          <span class="news-item-title">马萨诸塞州一城镇抗议亚马逊的无人机派送服务</span>
          <span class="news-item-title-en">A Massachusetts Town Revolts Against Amazon’s Delivery Drones</span>
          <span class="news-value-point">💡 亚马逊希望提供更快的配送服务</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/029/128.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 19 日消息，今年 10 月底，华为 WATCH 5 系列、ULTIMATE DESIGN 星钻绽放等手表开启 HarmonyOS 7 花粉 Beta 版招募。随后 7.0.0.107 SP18 版本开启推送。但据用户反馈，部分设备更新后出现 BUG，因此升级活动暂缓。IT之家注意到，华为官方最新宣布，HarmonyOS 7.0.0.107SP41 版本开始分批推送给花粉 Beta 版升级尝鲜报名入选成功的 WATCH 5 系列用户。适配机型HUAWEI WATCH 5 42mm（含十周年款）（SOC-AL00）HUAWEI WATCH 5 46mm（含十周年款）（RTS-AL00）版本更新日志6.1.0.330SP18/6.1.0.330SP22/6.1.0.333/6" data-title="华为 WATCH 5 智能手表重启鸿蒙 HarmonyOS 7 花粉 Beta 版升级，新增地震预警消息等功能" data-date="11-19 01:28" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-19 01:28</span>
          <span class="news-item-title">华为 WATCH 5 智能手表重启鸿蒙 HarmonyOS 7 花粉 Beta 版升级，新增地震预警消息等功能</span>
          <span class="news-value-point">💡 IT之家 11 月 19 日消息，今年 10 月底，华为 WATCH 5 系列、ULTIMATE DESIGN 星钻绽放等手表开启 Harmon…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/029/126.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 19 日消息，近期 AI 逆向实现了很多有趣的项目，让很多不少设备有了新玩法。其中，让各式各样的设备刷入苹果 iOS 系统，是当下最受欢迎的探索方向之一。参考IT之家此前报道，已有小米 8 刷入 iOS 16.5 系统并伪装成 iPhone X、REDMI K20 Pro 刷入苹果 iOS 16 测试固件包变身真“全面屏 iPhone”等先例。不过刷入 iOS 后的设备常常伴随着功能缺失和运行不稳定，最典型的就是 Wi-Fi 下线、Face ID / Touch ID 失效等。博主 @BugOS技术组 昨晚分享的视频显示，已有刷入 iOS 系统的安卓设备成功“复活”Touch ID，实现指纹解锁功能，同时录制指纹也是正常的。从目前的进度来看，安卓手机刷入 iOS 系统已从" data-title="Touch ID 成功复活：“安卓版”iOS 系统实现指纹解锁功能" data-date="11-19 01:10" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-19 01:10</span>
          <span class="news-item-title">Touch ID 成功复活：“安卓版”iOS 系统实现指纹解锁功能</span>
          <span class="news-value-point">💡 IT之家 11 月 19 日消息，近期 AI 逆向实现了很多有趣的项目，让很多不少设备有了新玩法</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/029/125.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 19 日消息，华为 Mate 90 系列手机已率先开启鸿蒙 HarmonyOS 7.0.0.115 SP11 版本升级，系统包大小约 10.31GB，带来了 AI 快捷栏等功能。据博主 @怪咖学徒_ 反馈，在升级 HarmonyOS 7.0.0.115 版本后，华为 Mate 90 系列手机“悄悄”上线了完全体 3D 空间壁纸功能，支持重力感应特性。从视频演示效果来看，该功能可将壁纸 3D 空间化，手机晃动，壁纸内容也会跟随晃动。参考IT之家此前报道，今年 9 月发布的 HarmonyOS 7 操作系统主打全新空间美学设计语言，锁屏界面新增 3D 空间壁纸、空间时钟功能，可将照片中的元素与 3D 时钟巧妙结合，带来更加立体的壁纸效果。新系统还将液态玻璃带到了通知中心、文件" data-title="华为 Mate 90 系列手机推 HarmonyOS 7.0.0.115 升级，“悄悄”上线完全体 3D 空间壁纸功能" data-date="11-19 00:55" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-19 00:55</span>
          <span class="news-item-title">华为 Mate 90 系列手机推 HarmonyOS 7.0.0.115 升级，“悄悄”上线完全体 3D 空间壁纸功能</span>
          <span class="news-value-point">💡 IT之家 11 月 19 日消息，华为 Mate 90 系列手机已率先开启鸿蒙 HarmonyOS 7.0.0.115 SP11 版本升级，系统…</span>
        </a>
  </div>
</div>
<script defer src="{{ "/assets/js/news-feed.js" | relative_url }}"></script>


<p class="news-updated">🕐 抓取更新于 2026-11-19 04:45（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
