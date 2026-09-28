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
      <span>2026-09-28 15:49 抓取更新</span>
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
        <span class="channel-count">49</span>
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
        <span class="channel-count">4</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('zonghe', this)">
        <span>📰 综合与社会</span>
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('meimei', this)">
        <span>🌍 西方媒体视角</span>
        <span class="channel-count">0</span>
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
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/09-28/10704899.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京9月28日电 (记者 谢雁冰)中国外交部发言人郭嘉昆28日主持例行记者会。有记者就今天是中国和古巴建交66年纪念日提问。" data-title="外交部：坚定支持古巴维护国家主权 反对外来干涉" data-date="09-28 15:49" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 09-28 15:49</span>
      </div>
      <h2 class="hero-featured-title">外交部：坚定支持古巴维护国家主权 反对外来干涉</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/007/849.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 28 日消息，据韩媒 News1 昨天（27 日）报道，当地时间 28 日，英伟达 CEO 黄仁勋将在美国纽约会见三星电子会长李在镕和 SK 集团会长崔泰源。全球 AI 半导体供应链三家核心企业的掌门人也将在两个月后再次聚首，下一代高带宽内存（HBM）和 AI 基础设施合作会谈到哪些内容因此备受关注。韩国商界 27 日消息称，李在镕和崔泰源计划参加 28 日在纽约举行的韩国协会年度晚宴，黄仁勋也会出席当天活动。英伟达、三星和 SK 又都是全球 AI 半导体供应链的重要企业，因此各方是否会讨论进一步合作成为外界关注的焦点。业界预计，HBM 将是此次会面的重点之一，三星电子和 SK 海力士均是英伟达在全球 HBM 市场的主要内存供应商。三星电子 DS 部门负责人全永铉今年 6" data-title="AI 半导体供应链三巨头时隔两月再聚首，曝英伟达黄仁勋、三星李在镕、SK 崔泰源将在美会面" data-date="09-28 15:42" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">AI 半导体供应链三巨头时隔两月再聚首，曝英伟达黄仁勋、三星李在镕、SK 崔泰源将在美会面</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.com/zhongwen/articles/ckjrxw02e7q3o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Big Bang 在伦敦托特纳姆热刺体育场举行了演唱会，这标志着这个帮助奠定现代 K-pop 蓝图的组合回归，可谓是万众期待。" data-title="BigBang伦敦开唱：K" data-date="09-28 14:40" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">BigBang伦敦开唱：K</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/007/854.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 28 日消息，新奥集团今日宣布，新奥氢硼聚变商业化在 2026 年 9 月下旬取得重大突破：“玄龙-50U”装置实现氢硼聚变反应。这是全球商业化聚变公司在自有装置上首次实现氢硼聚变反应，也是我国磁约束聚变装置首次实现加注先进燃料（氢硼、氘氦 3）的清洁无中子聚变反应。氢硼聚变具有无中子、燃料丰富易得、低成本等商业化优势，产物是氦（α 粒子），但相对于氘氚聚变，其反应温度及三乘积要求更高，反应条件更苛刻。本次新奥聚变团队通过高能中性束注入与射频波的协同，大幅提高了氢硼反应第一共振峰的非热平衡快质子份额，实现了大于 108/秒的氢硼聚变反应率。这表明新奥氢硼聚变迈入燃烧等离子体相关实验阶段，是中国多路径聚变能发展的重大突破。来自全球多个国家科研院所与知名高校的十余位聚变权威专家" data-title="全球首次：新奥氢硼聚变商业化取得重大突破，2035 年前实现稳态大功率发电" data-date="09-28 15:50" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">全球首次：新奥氢硼聚变商业化取得重大突破，2035 年前实现稳态大功率发电</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-28/10704899.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京9月28日电 (记者 谢雁冰)中国外交部发言人郭嘉昆28日主持例行记者会。有记者就今天是中国和古巴建交66年纪念日提问。" data-title="外交部：坚定支持古巴维护国家主权 反对外来干涉" data-date="09-28 15:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-28 15:49</span>
          <span class="news-item-title">外交部：坚定支持古巴维护国家主权 反对外来干涉</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-28/10704864.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网天津9月28日电 (记者 周亚强)中国新型政党制度理论研讨会28日在天津召开，会上发布《中国新型政党制度自主知识体系研究报告》。" data-title="中国新型政党制度自主知识体系研究报告在天津发布" data-date="09-28 15:25" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-28 15:25</span>
          <span class="news-item-title">中国新型政党制度自主知识体系研究报告在天津发布</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-28/10704857.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月28日电 据外媒报道，德国方面9月27日发布的一项最新民调结果显示，德国总理默茨领导的联盟党(基民盟/基社盟)支持率降至19%，为本届联邦议会选举周期以来最低水平，与选择党相差10个百分点。" data-title="外媒：默茨领导的联盟党支持率跌至议会选举期以来最低" data-date="09-28 15:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-28 15:13</span>
          <span class="news-item-title">外媒：默茨领导的联盟党支持率跌至议会选举期以来最低</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-28/10704849.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网昆明9月28日电 (记者 韩帅南)9月28日，云南省生态环境厅举行“环境安全，我们在行动——听民声、防风险、护家园”专题新闻发布会通报称，截至9月，今年以来云南省生态环境部门职责范围内投诉举报件按期办结率达100%；全省重点环境风险区域已实现4小时应急物资保障圈；曲靖花山化工园区突发水污染事件环境应急三级防控体系建设试点8月顺利通过国家验收。" data-title="云南重点环境风险区域实现4小时应急物资保障圈" data-date="09-28 14:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-28 14:57</span>
          <span class="news-item-title">云南重点环境风险区域实现4小时应急物资保障圈</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-28/10704843.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网广州9月28日电 (记者 方伟彬)广州法治大厦项目28日正式开工。同日，作为拟入驻机构的广州互联网法院迎来挂牌成立8周年，其建设发展迈入新阶段。" data-title="广州法治大厦项目正式开工" data-date="09-28 14:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-28 14:44</span>
          <span class="news-item-title">广州法治大厦项目正式开工</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-28/10704837.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月28日电 北京时间9月27日晚，英国歌唱家莎拉·布莱曼在社交媒体平台上悼念中国音乐家刘欢。" data-title="英国歌唱家莎拉·布莱曼发文悼念刘欢：将永远怀念他" data-date="09-28 14:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-28 14:14</span>
          <span class="news-item-title">英国歌唱家莎拉·布莱曼发文悼念刘欢：将永远怀念他</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-28/10704823.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网乌鲁木齐9月28日电 (袁鹏冲)从校园课堂的思政浸润，到中华优秀传统文化的滋养熏陶，再到跨城研学的心灵牵手，近年来，新疆和田地区各族青少年在多层次、全方位的援疆育人举措中茁壮成长。" data-title="京和同心育新苗 “六位一体”铸牢新疆和田少年中华魂" data-date="09-28 13:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-28 13:50</span>
          <span class="news-item-title">京和同心育新苗 “六位一体”铸牢新疆和田少年中华魂</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-28/10704810.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月28日电(记者 刁炜)俄著名智库“俄罗斯国际事务委员会”近日刊文披露，澳大利亚已允许日本自卫队使用该国靶场，开展包括高超音速武器在内的新型导弹测试。" data-title="提供12万平方公里靶场，澳大利亚要帮日本测试高超音速导弹" data-date="09-28 13:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-28 13:44</span>
          <span class="news-item-title">提供12万平方公里靶场，澳大利亚要帮日本测试高超音速导弹</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-28/10704737.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月28日电 综合消息：以色列方面当地时间27日表示，决定不再承认荷兰驻拉姆安拉代表处外交人员的外交身份，其享有的外交特权与豁免权将在7天后到期。" data-title="以色列取消荷兰驻拉姆安拉外交人员外交豁免" data-date="09-28 11:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-28 11:00</span>
          <span class="news-item-title">以色列取消荷兰驻拉姆安拉外交人员外交豁免</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-28/10704702.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网比勒陀利亚9月28日电(记者 孙翔)“同一轮圆月！”“同一种友谊！”9月26日至27日，2026中南中秋文化交流节在南非行政首都比勒陀利亚时代广场举行。舞台上下，一呼一应，不同的族群、语言与文化，在这一刻汇入同一片掌声与喝彩。" data-title="“同一轮圆月，同一种友谊”：中国中秋节与南非文化遗产月相遇" data-date="09-28 10:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-28 10:36</span>
          <span class="news-item-title">“同一轮圆月，同一种友谊”：中国中秋节与南非文化遗产月相遇</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-28/10704719.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月28日电 贝尔格莱德消息：塞尔维亚总统武契奇当地时间27日晚提交辞呈，辞去总统职务。他表示此后将以“普通公民”身份参加下届政府总理竞选。" data-title="塞尔维亚总统武契奇辞职 将竞选政府总理" data-date="09-28 10:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-28 10:36</span>
          <span class="news-item-title">塞尔维亚总统武契奇辞职 将竞选政府总理</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-28/10704708.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中国新闻周刊记者：杨智杰" data-title="非洲电商“新蓝海”" data-date="09-28 10:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-28 10:06</span>
          <span class="news-item-title">非洲电商“新蓝海”</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cx5yln334jq5o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="“我拒绝他们的协议，”特朗普周六表示，并补充美国已对该海峡拥有“完全控制权”，“大量石油”经此通行，导致全球油价大幅上涨，消费者燃料成本急升。" data-title="中美峰会后 伊朗提出七天达成协议 被特朗普拒绝" data-date="09-28 08:10" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-28 08:10</span>
          <span class="news-item-title">中美峰会后 伊朗提出七天达成协议 被特朗普拒绝</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/27/us/politics/trump-weapons-sale-china.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="特朗普总统向中国领导人习近平提出了这一提议，驻华大使大卫·珀杜（ David Perdue ）说。白宫后来表示，美国没有计划进行此类销售。" data-title="美国大使说，特朗普提出向中国出售武器" data-date="09-28 07:33" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-28 07:33</span>
          <span class="news-item-title">美国大使说，特朗普提出向中国出售武器</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/27/us/politics/trump-ad-government-campaign.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="伦理专家称，这则广告可能违反了联邦法律。这则广告显示，特朗普誓言要“将战争贩子驱逐出政府，与“深层国家”作斗争，即使他正在与伊朗开战。" data-title="特朗普2024竞选广告回归，现在由政府带给您" data-date="09-28 06:12" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-28 06:12</span>
          <span class="news-item-title">特朗普2024竞选广告回归，现在由政府带给您</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/007/849.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 28 日消息，据韩媒 News1 昨天（27 日）报道，当地时间 28 日，英伟达 CEO 黄仁勋将在美国纽约会见三星电子会长李在镕和 SK 集团会长崔泰源。全球 AI 半导体供应链三家核心企业的掌门人也将在两个月后再次聚首，下一代高带宽内存（HBM）和 AI 基础设施合作会谈到哪些内容因此备受关注。韩国商界 27 日消息称，李在镕和崔泰源计划参加 28 日在纽约举行的韩国协会年度晚宴，黄仁勋也会出席当天活动。英伟达、三星和 SK 又都是全球 AI 半导体供应链的重要企业，因此各方是否会讨论进一步合作成为外界关注的焦点。业界预计，HBM 将是此次会面的重点之一，三星电子和 SK 海力士均是英伟达在全球 HBM 市场的主要内存供应商。三星电子 DS 部门负责人全永铉今年 6" data-title="AI 半导体供应链三巨头时隔两月再聚首，曝英伟达黄仁勋、三星李在镕、SK 崔泰源将在美会面" data-date="09-28 15:42" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-28 15:42</span>
          <span class="news-item-title">AI 半导体供应链三巨头时隔两月再聚首，曝英伟达黄仁勋、三星李在镕、SK 崔泰源将在美会面</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/007/848.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 28 日消息，据韩媒 smedaily 当地时间今日报道，SK 海力士驳斥了“日本东北地区晶圆厂项目已启动”的传闻，称这“纯属无稽之谈”。消息人士此前表示，一座与 SK 海力士有关的日本晶圆厂已在进行基础工程施工，尚不清楚是独资还是与铠侠合资；SK 海力士近期要求韩国零部件企业扩大供应规模，以应对内存供应短缺。相关阅读：《SK 集团会长崔泰源：SK 海力士正考虑在日本设厂事宜》" data-title="SK 海力士驳斥“日本东北地区晶圆厂动工”传闻，称“纯属无稽之谈”" data-date="09-28 15:41" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-28 15:41</span>
          <span class="news-item-title">SK 海力士驳斥“日本东北地区晶圆厂动工”传闻，称“纯属无稽之谈”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-28/10704888.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="新华社北京9月28日电(记者吴梦桐、冯歆然)外交部发言人郭嘉昆28日在例行记者会上答问时表示，中方始终秉持建设性、负责任态度参与人工智能全球治理，持续不断贡献中国方案。中方一贯主张应当坚持发挥联合国主渠道作用，构建公正合理的全球人工智能治理体系。同时，我们也愿同美方通过人工智能政府间对话等渠道保持沟通交流。这既是促进全球人工智能向善普惠发展的重要路径，也是构建“基于尊重、公平、对等的中美建设性战略稳定关系”的应有之义。" data-title="外交部：愿同美方通过人工智能政府间对话等渠道保持沟通" data-date="09-28 15:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-28 15:39</span>
          <span class="news-item-title">外交部：愿同美方通过人工智能政府间对话等渠道保持沟通</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-28/10704825.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新社北京9月28日电 (记者 孙自法)中国科学院28日消息，作为其未来五年的总体“路线图”和具体“施工图”，该院“十五五”发展规划近日正式发布，其中明确提出，积极拥抱人工智能(AI)蓬勃发展战略机遇，赋能科技创新和科研管理变革。" data-title="中国科学院发布“十五五”规划：积极拥抱人工智能" data-date="09-28 13:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-28 13:52</span>
          <span class="news-item-title">中国科学院发布“十五五”规划：积极拥抱人工智能</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1001193/engram-sampler-ai-hallucinations-music" target="_blank" rel="noopener" data-cat="keji" data-summary="音乐创业公司Thoughtful Things刚刚推出了其首款乐器Engram的Kickstarter活动。它是一个采样器和Groovebox ，使用AI来破坏传入的音频，甚至使全新的声音产生幻觉。不过，这不是盒子里的苏诺。这不是一个“按钮，让歌声响起”的设备，旨在创造一些听起来已经准备好进入40强的设备[…]" data-title="Engram是一个将破碎的人工智能幻觉转化为音乐的采样器" data-date="09-28 04:46" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-28 04:46</span>
          <span class="news-item-title">Engram是一个将破碎的人工智能幻觉转化为音乐的采样器</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/27/anthropics-ceo-is-about-to-have-dinner-with-president-trump/" target="_blank" rel="noopener" data-cat="keji" data-summary="这将是Dario Amodei和唐纳德·特朗普之间的首次一对一会面" data-title="Anthropic首席执行官即将与特朗普总统共进晚餐" data-date="09-28 04:34" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-28 04:34</span>
          <span class="news-item-title">Anthropic首席执行官即将与特朗普总统共进晚餐</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/27/can-muse-overcome-metas-trust-issues/" target="_blank" rel="noopener" data-cat="keji" data-summary="关于Equity ，我们讨论了Meta的人工智能公告如何设法从OpenAI和Anthropic抢走聚光灯。" data-title="Muse能否克服Meta的信任问题？" data-date="09-28 03:57" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-28 03:57</span>
          <span class="news-item-title">Muse能否克服Meta的信任问题？</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1001178/openai-agents-bruteforce-un-website" target="_blank" rel="noopener" data-cat="keji" data-summary="安全研究员罗恩·霍华德-琼斯（ Rowan Howard-Jones ）表示， OpenAI特工在4月至6月期间扫描了联合国贸易和发展会议（ UNCTAD ）的统计数据网站超过16,000次。虽然该事件并未达到拥抱面部黑客攻击或最近对美国政府网站的攻击的水平，但这是另一个令人担忧的人工智能[…]的例子。" data-title="OpenAI特工试图“蛮力”联合国网站" data-date="09-28 01:21" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-28 01:21</span>
          <span class="news-item-title">OpenAI特工试图“蛮力”联合国网站</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/27/anthropics-dario-amodei-gets-the-snl-treatment/" target="_blank" rel="noopener" data-cat="keji" data-summary="“人工智能是魔鬼，我是创造者。”" data-title="Anthropic的Dario Amodei接受SNL治疗" data-date="09-28 00:30" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-28 00:30</span>
          <span class="news-item-title">Anthropic的Dario Amodei接受SNL治疗</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/27/world/asia/china-us-ai-distrust.html" target="_blank" rel="noopener" data-cat="keji" data-summary="在中国，人工智能世界末日警告可能让人感觉明显是西方的，或者像是阻止中国人工智能公司试图超越美国竞争对手的伎俩。" data-title="中国对人工智能安全呼叫持怀疑态度的惊人原因" data-date="09-28 00:07" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-28 00:07</span>
          <span class="news-item-title">中国对人工智能安全呼叫持怀疑态度的惊人原因</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/007/612.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 27 日消息，iQOO Pad Ultra 平板 9 月 27 日官宣搭载 9020mAh 蓝海大电池，8.8 英寸机身轻至 298g，机身厚度仅 5.74mm。IT之家注意到，iQOO Pad Ultra 小平板已官宣将于 9 月 29 日 19:00 发布，新机提供星铠银 / 末影黑双色、内置风扇，采用全金属机身，将首批搭载高通第六代骁龙 8 超级至尊版处理器，配备对称式超线性双扬声器、双 X 轴线性马达。iQOO Pad Ultra 搭载 8.8 英寸 165Hz OLED 极竞屏，四等边 2.65mm 边框。根据官方海报，iQOO Pad Ultra 屏幕局部峰值亮度 4500nits，响应速度 此外，iQOO Pad Ultra 搭载冰穹五重风冷散热系统，内置一颗" data-title="iQOO Pad Ultra 平板官宣搭载 9020mAh 蓝海电池，8.8 英寸机身轻至 298g" data-date="09-27 23:47" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-27 23:47</span>
          <span class="news-item-title">iQOO Pad Ultra 平板官宣搭载 9020mAh 蓝海电池，8.8 英寸机身轻至 298g</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/laptops/gaming-laptops/grab-this-14-inch-compact-gaming-laptop-powerhouse-for-usd1000-off-hp-omen-transcend-14-with-rtx-5070-and-3k-oled-display-drops-to-usd1-999-99-at-best-buy" target="_blank" rel="noopener" data-cat="keji" data-summary="这款游戏笔记本电脑将英特尔的Core Ultra 9 285H与英伟达的RTX 5070笔记本电脑GPU和3K 120Hz OLED显示屏配对，以更低的价格为买家提供强大的紧凑型机器。" data-title="购买这款14英寸紧凑型游戏笔记本电脑，立省$ 1000" data-date="09-27 23:21" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-27 23:21</span>
          <span class="news-item-title">购买这款14英寸紧凑型游戏笔记本电脑，立省$ 1000</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/498633.html" target="_blank" rel="noopener" data-cat="keji" data-summary="量子AI创业来了一支“清华梦之队”：10亿估值，用量子改造大模型底层" data-title="量子AI创业来了一支“清华梦之队”：10亿估值，用量子改造大模型底层" data-date="09-27 22:20" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-27 22:20</span>
          <span class="news-item-title">量子AI创业来了一支“清华梦之队”：10亿估值，用量子改造大模型底层</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/thieves-steal-nvidia-labeled-trailers-expecting-massive-ai-gpu-payday-but-score-40-000-pounds-of-sand-instead-crooks-duped-by-20-tons-of-ballast-sand" target="_blank" rel="noopener" data-cat="keji" data-summary="两辆带有Nvidia合作伙伴标记的PlusAI预告片显然被留在了初创公司的仓库外，使其成为希望在AI GPU上轻松赚钱的犯罪分子的诱人目标。然而，他们被故意留在外面，因为拖车只包含用于模拟真实世界卡车载荷的沙子。" data-title="窃贼窃取Nvidia标签的预告片，期待大量的AI GPU发薪日，但却获得了40,000磅的沙子" data-date="09-27 22:14" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-27 22:14</span>
          <span class="news-item-title">窃贼窃取Nvidia标签的预告片，期待大量的AI GPU发薪日，但却获得了40,000磅的沙子</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/498605.html" target="_blank" rel="noopener" data-cat="keji" data-summary="想让开发者“说句话就能跑量子计算”" data-title="量子计算走上桌面！“小盒子”跑通端到端，数据全程不出门" data-date="09-27 21:57" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-27 21:57</span>
          <span class="news-item-title">量子计算走上桌面！“小盒子”跑通端到端，数据全程不出门</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">4 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/ckjrxw02e7q3o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Big Bang 在伦敦托特纳姆热刺体育场举行了演唱会，这标志着这个帮助奠定现代 K-pop 蓝图的组合回归，可谓是万众期待。" data-title="BigBang伦敦开唱：K" data-date="09-28 14:40" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-28 14:40</span>
          <span class="news-item-title">BigBang伦敦开唱：K</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmn45n5d8wq7o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在控球率超过60%的球队中，只有36%的球队在本赛季赢得了英超联赛的冠军。BBC Sport着眼于为什么？" data-title="英超联赛控球比赛即将结束吗？" data-date="09-28 14:10" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-28 14:10</span>
          <span class="news-item-title">英超联赛控球比赛即将结束吗？</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/commentisfree/2026/sep/27/the-guardian-view-on-manchester-city-a-strange-kind-of-glory" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="如果对俱乐部多项财务错误报告的有罪判决得到支持，那么它在现代取得的成就将永远受到玷污。在英超联赛最伟大时刻的调查中，足球支持者经常为塞尔吉奥·阿圭罗（ Sergio Agüero ）在2012年赢得曼城冠军的目标感到自豪。本赛季最后一天在伤病时间得分，阿奎罗对皇后公园巡游者的罢工首次" data-title="卫报对曼城的看法：一种奇怪的荣耀|社论" data-date="09-28 00:25" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-28 00:25</span>
          <span class="news-item-title">卫报对曼城的看法：一种奇怪的荣耀|社论</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cw3d77ne44k5o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="花了两年多的时间，但似乎终于对针对曼城的115项指控做出了判决。以下是它的含义。" data-title="为什么英超在曼城统治后面临不确定性和混乱" data-date="09-27 22:24" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-27 22:24</span>
          <span class="news-item-title">为什么英超在曼城统治后面临不确定性和混乱</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/007/854.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 28 日消息，新奥集团今日宣布，新奥氢硼聚变商业化在 2026 年 9 月下旬取得重大突破：“玄龙-50U”装置实现氢硼聚变反应。这是全球商业化聚变公司在自有装置上首次实现氢硼聚变反应，也是我国磁约束聚变装置首次实现加注先进燃料（氢硼、氘氦 3）的清洁无中子聚变反应。氢硼聚变具有无中子、燃料丰富易得、低成本等商业化优势，产物是氦（α 粒子），但相对于氘氚聚变，其反应温度及三乘积要求更高，反应条件更苛刻。本次新奥聚变团队通过高能中性束注入与射频波的协同，大幅提高了氢硼反应第一共振峰的非热平衡快质子份额，实现了大于 108/秒的氢硼聚变反应率。这表明新奥氢硼聚变迈入燃烧等离子体相关实验阶段，是中国多路径聚变能发展的重大突破。来自全球多个国家科研院所与知名高校的十余位聚变权威专家" data-title="全球首次：新奥氢硼聚变商业化取得重大突破，2035 年前实现稳态大功率发电" data-date="09-28 15:50" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-28 15:50</span>
          <span class="news-item-title">全球首次：新奥氢硼聚变商业化取得重大突破，2035 年前实现稳态大功率发电</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/007/850.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 28 日消息，鸿蒙智行旗下享界品牌首款 MPV—— 享界 V8 今日正式开启预订，官方预售价 32.98 万元起，现在下订可享价值 6000 元权益。新车定位家庭智慧旗舰 MPV，提供纯电与增程两种动力形式，全系标配 800V 高压平台和华为干昆智驾系统。享界 V8 纯电版搭载 120 kWh 超大电池，CLTC 工况续航最高达 830km，四驱版续航为 775km。增程版则搭载 1.5T 增程器，最大功率 118kW，提供 56kWh 与 75.4kWh 两种电池规格，WLTC 纯电续航分别为 260km、275km 和 339km，CLTC 综合续航超过 1400km。享界 V8 车身尺寸为 5335/2005/1805mm，轴距 3250mm，采用 2+2+3 七座布" data-title="32.98 万元起鸿蒙智行享界 V8 开启预订：全系 800V 高压平台 + 华为干昆智驾，纯电续航 830km" data-date="09-28 15:44" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-28 15:44</span>
          <span class="news-item-title">32.98 万元起鸿蒙智行享界 V8 开启预订：全系 800V 高压平台 + 华为干昆智驾，纯电续航 830km</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/007/846.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 28 日消息，森海塞尔 MOMENTUM 5 头戴式耳机现已新增焦糖棕、薰衣草两种配色，定价均为 3299 元。京东森海塞尔 MOMENTUM5 头戴式耳机 3299 元直达链接IT之家从商品页面获悉，新品采用森海塞尔自主研发的 42 毫米动圈驱动单元，其灵感源自经久不衰的高保真 HD600 系列，搭配数十年的声学调校经验。新品兼容 SBC、AAC、aptX、aptX HD、aptX Adaptive 等主流编解码器，更搭载骁龙畅听 TT 技术，支持 aptX Lossless 编解码器，可以通过蓝牙实现 CD 品质的无损音频传输（16 bit/44.1kHz）。配合 Hi-Res 认证，支持无线高解析音频、杜比全景声空间音频。森海塞尔提升了 MOMENTUM5 无线耳机的" data-title="森海塞尔 MOMENTUM 5 头戴式耳机新增焦糖棕、薰衣草配色，3299 元" data-date="09-28 15:39" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-28 15:39</span>
          <span class="news-item-title">森海塞尔 MOMENTUM 5 头戴式耳机新增焦糖棕、薰衣草配色，3299 元</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-28/10704885.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="千里秦岭不再是天堑，南北烟火从此双向奔赴！" data-title="西康高铁开通！肉夹馍离重庆火锅不远啦！" data-date="09-28 15:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-28 15:32</span>
          <span class="news-item-title">西康高铁开通！肉夹馍离重庆火锅不远啦！</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/007/841.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 28 日消息，极米 Z 系列投影仪新品今天在京东开启新品预约，价格暂未公布，预计将于 10 月 15 日 20:00 开售。京东极米 Z 系列 投影仪新品未公布立即预约据官方介绍，该投影仪主打“经典焕新”，相比此前产品全面升级。现阶段预约可享加赠芒果 TV 会员月卡。截至目前，极米暂未公布这款新品的详细信息，IT之家将持续关注，第一时间带来最新消息。" data-title="极米 Z 系列投影仪新品开启预约，预计 10 月 15 日开售" data-date="09-28 15:24" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-28 15:24</span>
          <span class="news-item-title">极米 Z 系列投影仪新品开启预约，预计 10 月 15 日开售</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-28/10704863.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社圣保罗9月28日电 (记者 林春茵)当地时间27日，可纳千余人的巴西圣保罗保罗·奥特朗剧院座无虚席。“中巴文化年”中外经典歌剧选段音乐会在此间举行，来自中国中央歌剧院的音乐家们与巴西歌唱家联袂演出，以乐会友。" data-title="“中巴文化年”中外经典歌剧选段音乐会在圣保罗举行" data-date="09-28 15:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-28 15:21</span>
          <span class="news-item-title">“中巴文化年”中外经典歌剧选段音乐会在圣保罗举行</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/28/world/europe/raf-fairford-incident-air-base-terrorism-uk.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Five men were arrested Sunday as they approached R.A.F. Fairford, a British installation used by the U.S. in its war against Iran. The men are being held on suspicion of terrorism." data-title="英国皇家空军费尔福德空军基地可能发生的恐怖阴谋：我们所知道的" data-date="09-28 15:20" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-28 15:20</span>
          <span class="news-item-title">英国皇家空军费尔福德空军基地可能发生的恐怖阴谋：我们所知道的</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-28/10704852.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="法治在线丨半分钟广告弹窗近20次 防不胜防的手机广告弹窗该如何治？" data-title="半分钟广告弹窗近20次 防不胜防的手机广告弹窗该如何治？" data-date="09-28 15:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-28 15:01</span>
          <span class="news-item-title">半分钟广告弹窗近20次 防不胜防的手机广告弹窗该如何治？</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-28/10704841.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网上海9月28日电 (记者 陈静)“我也想站到那个最高的世界舞台上，让大家看到中国男护士的力量和温度。”第48届世界技能大赛(下称：世赛)“健康和社会照护”项目金牌获得者——上海健康医学院2022级护理学专业本科生闵思达曾这样说。他真的做到了。" data-title="世赛金牌获得者闵思达：让世界看到中国男护士的力量和温度" data-date="09-28 14:46" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-28 14:46</span>
          <span class="news-item-title">世赛金牌获得者闵思达：让世界看到中国男护士的力量和温度</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-28/10704846.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="据国家移民管理局通报，今年中秋节假期全国边检机关共保障670.9万人次中外人员出入境，日均223.6万人次，较去年中秋节期间增长16.8%；单日出入境通关最高峰出现在9月26日，达234.2万人次。其中：" data-title="中秋节假期670.9万人次出入境" data-date="09-28 14:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-28 14:32</span>
          <span class="news-item-title">中秋节假期670.9万人次出入境</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-28/10704840.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网广州9月28日电 (记者 王坚)广东省水利厅28日通报称，广东今年把“推动建设超100条(个)幸福河湖，超5个县(市、区)开展全域幸福河湖建设”列入广东省十件民生实事。截至目前，全省第一批16个县(市、区)全域幸福河湖建设实施方案已全部印发，106条(个)“母亲河”、骨干河湖幸福河湖开工建设，标志着广东省首批全域幸福河湖建设由蓝图绘制转入全面实施。" data-title="广东首批县（市、区）全域幸福河湖建设全面实施" data-date="09-28 14:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-28 14:29</span>
          <span class="news-item-title">广东首批县（市、区）全域幸福河湖建设全面实施</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-28/10704829.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网上海9月28日电(记者 高萌)现象级电视剧《繁花》不仅带火了海派文化，更作为优质国产IP走出国门。而伴随热度而来的，还有猖獗的跨境盗版乱象。面对一起零口供、高对抗的《繁花》等影视作品跨境盗版案件，检察机关是如何击碎犯罪分子逍遥法外幻想的？" data-title="《繁花》等影视作品跨境盗版案背后：检察护航文化出海" data-date="09-28 13:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-28 13:55</span>
          <span class="news-item-title">《繁花》等影视作品跨境盗版案背后：检察护航文化出海</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-28/10704817.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网昌吉9月28日电 题：天山小院里一个社区自助养老院的母女“接力”" data-title="天山小院里 一个社区自助养老院的母女“接力”" data-date="09-28 13:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-28 13:49</span>
          <span class="news-item-title">天山小院里 一个社区自助养老院的母女“接力”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-28/10704816.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网郑州9月28日电 (刘鹏 杨震) 中国铁路郑州局集团有限公司(以下简称“国铁集团郑州局”)28日消息，9月25日至27日，中秋假期3天，国铁集团郑州局累计加开临客列车210列，发送旅客202.7万人次。" data-title="国铁郑州局中秋假期累计加开临客210列 发送旅客超202万人次" data-date="09-28 13:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-28 13:48</span>
          <span class="news-item-title">国铁郑州局中秋假期累计加开临客210列 发送旅客超202万人次</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/crgjq913xgxgo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="声称入侵美国联邦调查局（FBI）的网络罪犯表示，他们掌握数以千计特工极为敏感的医疗资料。现任及前任特工向BBC讲述事件带来的毁灭性影响。" data-title="FBI遭黑客入侵起底 特工们的恐惧与愤怒" data-date="09-28 13:45" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-28 13:45</span>
          <span class="news-item-title">FBI遭黑客入侵起底 特工们的恐惧与愤怒</span>
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


<p class="news-updated">🕐 抓取更新于 2026-09-28 15:49（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
