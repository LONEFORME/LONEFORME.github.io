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
      <span>2026-10-24 01:19 抓取更新</span>
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
        <span class="channel-count">53</span>
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
        <span class="channel-count">8</span>
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
  <div class="ov-item"><span class="ov-num">53</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×19 · The Verge×6</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.nytimes.com/2026/10/23/us/politics/democratic-agenda.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="民主党一直致力于降低生活成本，并追究特朗普政府的责任。这是如果他们赢得大多数人的话，看看他们的待办事项清单。" data-title="Here’s What Democrats Plan to Do With Their Power if They Win Back Congress" data-date="10-24 01:14" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 10-24 01:14</span>
      </div>
      <h2 class="hero-featured-title">以下是民主党人计划在赢回国会时如何利用他们的权力</h2>
      <div class="hero-featured-title-en">Here’s What Democrats Plan to Do With Their Power if They Win Back Congress</div>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.theverge.com/tech/1017600/google-personal-intelligence-privacy-policy-ads-update" target="_blank" rel="noopener" data-cat="keji" data-summary="谷歌更新了隐私政策，这意味着如果您使用个性化的人工智能功能，您将开始看到基于个人数据的定向广告。该更新由Android Authority发现，为其承诺增加了一个例外，即" data-title="Now Google says it might use your Gmail and Google Photos data to target ads" data-date="10-24 00:52" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">Now Google says it might use your Gmail and Google Photos data to target ads</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/2026/oct/23/premier-league-team-news-predicted-lineups" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="周六是切尔西东道主托特纳姆，周日中午12:30 ，曼联在老特拉福德面对伯恩茅斯。TNT Sports 1 Venue Villa Park继续阅读..." data-title="Premier League team news: predicted lineups for the weekend action" data-date="10-23 23:42" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Premier League team news: predicted lineups for the weekend action</p>
    </a>
    <a class="hero-sub-card" href="https://www.theverge.com/podcast/1017447/iphone-duo-ipad-review-score-vergecast" target="_blank" rel="noopener" data-cat="zonghe" data-summary="我们给了iPhone Duo 7/10分。但这并不总是我们计划的分数，它可能不会永远是正确的分数。这就是回顾和评估一个关于历史上最受欢迎的智能手机的大型新想法所面临的挑战。" data-title="The iPhone Duo should have been an iPad" data-date="10-24 01:00" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">The iPhone Duo should have been an iPad</p>
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
        <a class="news-item" href="https://www.nytimes.com/2026/10/23/us/politics/democratic-agenda.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="民主党一直致力于降低生活成本，并追究特朗普政府的责任。这是如果他们赢得大多数人的话，看看他们的待办事项清单。" data-title="Here’s What Democrats Plan to Do With Their Power if They Win Back Congress" data-date="10-24 01:14" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-24 01:14</span>
          <span class="news-item-title">以下是民主党人计划在赢回国会时如何利用他们的权力</span>
          <span class="news-item-title-en">Here’s What Democrats Plan to Do With Their Power if They Win Back Congress</span>
          <span class="news-value-point">💡 民主党一直致力于降低生活成本，并追究特朗普政府的责任</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/23/world/middleeast/west-bank-shooting-israel.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="以色列军方说，两名士兵和两名袭击者被打死，三名士兵受伤。以色列总理本雅明·内塔尼亚胡（ Benjamin Netanyahu ）发誓要在以色列占领的领土上发动重大攻势。" data-title="Palestinian Gunmen Open Fire on Israelis in the West Bank, Officials Say" data-date="10-24 01:11" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-24 01:11</span>
          <span class="news-item-title">官员说，巴勒斯坦枪手在约旦河西岸向以色列人开火</span>
          <span class="news-item-title-en">Palestinian Gunmen Open Fire on Israelis in the West Bank, Officials Say</span>
          <span class="news-value-point">💡 以色列军方说，两名士兵和两名袭击者被打死，三名士兵受伤</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-24/10720160.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社加德满都10月23日电 (记者 崔楠)尼泊尔救援人员23日在该国西北部山区发现两名此前失联的日本登山者遗体。" data-title="两名日本登山者在尼泊尔失联多日后遗体被发现" data-date="10-24 01:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 01:01</span>
          <span class="news-item-title">两名日本登山者在尼泊尔失联多日后遗体被发现</span>
          <span class="news-value-point">💡 中新社加德满都10月23日电 (记者 崔楠)尼泊尔救援人员23日在该国西北部山区发现两名此前失联的日本登山者遗体</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-24/10720159.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间23日，以军总参谋长扎米尔在约旦河西岸城市希伯伦附近的枪击事件现场表示，以军目前已在所有战线都进入最高戒备状态。他强调，鉴于即将进入以色列议会选举的敏感时期，以军将继续在各区域采取主动军事行动，以确保当地的安全与稳定。" data-title="以军总参谋长：已在所有战线进入最高戒备状态" data-date="10-24 00:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 00:20</span>
          <span class="news-item-title">以军总参谋长：已在所有战线进入最高戒备状态</span>
          <span class="news-value-point">💡 当地时间23日，以军总参谋长扎米尔在约旦河西岸城市希伯伦附近的枪击事件现场表示，以军目前已在所有战线都进入最高戒备状态</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-24/10720158.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="乌克兰总统泽连斯基23日表示，他已与美国总统特使威特科夫和女婿库什纳通话，与俄罗斯和美国方面举行会晤的计划安排在11月上半月。泽连斯基同时表示，乌方愿意在任何一天举行会晤。" data-title="泽连斯基确认乌美俄三方会谈将于11月上半月举行" data-date="10-24 00:19" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-24 00:19</span>
          <span class="news-item-title">泽连斯基确认乌美俄三方会谈将于11月上半月举行</span>
          <span class="news-value-point">💡 乌克兰总统泽连斯基23日表示，他已与美国总统特使威特科夫和女婿库什纳通话，与俄罗斯和美国方面举行会晤的计划安排在11月上半月</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/23/us/politics/florida-republicans-midterms-.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="特朗普总统将于周五在一个共和党州集会，民主党人将关注众议院的几场比赛。" data-title="Big Names Flock to Ruby-Red Florida to Sway Voters in Unexpectedly Close Contests" data-date="10-24 00:09" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-24 00:09</span>
          <span class="news-item-title">大牌涌向红宝石佛罗里达州，在意外收盘比赛中动摇选民</span>
          <span class="news-item-title-en">Big Names Flock to Ruby-Red Florida to Sway Voters in Unexpectedly Close Contests</span>
          <span class="news-value-point">💡 特朗普总统将于周五在一个共和党州集会，民主党人将关注众议院的几场比赛</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-23/10720148.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月23日电 (记者 李京泽)10月23日，“中国人民大学区域国别学院成立暨中国区域国别研究自主知识体系研究联盟启动与研讨会”在北京举办。会上，中国人民大学区域国别学院正式成立，中国区域国别学自主知识体系联盟同步启动。" data-title="中国人民大学区域国别学院正式成立" data-date="10-23 23:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 23:33</span>
          <span class="news-item-title">中国人民大学区域国别学院正式成立</span>
          <span class="news-value-point">💡 中新网北京10月23日电 (记者 李京泽)10月23日，“中国人民大学区域国别学院成立暨中国区域国别研究自主知识体系研究联盟启动与研讨会”在北京…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-23/10720143.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网伦敦10月23日电 (记者 欧阳开宇)第三届中英私立医疗会议日前在伦敦大英图书馆举行。活动汇聚中英政商、医疗及科技界代表，聚焦AI的规模化应用、监管与临床实践，探讨如何以技术创新改善医疗服务、惠及患者。" data-title="中英业内人士伦敦研讨医疗AI规模化应用" data-date="10-23 23:18" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 23:18</span>
          <span class="news-item-title">中英业内人士伦敦研讨医疗AI规模化应用</span>
          <span class="news-value-point">💡 中新网伦敦10月23日电 (记者 欧阳开宇)第三届中英私立医疗会议日前在伦敦大英图书馆举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-23/10720141.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社首尔10月23日电 (记者 金旭)当地时间23日，韩国首尔高等法院针对首尔市长吴世勋涉嫌违反《政治资金法》案作出二审判决，判处吴世勋无罪。" data-title="韩国首尔市长吴世勋二审被判无罪" data-date="10-23 23:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 23:04</span>
          <span class="news-item-title">韩国首尔市长吴世勋二审被判无罪</span>
          <span class="news-value-point">💡 中新社首尔10月23日电 (记者 金旭)当地时间23日，韩国首尔高等法院针对首尔市长吴世勋涉嫌违反《政治资金法》案作出二审判决，判处吴世勋无罪</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-23/10720139.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社布鲁塞尔10月23日电 (记者 德永健)在也门军事冲突持续升级之际，欧盟23日宣布向也门追加2250万欧元人道主义援助，用于应对当地日益增加的人道主义需求。" data-title="欧盟向也门追加2250万欧元人道主义援助" data-date="10-23 23:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 23:02</span>
          <span class="news-item-title">欧盟向也门追加2250万欧元人道主义援助</span>
          <span class="news-value-point">💡 中新社布鲁塞尔10月23日电 (记者 德永健)在也门军事冲突持续升级之际，欧盟23日宣布向也门追加2250万欧元人道主义援助，用于应对当地日益增…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-23/10720094.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社河北雄安10月23日电 (记者 曾玥 周昕)10月23日，中共中央政治局委员、外交部长王毅在河北雄安新区会见来华出席2026全球治理论坛(雄安)的美国亚洲协会董事会共同主席桑顿和《纽约时报》专栏作家弗里德曼。" data-title="王毅会见美国亚洲协会董事会共同主席桑顿、《纽约时报》专栏作家弗里德曼" data-date="10-23 22:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 22:27</span>
          <span class="news-item-title">王毅会见美国亚洲协会董事会共同主席桑顿、《纽约时报》专栏作家弗里德曼</span>
          <span class="news-value-point">💡 中新社河北雄安10月23日电 (记者 曾玥 周昕)10月23日，中共中央政治局委员、外交部长王毅在河北雄安新区会见来华出席2026全球治理论坛(…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-23/10720096.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社首尔10月23日电 (记者 金旭)韩国国防部23日正式向朝鲜提议举行韩朝军方会谈，就相互确认韩朝陆地军事分界线的准确位置、恢复军事通信线路以及防止边境地区发生意外冲突的方案进行协商。" data-title="韩国国防部向朝鲜提议举行韩朝军方会谈" data-date="10-23 22:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 22:10</span>
          <span class="news-item-title">韩国国防部向朝鲜提议举行韩朝军方会谈</span>
          <span class="news-value-point">💡 中新社首尔10月23日电 (记者 金旭)韩国国防部23日正式向朝鲜提议举行韩朝军方会谈，就相互确认韩朝陆地军事分界线的准确位置、恢复军事通信线路…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-23/10720100.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社天津10月23日电 (孙翼飞)台湾退役海军少校、前“新江舰”舰长吕礼诗23日到天津天后宫参访。在宫内祈福牌上，他写下“两岸大家、小家团聚”的心愿。" data-title="台湾退役海军少校吕礼诗天津寻根：愿两岸大家小家皆团聚" data-date="10-23 22:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 22:03</span>
          <span class="news-item-title">台湾退役海军少校吕礼诗天津寻根：愿两岸大家小家皆团聚</span>
          <span class="news-value-point">💡 中新社天津10月23日电 (孙翼飞)台湾退役海军少校、前“新江舰”舰长吕礼诗23日到天津天后宫参访</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-23/10720023.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="历史长河奔腾不息，精神坐标巍然矗立。" data-title="第一观察｜党和人民军队铿锵前进的制胜之道" data-date="10-23 21:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 21:35</span>
          <span class="news-item-title">第一观察｜党和人民军队铿锵前进的制胜之道</span>
          <span class="news-value-point">💡 历史长河奔腾不息，精神坐标巍然矗立</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-23/10720050.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网广西钦州10月23日电 题：台胞畅游平陆运河：百年构想终成“通江达海”实景" data-title="台胞畅游平陆运河：百年构想终成“通江达海”实景" data-date="10-23 21:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 21:16</span>
          <span class="news-item-title">台胞畅游平陆运河：百年构想终成“通江达海”实景</span>
          <span class="news-value-point">💡 中新网广西钦州10月23日电 题：台胞畅游平陆运河：百年构想终成“通江达海”实景</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theverge.com/tech/1017600/google-personal-intelligence-privacy-policy-ads-update" target="_blank" rel="noopener" data-cat="keji" data-summary="谷歌更新了隐私政策，这意味着如果您使用个性化的人工智能功能，您将开始看到基于个人数据的定向广告。该更新由Android Authority发现，为其承诺增加了一个例外，即" data-title="Now Google says it might use your Gmail and Google Photos data to target ads" data-date="10-24 00:52" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-24 00:52</span>
          <span class="news-item-title">现在，谷歌表示可能会使用您的Gmail和Google相册数据来定位广告</span>
          <span class="news-item-title-en">Now Google says it might use your Gmail and Google Photos data to target ads</span>
          <span class="news-value-point">💡 谷歌更新了隐私政策，这意味着如果您使用个性化的人工智能功能，您将开始看到基于个人数据的定向广告</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-23/10720155.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网阿斯塔纳10月23日电 (记者 单璐)哈萨克斯坦拥有丰富的能源储备，如何利用这一优势发展人工智能？英伟达创始人兼首席执行官黄仁勋23日在哈萨克斯坦首都阿斯塔纳表示，能源是发展人工智能的重要基础，但要将这一优势转化为产业发展动力，还需要在算力基础设施建设、人才培养、技术应用等方面持续发力。" data-title="黄仁勋在哈萨克斯坦谈AI发展：能源与人才成关键词" data-date="10-23 23:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 23:44</span>
          <span class="news-item-title">黄仁勋在哈萨克斯坦谈AI发展：能源与人才成关键词</span>
          <span class="news-value-point">💡 中新网阿斯塔纳10月23日电 (记者 单璐)哈萨克斯坦拥有丰富的能源储备，如何利用这一优势发展人工智能</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/ssds/microns-next-generation-3d-nand-to-double-bit-density-with-over-400-layers-offering-extreme-performance-g11-3d-nand-promises-42-gb-mm2-and-5-400-mt-s-interface-speed" target="_blank" rel="noopener" data-cat="keji" data-summary="美光的G11 3D NAND承诺42 Gb/mm2和5,400 MT/s的接口速度，使SSD具有极高的容量和性能。" data-title="Micron&#39;s next-generation 3D NAND to double bit density with over 400 layers, offering extreme performance" data-date="10-23 23:32" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-23 23:32</span>
          <span class="news-item-title">美光的下一代3D NAND具有超过400层的双比特密度，可提供极致的性能</span>
          <span class="news-item-title-en">Micron's next-generation 3D NAND to double bit density with over 400 layers, offering extreme performance</span>
          <span class="news-value-point">💡 美光的G11 3D NAND承诺42 Gb/mm2和5,400 MT/s的接口速度，使SSD具有极高的容量和性能</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/ssds/solidigm-confirms-plans-to-build-a-fab-in-the-us-abandons-ipo-plans-unfavorable-stock-market-conditions-and-semiconductor-share-price-trends-reasons-given" target="_blank" rel="noopener" data-cat="keji" data-summary="SK海力士放弃Solidigm的IPO计划，确认计划在美国建造Solidigm 3D NAND晶圆厂" data-title="Solidigm confirms plans to build a fab in the US, abandons IPO plans" data-date="10-23 23:21" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-23 23:21</span>
          <span class="news-item-title">Solidigm确认在美国建造晶圆厂的计划，放弃IPO计划</span>
          <span class="news-item-title-en">Solidigm confirms plans to build a fab in the US, abandons IPO plans</span>
          <span class="news-value-point">💡 SK海力士放弃Solidigm的IPO计划，确认计划在美国建造Solidigm 3D NAND晶圆厂</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/motherboards/gigabyte-z890m-aorus-elite-wifi7-motherboard-review" target="_blank" rel="noopener" data-cat="keji" data-summary="$ 209 Gigabyte Z890M Aorus Elite Wifi 7 Ice是外观更好看的Micro ATX板之一，具有冰白色美学和全散热器覆盖，为白色主题的英特尔构建提供高级氛围。" data-title="Gigabyte Z890M Aorus Elite WiFi7 Motherboard Review: Icy-white SFF board offers full-size features for Intel" data-date="10-23 23:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-23 23:00</span>
          <span class="news-item-title">技嘉Z890M Aorus Elite WiFi7主板评论：冰白色SFF主板为英特尔提供全尺寸功能</span>
          <span class="news-item-title-en">Gigabyte Z890M Aorus Elite WiFi7 Motherboard Review: Icy-white SFF board offers full-size features for Intel</span>
          <span class="news-value-point">💡 $ 209 Gigabyte Z890M Aorus Elite Wifi 7 Ice是外观更好看的Micro ATX板之一，具有冰白色美学和全…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1017450/meta-business-terms-delayed-ai-scraping" target="_blank" rel="noopener" data-cat="keji" data-summary="正如Fast Company早些时候报道的那样，在发布商表示担心他们可能允许该公司抓取新闻网站进行人工智能培训之后， Meta正在推迟其新业务条款的执行。在给The Verge的一份声明中， Meta发言人Da" data-title="Meta delays new business terms after publisher pushback on AI scraping" data-date="10-23 22:47" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-23 22:47</span>
          <span class="news-item-title">在发布商拒绝人工智能抓取后， Meta推迟了新的商业条款</span>
          <span class="news-item-title-en">Meta delays new business terms after publisher pushback on AI scraping</span>
          <span class="news-value-point">💡 正如Fast Company早些时候报道的那样，在发布商表示担心他们可能允许该公司抓取新闻网站进行人工智能培训之后， Meta正在推迟其新业务条…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/274.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 23 日消息，OpenAI 联合 PerturbAI 和斯克里普斯研究所（Scripps Research），利用数千个 AI 智能体分析数百万个小鼠脑细胞的生物学数据，整个分析过程仅耗时 32 分钟。研究团队估计，如果由人类研究人员逐项分析实验结果并检索相关文献，完成同等工作可能需要数月到一年。根据 OpenAI 10 月 21 日发布的介绍，这项研究使用了专为生命科学研究设计的 GPT-Rosalind 模型，分析一份覆盖整个小鼠大脑的 CRISPR 图谱。该图谱记录了不同基因受到干预后，各类脑细胞产生的变化，有助于研究人员了解基因功能及其与疾病之间的潜在联系。研究团队采用分布式 AI 智能体架构，将大量分析任务拆分后并行执行。每个智能体负责研究一种基因干预，分析相关" data-title="OpenAI 联合研究机构部署数千个 AI 智能体：32 分钟分析数百万个小鼠脑细胞，相当于人类数月时间" data-date="10-23 22:43" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-23 22:43</span>
          <span class="news-item-title">OpenAI 联合研究机构部署数千个 AI 智能体：32 分钟分析数百万个小鼠脑细胞，相当于人类数月时间</span>
          <span class="news-value-point">💡 IT之家 10 月 23 日消息，OpenAI 联合 PerturbAI 和斯克里普斯研究所（Scripps Research），利用数千个 A…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/amazon-bows-to-local-backlash-over-ai-data-centers-scraps-plans-to-build-four-new-facilities-in-northern-virginia-site-to-be-repurposed-for-mixed-use-and-residential-development" target="_blank" rel="noopener" data-cat="keji" data-summary="在当地居民和官员的强烈抗议下，亚马逊放弃了在弗吉尼亚州北部劳登县建造四个新数据中心的计划。现在，这片土地将被重新用于混合和住宅用途。" data-title="Amazon bows to local backlash over AI data centers, scraps plans to build four new facilities in Northern Virginia" data-date="10-23 21:36" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-23 21:36</span>
          <span class="news-item-title">亚马逊屈服于当地对人工智能数据中心的强烈反对，取消了在弗吉尼亚州北部建造四个新设施的计划</span>
          <span class="news-item-title-en">Amazon bows to local backlash over AI data centers, scraps plans to build four new facilities in Northern Virginia</span>
          <span class="news-value-point">💡 在当地居民和官员的强烈抗议下，亚马逊放弃了在弗吉尼亚州北部劳登县建造四个新数据中心的计划</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/china-can-make-advanced-chips-without-euv-but-the-bill-keeps-growing-duv-multiple-patterning-means-bigger-dies-lower-yields-and-longer-manufacturing-times" target="_blank" rel="noopener" data-cat="keji" data-summary="中国已经将旧的DUV光刻技术延伸到比预期更远的地方，使用多重图案来接近没有EUV的5nm级。但专家表示，成本、产量和模具尺寸的折衷意味着在经济上不太可能取得进一步的进步vi" data-title="China can make advanced chips without EUV, but the bill keeps growing" data-date="10-23 21:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-23 21:30</span>
          <span class="news-item-title">中国可以在没有EUV的情况下制造先进的芯片，但该法案仍在不断增长</span>
          <span class="news-item-title-en">China can make advanced chips without EUV, but the bill keeps growing</span>
          <span class="news-value-point">💡 中国已经将旧的DUV光刻技术延伸到比预期更远的地方，使用多重图案来接近没有EUV的5nm级</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c370pr45nelgo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="人工智能发现了长期未被察觉的程式漏洞，引发全球罕见的大规模网络安全应对行动。" data-title="PHP是什么？为何它引发全球网络安全危机？" data-date="10-23 16:09" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-23 16:09</span>
          <span class="news-item-title">PHP是什么？为何它引发全球网络安全危机？</span>
          <span class="news-value-point">💡 人工智能发现了长期未被察觉的程式漏洞，引发全球罕见的大规模网络安全应对行动</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/504901.html" target="_blank" rel="noopener" data-cat="keji" data-summary="10月21日，百度官方公众号发文披露了百度世界2026分论坛的更多议程信息。" data-title="百度世界2026前瞻：10+重磅分论坛，全面解码AI时代的智能组织进化路径" data-date="10-23 15:35" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-23 15:35</span>
          <span class="news-item-title">百度世界2026前瞻：10+重磅分论坛，全面解码AI时代的智能组织进化路径</span>
          <span class="news-value-point">💡 10月21日，百度官方公众号发文披露了百度世界2026分论坛的更多议程信息</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/22/uber-rival-indrive-eyes-2027-robotaxi-tests-in-central-asia-with-pony-ai-and-nvidia/" target="_blank" rel="noopener" data-cat="keji" data-summary="该公司计划于2027年上半年在哈萨克斯坦首都开始测试Pony.ai的机器人出租车。" data-title="Uber rival inDrive eyes 2027 robotaxi tests in Central Asia with Pony AI and Nvidia" data-date="10-23 12:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-23 12:00</span>
          <span class="news-item-title">优步的竞争对手inDrive Eyes 2027在中亚通过Pony AI和Nvidia进行机器人出租车测试</span>
          <span class="news-item-title-en">Uber rival inDrive eyes 2027 robotaxi tests in Central Asia with Pony AI and Nvidia</span>
          <span class="news-value-point">💡 该公司计划于2027年上半年在哈萨克斯坦首都开始测试Pony.ai的机器人出租车</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/22/left-alone-with-nothing-to-do-ai-agents-started-playing/" target="_blank" rel="noopener" data-cat="keji" data-summary="麻省理工学院的研究人员在一个虚拟岛屿上放逐了13个人工智能，他们通过发明游戏，哀悼丢失的戒指，最终在工作中变得更好。" data-title="Left alone with nothing to do, AI agents started playing" data-date="10-23 08:45" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-23 08:45</span>
          <span class="news-item-title">独自一人无事可做，人工智能特工开始玩</span>
          <span class="news-item-title-en">Left alone with nothing to do, AI agents started playing</span>
          <span class="news-value-point">💡 麻省理工学院的研究人员在一个虚拟岛屿上放逐了13个人工智能，他们通过发明游戏，哀悼丢失的戒指，最终在工作中变得更好</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/22/openai-working-on-new-30b-raise-at-1-25t-valuation-ahead-of-ipo/" target="_blank" rel="noopener" data-cat="keji" data-summary="如果OpenAI在这轮融资中获得超过1万亿美元的估值，它将打破有史以来估值最高的私人公司的纪录。" data-title="OpenAI working on new $30B raise at $1.25T valuation ahead of IPO" data-date="10-23 06:08" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-23 06:08</span>
          <span class="news-item-title">OpenAI在IPO之前以$ 1.25 T的估值进行新的$ 300亿加息</span>
          <span class="news-item-title-en">OpenAI working on new $30B raise at $1.25T valuation ahead of IPO</span>
          <span class="news-value-point">💡 如果OpenAI在这轮融资中获得超过1万亿美元的估值，它将打破有史以来估值最高的私人公司的纪录</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/22/1password-launches-a-way-for-ai-agents-to-log-in-on-your-behalf-without-seeing-your-password/" target="_blank" rel="noopener" data-cat="keji" data-summary="新功能允许客服代表登录客户的个人账号，同时保护用于保护这些账号的私人凭据。" data-title="1Password launches a way for AI agents to log in on your behalf without seeing your password" data-date="10-23 03:07" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-23 03:07</span>
          <span class="news-item-title">1Password为AI代理推出了一种无需查看密码即可代您登录的方式</span>
          <span class="news-item-title-en">1Password launches a way for AI agents to log in on your behalf without seeing your password</span>
          <span class="news-value-point">💡 新功能允许客服代表登录客户的个人账号，同时保护用于保护这些账号的私人凭据</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">8 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/23/premier-league-team-news-predicted-lineups" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="周六是切尔西东道主托特纳姆，周日中午12:30 ，曼联在老特拉福德面对伯恩茅斯。TNT Sports 1 Venue Villa Park继续阅读..." data-title="Premier League team news: predicted lineups for the weekend action" data-date="10-23 23:42" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-23 23:42</span>
          <span class="news-item-title">英超球队新闻：周末动作的预测阵容</span>
          <span class="news-item-title-en">Premier League team news: predicted lineups for the weekend action</span>
          <span class="news-value-point">💡 周六是切尔西东道主托特纳姆，周日中午12:30 ，曼联在老特拉福德面对伯恩茅斯</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmwyql6v5q82o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳前锋布卡约·萨卡（ Bukayo Saka ）在对拜仁慕尼黑的比赛中受伤，可能会缺阵长达八周。" data-title="Arsenal fear Saka could be out for two months" data-date="10-23 22:09" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-23 22:09</span>
          <span class="news-item-title">阿森纳担心萨卡可能会缺席两个月</span>
          <span class="news-item-title-en">Arsenal fear Saka could be out for two months</span>
          <span class="news-value-point">💡 阿森纳前锋布卡约·萨卡（ Bukayo Saka ）在对拜仁慕尼黑的比赛中受伤，可能会缺阵长达八周</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cq78pv0073dlo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）在媒体简报会上发表了五分钟不间断的讲话，概述了曼联对他的意义，然后拒绝排除放弃布鲁诺·费尔南德斯（ Bruno Fernandes ）的可能性。" data-title="Carrick refuses to rule out dropping Fernandes in emotional address" data-date="10-23 21:55" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-23 21:55</span>
          <span class="news-item-title">卡里克拒绝排除在情感地址中放弃费尔南德斯</span>
          <span class="news-item-title-en">Carrick refuses to rule out dropping Fernandes in emotional address</span>
          <span class="news-value-point">💡 迈克尔·卡里克（ Michael Carrick ）在媒体简报会上发表了五分钟不间断的讲话，概述了曼联对他的意义，然后拒绝排除放弃布鲁诺·费尔南…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/23/crystal-palace-and-newcastle-face-off-with-both-in-search-of-season-kickstart" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="皮埃尔·塞奇（ Pierre Sage ）和马蒂亚斯·贾斯勒（ Matthias Jaissle ）面临着一些关键问题：两人都在今年夏天被任命，但成绩和结果都被证明是难以捉摸的在七场英超联赛中承认17个进球并不完全是皮埃尔·塞奇或水晶宫的等级制度的开始" data-title="Crystal Palace and Newcastle face off with both in search of season kickstart" data-date="10-23 21:36" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-23 21:36</span>
          <span class="news-item-title">水晶宫和纽卡斯尔对决，寻找赛季开局</span>
          <span class="news-item-title-en">Crystal Palace and Newcastle face off with both in search of season kickstart</span>
          <span class="news-value-point">💡 皮埃尔·塞奇（ Pierre Sage ）和马蒂亚斯·贾斯勒（ Matthias Jaissle ）面临着一些关键问题：两人都在今年夏天被任命，…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmvg6j8jezn7o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="安东尼奥·孔蒂（ Antonio Conte ）表示，他没有与任何俱乐部进行高级谈判，以回应他与曼联进行谈判的猜测。" data-title="Conte plays down &#39;unfounded&#39; Man Utd speculation" data-date="10-23 20:15" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-23 20:15</span>
          <span class="news-item-title">孔蒂淡化了“毫无根据”的曼联猜测</span>
          <span class="news-item-title-en">Conte plays down 'unfounded' Man Utd speculation</span>
          <span class="news-value-point">💡 安东尼奥·孔蒂（ Antonio Conte ）表示，他没有与任何俱乐部进行高级谈判，以回应他与曼联进行谈判的猜测</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cwg7xvz8e8dpo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="首席足球作家菲尔·麦克纳尔蒂（ Phil McNulty ）表示， Unai Emery令人印象深刻的2.0重启让阿斯顿维拉的粉丝们在任命四周年之际情绪高涨。" data-title="Emery&#39;s Villa 2.0 reboot restores optimism before Man City meeting" data-date="10-23 19:23" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-23 19:23</span>
          <span class="news-item-title">Emery的别墅2.0重启在曼城会议之前恢复了乐观情绪</span>
          <span class="news-item-title-en">Emery's Villa 2.0 reboot restores optimism before Man City meeting</span>
          <span class="news-value-point">💡 首席足球作家菲尔·麦克纳尔蒂（ Phil McNulty ）表示， Unai Emery令人印象深刻的2.0重启让阿斯顿维拉的粉丝们在任命四周年…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cw3djpg15045o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="诺丁汉森林队在英超联赛中排名倒数三，但老板奥利弗·格拉斯纳（ Oliver Glasner ）认为他们本赛季应该得到更多。" data-title="Forest&#39;s start raises questions - but belief in Glasner remains" data-date="10-23 16:14" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-23 16:14</span>
          <span class="news-item-title">森林的开始引发了疑问-但对格拉斯纳的信念仍然存在</span>
          <span class="news-item-title-en">Forest's start raises questions - but belief in Glasner remains</span>
          <span class="news-value-point">💡 诺丁汉森林队在英超联赛中排名倒数三，但老板奥利弗·格拉斯纳（ Oliver Glasner ）认为他们本赛季应该得到更多</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/23/premier-league-10-things-to-look-out-for-this-weekend" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="马克斯·道曼可能有机会，马刺需要在斯坦福桥找到平衡，阿克塞尔·迪萨西必须做出弥补英超联赛得分王经过七场比赛，诺丁汉森林的记录与上赛季惊人地相似：五分，五个进球。是的" data-title="Premier League: 10 things to look out for this weekend" data-date="10-23 07:01" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-23 07:01</span>
          <span class="news-item-title">英超联赛：本周末需要注意的10件事</span>
          <span class="news-item-title-en">Premier League: 10 things to look out for this weekend</span>
          <span class="news-value-point">💡 马克斯·道曼可能有机会，马刺需要在斯坦福桥找到平衡，阿克塞尔·迪萨西必须做出弥补英超联赛得分王经过七场比赛，诺丁汉森林的记录与上赛季惊人地相似：…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theverge.com/podcast/1017447/iphone-duo-ipad-review-score-vergecast" target="_blank" rel="noopener" data-cat="zonghe" data-summary="我们给了iPhone Duo 7/10分。但这并不总是我们计划的分数，它可能不会永远是正确的分数。这就是回顾和评估一个关于历史上最受欢迎的智能手机的大型新想法所面临的挑战。" data-title="The iPhone Duo should have been an iPad" data-date="10-24 01:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-24 01:00</span>
          <span class="news-item-title">IPhone Duo应该是iPad</span>
          <span class="news-item-title-en">The iPhone Duo should have been an iPad</span>
          <span class="news-value-point">💡 我们给了iPhone Duo 7/10分</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/23/world/middleeast/west-bank-settlers-palestinians-harvest.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="今年在以色列占领的约旦河西岸收获的橄榄是多年来最暴力的，因为定居者袭击了农民和被围困的房屋，引起了美国官员和其他人的谴责。" data-title="Israeli Settlers Turn a Palestinian Rite Into a Gantlet of Violence and Fear" data-date="10-24 00:47" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-24 00:47</span>
          <span class="news-item-title">以色列定居者将巴勒斯坦仪式转变为暴力和恐惧</span>
          <span class="news-item-title-en">Israeli Settlers Turn a Palestinian Rite Into a Gantlet of Violence and Fear</span>
          <span class="news-value-point">💡 今年在以色列占领的约旦河西岸收获的橄榄是多年来最暴力的，因为定居者袭击了农民和被围困的房屋，引起了美国官员和其他人的谴责</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1017623/iphone-duo-broken-cracked-screen" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IPhone Duo今天正式发售，但有几台屏幕已经坏了。根据Reddit上有关受影响单位的帖子，该问题似乎发生在所有受影响单位的类似位置：" data-title="The first broken iPhone Duos are here" data-date="10-24 00:37" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-24 00:37</span>
          <span class="news-item-title">首款破损的iPhone Duo现已推出</span>
          <span class="news-item-title-en">The first broken iPhone Duos are here</span>
          <span class="news-value-point">💡 IPhone Duo今天正式发售，但有几台屏幕已经坏了</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/peripherals/gaming-mice/razer-basilisk-v4-pro-review" target="_blank" rel="noopener" data-cat="zonghe" data-summary="雷蛇的Basilisk V4 Pro游戏鼠标具有符合人体工程学的外形、更轻的重量和几个额外的按钮，以及雷蛇的Focus Pro 50K光学传感器。" data-title="Razer Basilisk V4 Pro Review: Tried and true and now with AI" data-date="10-24 00:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-24 00:00</span>
          <span class="news-item-title">Razer Basilisk V4 Pro评论：尝试和真实，现在使用AI</span>
          <span class="news-item-title-en">Razer Basilisk V4 Pro Review: Tried and true and now with AI</span>
          <span class="news-value-point">💡 雷蛇的Basilisk V4 Pro游戏鼠标具有符合人体工程学的外形、更轻的重量和几个额外的按钮，以及雷蛇的Focus Pro 50K光学传感器</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-23/10720153.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网上海10月23日电 (蒋小威)2026年上海市女农人庆丰收主题活动23日在金山区廊下镇友好村举行。活动现场设有女性社会组织市集、“金山游礼”巾帼好物后备箱市集、稻田T台秀、游园体验、萌宠互动等环节。女农人、女企业家、驻村书记等带来特色产品，摊位前人头攒动。稻田边，女农人、女企业家、女大学生等身着旗袍、羊绒服饰登台走秀，在田间展示风采。" data-title="上海举行女农人庆丰收活动 巾帼好物市集搬进田间" data-date="10-23 23:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 23:43</span>
          <span class="news-item-title">上海举行女农人庆丰收活动 巾帼好物市集搬进田间</span>
          <span class="news-value-point">💡 中新网上海10月23日电 (蒋小威)2026年上海市女农人庆丰收主题活动23日在金山区廊下镇友好村举行</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/278.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 23 日消息，由于把“110”设成紧急联系人，浙江一男子醉驾后，车辆发现异常上报给车企紧急救援中心并自动报警，后续被民警当场查获。该男子显然不服，并辩称这属于自首。那么，这类车机触发的报警，法律上到底能不能认定为自首？据央视《法治在线》今日报道，这类新型醉驾案在法律上不能被认定为自首。车辆紧急救援系统自动拨出的报警电话，不能替驾驶人完成“自动投案”。此次事件发生于 2026 年 3 月 19 日晚，周某酒后驾驶一辆小型普通客车返回家中，途中开启车辆驾驶辅助功能，后因酒劲上头困意难忍而选择在路边停车，随后在驾驶位昏睡起来。但此时车辆仍处于启动状态，车企紧急救援中心监测到车辆长时间无人接管、多次呼叫驾驶人无应答后，按照应急处置流程拨打了周某预设的紧急联系人电话 ——110。民" data-title="男子醉酒后车机自动报警被判不构成自首：系统可以替你报警但不能替你自首" data-date="10-23 23:41" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-23 23:41</span>
          <span class="news-item-title">男子醉酒后车机自动报警被判不构成自首：系统可以替你报警但不能替你自首</span>
          <span class="news-value-point">💡 IT之家 10 月 23 日消息，由于把“110”设成紧急联系人，浙江一男子醉驾后，车辆发现异常上报给车企紧急救援中心并自动报警，后续被民警当场…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-23/10720149.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网拉萨10月23日电(白玛玉珍)10月22日22时33分，西藏自治区那曲市巴青县发生7.0级地震，震源深度10千米，造成重大人员伤亡。震区平均海拔接近4800米，夜间气温低，民众安置和防寒保暖成为震后最紧迫的民生任务之一。" data-title="中国电建成都院驰援西藏巴青抗震救灾 调运40套板房100套取暖器" data-date="10-23 23:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 23:35</span>
          <span class="news-item-title">中国电建成都院驰援西藏巴青抗震救灾 调运40套板房100套取暖器</span>
          <span class="news-value-point">💡 中新网拉萨10月23日电(白玛玉珍)10月22日22时33分，西藏自治区那曲市巴青县发生7.0级地震，震源深度10千米，造成重大人员伤亡</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-23/10720145.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网湖北宜都10月23日电 题：湖北宜昌：“电化长江”从蓝图照进现实" data-title="湖北宜昌：“电化长江” 从蓝图照进现实" data-date="10-23 23:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 23:30</span>
          <span class="news-item-title">湖北宜昌：“电化长江” 从蓝图照进现实</span>
          <span class="news-value-point">💡 中新网湖北宜都10月23日电 题：湖北宜昌：“电化长江”从蓝图照进现实</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/transportation/1017435/nhtsa-autonomous-vehicle-cyan-lighting-fmvss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="经过多年的辩论，无人驾驶汽车应该如何告诉世界没有人在车轮上-闪烁文本，音频警报，定制灯-联邦调查局刚刚介入了一个答案：青色。美国国家公路交通安全管理局发布了" data-title="Feds want robotaxis to signal ‘I’m driving’ with cyan" data-date="10-23 23:24" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-23 23:24</span>
          <span class="news-item-title">联邦调查局希望机器人出租车用青色表示“我在开车”</span>
          <span class="news-item-title-en">Feds want robotaxis to signal ‘I’m driving’ with cyan</span>
          <span class="news-value-point">💡 经过多年的辩论，无人驾驶汽车应该如何告诉世界没有人在车轮上-闪烁文本，音频警报，定制灯-联邦调查局刚刚介入了一个答案：青色</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-23/10720110.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网10月23日电 当地时间10月21日，《生物多样性公约》第十七次缔约方大会(COP17)中国角系列活动之一“保护生物多样性 尊重多元文化 践行多边主义”主题边会在亚美尼亚埃里温举行。" data-title="COP17中国角主题边会举行，呼吁携手应对生物多样性丧失挑战" data-date="10-23 23:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 23:21</span>
          <span class="news-item-title">COP17中国角主题边会举行，呼吁携手应对生物多样性丧失挑战</span>
          <span class="news-value-point">💡 中新网10月23日电 当地时间10月21日，《生物多样性公约》第十七次缔约方大会(COP17)中国角系列活动之一“保护生物多样性 尊重多元文化 …</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/277.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 23 日消息，长城汽车今日宣布魏牌二代蓝山全球首秀定档 10 月 27 日。新车采用方盒子设计，搭载由 2.0T 发动机组成的 Hi-4 插电混动系统。据介绍，魏牌二代蓝山主打“东方豪华”，尺寸为 5300×2050×1960mm、轴距 3010mm，轮胎规格 275/50 R21。新车搭载 2.0T 混动专用发动机，匹配 4 挡混动专用变速箱，电机功率为前 110kW、后 220kW，内置 66.6kWh（1/3C）电池。IT之家注意到，官方公布了该车的曜石黑、浅蓝外观配色，新车也已经在工信部完成申报。其尺寸为 5300×2050×1960mm、轴距 3010mm，轮胎规格 275/50 R21。新车正面配备直瀑式镀铬格栅，前大灯是复古风的圆形设计，尾部印有“蓝山”标识" data-title="长城魏牌二代蓝山全球首秀定档 10 月 27 日，搭载 Hi" data-date="10-23 23:20" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-23 23:20</span>
          <span class="news-item-title">长城魏牌二代蓝山全球首秀定档 10 月 27 日，搭载 Hi</span>
          <span class="news-value-point">💡 IT之家 10 月 23 日消息，长城汽车今日宣布魏牌二代蓝山全球首秀定档 10 月 27 日</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-23/10720142.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网长春10月23日电 题：全国“十佳环卫人”高茹：32年环卫路，一叶见初心" data-title="全国“十佳环卫人”高茹：32年环卫路，一叶见初心" data-date="10-23 23:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 23:17</span>
          <span class="news-item-title">全国“十佳环卫人”高茹：32年环卫路，一叶见初心</span>
          <span class="news-value-point">💡 中新网长春10月23日电 题：全国“十佳环卫人”高茹：32年环卫路，一叶见初心</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/science/1017477/spacex-cell-sites-major-us-carrier" target="_blank" rel="noopener" data-cat="zonghe" data-summary="根据彭博社的一份报告， SpaceX计划访问至少8万个基站，作为与Verizon、T-Mobile和AT&amp;T直接竞争的努力的一部分。消息人士告诉该出版物， SpaceX正在与皇冠城堡公司（ Crown Castle Inc. ）进行谈判，该公司是" data-title="SpaceX’s mobile carrier push reportedly involves tapping into 80,000 cell sites" data-date="10-23 23:16" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-23 23:16</span>
          <span class="news-item-title">据报道， SpaceX的移动运营商推动涉及利用80,000个蜂窝站点</span>
          <span class="news-item-title-en">SpaceX’s mobile carrier push reportedly involves tapping into 80,000 cell sites</span>
          <span class="news-value-point">💡 根据彭博社的一份报告， SpaceX计划访问至少8万个基站，作为与Verizon、T-Mobile和AT&T直接竞争的努力的一部分</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/017/276.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 23 日消息，据新浪科技报道，随着苹果首款折叠屏手机 iPhone Duo 发售，目前苹果在全国所有 Apple Store 零售店均安排了中国移动、中国联通和中国电信的工作人员，为顾客现场办理 eSIM 激活业务。据报道，只要顾客是在苹果 Apple Store 门店现场取货，就可以在店内由运营商工作人员协助办理相关业务，免去以往购机后再单独前往运营商营业厅开通的环节。IT之家注意到，今天移动还发布公告，透露官方将持续推动 eSIM 线上自助办理能力上线，进一步拓宽办理路径，持续降低 eSIM 业务的使用门槛。" data-title="消息称苹果在全国 Apple Store 安排移动 / 联通 / 电信工作人员坐镇，现场为 iPhone Duo 取货顾客办理 eSIM" data-date="10-23 23:05" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-23 23:05</span>
          <span class="news-item-title">消息称苹果在全国 Apple Store 安排移动 / 联通 / 电信工作人员坐镇，现场为 iPhone Duo 取货顾客办理 eSIM</span>
          <span class="news-value-point">💡 IT之家 10 月 23 日消息，据新浪科技报道，随着苹果首款折叠屏手机 iPhone Duo 发售，目前苹果在全国所有 Apple Store…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-23/10720138.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网三亚10月23日电 题：给水稻写一本带照片的“成长日记”：科技赋能南繁育种" data-title="（活力中国调研行）给水稻写一本带照片的“成长日记”：科技赋能南繁育种" data-date="10-23 23:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-23 23:05</span>
          <span class="news-item-title">（活力中国调研行）给水稻写一本带照片的“成长日记”：科技赋能南繁育种</span>
          <span class="news-value-point">💡 中新网三亚10月23日电 题：给水稻写一本带照片的“成长日记”：科技赋能南繁育种</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-24 01:19（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
