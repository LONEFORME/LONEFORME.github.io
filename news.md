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
      <span>2026-11-05 03:55 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">天空体育×13 · 中国新闻网×11</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.nytimes.com/2026/11/04/us/politics/democrats-house-senate-congress-trump.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="两年来，特朗普总统在共和党的帮助下篡夺了立法部门的权力。民主党现在正试图收回国会的一些特权。" data-title="With Democrats’ Sweep, Congress Is Set to Reassert Power to Check Trump" data-date="11-05 03:51" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 11-05 03:51</span>
      </div>
      <h2 class="hero-featured-title">随着民主党的扫荡，国会将重申权力以制衡特朗普</h2>
      <div class="hero-featured-title-en">With Democrats’ Sweep, Congress Is Set to Reassert Power to Check Trump</div>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://techcrunch.com/video/open-source-ai-is-booming-hugging-face-explains-who-profits/" target="_blank" rel="noopener" data-cat="keji" data-summary="开源模型正变得越来越主流，因为企业、政府和初创公司都依赖于更低成本、更多控制和更大灵活性的承诺。但是，随着功能越来越强大的模型变得更加免费，公司如何" data-title="Open source AI is booming. Hugging Face explains who profits." data-date="11-05 03:30" data-source="TechCrunch">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
      </div>
      <p class="hero-sub-title">Open source AI is booming. Hugging Face explains who profits.</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/football/live-blog/11661/13025491/aston-villa-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Aston Villa latest: Club hold &#39;positive discussions&#39; over Emery contract extension" data-title="Aston Villa latest: Club hold &#39;positive discussions&#39; over Emery contract extension" data-date="11-05 03:00" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">Aston Villa latest: Club hold 'positive discussions' over Emery contract extension</p>
    </a>
    <a class="hero-sub-card" href="https://www.theverge.com/gadgets/1025370/google-pixel-11-pro-phone-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在11月8日之前，您可以在Google的Pixel 11手机上节省大量资金，无论您想要的是最便宜的Pixel 11 ，还是拍摄更好照片的稍贵的Pixel 11 Pro。即使是持久耐用的大型Pixel 11 Pro XL" data-title="Google’s Pixel 11 phones are up to 27 percent off" data-date="11-05 03:00" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">Google’s Pixel 11 phones are up to 27 percent off</p>
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
        <a class="news-item" href="https://www.nytimes.com/2026/11/04/us/politics/democrats-house-senate-congress-trump.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="两年来，特朗普总统在共和党的帮助下篡夺了立法部门的权力。民主党现在正试图收回国会的一些特权。" data-title="With Democrats’ Sweep, Congress Is Set to Reassert Power to Check Trump" data-date="11-05 03:51" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-05 03:51</span>
          <span class="news-item-title">随着民主党的扫荡，国会将重申权力以制衡特朗普</span>
          <span class="news-item-title-en">With Democrats’ Sweep, Congress Is Set to Reassert Power to Check Trump</span>
          <span class="news-value-point">💡 两年来，特朗普总统在共和党的帮助下篡夺了立法部门的权力</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-05/10726334.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="维谢格拉德集团(波兰、匈牙利、捷克、斯洛伐克)总统峰会4日在斯洛伐克西部城市特伦钦拉开帷幕，峰会将持续至5日。此次峰会旨在重振四国合作机制，加强成员国在欧洲事务中的集体影响力，推动共同关心事项的落实。" data-title="中东欧四国总统峰会在斯洛伐克举行" data-date="11-05 00:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-05 00:09</span>
          <span class="news-item-title">中东欧四国总统峰会在斯洛伐克举行</span>
          <span class="news-value-point">💡 维谢格拉德集团(波兰、匈牙利、捷克、斯洛伐克)总统峰会4日在斯洛伐克西部城市特伦钦拉开帷幕，峰会将持续至5日</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-04/10726324.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社雅加达11月4日电 (记者 李志全)印度尼西亚卫生部4日表示，受森林和土地火灾影响，印尼累计报告急性呼吸道感染病例超过40万例。" data-title="火灾烟霾致印尼急性呼吸道感染病例超40万例" data-date="11-04 23:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-04 23:01</span>
          <span class="news-item-title">火灾烟霾致印尼急性呼吸道感染病例超40万例</span>
          <span class="news-value-point">💡 中新社雅加达11月4日电 (记者 李志全)印度尼西亚卫生部4日表示，受森林和土地火灾影响，印尼累计报告急性呼吸道感染病例超过40万例</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-04/10726317.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="韩国海关部门4日通报，驻韩美军两名士兵因涉嫌利用美国军方邮政系统走私毒品被捕，已被移交韩国检方。调查显示，驻韩美军基地内存在毒品交易和分销迹象。" data-title="驻韩美军两名士兵涉嫌走私毒品被捕" data-date="11-04 22:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-04 22:31</span>
          <span class="news-item-title">驻韩美军两名士兵涉嫌走私毒品被捕</span>
          <span class="news-value-point">💡 韩国海关部门4日通报，驻韩美军两名士兵因涉嫌利用美国军方邮政系统走私毒品被捕，已被移交韩国检方</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-04/10726314.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网攀枝花11月4日电 (韩金雨)一座以花命名的城市，既藏着中国20世纪建成投产的最大水电站，也守护着近40万株与恐龙同时代的“植物活化石”。11月4日，2026台湾自媒体人天府游记·攀西行活动走进四川省攀枝花市，近20名两岸自媒体人和媒体记者先后探访二滩水电站、攀枝花苏铁国家级自然保护区，感受这座城市的工业力量与生态之美。" data-title="从大国水电到“植物活化石”：台湾自媒体人感受四川攀枝花的生态与工业力量" data-date="11-04 22:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-04 22:28</span>
          <span class="news-item-title">从大国水电到“植物活化石”：台湾自媒体人感受四川攀枝花的生态与工业力量</span>
          <span class="news-value-point">💡 中新网攀枝花11月4日电 (韩金雨)一座以花命名的城市，既藏着中国20世纪建成投产的最大水电站，也守护着近40万株与恐龙同时代的“植物活化石”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-04/10726313.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网银川11月4日电 (记者 于晶)11月4日，记者从宁夏回族自治区财政厅获悉，2026年宁夏统筹各类人才资金总规模达10亿元，以稳定财政投入为人才强区战略筑牢资金底盘，持续吸引集聚各类人才服务宁夏高质量发展。" data-title="宁夏统筹10亿元财力托举人才强区 真金白银引才育才" data-date="11-04 22:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-04 22:27</span>
          <span class="news-item-title">宁夏统筹10亿元财力托举人才强区 真金白银引才育才</span>
          <span class="news-value-point">💡 中新网银川11月4日电 (记者 于晶)11月4日，记者从宁夏回族自治区财政厅获悉，2026年宁夏统筹各类人才资金总规模达10亿元，以稳定财政投入…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-04/10726309.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月4日电 (尹李梅)11月4日，2026京港澳青年科学家大会在北京举行。大会作为第29届京港洽谈会专题活动之一，以“两新融合 向新而行”为主题，汇聚京港澳多方科创主体，搭建科创合作、青年人才赋能与成果转化平台。" data-title="2026京港澳青年科学家大会在北京召开" data-date="11-04 22:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-04 22:23</span>
          <span class="news-item-title">2026京港澳青年科学家大会在北京召开</span>
          <span class="news-value-point">💡 中新网北京11月4日电 (尹李梅)11月4日，2026京港澳青年科学家大会在北京举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-04/10726307.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网重庆11月4日电 (记者 钟旖)重庆市4日召开2026年度全市人力社保网络安全与信息化工作会。" data-title="“十五五”时期 重庆将加快就业等“AI+”综合场景上线" data-date="11-04 22:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-04 22:21</span>
          <span class="news-item-title">“十五五”时期 重庆将加快就业等“AI+”综合场景上线</span>
          <span class="news-value-point">💡 中新网重庆11月4日电 (记者 钟旖)重庆市4日召开2026年度全市人力社保网络安全与信息化工作会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-04/10726296.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网伦敦11月4日电 （记者 欧阳开宇）当地时间11月3日晚，海南（伦敦）旅游文化交流推广活动在英国伦敦举行。活动通过旅游资源推介、合作签约及互动交流，向英国旅游业界展示海南特色文旅资源与自贸港发展机遇，推动双方在目的地推广、旅游产品开发和客源互送等领域深化合作。" data-title="海南（伦敦）旅游文化交流推广活动举行" data-date="11-04 22:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-04 22:15</span>
          <span class="news-item-title">海南（伦敦）旅游文化交流推广活动举行</span>
          <span class="news-value-point">💡 中新网伦敦11月4日电 （记者 欧阳开宇）当地时间11月3日晚，海南（伦敦）旅游文化交流推广活动在英国伦敦举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-04/10726265.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月4日电 亚的斯亚贝巴消息：一名埃塞俄比亚高级官员11月4日证实，埃塞俄比亚已下令6名苏丹外交官限期离境。" data-title="埃塞俄比亚要求6名苏丹外交官离境" data-date="11-04 21:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-04 21:39</span>
          <span class="news-item-title">埃塞俄比亚要求6名苏丹外交官离境</span>
          <span class="news-value-point">💡 中新社北京11月4日电 亚的斯亚贝巴消息：一名埃塞俄比亚高级官员11月4日证实，埃塞俄比亚已下令6名苏丹外交官限期离境</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-04/10726258.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月4日 综合外媒报道，当地时间11月4日，随着美国多场关键选战结果陆续揭晓，美国国会权力格局将出现重大变化。多家美媒预测，民主党在3日举行的中期选举中力压共和党夺回参议院和众议院控制权，重新掌控美国国会。" data-title="美国中期选举变局：民主党或重掌两院，特朗普面临更强制衡" data-date="11-04 21:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-04 21:21</span>
          <span class="news-item-title">美国中期选举变局：民主党或重掌两院，特朗普面临更强制衡</span>
          <span class="news-value-point">💡 中新网11月4日 综合外媒报道，当地时间11月4日，随着美国多场关键选战结果陆续揭晓，美国国会权力格局将出现重大变化</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/04/world/middleeast/israel-president-herzog-election-government.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="总统艾萨克·赫尔佐格（ Isaac Herzog ）在很大程度上是仪式性的角色，他试图避免争议并治愈分歧。但他作为精明的调解人的技能可能在选举结果不佳后发挥重要作用。" data-title="Israel’s President Could Play Key Role in Breaking Post" data-date="11-04 21:18" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-04 21:18</span>
          <span class="news-item-title">以色列总统可以在破坏岗位方面发挥关键作用</span>
          <span class="news-item-title-en">Israel’s President Could Play Key Role in Breaking Post</span>
          <span class="news-value-point">💡 总统艾萨克·赫尔佐格（ Isaac Herzog ）在很大程度上是仪式性的角色，他试图避免争议并治愈分歧</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-04/10726251.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月4日电 据卡塔尔半岛电视台当地时间4日报道，伊朗最高领袖穆杰塔巴·哈梅内伊警告称，美国若再次对伊朗发动袭击，将引发更广泛的回应。" data-title="伊朗最高领袖警告美国：若再袭伊朗将引发更广泛报复" data-date="11-04 21:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-04 21:14</span>
          <span class="news-item-title">伊朗最高领袖警告美国：若再袭伊朗将引发更广泛报复</span>
          <span class="news-value-point">💡 中新网11月4日电 据卡塔尔半岛电视台当地时间4日报道，伊朗最高领袖穆杰塔巴·哈梅内伊警告称，美国若再次对伊朗发动袭击，将引发更广泛的回应</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c6lykq34zd19o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在密歇根州，民主党候选人阿卜杜勒·赛义德如今将成为美国首位穆斯林联邦参议员。" data-title="笃定成为首位穆斯林美国参议员，42岁的赛义德是谁？" data-date="11-04 21:14" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-04 21:14</span>
          <span class="news-item-title">笃定成为首位穆斯林美国参议员，42岁的赛义德是谁？</span>
          <span class="news-value-point">💡 在密歇根州，民主党候选人阿卜杜勒·赛义德如今将成为美国首位穆斯林联邦参议员</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c6kgq8l48q2po/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="两场一年前还被认为将势均力敌的美国参议院选举，最终都成为民主党轻松取胜的选战。" data-title="美国民主党历史性胜利 深入共和党票仓攻城掠地" data-date="11-04 18:52" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-04 18:52</span>
          <span class="news-item-title">美国民主党历史性胜利 深入共和党票仓攻城掠地</span>
          <span class="news-value-point">💡 两场一年前还被认为将势均力敌的美国参议院选举，最终都成为民主党轻松取胜的选战</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://techcrunch.com/video/open-source-ai-is-booming-hugging-face-explains-who-profits/" target="_blank" rel="noopener" data-cat="keji" data-summary="开源模型正变得越来越主流，因为企业、政府和初创公司都依赖于更低成本、更多控制和更大灵活性的承诺。但是，随着功能越来越强大的模型变得更加免费，公司如何" data-title="Open source AI is booming. Hugging Face explains who profits." data-date="11-05 03:30" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-05 03:30</span>
          <span class="news-item-title">开源人工智能正在蓬勃发展。拥抱的脸解释了谁获利。</span>
          <span class="news-item-title-en">Open source AI is booming. Hugging Face explains who profits.</span>
          <span class="news-value-point">💡 开源模型正变得越来越主流，因为企业、政府和初创公司都依赖于更低成本、更多控制和更大灵活性的承诺</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/04/duckduckgo-pitches-itself-to-schools-amid-backlash-over-googles-ai-policy/" target="_blank" rel="noopener" data-cat="keji" data-summary="DuckDuckGo正在向对谷歌人工智能限制感到沮丧的学校求助，向教育工作者指出其搜索引擎和禁用人工智能功能的选项。" data-title="DuckDuckGo pitches itself to schools amid backlash over Google’s AI policy" data-date="11-05 03:29" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-05 03:29</span>
          <span class="news-item-title">在对谷歌人工智能政策的强烈反对中， DuckDuckGo向学校推销自己</span>
          <span class="news-item-title-en">DuckDuckGo pitches itself to schools amid backlash over Google’s AI policy</span>
          <span class="news-value-point">💡 DuckDuckGo正在向对谷歌人工智能限制感到沮丧的学校求助，向教育工作者指出其搜索引擎和禁用人工智能功能的选项</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/podcast/building-on-open-source-ai-hugging-faces-policy-chief-on-the-costs-risks-and-trade-offs/" target="_blank" rel="noopener" data-cat="keji" data-summary="开源模型正变得越来越主流，因为企业、政府和初创公司都依赖于更低成本、更多控制和更大灵活性的承诺。但是，随着功能越来越强大的模型变得更加免费，公司如何" data-title="Building on open source AI? Hugging Face’s policy chief on the costs, risks, and trade" data-date="11-05 02:44" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-05 02:44</span>
          <span class="news-item-title">建立在开源人工智能之上？拥抱Face的成本、风险和贸易政策主管</span>
          <span class="news-item-title-en">Building on open source AI? Hugging Face’s policy chief on the costs, risks, and trade</span>
          <span class="news-value-point">💡 开源模型正变得越来越主流，因为企业、政府和初创公司都依赖于更低成本、更多控制和更大灵活性的承诺</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1026586/nothing-screen-free-ai-device-carl-pei" target="_blank" rel="noopener" data-cat="keji" data-summary="首席执行官Carl Pei在X上的一篇帖子中表示，该公司将于12月推出其首款人工智能设备。就在一年多前，贝聿铭宣布了“AI原生”设备和人工智能操作系统的计划。他没有透露太多关于什么" data-title="Nothing teases a screen-free AI device ahead of launch next month" data-date="11-05 02:26" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-05 02:26</span>
          <span class="news-item-title">在下个月推出之前，没有任何东西可以取笑无屏幕的人工智能设备</span>
          <span class="news-item-title-en">Nothing teases a screen-free AI device ahead of launch next month</span>
          <span class="news-value-point">💡 首席执行官Carl Pei在X上的一篇帖子中表示，该公司将于12月推出其首款人工智能设备</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1026474/openai-chatgpt-animated-gifs-images-2-6" target="_blank" rel="noopener" data-cat="keji" data-summary="ChatGPT现在可以使用上传到AI聊天机器人的提示或照片创建GIF。该更新与OpenAI的新图像2.6模型一起推出，允许您调整GIF的动画速度，编辑单个帧，并与其他" data-title="ChatGPT will now make you animated GIFs" data-date="11-05 02:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-05 02:00</span>
          <span class="news-item-title">ChatGPT现在将为您制作动画GIF</span>
          <span class="news-item-title-en">ChatGPT will now make you animated GIFs</span>
          <span class="news-value-point">💡 ChatGPT现在可以使用上传到AI聊天机器人的提示或照片创建GIF</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/nintendo/nintendo-rom-chip-supplier-macronix-quits-to-focus-on-chips-for-ai-data-centers-game-key-cards-may-be-more-available-as-large-game-storage-chips-become-more-expensive" target="_blank" rel="noopener" data-cat="keji" data-summary="任天堂的ROM芯片制造商之一Macronix正在关闭业务，以重新分配人工智能行业所需的NOR和NAND闪存芯片的制造。" data-title="Nintendo ROM chip supplier Macronix quits to focus on chips for AI data centers, reports indicate" data-date="11-05 01:10" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-05 01:10</span>
          <span class="news-item-title">报告显示，任天堂ROM芯片供应商Macronix退出，专注于人工智能数据中心的芯片</span>
          <span class="news-item-title-en">Nintendo ROM chip supplier Macronix quits to focus on chips for AI data centers, reports indicate</span>
          <span class="news-value-point">💡 任天堂的ROM芯片制造商之一Macronix正在关闭业务，以重新分配人工智能行业所需的NOR和NAND闪存芯片的制造</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/04/i-tried-apples-siri-recaps-theyre-surprisingly-useful-and-a-little-unsettling/" target="_blank" rel="noopener" data-cat="keji" data-summary="尽管我保留了隐私，但苹果的人工智能Siri Recaps在短短一天内就赢得了我的支持。但仍有改进的余地。" data-title="I tried Apple’s Siri Recaps. They’re surprisingly useful — and a little unsettling" data-date="11-05 00:51" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-05 00:51</span>
          <span class="news-item-title">我试过苹果的Siri回顾。它们令人惊讶地有用—并且有点令人不安</span>
          <span class="news-item-title-en">I tried Apple’s Siri Recaps. They’re surprisingly useful — and a little unsettling</span>
          <span class="news-value-point">💡 尽管我保留了隐私，但苹果的人工智能Siri Recaps在短短一天内就赢得了我的支持</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/04/google-faces-backlash-for-plan-that-would-turn-off-search-for-schools-that-restrict-ai/" target="_blank" rel="noopener" data-cat="keji" data-summary="左翼政客，如纽约市市长Zohran Mamdani和前联邦贸易委员会主席Lina Khan ，指责谷歌充当不受监管的垄断者。" data-title="Google faces backlash for plan that would turn off Search for schools that restrict AI" data-date="11-05 00:17" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-05 00:17</span>
          <span class="news-item-title">谷歌面临计划的强烈反对，该计划将关闭搜索限制人工智能的学校</span>
          <span class="news-item-title-en">Google faces backlash for plan that would turn off Search for schools that restrict AI</span>
          <span class="news-value-point">💡 左翼政客，如纽约市市长Zohran Mamdani和前联邦贸易委员会主席Lina Khan ，指责谷歌充当不受监管的垄断者</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/507647.html" target="_blank" rel="noopener" data-cat="keji" data-summary="连路人都有自己的想法" data-title="百度无人车搞出“黑客帝国”！世界模型实时推演全局，跑一天抵三年" data-date="11-05 00:13" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-05 00:13</span>
          <span class="news-item-title">百度无人车搞出“黑客帝国”！世界模型实时推演全局，跑一天抵三年</span>
          <span class="news-value-point">💡 连路人都有自己的想法</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/022/468.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="北京时间 11 月 4 日消息，Anthropic 尚未正式发布的下一代旗舰模型 Claude Fable 5.5 近日在海外开发者社区引发关注。多名开发者在社交平台 X 上分享了据称来自该模型的早期测试结果。其中，一段完全通过编程生成的 66 秒动画短片尤为引人注目。测试者称，模型在没有调用图像或视频生成工具的情况下，连续自主编写和运行代码约 2 小时 40 分钟，完成了动画画面、配乐及音效制作。11 月 2 日，X 平台 AI 开发者 Chetaslua 发布了一段动画短片，并声称其由 Fable 5.5 独立完成。按照他的介绍，短片长度为 66 秒，分辨率 1920×804，帧率 24fps，画面包含狐狸、纸鸟、云层、文字及光影效果，背景音乐和音效同样由模型编写的 Python 代码生" data-title="连续 2 小时 40 分钟纯代码生成 66 秒动画，Anthropic 新旗舰 Fable 5.5 实测曝光" data-date="11-04 23:14" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-04 23:14</span>
          <span class="news-item-title">连续 2 小时 40 分钟纯代码生成 66 秒动画，Anthropic 新旗舰 Fable 5.5 实测曝光</span>
          <span class="news-value-point">💡 北京时间 11 月 4 日消息，Anthropic 尚未正式发布的下一代旗舰模型 Claude Fable 5.5 近日在海外开发者社区引发关注</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/peripherals/gaming-mice/logitech-g-pro-x3-superstrike-review" target="_blank" rel="noopener" data-cat="keji" data-summary="罗技的G Pro X3 Superstrike是其革命性鼠标的一个小但明显的更新—有一个新的芯片组，重量已经重新平衡，所以它的持续时间更长，感觉更好。费用为200 $。" data-title="Logitech G Pro X3 Superstrike Review: $200 for the illusion of a click" data-date="11-04 23:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-04 23:00</span>
          <span class="news-item-title">罗技G Pro X3 Superstrike评测： $ 200的点击幻觉</span>
          <span class="news-item-title-en">Logitech G Pro X3 Superstrike Review: $200 for the illusion of a click</span>
          <span class="news-value-point">💡 罗技的G Pro X3 Superstrike是其革命性鼠标的一个小但明显的更新—有一个新的芯片组，重量已经重新平衡，所以它的持续时间更长，感觉…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/thermal-paste/thermal-grizzly-launches-phasesheet-ptm-pro-with-improved-thermal-conductivity-new-thermal-pad-promises-easier-installation-and-better-cooling-performance" target="_blank" rel="noopener" data-cat="keji" data-summary="PhaseSheet PTM Pro专为没有集成散热器的CPU、GPU和其他组件而设计，可重复使用，不导电，并且不易受到与传统散热浆料相关的泵出效应的影响。" data-title="Thermal Grizzly launches PhaseSheet PTM Pro with improved thermal conductivity —  new thermal pad promises easier installation and better cooling performance" data-date="11-04 22:36" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-04 22:36</span>
          <span class="news-item-title">Thermal Grizzly推出具有改进导热性的PhaseSheet PTM Pro —新的导热垫有望简化安装并提高冷却性能</span>
          <span class="news-item-title-en">Thermal Grizzly launches PhaseSheet PTM Pro with improved thermal conductivity —  new thermal pad promises easier installation and better cooling performance</span>
          <span class="news-value-point">💡 PhaseSheet PTM Pro专为没有集成散热器的CPU、GPU和其他组件而设计，可重复使用，不导电，并且不易受到与传统散热浆料相关的泵出…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/022/438.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 4 日消息，NVIDIA（英伟达）发布 GeForce &amp; RTX Spark Game Ready 621.14 显卡驱动，面向《魔兽世界：永恒》、《毁灭战士：黑暗时代》新内容及新增 DLSS 5 支持的游戏提供优化，并修复此前版本引入的视频播放异常问题。IT之家附官方公告链接（https://www.nvidia.com/en-us/geforce/news/world-of-warcraft-forever-geforce-rtx-spark-game-ready-driver）。新游戏支持与性能优化为 《魔兽世界：永恒》 提供 Game Ready 优化，确保 GeForce RTX 平台最佳游戏体验；针对 《毁灭战士：黑暗时代 | 启示录》新增的屠戮模式 提供性" data-title="英伟达发布 Game Ready 621.14 驱动：优化《魔兽世界：永恒》，修复视频黑屏问题" data-date="11-04 22:18" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-04 22:18</span>
          <span class="news-item-title">英伟达发布 Game Ready 621.14 驱动：优化《魔兽世界：永恒》，修复视频黑屏问题</span>
          <span class="news-value-point">💡 IT之家 11 月 4 日消息，NVIDIA（英伟达）发布 GeForce & RTX Spark Game Ready 621.14 显卡驱动…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/dram/micron-details-ambitious-dram-and-nand-roadmap-3d-nand-high-na-euv-new-materials-and-custom-silicon-makes-a-comeback" target="_blank" rel="noopener" data-cat="keji" data-summary="随着DRAM和3D NAND即将采用全新技术，随着人工智能开发人员面临当前解决方案的限制，定制类型的内存即将成为主流。" data-title="Micron details ambitious DRAM and NAND roadmap — 3D NAND, High-NA EUV, new materials, and custom silicon makes a comeback" data-date="11-04 22:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-04 22:00</span>
          <span class="news-item-title">美光详细介绍雄心勃勃的DRAM和NAND路线图— 3D NAND、High-NA EUV、新材料和定制硅卷土重来</span>
          <span class="news-item-title-en">Micron details ambitious DRAM and NAND roadmap — 3D NAND, High-NA EUV, new materials, and custom silicon makes a comeback</span>
          <span class="news-value-point">💡 随着DRAM和3D NAND即将采用全新技术，随着人工智能开发人员面临当前解决方案的限制，定制类型的内存即将成为主流</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/ai-data-centers-comprehensively-defeated-at-us-midterm-elections-45-measures-put-on-the-ballot-as-americans-overwhelmingly-vote-against-developments" target="_blank" rel="noopener" data-cat="keji" data-summary="在中期选举期间，一些县将数据中心问题列入选票，大多数美国人投票反对其县的数据中心开发。" data-title="AI data centers comprehensively defeated at US midterm elections — 45 measures put on the ballot as Americans overwhelmingly vote against developments" data-date="11-04 21:13" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-04 21:13</span>
          <span class="news-item-title">人工智能数据中心在美国中期选举中被全面击败—美国人以压倒性多数投票反对发展，投票通过了45项措施</span>
          <span class="news-item-title-en">AI data centers comprehensively defeated at US midterm elections — 45 measures put on the ballot as Americans overwhelmingly vote against developments</span>
          <span class="news-value-point">💡 在中期选举期间，一些县将数据中心问题列入选票，大多数美国人投票反对其县的数据中心开发</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">12 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025491/aston-villa-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Aston Villa latest: Club hold &#39;positive discussions&#39; over Emery contract extension" data-title="Aston Villa latest: Club hold &#39;positive discussions&#39; over Emery contract extension" data-date="11-05 03:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-05 03:00</span>
          <span class="news-item-title">阿斯顿维拉最新消息：俱乐部就延长埃默里合同举行“积极讨论”</span>
          <span class="news-item-title-en">Aston Villa latest: Club hold 'positive discussions' over Emery contract extension</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/slavia-prague-vs-arsenal/live/577667" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Slavia Prague vs Arsenal LIVE!" data-title="Slavia Prague vs Arsenal LIVE!" data-date="11-05 02:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-05 02:00</span>
          <span class="news-item-title">斯拉维亚布拉格vs阿森纳现场直播！</span>
          <span class="news-item-title-en">Slavia Prague vs Arsenal LIVE!</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/04/bournemouth-marco-rose-premier-league-games-opta" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Marco Rose的球队在英超联赛的前六场比赛中没有赢得任何一场比赛，但他保持冷静和积极的态度Opta Analyst即使是伯恩茅斯的球迷也会感到沮丧和担忧，这也是很容易理解的。他们尊敬的主教练安藤" data-title="Bournemouth’s decision not to panic after their tough start is paying off" data-date="11-05 01:01" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-05 01:01</span>
          <span class="news-item-title">伯恩茅斯在艰难的开局后不惊慌的决定正在得到回报</span>
          <span class="news-item-title-en">Bournemouth’s decision not to panic after their tough start is paying off</span>
          <span class="news-value-point">💡 Marco Rose的球队在英超联赛的前六场比赛中没有赢得任何一场比赛，但他保持冷静和积极的态度Opta Analyst即使是伯恩茅斯的球迷也会…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/nfl/news/12040/13608003/tom-brady-seven-time-super-bowl-champion-returns-to-new-england-patriots-as-broadcaster-for-first-time-at-foxboro" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="汤姆·布雷迪（ Tom Brady ）本周末将作为广播员重返新英格兰，这是他从足球界退役以来的第一次情绪激动地回归。" data-title="Brady returns to Patriots as commentator for first time" data-date="11-05 00:50" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-05 00:50</span>
          <span class="news-item-title">布雷迪首次以评论员的身份重返爱国者队</span>
          <span class="news-item-title-en">Brady returns to Patriots as commentator for first time</span>
          <span class="news-value-point">💡 汤姆·布雷迪（ Tom Brady ）本周末将作为广播员重返新英格兰，这是他从足球界退役以来的第一次情绪激动地回归</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/fenerbahce-vs-liverpool/live/577663" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Fenerbahce complete remarkable comeback to beat Liverpool LIVE!" data-title="Fenerbahce complete remarkable comeback to beat Liverpool LIVE!" data-date="11-05 00:15" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-05 00:15</span>
          <span class="news-item-title">费内巴切（ Fenerbahce ）完成了非凡的复出，击败了利物浦直播！</span>
          <span class="news-item-title-en">Fenerbahce complete remarkable comeback to beat Liverpool LIVE!</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqx28zjxdxxzo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在对阵罗马的比赛中取得了令人难忘的复出胜利后，曼联能否避免重蹈覆辙，继而取得连续的胜利？" data-title="Why Man Utd&#39;s Roma comeback has echoes of Mourinho and Solskjaer" data-date="11-05 00:12" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-05 00:12</span>
          <span class="news-item-title">为什么曼联的罗马复出与穆里尼奥和索尔斯克亚的回响相呼应</span>
          <span class="news-item-title-en">Why Man Utd's Roma comeback has echoes of Mourinho and Solskjaer</span>
          <span class="news-value-point">💡 在对阵罗马的比赛中取得了令人难忘的复出胜利后，曼联能否避免重蹈覆辙，继而取得连续的胜利</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13607916/man-utd-youngsters-paul-merson-has-his-say-on-shea-lacey-and-jj-gabriel" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育的保罗·默森（ Paul Merson ）对谢伊·莱西（ Shea Lacey ）对罗马队的表现表示欢迎，并就JJ加布里埃尔（ JJ Gabriel ）可能转会皇家马" data-title="&#39;Bed him in slowly&#39; - Merse has his say on Lacey and JJ Gabriel update" data-date="11-04 20:32" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-04 20:32</span>
          <span class="news-item-title">“让他慢慢入睡” - Merse对Lacey和JJ Gabriel的最新消息发表了自己的看法</span>
          <span class="news-item-title-en">'Bed him in slowly' - Merse has his say on Lacey and JJ Gabriel update</span>
          <span class="news-value-point">💡 天空体育的保罗·默森（ Paul Merson ）对谢伊·莱西（ Shea Lacey ）对罗马队的表现表示欢迎，并就JJ加布里埃尔（ JJ G…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025492/man-utd-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Man Utd latest: Baleba injured, Lacey in? Pick your team to face Aston Villa" data-title="Man Utd latest: Baleba injured, Lacey in? Pick your team to face Aston Villa" data-date="11-04 19:55" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-04 19:55</span>
          <span class="news-item-title">曼联最新消息： Baleba受伤， Lacey受伤？选择您的团队面对阿斯顿维拉</span>
          <span class="news-item-title-en">Man Utd latest: Baleba injured, Lacey in? Pick your team to face Aston Villa</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cq146dnrn541o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在与这位少年达成口头协议后，皇家马德里有信心赢得签下曼联前锋JJ加布里埃尔的比赛。" data-title="Real Madrid reach verbal agreement to sign Gabriel" data-date="11-04 19:49" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-04 19:49</span>
          <span class="news-item-title">皇家马德里达成口头协议签署加布里埃尔</span>
          <span class="news-item-title-en">Real Madrid reach verbal agreement to sign Gabriel</span>
          <span class="news-value-point">💡 在与这位少年达成口头协议后，皇家马德里有信心赢得签下曼联前锋JJ加布里埃尔的比赛</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqp9gelp4em2o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="水晶宫在周六被托特纳姆热刺击败时失去了对Jean-Philippe Mateta红牌的吸引力。" data-title="Palace lose appeal against Mateta red card" data-date="11-04 18:23" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-04 18:23</span>
          <span class="news-item-title">宫殿对Mateta红牌失去吸引力</span>
          <span class="news-item-title-en">Palace lose appeal against Mateta red card</span>
          <span class="news-value-point">💡 水晶宫在周六被托特纳姆热刺击败时失去了对Jean-Philippe Mateta红牌的吸引力</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13607845/jj-gabriel-real-madrid-reach-verbal-agreement-with-man-utd-teenager-who-requested-to-leave-old-trafford" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="皇家马德里与16岁的JJ加布里埃尔就潜在的转会圣地亚哥伯纳乌达成了口头协议。" data-title="Real Madrid reach verbal agreement with Man Utd teen star JJ Gabriel" data-date="11-04 17:28" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-04 17:28</span>
          <span class="news-item-title">皇家马德里与曼联青少年明星JJ Gabriel达成口头协议</span>
          <span class="news-item-title-en">Real Madrid reach verbal agreement with Man Utd teen star JJ Gabriel</span>
          <span class="news-value-point">💡 皇家马德里与16岁的JJ加布里埃尔就潜在的转会圣地亚哥伯纳乌达成了口头协议</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13607700/manchester-united-3-2-roma-bruno-fernandes-claims-players-dont-need-to-save-michael-carricks-job-after-first-win-in-10-games" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联队长布鲁诺·费尔南德斯（ Bruno Fernandes ）已经出来支持主教练迈克尔·卡里克（ Michael Carrick ） ，但重申球员在对阵罗马的3-2复出胜利中不需要挽救他的工作。" data-title="Fernandes hits back at &#39;lies&#39; and claims players don&#39;t need to save Carrick&#39;s job" data-date="11-04 15:20" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-04 15:20</span>
          <span class="news-item-title">费尔南德斯反击“谎言” ，声称玩家不需要挽救卡里克的工作</span>
          <span class="news-item-title-en">Fernandes hits back at 'lies' and claims players don't need to save Carrick's job</span>
          <span class="news-value-point">💡 曼联队长布鲁诺·费尔南德斯（ Bruno Fernandes ）已经出来支持主教练迈克尔·卡里克（ Michael Carrick ） ，但重申…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theverge.com/gadgets/1025370/google-pixel-11-pro-phone-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在11月8日之前，您可以在Google的Pixel 11手机上节省大量资金，无论您想要的是最便宜的Pixel 11 ，还是拍摄更好照片的稍贵的Pixel 11 Pro。即使是持久耐用的大型Pixel 11 Pro XL" data-title="Google’s Pixel 11 phones are up to 27 percent off" data-date="11-05 03:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-05 03:00</span>
          <span class="news-item-title">谷歌Pixel 11手机最高可享27%折扣</span>
          <span class="news-item-title-en">Google’s Pixel 11 phones are up to 27 percent off</span>
          <span class="news-value-point">💡 在11月8日之前，您可以在Google的Pixel 11手机上节省大量资金，无论您想要的是最便宜的Pixel 11 ，还是拍摄更好照片的稍贵的P…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/news/1026455/xbox-nano-direct-cloud-wifi-connection-xbox-cloud-gaming-phone-controller" target="_blank" rel="noopener" data-cat="zonghe" data-summary="我昨天透露，新的Xbox Nano控制器支持直接连接到Xbox Cloud Gaming的Wi-Fi连接，现在微软今天正式推出。两个新的Xbox预览将允许玩家尝试使用手机作为智能电视上的控制器" data-title="Xbox previews two new ways to control cloud games" data-date="11-05 03:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-05 03:00</span>
          <span class="news-item-title">Xbox预览了两种控制云游戏的新方法</span>
          <span class="news-item-title-en">Xbox previews two new ways to control cloud games</span>
          <span class="news-value-point">💡 我昨天透露，新的Xbox Nano控制器支持直接连接到Xbox Cloud Gaming的Wi-Fi连接，现在微软今天正式推出</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/cardiff-city-vs-west-ham-united/live/560663" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Cardiff vs West Ham as Parker takes charge LIVE!" data-title="Cardiff vs West Ham as Parker takes charge LIVE!" data-date="11-05 02:45" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-05 02:45</span>
          <span class="news-item-title">卡迪夫vs西汉姆，帕克负责现场直播！</span>
          <span class="news-item-title-en">Cardiff vs West Ham as Parker takes charge LIVE!</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/nfl/news/12040/13608069/nfl-detroit-lions-jack-campbell-has-full-movement-in-lower-body-after-neck-injury-suffered-in-win-over-the-minnesota-vikings" target="_blank" rel="noopener" data-cat="zonghe" data-summary="底特律雄狮队后卫杰克坎贝尔说，在周日的NFL战胜明尼苏达维京人队期间，他因颈部受伤而被送往医院后，他的下半身完全移动。" data-title="Lions&#39; Campbell has full movement in lower body after neck injury" data-date="11-05 02:45" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-05 02:45</span>
          <span class="news-item-title">Lions 'Campbell在颈部受伤后下半身完全活动</span>
          <span class="news-item-title-en">Lions' Campbell has full movement in lower body after neck injury</span>
          <span class="news-value-point">💡 底特律雄狮队后卫杰克坎贝尔说，在周日的NFL战胜明尼苏达维京人队期间，他因颈部受伤而被送往医院后，他的下半身完全移动</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1026604/apple-icloud-links-harmful-content-27-3" target="_blank" rel="noopener" data-cat="zonghe" data-summary="该公司表示，从iOS 27.3和其他27.3更新开始，苹果将开始检查任何拥有“有害内容”链接的人都可以访问的iCloud项目。&quot;当您共享一个可供任何人通过链接访问的项目时，" data-title="Apple will check shared iCloud links for ‘harmful content’" data-date="11-05 02:23" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-05 02:23</span>
          <span class="news-item-title">Apple将检查共享的iCloud链接是否存在“有害内容”</span>
          <span class="news-item-title-en">Apple will check shared iCloud links for ‘harmful content’</span>
          <span class="news-value-point">💡 该公司表示，从iOS 27.3和其他27.3更新开始，苹果将开始检查任何拥有“有害内容”链接的人都可以访问的iCloud项目</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/column/1026464/optimizer-amazon-bee-frontier-ambient-listening-wearables" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这是由Verge资深评论员Victoria Song发送的每周时事通讯Optimizer ，它剖析并讨论了最新的小玩意和药水，这些小玩意和药水宣称它们将改变你的生活。在此选择Optimizer。“这让你有什么感觉？”我问道，" data-title="My therapist thinks I should chuck the Amazon Bee Frontier out a window" data-date="11-05 02:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-05 02:00</span>
          <span class="news-item-title">我的治疗师认为我应该把Amazon Bee Frontier扔出窗外</span>
          <span class="news-item-title-en">My therapist thinks I should chuck the Amazon Bee Frontier out a window</span>
          <span class="news-value-point">💡 这是由Verge资深评论员Victoria Song发送的每周时事通讯Optimizer ，它剖析并讨论了最新的小玩意和药水，这些小玩意和药水宣…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/boxing/news/12040/13608064/joshua-buatsi-open-to-potential-world-title-rematch-with-zach-parker-if-he-beats-dangerous-puncher-umar-dzambekov" target="_blank" rel="noopener" data-cat="zonghe" data-summary="扎克·帕克（ Zach Parker ）希望周六战胜乌马尔·詹贝科夫（ Umar Dzambekov ）可以让他与约书亚·布阿齐（ Joshua Buatsi ）复赛，并有可能" data-title="Buatsi &#39;open&#39; to potential world title rematch with Parker" data-date="11-05 01:58" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-05 01:58</span>
          <span class="news-item-title">Buatsi与Parker “开放”潜在的世界冠军复赛</span>
          <span class="news-item-title-en">Buatsi 'open' to potential world title rematch with Parker</span>
          <span class="news-value-point">💡 扎克·帕克（ Zach Parker ）希望周六战胜乌马尔·詹贝科夫（ Umar Dzambekov ）可以让他与约书亚·布阿齐（ Joshua…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/04/business/cvs-health-split.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在计划于2028年进行的分拆中， CVS Health打算将其保险和药房福利部门整合在一起，并为其药房创建一家独立的公司。" data-title="CVS to Split Off Drugstore Business, Ending Its Bigger" data-date="11-05 01:44" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-05 01:44</span>
          <span class="news-item-title">CVS将拆分药店业务，结束其规模更大的业务</span>
          <span class="news-item-title-en">CVS to Split Off Drugstore Business, Ending Its Bigger</span>
          <span class="news-value-point">💡 在计划于2028年进行的分拆中， CVS Health打算将其保险和药房福利部门整合在一起，并为其药房创建一家独立的公司</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/tennis/news/12040/13607999/atp-paris-masters-novak-djokovic-eliminated-from-atp-finals-race-as-world-no-1-alexander-zverev-also-suffers-shock-exit" target="_blank" rel="noopener" data-cat="zonghe" data-summary="诺瓦克·德约科维奇（ Novak Djokovic ）在劳力士巴黎大师赛（ Rolex Paris Masters ）第二轮失利后，在20个赛季中第二次未能获得本赛季结束的ATP总决赛的资格。" data-title="Djokovic out of ATP Finals race after shock Paris exit along with No 1 Zverev" data-date="11-05 01:43" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-05 01:43</span>
          <span class="news-item-title">德约科维奇（ Djokovic ）与第一名兹韦列夫（ Zverev ）一起在巴黎出局后退出ATP总决</span>
          <span class="news-item-title-en">Djokovic out of ATP Finals race after shock Paris exit along with No 1 Zverev</span>
          <span class="news-value-point">💡 诺瓦克·德约科维奇（ Novak Djokovic ）在劳力士巴黎大师赛（ Rolex Paris Masters ）第二轮失利后，在20个赛季…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/rugby-union/news/12040/13608052/fin-smith-england-pretty-optimistic-fly-half-will-be-fit-for-australia-match-at-twickenham-in-nations-championship" target="_blank" rel="noopener" data-cat="zonghe" data-summary="England &#39;pretty optimistic&#39; Smith will  be fit to face Australia" data-title="England &#39;pretty optimistic&#39; Smith will  be fit to face Australia" data-date="11-05 01:30" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-05 01:30</span>
          <span class="news-item-title">英格兰“相当乐观”的史密斯将适合面对澳大利亚</span>
          <span class="news-item-title-en">England 'pretty optimistic' Smith will  be fit to face Australia</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/games/1026448/sony-playstation-god-of-war-laufey-delay" target="_blank" rel="noopener" data-cat="zonghe" data-summary="开发商Santa Monica Studio今天宣布， God of War Laufey的发布日期将推迟到2027年5月20日。它原定于2月16日在PlayStation 5上推出。以下是Santa Monica Studio关于延迟的完整消息：自从" data-title="God of War Laufey delayed until May" data-date="11-05 01:10" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-05 01:10</span>
          <span class="news-item-title">战神劳菲推迟到5月</span>
          <span class="news-item-title-en">God of War Laufey delayed until May</span>
          <span class="news-value-point">💡 开发商Santa Monica Studio今天宣布， God of War Laufey的发布日期将推迟到2027年5月20日</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/games/1026426/nintendo-switch-cartridges-rom-supplier-data-center" target="_blank" rel="noopener" data-cat="zonghe" data-summary="任天堂即将失去其Switch墨盒的主要内存供应商。供应商Macronix在最近的季度财报电话会议上宣布，它将逐步淘汰ROM生产，而是专注于NOR闪存" data-title="Nintendo is losing a Switch cartridge supplier" data-date="11-05 01:03" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-05 01:03</span>
          <span class="news-item-title">任天堂正在失去Switch墨盒供应商</span>
          <span class="news-item-title-en">Nintendo is losing a Switch cartridge supplier</span>
          <span class="news-value-point">💡 任天堂即将失去其Switch墨盒的主要内存供应商</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/service-providers/network-providers/t-mobile-launches-usd90-5-gbps-fiber-internet-plan-2-5x-speed-boost-comes-with-10-year-price-guarantee" target="_blank" rel="noopener" data-cat="zonghe" data-summary="T-Mobile提供高达5 Gbps的光纤互联网，每月不到100 $" data-title="T-Mobile launches $90 5 Gbps fiber internet plan" data-date="11-05 00:50" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-05 00:50</span>
          <span class="news-item-title">T-Mobile推出$ 90 5 Gbps光纤互联网计划</span>
          <span class="news-item-title-en">T-Mobile launches $90 5 Gbps fiber internet plan</span>
          <span class="news-value-point">💡 T-Mobile提供高达5 Gbps的光纤互联网，每月不到100 $</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/022/472.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 5 日消息，华为云 11 月 1 日发布公告，MaaS 模型即服务平台将于 2026 年 11 月 6 日停止销售 openPangu-2.0-Flash 和 openPangu-2.0-Pro 两款模型服务，并于 11 月 30 日 00:00 正式下线。不过华为官方表示，openPangu 系列新版本模型已在规划中，后续将逐步推出上线。IT之家实测发现，小艺 Work 率先上线了 openPangu-2.1-Pro 模型，主打“鸿蒙任务增强”。华为官方暂未公布该模型的具体能力，同时 openPangu-2.1-Pro 模型的具体参数规格（参数量、激活量、上下文、训练数据等）也尚无公开资料。这说明 2.1-Pro 是非常新且尚未对外公开发布的型号，目前仅在小艺 Work" data-title="华为小艺 Work 率先上线 openPangu-2.1-Pro 模型，主打“鸿蒙任务增强”" data-date="11-05 00:39" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-05 00:39</span>
          <span class="news-item-title">华为小艺 Work 率先上线 openPangu-2.1-Pro 模型，主打“鸿蒙任务增强”</span>
          <span class="news-value-point">💡 IT之家 11 月 5 日消息，华为云 11 月 1 日发布公告，MaaS 模型即服务平台将于 2026 年 11 月 6 日停止销售 open…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/022/470.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 4 日消息，微信鸿蒙版 App 今晚在华为应用市场（App Gallery）发布了 8.0.23.34 正式版更新。和往常一样，本次更新的说明依旧为“修复了一些已知问题”。据用户反馈，8.0.23 版本的微信新增了如下特性：部分 Flutter 跨端页面（如朋友圈、听一听、表情管理等页面）响应系统字体粗细；更换铃声选择界面右上角新增铃声设置入口，支持启用或停用个性化内容推荐；发表视频号内容时新增添加标注，视频号已发布的内容点击分享同步新增添加标注；发现-直播-更多直播新增搜索按钮；听一听主页面右下角新增小微分支入口浮动按钮，并根据当前页面内容弹出对应提示词，可快速使用听一听相关问小微功能，播放页面点击分享新增问小微（主页面右下角浮动按钮为逐步开放）；公众号图标焕新，对齐其" data-title="微信鸿蒙版 App 推 8.0.23.34 正式版更新，更多用户灰度合并发图功能" data-date="11-04 23:56" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-04 23:56</span>
          <span class="news-item-title">微信鸿蒙版 App 推 8.0.23.34 正式版更新，更多用户灰度合并发图功能</span>
          <span class="news-value-point">💡 IT之家 11 月 4 日消息，微信鸿蒙版 App 今晚在华为应用市场（App Gallery）发布了 8.0.23.34 正式版更新</span>
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


<p class="news-updated">🕐 抓取更新于 2026-11-05 03:55（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
