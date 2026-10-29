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
      <span>2026-10-29 22:34 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×21 · 天空体育×9</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/10-29/10723030.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中国共产党第二十届中央委员会第五次全体会议，于2026年10月26日至29日在北京举行。全会决定，中国共产党第二十一次全国代表大会于2027年下半年在北京召开。" data-title="海报丨中国共产党第二十一次全国代表大会于2027年下半年在北京召开" data-date="10-29 22:08" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-29 22:08</span>
      </div>
      <h2 class="hero-featured-title">海报丨中国共产党第二十一次全国代表大会于2027年下半年在北京召开</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/019/783.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 29 日消息，人工智能实验室扩散智能 (DiffuSpace) 昨日发布了其 Clover（三叶草）系列模型家族的首个成员：Clover-35B-A3B-Preview，并以 Apache 许可开源。Clover-35B-A3B-Preview 是一款采用 MoE 架构的扩散语言模型。与传统自回归模型不同的是，其具备“全局思维”，通过多轮迭代实现结果的从模糊到具体。DiffuSpace 表示，Clover-35B-A3B-Preview 的诞生证明扩散语言模型能在更大的参数尺度下与自回归模型竞争甚至略胜一筹，同时保持更快生成速度。该模型在多项基准测试中性能超过同规模的自回归模型 Qwen3.6-35B-A3B，尤其擅长智能体编程与工具使用任务。参考https://diff" data-title="DiffuSpace 推出 Clover-35B-A3B-Preview 扩散语言模型，兼顾性能与速度" data-date="10-29 22:33" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">DiffuSpace 推出 Clover-35B-A3B-Preview 扩散语言模型，兼顾性能与速度</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/football/news/12040/13605331/manchester-united-michael-carrick-ready-to-move-forward-with-bruno-fernandes-as-captain-and-doesnt-require-assurances-on-his-future" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）表示，他已准备好与布鲁诺·费尔南德斯（ Bruno Fernandes ）一起担任曼联队" data-title="Carrick ready to &#39;move forward&#39; with Fernandes as captain" data-date="10-29 22:00" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">Carrick ready to 'move forward' with Fernandes as captain</p>
    </a>
    <a class="hero-sub-card" href="https://www.theverge.com/gadgets/1022103/ocarina-of-time-remake-apple-mac-mini-ssd-hdmi-dock-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="期待已久的《塞尔达传说： Nintendo Switch 2时间之笛》重制版将于11月5日星期四推出。换句话说，您还有一周的时间在亚马逊和沃尔玛享受10 $的折扣。" data-title="There’s one week left to preorder the Ocarina of Time remake for $10 off" data-date="10-29 22:24" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">There’s one week left to preorder the Ocarina of Time remake for $10 off</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-29/10723030.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中国共产党第二十届中央委员会第五次全体会议，于2026年10月26日至29日在北京举行。全会决定，中国共产党第二十一次全国代表大会于2027年下半年在北京召开。" data-title="海报丨中国共产党第二十一次全国代表大会于2027年下半年在北京召开" data-date="10-29 22:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 22:08</span>
          <span class="news-item-title">海报丨中国共产党第二十一次全国代表大会于2027年下半年在北京召开</span>
          <span class="news-value-point">💡 中国共产党第二十届中央委员会第五次全体会议，于2026年10月26日至29日在北京举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-29/10722999.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网海口10月29日电 题：跨越南洋“鼓舞还乡” 海南首支二十四节令鼓队擂响百年学府" data-title="跨越南洋“鼓舞还乡” 海南首支二十四节令鼓队擂响百年学府" data-date="10-29 21:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 21:23</span>
          <span class="news-item-title">跨越南洋“鼓舞还乡” 海南首支二十四节令鼓队擂响百年学府</span>
          <span class="news-value-point">💡 中新网海口10月29日电 题：跨越南洋“鼓舞还乡” 海南首支二十四节令鼓队擂响百年学府</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-29/10722989.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月29日电 据美联社报道，保加利亚海事部门29日表示，一艘悬挂利比里亚国旗的船只在保加利亚黑海沿岸被无人机击中后沉没。" data-title="一艘商船在保加利亚黑海沿岸被无人机击中后沉没" data-date="10-29 21:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 21:16</span>
          <span class="news-item-title">一艘商船在保加利亚黑海沿岸被无人机击中后沉没</span>
          <span class="news-value-point">💡 中新网北京10月29日电 据美联社报道，保加利亚海事部门29日表示，一艘悬挂利比里亚国旗的船只在保加利亚黑海沿岸被无人机击中后沉没</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-29/10722950.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网固原10月29日电 (记者 李佩珊)10月28日晚，“强国复兴有我”群众性主题宣传教育活动暨《长征组歌》大型交响合唱音乐会在固原市上演，各界干部群众齐聚现场，共赏红色经典，追忆峥嵘岁月，汲取奋进力量。" data-title="（长征胜利90周年）会师之地唱响长征赞歌 《长征组歌》唱响固原" data-date="10-29 21:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 21:11</span>
          <span class="news-item-title">（长征胜利90周年）会师之地唱响长征赞歌 《长征组歌》唱响固原</span>
          <span class="news-value-point">💡 中新网固原10月29日电 (记者 李佩珊)10月28日晚，“强国复兴有我”群众性主题宣传教育活动暨《长征组歌》大型交响合唱音乐会在固原市上演，各…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-29/10722978.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网哈尔滨10月29日电(记者 刘璐)“‘十五五’时期是绿色龙江建设夯实基础、承前启后、扩面提质的关键阶段，黑龙江省将锚定美丽中国先行区建设目标，既守护好‘大美山河’的生态底色，也办好‘小美生活’的民生实事，推动生态优势从绿色本底向绿色发展动能转变，持续筑牢祖国北方生态安全屏障。”10月29日，黑龙江省生态环境厅党组书记、厅长刘伟如是说。" data-title="黑龙江：以生态振兴激活绿色发展动能" data-date="10-29 21:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 21:08</span>
          <span class="news-item-title">黑龙江：以生态振兴激活绿色发展动能</span>
          <span class="news-value-point">💡 中新网哈尔滨10月29日电(记者 刘璐)“‘十五五’时期是绿色龙江建设夯实基础、承前启后、扩面提质的关键阶段，黑龙江省将锚定美丽中国先行区建设目…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/video/us/elections/100000011223984/the-red-states-that-could-decide-the-senate.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="民主党人需要翻转四个共和党参议院席位才能重新获得多数席位，但他们的一些目标在2024年特朗普总统以两位数获胜的州。我们的选举数据记者埃文·雷诺兹（ Evan Reynolds ）解释了这可能有多么困难。" data-title="The Red States That Could Decide the Senate" data-date="10-29 21:00" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-29 21:00</span>
          <span class="news-item-title">可以决定参议院的红州</span>
          <span class="news-item-title-en">The Red States That Could Decide the Senate</span>
          <span class="news-value-point">💡 民主党人需要翻转四个共和党参议院席位才能重新获得多数席位，但他们的一些目标在2024年特朗普总统以两位数获胜的州</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-29/10722981.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网广州10月29日电 (记者 王坚)据水利部珠江水利委员会(下称“珠江委”)29日消息，为落实西江流域水量分配方案和调度方案，强化西江流域水资源统一调度，珠江委组织编制了《2026-2027年度西江流域水资源调度计划》(简称《年度计划》)。《年度计划》近日经水利部批准下达，标志着西江流域2026-2027年度水资源统一调度正式启动实施。" data-title="2026-2027年度西江流域水资源调度计划获批下达" data-date="10-29 20:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 20:59</span>
          <span class="news-item-title">2026-2027年度西江流域水资源调度计划获批下达</span>
          <span class="news-value-point">💡 中新网广州10月29日电 (记者 王坚)据水利部珠江水利委员会(下称“珠江委”)29日消息，为落实西江流域水量分配方案和调度方案，强化西江流域水…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-29/10722936.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月29日电 综合消息：欧盟-加拿大峰会定于当地时间29日至30日在加拿大蒙特利尔举行。加拿大媒体称，双方预计30日发表的联合声明将删除给予加拿大欧盟“联席成员”身份的表述，改为呼吁建立“更紧密的联系”。" data-title="加媒称加拿大和欧盟联合声明将删去“联席成员”表述" data-date="10-29 20:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 20:15</span>
          <span class="news-item-title">加媒称加拿大和欧盟联合声明将删去“联席成员”表述</span>
          <span class="news-value-point">💡 中新网北京10月29日电 综合消息：欧盟-加拿大峰会定于当地时间29日至30日在加拿大蒙特利尔举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-29/10722963.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月29日电 据伊朗媒体报道，伊朗伊斯兰革命卫队当地时间29日发布声明称，在霍尔木兹海峡以西地区开展了一次进攻性电子战行动，成功控制一架美军间谍无人机，并使其安全降落。" data-title="伊朗伊斯兰革命卫队称捕获一架美军间谍无人机" data-date="10-29 20:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 20:13</span>
          <span class="news-item-title">伊朗伊斯兰革命卫队称捕获一架美军间谍无人机</span>
          <span class="news-value-point">💡 中新网10月29日电 据伊朗媒体报道，伊朗伊斯兰革命卫队当地时间29日发布声明称，在霍尔木兹海峡以西地区开展了一次进攻性电子战行动，成功控制一架…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-29/10722934.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间28日，以色列中央选举委员会公布了议会选举的初步计票结果。目前，以总理内塔尼亚胡领导的右翼阵营领先于前国防军总参谋长埃森科特领衔的反对派阵营，但双方均未达到议会多数席位。" data-title="以色列两大阵营均未获多数议席 不同组阁结果影响几何" data-date="10-29 19:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 19:44</span>
          <span class="news-item-title">以色列两大阵营均未获多数议席 不同组阁结果影响几何</span>
          <span class="news-value-point">💡 当地时间28日，以色列中央选举委员会公布了议会选举的初步计票结果</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-29/10722882.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月29日电 德国总统施泰因迈尔于10月27日至31日对中国进行国事访问。多家外媒对此进行了报道，称这表明德国高度重视对华关系。此次访问对于推进中德双方务实合作、挖掘更多发展机遇具有重要意义。" data-title="外媒聚焦：德国总统访华释放积极信号，中德务实合作前景广阔" data-date="10-29 18:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 18:55</span>
          <span class="news-item-title">外媒聚焦：德国总统访华释放积极信号，中德务实合作前景广阔</span>
          <span class="news-value-point">💡 中新网10月29日电 德国总统施泰因迈尔于10月27日至31日对中国进行国事访问</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-29/10722812.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月29日电 据英国《太阳报》28日报道，乌克兰总统泽连斯基在接受该媒体采访时表示，俄乌之间的和平谈判将在美国中期选举后数日内举行，此次谈判预计将由美国代表团牵头，在阿联酋阿布扎比举行。" data-title="泽连斯基：乌方愿进行任何形式的谈判，准备好讨论任何议题" data-date="10-29 16:51" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 16:51</span>
          <span class="news-item-title">泽连斯基：乌方愿进行任何形式的谈判，准备好讨论任何议题</span>
          <span class="news-value-point">💡 中新网10月29日电 据英国《太阳报》28日报道，乌克兰总统泽连斯基在接受该媒体采访时表示，俄乌之间的和平谈判将在美国中期选举后数日内举行，此次…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cqly0rmlde73o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="自1948 年建国以来，该国一直由联合政府执政，但下一届政府是否会包括现任总理内塔尼亚胡？" data-title="以色列大选结束，内塔尼亚胡能否执政为何依然悬而未决？" data-date="10-29 15:36" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-29 15:36</span>
          <span class="news-item-title">以色列大选结束，内塔尼亚胡能否执政为何依然悬而未决？</span>
          <span class="news-value-point">💡 自1948 年建国以来，该国一直由联合政府执政，但下一届政府是否会包括现任总理内塔尼亚胡</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-29/10722742.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月29日电 (记者 谢雁冰)中国外交部发言人郭嘉昆29日主持例行记者会。" data-title="外交部：敦促美方停止以人权为幌子干涉中国内政" data-date="10-29 15:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 15:28</span>
          <span class="news-item-title">外交部：敦促美方停止以人权为幌子干涉中国内政</span>
          <span class="news-value-point">💡 中新网北京10月29日电 (记者 谢雁冰)中国外交部发言人郭嘉昆29日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-29/10722741.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月29日电 (记者 谢雁冰 李京泽)中国外交部发言人郭嘉昆29日主持例行记者会。" data-title="中方再次敦促美方立即停止对古巴的封锁制裁" data-date="10-29 15:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 15:28</span>
          <span class="news-item-title">中方再次敦促美方立即停止对古巴的封锁制裁</span>
          <span class="news-value-point">💡 中新网北京10月29日电 (记者 谢雁冰 李京泽)中国外交部发言人郭嘉昆29日主持例行记者会</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/019/783.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 29 日消息，人工智能实验室扩散智能 (DiffuSpace) 昨日发布了其 Clover（三叶草）系列模型家族的首个成员：Clover-35B-A3B-Preview，并以 Apache 许可开源。Clover-35B-A3B-Preview 是一款采用 MoE 架构的扩散语言模型。与传统自回归模型不同的是，其具备“全局思维”，通过多轮迭代实现结果的从模糊到具体。DiffuSpace 表示，Clover-35B-A3B-Preview 的诞生证明扩散语言模型能在更大的参数尺度下与自回归模型竞争甚至略胜一筹，同时保持更快生成速度。该模型在多项基准测试中性能超过同规模的自回归模型 Qwen3.6-35B-A3B，尤其擅长智能体编程与工具使用任务。参考https://diff" data-title="DiffuSpace 推出 Clover-35B-A3B-Preview 扩散语言模型，兼顾性能与速度" data-date="10-29 22:33" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 22:33</span>
          <span class="news-item-title">DiffuSpace 推出 Clover-35B-A3B-Preview 扩散语言模型，兼顾性能与速度</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，人工智能实验室扩散智能 (DiffuSpace) 昨日发布了其 Clover（三叶草）系列模型家族的首个成员：…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/019/782.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 29 日消息，月之暗面今天在海外宣布，Kimi 现已接入谷歌 Gmail、Google Drive 和日历，用户可通过 Plugins（插件）页面启用。据官方介绍，用户现在可以总结 Gmail 邮件对话、查找 Google Drive 的文件，还能利用 Google 日历规划每日行程。所有操作均通过安全的 OAuth 授权机制进行。IT之家了解到，Kimi 插件是接入 Kimi AI 的外部工具与服务扩展，能够让 Kimi 在处理任务时直接调用第三方能力或自动化执行操作。" data-title="月之暗面 Kimi 接入谷歌 Gmail、云端硬盘和日历" data-date="10-29 22:27" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 22:27</span>
          <span class="news-item-title">月之暗面 Kimi 接入谷歌 Gmail、云端硬盘和日历</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，月之暗面今天在海外宣布，Kimi 现已接入谷歌 Gmail、Google Drive 和日历，用户可通过 Pl…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/019/781.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 29 日消息，微软于 10 月 28 日宣布推出 DirectX 12 Agility SDK 1.620 正式版和 1.722 预览版，为 DirectX 光线追踪（DXR）带来多项更新。新版预览 SDK 引入集群几何体（Clustered Geometry）、分区顶层加速结构（PTLAS）和间接加速结构构建等功能，旨在降低复杂动态场景的光追计算开销。微软称，这是 DXR 自 2018 年推出以来最重大的一次更新。传统光线追踪需要构建和更新加速结构，以便 GPU 快速判断光线与场景几何体的相交关系。这些结构通常采用包围体层次结构（BVH）等形式。在包含大量动画、几何体流式加载以及频繁变化物体的场景中，反复构建加速结构可能带来较大的计算开销。微软此次推出的集群几何体功能，" data-title="微软发布自 2018 年以来最大 DirectX 光追升级：AMD RX 9070 示例性能提升约 66 倍" data-date="10-29 22:27" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 22:27</span>
          <span class="news-item-title">微软发布自 2018 年以来最大 DirectX 光追升级：AMD RX 9070 示例性能提升约 66 倍</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，微软于 10 月 28 日宣布推出 DirectX 12 Agility SDK 1.620 正式版和 1.7…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/019/780.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 29 日消息，据中国医药创新促进会分享，10 月 24 日，由该会与香港交易所主办的第十一届医药创新与投资大会在南京召开。华为制药军团总裁樊杰出席大会并接受媒体采访。对于外界关心的华为是否会直接进入药物研发，樊杰明确表示：“华为不做药，也不做管线。”华为希望发挥自身在计算、通信和人工智能领域的优势，为药企、科研机构及 AI 制药企业提供算力、存储、网络、工具链和数据治理能力，成为 AI 制药产业的技术底座与生态支持者。在樊杰看来，AI 制药仍处于快速发展、市场预期较高的阶段。蛋白质结构预测、分子模拟等部分技术已进入实际应用，但整个药物研发链条尚未打通。下一阶段，行业需要回答的不只是模型规模有多大，而是模型能否进入真实研发流程，并与实验数据和研发决策形成闭环。樊杰表示，中国" data-title="华为制药军团总裁樊杰明确“华为不做药”，希望成为 AI 制药产业技术底座" data-date="10-29 22:24" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 22:24</span>
          <span class="news-item-title">华为制药军团总裁樊杰明确“华为不做药”，希望成为 AI 制药产业技术底座</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，据中国医药创新促进会分享，10 月 24 日，由该会与香港交易所主办的第十一届医药创新与投资大会在南京召开</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/nvidia-geforce-rtx-5080-prices-hit-usd2-000-costing-more-than-the-rtx-5090-did-at-launch-and-with-limited-stock-available-original-usd999-msrp-long-forgotten-with-prices-now-2-3x-higher" target="_blank" rel="noopener" data-cat="keji" data-summary="现在购买Nvidia GeForce RTX 5080的成本与RTX 5090的发布价格一样高，现在这款高规格GPU的价格至少高出两倍。" data-title="Nvidia GeForce RTX 5080 prices hit $2,000, costing more than the RTX 5090 did at launch and with limited stock available — original $999 MSRP long forgotten, with prices now 2-3x higher" data-date="10-29 22:21" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-29 22:21</span>
          <span class="news-item-title">Nvidia GeForce RTX 5080价格达到2,000 $ ，比RTX 5090推出时的价格更高，库存有限—原价999 $的建议零售价早已被遗忘，现在价格高出2-3倍</span>
          <span class="news-item-title-en">Nvidia GeForce RTX 5080 prices hit $2,000, costing more than the RTX 5090 did at launch and with limited stock available — original $999 MSRP long forgotten, with prices now 2-3x higher</span>
          <span class="news-value-point">💡 现在购买Nvidia GeForce RTX 5080的成本与RTX 5090的发布价格一样高，现在这款高规格GPU的价格至少高出两倍</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/podcast/1021322/anthropic-ipo-filing-s-1-claude-semianalysis-joey-brookhart-interview" target="_blank" rel="noopener" data-cat="keji" data-summary="今天在Decoder上，我与芯片和人工智能研究公司SemiAnalysis的分析师乔伊·布鲁克哈特（ Joey Brookhart ）一起，帮助我深入了解Anthropic IPO申请的数量—一份被称为S-1的文件。Anthropic刚刚提交了S-1申请" data-title="Anthropic is asking Wall Street to believe in AGI" data-date="10-29 22:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-29 22:00</span>
          <span class="news-item-title">Anthropic要求华尔街相信AGI</span>
          <span class="news-item-title-en">Anthropic is asking Wall Street to believe in AGI</span>
          <span class="news-value-point">💡 今天在Decoder上，我与芯片和人工智能研究公司SemiAnalysis的分析师乔伊·布鲁克哈特（ Joey Brookhart ）一起，帮助…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1022140/amazon-alexa-for-shopping-grocery-lists-gift-registries" target="_blank" rel="noopener" data-cat="keji" data-summary="亚马逊正在为其人工智能购物助手添加一些新功能，包括在购物清单和礼品登记处之间创建、编辑和移动商品的方式。例如，亚马逊表示，您现在可以要求Alexa购物“创建一个新的购物清单" data-title="Amazon’s AI shopping assistant can now edit your grocery lists and gift registries" data-date="10-29 21:52" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-29 21:52</span>
          <span class="news-item-title">亚马逊的人工智能购物助手现在可以编辑您的生鲜杂货清单和礼品登记</span>
          <span class="news-item-title-en">Amazon’s AI shopping assistant can now edit your grocery lists and gift registries</span>
          <span class="news-value-point">💡 亚马逊正在为其人工智能购物助手添加一些新功能，包括在购物清单和礼品登记处之间创建、编辑和移动商品的方式</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1022113/kevin-bates-arduboy-digital-candle-ai-simulate-flame" target="_blank" rel="noopener" data-cat="keji" data-summary="在设计了一个可以包裹在杂志上的俄罗斯方块的灵活版本之后， Kevin Bates的最新创作是一款数字蜡烛，它使用自定义的人工智能模型来精确地模拟LED网格上闪烁的火焰的外观。" data-title="This $149 digital candle uses AI to accurately simulate a flickering flame" data-date="10-29 21:37" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-29 21:37</span>
          <span class="news-item-title">这支$ 149的数字蜡烛使用人工智能精确模拟闪烁的火焰</span>
          <span class="news-item-title-en">This $149 digital candle uses AI to accurately simulate a flickering flame</span>
          <span class="news-value-point">💡 在设计了一个可以包裹在杂志上的俄罗斯方块的灵活版本之后， Kevin Bates的最新创作是一款数字蜡烛，它使用自定义的人工智能模型来精确地模拟…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1021476/anthropic-s-1-compute-recursive" target="_blank" rel="noopener" data-cat="keji" data-summary="Anthropic S-1似乎为公司在计算上花费尽可能多的资金提供了财务上的理由。如果你是那种想知道人类是否正在尽最大努力建立一个机器神，同时又相信" data-title="Anthropic’s business plan: Build God or die trying" data-date="10-29 21:30" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-29 21:30</span>
          <span class="news-item-title">Anthropic的商业计划：建立上帝或尝试死亡</span>
          <span class="news-item-title-en">Anthropic’s business plan: Build God or die trying</span>
          <span class="news-value-point">💡 Anthropic S-1似乎为公司在计算上花费尽可能多的资金提供了财务上的理由</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-29/10722990.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网上海10月29日电 (记者 陈静)AI与数学是什么关系？数学会因为AI消失吗？数学到底有没有用？2002年菲尔兹奖得主、法国科学院院士洛朗·拉福格(Laurent Lafforgue)28日在沪表示，数学家的文本是AI的源头，AI也会反过来改变数学被书写的方式。" data-title="菲尔兹奖得主洛朗·拉福格在沪谈AI、数学与人文" data-date="10-29 21:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 21:09</span>
          <span class="news-item-title">菲尔兹奖得主洛朗·拉福格在沪谈AI、数学与人文</span>
          <span class="news-value-point">💡 中新网上海10月29日电 (记者 陈静)AI与数学是什么关系</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/policy/nvidia-ceo-jensen-huang-may-have-been-the-target-of-a-spy-plot-through-chinese-intelligence-asset-report-claims-exec-from-firm-under-investigation-for-smuggling-banned-ai-chips-to-china-accused-of-being-a-spy-was-also-feeding-information-to-beijing" target="_blank" rel="noopener" data-cat="keji" data-summary="消息人士称， Nvidia云合作伙伴的高管Alice Huang与Jensen Huang关系密切，涉嫌向北京传递信息。" data-title="Nvidia CEO Jensen Huang may have been the target of a spy plot through &#39;Chinese intelligence asset,&#39; report claims" data-date="10-29 21:04" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-29 21:04</span>
          <span class="news-item-title">报告称，英伟达首席执行官黄延森可能是“中国情报资产”间谍阴谋的目标</span>
          <span class="news-item-title-en">Nvidia CEO Jensen Huang may have been the target of a spy plot through 'Chinese intelligence asset,' report claims</span>
          <span class="news-value-point">💡 消息人士称， Nvidia云合作伙伴的高管Alice Huang与Jensen Huang关系密切，涉嫌向北京传递信息</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/dept-of-justice-reportedly-probes-nvidia-over-usd13-billion-hugging-face-ai-platform-acquisition-concerns-raised-over-competition-in-ai-and-pressure-on-customers" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达(Nvidia)以近130亿美元收购Hugging Face的交易因担心这将影响人工智能领域的竞争而受到密切关注。" data-title="Dept of Justice reportedly probes Nvidia over $13 billion Hugging Face AI platform acquisition" data-date="10-29 20:49" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-29 20:49</span>
          <span class="news-item-title">据报道，司法部调查英伟达逾130亿美元收购Hugging Face AI平台</span>
          <span class="news-item-title-en">Dept of Justice reportedly probes Nvidia over $13 billion Hugging Face AI platform acquisition</span>
          <span class="news-value-point">💡 英伟达(Nvidia)以近130亿美元收购Hugging Face的交易因担心这将影响人工智能领域的竞争而受到密切关注</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/our-first-step-at-defining-a-cpu-benchmark-for-agentic-ai-how-we-can-measure-throughput-of-agentic-ai-workloads-without-any-gpu-involved" target="_blank" rel="noopener" data-cat="keji" data-summary="在过去的六个月中，随着代理AI工作负载的发展， CPU已成为焦点。这是我们在运行代理工作负载时尝试测量CPU性能的第一次尝试。" data-title="Our first step at defining a CPU benchmark for agentic AI" data-date="10-29 20:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-29 20:20</span>
          <span class="news-item-title">我们为agentic AI定义CPU基准的第一步</span>
          <span class="news-item-title-en">Our first step at defining a CPU benchmark for agentic AI</span>
          <span class="news-value-point">💡 在过去的六个月中，随着代理AI工作负载的发展， CPU已成为焦点</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/28/us/politics/trump-midterms-white-house-mood.html" target="_blank" rel="noopener" data-cat="keji" data-summary="在中期选举中，白宫一直被人员流动和焦虑所震撼。正如一位助手所说，总统正在收紧他的核心圈子，他猛烈抨击批评者，举行蜿蜒的集会，并以新闻剪辑和“人工智能污点”为食。" data-title="As Trump Faces Down the Midterms, a Grim Mood Takes Over the White House" data-date="10-29 20:18" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-29 20:18</span>
          <span class="news-item-title">随着特朗普面临中期选举，一种严峻的情绪接管了白宫</span>
          <span class="news-item-title-en">As Trump Faces Down the Midterms, a Grim Mood Takes Over the White House</span>
          <span class="news-value-point">💡 在中期选举中，白宫一直被人员流动和焦虑所震撼</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/fujifilm-plans-5x-production-boost-of-100tb-magnetic-storage-tapes-driven-by-ai-usd63-million-injection-is-the-largest-investment-in-tape-for-20-years" target="_blank" rel="noopener" data-cat="keji" data-summary="富士胶片计划将磁带的产量提高5倍，以满足人工智能数据中心存储的新需求。" data-title="Fujifilm plans 5x production boost of 100TB magnetic storage tapes driven by skyrocketing AI storage demand" data-date="10-29 19:40" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-29 19:40</span>
          <span class="news-item-title">富士胶片计划在人工智能存储需求飙升的推动下，将100TB磁带的产量提高5倍</span>
          <span class="news-item-title-en">Fujifilm plans 5x production boost of 100TB magnetic storage tapes driven by skyrocketing AI storage demand</span>
          <span class="news-value-point">💡 富士胶片计划将磁带的产量提高5倍，以满足人工智能数据中心存储的新需求</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13605331/manchester-united-michael-carrick-ready-to-move-forward-with-bruno-fernandes-as-captain-and-doesnt-require-assurances-on-his-future" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）表示，他已准备好与布鲁诺·费尔南德斯（ Bruno Fernandes ）一起担任曼联队" data-title="Carrick ready to &#39;move forward&#39; with Fernandes as captain" data-date="10-29 22:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 22:00</span>
          <span class="news-item-title">卡里克准备与费尔南德斯一起“前进”</span>
          <span class="news-item-title-en">Carrick ready to 'move forward' with Fernandes as captain</span>
          <span class="news-value-point">💡 迈克尔·卡里克（ Michael Carrick ）表示，他已准备好与布鲁诺·费尔南德斯（ Bruno Fernandes ）一起担任曼联队</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13605331/manchester-united-michael-carrick-ready-to-move-forward-with-bruno-fernandes-as-captain-and-doesnt-require-assurances-on-his-future" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）表示，他已准备好与布鲁诺·费尔南德斯（ Bruno Fernandes ）一起担任曼联队" data-title="Carrick ready to &#39;move forward&#39; with Fernandes as captain" data-date="10-29 22:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 22:00</span>
          <span class="news-item-title">卡里克准备与费尔南德斯一起“前进”</span>
          <span class="news-item-title-en">Carrick ready to 'move forward' with Fernandes as captain</span>
          <span class="news-value-point">💡 迈克尔·卡里克（ Michael Carrick ）表示，他已准备好与布鲁诺·费尔南德斯（ Bruno Fernandes ）一起担任曼联队</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cv2d6ze63gk2o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="背靠背降级到英格兰足球第三梯队变得越来越普遍，本赛季伯恩利可能会在卢顿镇和莱斯特之后成为帽子戏法。" data-title="Is the double drop from the Premier League becoming more common?" data-date="10-29 21:19" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-29 21:19</span>
          <span class="news-item-title">英超联赛的双降是否变得越来越普遍？</span>
          <span class="news-item-title-en">Is the double drop from the Premier League becoming more common?</span>
          <span class="news-value-point">💡 背靠背降级到英格兰足球第三梯队变得越来越普遍，本赛季伯恩利可能会在卢顿镇和莱斯特之后成为帽子戏法</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/articles/cwx2836e1mp7o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="BBC Sport的Ask Me Anything团队解释了本周末英超联赛的周日14:00 GMT开球在哪里。" data-title="Why is there only one Premier League match on Sunday?" data-date="10-29 20:47" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-29 20:47</span>
          <span class="news-item-title">为什么周日只有一场英超比赛？</span>
          <span class="news-item-title-en">Why is there only one Premier League match on Sunday?</span>
          <span class="news-value-point">💡 BBC Sport的Ask Me Anything团队解释了本周末英超联赛的周日14:00 GMT开球在哪里</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cjvgx0ek6rz2o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="加里·内维尔（ Gary Neville ）表示，由于曼联坚持与压力不足的老板迈克尔·卡里克（ Michael Carrick ）合作，有时需要“为了自己的利益”解雇经理。" data-title="Sometimes managers need sacking for own good" data-date="10-29 19:00" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-29 19:00</span>
          <span class="news-item-title">有时管理者需要为了自己的利益而解雇</span>
          <span class="news-item-title-en">Sometimes managers need sacking for own good</span>
          <span class="news-value-point">💡 加里·内维尔（ Gary Neville ）表示，由于曼联坚持与压力不足的老板迈克尔·卡里克（ Michael Carrick ）合作，有时需要…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/rugby-league/news/12040/13605180/rugby-league-world-cup-englands-brian-mcdermott-admits-side-face-unique-task-to-progress-and-cant-get-distracted" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="布莱恩·麦克德莫特（ Brian McDermott ）警告英格兰队不要追逐积分，因为他们希望在对阵巴布亚新几内亚的大胜中保持他们苗条的橄榄球联赛世界杯希望。" data-title="McDermott: England face &#39;unique task&#39; to progress and can&#39;t get distracted" data-date="10-29 19:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 19:00</span>
          <span class="news-item-title">麦克德莫特：英格兰面临进步的“独特任务” ，不能分心</span>
          <span class="news-item-title-en">McDermott: England face 'unique task' to progress and can't get distracted</span>
          <span class="news-value-point">💡 布莱恩·麦克德莫特（ Brian McDermott ）警告英格兰队不要追逐积分，因为他们希望在对阵巴布亚新几内亚的大胜中保持他们苗条的橄榄球联…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-29/10722874.shtml" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="中新网10月29日电 近日，效力于西甲皇家马德里俱乐部的法国球员姆巴佩发表涉华不当言论。事件持续发酵后，不少网友自发抵制，多个品牌官宣终止与其合作，相关平台也暂停了西甲赛事转播。北京时间10月27日，姆巴佩发布道歉声明。西甲联盟也于当日作出回应，称相关言论仅为球员个人观点，不代表西甲联盟立场，并向中国球迷致歉。10月28日，皇马俱乐部发布官方声明，就姆巴佩不当言论正式致歉，其中提到：我们将始终秉持尊重、共处及跨文化理解的价值观，并期待进一步加强与中国及其人民之间的友谊与情感纽带。" data-title="外媒关注姆巴佩不当言论事件 消息人士：西甲主席考虑前往中国" data-date="10-29 18:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 18:48</span>
          <span class="news-item-title">外媒关注姆巴佩不当言论事件 消息人士：西甲主席考虑前往中国</span>
          <span class="news-value-point">💡 中新网10月29日电 近日，效力于西甲皇家马德里俱乐部的法国球员姆巴佩发表涉华不当言论</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/cricket/news/12040/13604022/county-cricket-ins-and-outs-all-the-signings-departures-and-overseas-arrivals-ahead-of-the-2027-season" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="跟上2027赛季县板球的所有签约、出发和海外球员的步伐。" data-title="County cricket ins and outs 2027" data-date="10-29 18:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 18:00</span>
          <span class="news-item-title">2027年县板球进出</span>
          <span class="news-item-title-en">County cricket ins and outs 2027</span>
          <span class="news-value-point">💡 跟上2027赛季县板球的所有签约、出发和海外球员的步伐</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/basketball/news/12040/13605210/wnba-finals-game-6-live-on-sky-sports-thursday-at-4-30pm-as-golden-state-valkyries-vs-atlanta-dream-makes-history" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="周四，金州女武神队将在他们存在的第二年赢得WNBA总冠军，或者在天空体育上直播，或者亚特兰大之梦将迫使联盟历史上的第一场第7场比赛。" data-title="WNBA Finals set to make history: Watch Game 6 live on Sky Sports" data-date="10-29 16:23" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 16:23</span>
          <span class="news-item-title">WNBA总决赛将创造历史：在天空体育现场观看第6场比赛</span>
          <span class="news-item-title-en">WNBA Finals set to make history: Watch Game 6 live on Sky Sports</span>
          <span class="news-value-point">💡 周四，金州女武神队将在他们存在的第二年赢得WNBA总冠军，或者在天空体育上直播，或者亚特兰大之梦将迫使联盟历史上的第一场第7场比赛</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/29/tottenham-season-spurs-chelsea-win-table" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="马刺有一个糟糕的开局，但在切尔西取得令人印象深刻的胜利后，他们突然抬头看了看Opta Analyst的桌子，实际上只有三分。托特纳姆热刺上周六晚上在切尔西的2-0胜利是一个有益的推动力" data-title="Tottenham’s season has finally taken off. How far up the table can they go?" data-date="10-29 16:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-29 16:00</span>
          <span class="news-item-title">托特纳姆热刺的赛季终于起飞了。他们能在桌子上走多远？</span>
          <span class="news-item-title-en">Tottenham’s season has finally taken off. How far up the table can they go?</span>
          <span class="news-value-point">💡 马刺有一个糟糕的开局，但在切尔西取得令人印象深刻的胜利后，他们突然抬头看了看Opta Analyst的桌子，实际上只有三分</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025501/liverpool-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Liverpool latest: &#39;Only team I didn&#39;t want,&#39; says Iraola after drawing Bournemouth" data-title="Liverpool latest: &#39;Only team I didn&#39;t want,&#39; says Iraola after drawing Bournemouth" data-date="10-29 15:54" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 15:54</span>
          <span class="news-item-title">利物浦最新消息： “我唯一不想要的球队，” Iraola在绘制伯恩茅斯之后说道</span>
          <span class="news-item-title-en">Liverpool latest: 'Only team I didn't want,' says Iraola after drawing Bournemouth</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cx05487d6r9vo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="塔里克·穆哈雷莫维奇（ Tarik Muharemovic ）花费了利兹联（ Leeds United ）一笔“令人垂涎的”费用，给人留下了深刻的印象，以至于有些人担心俱乐部会" data-title="Chiellini guidance to Leeds &#39;rock&#39; - could Muharemovic be signing of season?" data-date="10-29 14:27" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-29 14:27</span>
          <span class="news-item-title">基耶利尼对利兹“摇滚”的指导-穆哈雷莫维奇会签下本赛季吗？</span>
          <span class="news-item-title-en">Chiellini guidance to Leeds 'rock' - could Muharemovic be signing of season?</span>
          <span class="news-value-point">💡 塔里克·穆哈雷莫维奇（ Tarik Muharemovic ）花费了利兹联（ Leeds United ）一笔“令人垂涎的”费用，给人留下了深刻…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13605140/liverpool-transfer-news-reds-make-contact-with-lamine-camara-camp-ahead-of-proposed-january-move-for-monaco-midfielder-paper-talk" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="周四报纸的热门报道和转移谣言..." data-title="Papers: Liverpool make contact with Monaco midfielder Camara" data-date="10-29 07:20" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 07:20</span>
          <span class="news-item-title">论文：利物浦与摩纳哥中场卡马拉取得联系</span>
          <span class="news-item-title-en">Papers: Liverpool make contact with Monaco midfielder Camara</span>
          <span class="news-value-point">💡 周四报纸的热门报道和转移谣言...</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13605014/vincent-kompany-bayern-munich-head-coach-discharged-from-hospital-after-collapsing-at-training" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="拜仁慕尼黑主教练文森特·康帕尼（ Vincent Kompany ）上周因脑膜刺激而在训练中瘫痪后出院，体育董事会成员马克斯·埃伯尔（ Max Eberl ）周三表示。" data-title="Kompany discharged from hospital after collapsing at training" data-date="10-29 06:40" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 06:40</span>
          <span class="news-item-title">Kompany在训练时晕倒后出院</span>
          <span class="news-item-title-en">Kompany discharged from hospital after collapsing at training</span>
          <span class="news-value-point">💡 拜仁慕尼黑主教练文森特·康帕尼（ Vincent Kompany ）上周因脑膜刺激而在训练中瘫痪后出院，体育董事会成员马克斯·埃伯尔（ Max …</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/arsenal-women-vs-benfica-women/report/578250" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿莱西亚·鲁索（ Alessia Russo ）成为女子冠军联赛历史上最高的英国射手，他对本菲卡（ Benfica ）进行了帽子戏法，因为阿森纳（ Arsenal ）在联赛阶段的比赛中以3-0获胜。" data-title="History-maker Russo scores hat-trick as Arsenal dismiss Benfica" data-date="10-29 06:10" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 06:10</span>
          <span class="news-item-title">历史悠久的Russo在阿森纳解雇本菲卡时为帽子戏法得分</span>
          <span class="news-item-title-en">History-maker Russo scores hat-trick as Arsenal dismiss Benfica</span>
          <span class="news-value-point">💡 阿莱西亚·鲁索（ Alessia Russo ）成为女子冠军联赛历史上最高的英国射手，他对本菲卡（ Benfica ）进行了帽子戏法，因为阿森纳…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theverge.com/gadgets/1022103/ocarina-of-time-remake-apple-mac-mini-ssd-hdmi-dock-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="期待已久的《塞尔达传说： Nintendo Switch 2时间之笛》重制版将于11月5日星期四推出。换句话说，您还有一周的时间在亚马逊和沃尔玛享受10 $的折扣。" data-title="There’s one week left to preorder the Ocarina of Time remake for $10 off" data-date="10-29 22:24" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-29 22:24</span>
          <span class="news-item-title">距离预购《时光之笛》翻拍仅剩一周，立减$ 10</span>
          <span class="news-item-title-en">There’s one week left to preorder the Ocarina of Time remake for $10 off</span>
          <span class="news-value-point">💡 期待已久的《塞尔达传说： Nintendo Switch 2时间之笛》重制版将于11月5日星期四推出</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/019/779.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 29 日消息，CORSAIR（海盗船）当地时间今日宣布与 Embark Studios 合作，携主品牌与旗下 SCUF、Elgato 推出多款《ARC Raiders》（弧光猎人）联名硬件，庆祝这款多人在线射击游戏发售一周年。此次联名产品阵容涵盖 SCUF 的三款手柄控制器，海盗船 CLIPPER PRO MINI 60 磁轴键盘、SABRE v2 PRO Wireless MG 镁合金鼠标、HS80 RGB WIRELESS 耳机、MM Anti-Fray Cloth 鼠标垫，Elgato Stream Deck MK.2 直播控台。这些款式均采用《ARC Raiders》标志性的四条纹配色，购买即可解锁专属游戏内物品。" data-title="庆祝《ARC Raiders》发售一周年，海盗船携旗下品牌推出联名外设" data-date="10-29 22:15" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 22:15</span>
          <span class="news-item-title">庆祝《ARC Raiders》发售一周年，海盗船携旗下品牌推出联名外设</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，CORSAIR（海盗船）当地时间今日宣布与 Embark Studios 合作，携主品牌与旗下 SCUF、El…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/019/777.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 29 日消息，据游戏媒体 GamesRadar 今天报道，在《GTA6》的雷奥奈达州，玩家即使不开车也能相当方便地出行。游戏中拥有一套完整的公共交通系统，巴士、火车将按照固定路线和时刻表运行。据报道，玩家在雷奥奈达州探索时不只可以选择汽车、电动滑板车或船只。Rockstar 为游戏打造了一整套公共交通网络，覆盖整个雷奥奈达州。例如，游戏中的公交车将按照固定路线图行驶，运行时刻表也是有的。据 Rockstar 开发人员 Phil Hooker 透露，他测试游戏时经常会在车站等车，检查巴士是否准时到站，然后乘车游览城市。总的来说，公交和铁路网络可能会让雷奥奈达州更像是真实城市，玩家可以坐在车上，以不同的方式消磨时间。IT之家注意到，公共交通在《GTA》系列游戏中并不是新鲜事物" data-title="《GTA6》游戏公共交通系统详解：火车、巴士有固定路线和时刻表" data-date="10-29 22:06" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 22:06</span>
          <span class="news-item-title">《GTA6》游戏公共交通系统详解：火车、巴士有固定路线和时刻表</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，据游戏媒体 GamesRadar 今天报道，在《GTA6》的雷奥奈达州，玩家即使不开车也能相当方便地出行</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/019/776.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 29 日消息，苹果北京时间今日发布了 MacBook Pro (PROLED XDR 显示屏)。在首款 OLED MacBook 产品面世后，研调机构 TrendForce（集邦）发布了对整体 OLED 笔电市场的最新预测。机构认为，配备 OLED 屏幕的笔记本电脑整机出货量在 2026~2030 年期间维持超 30% 的同比增幅，其中 2027~2029 年增长都将超过 40%；出货总量将从今年的 1260 万台增长至期末的 4660 万台。▲ 图源：TrendForce针对 OLED MacBook Pro，机构的看法是其短期内需求动能将受到高价定位与产品重叠的限制，但长远来看有助于进一步巩固苹果高端产品的技术形象与溢价定位。该机型 2027 年预计可出货 120~1" data-title="TrendForce 预测：全球 OLED 笔电出货量有望在中期维持超 30% 年增幅" data-date="10-29 22:05" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 22:05</span>
          <span class="news-item-title">TrendForce 预测：全球 OLED 笔电出货量有望在中期维持超 30% 年增幅</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，苹果北京时间今日发布了 MacBook Pro (PROLED XDR 显示屏)</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/desktops/gaming-pcs/hyperx-omen-35l-review" target="_blank" rel="noopener" data-cat="zonghe" data-summary="优质的造型、安静的操作和令人印象深刻的性能使HyperX Omen 35L与市场上最好的产品竞争。但是，是否物有所值取决于您选择的配置。" data-title="HyperX Omen 35L review: A polished gaming PC for deep pockets" data-date="10-29 22:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-29 22:00</span>
          <span class="news-item-title">HyperX Omen 35L评论：一款抛光的游戏PC ，口袋更深</span>
          <span class="news-item-title-en">HyperX Omen 35L review: A polished gaming PC for deep pockets</span>
          <span class="news-value-point">💡 优质的造型、安静的操作和令人印象深刻的性能使HyperX Omen 35L与市场上最好的产品竞争</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c95ynv03lmk8o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这场造成168人死亡的大火发生将近一年后，香港特首李家超首次率领官员鞠躬道歉。" data-title="香港宏福苑大火报告公开：特首率官员鞠躬道歉，房屋局长请辞" data-date="10-29 21:51" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-29 21:51</span>
          <span class="news-item-title">香港宏福苑大火报告公开：特首率官员鞠躬道歉，房屋局长请辞</span>
          <span class="news-value-point">💡 这场造成168人死亡的大火发生将近一年后，香港特首李家超首次率领官员鞠躬道歉</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/019/775.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 29 日消息，SpaceX 在筹备星舰第 15 次试飞的路上又完成了一项重要里程碑，这次试飞有望极具看点。该公司于当地时间 10 月 26 日（周一）、27 日（周二）开展了星舰上面级的静态点火测试，被称为 Ship 42 的箭体固定在地面，点燃多台猛禽发动机。SpaceX 在 10 月 28 日（周三）于 X 平台发布测试视频并写道：“Ship 42 静态点火全部完成。备战第 15 飞的星舰完成了全时长六台发动机的静态点火，还单独点燃了一台猛禽发动机，模拟离轨制动点火。”在 Ship 42 测试之前，本次试飞配套的超重型助推器 Booster 22 已经顺利完成 33 台发动机同步静态点火。从目前进度来看，第 15 次试飞一切按计划推进。SpaceX 创始人兼首席执行官" data-title="SpaceX 星舰完成上面级静态点火测试，准备进行第 15 次试飞" data-date="10-29 21:50" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 21:50</span>
          <span class="news-item-title">SpaceX 星舰完成上面级静态点火测试，准备进行第 15 次试飞</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，SpaceX 在筹备星舰第 15 次试飞的路上又完成了一项重要里程碑，这次试飞有望极具看点</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-29/10723014.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="央视网消息(新闻联播)：前三季度，我国铁路货运量稳步增长，物流产品不断丰富，通道效率显著提升。" data-title="我国铁路物流提质增效步伐加快" data-date="10-29 21:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 21:48</span>
          <span class="news-item-title">我国铁路物流提质增效步伐加快</span>
          <span class="news-value-point">💡 央视网消息(新闻联播)：前三季度，我国铁路货运量稳步增长，物流产品不断丰富，通道效率显著提升</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-29/10723005.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社上海10月29日电 (李姝征 狄权)2026智元创新日29日在上海举行，吸引来自全球各地的逾千名科研伙伴、开发者、商业伙伴参与。会场里，海外客商既了解机器人具备哪些新本领，也寻找能够带回国、解决实际问题的机器人“工友”。" data-title="海外客商在上海寻找机器人“工友”" data-date="10-29 21:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 21:27</span>
          <span class="news-item-title">海外客商在上海寻找机器人“工友”</span>
          <span class="news-value-point">💡 中新社上海10月29日电 (李姝征 狄权)2026智元创新日29日在上海举行，吸引来自全球各地的逾千名科研伙伴、开发者、商业伙伴参与</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/report/1022013/apple-touchscreen-macbook-pro-toaster-refrigerator" target="_blank" rel="noopener" data-cat="zonghe" data-summary="15多年来，苹果对触摸屏MacBook的想法有一个非常简单的答案：否。昨天，苹果终于决定改变想法，并宣布了一个。“你必须触摸它才能相信它，”苹果首席执行官约翰·特纳斯（ John Ternus ）说。他" data-title="Apple finally combined a toaster and a refrigerator" data-date="10-29 21:21" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-29 21:21</span>
          <span class="news-item-title">苹果终于把烤面包机和冰箱结合起来</span>
          <span class="news-item-title-en">Apple finally combined a toaster and a refrigerator</span>
          <span class="news-value-point">💡 15多年来，苹果对触摸屏MacBook的想法有一个非常简单的答案：否</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-29/10722997.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网满洲里10月29日电 题：跨国“串门”说走就走，2026年满洲里口岸出入境人员破110万人次" data-title="跨国“串门”说走就走，2026年满洲里口岸出入境人员破110万人次" data-date="10-29 21:19" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 21:19</span>
          <span class="news-item-title">跨国“串门”说走就走，2026年满洲里口岸出入境人员破110万人次</span>
          <span class="news-value-point">💡 中新网满洲里10月29日电 题：跨国“串门”说走就走，2026年满洲里口岸出入境人员破110万人次</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-29/10722993.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网太原10月29日电 (杨杰英 杨润德 王惠林)难老泉复流后，泉水如何有序调配一直受到关注。记者29日从山西省太原市晋源区水务局获悉，晋祠泉域保护与生态修复综合治理工程项目已进入社会稳定风险评估征询公众意见公示阶段，复流后的难老泉水往哪流有了新进展。" data-title="难老泉复流后水往哪流？晋祠泉域保护与生态修复工程进入公示阶段" data-date="10-29 21:18" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 21:18</span>
          <span class="news-item-title">难老泉复流后水往哪流？晋祠泉域保护与生态修复工程进入公示阶段</span>
          <span class="news-value-point">💡 中新网太原10月29日电 (杨杰英 杨润德 王惠林)难老泉复流后，泉水如何有序调配一直受到关注</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-29/10722996.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="夜幕落下，汴河灯火流光，一场网络辟谣主题宣传活动，正在古城开封铺开。" data-title="一堂开进古都的辟谣课，为何让人着迷？" data-date="10-29 21:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 21:14</span>
          <span class="news-item-title">一堂开进古都的辟谣课，为何让人着迷？</span>
          <span class="news-value-point">💡 夜幕落下，汴河灯火流光，一场网络辟谣主题宣传活动，正在古城开封铺开</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-29/10722992.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网梧州10月29日电 题：广西梧州六堡茶：生态淬炼好茶 借运河香飘东盟" data-title="广西梧州六堡茶：生态淬炼好茶 借运河香飘东盟" data-date="10-29 21:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 21:10</span>
          <span class="news-item-title">广西梧州六堡茶：生态淬炼好茶 借运河香飘东盟</span>
          <span class="news-value-point">💡 中新网梧州10月29日电 题：广西梧州六堡茶：生态淬炼好茶 借运河香飘东盟</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/29/deepgram-acquires-pipecat-maker-daily-to-bolster-its-voice-ai-infrastructure/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Deepgram表示，它致力于保持Pipecat的开源。" data-title="Deepgram acquires Pipecat-maker Daily to bolster its voice AI infrastructure" data-date="10-29 21:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-29 21:00</span>
          <span class="news-item-title">Deepgram收购Pipecat制造商Daily ，以加强其语音人工智能基础设施</span>
          <span class="news-item-title-en">Deepgram acquires Pipecat-maker Daily to bolster its voice AI infrastructure</span>
          <span class="news-value-point">💡 Deepgram表示，它致力于保持Pipecat的开源</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-29 22:34（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
