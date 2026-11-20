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
      <span>2026-11-20 17:18 抓取更新</span>
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
        <span class="channel-count">61</span>
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
      <button class="channel-btn" onclick="filterNewsChannel('meimei', this)">
        <span>🌍 西方媒体视角</span>
        <span class="channel-count">1</span>
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
  <div class="ov-item"><span class="ov-num">61</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×20 · 天空体育×13</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">按来源聚合 · 最近 24 小时精选</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/11-20/10735303.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月20日电 (记者 孙自法)《地球大数据支撑可持续发展目标报告(2026)——全球发展倡议五周年特别报告》11月20日在北京发布，这一被形象称为地球的年度“体检”报告显示，根据15项全球一致可比的指标评估测算，中国综合可持续发展目标(SDGs)贡献度达5.84%，位列全球第一，在工业热源排放改善、城市公共交通普及、粮食单产提升、城市绿地建设等领域，中国贡献度均居全球首位。" data-title="2026地球“体检”报告：中国多个可持续发展指标贡献度居全球首位" data-date="11-20 16:57" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 11-20 16:57</span>
      </div>
      <h2 class="hero-featured-title">2026地球“体检”报告：中国多个可持续发展指标贡献度居全球首位</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/030/131.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 20 日消息，AMD 当地时间 19 日宣布，其锐龙 AI 处理器上的 &quot;XDNA 2&quot; NPU 成为首款获得 Unsloth Desktop 本地界面支持的神经网络处理器。具体来看，兼容的应用程序向 Unsloth Desktop API 发送模型请求，而 Lemonade 和 FastFlowLM 则在 AMD XDNA 2 NPU 上处理模型服务和推理。模型的响应返回给应用程序，供其工作流程使用。这意味着 OpenClaw、Hermes 等超百款智能体可通过 Unsloth Desktop 在锐龙 AI 处理器的 NPU 上本地运行，从 CPU 和 GPU 上卸载相关 AI 工作负载，留出更多算力以供其它任务使用，也有助于延长带电池设备的续航。" data-title="AMD XDNA2 NPU 率先获得 Unsloth Desktop 适配，支持超百款智能体" data-date="11-20 17:13" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">AMD XDNA2 NPU 率先获得 Unsloth Desktop 适配，支持超百款智能体</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/live/2026/nov/20/weekend-football-countdown-live-news-updates" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="⚽ 周末即将到来之际的所有最新足球新闻⚽ 赛程 | 排行榜 | 十大看点 | 致函Tom感谢国际足球、足总杯和曼联智囊团，这真有意思。我们很快会再见。现在是时候" data-title="Premier League returns, Pochettino readies for United test and more" data-date="11-20 17:15" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">英超联赛回归，波切蒂诺为曼联的考验做好准备，以及更多资讯</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/11-20/10735330.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网南昌11月20日电 陕西富平县日前于江西南昌举办两场文旅推介活动，依托活动搭建黄河文化与长江文化交流平台，拓展省外旅游客源市场。" data-title="富平赴南昌开展两场文旅推介 推进赣陕文旅协作" data-date="11-20 17:10" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">富平赴南昌开展两场文旅推介 推进赣陕文旅协作</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-20/10735303.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月20日电 (记者 孙自法)《地球大数据支撑可持续发展目标报告(2026)——全球发展倡议五周年特别报告》11月20日在北京发布，这一被形象称为地球的年度“体检”报告显示，根据15项全球一致可比的指标评估测算，中国综合可持续发展目标(SDGs)贡献度达5.84%，位列全球第一，在工业热源排放改善、城市公共交通普及、粮食单产提升、城市绿地建设等领域，中国贡献度均居全球首位。" data-title="2026地球“体检”报告：中国多个可持续发展指标贡献度居全球首位" data-date="11-20 16:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 16:57</span>
          <span class="news-item-title">2026地球“体检”报告：中国多个可持续发展指标贡献度居全球首位</span>
          <span class="news-value-point">💡 中新网北京11月20日电 (记者 孙自法)《地球大数据支撑可持续发展目标报告(2026)——全球发展倡议五周年特别报告》11月20日在北京发布，…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-20/10735308.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="自11月25日起，北京经乌兰巴托至伊尔库茨克的中蒙俄国际旅客列车每周往返开行，将进一步促进中蒙俄三国人员往来、经贸合作和人文交流。" data-title="中蒙俄国际旅客列车11月25日起每周往返开行" data-date="11-20 16:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 16:36</span>
          <span class="news-item-title">中蒙俄国际旅客列车11月25日起每周往返开行</span>
          <span class="news-value-point">💡 自11月25日起，北京经乌兰巴托至伊尔库茨克的中蒙俄国际旅客列车每周往返开行，将进一步促进中蒙俄三国人员往来、经贸合作和人文交流</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-20/10735305.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="羊城晚报#8226;羊城派 古司祺 沉重光 等" data-title="深度｜APEC领导人会议周的外媒记者，看到一个怎样的中国？" data-date="11-20 16:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 16:32</span>
          <span class="news-item-title">深度｜APEC领导人会议周的外媒记者，看到一个怎样的中国？</span>
          <span class="news-value-point">💡 羊城晚报#8226;羊城派 古司祺 沉重光 等</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-20/10735302.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="11月18日至19日，亚太经合组织第三十三次领导人非正式会议在深圳举行，多国媒体与智库从不同视角关注中国在亚太合作中的引领作用。" data-title="全球媒体聚焦 | “中国的发展为亚太各方带来实实在在新机遇”" data-date="11-20 16:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 16:28</span>
          <span class="news-item-title">全球媒体聚焦 | “中国的发展为亚太各方带来实实在在新机遇”</span>
          <span class="news-value-point">💡 11月18日至19日，亚太经合组织第三十三次领导人非正式会议在深圳举行，多国媒体与智库从不同视角关注中国在亚太合作中的引领作用</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-20/10735283.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月20日电 (记者 曾玥)中国外交部发言人20日宣布：应新加坡副总理颜金勇邀请，中共中央政治局常委、国务院副总理丁薛祥将于11月22日至23日访问新加坡，同颜金勇副总理共同主持中新双边合作联委会第二十二次会议、中新苏州工业园区联合协调理事会第二十七次会议、中新天津生态城联合协调理事会第十八次会议、中新(重庆)战略性互联互通示范项目联合协调理事会第十次会议。" data-title="丁薛祥将访问新加坡并主持中新双边合作机制会议 外交部介绍有关情况" data-date="11-20 16:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 16:24</span>
          <span class="news-item-title">丁薛祥将访问新加坡并主持中新双边合作机制会议 外交部介绍有关情况</span>
          <span class="news-value-point">💡 中新网北京11月20日电 (记者 曾玥)中国外交部发言人20日宣布：应新加坡副总理颜金勇邀请，中共中央政治局常委、国务院副总理丁薛祥将于11月2…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-20/10735268.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社深圳11月20日电 11月20日中午，中国国家主席习近平在深圳会见来华出席亚太经合组织领导人非正式会议的马来西亚总理安瓦尔。" data-title="（深圳APEC）习近平会见马来西亚总理安瓦尔" data-date="11-20 16:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 16:20</span>
          <span class="news-item-title">（深圳APEC）习近平会见马来西亚总理安瓦尔</span>
          <span class="news-value-point">💡 中新社深圳11月20日电 11月20日中午，中国国家主席习近平在深圳会见来华出席亚太经合组织领导人非正式会议的马来西亚总理安瓦尔</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-20/10735154.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社深圳11月20日电 (记者 张焕迪 王宗汉 迟瀚宇 李京泽)亚太经合组织(APEC)吸引人的“魔力”是什么？" data-title="（深圳APEC）与会多国人士眼中的深圳APEC" data-date="11-20 13:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 13:07</span>
          <span class="news-item-title">（深圳APEC）与会多国人士眼中的深圳APEC</span>
          <span class="news-value-point">💡 中新社深圳11月20日电 (记者 张焕迪 王宗汉 迟瀚宇 李京泽)亚太经合组织(APEC)吸引人的“魔力”是什么</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/20/world/europe/putin-trump-xi-summit-apec.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="站在美国和中国领导人身旁，弗拉基米尔·V·普京总统在其长期致力于恢复俄罗斯全球大国地位的努力中取得了象征性的胜利。" data-title="A Summit Gives Putin the Win He Craves: Equal Stature With Superpowers" data-date="11-20 13:01" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-20 13:01</span>
          <span class="news-item-title">峰会为普京带来了他梦寐以求的胜利：与超级大国平起平坐</span>
          <span class="news-item-title-en">A Summit Gives Putin the Win He Craves: Equal Stature With Superpowers</span>
          <span class="news-value-point">💡 站在美国和中国领导人身旁，弗拉基米尔·V·普京总统在其长期致力于恢复俄罗斯全球大国地位的努力中取得了象征性的胜利</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-20/10735143.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月20日电 11月19日，美国总统特朗普结束深圳行，启程离开中国。特朗普在返美途中发文称，“这是一次非常精彩且影响深远的访问。”白宫援引特朗普的这条帖文时同样表示，此行意义深远。" data-title="结束中国之行后，特朗普和白宫接连发文：非常精彩、影响深远" data-date="11-20 12:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 12:05</span>
          <span class="news-item-title">结束中国之行后，特朗普和白宫接连发文：非常精彩、影响深远</span>
          <span class="news-value-point">💡 中新网11月20日电 11月19日，美国总统特朗普结束深圳行，启程离开中国</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/19/us/politics/white-house-cyber-director-departs.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在过去一周，一系列技术故障影响了美国公司和联邦机构，随后Sean Cairncross离职。" data-title="Top White House Cybersecurity Official Is Replaced" data-date="11-20 11:31" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-20 11:31</span>
          <span class="news-item-title">白宫网络安全事务最高官员被撤换</span>
          <span class="news-item-title-en">Top White House Cybersecurity Official Is Replaced</span>
          <span class="news-value-point">💡 在过去一周，一系列技术故障影响了美国公司和联邦机构，随后Sean Cairncross离职</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-20/10735044.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网曼谷11月20日电 (李映民 梁峻祥 王茜)“中泰相约 山海共鸣”中泰媒体合作交流对话会暨海南广播电视总台与泰国广播电视专业协会联合会合作协议签署仪式19日在曼谷举行。" data-title="中泰媒体合作交流活动在曼谷举行" data-date="11-20 10:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 10:32</span>
          <span class="news-item-title">中泰媒体合作交流活动在曼谷举行</span>
          <span class="news-value-point">💡 中新网曼谷11月20日电 (李映民 梁峻祥 王茜)“中泰相约 山海共鸣”中泰媒体合作交流对话会暨海南广播电视总台与泰国广播电视专业协会联合会合作…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-20/10735012.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社圣保罗11月19日电 巴西农业部19日发布数据显示，2026年巴西农牧业总产值预计达1.46万亿雷亚尔，较上年创下的历史纪录下降2.6%。尽管受不利气候条件影响，农牧业产值有所回落，但巴西农产品出口继续保持增长势头。" data-title="巴西2026年农牧业总产值预计达1.46万亿雷亚尔" data-date="11-20 10:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 10:30</span>
          <span class="news-item-title">巴西2026年农牧业总产值预计达1.46万亿雷亚尔</span>
          <span class="news-value-point">💡 中新社圣保罗11月19日电 巴西农业部19日发布数据显示，2026年巴西农牧业总产值预计达1.46万亿雷亚尔，较上年创下的历史纪录下降2.6%</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-20/10735056.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月20日电 据日本《东京新闻》报道，当地时间19日，上万名日本民众在东京日本国会议事堂举行集会，抗议高市政府谋求修改“无核三原则”等一系列政策和动向。" data-title="上万日本民众举行抗议集会 反对高市政府扩军修宪" data-date="11-20 09:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 09:39</span>
          <span class="news-item-title">上万日本民众举行抗议集会 反对高市政府扩军修宪</span>
          <span class="news-value-point">💡 中新网11月20日电 据日本《东京新闻》报道，当地时间19日，上万名日本民众在东京日本国会议事堂举行集会，抗议高市政府谋求修改“无核三原则”等一…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-20/10735023.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="昔日宿敌签下军事协议，美防长称委内瑞拉已变“顺从伙伴”，马杜罗狱中荐书 | 国际早察" data-title="昔日宿敌签下军事协议，美防长称委内瑞拉已变“顺从伙伴”，马杜罗狱中荐书" data-date="11-20 08:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 08:53</span>
          <span class="news-item-title">昔日宿敌签下军事协议，美防长称委内瑞拉已变“顺从伙伴”，马杜罗狱中荐书</span>
          <span class="news-value-point">💡 昔日宿敌签下军事协议，美防长称委内瑞拉已变“顺从伙伴”，马杜罗狱中荐书 | 国际早察</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/19/world/europe/myanmar-genocide-icj-decision-.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在一项可能产生深远影响的裁决中，国际法院首次裁定一个国家犯有种族灭绝罪。" data-title="Myanmar Committed Genocide Against the Rohingya, Top Global Court Finds" data-date="11-20 02:27" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-20 02:27</span>
          <span class="news-item-title">全球最高法院裁定缅甸对罗兴亚人实施种族灭绝</span>
          <span class="news-item-title-en">Myanmar Committed Genocide Against the Rohingya, Top Global Court Finds</span>
          <span class="news-value-point">💡 在一项可能产生深远影响的裁决中，国际法院首次裁定一个国家犯有种族灭绝罪</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/030/131.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 20 日消息，AMD 当地时间 19 日宣布，其锐龙 AI 处理器上的 &quot;XDNA 2&quot; NPU 成为首款获得 Unsloth Desktop 本地界面支持的神经网络处理器。具体来看，兼容的应用程序向 Unsloth Desktop API 发送模型请求，而 Lemonade 和 FastFlowLM 则在 AMD XDNA 2 NPU 上处理模型服务和推理。模型的响应返回给应用程序，供其工作流程使用。这意味着 OpenClaw、Hermes 等超百款智能体可通过 Unsloth Desktop 在锐龙 AI 处理器的 NPU 上本地运行，从 CPU 和 GPU 上卸载相关 AI 工作负载，留出更多算力以供其它任务使用，也有助于延长带电池设备的续航。" data-title="AMD XDNA2 NPU 率先获得 Unsloth Desktop 适配，支持超百款智能体" data-date="11-20 17:13" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-20 17:13</span>
          <span class="news-item-title">AMD XDNA2 NPU 率先获得 Unsloth Desktop 适配，支持超百款智能体</span>
          <span class="news-value-point">💡 IT之家 11 月 20 日消息，AMD 当地时间 19 日宣布，其锐龙 AI 处理器上的 "XDNA 2" NPU 成为首款获得 Unslot…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/130.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 20 日消息，当地时间 11 月 19 日，美光位于新加坡的高带宽内存（HBM）先进封装厂举行了首台设备搬入仪式，庆祝第一台制造设备搬入厂内无尘室。美光科技全球封装与测试高级副总裁陈国兴表示，该 HBM 先进封装厂的建设进展顺利，预计将于 2027 年初实现首批产出。2025 年 1 月，美光新加坡 HBM 先进封装厂破土动工，总投资金额约 70 亿美元（IT之家注：现汇率约合 468.44 亿元人民币），相关投资将持续至 2030 年后。2026 年 1 月，美光先进晶圆制造厂破土动工，官方称该工厂将成为其 NAND 卓越中心（NAND Center of Excellence）不可或缺的一部分，预计将于 2028 年下半年实现晶圆产出。据介绍，该 HBM 先进封装厂初" data-title="美光新加坡 HBM 先进封装厂首台设备进驻，预计 2027 年初首批产出" data-date="11-20 17:13" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-20 17:13</span>
          <span class="news-item-title">美光新加坡 HBM 先进封装厂首台设备进驻，预计 2027 年初首批产出</span>
          <span class="news-value-point">💡 IT之家 11 月 20 日消息，当地时间 11 月 19 日，美光位于新加坡的高带宽内存（HBM）先进封装厂举行了首台设备搬入仪式，庆祝第一台…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/127.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 20 日消息，据《商业内幕》报道，今年 9 月，Anthropic 前研究员雅各布 · 考克森因担忧 AI 发展而离职，并在美国引发了对 AI 技术的广泛恐慌。时间来到当地时间 19 日，随着 Anthropic 股票首次上市交易，考克森再次呼吁公众关注 AI 安全问题。这次，他在接受采访时强调：“他们买不买股票根本不重要。我们必须阻止递归自我改进。”IT之家注：“递归自我改进”指让先进 AI 系统参与训练下一代 AI，从而推动 AI 能力不断提升。当天，考克森与数十名抗议者聚集在 Anthropic 旧金山总部外，要求禁止有关技术。抗议者举着标语、高喊口号，现场还有考克森、OpenAI 前研究员丹尼尔 · 科科塔伊洛和 YouTube 博主罗布 · 迈尔斯发表演讲，随后" data-title="Anthropic 上市当天，离职研究员考克森在其总部外呼吁禁止 AI 递归自我改进" data-date="11-20 17:06" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-20 17:06</span>
          <span class="news-item-title">Anthropic 上市当天，离职研究员考克森在其总部外呼吁禁止 AI 递归自我改进</span>
          <span class="news-value-point">💡 IT之家 11 月 20 日消息，据《商业内幕》报道，今年 9 月，Anthropic 前研究员雅各布 · 考克森因担忧 AI 发展而离职，并在…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/123.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 20 日消息，由捷克个人开发者 Vojtěch Peták 开发的经营模拟游戏《KeyCapy》近日发布了预告。在该作中，玩家将扮演一家小型客制化工作室的经营者，为水豚客户组装、维修键盘或设计独家创意键盘，每一个选择都会改变键盘成品的声音效果。▲ 键帽方案▲ 轴体安装本作计划发行日期即将宣布，最低配置需求如下：操作系统: Windows 10 64-bit处理器: Intel Core i5-4460 or AMD FX-8350 or equivalent内存: 8 GB RAM显卡: NVIDIA GeForce GTX 1050 Ti / AMD Radeon RX 560DirectX 版本: 12存储空间: 需要 5 GB 可用空间参考https://store" data-title="为水豚客户组装键盘：游戏《KeyCapy》发布预告" data-date="11-20 16:54" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-20 16:54</span>
          <span class="news-item-title">为水豚客户组装键盘：游戏《KeyCapy》发布预告</span>
          <span class="news-value-point">💡 IT之家 11 月 20 日消息，由捷克个人开发者 Vojtěch Peták 开发的经营模拟游戏《KeyCapy》近日发布了预告</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-20/10735273.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网哈尔滨11月20日电 (记者 田德雨)“2026年作为‘十五五’开局起步关键之年，黑龙江省牢牢把握国家赋予的‘三基地、一屏障、一高地’重大使命任务，锚定数字经济高质量发展主线，推动数据要素赋能人工智能创新发展，加快培育壮大新质生产力。”20日，黑龙江省发展和改革委员会党组成员，省数据局党组书记、局长高炽扬介绍，该省农业数字化转型实现领跑，智能农机、无人农场、黑土地数字化监测全面铺开。" data-title="黑龙江：智能农机、无人农场、黑土地数字化监测全面铺开" data-date="11-20 16:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 16:05</span>
          <span class="news-item-title">黑龙江：智能农机、无人农场、黑土地数字化监测全面铺开</span>
          <span class="news-value-point">💡 中新网哈尔滨11月20日电 (记者 田德雨)“2026年作为‘十五五’开局起步关键之年，黑龙江省牢牢把握国家赋予的‘三基地、一屏障、一高地’重大…</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/511610.html" target="_blank" rel="noopener" data-cat="keji" data-summary="国产算力的成熟，把具身竞争维度从“芯片有多强”，拉入了一个比拼训练效率、数据规模、部署成本和场景落地速度的多维战场。" data-title="升腾算力训出了双榜SOTA的具身世界模型，华为云这次想把整套底座开放出来" data-date="11-20 16:04" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-20 16:04</span>
          <span class="news-item-title">升腾算力训出了双榜SOTA的具身世界模型，华为云这次想把整套底座开放出来</span>
          <span class="news-value-point">💡 国产算力的成熟，把具身竞争维度从“芯片有多强”，拉入了一个比拼训练效率、数据规模、部署成本和场景落地速度的多维战场</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cw7v2zlle4v4o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="备受瞩目的Anthropic上市案，预料将让其晋身美国十大最具价值企业之列，但AI产业前景依然存在变数。" data-title="Anthropic 破纪录IPO能否阻止AI泡沫破裂？" data-date="11-20 15:52" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-20 15:52</span>
          <span class="news-item-title">Anthropic 破纪录IPO能否阻止AI泡沫破裂？</span>
          <span class="news-value-point">💡 备受瞩目的Anthropic上市案，预料将让其晋身美国十大最具价值企业之列，但AI产业前景依然存在变数</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/511582.html" target="_blank" rel="noopener" data-cat="keji" data-summary="已开源Agnes Harness" data-title="双系统决策+双层自进化，Agnes让Agent效率最高提速14倍，成本骤降至1/27！" data-date="11-20 13:24" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-20 13:24</span>
          <span class="news-item-title">双系统决策+双层自进化，Agnes让Agent效率最高提速14倍，成本骤降至1/27！</span>
          <span class="news-value-point">💡 已开源Agnes Harness</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/19/world/asia/trump-xi-putin.html" target="_blank" rel="noopener" data-cat="keji" data-summary="特朗普总统称俄罗斯领导人是他的“朋友”，并对中国在他首次三方峰会上的热情接待感到惊叹。但在核控制、乌克兰战争或人工智能方面都没有取得突破。" data-title="Trump Flaunts Camaraderie With Xi and Putin but Has Little to Show for It" data-date="11-20 10:10" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-20 10:10</span>
          <span class="news-item-title">特朗普炫耀与习近平和普京的友好关系，但却没有什么实际成果可展示</span>
          <span class="news-item-title-en">Trump Flaunts Camaraderie With Xi and Putin but Has Little to Show for It</span>
          <span class="news-value-point">💡 特朗普总统称俄罗斯领导人是他的“朋友”，并对中国在他首次三方峰会上的热情接待感到惊叹</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/511426.html" target="_blank" rel="noopener" data-cat="keji" data-summary="一批卡可以轮流服务多家公司，一次适配也能让更多团队受益。算力不必家家从头买，工程上的坑也不用家家重新踩。" data-title="具身机器人进入真机时代，华为云CloudRobo开始组队发力了" data-date="11-20 09:07" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-20 09:07</span>
          <span class="news-item-title">具身机器人进入真机时代，华为云CloudRobo开始组队发力了</span>
          <span class="news-value-point">💡 一批卡可以轮流服务多家公司，一次适配也能让更多团队受益</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/get-an-rtx-5070-for-just-usd839-99-a-rare-savings-in-the-gpu-wasteland-msi-geforce-rtx-5070-ventus-2x-oc-12-gb-is-currently-on-sale-at-newegg" target="_blank" rel="noopener" data-cat="keji" data-summary="仅需 839.99 美元即可购得 RTX 5070——MSI GeForce RTX 5070 Ventus 2X OC 12 GB 目前正在 Newegg 促销" data-title="Get an RTX 5070 for just $839.99, a rare savings in the GPU wasteland" data-date="11-20 08:59" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-20 08:59</span>
          <span class="news-item-title">仅需 839.99 美元即可获得 RTX 5070，在显卡荒漠中难得的优惠</span>
          <span class="news-item-title-en">Get an RTX 5070 for just $839.99, a rare savings in the GPU wasteland</span>
          <span class="news-value-point">💡 仅需 839.99 美元即可购得 RTX 5070——MSI GeForce RTX 5070 Ventus 2X OC 12 GB 目前正在 …</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/19/apple-may-be-developing-its-own-ai-agent-that-runs-your-mac/" target="_blank" rel="noopener" data-cat="keji" data-summary="这家iPhone制造商似乎正在打造能够与Meta Muse、Instinct、Claude和OpenAI Dots等产品竞争的智能体。" data-title="Apple may be developing its own AI agent that runs your Mac" data-date="11-20 08:56" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-20 08:56</span>
          <span class="news-item-title">苹果可能正在开发自己的AI代理来运行您的Mac</span>
          <span class="news-item-title-en">Apple may be developing its own AI agent that runs your Mac</span>
          <span class="news-value-point">💡 这家iPhone制造商似乎正在打造能够与Meta Muse、Instinct、Claude和OpenAI Dots等产品竞争的智能体</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/19/anthropics-7-founders-cashed-out-nearly-2b-in-record-breaking-ipo/" target="_blank" rel="noopener" data-cat="keji" data-summary="按照上调后的83美元/股IPO价格，Anthropic的七位创始人每人赚取了2.8亿美元，而该公司则获得了近1050亿美元。" data-title="Anthropic’s 7 founders cashed out nearly $2B in record" data-date="11-20 08:43" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-20 08:43</span>
          <span class="news-item-title">Anthropic的7位创始人创纪录地套现近20亿美元</span>
          <span class="news-item-title-en">Anthropic’s 7 founders cashed out nearly $2B in record</span>
          <span class="news-value-point">💡 按照上调后的83美元/股IPO价格，Anthropic的七位创始人每人赚取了2.8亿美元，而该公司则获得了近1050亿美元</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/19/technology/anthropic-ipo-employees-payout.html" target="_blank" rel="noopener" data-cat="keji" data-summary="许多几年前加入这家人工智能公司的人可能很少会想到Anthropic会发展得如此壮大。他们现在的身家已达数千万美元，甚至更多。" data-title="Anthropic’s I.P.O. Turns Tech Researchers Into Overnight Millionaires" data-date="11-20 08:25" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-20 08:25</span>
          <span class="news-item-title">Anthropic的IPO一夜之间将科技研究人员变成了百万富翁</span>
          <span class="news-item-title-en">Anthropic’s I.P.O. Turns Tech Researchers Into Overnight Millionaires</span>
          <span class="news-value-point">💡 许多几年前加入这家人工智能公司的人可能很少会想到Anthropic会发展得如此壮大</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/19/technology/anthropic-2-trillion.html" target="_blank" rel="noopener" data-cat="keji" data-summary="这家旧金山公司是第一家在科技行业备受瞩目的时刻上市的主要人工智能实验室，截至当日收盘，其市值达到1.7万亿美元。" data-title="Anthropic Debuts on Wall Street as a $2 Trillion Company" data-date="11-20 06:45" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-20 06:45</span>
          <span class="news-item-title">Anthropic以2万亿美元的市值在华尔街首次亮相</span>
          <span class="news-item-title-en">Anthropic Debuts on Wall Street as a $2 Trillion Company</span>
          <span class="news-value-point">💡 这家旧金山公司是第一家在科技行业备受瞩目的时刻上市的主要人工智能实验室，截至当日收盘，其市值达到1.7万亿美元</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/nov/20/weekend-football-countdown-live-news-updates" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="⚽ 周末即将到来之际的所有最新足球新闻⚽ 赛程 | 排行榜 | 十大看点 | 致函Tom感谢国际足球、足总杯和曼联智囊团，这真有意思。我们很快会再见。现在是时候" data-title="Premier League returns, Pochettino readies for United test and more" data-date="11-20 17:15" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-20 17:15</span>
          <span class="news-item-title">英超联赛回归，波切蒂诺为曼联的考验做好准备，以及更多资讯</span>
          <span class="news-item-title-en">Premier League returns, Pochettino readies for United test and more</span>
          <span class="news-value-point">💡 ⚽ 周末即将到来之际的所有最新足球新闻⚽ 赛程 | 排行榜 | 十大看点 | 致函Tom感谢国际足球、足总杯和曼联智囊团，这真有意思</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13279313/fulham-transfers-latest-news-rumours-and-gossip-live-updates-goals-and-highlights" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Fulham latest: Leno open to new challenge amid Bayern links" data-title="Fulham latest: Leno open to new challenge amid Bayern links" data-date="11-20 16:40" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-20 16:40</span>
          <span class="news-item-title">富勒姆最新消息：莱诺在与拜仁传出绯闻之际表示愿意接受新挑战</span>
          <span class="news-item-title-en">Fulham latest: Leno open to new challenge amid Bayern links</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/20/premier-league-table-history-after-10-games-season" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="过去几年的情况表明，开局缓慢的球队很难大幅提升排名，但目前排名靠前的球队中也会有球队降级。英超联赛即将进入本赛季最激烈的阶段。在过去三个月里进行了 10 轮比赛之后，" data-title="What history tells us about the Premier League table after 10 games of a season" data-date="11-20 16:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-20 16:00</span>
          <span class="news-item-title">从历史看英超联赛赛季10轮后的积分榜</span>
          <span class="news-item-title-en">What history tells us about the Premier League table after 10 games of a season</span>
          <span class="news-value-point">💡 过去几年的情况表明，开局缓慢的球队很难大幅提升排名，但目前排名靠前的球队中也会有球队降级</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13614140/how-the-story-of-dylan-tombides-is-helping-educate-fifa-u17-world-cup-players-about-testicular-cancer" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="十五年前，西汉姆联队前锋迪伦·汤比德斯在U17世界杯上发现自己患有睾丸癌。如今，他的母亲和弟弟重返赛场，为新一代球员发表鼓舞人心、充满情感的讲话，以提高人们对睾丸癌的认识。" data-title="How West Ham striker&#39;s testicular cancer tragedy is educating next generation" data-date="11-20 16:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-20 16:00</span>
          <span class="news-item-title">西汉姆联队前锋的睾丸癌悲剧如何教育下一代</span>
          <span class="news-item-title-en">How West Ham striker's testicular cancer tragedy is educating next generation</span>
          <span class="news-value-point">💡 十五年前，西汉姆联队前锋迪伦·汤比德斯在U17世界杯上发现自己患有睾丸癌</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/20/premier-league-10-things-to-look-out-for-this-weekend" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="布鲁诺·吉马良斯将在泰恩赛德感受热烈气氛，亚历克斯·斯科特的回归让樱桃军团更加欢欣鼓舞，曼城将面对最喜欢的“出气筒”。在英超联赛中遭遇三连败后，曼城需要一些东西或某个人来帮助他们" data-title="Premier League: 10 things to look out for this weekend" data-date="11-20 08:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-20 08:00</span>
          <span class="news-item-title">英超联赛：本周末需要注意的10件事</span>
          <span class="news-item-title-en">Premier League: 10 things to look out for this weekend</span>
          <span class="news-value-point">💡 布鲁诺·吉马良斯将在泰恩赛德感受热烈气氛，亚历克斯·斯科特的回归让樱桃军团更加欢欣鼓舞，曼城将面对最喜欢的“出气筒”</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025492/man-utd-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Man Utd latest: Drone footage &#39;a significant tactical advantage to Liverpool&#39;" data-title="Man Utd latest: Drone footage &#39;a significant tactical advantage to Liverpool&#39;" data-date="11-20 05:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-20 05:00</span>
          <span class="news-item-title">曼联最新消息：无人机拍摄的画面“对利物浦来说是一个重大的战术优势”</span>
          <span class="news-item-title-en">Man Utd latest: Drone footage 'a significant tactical advantage to Liverpool'</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13614159/manchester-united-drone-footage-of-mauricio-pochettinos-first-training-session-leaked-online" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="毛里西奥·波切蒂诺（Mauricio Pochettino）今天在曼联的首堂训练课因重大安保漏洞而被泄露到网上。" data-title="Drone footage of Pochettino&#39;s first Man Utd training session leaked online" data-date="11-20 04:28" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-20 04:28</span>
          <span class="news-item-title">波切蒂诺执教曼联的首堂训练课无人机拍摄的画面在网上泄露</span>
          <span class="news-item-title-en">Drone footage of Pochettino's first Man Utd training session leaked online</span>
          <span class="news-value-point">💡 毛里西奥·波切蒂诺（Mauricio Pochettino）今天在曼联的首堂训练课因重大安保漏洞而被泄露到网上</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cje3900n0vvro?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="托马斯·弗兰克在以水晶宫主帅身份首次出席新闻发布会后表示，很高兴“重回江湖”。" data-title="Frank happy to be &#39;back in the circus&#39; at Palace" data-date="11-20 04:16" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-20 04:16</span>
          <span class="news-item-title">弗兰克很高兴“重返帕拉蒂的舞台”</span>
          <span class="news-item-title-en">Frank happy to be 'back in the circus' at Palace</span>
          <span class="news-value-point">💡 托马斯·弗兰克在以水晶宫主帅身份首次出席新闻发布会后表示，很高兴“重回江湖”</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/arsenal-women-vs-olympiques-lyon-women/live/578272" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="WCL: Dominant Lyon take the lead at Arsenal through Brand LIVE!" data-title="WCL: Dominant Lyon take the lead at Arsenal through Brand LIVE!" data-date="11-20 03:03" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-20 03:03</span>
          <span class="news-item-title">WCL：里昂占据主导，通过布兰德的进球在阿森纳取得领先！</span>
          <span class="news-item-title-en">WCL: Dominant Lyon take the lead at Arsenal through Brand LIVE!</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c50mdnxy3ry0o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="BBC体育足球专家克里斯·萨顿（Chris Sutton）将与世界冠军拳击手劳伦·普莱斯（Lauren Price）、BBC读者以及人工智能一较高下，预测本周末英超联赛的赛果。" data-title="Sutton&#39;s predictions v world champion boxer Lauren Price" data-date="11-20 02:52" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-20 02:52</span>
          <span class="news-item-title">萨顿的预测与世界冠军拳手劳伦·普莱斯</span>
          <span class="news-item-title-en">Sutton's predictions v world champion boxer Lauren Price</span>
          <span class="news-value-point">💡 BBC体育足球专家克里斯·萨顿（Chris Sutton）将与世界冠军拳击手劳伦·普莱斯（Lauren Price）、BBC读者以及人工智能一较…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13611640/premier-league-predictions-jones-knows-best-bets-newcastle-vs-arsenal-liverpool-vs-manchester-united-and-much-more" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="随着英超联赛在国际比赛日后回归，我们的顶级投注专家Lewis Jones（又名Jones Knows）将提供他的分析和投注见解。" data-title="PL Predictions: How will your club fare this weekend?" data-date="11-20 02:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-20 02:00</span>
          <span class="news-item-title">英超预测：您的俱乐部本周末表现如何？</span>
          <span class="news-item-title-en">PL Predictions: How will your club fare this weekend?</span>
          <span class="news-value-point">💡 随着英超联赛在国际比赛日后回归，我们的顶级投注专家Lewis Jones（又名Jones Knows）将提供他的分析和投注见解</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13611640/premier-league-predictions-jones-knows-best-bets-newcastle-vs-arsenal-liverpool-vs-manchester-united-and-much-more" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="随着英超联赛在国际比赛日后回归，我们的顶级投注专家Lewis Jones（又名Jones Knows）将提供他的分析和投注见解。" data-title="PL Predictions: How will your club fare this weekend?" data-date="11-20 02:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-20 02:00</span>
          <span class="news-item-title">英超预测：您的俱乐部本周末表现如何？</span>
          <span class="news-item-title-en">PL Predictions: How will your club fare this weekend?</span>
          <span class="news-value-point">💡 随着英超联赛在国际比赛日后回归，我们的顶级投注专家Lewis Jones（又名Jones Knows）将提供他的分析和投注见解</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/12040/13279295/brighton-transfers-latest-news-rumours-and-gossip-live-updates-goals-and-highlights" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Brighton latest: Hurzeler not leaving for a long time, says Bloom" data-title="Brighton latest: Hurzeler not leaving for a long time, says Bloom" data-date="11-20 01:23" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-20 01:23</span>
          <span class="news-item-title">布莱顿最新消息：布卢姆表示，许策尔不会在很长一段时间内离开</span>
          <span class="news-item-title-en">Brighton latest: Hurzeler not leaving for a long time, says Bloom</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/12040/13025489/tottenham-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Spurs latest: &#39;You only know a tenth of the truth,&#39; says Frank" data-title="Spurs latest: &#39;You only know a tenth of the truth,&#39; says Frank" data-date="11-20 01:20" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-20 01:20</span>
          <span class="news-item-title">热刺最新消息：弗兰克表示：“你只知道十分之一的真相。”</span>
          <span class="news-item-title-en">Spurs latest: 'You only know a tenth of the truth,' says Frank</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/19/premier-league-vote-new-rules-financial-indemnity-lawsuits" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="个人赔偿责任范围扩大至潜在诉讼 关键人物可能被列入针对曼城俱乐部的诉讼 在周四的一次关键投票中，各俱乐部团结在英超联赛领导层周围，以压倒性多数支持旨在保护英超联赛首席执行官的新规则。" data-title="Premier League clubs vote through new rules to increase legal protection for board" data-date="11-20 00:03" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-20 00:03</span>
          <span class="news-item-title">英超俱乐部投票通过新规，加强对董事会的法律保护</span>
          <span class="news-item-title-en">Premier League clubs vote through new rules to increase legal protection for board</span>
          <span class="news-value-point">💡 个人赔偿责任范围扩大至潜在诉讼
关键人物可能被列入针对曼城俱乐部的诉讼
在周四的一次关键投票中，各俱乐部团结在英超联赛领导层周围，以压倒性多数支…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-20/10735330.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网南昌11月20日电 陕西富平县日前于江西南昌举办两场文旅推介活动，依托活动搭建黄河文化与长江文化交流平台，拓展省外旅游客源市场。" data-title="富平赴南昌开展两场文旅推介 推进赣陕文旅协作" data-date="11-20 17:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 17:10</span>
          <span class="news-item-title">富平赴南昌开展两场文旅推介 推进赣陕文旅协作</span>
          <span class="news-value-point">💡 中新网南昌11月20日电 陕西富平县日前于江西南昌举办两场文旅推介活动，依托活动搭建黄河文化与长江文化交流平台，拓展省外旅游客源市场</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-20/10735328.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网济南11月20日电 (刘驰原)立冬过后，寒意渐浓。山东各地开展供热保障工作，从管网体检、系统调试、智慧调度等方面发力，全力保障民众温暖过冬。" data-title="山东各地开展供热保障工作 守护民众冬日暖意" data-date="11-20 17:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 17:10</span>
          <span class="news-item-title">山东各地开展供热保障工作 守护民众冬日暖意</span>
          <span class="news-value-point">💡 中新网济南11月20日电 (刘驰原)立冬过后，寒意渐浓</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/124.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 20 日消息，小米“可穿戴产品小助理”官方微博今日宣布，Xiaomi Watch S5 46mm、Xiaomi Watch 5 澎湃 OS4 新版本开启先锋内测。据介绍，本次各产品邀请 100 位内测用户，需签署保密协议；计划 11 月 23 日公布名单，将通过短信 / 私信发送飞书链接，选中的朋友进群签约即可体验。官方暂未公布新版本任何信息，IT之家附报名链接：https://m.beehive.miui.com/2wK_Koq9KBYlFpWDyURp1Q/desktop/home" data-title="小米 Watch S5 46mm、Watch 5 手表开启澎湃 OS4 新版本先锋内测，需签署保密协议" data-date="11-20 16:57" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-20 16:57</span>
          <span class="news-item-title">小米 Watch S5 46mm、Watch 5 手表开启澎湃 OS4 新版本先锋内测，需签署保密协议</span>
          <span class="news-value-point">💡 IT之家 11 月 20 日消息，小米“可穿戴产品小助理”官方微博今日宣布，Xiaomi Watch S5 46mm、Xiaomi Watch …</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c5n4eylmmg8po/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="BBC国际编辑写道，律师将研究冈比亚如何证明缅甸意图实施种族灭绝。" data-title="缅甸种族灭绝裁决影响深远的历史意义" data-date="11-20 16:53" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-20 16:53</span>
          <span class="news-item-title">缅甸种族灭绝裁决影响深远的历史意义</span>
          <span class="news-value-point">💡 BBC国际编辑写道，律师将研究冈比亚如何证明缅甸意图实施种族灭绝</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/121.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 20 日消息，据汽车之家消息，奇瑞捷途环游者 EV 将于 11 月 24 日上市。据IT之家此前报道，11 月 16 日，奇瑞捷途环游者 EV 开启预售，定位紧凑型纯电 SUV，并搭载猎鹰 500 辅助驾驶，预售价 9.99-14.59 万元：550km 后驱畅行版：预售价 9.99 万元550km 后驱智行版：预售价 10.99 万元550km 后驱智臻版：预售价 12.49 万元550km 后驱智臻版 +：预售价 12.69 万元510km XWD 四驱智臻版：预售价 14.59 万元新车风阻系数 0.32，尺寸为 4605×1880×1700mm、轴距 2735mm；搭载猎鹰 500 智能辅助驾驶系统，支持高速 NOA、城市 NOA 以及全场景智能泊车等功能。新车采" data-title="奇瑞捷途环游者 EV 将于 11 月 24 日上市，预售 9.99 万元起" data-date="11-20 16:45" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-20 16:45</span>
          <span class="news-item-title">奇瑞捷途环游者 EV 将于 11 月 24 日上市，预售 9.99 万元起</span>
          <span class="news-value-point">💡 IT之家 11 月 20 日消息，据汽车之家消息，奇瑞捷途环游者 EV 将于 11 月 24 日上市</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/rugby-union/news/12040/13614260/rassie-erasmus-sky-sports-understands-south-africa-head-coach-running-the-risk-of-breaching-suspension-with-watchalong" target="_blank" rel="noopener" data-cat="zonghe" data-summary="据天空体育了解，如果南非主教练Rassie Erasmus按计划在网上观看周六的国际锦标赛与爱尔兰的对决，他将冒着违反六场测试赛禁赛规定的风险。" data-title="Erasmus running risk of breaching World Rugby ban with watchalong" data-date="11-20 16:30" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-20 16:30</span>
          <span class="news-item-title">埃拉斯莫斯因观看比赛而面临违反世界橄榄球禁令的风险</span>
          <span class="news-item-title-en">Erasmus running risk of breaching World Rugby ban with watchalong</span>
          <span class="news-value-point">💡 据天空体育了解，如果南非主教练Rassie Erasmus按计划在网上观看周六的国际锦标赛与爱尔兰的对决，他将冒着违反六场测试赛禁赛规定的风险</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-20/10735294.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="一座长安城，半部《全唐诗》。在西安，古典诗词不再只是典籍里的文字，而是散落在城垣街巷、碑石古塔、山水舞台之间，触手可及的城市风景。" data-title="寻访诗词文脉 赴一场长安诗约" data-date="11-20 16:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 16:20</span>
          <span class="news-item-title">寻访诗词文脉 赴一场长安诗约</span>
          <span class="news-value-point">💡 一座长安城，半部《全唐诗》</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-20/10735291.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在今年APEC领导人非正式会议上，包含香云纱元素的国礼惊艳亮相，这份别出心裁的礼物，是如何做到传统又创新？" data-title="“粤”上新台阶丨何以“香云纱”？" data-date="11-20 16:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 16:16</span>
          <span class="news-item-title">“粤”上新台阶丨何以“香云纱”？</span>
          <span class="news-value-point">💡 在今年APEC领导人非正式会议上，包含香云纱元素的国礼惊艳亮相，这份别出心裁的礼物，是如何做到传统又创新</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/cricket/news/12040/13614266/australias-sandpapergate-usman-khawaja-called-traitor-by-former-south-africa-bowler-for-ball-tampering-claims" target="_blank" rel="noopener" data-cat="zonghe" data-summary="前南非投球手法尼·德·维利尔斯（Fanie de Villiers）在澳大利亚前击球手乌斯曼·卡瓦贾（Usman Khawaja）对“砂纸门”事件提出指控后，称其为“他见过的最大的叛徒”。" data-title="Khawaja branded &#39;biggest traitor ever&#39; in Sandpaper fallout" data-date="11-20 16:10" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-20 16:10</span>
          <span class="news-item-title">在“砂纸门”事件中，哈瓦贾被冠以“史上最大叛徒”的称号</span>
          <span class="news-item-title-en">Khawaja branded 'biggest traitor ever' in Sandpaper fallout</span>
          <span class="news-value-point">💡 前南非投球手法尼·德·维利尔斯（Fanie de Villiers）在澳大利亚前击球手乌斯曼·卡瓦贾（Usman Khawaja）对“砂纸门”事…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-20/10735277.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京11月20日电 (记者 陈杭)记者20日从北京市科委、中关村管委会获悉，2025年度北京市科学技术奖正式公布。王中林、王拥军荣获突出贡献中关村奖。59项成果荣获自然科学奖，包括一等奖15项，二等奖44项；26项成果荣获技术发明奖，包括一等奖6项，二等奖20项；109项成果荣获科学技术进步奖，包括一等奖29项，二等奖80项。" data-title="2025年度北京市科学技术奖揭晓 基础研究成果持续涌现" data-date="11-20 16:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 16:07</span>
          <span class="news-item-title">2025年度北京市科学技术奖揭晓 基础研究成果持续涌现</span>
          <span class="news-value-point">💡 中新网北京11月20日电 (记者 陈杭)记者20日从北京市科委、中关村管委会获悉，2025年度北京市科学技术奖正式公布</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-20/10735262.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="今年以来，我国邮政行业寄递量稳步增长，国家邮政局数据显示，前10个月，邮政行业寄递业务量累计完成1830.3亿件，同比增长3.3%。" data-title="中转场更智能、乡村邮路更通畅 邮政寄递量稳步增长" data-date="11-20 15:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 15:35</span>
          <span class="news-item-title">中转场更智能、乡村邮路更通畅 邮政寄递量稳步增长</span>
          <span class="news-value-point">💡 今年以来，我国邮政行业寄递量稳步增长，国家邮政局数据显示，前10个月，邮政行业寄递业务量累计完成1830.3亿件，同比增长3.3%</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13614252/indianapolis-colts-houston-texans-nfl-highlights" target="_blank" rel="noopener" data-cat="zonghe" data-summary="NFL赛季第11周印第安纳波利斯小马队对休斯敦德州人队的精彩集锦。" data-title="Indianapolis Colts @ Houston Texans | NFL highlights" data-date="11-20 15:11" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-20 15:11</span>
          <span class="news-item-title">印第安纳波利斯小马队对休斯敦德州人队 | NFL精彩集锦</span>
          <span class="news-item-title-en">Indianapolis Colts @ Houston Texans | NFL highlights</span>
          <span class="news-value-point">💡 NFL赛季第11周印第安纳波利斯小马队对休斯敦德州人队的精彩集锦</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-20/10735243.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网海口11月20日电 记者从海南省委网信办获悉，“红星照耀中国·从琼崖烽火到开放自贸港”网络主题宣传活动，将于今日启动。来自中央、地方新闻单位的媒体记者以及知名网络大V，将走进海南自贸港，在深入挖掘海南红色文化资源的同时，以多元新闻产品展现自贸港建设的新气象。" data-title="“红星照耀中国·从琼崖烽火到开放自贸港”网络主题宣传活动将于今日启动" data-date="11-20 15:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 15:04</span>
          <span class="news-item-title">“红星照耀中国·从琼崖烽火到开放自贸港”网络主题宣传活动将于今日启动</span>
          <span class="news-value-point">💡 中新网海口11月20日电 记者从海南省委网信办获悉，“红星照耀中国·从琼崖烽火到开放自贸港”网络主题宣传活动，将于今日启动</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/nfl/news/12040/13614247/nfl-cj-stroud-stars-as-houston-texans-finally-win-at-home-this-season-with-26-3-defeat-of-indianapolis-colts" target="_blank" rel="noopener" data-cat="zonghe" data-summary="CJ Stroud 再度有出色表现，帮助休斯敦德州人队在主场终于取得一场胜利，击败了印第安纳波利斯小马队。" data-title="Stroud stars as Texans finally win at home with defeat of Colts" data-date="11-20 14:47" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-20 14:47</span>
          <span class="news-item-title">斯特劳德大放异彩，德州人队终于在主场击败小马队，取得胜利</span>
          <span class="news-item-title-en">Stroud stars as Texans finally win at home with defeat of Colts</span>
          <span class="news-value-point">💡 CJ Stroud 再度有出色表现，帮助休斯敦德州人队在主场终于取得一场胜利，击败了印第安纳波利斯小马队</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/511603.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="11月19日，由微博与新浪新闻联合主办的“新浪新闻·2026探索大会”在北京举办。" data-title="新浪新闻·2026探索大会在京举行 虚实交融共探智能时代共生新图景" data-date="11-20 14:16" data-source="量子位">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-20 14:16</span>
          <span class="news-item-title">新浪新闻·2026探索大会在京举行 虚实交融共探智能时代共生新图景</span>
          <span class="news-value-point">💡 11月19日，由微博与新浪新闻联合主办的“新浪新闻·2026探索大会”在北京举办</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🌍</span>
      <span class="news-category-title">西方媒体视角 (外媒看中国 · 奇葩言论集锦)</span>
      <span class="news-category-count">1 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/11/19/us/politics/trump-summit-power.html" target="_blank" rel="noopener" data-cat="meimei" data-summary="中期选举削弱了特朗普总统的实力，他向来自俄罗斯和中国的独裁者敞开怀抱、拍拍肩膀、面带微笑，这与他对华盛顿势头正盛的民主党人发出的威胁形成鲜明对比。" data-title="At Summit With Xi and Putin, Trump Seeks to Project Power Abroad While Sharing It at Home" data-date="11-20 01:05" data-source="纽约时报">
          <span class="news-cat-tag cat-meimei">🌍 外媒视角</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-20 01:05</span>
          <span class="news-item-title">在与习近平和普京的峰会上，特朗普试图在与国内分享权力的同时，向国外展示权力</span>
          <span class="news-item-title-en">At Summit With Xi and Putin, Trump Seeks to Project Power Abroad While Sharing It at Home</span>
          <span class="news-value-point">💡 中期选举削弱了特朗普总统的实力，他向来自俄罗斯和中国的独裁者敞开怀抱、拍拍肩膀、面带微笑，这与他对华盛顿势头正盛的民主党人发出的威胁形成鲜明对比</span>
        </a>
  </div>
</div>
<script defer src="{{ "/assets/js/news-feed.js" | relative_url }}"></script>


<p class="news-updated">🕐 抓取更新于 2026-11-20 17:18（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
