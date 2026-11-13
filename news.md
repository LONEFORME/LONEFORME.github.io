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
      <span>2026-11-13 16:51 抓取更新</span>
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
        <span class="channel-count">57</span>
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
        <span class="channel-count">10</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('zonghe', this)">
        <span>📰 综合与社会</span>
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('meimei', this)">
        <span>🌍 西方媒体视角</span>
        <span class="channel-count">2</span>
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
  <div class="ov-item"><span class="ov-num">57</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×19 · 天空体育×12</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gj/2026/11-13/10731548.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网伊斯坦布尔11月13日电(魏园 王高飞 吴辛茹)“在气候协作与伙伴关系当中，全球南方国家必须成为共建者。”联合国环境规划署(UNEP)臭氧行动处前处长拉杰德拉·山地(Rajendra Shende)表示，全球南方国家应构建重在落地的伙伴关系，切实把气候承诺转化为行动成果。" data-title="联合国环境规划署前官员：“全球南方接受气候援助”这一认知已过时，期待携手推动气候治理｜新闻会客厅" data-date="11-13 16:36" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 11-13 16:36</span>
      </div>
      <h2 class="hero-featured-title">联合国环境规划署前官员：“全球南方接受气候援助”这一认知已过时，期待携手推动气候治理｜新闻会客厅</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/gn/2026/11-13/10731540.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网北京11月13日电 (记者 孙自法)大脑中的导航系统是如何实时对手部等肢体运动进行定位的？这一神经科学领域的重要研究方向，对人工智能(AI)发展尤其是脑机接口技术研发应用至为关键，因此备受关注。" data-title="中国团队揭示大脑三维空间实时导航系统 助力新一代脑机接口研发" data-date="11-13 16:33" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">中国团队揭示大脑三维空间实时导航系统 助力新一代脑机接口研发</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/football/news/11661/13611749/bruno-fernandes-rejects-second-manchester-united-contract-offer" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Manchester United captain Bruno Fernandes has rejected a second contract offer from the club, with his current deal due to expire at the end of the season." data-title="Fernandes rejects second Man Utd contract offer" data-date="11-13 07:39" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">Fernandes rejects second Man Utd contract offer</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/cricket/news/12040/13611802/england-crumble-against-australia-in-perth-again-as-mitchell-marshs-side-win-first-odi-amid-sandpapergate-storm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="England capitulated in Perth for the second year running as an Australia side engulfed by the &#39;Sandpapergate&#39; storm cruised to a seven-wicket victory in a series-opening ODI in which debutant Mahli Beardman recorded a six-wicket haul." data-title="England crumble in Perth again as Australia win first ODI amid sandpaper storm" data-date="11-13 16:40" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">England crumble in Perth again as Australia win first ODI amid sandpaper storm</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-13/10731548.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网伊斯坦布尔11月13日电(魏园 王高飞 吴辛茹)“在气候协作与伙伴关系当中，全球南方国家必须成为共建者。”联合国环境规划署(UNEP)臭氧行动处前处长拉杰德拉·山地(Rajendra Shende)表示，全球南方国家应构建重在落地的伙伴关系，切实把气候承诺转化为行动成果。" data-title="联合国环境规划署前官员：“全球南方接受气候援助”这一认知已过时，期待携手推动气候治理｜新闻会客厅" data-date="11-13 16:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 16:36</span>
          <span class="news-item-title">联合国环境规划署前官员：“全球南方接受气候援助”这一认知已过时，期待携手推动气候治理｜新闻会客厅</span>
          <span class="news-value-point">💡 中新网伊斯坦布尔11月13日电(魏园 王高飞 吴辛茹)“在气候协作与伙伴关系当中，全球南方国家必须成为共建者</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-13/10731551.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="APEC朋友圈丨中俄研究者贝加尔湖畔携手探索地球奥秘" data-title="中俄研究者贝加尔湖畔携手探索地球奥秘" data-date="11-13 16:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 16:33</span>
          <span class="news-item-title">中俄研究者贝加尔湖畔携手探索地球奥秘</span>
          <span class="news-value-point">💡 APEC朋友圈丨中俄研究者贝加尔湖畔携手探索地球奥秘</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-13/10731545.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="如果要在中国国际进口博览会超过44万平方米的展区中，挑一件最不容错过的展品，它并不陈列在展台上。" data-title="打包也带不走！进博会最有价值的一件“展品”……" data-date="11-13 16:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 16:27</span>
          <span class="news-item-title">打包也带不走！进博会最有价值的一件“展品”……</span>
          <span class="news-value-point">💡 如果要在中国国际进口博览会超过44万平方米的展区中，挑一件最不容错过的展品，它并不陈列在展台上</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-13/10731536.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="《中共中央关于持之以恒推进全面从严治党若干重大问题的决定》鲜明指出，全面从严治党面临许多新情况新问题，对党在新形势下的执政能力、领导水平、队伍素质、拒腐防变带来重大挑战。这是我们党首次提出“四大挑战”。对此，需要全面加以理解。" data-title="新华漫说丨党在新形势下的“四大挑战”" data-date="11-13 16:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 16:23</span>
          <span class="news-item-title">新华漫说丨党在新形势下的“四大挑战”</span>
          <span class="news-value-point">💡 《中共中央关于持之以恒推进全面从严治党若干重大问题的决定》鲜明指出，全面从严治党面临许多新情况新问题，对党在新形势下的执政能力、领导水平、队伍素…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-13/10731530.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月13日电 13日，国家卫生健康委召开新闻发布会，介绍时令节气与健康(立冬、小雪)有关情况。国家卫生健康委新闻发言人、宣传司副司长杨金瑞在会上指出，我国严禁任何形式代孕。组织代孕属于违法犯罪行为，将面临法律严惩，违背伦理道德。" data-title="国家卫健委：我国严禁任何形式代孕 组织代孕属于违法犯罪行为" data-date="11-13 16:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 16:23</span>
          <span class="news-item-title">国家卫健委：我国严禁任何形式代孕 组织代孕属于违法犯罪行为</span>
          <span class="news-value-point">💡 中新网11月13日电 13日，国家卫生健康委召开新闻发布会，介绍时令节气与健康(立冬、小雪)有关情况</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-13/10731522.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月13日电 据国家疾控局网站消息，为进一步加强公共场所卫生监督量化分级管理工作，提升事中事后监管的科学性、精准性，根据公共场所卫生管理相关法律法规要求，13日，国家疾病预防控制局发布《公共场所卫生监督量化分级管理指南》。文件自2027年1月1日起实施。此前发布的有关公共场所卫生监督量化分级的工作文件与本文件不一致的，按该文件执行。" data-title="新版《公共场所卫生监督量化分级管理指南》发布 2027年起正式实施" data-date="11-13 16:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 16:06</span>
          <span class="news-item-title">新版《公共场所卫生监督量化分级管理指南》发布 2027年起正式实施</span>
          <span class="news-value-point">💡 中新网11月13日电 据国家疾控局网站消息，为进一步加强公共场所卫生监督量化分级管理工作，提升事中事后监管的科学性、精准性，根据公共场所卫生管理…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-13/10731477.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网马尼拉11月13日电 菲律宾国家警察总局12日表示，为确保第49届东盟峰会及系列会议安全举行，于13日零时起对部分警力实施全面戒备状态，以加强峰会主要活动区域及相关交通路线的安全保卫工作。" data-title="菲律宾启动东盟峰会安保戒备 逾2.3万安保人员部署到位" data-date="11-13 15:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 15:26</span>
          <span class="news-item-title">菲律宾启动东盟峰会安保戒备 逾2.3万安保人员部署到位</span>
          <span class="news-value-point">💡 中新网马尼拉11月13日电 菲律宾国家警察总局12日表示，为确保第49届东盟峰会及系列会议安全举行，于13日零时起对部分警力实施全面戒备状态，以…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-13/10731499.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月13日电 近日，日本执政党自民党及其执政伙伴日本维新会就修订“安保三文件”启动了实务层面磋商。日本《赤旗报》13日批评称，谋求修改“无核三原则”是增加核战争风险的鲁莽行径。" data-title="日媒呼吁坚持“无核三原则” 反对高市政府鲁莽行径" data-date="11-13 15:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 15:21</span>
          <span class="news-item-title">日媒呼吁坚持“无核三原则” 反对高市政府鲁莽行径</span>
          <span class="news-value-point">💡 中新网11月13日电 近日，日本执政党自民党及其执政伙伴日本维新会就修订“安保三文件”启动了实务层面磋商</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/12/us/politics/van-hollen-schumer-democrats-majority-leader.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="Senator Chris Van Hollen of Maryland has emerged as a favorite of Democrats seeking an alternative to Senator Chuck Schumer, who says he has the votes to win." data-title="Chris Van Hollen Set to Challenge Chuck Schumer for Senate Majority Leader" data-date="11-13 12:11" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-13 12:11</span>
          <span class="news-item-title">Chris Van Hollen Set to Challenge Chuck Schumer for Senate Majority Leader</span>
          <span class="news-value-point">💡 Senator Chris Van Hollen of Maryland has emerged as a favorite of Democr…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-13/10731357.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月13日电 综合消息：伊朗专家会议当地时间12日发表声明，呼吁有关部门审议退出《不扩散核武器条约》。" data-title="伊朗专家会议呼吁审议退出《不扩散核武器条约》" data-date="11-13 11:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 11:57</span>
          <span class="news-item-title">伊朗专家会议呼吁审议退出《不扩散核武器条约》</span>
          <span class="news-value-point">💡 中新社北京11月13日电 综合消息：伊朗专家会议当地时间12日发表声明，呼吁有关部门审议退出《不扩散核武器条约》</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-13/10731394.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="12日，日本多个民间团体在东京众议院第二议员会馆前举行抗议集会，反对高市政权推动修宪扩军等相关动向。集会参加者表示，近期高市政权讨论修改“安保三文件”以及不断推动修改日本宪法等举动令人担忧，日本绝不能再次走上战争道路。" data-title="日本民间团体举行集会 反对高市政权修宪扩军" data-date="11-13 11:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 11:41</span>
          <span class="news-item-title">日本民间团体举行集会 反对高市政权修宪扩军</span>
          <span class="news-value-point">💡 12日，日本多个民间团体在东京众议院第二议员会馆前举行抗议集会，反对高市政权推动修宪扩军等相关动向</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-13/10731385.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="日本正在加速谋划年内对“安保三文件”进行修订。据日本方面12日消息，日本政府计划将所谓“集体韧性”的理念写入“安保三文件”之一的《国家安全保障战略》。" data-title="日本政府计划将“集体韧性”写入安保战略 进一步恶化地区环境" data-date="11-13 11:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 11:29</span>
          <span class="news-item-title">日本政府计划将“集体韧性”写入安保战略 进一步恶化地区环境</span>
          <span class="news-value-point">💡 日本正在加速谋划年内对“安保三文件”进行修订</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/12/us/kansas-governor-democrat-holscher-wins.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="State Senator Cindy Holscher won the race. Though Kansas is reliably Republican in presidential elections, its voters often break for Democrats in midterms." data-title="Holscher Wins Kansas Governor Race, Retaining Seat for Democrats" data-date="11-13 07:16" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-13 07:16</span>
          <span class="news-item-title">Holscher Wins Kansas Governor Race, Retaining Seat for Democrats</span>
          <span class="news-value-point">💡 State Senator Cindy Holscher won the race. Though Kansas is reliably Rep…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/12/us/politics/trump-vance-iran-fraud.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="社交媒体上的这一声明加深了人们对总统结束战争的计划的疑问。“我们不需要与伊朗达成协议，”他写道。" data-title="Trump Says He’s Pulling Vance Off Iran Talks to Focus on Fraud Campaign" data-date="11-13 03:38" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-13 03:38</span>
          <span class="news-item-title">特朗普表示，他将让万斯退出伊朗谈判，以专注于选举舞弊问题</span>
          <span class="news-item-title-en">Trump Says He’s Pulling Vance Off Iran Talks to Focus on Fraud Campaign</span>
          <span class="news-value-point">💡 社交媒体上的这一声明加深了人们对总统结束战争的计划的疑问</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/12/business/nvidia-megaspeed-alice-huang.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新加坡在一份声明中表示，在特朗普总统被告知黄静是间谍的数月后，新加坡才扣留了她的护照。" data-title="Singapore Says US Not Helpful on Investigation Into Alice Huang and Megaspeed" data-date="11-13 03:19" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-13 03:19</span>
          <span class="news-item-title">新加坡表示，美国对爱丽丝·黄和Megaspeed的调查没有帮助</span>
          <span class="news-item-title-en">Singapore Says US Not Helpful on Investigation Into Alice Huang and Megaspeed</span>
          <span class="news-value-point">💡 新加坡在一份声明中表示，在特朗普总统被告知黄静是间谍的数月后，新加坡才扣留了她的护照</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-13/10731540.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网北京11月13日电 (记者 孙自法)大脑中的导航系统是如何实时对手部等肢体运动进行定位的？这一神经科学领域的重要研究方向，对人工智能(AI)发展尤其是脑机接口技术研发应用至为关键，因此备受关注。" data-title="中国团队揭示大脑三维空间实时导航系统 助力新一代脑机接口研发" data-date="11-13 16:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 16:33</span>
          <span class="news-item-title">中国团队揭示大脑三维空间实时导航系统 助力新一代脑机接口研发</span>
          <span class="news-value-point">💡 中新网北京11月13日电 (记者 孙自法)大脑中的导航系统是如何实时对手部等肢体运动进行定位的</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/026/801.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 13 日消息，据央视新闻报道，11 月 13 日，2026 世界中文大会在北京开幕，会上发布语飞国际中文教育垂直大模型，为全球中文学习者、教师和教育机构提供智能化服务。面向全球中文学习者，模型可提供即时反馈的学习评测、随问随答的个性化辅导；面向教师，支持在多轮对话中快速生成覆盖课前备课、课堂互动、课后巩固的教学素材，提升教学效率；面向全球中文教育机构，提供标准化接口，连接各方、赋能应用，让数智化创新在更多教学场景落地生根。IT之家从该报道中获悉，该模型将人工智能技术与国际中文教育实际需求相结合，深度融入专业知识、教学规律与真实场景，专项适配教与学各个环节，推动优质教学资源与智能服务共享，助力国际中文教育数智化发展。" data-title="国际中文教育垂直大模型亮相，为全球中文学习者等群体提供智能化服务" data-date="11-13 16:01" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-13 16:01</span>
          <span class="news-item-title">国际中文教育垂直大模型亮相，为全球中文学习者等群体提供智能化服务</span>
          <span class="news-value-point">💡 IT之家 11 月 13 日消息，据央视新闻报道，11 月 13 日，2026 世界中文大会在北京开幕，会上发布语飞国际中文教育垂直大模型，为全…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cmn80j4vnj1jo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="美国议员现在想就他被指控的其中一段关系是否与中国间谍有关对他进行质询。" data-title="深陷丑闻的黄仁勋辞职，AI芯片巨头Nvidia陷入动荡" data-date="11-13 12:33" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-13 12:33</span>
          <span class="news-item-title">深陷丑闻的黄仁勋辞职，AI芯片巨头Nvidia陷入动荡</span>
          <span class="news-value-point">💡 美国议员现在想就他被指控的其中一段关系是否与中国间谍有关对他进行质询</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/12/us/politics/trump-jensen-huang-nvidia.html" target="_blank" rel="noopener" data-cat="keji" data-summary="The president called the Nvidia chief on Tuesday, continuing a pattern of supporting him even as the spy scandal was intensifying." data-title="Trump Had Urged Nvidia’s Jensen Huang to Fight for His Job" data-date="11-13 11:27" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-13 11:27</span>
          <span class="news-item-title">Trump Had Urged Nvidia’s Jensen Huang to Fight for His Job</span>
          <span class="news-value-point">💡 The president called the Nvidia chief on Tuesday, continuing a pattern o…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/12/us/politics/lutnick-nvidia-commerce-china-chips.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Critics say Howard Lutnick, the commerce secretary, and his department have shielded Nvidia as concerns have grown over A.I. chip sales to firms like Megaspeed." data-title="Howard Lutnick Took Softer Line on Nvidia as Calls for Tougher Controls Grew" data-date="11-13 09:28" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-13 09:28</span>
          <span class="news-item-title">Howard Lutnick Took Softer Line on Nvidia as Calls for Tougher Controls Grew</span>
          <span class="news-value-point">💡 Critics say Howard Lutnick, the commerce secretary, and his department h…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1032774/president-donald-trump-tim-cook-nvidia-jensen-huang" target="_blank" rel="noopener" data-cat="keji" data-summary="Jensen Huang resigned this morning as Nvidia&#39;s CEO following reports of affairs, including one with an alleged Chinese spy. Right now, the company is being led by its CFO on an interim basis. But President Donald Trump is already throwing around one person he thinks should take over the chipmaking giant: former Apple CEO Tim […]" data-title="Donald Trump really wants Tim Cook to run Nvidia" data-date="11-13 08:46" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-13 08:46</span>
          <span class="news-item-title">Donald Trump really wants Tim Cook to run Nvidia</span>
          <span class="news-value-point">💡 Jensen Huang resigned this morning as Nvidia's CEO following reports of …</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/12/democrats-launch-nvidia-investigation-write-scathing-letter-on-huangs-scheme-with-trump/" target="_blank" rel="noopener" data-cat="keji" data-summary="This Congressional investigation into Nvidia&#39;s China sales and its dealings with Trump is the second one, so far, since news of the alleged spy affair broke." data-title="Democrats launch Nvidia investigation, write scathing letter on Huang’s ‘scheme’ with Trump" data-date="11-13 06:42" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-13 06:42</span>
          <span class="news-item-title">Democrats launch Nvidia investigation, write scathing letter on Huang’s ‘scheme’ with Trump</span>
          <span class="news-value-point">💡 This Congressional investigation into Nvidia's China sales and its deali…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1032505/google-search-ai-mode-gemini-4-hydrogen" target="_blank" rel="noopener" data-cat="keji" data-summary="Google says its new Gemini 4 Hydrogen model can give more helpful answers to complex questions, including &quot;questions with multiple parts, hard-to-understand typos, or highly specific requests.&quot; The new model can break down your questions and address each part in its responses. It&#39;s available starting today in search, the Gemini app, all tiers of Go" data-title="Google’s new Gemini model is better at understanding complicated questions" data-date="11-13 05:55" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-13 05:55</span>
          <span class="news-item-title">Google’s new Gemini model is better at understanding complicated questions</span>
          <span class="news-value-point">💡 Google says its new Gemini 4 Hydrogen model can give more helpful answer…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1032434/nvidia-jensen-huang-resignation-reactions" target="_blank" rel="noopener" data-cat="keji" data-summary="Nvidia announced this morning that Jensen Huang has resigned as CEO following reports of two affairs, including one with an alleged Chinese spy and one with a direct report. The situation surrounding Huang has unfolded quickly, with The New York Times only reporting on Friday that Huang and the suspected spy were &quot;close&quot; before other […]" data-title="‘It’s a mistake’: reactions from tech leaders on Jensen Huang’s resignation" data-date="11-13 05:45" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-13 05:45</span>
          <span class="news-item-title">‘It’s a mistake’: reactions from tech leaders on Jensen Huang’s resignation</span>
          <span class="news-value-point">💡 Nvidia announced this morning that Jensen Huang has resigned as CEO foll…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/12/nvidia-ceo-jensen-huangs-affair-with-alleged-chinese-spy-a-timeline/" target="_blank" rel="noopener" data-cat="keji" data-summary="Jensen Huang在曝出婚外情后已从Nvidia辞职，鉴于美国和中国正在竞相开发最先进的人工智能基础设施，此事可能对国家安全产生影响。" data-title="The unfolding Jensen Huang scandal: a timeline" data-date="11-13 05:35" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-13 05:35</span>
          <span class="news-item-title">正在发酵的黄仁勋丑闻：时间线</span>
          <span class="news-item-title-en">The unfolding Jensen Huang scandal: a timeline</span>
          <span class="news-value-point">💡 Jensen Huang在曝出婚外情后已从Nvidia辞职，鉴于美国和中国正在竞相开发最先进的人工智能基础设施，此事可能对国家安全产生影响</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/12/nebius-tests-the-neocloud-playbook-with-40-billion-in-planned-spending/" target="_blank" rel="noopener" data-cat="keji" data-summary="Nebius plans to fund its $40 billion AI infrastructure expansion through customer prepayments and loans, even as delays at a Microsoft data center raise questions about its financing model." data-title="Nebius tests the neocloud playbook with $40 billion in planned spending" data-date="11-13 05:27" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-13 05:27</span>
          <span class="news-item-title">Nebius tests the neocloud playbook with $40 billion in planned spending</span>
          <span class="news-value-point">💡 Nebius plans to fund its $40 billion AI infrastructure expansion through…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/12/jensen-huang-was-having-a-third-affair-reuters-reports/" target="_blank" rel="noopener" data-cat="keji" data-summary="Reuters is withholding the name of the new employee linked to Huang, but says she is an employee of Nvidia." data-title="Jensen Huang was having a third affair, Reuters reports" data-date="11-13 04:26" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-13 04:26</span>
          <span class="news-item-title">Jensen Huang was having a third affair, Reuters reports</span>
          <span class="news-value-point">💡 Reuters is withholding the name of the new employee linked to Huang, but…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1032125/ai-agents-maya-site-archeology-discovery" target="_blank" rel="noopener" data-cat="keji" data-summary="本周早些时候，谷歌研究员Pietro Miotti声称，在人工智能代理团队的协助下，他发现了墨西哥一处可能尚未被标注在地图上的玛雅遗址。只有一个问题：该遗址早已被发现，并发表在学术期刊上。" data-title="No, AI agents did not discover a previously unknown Maya site" data-date="11-13 03:42" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-13 03:42</span>
          <span class="news-item-title">不，AI 代理并未发现此前未知的玛雅遗址</span>
          <span class="news-item-title-en">No, AI agents did not discover a previously unknown Maya site</span>
          <span class="news-value-point">💡 本周早些时候，谷歌研究员Pietro Miotti声称，在人工智能代理团队的协助下，他发现了墨西哥一处可能尚未被标注在地图上的玛雅遗址</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/12/googles-latest-search-upgrade-promises-better-answers-to-your-most-complicated-questions/" target="_blank" rel="noopener" data-cat="keji" data-summary="得益于Gemini 4 Hydrogen，Google的AI模式在理解复杂查询、显示相关链接和提供更丰富的视觉响应方面正变得越来越出色。" data-title="Google’s latest Search upgrade promises better answers to your most complicated questions" data-date="11-13 03:27" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-13 03:27</span>
          <span class="news-item-title">谷歌最新的搜索升级承诺为您最复杂的问题提供更好的答案</span>
          <span class="news-item-title-en">Google’s latest Search upgrade promises better answers to your most complicated questions</span>
          <span class="news-value-point">💡 得益于Gemini 4 Hydrogen，Google的AI模式在理解复杂查询、显示相关链接和提供更丰富的视觉响应方面正变得越来越出色</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/12/nectar-launches-an-ai-agent-to-automate-creator-discovery-and-outreach-for-brands/" target="_blank" rel="noopener" data-cat="keji" data-summary="Nectar 的新版 AI 代理可实现网红营销自动化，帮助品牌发现创作者、管理推广和合作关系，并跟踪营销活动的效果。" data-title="Nectar launches an AI agent to automate creator discovery and outreach for brands" data-date="11-13 03:11" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-13 03:11</span>
          <span class="news-item-title">Nectar推出AI代理，帮助品牌方自动化创作者发现和联系流程</span>
          <span class="news-item-title-en">Nectar launches an AI agent to automate creator discovery and outreach for brands</span>
          <span class="news-value-point">💡 Nectar 的新版 AI 代理可实现网红营销自动化，帮助品牌发现创作者、管理推广和合作关系，并跟踪营销活动的效果</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">10 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13611749/bruno-fernandes-rejects-second-manchester-united-contract-offer" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Manchester United captain Bruno Fernandes has rejected a second contract offer from the club, with his current deal due to expire at the end of the season." data-title="Fernandes rejects second Man Utd contract offer" data-date="11-13 07:39" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-13 07:39</span>
          <span class="news-item-title">Fernandes rejects second Man Utd contract offer</span>
          <span class="news-value-point">💡 Manchester United captain Bruno Fernandes has rejected a second contract…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13611745/mauricio-pochettino-manchester-united-agree-two-and-a-half-year-deal-with-usa-manager-to-replace-michael-carrick" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Manchester United and Mauricio Pochettino have agreed a deal for him to become the club&#39;s next head coach." data-title="Pochettino agrees two-and-a-half-year deal to become Man Utd boss" data-date="11-13 07:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-13 07:00</span>
          <span class="news-item-title">Pochettino agrees two-and-a-half-year deal to become Man Utd boss</span>
          <span class="news-value-point">💡 Manchester United and Mauricio Pochettino have agreed a deal for him to …</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13611631/mauricio-pochettino-to-manchester-united-how-uniteds-pursuit-of-former-tottenham-and-chelsea-manager-unfolded" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Manchester United&#39;s bosses met Mauricio Pochettino two years ago and considered him as a possible replacement for Erik ten Hag." data-title="Inside Man Utd&#39;s pursuit of Pochettino" data-date="11-13 01:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-13 01:00</span>
          <span class="news-item-title">曼联追求波切蒂诺的幕后故事</span>
          <span class="news-item-title-en">Inside Man Utd's pursuit of Pochettino</span>
          <span class="news-value-point">💡 Manchester United's bosses met Mauricio Pochettino two years ago and con…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqdr1jlr1707o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联是如何确定毛里西奥·波切蒂诺为新任主教练的——以及在迈克尔·卡里克被晾在一边的那一周里发生了什么。" data-title="How Pochettino came on Man Utd&#39;s radar - and what Carrick was told when" data-date="11-13 00:12" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-13 00:12</span>
          <span class="news-item-title">波切蒂诺是如何进入曼联视野的——以及卡里克当时被告知了什么</span>
          <span class="news-item-title-en">How Pochettino came on Man Utd's radar - and what Carrick was told when</span>
          <span class="news-value-point">💡 曼联是如何确定毛里西奥·波切蒂诺为新任主教练的——以及在迈克尔·卡里克被晾在一边的那一周里发生了什么</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/12/mauricio-pochettino-manchester-united-usmnt-nations-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="美国男足主教练已同意与曼联的协议框架曼联已与美国足协取得联系巴洛贡：“我希望事情保持现状”波切蒂诺加盟曼联的最新消息和反应毛里西奥·波切蒂诺将执教美国男足国家队" data-title="Pochettino expected to lead US in Nations League games before Manchester United move" data-date="11-12 22:57" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-12 22:57</span>
          <span class="news-item-title">波切蒂诺预计将在执教曼联之前率领美国队参加欧国联比赛</span>
          <span class="news-item-title-en">Pochettino expected to lead US in Nations League games before Manchester United move</span>
          <span class="news-value-point">💡 美国男足主教练已同意与曼联的协议框架曼联已与美国足协取得联系巴洛贡：“我希望事情保持现状”波切蒂诺加盟曼联的最新消息和反应毛里西奥·波切蒂诺将执…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13611501/gary-neville-man-utds-treatment-of-michael-carrick-disgusting-as-mauricio-pochettino-prepares-to-take-over-at-old-trafford" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在曼联传奇人物迈克尔·卡里克被解雇主教练职务后，天空体育的加里·内维尔将曼联对他的处理方式描述为“令人作呕”，而毛里西奥·波切蒂诺即将接替他在老特拉福德的职位。" data-title="Neville &#39;disgusted&#39; at Man Utd&#39;s treatment of Carrick" data-date="11-12 22:49" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-12 22:49</span>
          <span class="news-item-title">内维尔对曼联对待卡里克的方式感到“厌恶”</span>
          <span class="news-item-title-en">Neville 'disgusted' at Man Utd's treatment of Carrick</span>
          <span class="news-value-point">💡 在曼联传奇人物迈克尔·卡里克被解雇主教练职务后，天空体育的加里·内维尔将曼联对他的处理方式描述为“令人作呕”，而毛里西奥·波切蒂诺即将接替他在老…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13611501/gary-neville-man-utds-treatment-of-michael-carrick-disgusting-as-mauricio-pochettino-prepares-to-take-over-at-old-trafford" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在曼联传奇人物迈克尔·卡里克被解雇主教练职务后，天空体育的加里·内维尔将曼联对他的处理方式描述为“令人作呕”，而毛里西奥·波切蒂诺即将接替他在老特拉福德的职位。" data-title="Neville &#39;disgusted&#39; at Man Utd&#39;s treatment of Carrick" data-date="11-12 22:49" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-12 22:49</span>
          <span class="news-item-title">内维尔对曼联对待卡里克的方式感到“厌恶”</span>
          <span class="news-item-title-en">Neville 'disgusted' at Man Utd's treatment of Carrick</span>
          <span class="news-value-point">💡 在曼联传奇人物迈克尔·卡里克被解雇主教练职务后，天空体育的加里·内维尔将曼联对他的处理方式描述为“令人作呕”，而毛里西奥·波切蒂诺即将接替他在老…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13602738/michael-carrick-sacked-by-man-utd-how-his-old-trafford-reign-unravelled-in-worst-start-to-a-season-in-40-years" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（Michael Carrick）被解雇了曼联主教练的职务，那么他的老特拉福德执教生涯为何如此迅速地走向失败？" data-title="How Carrick&#39;s reign unravelled" data-date="11-12 18:50" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-12 18:50</span>
          <span class="news-item-title">卡里克执教生涯的终结</span>
          <span class="news-item-title-en">How Carrick's reign unravelled</span>
          <span class="news-value-point">💡 迈克尔·卡里克（Michael Carrick）被解雇了曼联主教练的职务，那么他的老特拉福德执教生涯为何如此迅速地走向失败</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13606106/man-utd-sack-michael-carrick-with-mauricio-pochettino-set-to-be-appointed-after-worst-start-to-premier-league-season" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克已被解雇，不再担任曼联主教练，毛里西奥·波切蒂诺将接替他的职位。" data-title="Carrick sacked as Man Utd reach full agreement with Pochettino" data-date="11-12 18:27" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-12 18:27</span>
          <span class="news-item-title">曼联与波切蒂诺达成全面协议，卡里克被解雇</span>
          <span class="news-item-title-en">Carrick sacked as Man Utd reach full agreement with Pochettino</span>
          <span class="news-value-point">💡 迈克尔·卡里克已被解雇，不再担任曼联主教练，毛里西奥·波切蒂诺将接替他的职位</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cm0rl4kwn8vqo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克成为三赛季内被解雇的第三位曼联主帅——问题出在哪里？" data-title="The chaos that took Carrick from two-year deal to sacked within 15 games" data-date="11-12 18:21" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-12 18:21</span>
          <span class="news-item-title">卡里克从签下两年合同到在15场比赛后被解雇的混乱经历</span>
          <span class="news-item-title-en">The chaos that took Carrick from two-year deal to sacked within 15 games</span>
          <span class="news-value-point">💡 迈克尔·卡里克成为三赛季内被解雇的第三位曼联主帅——问题出在哪里</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/cricket/news/12040/13611802/england-crumble-against-australia-in-perth-again-as-mitchell-marshs-side-win-first-odi-amid-sandpapergate-storm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="England capitulated in Perth for the second year running as an Australia side engulfed by the &#39;Sandpapergate&#39; storm cruised to a seven-wicket victory in a series-opening ODI in which debutant Mahli Beardman recorded a six-wicket haul." data-title="England crumble in Perth again as Australia win first ODI amid sandpaper storm" data-date="11-13 16:40" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-13 16:40</span>
          <span class="news-item-title">England crumble in Perth again as Australia win first ODI amid sandpaper storm</span>
          <span class="news-value-point">💡 England capitulated in Perth for the second year running as an Australia…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-13/10731543.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网海口11月13日电 (记者 王晓斌)一种叫“衍射光波导”的技术，正在改变中国博物馆里看文物的方式。记者在13日开幕的第十一届中国博物馆及相关产品与技术博览会(下称“博博会”)上看到，这项“魔法光”技术已经和文博场景深度结合——观众可以选择戴上AI眼镜看文物讲解，也可以什么都不戴，看三维影像悬浮在一块透明玻璃中。" data-title="博物馆里的“魔法光”：戴上眼镜看细节，摘下眼镜看悬浮" data-date="11-13 16:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 16:37</span>
          <span class="news-item-title">博物馆里的“魔法光”：戴上眼镜看细节，摘下眼镜看悬浮</span>
          <span class="news-value-point">💡 中新网海口11月13日电 (记者 王晓斌)一种叫“衍射光波导”的技术，正在改变中国博物馆里看文物的方式</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/026/811.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 13 日消息，据中国铁路昆明局集团有限公司消息，11 月 12 日上午，随着最后一方钢管混凝土顺利完成顶升，文蒙铁路南溪河特大桥 9 号格构墩顺利完工。这是国内铁路工程首次应用格构墩结构，标志着我国在山区高墩桥梁建设领域取得重要技术突破。南溪河特大桥位于云南省蒙自市芷村镇，全长 789.71 米，桥面与地面最大高差达 118 米，是文蒙铁路全线最高桥梁。桥址区地形起伏剧烈，跨越深切沟谷，存在危岩落石、岩溶发育等不良地质，施工难度极大。全桥共设计 3 座格构墩，其中 9 号墩高 105 米，为全线最高桥墩，其格构部分分为 7 个节段、176 个散件拼装工艺，最大单个构件重达 24 吨，施工犹如在百米高空“搭巨型积木”。据介绍，此次应用的钢管混凝土格构墩，通过钢管与工字钢拼装" data-title="百米高空“搭巨型积木”，我国铁路工程首次应用格构墩结构完成桥墩施工" data-date="11-13 16:33" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-13 16:33</span>
          <span class="news-item-title">百米高空“搭巨型积木”，我国铁路工程首次应用格构墩结构完成桥墩施工</span>
          <span class="news-value-point">💡 IT之家 11 月 13 日消息，据中国铁路昆明局集团有限公司消息，11 月 12 日上午，随着最后一方钢管混凝土顺利完成顶升，文蒙铁路南溪河特…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-13/10731537.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网巴彦淖尔11月13日电 题：探访内蒙古戈壁小站：为边民 “加油”，为共富 “续航”" data-title="探访内蒙古戈壁小站：为边民 “加油”，为共富 “续航”" data-date="11-13 16:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 16:31</span>
          <span class="news-item-title">探访内蒙古戈壁小站：为边民 “加油”，为共富 “续航”</span>
          <span class="news-value-point">💡 中新网巴彦淖尔11月13日电 题：探访内蒙古戈壁小站：为边民 “加油”，为共富 “续航”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-13/10731534.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网青海乌图美仁11月13日电 题：柴达木戈壁“追光人”：烟火人间的荒漠守护" data-title="柴达木戈壁“追光人”：烟火人间的荒漠守护" data-date="11-13 16:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 16:28</span>
          <span class="news-item-title">柴达木戈壁“追光人”：烟火人间的荒漠守护</span>
          <span class="news-value-point">💡 中新网青海乌图美仁11月13日电 题：柴达木戈壁“追光人”：烟火人间的荒漠守护</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-13/10731532.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社福州11月13日电 (叶秋云)“万里茶道”中蒙美术家精品联合巡展(福州站)13日在福建省画院开幕，展出中国和蒙古国美术家的百余幅作品。" data-title="“万里茶道”中蒙美术家精品联合巡展走进福州" data-date="11-13 16:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 16:26</span>
          <span class="news-item-title">“万里茶道”中蒙美术家精品联合巡展走进福州</span>
          <span class="news-value-point">💡 中新社福州11月13日电 (叶秋云)“万里茶道”中蒙美术家精品联合巡展(福州站)13日在福建省画院开幕，展出中国和蒙古国美术家的百余幅作品</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-13/10731544.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="青春华章·我们的新长征｜天开“多点”走好新时代科创长征路" data-title="天开“多点”走好新时代科创长征路" data-date="11-13 16:25" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 16:25</span>
          <span class="news-item-title">天开“多点”走好新时代科创长征路</span>
          <span class="news-value-point">💡 青春华章·我们的新长征｜天开“多点”走好新时代科创长征路</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/026/802.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 13 日消息，科技媒体 sammyguru 昨日（11 月 12 日）发布博文，分享了一组照片，声称是三星 Galaxy S27 系列手机默认壁纸，共有 5 种配色，采用折叠丝带设计，暗示三星最新旗舰手机也会采用这 5 种颜色。通常情况下，三星会为 Galaxy S 系列旗舰手机的不同颜色，推出专属壁纸。IT之家援引博文介绍，以 Galaxy S26 Ultra 为例，三星分别推出了黑色、白色、蓝色、紫色、粉色和灰色共计 6 种颜色壁纸，分别对应旷宇黑、映雪白、浅云蓝、幽夜紫四种常规颜色，以及绯霞金和镜月银两种专属色。该媒体推测三星 Galaxy S27 系列会沿用这种模式，并指出 Galaxy S27 系列会有以下 5 种颜色：颜色视觉特点适合人群 / 气质海军蓝 Na" data-title="三星 Galaxy S27 系列手机壁纸曝光：5 种颜色，折叠丝带设计吸睛" data-date="11-13 16:04" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-13 16:04</span>
          <span class="news-item-title">三星 Galaxy S27 系列手机壁纸曝光：5 种颜色，折叠丝带设计吸睛</span>
          <span class="news-value-point">💡 IT之家 11 月 13 日消息，科技媒体 sammyguru 昨日（11 月 12 日）发布博文，分享了一组照片，声称是三星 Galaxy S…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-13/10731527.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="国家卫生健康委今天举行新闻发布会，介绍时令节气与健康有关情况。国家卫生健康委新闻发言人杨金瑞表示，近期，有媒体报道非法中介机构在无医疗条件的场所内开展“地下代孕”，由无资质的非专业人员实施，操作过程极不规范，风险极高。这些非法机构往往滥用促排卵药物，极易引发女性卵巢损伤，造成大出血和严重感染等，甚至危及生命；同时，胚胎培养和移植条件差，极易造成新生儿流产、早产、死胎死产和严重出生缺陷。" data-title="国家卫健委：我国严禁任何形式代孕 组织代孕属于违法犯罪行为" data-date="11-13 16:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 16:04</span>
          <span class="news-item-title">国家卫健委：我国严禁任何形式代孕 组织代孕属于违法犯罪行为</span>
          <span class="news-value-point">💡 国家卫生健康委今天举行新闻发布会，介绍时令节气与健康有关情况</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/nfl/news/12040/13611793/nfl-washington-commanders-rally-to-defeat-the-new-york-giants-thanks-to-jayden-daniels-and-stefon-diggs" target="_blank" rel="noopener" data-cat="zonghe" data-summary="The Washington Commanders stunned the New York Giants 24-21 to keep their season alive." data-title="Commanders dig deep to save season with late rally against Giants" data-date="11-13 16:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-13 16:00</span>
          <span class="news-item-title">Commanders dig deep to save season with late rally against Giants</span>
          <span class="news-value-point">💡 The Washington Commanders stunned the New York Giants 24-21 to keep thei…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/golf/live-blog/12040/13611568/dp-world-tour-championship-second-round-live-latest-scores-highlights-as-rory-mcilroy-hunts-eighth-race-to-dubai-title" target="_blank" rel="noopener" data-cat="zonghe" data-summary="McIlroy out to capitalise on fast start, as Luiten leads in Dubai LIVE!" data-title="McIlroy out to capitalise on fast start, as Luiten leads in Dubai LIVE!" data-date="11-13 15:45" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-13 15:45</span>
          <span class="news-item-title">McIlroy out to capitalise on fast start, as Luiten leads in Dubai LIVE!</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-13/10731496.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京11月13日电 (记者 吕少威)记者13日从北京市交通委获悉，今年以来，北京静态交通治理坚持新增建设与存量盘活并重、设施供给与综合治理协同，取得阶段性成效：全市新增道路非机动车停车22.2万个，中心城区新增居住停车位3.7万个，非机动车停放秩序月度达标率由4月的75%提升至10月的94%，市民出行环境持续改善。" data-title="今年以来北京新增道路非机动车停车位22.2万个" data-date="11-13 15:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-13 15:35</span>
          <span class="news-item-title">今年以来北京新增道路非机动车停车位22.2万个</span>
          <span class="news-value-point">💡 中新网北京11月13日电 (记者 吕少威)记者13日从北京市交通委获悉，今年以来，北京静态交通治理坚持新增建设与存量盘活并重、设施供给与综合治理…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/crvg2d7v05yno/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="监测网站显示，这次中断影响74个国家的用户，已持续超过八小时。" data-title="微软系统全球瘫痪：Outlook、Teams、Copilot受影响" data-date="11-13 15:32" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-13 15:32</span>
          <span class="news-item-title">微软系统全球瘫痪：Outlook、Teams、Copilot受影响</span>
          <span class="news-value-point">💡 监测网站显示，这次中断影响74个国家的用户，已持续超过八小时</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/tennis/news/12040/13611773/wta-finals-jessica-pegula-saves-match-8204point-in-stunning-win-over-linda-noskova-to-send-coco-gauff-out-and-set-up-mirra-andreeva-clash" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Jessica Pegula saved a match ‌point en route to a gritty 7-6 (7-2) 4-6 7-5 win over Linda Noskova to advance to the semi-finals at the WTA Finals and ​send fellow American Coco Gauff packing from the season-ending championships." data-title="&#39;It&#39;s the match people wanted&#39; - Pegula to face Andreeva at WTA Finals" data-date="11-13 15:12" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-13 15:12</span>
          <span class="news-item-title">'It's the match people wanted' - Pegula to face Andreeva at WTA Finals</span>
          <span class="news-value-point">💡 Jessica Pegula saved a match ‌point en route to a gritty 7-6 (7-2) 4-6 7…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/racing/news/12040/13611165/today-on-sky-sports-racing-bahrain-sedgefield-and-southwell" target="_blank" rel="noopener" data-cat="zonghe" data-summary="We have a busy day’s racing on Friday with action from Bahrain, Sedgefield and Southwell, live on Sky Sports Racing..." data-title="Royal Champion out to defend his Bahrain crown" data-date="11-13 15:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-13 15:00</span>
          <span class="news-item-title">Royal Champion out to defend his Bahrain crown</span>
          <span class="news-value-point">💡 We have a busy day’s racing on Friday with action from Bahrain, Sedgefie…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🌍</span>
      <span class="news-category-title">西方媒体视角 (外媒看中国 · 奇葩言论集锦)</span>
      <span class="news-category-count">2 条</span>
    </div>
        <a class="news-item" href="https://techcrunch.com/2026/11/12/jensen-huang-agrees-to-testify-before-congress/" target="_blank" rel="noopener" data-cat="meimei" data-summary="黄先生在被曝与一名涉嫌为中国从事间谍活动的女性有染后被免去首席执行官职务，在多名高级议员威胁传唤他出庭后，他同意于周三作证。" data-title="Jensen Huang agrees to testify before Congress" data-date="11-13 00:36" data-source="TechCrunch">
          <span class="news-cat-tag cat-meimei">🌍 外媒视角</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-13 00:36</span>
          <span class="news-item-title">黄仁勋同意在国会作证</span>
          <span class="news-item-title-en">Jensen Huang agrees to testify before Congress</span>
          <span class="news-value-point">💡 黄先生在被曝与一名涉嫌为中国从事间谍活动的女性有染后被免去首席执行官职务，在多名高级议员威胁传唤他出庭后，他同意于周三作证</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cje391ee1xvlo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="meimei" data-summary="据报导，卷入婚外情、被指涉入中国间谍活动的女子黄乐（Alice Huang Le）已经返回中国。近年来，她曾十次入境美国、八次入境台湾。" data-title="黄仁勋婚外情：黄乐据称身在北京，台湾废止其入境许可证" data-date="11-12 18:15" data-source="BBC">
          <span class="news-cat-tag cat-meimei">🌍 外媒视角</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-12 18:15</span>
          <span class="news-item-title">黄仁勋婚外情：黄乐据称身在北京，台湾废止其入境许可证</span>
          <span class="news-value-point">💡 据报导，卷入婚外情、被指涉入中国间谍活动的女子黄乐（Alice Huang Le）已经返回中国</span>
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


<p class="news-updated">🕐 抓取更新于 2026-11-13 16:51（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
