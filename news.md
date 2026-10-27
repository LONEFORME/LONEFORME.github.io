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
      <span>2026-10-28 02:07 抓取更新</span>
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
        <span class="channel-count">12</span>
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
  <div class="ov-item"><span class="ov-num">57</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">10</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×14 · 天空体育×12</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.nytimes.com/2026/10/25/world/middleeast/israel-election-guide-netanyahu-eisenkot.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="以色列人将于周二前往投票站进行选举，以决定该国的下一任总理。但组建新政府可能需要数周、数月或更长时间。" data-title="Israel’s High-Stakes Election: What to Know" data-date="10-28 01:16" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 10-28 01:16</span>
      </div>
      <h2 class="hero-featured-title">以色列高风险选举：须知</h2>
      <div class="hero-featured-title-en">Israel’s High-Stakes Election: What to Know</div>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.theverge.com/ai-artificial-intelligence/1017064/visionquest-marvel-rogue-ai" target="_blank" rel="noopener" data-cat="keji" data-summary="在漫威的VisionQuest中，一个超级强大的机器人试图通过迷失在精心制作的数字白日梦中来更好地了解人类，在这些白日梦中，他和其他人工智能驱动的生物一起生活在一个家中。这个系列非常梦幻，" data-title="VisionQuest is what happens when AI really goes rogue" data-date="10-28 01:30" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">VisionQuest is what happens when AI really goes rogue</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/football/news/12040/13604361/michael-carrick-why-man-utd-head-coach-will-stay-on-and-could-bruno-fernandes-play-vs-chelsea-plus-other-key-questions" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）有机会扭转曼联的局面-这一令人震惊的决定使支持者和天空体育的专家意见分歧。" data-title="&#39;Delaying the inevitable&#39; or right call? Key questions as Carrick stays" data-date="10-27 22:40" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">'Delaying the inevitable' or right call? Key questions as Carrick stays</p>
    </a>
    <a class="hero-sub-card" href="https://www.tomshardware.com/laptops/military-drone-outfit-anduril-partners-with-qualcomm-to-build-laptops-on-us-soil-with-new-bluechip-venture-defense-contractor-targets-a-100-percent-domestic-supply-chain-in-the-future" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这家国防承包商的目标是全面恢复美国海岸的笔记本电脑制造，其首批BlueChip笔记本电脑原型机的采购成本90%来自美国和其他盟国的供应商。" data-title="Military drone outfit Anduril partners with Qualcomm to build laptops on US soil with new BlueChip venture" data-date="10-28 01:42" data-source="Tom's Hardware">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
      </div>
      <p class="hero-sub-title">Military drone outfit Anduril partners with Qualcomm to build laptops on US soil with new BlueChip venture</p>
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
        <a class="news-item" href="https://www.nytimes.com/2026/10/25/world/middleeast/israel-election-guide-netanyahu-eisenkot.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="以色列人将于周二前往投票站进行选举，以决定该国的下一任总理。但组建新政府可能需要数周、数月或更长时间。" data-title="Israel’s High-Stakes Election: What to Know" data-date="10-28 01:16" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-28 01:16</span>
          <span class="news-item-title">以色列高风险选举：须知</span>
          <span class="news-item-title-en">Israel’s High-Stakes Election: What to Know</span>
          <span class="news-value-point">💡 以色列人将于周二前往投票站进行选举，以决定该国的下一任总理</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/27/climate/trump-methane-rules-epa-greenhouse-gas.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="拜登政府曾试图打击甲烷泄漏，这是气候变化的主要驱动因素。这些规则现在正在缩减。" data-title="E.P.A. to Loosen Methane Rules for Oil Firms" data-date="10-28 01:08" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-28 01:08</span>
          <span class="news-item-title">美国环保署放宽石油公司的甲烷规则</span>
          <span class="news-item-title-en">E.P.A. to Loosen Methane Rules for Oil Firms</span>
          <span class="news-value-point">💡 拜登政府曾试图打击甲烷泄漏，这是气候变化的主要驱动因素</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-28/10721960.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="巴西联邦最高法院法官弗拉维奥·迪诺27日作出裁定，要求巴西联邦警察就巴西总统选举中败选的自由党候选人弗拉维奥·博索纳罗在竞选活动中涉嫌接受外国资金和操纵社交媒体一事展开调查。" data-title="巴西联邦最高法院要求调查博索纳罗涉嫌接受外国资金" data-date="10-28 00:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-28 00:26</span>
          <span class="news-item-title">巴西联邦最高法院要求调查博索纳罗涉嫌接受外国资金</span>
          <span class="news-value-point">💡 巴西联邦最高法院法官弗拉维奥·迪诺27日作出裁定，要求巴西联邦警察就巴西总统选举中败选的自由党候选人弗拉维奥·博索纳罗在竞选活动中涉嫌接受外国资…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-27/10721958.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社首尔10月27日电 (记者 金旭)当地时间27日，韩国最高法院以“存在毁灭证据或潜逃的可能性”为由，签发对韩国前总统尹锡悦妻子金建希的追加逮捕令。金建希原定于10月31日到期的羁押期限将暂时延长两个月，至今年年底。" data-title="韩国前总统尹锡悦妻子金建希将被羁押至年底" data-date="10-27 23:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-27 23:48</span>
          <span class="news-item-title">韩国前总统尹锡悦妻子金建希将被羁押至年底</span>
          <span class="news-value-point">💡 中新社首尔10月27日电 (记者 金旭)当地时间27日，韩国最高法院以“存在毁灭证据或潜逃的可能性”为由，签发对韩国前总统尹锡悦妻子金建希的追加…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/27/health/shuford-cdc-resign.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="备受尊敬的德克萨斯州前卫生官员詹妮弗·舒福德博士被特朗普总统任命，以帮助稳定该机构。" data-title="Trump-Appointed CDC Deputy Director Jennifer Shuford Resigns After 4 Months" data-date="10-27 23:07" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-27 23:07</span>
          <span class="news-item-title">特朗普任命的CDC副主任Jennifer Shuford在4个月后辞职</span>
          <span class="news-item-title-en">Trump-Appointed CDC Deputy Director Jennifer Shuford Resigns After 4 Months</span>
          <span class="news-value-point">💡 备受尊敬的德克萨斯州前卫生官员詹妮弗·舒福德博士被特朗普总统任命，以帮助稳定该机构</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-27/10721918.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月27日电 综合外媒报道，伊朗海军当地时间27日表示，一艘油轮试图通过霍尔木兹海峡东部禁航区，发生了触雷和起火事故。" data-title="伊朗：一油轮在霍尔木兹海峡东部触雷起火" data-date="10-27 21:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-27 21:45</span>
          <span class="news-item-title">伊朗：一油轮在霍尔木兹海峡东部触雷起火</span>
          <span class="news-value-point">💡 中新网10月27日电 综合外媒报道，伊朗海军当地时间27日表示，一艘油轮试图通过霍尔木兹海峡东部禁航区，发生了触雷和起火事故</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-27/10721917.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月27日电 综合报道，乌克兰总统泽连斯基27日在社交媒体发文称，俄罗斯军队对乌克兰基础设施的袭击“严重升级”。" data-title="泽连斯基：俄军对乌基础设施袭击“严重升级”" data-date="10-27 21:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-27 21:44</span>
          <span class="news-item-title">泽连斯基：俄军对乌基础设施袭击“严重升级”</span>
          <span class="news-value-point">💡 中新网10月27日电 综合报道，乌克兰总统泽连斯基27日在社交媒体发文称，俄罗斯军队对乌克兰基础设施的袭击“严重升级”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-27/10721868.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月27日电 加拉加斯消息：委内瑞拉代总统德尔西·罗德里格斯当地时间26日表示，委政府正推进司法改革，致力于提高司法体系的独立性和透明度，主张对委制裁、推动外部干预的人士应反思自身立场。" data-title="委内瑞拉推进司法改革 最高法院改组工作取得进展" data-date="10-27 21:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-27 21:12</span>
          <span class="news-item-title">委内瑞拉推进司法改革 最高法院改组工作取得进展</span>
          <span class="news-value-point">💡 中新网北京10月27日电 加拉加斯消息：委内瑞拉代总统德尔西·罗德里格斯当地时间26日表示，委政府正推进司法改革，致力于提高司法体系的独立性和透…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-27/10721867.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月27日电 据市场监管总局网站消息，近日，市场监管总局发布JJF 2422—2026《尿量仪校准规范》国家计量技术规范(以下简称《规范》)，补齐我国尿量仪计量校准的技术短板，进一步织密重症医疗民生计量监管网络。" data-title="划定三项评价维度 市场监管总局发布《尿量仪校准规范》" data-date="10-27 21:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-27 21:01</span>
          <span class="news-item-title">划定三项评价维度 市场监管总局发布《尿量仪校准规范》</span>
          <span class="news-value-point">💡 中新网10月27日电 据市场监管总局网站消息，近日，市场监管总局发布JJF 2422—2026《尿量仪校准规范》国家计量技术规范(以下简称《规范…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-27/10721847.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社莫斯科10月27日电 俄罗斯总统普京27日应约与芬兰总统斯图布、挪威首相斯特勒通电话，就解决乌克兰危机等议题交换意见。" data-title="普京与芬兰、挪威领导人通话讨论乌克兰危机" data-date="10-27 20:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-27 20:54</span>
          <span class="news-item-title">普京与芬兰、挪威领导人通话讨论乌克兰危机</span>
          <span class="news-value-point">💡 中新社莫斯科10月27日电 俄罗斯总统普京27日应约与芬兰总统斯图布、挪威首相斯特勒通电话，就解决乌克兰危机等议题交换意见</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-27/10721820.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社浙江台州10月27日电 (周健)2026和合文化论坛27日在浙江省台州市天台县开幕。来自全球23个国家和地区的220余位政界、学界代表与会，以“和合”为媒，凝聚全球共识、汇聚全球智慧。" data-title="2026和合文化论坛开幕 海内外人士共话全球治理之道" data-date="10-27 19:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-27 19:39</span>
          <span class="news-item-title">2026和合文化论坛开幕 海内外人士共话全球治理之道</span>
          <span class="news-value-point">💡 中新社浙江台州10月27日电 (周健)2026和合文化论坛27日在浙江省台州市天台县开幕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-27/10721788.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京10月27日电 10月27日，国家主席习近平向日本前首相福田康夫遗属致唁电，对福田康夫逝世表示哀悼，向其遗属表示慰问。" data-title="习近平向日本前首相福田康夫遗属致唁电" data-date="10-27 19:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-27 19:03</span>
          <span class="news-item-title">习近平向日本前首相福田康夫遗属致唁电</span>
          <span class="news-value-point">💡 新华社北京10月27日电 10月27日，国家主席习近平向日本前首相福田康夫遗属致唁电，对福田康夫逝世表示哀悼，向其遗属表示慰问</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-27/10721787.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京10月27日电 10月27日，国家主席习近平致电卢拉，祝贺他当选连任巴西联邦共和国总统。" data-title="习近平致电祝贺卢拉当选连任巴西总统" data-date="10-27 19:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-27 19:02</span>
          <span class="news-item-title">习近平致电祝贺卢拉当选连任巴西总统</span>
          <span class="news-value-point">💡 新华社北京10月27日电 10月27日，国家主席习近平致电卢拉，祝贺他当选连任巴西联邦共和国总统</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-27/10721759.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社快讯：习近平致电祝贺卢拉当选连任巴西总统。" data-title="习近平致电祝贺卢拉当选连任巴西总统" data-date="10-27 18:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-27 18:04</span>
          <span class="news-item-title">习近平致电祝贺卢拉当选连任巴西总统</span>
          <span class="news-value-point">💡 新华社快讯：习近平致电祝贺卢拉当选连任巴西总统</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-27/10721761.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社快讯：习近平向日本前首相福田康夫遗属致唁电。" data-title="习近平向日本前首相福田康夫遗属致唁电" data-date="10-27 18:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-27 18:03</span>
          <span class="news-item-title">习近平向日本前首相福田康夫遗属致唁电</span>
          <span class="news-value-point">💡 新华社快讯：习近平向日本前首相福田康夫遗属致唁电</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1017064/visionquest-marvel-rogue-ai" target="_blank" rel="noopener" data-cat="keji" data-summary="在漫威的VisionQuest中，一个超级强大的机器人试图通过迷失在精心制作的数字白日梦中来更好地了解人类，在这些白日梦中，他和其他人工智能驱动的生物一起生活在一个家中。这个系列非常梦幻，" data-title="VisionQuest is what happens when AI really goes rogue" data-date="10-28 01:30" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-28 01:30</span>
          <span class="news-item-title">VisionQuest是当人工智能真正变成流氓时会发生什么</span>
          <span class="news-item-title-en">VisionQuest is what happens when AI really goes rogue</span>
          <span class="news-value-point">💡 在漫威的VisionQuest中，一个超级强大的机器人试图通过迷失在精心制作的数字白日梦中来更好地了解人类，在这些白日梦中，他和其他人工智能驱动…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/27/frontier-ai-labs-say-their-models-refuted-the-exponential-time-hypothesis-what-does-that-mean/" target="_blank" rel="noopener" data-cat="keji" data-summary="TechCrunch采访了负责解释OpenAI最新发现的麻省理工学院计算机科学家" data-title="Frontier AI labs say their models refuted the Exponential Time Hypothesis. What does that mean?" data-date="10-28 01:08" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-28 01:08</span>
          <span class="news-item-title">前沿人工智能实验室表示，他们的模型驳斥了指数时间假说。这是什么意思？</span>
          <span class="news-item-title-en">Frontier AI labs say their models refuted the Exponential Time Hypothesis. What does that mean?</span>
          <span class="news-value-point">💡 TechCrunch采访了负责解释OpenAI最新发现的麻省理工学院计算机科学家</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1019470/anthropic-ipo-resist-investor-pressure-cut-corners-safety" target="_blank" rel="noopener" data-cat="keji" data-summary="Anthropic希望两者兼得。随着即将进行的首次公开募股，它希望利用公共市场的巨大财富，并坚称它不想妥协其安全开发人工智能并造福人类的核心使命。但更大的模式" data-title="Anthropic’s elaborate plan to keep Wall Street at bay" data-date="10-28 00:51" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-28 00:51</span>
          <span class="news-item-title">Anthropic让华尔街陷入困境的精心计划</span>
          <span class="news-item-title-en">Anthropic’s elaborate plan to keep Wall Street at bay</span>
          <span class="news-value-point">💡 Anthropic希望两者兼得</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/27/googles-genie-4-world-model-adds-audio-more-realistic-worlds-and-real-time-steering/" target="_blank" rel="noopener" data-cat="keji" data-summary="Google DeepMind发布了Genie 4 ，这是一个具有实时音频、更真实模拟和中间模拟文本提示的世界模型，可供值得信赖的测试人员进行研究预览。" data-title="Google’s Genie 4 world model adds audio, more realistic worlds, and real" data-date="10-28 00:30" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-28 00:30</span>
          <span class="news-item-title">谷歌的Genie 4世界模型增加了音频，更逼真的世界和真实的</span>
          <span class="news-item-title-en">Google’s Genie 4 world model adds audio, more realistic worlds, and real</span>
          <span class="news-value-point">💡 Google DeepMind发布了Genie 4 ，这是一个具有实时音频、更真实模拟和中间模拟文本提示的世界模型，可供值得信赖的测试人员进行研…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1019551/firefox-smart-window-ai-fill-forms" target="_blank" rel="noopener" data-cat="keji" data-summary="Mozilla正在更新智能窗口（ Firefox的人工智能浏览体验） ，其新功能可以帮助您根据打开的标签页填写在线表单。例如， Mozilla表示智能窗口可以从您的在线投资组合中提取信息" data-title="Firefox’s Smart Window adds AI form filling and webpage monitoring" data-date="10-28 00:14" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-28 00:14</span>
          <span class="news-item-title">Firefox的智能窗口增加了AI表单填写和网页监控功能</span>
          <span class="news-item-title-en">Firefox’s Smart Window adds AI form filling and webpage monitoring</span>
          <span class="news-value-point">💡 Mozilla正在更新智能窗口（ Firefox的人工智能浏览体验） ，其新功能可以帮助您根据打开的标签页填写在线表单</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/27/well/ai-chatgpt-medication-epilepsy-death.html" target="_blank" rel="noopener" data-cat="keji" data-summary="聊天机器人帮助一名妇女逐渐戒掉了一种拯救生命的药物，并向她的医生隐瞒了这一计划，这些建议带来了毁灭性的后果。" data-title="ChatGPT’s Advice to Cut Her Seizure Drug Led to Devastating Consequences" data-date="10-28 00:09" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-28 00:09</span>
          <span class="news-item-title">ChatGPT关于减少癫痫药物的建议导致了毁灭性的后果</span>
          <span class="news-item-title-en">ChatGPT’s Advice to Cut Her Seizure Drug Led to Devastating Consequences</span>
          <span class="news-value-point">💡 聊天机器人帮助一名妇女逐渐戒掉了一种拯救生命的药物，并向她的医生隐瞒了这一计划，这些建议带来了毁灭性的后果</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1019076/google-genie-4-ai-model" target="_blank" rel="noopener" data-cat="keji" data-summary="谷歌今天宣布推出使用人工智能生成交互式体验的Genie 4世界模型。该公司表示，该模型有四个主要更新：它允许更逼真的世界，允许用户使用自然语言实时更新体验" data-title="Google’s next Genie AI model generates more realistic experiences" data-date="10-28 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-28 00:00</span>
          <span class="news-item-title">谷歌的下一个Genie AI模型生成更逼真的体验</span>
          <span class="news-item-title-en">Google’s next Genie AI model generates more realistic experiences</span>
          <span class="news-value-point">💡 谷歌今天宣布推出使用人工智能生成交互式体验的Genie 4世界模型</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/018/696.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 27 日消息，据科技媒体 TechCrunch 今天报道，Meta 人工智能负责人罗希特 · 帕特尔（Rohit Patel）已经离开公司，他曾在 Meta 从事 AI 研发工作八年，并担任 Meta 超级智能实验室负责人。据报道，帕特尔已创立 Ndoc 公司，他将开发一款原生 AI 办公软件，旨在取代微软 Office 和谷歌 Workspace。这名前 Meta 研究员希望，Ndoc 不能只是叠加在现有工作流的 AI 工具，而是要改变人们使用各种工具的碎片化现状。例如大家经常要来回切换 Excel、Word、PowerPoint 和 Tableau 等软件，还要不断把内容复制粘贴到 ChatGPT 中。Ndoc 的目标是将上述所有工作流整合到统一空间之中，让所有人都能" data-title="Meta AI 负责人罗希特 · 帕特尔离职创业，打造微软 Office 替代方案 Ndoc" data-date="10-27 23:27" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-27 23:27</span>
          <span class="news-item-title">Meta AI 负责人罗希特 · 帕特尔离职创业，打造微软 Office 替代方案 Ndoc</span>
          <span class="news-value-point">💡 IT之家 10 月 27 日消息，据科技媒体 TechCrunch 今天报道，Meta 人工智能负责人罗希特 · 帕特尔（Rohit Patel…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/27/meta-ai-director-rohit-patel-leaves-to-take-on-microsoft-office-and-google-workspace/" target="_blank" rel="noopener" data-cat="keji" data-summary="TechCrunch独家了解到， Rohit Patel在从事人工智能评估和强化学习八年后即将离开Meta。他的创业公司Ndoc的目标是接管微软Office套件。" data-title="Meta AI director Rohit Patel leaves to take on Microsoft Office and Google Workspace" data-date="10-27 22:59" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-27 22:59</span>
          <span class="news-item-title">Meta AI总监Rohit Patel离开，接手Microsoft Office和Google Workspace</span>
          <span class="news-item-title-en">Meta AI director Rohit Patel leaves to take on Microsoft Office and Google Workspace</span>
          <span class="news-value-point">💡 TechCrunch独家了解到， Rohit Patel在从事人工智能评估和强化学习八年后即将离开Meta</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/tsmc-reportedly-weighs-20-percent-cowos-price-increase-as-nvidia-blackwell-and-rubin-chips-put-pressure-on-packaging-capacity-equipment-lead-times-stretch-to-eight-months" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道，由于英伟达的Blackwell和即将推出的Rubin芯片加大了对产能的压力，台积电正在对其CoWoS先进封装技术进行高达20%的价格上涨。据报道，设备交付现在需要长达八个月的时间，而" data-title="TSMC reportedly weighs 20% CoWoS price increase as Nvidia Blackwell and Rubin chips put pressure on packaging capacity" data-date="10-27 22:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-27 22:30</span>
          <span class="news-item-title">据报道，由于英伟达Blackwell和Rubin芯片对封装容量施加压力，台积电称CoWoS价格上涨了20%</span>
          <span class="news-item-title-en">TSMC reportedly weighs 20% CoWoS price increase as Nvidia Blackwell and Rubin chips put pressure on packaging capacity</span>
          <span class="news-value-point">💡 据报道，由于英伟达的Blackwell和即将推出的Rubin芯片加大了对产能的压力，台积电正在对其CoWoS先进封装技术进行高达20%的价格上涨</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-27/10721940.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网西安10月27日电 (记者 阿琳娜)记者27日从西安交通大学获悉，由西安交通大学主办，机械工程学院、精密微纳制造技术全国重点实验室、期刊中心承办，高等教育出版社支持的Intelligent Equipment(《智能装备(英文)》)创刊发布会近日在西安举行。" data-title="搭建国际学术交流平台 《智能装备（英文）》正式创刊发布" data-date="10-27 22:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-27 22:17</span>
          <span class="news-item-title">搭建国际学术交流平台 《智能装备（英文）》正式创刊发布</span>
          <span class="news-value-point">💡 中新网西安10月27日电 (记者 阿琳娜)记者27日从西安交通大学获悉，由西安交通大学主办，机械工程学院、精密微纳制造技术全国重点实验室、期刊中…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-27/10721934.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网长沙10月27日电(冯军)10月27日，参加湘江“对话”塞纳河——2026欧洲华文媒体长沙行的华媒代表走进中联重科智慧产业城，观摩智能制造产线和人形机器人训练，实地感受湖南智能制造的硬核实力。" data-title="从挖掘机穿针到人形机器人训练 欧洲华媒感受湖南智造硬核实力" data-date="10-27 22:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-27 22:01</span>
          <span class="news-item-title">从挖掘机穿针到人形机器人训练 欧洲华媒感受湖南智造硬核实力</span>
          <span class="news-value-point">💡 中新网长沙10月27日电(冯军)10月27日，参加湘江“对话”塞纳河——2026欧洲华文媒体长沙行的华媒代表走进中联重科智慧产业城，观摩智能制造…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/police-reportedly-pulling-motorists-over-because-ai-algorithms-deem-their-driving-patterns-suspicious-rights-group-report-warns-ai-surveillance-systems-will-sweep-in-more-innocent-people-than-wrongdoers" target="_blank" rel="noopener" data-cat="keji" data-summary="美国公民自由联盟的一份报告声称，警方越来越多地使用人工智能来分析车牌阅读器数据，并根据旅行模式标记驾驶者，这引发了人们的担忧，即无辜的司机可能会因为算法认为他们的行动可疑而被停车" data-title="Police are reportedly pulling motorists over because AI algorithms deem their driving patterns &#39;suspicious&#39;" data-date="10-27 21:53" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-27 21:53</span>
          <span class="news-item-title">据报道，警方将驾驶者拉过来是因为人工智能算法认为他们的驾驶模式“可疑”</span>
          <span class="news-item-title-en">Police are reportedly pulling motorists over because AI algorithms deem their driving patterns 'suspicious'</span>
          <span class="news-value-point">💡 美国公民自由联盟的一份报告声称，警方越来越多地使用人工智能来分析车牌阅读器数据，并根据旅行模式标记驾驶者，这引发了人们的担忧，即无辜的司机可能会…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/27/general-compute-raises-100-million-series-a-countering-the-neocloud-disaster-narrative/" target="_blank" rel="noopener" data-cat="keji" data-summary="General Compute押注于Nvidia生态系统之外的推理芯片。" data-title="General Compute raises $100 million Series A, countering the neocloud disaster narrative" data-date="10-27 21:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-27 21:00</span>
          <span class="news-item-title">General Compute筹集了1亿美元的A轮融资，以对抗新云灾难的叙述</span>
          <span class="news-item-title-en">General Compute raises $100 million Series A, countering the neocloud disaster narrative</span>
          <span class="news-value-point">💡 General Compute押注于Nvidia生态系统之外的推理芯片</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/505865.html" target="_blank" rel="noopener" data-cat="keji" data-summary="人形机器人全套图纸开源！从关节到算法，下载就能自己造。" data-title="不藏了！人形机器人全开源动真格，从机械结构一路拆到运动算法" data-date="10-27 20:57" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-27 20:57</span>
          <span class="news-item-title">不藏了！人形机器人全开源动真格，从机械结构一路拆到运动算法</span>
          <span class="news-value-point">💡 人形机器人全套图纸开源</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">12 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13604361/michael-carrick-why-man-utd-head-coach-will-stay-on-and-could-bruno-fernandes-play-vs-chelsea-plus-other-key-questions" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）有机会扭转曼联的局面-这一令人震惊的决定使支持者和天空体育的专家意见分歧。" data-title="&#39;Delaying the inevitable&#39; or right call? Key questions as Carrick stays" data-date="10-27 22:40" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-27 22:40</span>
          <span class="news-item-title">“延迟不可避免的”或正确的呼叫？ Carrick入住期间的关键问题</span>
          <span class="news-item-title-en">'Delaying the inevitable' or right call? Key questions as Carrick stays</span>
          <span class="news-value-point">💡 迈克尔·卡里克（ Michael Carrick ）有机会扭转曼联的局面-这一令人震惊的决定使支持者和天空体育的专家意见分歧</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13604361/michael-carrick-why-man-utd-head-coach-will-stay-on-and-could-bruno-fernandes-play-vs-chelsea-plus-other-key-questions" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）有机会扭转曼联的局面-这一令人震惊的决定使支持者和天空体育的专家意见分歧。" data-title="&#39;Delaying the inevitable&#39; or right call? Key questions as Carrick stays" data-date="10-27 22:40" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-27 22:40</span>
          <span class="news-item-title">“延迟不可避免的”或正确的呼叫？ Carrick入住期间的关键问题</span>
          <span class="news-item-title-en">'Delaying the inevitable' or right call? Key questions as Carrick stays</span>
          <span class="news-value-point">💡 迈克尔·卡里克（ Michael Carrick ）有机会扭转曼联的局面-这一令人震惊的决定使支持者和天空体育的专家意见分歧</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025501/liverpool-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Liverpool latest: Iraola &#39;optimistic&#39; about Wirtz&#39;s availability for Chelsea" data-title="Liverpool latest: Iraola &#39;optimistic&#39; about Wirtz&#39;s availability for Chelsea" data-date="10-27 20:43" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-27 20:43</span>
          <span class="news-item-title">利物浦最新消息： Iraola对Wirtz在切尔西的可用性持“乐观”态度</span>
          <span class="news-item-title-en">Liverpool latest: Iraola 'optimistic' about Wirtz's availability for Chelsea</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c6x2v4p284ylo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="因在节目中以“独裁者”形容已故中国领导人毛泽东，法国足球明星基利安·姆巴佩（麦巴比）近日在中国引发争议，多家中国大型品牌先后宣布终止与其合作。姆巴佩发表道歉声明也不被中国网民接纳。" data-title="姆巴佩陷入“中国独裁者”迷因风波：品牌解约、央视停播" data-date="10-27 20:42" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-27 20:42</span>
          <span class="news-item-title">姆巴佩陷入“中国独裁者”迷因风波：品牌解约、央视停播</span>
          <span class="news-value-point">💡 因在节目中以“独裁者”形容已故中国领导人毛泽东，法国足球明星基利安·姆巴佩（麦巴比）近日在中国引发争议，多家中国大型品牌先后宣布终止与其合作</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025499/man-city-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Man City latest: Maresca defends Donnarumma and Guehi&#39;s form" data-title="Man City latest: Maresca defends Donnarumma and Guehi&#39;s form" data-date="10-27 20:35" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-27 20:35</span>
          <span class="news-item-title">曼城最新消息： Maresca捍卫Donnarumma和Guehi的身体</span>
          <span class="news-item-title-en">Man City latest: Maresca defends Donnarumma and Guehi's form</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/uk-news/video/2026/oct/27/why-man-city-fans-dont-care-about-the-cheating-video" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="随着曼城被判犯有100多项违反规则的指控，他们很快就会发现自己被英超联赛降级，甚至更糟。《卫报》记者和曼彻斯特居民海伦·皮德（ Helen Pidd ）在比赛日与足球迷交谈，" data-title="Why Man City fans ‘don’t care’ about the cheating scandal" data-date="10-27 20:25" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-27 20:25</span>
          <span class="news-item-title">为什么曼城球迷“不在乎”作弊丑闻</span>
          <span class="news-item-title-en">Why Man City fans ‘don’t care’ about the cheating scandal</span>
          <span class="news-value-point">💡 随着曼城被判犯有100多项违反规则的指控，他们很快就会发现自己被英超联赛降级，甚至更糟</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/crlykgeqzypyo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）将继续负责曼联本周末的切尔西之旅。" data-title="Carrick to stay in charge of Man Utd for Chelsea game" data-date="10-27 20:10" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-27 20:10</span>
          <span class="news-item-title">卡里克将继续负责曼联的切尔西比赛</span>
          <span class="news-item-title-en">Carrick to stay in charge of Man Utd for Chelsea game</span>
          <span class="news-value-point">💡 迈克尔·卡里克（ Michael Carrick ）将继续负责曼联本周末的切尔西之旅</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13604347/man-utd-boss-michael-carrick-to-remain-in-charge-vs-chelsea-and-given-chance-to-turn-situation-around" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）将继续负责曼联周六对阵切尔西的比赛。" data-title="Carrick to remain in charge of Man Utd for Chelsea trip" data-date="10-27 20:03" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-27 20:03</span>
          <span class="news-item-title">Carrick将继续负责曼联的切尔西之旅</span>
          <span class="news-item-title-en">Carrick to remain in charge of Man Utd for Chelsea trip</span>
          <span class="news-value-point">💡 迈克尔·卡里克（ Michael Carrick ）将继续负责曼联周六对阵切尔西的比赛</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13604347/man-utd-boss-michael-carrick-to-remain-in-charge-vs-chelsea-and-given-chance-to-turn-situation-around" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）将继续负责曼联周六对阵切尔西的比赛。" data-title="Carrick to remain in charge of Man Utd for Chelsea trip" data-date="10-27 20:03" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-27 20:03</span>
          <span class="news-item-title">Carrick将继续负责曼联的切尔西之旅</span>
          <span class="news-item-title-en">Carrick to remain in charge of Man Utd for Chelsea trip</span>
          <span class="news-value-point">💡 迈克尔·卡里克（ Michael Carrick ）将继续负责曼联周六对阵切尔西的比赛</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025497/chelsea-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Chelsea latest: Joao Pedro out for a &#39;few weeks&#39; with thigh injury" data-title="Chelsea latest: Joao Pedro out for a &#39;few weeks&#39; with thigh injury" data-date="10-27 20:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-27 20:00</span>
          <span class="news-item-title">切尔西最新消息： Joao Pedro因大腿受伤缺席“几周”</span>
          <span class="news-item-title-en">Chelsea latest: Joao Pedro out for a 'few weeks' with thigh injury</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13604005/are-chelsea-finally-playing-the-brand-of-football-sonia-bompastor-wants-and-is-it-wsl-title-worthy" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育专栏作家劳拉·亨特（ Laura Hunter ）分析了第六轮女子超级联赛的重要话题，让您更接近女子比赛的核心关键故事。此外：在接下来的几个主题中，对您想要涵盖的主题进行投票" data-title="Are Chelsea back? Have Man Utd weathered early" data-date="10-27 19:45" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-27 19:45</span>
          <span class="news-item-title">切尔西回来了吗，曼联提前风化了吗</span>
          <span class="news-item-title-en">Are Chelsea back? Have Man Utd weathered early</span>
          <span class="news-value-point">💡 天空体育专栏作家劳拉·亨特（ Laura Hunter ）分析了第六轮女子超级联赛的重要话题，让您更接近女子比赛的核心关键故事</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cw5ynr87jdr0o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳的防守状态证明了埃兹里·孔萨的表现，他在威廉·萨利巴缺席的情况下加强了表现，并获得了发光的机会。" data-title="No Saliba, no problem - Konsa stepping up for Arsenal" data-date="10-27 15:22" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-27 15:22</span>
          <span class="news-item-title">没有Saliba ，没有问题- Konsa为阿森纳挺身而出</span>
          <span class="news-item-title-en">No Saliba, no problem - Konsa stepping up for Arsenal</span>
          <span class="news-value-point">💡 阿森纳的防守状态证明了埃兹里·孔萨的表现，他在威廉·萨利巴缺席的情况下加强了表现，并获得了发光的机会</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.tomshardware.com/laptops/military-drone-outfit-anduril-partners-with-qualcomm-to-build-laptops-on-us-soil-with-new-bluechip-venture-defense-contractor-targets-a-100-percent-domestic-supply-chain-in-the-future" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这家国防承包商的目标是全面恢复美国海岸的笔记本电脑制造，其首批BlueChip笔记本电脑原型机的采购成本90%来自美国和其他盟国的供应商。" data-title="Military drone outfit Anduril partners with Qualcomm to build laptops on US soil with new BlueChip venture" data-date="10-28 01:42" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-28 01:42</span>
          <span class="news-item-title">军用无人机公司Anduril与高通公司合作，通过新的BlueChip合资企业在美国本土制造笔记本电脑</span>
          <span class="news-item-title-en">Military drone outfit Anduril partners with Qualcomm to build laptops on US soil with new BlueChip venture</span>
          <span class="news-value-point">💡 这家国防承包商的目标是全面恢复美国海岸的笔记本电脑制造，其首批BlueChip笔记本电脑原型机的采购成本90%来自美国和其他盟国的供应商</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/cyber-security/israeli-ad-tech-firm-tied-to-suspected-starlink-tracking-effort-report-claims-researchers-say-it-outbid-everyone-for-starlink-linked-ads-in-100-countries-including-where-the-service-is-banned" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Citizen Lab和Confiant将以色列公司Discover-Tech与通过在线广告进行的可疑监控联系起来。研究人员表示，其广告出现在近20万个网站和移动应用程序中。TrendAI单独识别了以下项下的相关活动：" data-title="Israeli ad tech firm tied to suspected Starlink tracking effort, report claims" data-date="10-28 01:37" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-28 01:37</span>
          <span class="news-item-title">报告称，以色列广告技术公司与涉嫌Starlink跟踪工作有关</span>
          <span class="news-item-title-en">Israeli ad tech firm tied to suspected Starlink tracking effort, report claims</span>
          <span class="news-value-point">💡 Citizen Lab和Confiant将以色列公司Discover-Tech与通过在线广告进行的可疑监控联系起来</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1019484/super-mouse-touchscreen-shortcuts-macros-kickstarter" target="_blank" rel="noopener" data-cat="zonghe" data-summary="一家名为Arctic Fox Technologies的公司宣布推出一款新的多功能鼠标，该鼠标在其表面上放弃了无数可定制的快捷键，而是在手下放置了一个紧凑的触摸屏。超级鼠标可能不会优先考虑" data-title="The Super Mouse puts a touchscreen macro pad under your hand" data-date="10-28 01:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-28 01:00</span>
          <span class="news-item-title">超级鼠标将触摸屏微距垫放在您的手下</span>
          <span class="news-item-title-en">The Super Mouse puts a touchscreen macro pad under your hand</span>
          <span class="news-value-point">💡 一家名为Arctic Fox Technologies的公司宣布推出一款新的多功能鼠标，该鼠标在其表面上放弃了无数可定制的快捷键，而是在手下放置…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/27/us/election-interference-trump-midterms.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="州和地方的选举日计划包括如何应对潜在的ICE突袭、联邦选举监督员的不当行为以及企图夺取选票或机器的行为。" data-title="Election Officials Fear Trump Administration’s Interference in Midterms Voting" data-date="10-28 00:51" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-28 00:51</span>
          <span class="news-item-title">选举官员担心特朗普政府干预中期投票</span>
          <span class="news-item-title-en">Election Officials Fear Trump Administration’s Interference in Midterms Voting</span>
          <span class="news-value-point">💡 州和地方的选举日计划包括如何应对潜在的ICE突袭、联邦选举监督员的不当行为以及企图夺取选票或机器的行为</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/27/us/politics/michigan-senate-race-jewish-muslim-voters.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="与美国其他地方相比，美国对以色列的政策处于迈克·罗杰斯（ Mike Rogers ）和阿卜杜勒·赛义德（ Abdul El-Sayed ）之间竞争的最前沿。" data-title="Michigan Senate Race Drives Anxiety Among Jewish and Muslim Voters" data-date="10-28 00:47" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-28 00:47</span>
          <span class="news-item-title">密歇根州参议院竞选引发犹太人和穆斯林选民的焦虑</span>
          <span class="news-item-title-en">Michigan Senate Race Drives Anxiety Among Jewish and Muslim Voters</span>
          <span class="news-value-point">💡 与美国其他地方相比，美国对以色列的政策处于迈克·罗杰斯（ Mike Rogers ）和阿卜杜勒·赛义德（ Abdul El-Sayed ）之间竞…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/policy/1019604/new-mexico-meta-cambridge-analytica-kids-safety-settlement" target="_blank" rel="noopener" data-cat="zonghe" data-summary="今年夏天，当美国各地的总检察长宣布与Meta达成170亿美元的和解协议时，这笔金额是前所未有的。但新墨西哥州一名法官上周的一项裁决将这个数字夸大了。法官命令Meta支付250亿美元" data-title="Meta’s $25 billion legal loss just put blood in the water" data-date="10-28 00:44" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-28 00:44</span>
          <span class="news-item-title">Meta的250 $合法损失只是把血放进水里</span>
          <span class="news-item-title-en">Meta’s $25 billion legal loss just put blood in the water</span>
          <span class="news-value-point">💡 今年夏天，当美国各地的总检察长宣布与Meta达成170亿美元的和解协议时，这笔金额是前所未有的</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/27/movies/event-horizon-good-bad.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="保罗· W · S ·安德森（ Paul W. S. Anderson ） 1997年由山姆·尼尔（ Sam Neill ）主演的噩梦般的太空电影，在震惊观众期待一次简单的太空冒险之后，成为了一部浆状恐怖经典" data-title="‘Event Horizon’: The Cosmic Horror Flop That Rose From the Void" data-date="10-28 00:30" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-28 00:30</span>
          <span class="news-item-title">“事件视界” ：从虚空中崛起的宇宙恐怖翻牌</span>
          <span class="news-item-title-en">‘Event Horizon’: The Cosmic Horror Flop That Rose From the Void</span>
          <span class="news-value-point">💡 保罗· W · S ·安德森（ Paul W. S. Anderson ） 1997年由山姆·尼尔（ Sam Neill ）主演的噩梦般的太空电…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/12040/13279295/brighton-transfers-latest-news-rumours-and-gossip-live-updates-goals-and-highlights" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Brighton latest: Minteh closes in on return" data-title="Brighton latest: Minteh closes in on return" data-date="10-28 00:04" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-28 00:04</span>
          <span class="news-item-title">布莱顿最新消息： Minteh回归后关闭</span>
          <span class="news-item-title-en">Brighton latest: Minteh closes in on return</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/report/1019478/major-league-baseball-fandom-social-media-world-series-influencers" target="_blank" rel="noopener" data-cat="zonghe" data-summary="10月2日，就在美国职业棒球大联盟分区系列赛开幕之际，美国职业棒球大联盟的主要Instagram和TikTok帐户发布了一段视频，炒作仍在参加世界大赛的球队。它展示了来自密尔沃基的球员的片段" data-title="Major League Baseball is looking for a new kind of fan" data-date="10-28 00:02" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-28 00:02</span>
          <span class="news-item-title">美国职业棒球大联盟正在寻找一种新的球迷</span>
          <span class="news-item-title-en">Major League Baseball is looking for a new kind of fan</span>
          <span class="news-value-point">💡 10月2日，就在美国职业棒球大联盟分区系列赛开幕之际，美国职业棒球大联盟的主要Instagram和TikTok帐户发布了一段视频，炒作仍在参加世…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1019298/matic-serene-robot-vacuum-price-specs-release-date" target="_blank" rel="noopener" data-cat="zonghe" data-summary="我最喜欢的机器人吸尘器背后的公司Matic正在推出自2023年首次亮相以来的第一款新型号： Matic Serene。新型机器人地板清洁剂有一个关键升级：降低噪音。承诺的最高输出仅为52分贝" data-title="My favorite robot vacuum just got quieter, and more expensive" data-date="10-28 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-28 00:00</span>
          <span class="news-item-title">我最喜欢的机器人吸尘器变得更安静，更昂贵</span>
          <span class="news-item-title-en">My favorite robot vacuum just got quieter, and more expensive</span>
          <span class="news-value-point">💡 我最喜欢的机器人吸尘器背后的公司Matic正在推出自2023年首次亮相以来的第一款新型号： Matic Serene</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/f1/news/12040/13604106/george-russell-toto-wolff-rejects-helmut-markos-doubts-over-mercedes-drivers-future-hopes-as-kimi-antonelli-nears-title" target="_blank" rel="noopener" data-cat="zonghe" data-summary="梅赛德斯车队首席执行官托托·沃尔夫（ Toto Wolff ）拒绝了赫尔穆特·马尔科（ Helmut Marko ）的建议，即乔治·拉塞尔（ George Russell ）在本赛季被他的队友基米·安东内利（ Kimi Antonelli ）超越后，将来几乎没有机会成为" data-title="Wolff rejects Marko&#39;s doubts over Russell&#39;s future F1 title hopes" data-date="10-28 00:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-28 00:00</span>
          <span class="news-item-title">沃尔夫拒绝接受马尔科对罗素未来F1冠军希望的怀疑</span>
          <span class="news-item-title-en">Wolff rejects Marko's doubts over Russell's future F1 title hopes</span>
          <span class="news-value-point">💡 梅赛德斯车队首席执行官托托·沃尔夫（ Toto Wolff ）拒绝了赫尔穆特·马尔科（ Helmut Marko ）的建议，即乔治·拉塞尔（ G…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/018/697.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 27 日消息，ATK RS8 Air、RS8 Neo 系列 87 配列高性能电竞键盘今日发布，已开启定金预定，RS8 Air 到手价 349 元起，RS8 Neo 到手价 299 元起，11 月 3 日 21 点尾款支付。IT之家从官方介绍获悉，该系列产品以 87 大配列带来完整 F 区与全功能按键，兼顾办公码字的便捷需求与电竞对局的操作自由度，拓展更多使用场景。外观搭载正面顶雾 PC 键帽，搭配侧边机甲翼镜结构。两款机型均采用五层满配填充 +GASKET 结构。RS8Air 搭载第三代烈风 Ultra 磁轴方案，全链路延迟低至 0.28ms，支持 0.001mmRT 精度。机身配备模式切换拨杆，一键快速切换多组板载预设。RS8Neo 采用 2.4G / 有线双 8K 机" data-title="ATK RS8 Air / Neo 电竞键盘发布：87 配列，到手价 299 元起" data-date="10-27 23:33" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-27 23:33</span>
          <span class="news-item-title">ATK RS8 Air / Neo 电竞键盘发布：87 配列，到手价 299 元起</span>
          <span class="news-value-point">💡 IT之家 10 月 27 日消息，ATK RS8 Air、RS8 Neo 系列 87 配列高性能电竞键盘今日发布，已开启定金预定，RS8 Air…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025492/man-utd-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Man Utd latest: Neville reacts to Carrick staying" data-title="Man Utd latest: Neville reacts to Carrick staying" data-date="10-27 23:30" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-27 23:30</span>
          <span class="news-item-title">曼联最新消息：内维尔对卡里克的入住做出反应</span>
          <span class="news-item-title-en">Man Utd latest: Neville reacts to Carrick staying</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/018/695.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 27 日消息，雷蛇今日宣布推出 Razer Reclusa Mini 65% 雷蛇隐蛛迷你版 65% 电竞磁轴键盘，售价 1099 元。京东雷蛇（Razer）隐蛛迷你版 65%【雷蛇磁轴】 有线无线蓝牙三模 RT0.1 热插拔客制化 68 键小键盘 打瓦 CS1099 元直达链接该键盘采用 68 键 65% 紧凑布局，在保留常用按键的同时大幅节省桌面空间，兼顾桌面整洁度与移动使用需求。核心配置上，该键盘搭载雷蛇霍尔效应磁轴，触发点位精准稳定可控，触发行程支持 0.1-4.0mm 自由自定义，按键敲击寿命约 1 亿次；同时支持快速触发模式，按键抬起仅 0.1mm 即可瞬间复位，配合 40 克轻盈触发压力，可显著提升游戏连击响应速度，适配急停、瞄准、闪避等电竞操作。这款键盘支" data-title="1099 元雷蛇隐蛛迷你版 65% 磁轴键盘发布，三色键帽混搭设计" data-date="10-27 23:25" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-27 23:25</span>
          <span class="news-item-title">1099 元雷蛇隐蛛迷你版 65% 磁轴键盘发布，三色键帽混搭设计</span>
          <span class="news-value-point">💡 IT之家 10 月 27 日消息，雷蛇今日宣布推出 Razer Reclusa Mini 65% 雷蛇隐蛛迷你版 65% 电竞磁轴键盘，售价 1…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025496/newcastle-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Newcastle latest: Jaissle &#39;owes&#39; cup run to the fans" data-title="Newcastle latest: Jaissle &#39;owes&#39; cup run to the fans" data-date="10-27 23:15" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-27 23:15</span>
          <span class="news-item-title">纽卡斯尔最新消息： Jaissle “欠”球迷的杯赛</span>
          <span class="news-item-title-en">Newcastle latest: Jaissle 'owes' cup run to the fans</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-28 02:07（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
