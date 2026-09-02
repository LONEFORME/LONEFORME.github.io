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
      <span>2026-09-02 19:41 抓取更新</span>
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
        <span class="channel-count">32</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('zuqiu', this)">
        <span>⚽ 英超与足球风云</span>
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('keji', this)">
        <span>🤖 科技 & AI</span>
        <span class="channel-count">1</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('shizheng', this)">
        <span>🏛️ 时政与国际</span>
        <span class="channel-count">9</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('zonghe', this)">
        <span>📰 综合与社会</span>
        <span class="channel-count">1</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('meimei', this)">
        <span>🌍 西方媒体视角</span>
        <span class="channel-count">6</span>
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
  <a class="hero-featured-card" href="https://www.skysports.com/football/news/11661/13574593/summer-transfer-spending-premier-league-efl-wsl-scottish-premiership-laliga-ligue-1-serie-a-and-bundesliga-breakdowns" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在暑假期间，俱乐部在转会方面的支出是多少？我们处理这些数字……" data-title="您的俱乐部花了多少钱？英超联赛打破转会纪录" data-date="09-02 19:42" data-source="天空体育">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
        <span class="hero-featured-date">🕒 09-02 19:42</span>
      </div>
      <h2 class="hero-featured-title">您的俱乐部花了多少钱？英超联赛打破转会纪录</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.skysports.com/football/news/11661/13580082/transfer-deadline-day-brings-record-spending-but-will-any-money-be-enough-for-these-premier-league-clubs" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="它总结了一个疯狂的转会截止日，英国转会纪录在窗口的最后几个小时内被追平。恩佐·费尔南德斯从切尔西转会到曼城，度过了一个非凡的夏天，其中的支出达到了顶峰。" data-title="转会支出破纪录，但有人真的高兴吗？" data-date="09-02 19:42" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">🔥 焦点</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">转会支出破纪录，但有人真的高兴吗？</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/watch/video/13580198/explained-why-chelsea-still-sold-enzo-fernandez-despite-collapse-of-lamina-camara-deal" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育首席记者Kaveh Solhekol解释了为什么切尔西将恩佐·费尔南德斯（ Enzo Fernandez ）卖给了竞争对手曼城（ Manchester City ） ，尽管他们在最后一分钟从摩纳哥签下拉明·卡马拉（ Lamine Camara ）的交易中失败了。" data-title="“非常不开心” -为什么尽管有卡马拉戏剧，切尔西仍然卖掉了费尔南德斯" data-date="09-02 19:42" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">🔥 焦点</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">“非常不开心” -为什么尽管有卡马拉戏剧，切尔西仍然卖掉了费尔南德斯</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/football/news/11661/13580189/lamine-camara-monaco-pull-out-of-selling-midfielder-to-chelsea-in-47m-deal-after-blues-agreed-deal-for-enzo-fernandez-replacement" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="摩纳哥已经退出将Lamine Camara出售给切尔西的交易，切尔西认为法国俱乐部以一种非凡且非常不专业的方式行事。" data-title="（切尔西真的很不开心！ &#39;-摩纳哥退出出售Camara" data-date="09-02 19:42" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">🔥 焦点</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">（切尔西真的很不开心！ '-摩纳哥退出出售Camara</p>
    </a>
  </div>
</div>
<div class="news-grid">
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13574593/summer-transfer-spending-premier-league-efl-wsl-scottish-premiership-laliga-ligue-1-serie-a-and-bundesliga-breakdowns" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在暑假期间，俱乐部在转会方面的支出是多少？我们处理这些数字……" data-title="您的俱乐部花了多少钱？英超联赛打破转会纪录" data-date="09-02 19:42" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">09-02 19:42</span>
          <span class="news-item-title">您的俱乐部花了多少钱？英超联赛打破转会纪录</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13580082/transfer-deadline-day-brings-record-spending-but-will-any-money-be-enough-for-these-premier-league-clubs" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="它总结了一个疯狂的转会截止日，英国转会纪录在窗口的最后几个小时内被追平。恩佐·费尔南德斯从切尔西转会到曼城，度过了一个非凡的夏天，其中的支出达到了顶峰。" data-title="转会支出破纪录，但有人真的高兴吗？" data-date="09-02 19:42" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">09-02 19:42</span>
          <span class="news-item-title">转会支出破纪录，但有人真的高兴吗？</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13580198/explained-why-chelsea-still-sold-enzo-fernandez-despite-collapse-of-lamina-camara-deal" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育首席记者Kaveh Solhekol解释了为什么切尔西将恩佐·费尔南德斯（ Enzo Fernandez ）卖给了竞争对手曼城（ Manchester City ） ，尽管他们在最后一分钟从摩纳哥签下拉明·卡马拉（ Lamine Camara ）的交易中失败了。" data-title="“非常不开心” -为什么尽管有卡马拉戏剧，切尔西仍然卖掉了费尔南德斯" data-date="09-02 19:42" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">09-02 19:42</span>
          <span class="news-item-title">“非常不开心” -为什么尽管有卡马拉戏剧，切尔西仍然卖掉了费尔南德斯</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13580189/lamine-camara-monaco-pull-out-of-selling-midfielder-to-chelsea-in-47m-deal-after-blues-agreed-deal-for-enzo-fernandez-replacement" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="摩纳哥已经退出将Lamine Camara出售给切尔西的交易，切尔西认为法国俱乐部以一种非凡且非常不专业的方式行事。" data-title="（切尔西真的很不开心！ &#39;-摩纳哥退出出售Camara" data-date="09-02 19:42" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">09-02 19:42</span>
          <span class="news-item-title">（切尔西真的很不开心！ '-摩纳哥退出出售Camara</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13580201/folarin-balogun-monaco-strikers-move-to-everton-falls-through-after-deal-scuppered-chelseas-chances-of-signing-lamine-camara" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在交易破坏了切尔西签下拉明·卡马拉的机会之后，埃弗顿对摩纳哥前锋Folarin Balogun的转会已经失败。" data-title="Balogun离开埃弗顿优惠" data-date="09-02 19:42" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">09-02 19:42</span>
          <span class="news-item-title">Balogun离开埃弗顿优惠</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13580209/transfer-deadline-day-then-story-of-the-day" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在天空体育新闻上重温转会截止日带来的所有刺激和溢出。" data-title="天空体育新闻转会截止日的故事！" data-date="09-02 19:42" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">09-02 19:42</span>
          <span class="news-item-title">天空体育新闻转会截止日的故事！</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13579972/enzo-fernandez-transfer-news-man-city-sign-midfielder-from-chelsea-in-british-record-equalling-125m-deal" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼城以1.25亿英镑的联合英国纪录费从切尔西签下了恩佐·费尔南德斯。" data-title="曼城签署费尔南德斯在英国创纪录的交易" data-date="09-02 19:42" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">09-02 19:42</span>
          <span class="news-item-title">曼城签署费尔南德斯在英国创纪录的交易</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/12476234/transfer-centre-live-football-transfer-news-updates-and-rumours" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="转机中心现场直播！英格兰窗户关闭后的晚间戏剧" data-title="转机中心现场直播！英格兰窗户关闭后的晚间戏剧" data-date="09-02 19:42" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">09-02 19:42</span>
          <span class="news-item-title">转机中心现场直播！英格兰窗户关闭后的晚间戏剧</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/tennis/news/12040/13580205/us-open-coco-gauff-makes-storming-start-while-serena-and-venus-williams-are-drawn-to-face-maya-joint-and-chan-hao-ching-in-womens-doubles" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Coco Gauff以直接击败Zeynep Sonmez开始了她的美国公开赛活动，而两届女子双打冠军Serena和Venus Williams将在周二的平局后面对Maya Joint和Chan Hao-Ching。" data-title="高夫让暴风雨开始了，因为兹韦列夫避免了重大沮丧" data-date="09-02 19:42" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">09-02 19:42</span>
          <span class="news-item-title">高夫让暴风雨开始了，因为兹韦列夫避免了重大沮丧</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/tennis/news/12040/13580206/us-open-britains-arthur-fery-admitted-he-still-has-plenty-to-work-on-after-his-new-york-debut-was-cut-short" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国的亚瑟·费里（ Arthur Fery ）表示，在周二美国公开赛首次亮相被缩短后，他现在知道自己需要做些什么。" data-title="“我知道我必须做什么” -尽管美国公开赛已经退出，但Fery已经准备好迎接最佳挑战" data-date="09-02 19:42" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">09-02 19:42</span>
          <span class="news-item-title">“我知道我必须做什么” -尽管美国公开赛已经退出，但Fery已经准备好迎接最佳挑战</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13580283/fan-sings-oasis-classic-wonderwall-during-arthur-fery-match-against-lorenzo-musetti-at-us-open" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在亚瑟·费里（ Arthur Fery ）在美国网球公开赛上与洛伦佐·穆塞蒂（ Lorenzo Musetti ）的比赛中，球迷们演唱了绿洲经典的“Wond" data-title="（你是我的Wonderwall ！ &#39;| Fan在美国网球公开赛Fery比赛期间演唱Oasis经典歌曲" data-date="09-02 19:42" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">09-02 19:42</span>
          <span class="news-item-title">（你是我的Wonderwall ！ '| Fan在美国网球公开赛Fery比赛期间演唱Oasis经典歌曲</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/f1/live-blog/12040/13580330/f1-italian-gp-live-friday-practice-updates-results-stream-highlights-from-formula-1-race-weekend-at-monza" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="法拉利揭示舒马赫风格的制服，车队宣布意大利大奖赛的新秀" data-title="法拉利揭示舒马赫风格的制服，车队宣布意大利大奖赛的新秀" data-date="09-02 19:42" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">09-02 19:42</span>
          <span class="news-item-title">法拉利揭示舒马赫风格的制服，车队宣布意大利大奖赛的新秀</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/f1/news/12040/13579867/f1-fans-will-crucify-teams-if-team-orders-are-used-in-2026-title-battle-says-former-world-champion-mika-hakkinen" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="两届世界冠军米卡·哈基宁（ Mika Hakkinen ）警告说，如果一级方程式车队执行车队订单以试图影响今年的冠军争夺战，他们就有可能被这项运动的球迷“钉死”。" data-title="“粉丝将把他们钉在十字架上” - Hakkinen在冠军争夺战中对团队订单发出警告" data-date="09-02 19:42" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">09-02 19:42</span>
          <span class="news-item-title">“粉丝将把他们钉在十字架上” - Hakkinen在冠军争夺战中对团队订单发出警告</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/racing/news/12040/13579505/today-on-sky-sports-racing-bath-and-newcastle" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="我们周三有繁忙的一天比赛，从巴斯和纽卡斯尔出发，在天空体育赛车上直播……" data-title="Etienne在Bath追逐第一次成功" data-date="09-02 19:42" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">09-02 19:42</span>
          <span class="news-item-title">Etienne在Bath追逐第一次成功</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/f1/news/12040/13580177/italian-gp-will-lewis-hamilton-george-russell-or-lando-norris-seize-title-race-opening-due-to-kimi-antonelli-grid-penalties" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="随着世界冠军领袖基米·安东内利（ Kimi Antonelli ）将从意大利大奖赛的赛道后方开始，试图在积分榜上追逐他的三位英国人将有一个重要的机会。" data-title="汉密尔顿、罗素或诺里斯是否会在蒙扎夺冠？" data-date="09-02 19:42" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">09-02 19:42</span>
          <span class="news-item-title">汉密尔顿、罗素或诺里斯是否会在蒙扎夺冠？</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">科技创新 & AI 算力</span>
      <span class="news-category-count">1 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-02/10688971.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网兰州9月2日电 (杨娜)2日，以“科技改变生活，创新赢得未来”为主题的2026年全国科普月兰州主场活动暨“黄河之滨科普行”启动。在这场“科普集市”上，兰州50余家单位拿出了“看家本领”，让高深的科学知识变得可触摸、可体验。" data-title="兰州“科”代表集合 “高精尖”遇见“烟火气”" data-date="09-02 19:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 科技前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-02 19:29</span>
          <span class="news-item-title">兰州“科”代表集合 “高精尖”遇见“烟火气”</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🏛️</span>
      <span class="news-category-title">时政要闻 & 国际动态</span>
      <span class="news-category-count">9 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/kong/2026/09-02/10688986.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="金秋启新学，奋进正当时。随着各地中小学、高校陆续开学，青春活力重回校园，广大青年学子踏上求知求索、逐梦成长的全新征程。" data-title="青春华章｜我苏青评：以科学之光，照亮开学第一课" data-date="09-02 19:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-02 19:37</span>
          <span class="news-item-title">青春华章｜我苏青评：以科学之光，照亮开学第一课</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/cul/2026/09-02/10688976.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网广州9月2日电 (记者 孙秋霞)第六届粤港澳大湾区文学周正在广州举行，来自国内外的知名作家、专家学者相聚一堂，围绕“APEC视野下的文学表达”主题，探索在跨文化交流新语境下，文学表达从“区域叙事”向“国际对话”的拓展路径，共答“文明互鉴”“如何共鸣”的文学之问。" data-title="中外知名作家畅谈“APEC视野下的文学表达”" data-date="09-02 19:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-02 19:34</span>
          <span class="news-item-title">中外知名作家畅谈“APEC视野下的文学表达”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-02/10688975.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网太原9月2日电 题：从“卖场”变“磁场” 线上阅读时代实体书店破局新路" data-title="从“卖场”变“磁场” 线上阅读时代实体书店破局新路" data-date="09-02 19:25" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-02 19:25</span>
          <span class="news-item-title">从“卖场”变“磁场” 线上阅读时代实体书店破局新路</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/02/world/middleeast/us-iran-strikes.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="美国军方表示，此次袭击是对最近针对美军和海上交通的袭击的报复。伊朗官员称，一场婚礼遭到袭击，平民丧生。" data-title="美国和伊朗在一夜的猛烈袭击后调查损失" data-date="09-02 18:43" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-02 18:43</span>
          <span class="news-item-title">美国和伊朗在一夜的猛烈袭击后调查损失</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/02/world/middleeast/iran-nuclear-program-iaea.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="随着战争的继续，国际原子能机构的一份内部报告称，伊朗拒绝允许其检查人员进入是一个紧迫的问题。" data-title="联合国监督机构称伊朗核计划状况尚不清楚" data-date="09-02 18:32" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-02 18:32</span>
          <span class="news-item-title">联合国监督机构称伊朗核计划状况尚不清楚</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/02/podcasts/the-headlines/russia-kyiv-strikes-whistleblower-warning-mail-voting.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="另外，在 91 岁时徒步旅行了 2,190 英里。" data-title="俄罗斯折磨基辅的新举措以及举报人对邮寄投票的警告" data-date="09-02 18:00" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-02 18:00</span>
          <span class="news-item-title">俄罗斯折磨基辅的新举措以及举报人对邮寄投票的警告</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/02/business/health-insurance-increases.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="美国的一项新调查预计，除非福利被削减，否则平均增幅将达到 11%，这是几十年来的最高水平。其他调查结果也预测该数字将急剧上升。" data-title="雇主健康成本预计将在 2027 年飙升" data-date="09-02 18:00" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-02 18:00</span>
          <span class="news-item-title">雇主健康成本预计将在 2027 年飙升</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/02/world/asia/uss-lincoln-arrives-thailand.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="数千名水手和海军陆战队员在美国服役。亚伯拉罕·林肯因在伊朗战争中的艰难部署而成为人们关注的焦点。" data-title="美国亚伯拉罕·林肯在泰国靠岸，让疲惫的船员休息一下" data-date="09-02 17:32" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-02 17:32</span>
          <span class="news-item-title">美国亚伯拉罕·林肯在泰国靠岸，让疲惫的船员休息一下</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c5y4rkd5zepo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="委内瑞拉近期没有举行选举，或者说，没有任何明确的选举计划，这在许多反对者看来是一种背叛。" data-title="美国公司获批委内瑞拉油田百年开采权 分析人士迷惑 国民震怒" data-date="09-02 16:59" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-02 16:59</span>
          <span class="news-item-title">美国公司获批委内瑞拉油田百年开采权 分析人士迷惑 国民震怒</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">1 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c4g5djd75gpo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="今年从巴基斯坦和伊朗遭遣返回阿富汗的人数，已再增加100万。" data-title="“我从未去过的祖国”：600万阿富汗人遭邻国驱逐，在塔利班治下重新开始" data-date="09-02 17:18" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-02 17:18</span>
          <span class="news-item-title">“我从未去过的祖国”：600万阿富汗人遭邻国驱逐，在塔利班治下重新开始</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🌍</span>
      <span class="news-category-title">🌍 西方媒体视角 (外媒看中国 · 奇葩言论集锦)</span>
      <span class="news-category-count">6 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-02/10688972.shtml" target="_blank" rel="noopener" data-cat="meimei" data-summary="中新网克拉玛依9月2日电 题：在新疆牧区，AI开始给牛羊“看”病" data-title="在新疆牧区，AI开始给牛羊“看”病" data-date="09-02 19:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-meimei">🌍 外媒视角</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-02 19:34</span>
          <span class="news-item-title">在新疆牧区，AI开始给牛羊“看”病</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-02/10688969.shtml" target="_blank" rel="noopener" data-cat="meimei" data-summary="中新社台北9月2日电 台湾一黄姓男子及其妻子涉嫌组织“爱情诈骗集团”，通过人工智能(AI)变声等技术行骗，犯罪所得超过9亿元新台币，受害者逾2万人。台北地方检察署2日起诉57名被告，对黄姓男子及其妻子分别求刑25年以上、18年以上。" data-title="台湾一诈骗集团利用AI变声行骗逾9亿元新台币" data-date="09-02 19:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-meimei">🌍 外媒视角</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-02 19:34</span>
          <span class="news-item-title">台湾一诈骗集团利用AI变声行骗逾9亿元新台币</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/dwq/2026/09-02/10688963.shtml" target="_blank" rel="noopener" data-cat="meimei" data-summary="中新社香港9月2日电 (张语洽 刘玥晴)由香港贸易发展局(简称“贸发局”)主办的第11届香港国际时尚汇展(CENTRESTAGE)2日在香港会议展览中心开幕，吸引来自24个国家和地区的约270个品牌参展，参展品牌数量创历届新高。" data-title="香港国际时尚汇展开幕   参展品牌数量创历届新高" data-date="09-02 19:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-meimei">🌍 外媒视角</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-02 19:31</span>
          <span class="news-item-title">香港国际时尚汇展开幕   参展品牌数量创历届新高</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cly7r8yrxe5o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="meimei" data-summary="现年29岁的民主派活动人士黄之锋，在法庭上承认一项中国《香港国安法》下的“串谋勾结外国势力危害国家安全”罪，判刑押后至另日进行。至今，黄之锋已失去自由逾2,100天。" data-title="黄之锋“勾结外国势力危害国家安全”案认罪，最高可囚终身" data-date="09-02 16:06" data-source="BBC">
          <span class="news-cat-tag cat-meimei">🌍 外媒视角</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-02 16:06</span>
          <span class="news-item-title">黄之锋“勾结外国势力危害国家安全”案认罪，最高可囚终身</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cz6zpzwwxlzo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="meimei" data-summary="事发河谷上游已形成两个堰塞湖。与此同时，原本散布在喜马拉雅山区的冰川湖，在灾区内有10座被标记为高风险，专家形容它们是“定时炸弹”。" data-title="尼泊尔—西藏泥石流：堰塞湖和冰湖是下一个“定时炸弹”？" data-date="09-02 08:01" data-source="BBC">
          <span class="news-cat-tag cat-meimei">🌍 外媒视角</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-02 08:01</span>
          <span class="news-item-title">尼泊尔—西藏泥石流：堰塞湖和冰湖是下一个“定时炸弹”？</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cp802gnj5kmo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="meimei" data-summary="吉隆口岸位处西藏与尼泊尔的重要贸易通路之上，中国与尼泊尔两侧各有数以百计外国旅客在泥石流冲击后下落不明。" data-title="泥石流摧毁西藏吉隆口岸的关键几分钟" data-date="09-01 20:01" data-source="BBC">
          <span class="news-cat-tag cat-meimei">🌍 外媒视角</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-01 20:01</span>
          <span class="news-item-title">泥石流摧毁西藏吉隆口岸的关键几分钟</span>
        </a>
  </div>
</div>

<script>
function onNewsSearch(query) {
  query = (query || '').trim().toLowerCase();
  const items = document.querySelectorAll('.news-item, .hero-featured-card, .hero-sub-card');
  let matched = 0;
  items.forEach(el => {
    const title = (el.getAttribute('data-title') || el.innerText || '').toLowerCase();
    const summary = (el.getAttribute('data-summary') || '').toLowerCase();
    const source = (el.getAttribute('data-source') || '').toLowerCase();
    const isMatch = !query || title.includes(query) || summary.includes(query) || source.includes(query);
    el.style.display = isMatch ? '' : 'none';
    if (isMatch) matched++;
  });
  document.querySelectorAll('.news-category').forEach(cat => {
    const visibleChildren = cat.querySelectorAll('.news-item:not([style*="display: none"])');
    cat.style.display = (visibleChildren.length > 0 || !query) ? '' : 'none';
  });
  const countEl = document.getElementById('news-search-count');
  if (countEl) {
    countEl.innerText = query ? `🔍 找到 ${matched} 条` : '';
  }
}

document.addEventListener('DOMContentLoaded', () => {
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

<p class="news-updated">🕐 抓取更新于 2026-09-02 19:41（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
