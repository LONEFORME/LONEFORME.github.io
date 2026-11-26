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
      <span>2026-11-27 01:50 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">4</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×14 · 天空体育×13</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">按来源聚合 · 最近 24 小时精选</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gj/2026/11-26/10738473.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社伦敦11月26日电 (记者 欧阳开宇)当地时间11月26日，伦敦地铁司机正式启动今冬首轮24小时罢工行动。据悉，本次冬季罢工共计八日，分多时段开展，将持续至2027年2月，预计持续扰乱伦敦公共交通秩序，影响数百万通勤民众出行。" data-title="英国伦敦地铁司机开启冬季罢工" data-date="11-26 23:34" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 11-26 23:34</span>
      </div>
      <h2 class="hero-featured-title">英国伦敦地铁司机开启冬季罢工</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.tomshardware.com/tech-industry/credit-rating-agency-puts-nvidia-on-notice-for-possible-downgrade-s-and-p-global-ratings-says-board-members-may-have-compromised-their-independence" target="_blank" rel="noopener" data-cat="keji" data-summary="标普全球评级（S&amp;P Global Ratings）表示，由于英伟达面临各种风险，包括走私指控以及缺乏首席执行官继任计划，该公司可能会下调英伟达的信用评级。" data-title="Credit rating agency puts Nvidia on notice for possible downgrade" data-date="11-27 01:00" data-source="Tom's Hardware">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
      </div>
      <p class="hero-sub-title">信用评级机构对英伟达发出可能下调评级的通知</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/football/live-blog/11661/13025489/tottenham-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Spurs latest: Savio set for several weeks out" data-title="Spurs latest: Savio set for several weeks out" data-date="11-27 01:00" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">热刺最新消息：萨维奥将缺席数周</p>
    </a>
    <a class="hero-sub-card" href="https://www.tomshardware.com/gift-guides-seasonal-sales/essential-3d-printer-maintenance-tool-deals-for-black-friday-save-up-to-30-percent-on-precision-tools-lights-snips-and-more" target="_blank" rel="noopener" data-cat="zonghe" data-summary="为了获得最佳的3D打印效果，始终需要备有一些常用的工具。" data-title="Essential 3D printer maintenance tool deals for Black Friday — save up to 30% on precision tools, lights, snips, and more" data-date="11-27 01:30" data-source="Tom's Hardware">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
      </div>
      <p class="hero-sub-title">黑色星期五必备3D打印机维护工具优惠——精密工具、照明灯、剪钳等最高立省30%</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-26/10738473.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社伦敦11月26日电 (记者 欧阳开宇)当地时间11月26日，伦敦地铁司机正式启动今冬首轮24小时罢工行动。据悉，本次冬季罢工共计八日，分多时段开展，将持续至2027年2月，预计持续扰乱伦敦公共交通秩序，影响数百万通勤民众出行。" data-title="英国伦敦地铁司机开启冬季罢工" data-date="11-26 23:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 23:34</span>
          <span class="news-item-title">英国伦敦地铁司机开启冬季罢工</span>
          <span class="news-value-point">💡 中新社伦敦11月26日电 (记者 欧阳开宇)当地时间11月26日，伦敦地铁司机正式启动今冬首轮24小时罢工行动</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-26/10738472.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社伦敦11月26日电 (记者 欧阳开宇)英国国防部26日宣布，已与本国企业巴布科克签署为期五年、总额80亿英镑的合作协议，用于升级英国海军核潜艇的维护保障体系，提升核潜艇战备水平。" data-title="英国斥资80亿英镑提升核潜艇战备水平" data-date="11-26 23:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 23:32</span>
          <span class="news-item-title">英国斥资80亿英镑提升核潜艇战备水平</span>
          <span class="news-value-point">💡 中新社伦敦11月26日电 (记者 欧阳开宇)英国国防部26日宣布，已与本国企业巴布科克签署为期五年、总额80亿英镑的合作协议，用于升级英国海军核…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-26/10738469.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="科威特军方发言人26日证实，两名意大利公民在当天伊朗无人机袭击科威特事件中受伤，后不治身亡。" data-title="两名意大利公民在伊朗无人机袭击科威特事件中身亡" data-date="11-26 22:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 22:49</span>
          <span class="news-item-title">两名意大利公民在伊朗无人机袭击科威特事件中身亡</span>
          <span class="news-value-point">💡 科威特军方发言人26日证实，两名意大利公民在当天伊朗无人机袭击科威特事件中受伤，后不治身亡</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-26/10738455.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网兰州11月26日电 (记者 丁思)26日，由甘肃省台办主办、兰州石化职业技术大学承办的纪念孙中山先生诞辰160周年陇台交流活动在兰州举行。" data-title="纪念孙中山诞辰160周年陇台交流活动在兰州举行" data-date="11-26 21:58" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 21:58</span>
          <span class="news-item-title">纪念孙中山诞辰160周年陇台交流活动在兰州举行</span>
          <span class="news-value-point">💡 中新网兰州11月26日电 (记者 丁思)26日，由甘肃省台办主办、兰州石化职业技术大学承办的纪念孙中山先生诞辰160周年陇台交流活动在兰州举行</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cwz0kymdzdd8o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="这是台北市自1994年恢复市长直选以来，首次有民进党参选人不举办选前之夜。有政治学者向BBC中文分析，沈伯洋取消活动可为交通争议“止血”，但同时窒碍了绿营凝聚声势。" data-title="九合一选前反转：沈伯洋破天荒取消台北“选前之夜”，如何影响选情？" data-date="11-26 21:41" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-26 21:41</span>
          <span class="news-item-title">九合一选前反转：沈伯洋破天荒取消台北“选前之夜”，如何影响选情？</span>
          <span class="news-value-point">💡 这是台北市自1994年恢复市长直选以来，首次有民进党参选人不举办选前之夜</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-26/10738424.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月26日电 据中国国防部网站消息，11月26日，中俄两军以视频会议方式举行战略磋商。双方围绕落实两国元首共识、推动两军关系持续深化拓展进行交流，就国际和地区形势深入交换意见，表示两军将进一步加强沟通协作，共同维护国际和地区安全稳定。(完)" data-title="中俄两军举行战略磋商" data-date="11-26 21:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 21:29</span>
          <span class="news-item-title">中俄两军举行战略磋商</span>
          <span class="news-value-point">💡 中新社北京11月26日电 据中国国防部网站消息，11月26日，中俄两军以视频会议方式举行战略磋商</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-26/10738436.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社乌鲁木齐11月26日电 (记者 苟继鹏)“如果一座城市只有3.7%的土地可以住人，沙漠和戈壁占了大部分，每年有几十天黄沙蔽日，该如何发展？”" data-title="中外代表新疆共话“绿色城市”发展之道" data-date="11-26 21:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 21:29</span>
          <span class="news-item-title">中外代表新疆共话“绿色城市”发展之道</span>
          <span class="news-value-point">💡 中新社乌鲁木齐11月26日电 (记者 苟继鹏)“如果一座城市只有3.7%的土地可以住人，沙漠和戈壁占了大部分，每年有几十天黄沙蔽日，该如何发展</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-26/10738437.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网昆明11月26日电 (记者 陈静 缪超)“‘幸福云南’应该是什么样的？就像报告里说的，各民族像石榴籽一样紧紧抱在一起，要像花儿一样绚烂。”26日，在中国共产党云南省第十二次代表大会现场，临沧市沧源县勐董镇龙乃村党总支书记赵爱军听完报告后，向记者描绘他心中的画面。" data-title="幸福云南什么样？“像花儿一样绚烂，像石榴籽一样抱团！”" data-date="11-26 21:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 21:24</span>
          <span class="news-item-title">幸福云南什么样？“像花儿一样绚烂，像石榴籽一样抱团！”</span>
          <span class="news-value-point">💡 中新网昆明11月26日电 (记者 陈静 缪超)“‘幸福云南’应该是什么样的</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-26/10738380.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="编者按：对口支援新疆是党中央、国务院为促进新疆发展、增进民族团结、维护新疆稳定作出的一项重大决策部署。1997年以来，中央单位和援疆省市先后选派12批次3万多名干部人才进疆工作。2026年，新一批援疆干部人才集中选派轮换工作已全面完成，对口援疆“朋友圈”迎来扩容。值此之际，《中国新闻》报策划推出《“援”定天山——对口援疆工作巡礼》系列报道，呈现对口援疆省市共建现代化新疆的生动实践。" data-title="“援”定天山：从一串葡萄到600个“甜果”的湘疆协作故事" data-date="11-26 21:19" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 21:19</span>
          <span class="news-item-title">“援”定天山：从一串葡萄到600个“甜果”的湘疆协作故事</span>
          <span class="news-value-point">💡 编者按：对口支援新疆是党中央、国务院为促进新疆发展、增进民族团结、维护新疆稳定作出的一项重大决策部署</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-26/10738377.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="石化园区里，光谱仪器向远处发射激光再反射接收，以往测不到的微量废气，如今成分、来源一目了然。以前，这类排查只能靠嗅辨员用鼻子一点点“闻”。" data-title="点“石”成新 老家底孕育新动能" data-date="11-26 21:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 21:01</span>
          <span class="news-item-title">点“石”成新 老家底孕育新动能</span>
          <span class="news-value-point">💡 石化园区里，光谱仪器向远处发射激光再反射接收，以往测不到的微量废气，如今成分、来源一目了然</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-26/10738390.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="“大鹏一日同风起，扶摇直上九万里。”世界的目光投向中国、聚焦深圳。亚太经合组织第三十三次领导人非正式会议及相关活动取得丰硕成果。以开放纾发展之困，以创新聚增长之势，以合作谋共享之福，亚太共同体建设前景光明，我们期待，亚太合作像大鹏一样展翅高飞、鹏程万里。" data-title="创意微视频｜鹏程万里" data-date="11-26 20:51" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 20:51</span>
          <span class="news-item-title">创意微视频｜鹏程万里</span>
          <span class="news-value-point">💡 “大鹏一日同风起，扶摇直上九万里</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-26/10738379.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社伦敦11月26日电 (记者 欧阳开宇)英国国家统计局26日发布数据显示，截至2026年6月底的过去一年，英国净移民人数由上年同期20.4万人降至7.7万人。该数据剔除新冠疫情管控时期特殊波动后，创下近三十年来最低纪录。" data-title="英国净移民人数降至近三十年低位" data-date="11-26 20:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 20:42</span>
          <span class="news-item-title">英国净移民人数降至近三十年低位</span>
          <span class="news-value-point">💡 中新社伦敦11月26日电 (记者 欧阳开宇)英国国家统计局26日发布数据显示，截至2026年6月底的过去一年，英国净移民人数由上年同期20.4万…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-26/10738312.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社阿斯塔纳11月26日电 (记者 单璐)哈萨克斯坦阿拉木图市一处民宅26日凌晨起火，造成5人遇难，其中包括1名未成年人。" data-title="哈萨克斯坦阿拉木图一民宅起火致5人遇难" data-date="11-26 20:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 20:00</span>
          <span class="news-item-title">哈萨克斯坦阿拉木图一民宅起火致5人遇难</span>
          <span class="news-value-point">💡 中新社阿斯塔纳11月26日电 (记者 单璐)哈萨克斯坦阿拉木图市一处民宅26日凌晨起火，造成5人遇难，其中包括1名未成年人</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-26/10738322.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间11月26日，塞尔维亚国民议会议长丘皮奇宣布将于12月27日举行总统选举。" data-title="塞尔维亚总统选举将于12月27日举行" data-date="11-26 19:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 19:23</span>
          <span class="news-item-title">塞尔维亚总统选举将于12月27日举行</span>
          <span class="news-value-point">💡 当地时间11月26日，塞尔维亚国民议会议长丘皮奇宣布将于12月27日举行总统选举</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cwlymzm5mnxyo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="这场选举将影响蓝绿政治版图，六都选情备受关注，包括台北、新北、桃园、台中、台南、高雄，BBC中文整理各地候选人的简介。" data-title="台湾“九合一”选举：六都市长候选人简介" data-date="11-26 19:11" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-26 19:11</span>
          <span class="news-item-title">台湾“九合一”选举：六都市长候选人简介</span>
          <span class="news-value-point">💡 这场选举将影响蓝绿政治版图，六都选情备受关注，包括台北、新北、桃园、台中、台南、高雄，BBC中文整理各地候选人的简介</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/credit-rating-agency-puts-nvidia-on-notice-for-possible-downgrade-s-and-p-global-ratings-says-board-members-may-have-compromised-their-independence" target="_blank" rel="noopener" data-cat="keji" data-summary="标普全球评级（S&amp;P Global Ratings）表示，由于英伟达面临各种风险，包括走私指控以及缺乏首席执行官继任计划，该公司可能会下调英伟达的信用评级。" data-title="Credit rating agency puts Nvidia on notice for possible downgrade" data-date="11-27 01:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-27 01:00</span>
          <span class="news-item-title">信用评级机构对英伟达发出可能下调评级的通知</span>
          <span class="news-item-title-en">Credit rating agency puts Nvidia on notice for possible downgrade</span>
          <span class="news-value-point">💡 标普全球评级（S&P Global Ratings）表示，由于英伟达面临各种风险，包括走私指控以及缺乏首席执行官继任计划，该公司可能会下调英伟达…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/dram/electronics-manufacturers-set-up-memory-war-rooms-to-find-lock-in-dram-supplies-amid-worst-shortage-in-history-employees-scour-ebay-contact-hundreds-of-brokers-and-snap-up-even-small-batches-of-just-5-to-12-units" target="_blank" rel="noopener" data-cat="keji" data-summary="内存芯片短缺正迫使各公司通过非传统渠道（如在线发布信息和灰色市场）来寻找供应。有些公司甚至借贷，只为有足够的现金在芯片一有货时就能马上买到。" data-title="Electronics manufacturers set up memory &#39;war rooms&#39; to find, lock in DRAM supplies amid worst shortage in history" data-date="11-27 00:11" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-27 00:11</span>
          <span class="news-item-title">电子产品制造商设立内存“战情室”，以在历史上最严重的短缺中寻找和锁定DRAM供应</span>
          <span class="news-item-title-en">Electronics manufacturers set up memory 'war rooms' to find, lock in DRAM supplies amid worst shortage in history</span>
          <span class="news-value-point">💡 内存芯片短缺正迫使各公司通过非传统渠道（如在线发布信息和灰色市场）来寻找供应</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/26/as-anthropic-ipos-grand-theft-auto-vi-proves-why-efficiency-isnt-a-virtue/" target="_blank" rel="noopener" data-cat="keji" data-summary="在Anthropic上市的同一天，一款精心打造的拟人化视频游戏成为了有史以来最成功的娱乐产品之一。" data-title="As Anthropic IPOs, Grand Theft Auto VI proves why efficiency isn’t a virtue" data-date="11-27 00:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-27 00:00</span>
          <span class="news-item-title">与Anthropic的IPO一样，《侠盗猎车手6》证明了效率为何不是一种美德</span>
          <span class="news-item-title-en">As Anthropic IPOs, Grand Theft Auto VI proves why efficiency isn’t a virtue</span>
          <span class="news-value-point">💡 在Anthropic上市的同一天，一款精心打造的拟人化视频游戏成为了有史以来最成功的娱乐产品之一</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/photonics/inside-the-indium-phosphide-squeeze-and-the-optical-boom-inp-remains-tightly-constrained-as-the-demand-from-ai-puts-the-entire-supply-chain-under-pressure" target="_blank" rel="noopener" data-cat="keji" data-summary="人工智能行业向光互连的转变正在使激光器、收发器和共封装光学器件背后的集中性 InP 供应链不堪重负。" data-title="Exploring the Indium phosphide supply chain — the material constraint tightening the optical interconnect bottleneck" data-date="11-27 00:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-27 00:00</span>
          <span class="news-item-title">探索磷化铟供应链——加剧光互连瓶颈的材料制约因素</span>
          <span class="news-item-title-en">Exploring the Indium phosphide supply chain — the material constraint tightening the optical interconnect bottleneck</span>
          <span class="news-value-point">💡 人工智能行业向光互连的转变正在使激光器、收发器和共封装光学器件背后的集中性 InP 供应链不堪重负</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/policy/nvidia-stops-ai-gpu-shipments-to-southeast-asia-report-claims-data-centers-in-singapore-other-countries-in-trouble-as-commerce-department-requires-cloud-providers-to-obtain-export-license" target="_blank" rel="noopener" data-cat="keji" data-summary="新加坡、马来西亚、泰国和印度尼西亚的数据中心现在必须获得出口许可证，才能获得Nvidia AI GPU的交付。" data-title="Nvidia stops AI GPU shipments to Southeast Asia amid purported China cloud access ban, report claims" data-date="11-27 00:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-27 00:00</span>
          <span class="news-item-title">据报道，由于所谓的中国云访问禁令，Nvidia停止向东南亚供应AI GPU。</span>
          <span class="news-item-title-en">Nvidia stops AI GPU shipments to Southeast Asia amid purported China cloud access ban, report claims</span>
          <span class="news-value-point">💡 新加坡、马来西亚、泰国和印度尼西亚的数据中心现在必须获得出口许可证，才能获得Nvidia AI GPU的交付</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/033/131.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 26 日消息，据路透社报道，瑞士联邦网络安全局（BACS）周四通报，过去几天瑞士发生五起网络攻击，攻击者使用 AI 智能体针对企业以及关键基础设施运营方发起入侵。IT之家注意到，该局在公告中表示，五起攻击里有四起攻击得手，相关系统遭到入侵。遭到攻击的对象包含三家关键基础设施运营主体，据瑞士公共广播公司 SRF 介绍，它们分别是电力、供水以及通信服务供应商。瑞士联邦网络安全局没有透露攻击的幕后主体信息。机构建议相关企业落实防护手段，其中包括定期开展网络安全检测。" data-title="瑞士发生五起 AI 智能体网络攻击，电力供水通信系统遭入侵" data-date="11-26 23:24" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-26 23:24</span>
          <span class="news-item-title">瑞士发生五起 AI 智能体网络攻击，电力供水通信系统遭入侵</span>
          <span class="news-value-point">💡 IT之家 11 月 26 日消息，据路透社报道，瑞士联邦网络安全局（BACS）周四通报，过去几天瑞士发生五起网络攻击，攻击者使用 AI 智能体针…</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/513021.html" target="_blank" rel="noopener" data-cat="keji" data-summary="已跑了超过一万次会话，在Lean4里验证通过了2400多条引理" data-title="381个AI直播冲刺证明P=NP！把GitHub干崩了" data-date="11-26 21:56" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-26 21:56</span>
          <span class="news-item-title">381个AI直播冲刺证明P=NP！把GitHub干崩了</span>
          <span class="news-value-point">💡 已跑了超过一万次会话，在Lean4里验证通过了2400多条引理</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-26/10738444.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新社台北11月26日电 台湾积体电路制造股份有限公司(台积电)将于当地时间12月4日在美国亚利桑那州厂区举行扩建典礼，另拟斥资逾200亿美元赴得克萨斯州设厂。在美投资不断加码，舆论对台积电先进制程加速外移的疑虑随之再起。" data-title="台积电拟扩大在美投资 舆论忧先进制程加速外移" data-date="11-26 21:46" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-26 21:46</span>
          <span class="news-item-title">台积电拟扩大在美投资 舆论忧先进制程加速外移</span>
          <span class="news-value-point">💡 中新社台北11月26日电 台湾积体电路制造股份有限公司(台积电)将于当地时间12月4日在美国亚利桑那州厂区举行扩建典礼，另拟斥资逾200亿美元赴…</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/512981.html" target="_blank" rel="noopener" data-cat="keji" data-summary="还得是科班尖子生" data-title="AI 3D界的“X光”来了！一图直出巴洛克雕塑，3D打印开箱即用" data-date="11-26 20:39" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-26 20:39</span>
          <span class="news-item-title">AI 3D界的“X光”来了！一图直出巴洛克雕塑，3D打印开箱即用</span>
          <span class="news-value-point">💡 还得是科班尖子生</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/26/business/nvidia-southeast-asia-sales.html" target="_blank" rel="noopener" data-cat="keji" data-summary="此次影响到四个国家的停运是继美国出台一项新规定之后发生的，该规定要求这些国家/地区的公司在购买先进人工智能芯片时必须持有许可证。" data-title="Nvidia Halts Sales to Southeast Asia as U.S. Tightens China Restrictions" data-date="11-26 20:04" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-26 20:04</span>
          <span class="news-item-title">随着美国收紧对中国的限制，Nvidia暂停向东南亚销售产品</span>
          <span class="news-item-title-en">Nvidia Halts Sales to Southeast Asia as U.S. Tightens China Restrictions</span>
          <span class="news-value-point">💡 此次影响到四个国家的停运是继美国出台一项新规定之后发生的，该规定要求这些国家/地区的公司在购买先进人工智能芯片时必须持有许可证</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/512972.html" target="_blank" rel="noopener" data-cat="keji" data-summary="全栈方案破解工业机器人连续作业难题" data-title="90 秒自动换装补能，具微科技“潘多拉”支撑机器人无人化值守" data-date="11-26 18:07" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-26 18:07</span>
          <span class="news-item-title">90 秒自动换装补能，具微科技“潘多拉”支撑机器人无人化值守</span>
          <span class="news-value-point">💡 全栈方案破解工业机器人连续作业难题</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/26/business/huawei-trump-china-ai.html" target="_blank" rel="noopener" data-cat="keji" data-summary="随着中国获得Nvidia先进芯片的机会越来越少，尽管华为与美国竞争对手存在巨大的技术差距，但它对北京来说正变得越来越不可或缺。" data-title="Trump Tried to Cripple Huawei. Now It Is Central to China’s A.I. Push." data-date="11-26 18:01" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-26 18:01</span>
          <span class="news-item-title">特朗普曾试图削弱华为。如今，它已成为中国人工智能发展的核心。</span>
          <span class="news-item-title-en">Trump Tried to Cripple Huawei. Now It Is Central to China’s A.I. Push.</span>
          <span class="news-value-point">💡 随着中国获得Nvidia先进芯片的机会越来越少，尽管华为与美国竞争对手存在巨大的技术差距，但它对北京来说正变得越来越不可或缺</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/512942.html" target="_blank" rel="noopener" data-cat="keji" data-summary="12月6日，WAIC将携手第六届“海聚英才”全球创新创业峰会，把这场关于“人”的讨论带回现场。" data-title="报名最后2天｜AI浪潮之中，来认识创造未来的人" data-date="11-26 15:36" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-26 15:36</span>
          <span class="news-item-title">报名最后2天｜AI浪潮之中，来认识创造未来的人</span>
          <span class="news-value-point">💡 12月6日，WAIC将携手第六届“海聚英才”全球创新创业峰会，把这场关于“人”的讨论带回现场</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/512916.html" target="_blank" rel="noopener" data-cat="keji" data-summary="30秒一镜到底，可自动编排镜头" data-title="顶尖商用级AI视频每秒只要5毛！中国开源新势力拿下全球第一" data-date="11-26 14:41" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-26 14:41</span>
          <span class="news-item-title">顶尖商用级AI视频每秒只要5毛！中国开源新势力拿下全球第一</span>
          <span class="news-value-point">💡 30秒一镜到底，可自动编排镜头</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/512897.html" target="_blank" rel="noopener" data-cat="keji" data-summary="李斌坦言：不做AI变革可能活不下去" data-title="任少卿带着世界模型3.0来了！蔚来智驾训练提效5倍，座舱也用上强化学习" data-date="11-26 11:23" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-26 11:23</span>
          <span class="news-item-title">任少卿带着世界模型3.0来了！蔚来智驾训练提效5倍，座舱也用上强化学习</span>
          <span class="news-value-point">💡 李斌坦言：不做AI变革可能活不下去</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025489/tottenham-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Spurs latest: Savio set for several weeks out" data-title="Spurs latest: Savio set for several weeks out" data-date="11-27 01:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-27 01:00</span>
          <span class="news-item-title">热刺最新消息：萨维奥将缺席数周</span>
          <span class="news-item-title-en">Spurs latest: Savio set for several weeks out</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c5wy43j1l3rwo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="切尔西主教练哈维·阿隆索表示，后卫韦斯利·福法纳已就其在未经俱乐部许可的情况下接受采访时发表的争议言论道歉。" data-title="Fofana has apologised for interview" data-date="11-27 00:47" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-27 00:47</span>
          <span class="news-item-title">福法纳就采访一事道歉</span>
          <span class="news-item-title-en">Fofana has apologised for interview</span>
          <span class="news-value-point">💡 切尔西主教练哈维·阿隆索表示，后卫韦斯利·福法纳已就其在未经俱乐部许可的情况下接受采访时发表的争议言论道歉</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/celta-vigo-vs-bournemouth/live/577814" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Europa and Conference League LIVE! Much-changed Bournemouth &amp; Brighton in action" data-title="Europa and Conference League LIVE! Much-changed Bournemouth &amp; Brighton in action" data-date="11-27 00:30" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-27 00:30</span>
          <span class="news-item-title">欧罗巴联赛和欧会杯直播！阵容大变的伯恩茅斯和布莱顿即将出战</span>
          <span class="news-item-title-en">Europa and Conference League LIVE! Much-changed Bournemouth & Brighton in action</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13616076/premier-league-predictions-jones-knows-best-bets-nottingham-forest-vs-chelsea-arsenal-vs-manchester-city-and-more" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="我们的顶级投注顾问刘易斯·琼斯（又名Jones Knows）提供他对英超联赛的分析和投注见解。" data-title="PL Predictions: How will your club fare this weekend?" data-date="11-27 00:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-27 00:00</span>
          <span class="news-item-title">英超预测：您的俱乐部本周末表现如何？</span>
          <span class="news-item-title-en">PL Predictions: How will your club fare this weekend?</span>
          <span class="news-value-point">💡 我们的顶级投注顾问刘易斯·琼斯（又名Jones Knows）提供他对英超联赛的分析和投注见解</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13616076/premier-league-predictions-jones-knows-best-bets-nottingham-forest-vs-chelsea-arsenal-vs-manchester-city-and-more" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="我们的顶级投注顾问刘易斯·琼斯（又名Jones Knows）提供他对英超联赛的分析和投注见解。" data-title="PL Predictions: How will your club fare this weekend?" data-date="11-27 00:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-27 00:00</span>
          <span class="news-item-title">英超预测：您的俱乐部本周末表现如何？</span>
          <span class="news-item-title-en">PL Predictions: How will your club fare this weekend?</span>
          <span class="news-value-point">💡 我们的顶级投注顾问刘易斯·琼斯（又名Jones Knows）提供他对英超联赛的分析和投注见解</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c3n0l29lrr27o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="BBC体育足球专家克里斯·萨顿（Chris Sutton）与Kings of Leon乐队鼓手内森·福洛威尔（Nathan Followill）就本周末英超联赛的比赛结果进行预测。" data-title="Sutton&#39;s predictions v Kings of Leon drummer Nathan Followill" data-date="11-26 23:01" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-26 23:01</span>
          <span class="news-item-title">Sutton的预测与Kings of Leon鼓手Nathan Followill的预测</span>
          <span class="news-item-title-en">Sutton's predictions v Kings of Leon drummer Nathan Followill</span>
          <span class="news-value-point">💡 BBC体育足球专家克里斯·萨顿（Chris Sutton）与Kings of Leon乐队鼓手内森·福洛威尔（Nathan Followill）…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmn4k7v93gvzo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联门将森内·拉门斯在与葡萄牙体育的2-2平局中犯下两次重大失误——毛里西奥·波切蒂诺会弃用这位门将吗？" data-title="Lammens - the Man Utd goalkeeper under scrutiny like never before" data-date="11-26 22:56" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-26 22:56</span>
          <span class="news-item-title">拉门斯——曼联门将正面临前所未有的审视</span>
          <span class="news-item-title-en">Lammens - the Man Utd goalkeeper under scrutiny like never before</span>
          <span class="news-value-point">💡 曼联门将森内·拉门斯在与葡萄牙体育的2-2平局中犯下两次重大失误——毛里西奥·波切蒂诺会弃用这位门将吗</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025497/chelsea-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Chelsea latest: Fofana apologised over unauthorised interview, says Alonso" data-title="Chelsea latest: Fofana apologised over unauthorised interview, says Alonso" data-date="11-26 22:15" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 22:15</span>
          <span class="news-item-title">切尔西最新消息：阿隆索表示，福法纳就未经授权的采访道歉</span>
          <span class="news-item-title-en">Chelsea latest: Fofana apologised over unauthorised interview, says Alonso</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025486/arsenal-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Arsenal latest: Merson backs Gyokeres for start against Man City" data-title="Arsenal latest: Merson backs Gyokeres for start against Man City" data-date="11-26 22:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 22:00</span>
          <span class="news-item-title">阿森纳最新消息：默森支持吉奥克雷斯首发对阵曼城</span>
          <span class="news-item-title-en">Arsenal latest: Merson backs Gyokeres for start against Man City</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/12040/13279298/crystal-palace-transfers-latest-news-rumours-and-gossip-live-updates-goals-and-highlights" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Palace latest: McNeil says Everton &#39;were really good&#39; after failed January move" data-title="Palace latest: McNeil says Everton &#39;were really good&#39; after failed January move" data-date="11-26 21:50" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 21:50</span>
          <span class="news-item-title">水晶宫最新消息：麦克尼尔表示，在1月份转会失败后，埃弗顿“表现得非常好”</span>
          <span class="news-item-title-en">Palace latest: McNeil says Everton 'were really good' after failed January move</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cr3wgd5exl0do?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="亚历杭德罗·加尔纳乔在阿斯顿维拉的短暂职业生涯似乎已经结束，那么这位 22 岁的球员接下来会怎样？" data-title="Not even making a 12-man bench - what next for Garnacho?" data-date="11-26 21:23" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-26 21:23</span>
          <span class="news-item-title">连12人替补名单都进不了——加尔纳乔接下来该怎么办？</span>
          <span class="news-item-title-en">Not even making a 12-man bench - what next for Garnacho?</span>
          <span class="news-value-point">💡 亚历杭德罗·加尔纳乔在阿斯顿维拉的短暂职业生涯似乎已经结束，那么这位 22 岁的球员接下来会怎样</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13616790/man-utds-controversial-refereeing-decisions-are-officials-making-mauricio-pochettinos-job-harder" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="毛里西奥·波切蒂诺要想扭转曼联本赛季的颓势，光靠出色的表现还不够——裁判的判罚也必须对他们有利。" data-title="Wrong calls and bad results: Are refs making Man Utd&#39;s problems worse?" data-date="11-26 20:20" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 20:20</span>
          <span class="news-item-title">误判和糟糕的结果：裁判是否在加剧曼联的问题？</span>
          <span class="news-item-title-en">Wrong calls and bad results: Are refs making Man Utd's problems worse?</span>
          <span class="news-value-point">💡 毛里西奥·波切蒂诺要想扭转曼联本赛季的颓势，光靠出色的表现还不够——裁判的判罚也必须对他们有利</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13616790/man-utds-controversial-refereeing-decisions-are-officials-making-mauricio-pochettinos-job-harder" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="毛里西奥·波切蒂诺要想扭转曼联本赛季的颓势，光靠出色的表现还不够——裁判的判罚也必须对他们有利。" data-title="Wrong calls and bad results: Are refs making Man Utd&#39;s problems worse?" data-date="11-26 20:20" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 20:20</span>
          <span class="news-item-title">误判和糟糕的结果：裁判是否在加剧曼联的问题？</span>
          <span class="news-item-title-en">Wrong calls and bad results: Are refs making Man Utd's problems worse?</span>
          <span class="news-value-point">💡 毛里西奥·波切蒂诺要想扭转曼联本赛季的颓势，光靠出色的表现还不够——裁判的判罚也必须对他们有利</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13616792/leny-yoro-red-card-written-reasons-why-manchester-united-defenders-red-card-at-liverpool-was-overturned-published-by-the-fa" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英格兰足球总会（FA）已公布书面理由，解释为何利物浦对阵曼联的比赛中，莱尼·约罗（Leny Yoro）的红牌被撤销——尽管裁判机构Pro Ref表示，场上判罚是正确的。" data-title="Yoro red card: Written reasons for overturned decision revealed" data-date="11-26 20:09" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 20:09</span>
          <span class="news-item-title">约罗红牌：推翻判罚的书面理由已披露</span>
          <span class="news-item-title-en">Yoro red card: Written reasons for overturned decision revealed</span>
          <span class="news-value-point">💡 英格兰足球总会（FA）已公布书面理由，解释为何利物浦对阵曼联的比赛中，莱尼·约罗（Leny Yoro）的红牌被撤销——尽管裁判机构Pro Ref…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cq20x16zxxzeo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="对于英超联赛的裁判来说，KMI小组的重要性可能超乎您的想象。它决定了他们薪水的很大一部分。" data-title="Why KMI Panel frustrates referees too - and impacts their salary" data-date="11-26 15:28" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-26 15:28</span>
          <span class="news-item-title">为什么KMI小组也会让裁判感到沮丧——并影响他们的薪酬</span>
          <span class="news-item-title-en">Why KMI Panel frustrates referees too - and impacts their salary</span>
          <span class="news-value-point">💡 对于英超联赛的裁判来说，KMI小组的重要性可能超乎您的想象</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.tomshardware.com/gift-guides-seasonal-sales/essential-3d-printer-maintenance-tool-deals-for-black-friday-save-up-to-30-percent-on-precision-tools-lights-snips-and-more" target="_blank" rel="noopener" data-cat="zonghe" data-summary="为了获得最佳的3D打印效果，始终需要备有一些常用的工具。" data-title="Essential 3D printer maintenance tool deals for Black Friday — save up to 30% on precision tools, lights, snips, and more" data-date="11-27 01:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-27 01:30</span>
          <span class="news-item-title">黑色星期五必备3D打印机维护工具优惠——精密工具、照明灯、剪钳等最高立省30%</span>
          <span class="news-item-title-en">Essential 3D printer maintenance tool deals for Black Friday — save up to 30% on precision tools, lights, snips, and more</span>
          <span class="news-value-point">💡 为了获得最佳的3D打印效果，始终需要备有一些常用的工具</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1035932/apple-macbook-neo-black-friday-2026-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="如果您正在寻找一台新笔记本电脑，或者想为身边的学生选购一份礼物，那么您可以在多家零售商处以100美元的优惠价格购买MacBook Neo，该优惠适用于两种存储容量和所有四种颜色。256GB 款目前在亚马逊和开市客的售价为 599.99 美元，" data-title="The MacBook Neo is receiving a rare $100 discount for Black Friday" data-date="11-27 01:07" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-27 01:07</span>
          <span class="news-item-title">MacBook Neo在黑色星期五享受罕见的100美元折扣</span>
          <span class="news-item-title-en">The MacBook Neo is receiving a rare $100 discount for Black Friday</span>
          <span class="news-value-point">💡 如果您正在寻找一台新笔记本电脑，或者想为身边的学生选购一份礼物，那么您可以在多家零售商处以100美元的优惠价格购买MacBook Neo，该优惠…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1043228/android-play-store-google-developer-address-eu" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在Google宣布从明年起将要求许多独立Android应用开发者公开分享电话号码和地址后，这些开发者对自己的隐私表示担忧。这项政策变更旨在符合欧盟法规。" data-title="Android app developers will soon have to share their address publicly" data-date="11-27 01:06" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-27 01:06</span>
          <span class="news-item-title">Android应用开发者很快将不得不公开其地址</span>
          <span class="news-item-title-en">Android app developers will soon have to share their address publicly</span>
          <span class="news-value-point">💡 在Google宣布从明年起将要求许多独立Android应用开发者公开分享电话号码和地址后，这些开发者对自己的隐私表示担忧</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1028991/black-friday-best-early-deals-2026" target="_blank" rel="noopener" data-cat="zonghe" data-summary="黑色星期五的倒计时已经开始，许多折扣已经上线。虽然购物节要到明天（11月27日）才正式开始，但零售商已经开始为我们最喜爱的部分科技产品推出提前优惠。当然，随着价格" data-title="The best Black Friday deals we’ve already found" data-date="11-27 00:55" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-27 00:55</span>
          <span class="news-item-title">我们已经找到的最佳黑色星期五优惠</span>
          <span class="news-item-title-en">The best Black Friday deals we’ve already found</span>
          <span class="news-value-point">💡 黑色星期五的倒计时已经开始，许多折扣已经上线</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/26/us/iowa-lead-ammunition-stockpile-history.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="一年多前，爱荷华州一家工厂就开始努力处置不稳定的爆炸物，但当时并未完成，为周三发生的争议性爆炸埋下了隐患。" data-title="The Army Knew Much Earlier of the Explosive Risk in Iowa, Evidence Suggests" data-date="11-27 00:50" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-27 00:50</span>
          <span class="news-item-title">有证据表明，陆军早在很久以前就知道爱荷华州存在爆炸风险</span>
          <span class="news-item-title-en">The Army Knew Much Earlier of the Explosive Risk in Iowa, Evidence Suggests</span>
          <span class="news-value-point">💡 一年多前，爱荷华州一家工厂就开始努力处置不稳定的爆炸物，但当时并未完成，为周三发生的争议性爆炸埋下了隐患</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/policy/1043116/fcc-disney-abc-broadcast-licenses-review-early-judge-block" target="_blank" rel="noopener" data-cat="zonghe" data-summary="美国地方法官洛伦·阿里汗（Loren AliKhan）通过一项初步禁令阻止了联邦通信委员会（FCC）对ABC广播许可证进行提前审查，并驳回了FCC驳回ABC第一修正案诉讼的请求。ABC指控" data-title="Federal judge blocks the FCC from reviewing ABC’s licenses early" data-date="11-27 00:38" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-27 00:38</span>
          <span class="news-item-title">联邦法官阻止联邦通信委员会提前审查ABC的执照</span>
          <span class="news-item-title-en">Federal judge blocks the FCC from reviewing ABC’s licenses early</span>
          <span class="news-value-point">💡 美国地方法官洛伦·阿里汗（Loren AliKhan）通过一项初步禁令阻止了联邦通信委员会（FCC）对ABC广播许可证进行提前审查，并驳回了FC…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/gift-guides-seasonal-sales/13-tech-bargains-for-just-usd13-or-less-to-upgrade-your-pc-setup-must-own-gadgets-and-impulse-buys-to-solve-everyday-problems-from-network-switches-to-cleaning-kits" target="_blank" rel="noopener" data-cat="zonghe" data-summary="今年黑色星期五，借助这13款科技小工具和实用工具，以不到13美元的价格升级您的装备，无需大破费。" data-title="13 tech bargains for only $13 or less to upgrade your desktop PC setup" data-date="11-27 00:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-27 00:30</span>
          <span class="news-item-title">只需$ 13或更少的13个技术交易，即可升级您的台式电脑设置</span>
          <span class="news-item-title-en">13 tech bargains for only $13 or less to upgrade your desktop PC setup</span>
          <span class="news-value-point">💡 今年黑色星期五，借助这13款科技小工具和实用工具，以不到13美元的价格升级您的装备，无需大破费</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13616899/phil-taylor-takes-first-dart-at-double-in-his-modus-competitive-comeback" target="_blank" rel="noopener" data-cat="zonghe" data-summary="菲尔·泰勒在朴茨茅斯的MODUS超级系列赛国际双人赛第4站中，与阿德里安·刘易斯搭档，在复出首场比赛中以一镖命中双倍区，以84分完成收官。" data-title="&#39;Super stuff!&#39; - Taylor takes first dart at double in his Modus competitive comeback!" data-date="11-27 00:28" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-27 00:28</span>
          <span class="news-item-title">“太棒了！”——泰勒在莫杜斯联赛的复出之战中，第一镖就命中双倍区域！</span>
          <span class="news-item-title-en">'Super stuff!' - Taylor takes first dart at double in his Modus competitive comeback!</span>
          <span class="news-value-point">💡 菲尔·泰勒在朴茨茅斯的MODUS超级系列赛国际双人赛第4站中，与阿德里安·刘易斯搭档，在复出首场比赛中以一镖命中双倍区，以84分完成收官</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13616889/let-andalucia-costa-del-sol-open-de-espana-day-one-highlights" target="_blank" rel="noopener" data-cat="zonghe" data-summary="西班牙马拉加安达卢西亚太阳海岸公开赛第一天的精彩瞬间。" data-title="Andalucia Costa Del Sol Open de Espana | Day one highlights" data-date="11-27 00:07" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-27 00:07</span>
          <span class="news-item-title">安达卢西亚太阳海岸西班牙公开赛 | 第一天精彩集锦</span>
          <span class="news-item-title-en">Andalucia Costa Del Sol Open de Espana | Day one highlights</span>
          <span class="news-value-point">💡 西班牙马拉加安达卢西亚太阳海岸公开赛第一天的精彩瞬间</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/033/132.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 27 日消息，Epic 本周送出的游戏是《Bread and Fred》，下周送出的游戏是《Strange Antiquities》。领取链接：《Bread and Fred》IT之家附《Bread and Fred》游戏简介：Bread &amp; Fred 是一款具有挑战性的合作平台游戏，两名玩家必须合作跳跃并爬上雪山之巅。扮演 Bread 和 Fred，进行令人恼火、有时甚至令人发狂的攀爬，每次跳跃都需要精确度。每一次着陆，你都会离山顶更近，离掌握平台跳跃更近一步，但从山上掉下来的距离会更远。企鹅机制：- 摇摆到达远处的平台！Bread 和 Fred 彼此依恋。这意味着你们不仅会一起坠落，而且还可以充分利用动量来摆动并推动彼此，超越任何一只企鹅所能跳跃的高度。确保其中一人锚" data-title="Epic 喜加一：《Bread and Fred》游戏免费领取" data-date="11-27 00:05" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-27 00:05</span>
          <span class="news-item-title">Epic 喜加一：《Bread and Fred》游戏免费领取</span>
          <span class="news-value-point">💡 IT之家 11 月 27 日消息，Epic 本周送出的游戏是《Bread and Fred》，下周送出的游戏是《Strange Antiquit…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1041762/best-black-friday-streaming-deals-2026" target="_blank" rel="noopener" data-cat="zonghe" data-summary="黑色星期五不仅是购买新电视的省钱好时机，也是节省电视观看费用的好机会。购物节通常会带来大幅度的流媒体优惠，今年也不例外，一些流媒体平台提供的优惠幅度超过50%。" data-title="Disney Plus, Hulu, and HBO Max are all over 50 percent off for Black Friday" data-date="11-27 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-27 00:00</span>
          <span class="news-item-title">Disney Plus、Hulu和HBO Max在黑色星期五均有五折以上的优惠</span>
          <span class="news-item-title-en">Disney Plus, Hulu, and HBO Max are all over 50 percent off for Black Friday</span>
          <span class="news-value-point">💡 黑色星期五不仅是购买新电视的省钱好时机，也是节省电视观看费用的好机会</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/games/1043169/rockstar-games-union-vote-iwgb" target="_blank" rel="noopener" data-cat="zonghe" data-summary="《侠盗猎车手6》开发商Rockstar Games的员工将不会组建工会，因为正式承认协议的投票未获通过，只有25%的选票支持组建工会。英国独立工人联盟（IWGB）表示，" data-title="GTA VI developers vote against unionization" data-date="11-26 23:55" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-26 23:55</span>
          <span class="news-item-title">《GTA VI》开发人员投票反对工会化</span>
          <span class="news-item-title-en">GTA VI developers vote against unionization</span>
          <span class="news-value-point">💡 《侠盗猎车手6》开发商Rockstar Games的员工将不会组建工会，因为正式承认协议的投票未获通过，只有25%的选票支持组建工会</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/f1/news/12040/13616749/george-russell-admits-feud-with-max-verstappen-is-avoidable-and-unnecessary-ahead-of-qatar-grand-prix" target="_blank" rel="noopener" data-cat="zonghe" data-summary="乔治·拉塞尔表示，在拉斯维加斯大奖赛上，他和马克斯·维斯塔潘的恩怨再次爆发后，他对维斯塔潘的批评感到“好笑”，但他也承认这场冲突是“可以避免的”。" data-title="Russell: I found Verstappen comments amusing" data-date="11-26 23:55" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-26 23:55</span>
          <span class="news-item-title">拉塞尔：我觉得维斯塔潘的评论很有趣</span>
          <span class="news-item-title-en">Russell: I found Verstappen comments amusing</span>
          <span class="news-value-point">💡 乔治·拉塞尔表示，在拉斯维加斯大奖赛上，他和马克斯·维斯塔潘的恩怨再次爆发后，他对维斯塔潘的批评感到“好笑”，但他也承认这场冲突是“可以避免的”</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/ssds/save-21-percent-on-this-ultra-fast-2tb-sandisk-optimus-gx-pro-8100-ssd-now-just-17-5-cents-per-gb-rebranded-sn8100-offers-gen-5-speeds-of-up-to-14-900-mb-s-at-a-record-low-price" target="_blank" rel="noopener" data-cat="zonghe" data-summary="第5代2TB Sandisk Optimus GX Pro 8100超值优惠，现价仅为349.99美元。" data-title="Save 21% on this ultra-fast 2TB SanDisk Optimus GX Pro 8100 SSD, now just 17.5 cents per GB" data-date="11-26 23:52" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-26 23:52</span>
          <span class="news-item-title">这款超高速2TB SanDisk Optimus GX Pro 8100固态硬盘现享七九折优惠，每GB仅需17.5美分</span>
          <span class="news-item-title-en">Save 21% on this ultra-fast 2TB SanDisk Optimus GX Pro 8100 SSD, now just 17.5 cents per GB</span>
          <span class="news-value-point">💡 第5代2TB Sandisk Optimus GX Pro 8100超值优惠，现价仅为349.99美元</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/gift-guides-seasonal-sales/15-tech-gadgets-that-improved-my-tech-life-are-on-sale-for-less-than-usd50-black-friday-pricing-means-some-are-even-under-usd25" target="_blank" rel="noopener" data-cat="zonghe" data-summary="从电动螺丝刀到高分辨率网络摄像头，这些都是便宜的游戏规则改变者。" data-title="15 tech gadgets that improved my tech life are on sale for less than $50" data-date="11-26 23:45" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-26 23:45</span>
          <span class="news-item-title">15款改善我科技生活的科技小工具正在以不到50美元的价格促销</span>
          <span class="news-item-title-en">15 tech gadgets that improved my tech life are on sale for less than $50</span>
          <span class="news-value-point">💡 从电动螺丝刀到高分辨率网络摄像头，这些都是便宜的游戏规则改变者</span>
        </a>
  </div>
</div>
<script defer src="{{ "/assets/js/news-feed.js" | relative_url }}"></script>


<p class="news-updated">🕐 抓取更新于 2026-11-27 01:50（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
