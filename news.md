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
      <span>2026-11-25 06:38 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num">7</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">4</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">天空体育×14 · 中国新闻网×13</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">按来源聚合 · 最近 24 小时精选</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.tomshardware.com/tech-industry/cyber-security/us-doj-touts-largest-ever-crackdown-on-scammers-across-the-globe-as-it-seizes-14-000-devices-and-usd17-billion-in-illicit-funds-operation-results-in-800-defendants-and-frees-2-200-forced-laborers" target="_blank" rel="noopener" data-cat="shizheng" data-summary="美国司法部宣布，其有史以来最大规模的反诈骗行动已追回超过80亿美元的受害人损失，并对800多名被告提起指控。" data-title="US DOJ touts &quot;largest-ever&quot; crackdown on scammers across the globe as it seizes 14,000 devices and $17 billion in illicit funds" data-date="11-25 06:30" data-source="Tom's Hardware">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
        <span class="hero-featured-date">🕒 11-25 06:30</span>
      </div>
      <h2 class="hero-featured-title">美国司法部宣称对全球诈骗犯进行了“有史以来最大规模”的打击，查获了1.4万台设备和170亿美元的非法资金。</h2>
      <div class="hero-featured-title-en">US DOJ touts "largest-ever" crackdown on scammers across the globe as it seizes 14,000 devices and $17 billion in illicit funds</div>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/gj/2026/11-25/10737278.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新社吉隆坡11月24日电 (记者 刘育英)马来西亚数字部部长戈宾德·辛格·德奥24日在国会下议院表示，政府高度重视儿童对人工智能(AI)陪伴类应用及互动聊天机器人产生情感依赖可能带来的风险，正研究相关保护措施，包括为陷入情绪困扰的用户提供援助机制。" data-title="马来西亚拟加强AI陪伴类应用监管" data-date="11-25 06:21" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">马来西亚拟加强AI陪伴类应用监管</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/cqzr5ylmeerlo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联和毛里西奥·波切蒂诺对VAR裁判约翰·布鲁克斯和裁判主管霍华德·韦伯处理莱尼·约罗红牌的方式感到愤怒。" data-title="Pochettino leads Man Utd fury at Yoro red card ruling" data-date="11-25 06:05" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">波切蒂诺带头对尤罗的红牌判罚表示不满</p>
    </a>
    <a class="hero-sub-card" href="https://techcrunch.com/2026/11/24/jensen-huang-still-thinks-a-succession-plan-creates-unnecessary-hierarchy/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="对于一家在过去两周一直在摸索没有创始人会发生什么情况的公司来说，这是一个非同寻常的立场。" data-title="Jensen Huang still thinks a succession plan creates unnecessary hierarchy" data-date="11-25 06:27" data-source="TechCrunch">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
      </div>
      <p class="hero-sub-title">黄仁勋仍然认为继任计划会造成不必要的层级关系</p>
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
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/cyber-security/us-doj-touts-largest-ever-crackdown-on-scammers-across-the-globe-as-it-seizes-14-000-devices-and-usd17-billion-in-illicit-funds-operation-results-in-800-defendants-and-frees-2-200-forced-laborers" target="_blank" rel="noopener" data-cat="shizheng" data-summary="美国司法部宣布，其有史以来最大规模的反诈骗行动已追回超过80亿美元的受害人损失，并对800多名被告提起指控。" data-title="US DOJ touts &quot;largest-ever&quot; crackdown on scammers across the globe as it seizes 14,000 devices and $17 billion in illicit funds" data-date="11-25 06:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-25 06:30</span>
          <span class="news-item-title">美国司法部宣称对全球诈骗犯进行了“有史以来最大规模”的打击，查获了1.4万台设备和170亿美元的非法资金。</span>
          <span class="news-item-title-en">US DOJ touts "largest-ever" crackdown on scammers across the globe as it seizes 14,000 devices and $17 billion in illicit funds</span>
          <span class="news-value-point">💡 美国司法部宣布，其有史以来最大规模的反诈骗行动已追回超过80亿美元的受害人损失，并对800多名被告提起指控</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-25/10737280.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社伦敦11月24日电 (记者 欧阳开宇)英国卫生安全局24日发布数据显示，2026年夏季英国高温相关死亡人数达5258人，创下该机构2016年开启相关统计以来的最高年度纪录。" data-title="英国2026年夏季高温致死人数创新高" data-date="11-25 06:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-25 06:24</span>
          <span class="news-item-title">英国2026年夏季高温致死人数创新高</span>
          <span class="news-value-point">💡 中新社伦敦11月24日电 (记者 欧阳开宇)英国卫生安全局24日发布数据显示，2026年夏季英国高温相关死亡人数达5258人，创下该机构2016…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-25/10737279.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社莫斯科11月24日电 俄罗斯国家航天集团24日表示，“进步MS-36”货运飞船当天从位于哈萨克斯坦境内的拜科努尔航天发射场发射升空，前往国际空间站。" data-title="俄“进步MS" data-date="11-25 06:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-25 06:23</span>
          <span class="news-item-title">俄“进步MS</span>
          <span class="news-value-point">💡 中新社莫斯科11月24日电 俄罗斯国家航天集团24日表示，“进步MS-36”货运飞船当天从位于哈萨克斯坦境内的拜科努尔航天发射场发射升空，前往国…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-25/10737276.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社快讯：神舟二十四号航天员汤洪波、武毅、穆罕默德·齐尚·阿里领命出征。" data-title="神舟二十四号航天员汤洪波、武毅、穆罕默德·齐尚·阿里领命出征" data-date="11-25 05:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-25 05:40</span>
          <span class="news-item-title">神舟二十四号航天员汤洪波、武毅、穆罕默德·齐尚·阿里领命出征</span>
          <span class="news-value-point">💡 新华社快讯：神舟二十四号航天员汤洪波、武毅、穆罕默德·齐尚·阿里领命出征</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-25/10737275.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社快讯：神舟二十四号载人飞行任务航天员乘组出征仪式在酒泉卫星发射中心问天阁圆梦园广场举行。" data-title="神舟二十四号载人飞行任务航天员乘组出征仪式在酒泉卫星发射中心问天阁圆梦园广场举行" data-date="11-25 05:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-25 05:39</span>
          <span class="news-item-title">神舟二十四号载人飞行任务航天员乘组出征仪式在酒泉卫星发射中心问天阁圆梦园广场举行</span>
          <span class="news-value-point">💡 新华社快讯：神舟二十四号载人飞行任务航天员乘组出征仪式在酒泉卫星发射中心问天阁圆梦园广场举行</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/policy/1041568/fisa-ndaa-blue-wave" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在立法会议结束前几周，一些国会议员正争相重新授权一项有争议的无证窃听权力，他们可能会将其附在必须通过的国防开支法案上。参议员迈克·朗兹（Mike Rounds，南达科他州共和党）告诉《政治报》：" data-title="The clock is running out for America’s most contentious spying law" data-date="11-25 04:00" data-source="The Verge">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-25 04:00</span>
          <span class="news-item-title">美国最具争议的间谍法案即将到期</span>
          <span class="news-item-title-en">The clock is running out for America’s most contentious spying law</span>
          <span class="news-value-point">💡 在立法会议结束前几周，一些国会议员正争相重新授权一项有争议的无证窃听权力，他们可能会将其附在必须通过的国防开支法案上</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/24/us/politics/tennessee-house-election-results-broderick-wins.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在一位技术支持人员在没有投放任何电视广告的情况下击败了一位连任八届的共和党议员后，民主党在中期选举中的大胜在众议院中继续扩大。" data-title="Broderick Wins Tennessee House Race, Giving Democrats Largest Majority in 30 Years" data-date="11-25 03:26" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-25 03:26</span>
          <span class="news-item-title">布罗德里克赢得田纳西州众议院席位，使民主党获得30年来最多的多数席位</span>
          <span class="news-item-title-en">Broderick Wins Tennessee House Race, Giving Democrats Largest Majority in 30 Years</span>
          <span class="news-value-point">💡 在一位技术支持人员在没有投放任何电视广告的情况下击败了一位连任八届的共和党议员后，民主党在中期选举中的大胜在众议院中继续扩大</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-24/10737270.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="2026年11月24日，中共中央政治局委员、外交部长王毅应约同英国外交大臣米利班德通电话。" data-title="王毅同英国外交大臣米利班德通电话" data-date="11-24 23:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 23:00</span>
          <span class="news-item-title">王毅同英国外交大臣米利班德通电话</span>
          <span class="news-value-point">💡 2026年11月24日，中共中央政治局委员、外交部长王毅应约同英国外交大臣米利班德通电话</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-24/10737230.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网东京11月24日电 (记者 朱晨曦)日本厚生劳动省24日公布的人口动态统计显示，今年1至9月，包括外国人在内的日本出生人口为52.3304万人，与去年同期相比减少1760人，降幅为0.3%。" data-title="日本今年1至9月出生人口同比减少0.3%" data-date="11-24 22:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 22:04</span>
          <span class="news-item-title">日本今年1至9月出生人口同比减少0.3%</span>
          <span class="news-value-point">💡 中新网东京11月24日电 (记者 朱晨曦)日本厚生劳动省24日公布的人口动态统计显示，今年1至9月，包括外国人在内的日本出生人口为52.3304…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-24/10737158.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网首尔11月24日电 (金旭 陈艺玲)据韩国国家数据处当地时间24日公布一项调查数据显示，韩国15岁及以上人口中，未婚人数达1388.1万人，其中30至39岁人群的未婚比例达53.1%，较2020年上升10.6个百分点，" data-title="韩国30至39岁人群未婚比例升至53.1%" data-date="11-24 22:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 22:04</span>
          <span class="news-item-title">韩国30至39岁人群未婚比例升至53.1%</span>
          <span class="news-value-point">💡 中新网首尔11月24日电 (金旭 陈艺玲)据韩国国家数据处当地时间24日公布一项调查数据显示，韩国15岁及以上人口中，未婚人数达1388.1万人…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-24/10737259.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社甘肃酒泉11月24日电 题：首飞太空，武毅与外籍航天员化友谊为志同道合" data-title="首飞太空，武毅与外籍航天员化友谊为志同道合" data-date="11-24 21:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 21:59</span>
          <span class="news-item-title">首飞太空，武毅与外籍航天员化友谊为志同道合</span>
          <span class="news-value-point">💡 中新社甘肃酒泉11月24日电 题：首飞太空，武毅与外籍航天员化友谊为志同道合</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-24/10737258.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月24日电(魏晨曦)有朋自远方来，不亦“乐”乎。近日，一首首风格迥异的乐曲跨越山海，在深圳同一座会场里相继响起。远道而来的客人，在熟悉的旋律中，体验了一把跨越文化的迎宾氛围。" data-title="特朗普停下脚步鼓掌，普京听到熟悉的歌：深圳APEC晚宴乐章曲目大有深意" data-date="11-24 21:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 21:53</span>
          <span class="news-item-title">特朗普停下脚步鼓掌，普京听到熟悉的歌：深圳APEC晚宴乐章曲目大有深意</span>
          <span class="news-value-point">💡 中新网11月24日电(魏晨曦)有朋自远方来，不亦“乐”乎</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-24/10737246.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网南宁11月24日电 (林浩 刘越 俞靖)11月24日，2026年“兴边富民助力高质量发展”网评引导活动在广西南宁市正式启动。" data-title="2026年“兴边富民助力高质量发展”网评引导活动在南宁启动" data-date="11-24 21:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 21:45</span>
          <span class="news-item-title">2026年“兴边富民助力高质量发展”网评引导活动在南宁启动</span>
          <span class="news-value-point">💡 中新网南宁11月24日电 (林浩 刘越 俞靖)11月24日，2026年“兴边富民助力高质量发展”网评引导活动在广西南宁市正式启动</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-24/10737228.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社甘肃酒泉11月24日电 题：大鹏一日同风起：巴基斯坦航天员酒泉吟古诗赢得掌声" data-title="大鹏一日同风起：巴基斯坦航天员酒泉吟古诗赢得掌声" data-date="11-24 21:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 21:42</span>
          <span class="news-item-title">大鹏一日同风起：巴基斯坦航天员酒泉吟古诗赢得掌声</span>
          <span class="news-value-point">💡 中新社甘肃酒泉11月24日电 题：大鹏一日同风起：巴基斯坦航天员酒泉吟古诗赢得掌声</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-24/10737219.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社甘肃酒泉11月24日电 题：从儿时日记本到“天宫”：一位巴基斯坦航天员的逐梦之旅" data-title="从儿时日记本到“天宫”：一位巴基斯坦航天员的逐梦之旅" data-date="11-24 20:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 20:53</span>
          <span class="news-item-title">从儿时日记本到“天宫”：一位巴基斯坦航天员的逐梦之旅</span>
          <span class="news-value-point">💡 中新社甘肃酒泉11月24日电 题：从儿时日记本到“天宫”：一位巴基斯坦航天员的逐梦之旅</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-25/10737278.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新社吉隆坡11月24日电 (记者 刘育英)马来西亚数字部部长戈宾德·辛格·德奥24日在国会下议院表示，政府高度重视儿童对人工智能(AI)陪伴类应用及互动聊天机器人产生情感依赖可能带来的风险，正研究相关保护措施，包括为陷入情绪困扰的用户提供援助机制。" data-title="马来西亚拟加强AI陪伴类应用监管" data-date="11-25 06:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-25 06:21</span>
          <span class="news-item-title">马来西亚拟加强AI陪伴类应用监管</span>
          <span class="news-value-point">💡 中新社吉隆坡11月24日电 (记者 刘育英)马来西亚数字部部长戈宾德·辛格·德奥24日在国会下议院表示，政府高度重视儿童对人工智能(AI)陪伴类…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/24/us/politics/nvidia-justice-department-todd-blanche.html" target="_blank" rel="noopener" data-cat="keji" data-summary="The remarks came even as Justice Department investigators have gathered evidence of Nvidia’s high-powered computer chips being illegally diverted by other firms to China, according to people familiar with the inquiries." data-title="Blanche Downplays Questions Over Nvidia as Company’s Customers Come Under Scrutiny" data-date="11-25 06:02" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-25 06:02</span>
          <span class="news-item-title">Blanche Downplays Questions Over Nvidia as Company’s Customers Come Under Scrutiny</span>
          <span class="news-value-point">💡 The remarks came even as Justice Department investigators have gathered …</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/24/in-all-hands-meeting-jensen-huang-thanks-white-house-and-says-hes-in-therapy/" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达创始人周二向员工道歉，并表示感谢大家给他第二次领导公司的机会。" data-title="In all-hands meeting, Jensen Huang thanks White House and says he’s in therapy" data-date="11-25 05:48" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-25 05:48</span>
          <span class="news-item-title">在全体员工大会上，黄仁勋感谢白宫，并表示他正在接受心理治疗</span>
          <span class="news-item-title-en">In all-hands meeting, Jensen Huang thanks White House and says he’s in therapy</span>
          <span class="news-value-point">💡 英伟达创始人周二向员工道歉，并表示感谢大家给他第二次领导公司的机会</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/24/technology/jensen-huang-apology-nvidia-ceo.html" target="_blank" rel="noopener" data-cat="keji" data-summary="A day after returning to his company, Mr. Huang acknowledged that he had violated Nvidia’s code of conduct and “made some terrible mistakes.”" data-title="Jensen Huang Apologizes to Nvidia Employees, Says He Is in Therapy" data-date="11-25 05:46" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-25 05:46</span>
          <span class="news-item-title">黄仁勋向英伟达员工道歉，并表示自己正在接受心理治疗</span>
          <span class="news-item-title-en">Jensen Huang Apologizes to Nvidia Employees, Says He Is in Therapy</span>
          <span class="news-value-point">💡 A day after returning to his company, Mr. Huang acknowledged that he had…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/24/even-the-best-ai-agents-struggle-with-everyday-life/" target="_blank" rel="noopener" data-cat="keji" data-summary="随着数以百万计的人开始使用个人人工智能助手，一项新的基准测试表明，即使是最先进的人工智能模型，在不引入潜在新问题的情况下，也很难可靠、安全地完成日常任务。" data-title="Even the best AI agents struggle with everyday life" data-date="11-25 05:33" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-25 05:33</span>
          <span class="news-item-title">即使是最好的 AI 代理也难以应对日常生活</span>
          <span class="news-item-title-en">Even the best AI agents struggle with everyday life</span>
          <span class="news-value-point">💡 随着数以百万计的人开始使用个人人工智能助手，一项新的基准测试表明，即使是最先进的人工智能模型，在不引入潜在新问题的情况下，也很难可靠、安全地完成…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/24/walmart-teams-up-with-meta-to-bring-black-friday-deals-to-ai-agent-muse/" target="_blank" rel="noopener" data-cat="keji" data-summary="沃尔玛现在允许顾客通过Meta的AI代理Muse选购黑色星期五特惠商品。" data-title="Walmart teams up with Meta to bring Black Friday deals to AI agent Muse" data-date="11-25 05:32" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-25 05:32</span>
          <span class="news-item-title">沃尔玛与Meta合作，将黑色星期五优惠带到AI代理Muse</span>
          <span class="news-item-title-en">Walmart teams up with Meta to bring Black Friday deals to AI agent Muse</span>
          <span class="news-value-point">💡 沃尔玛现在允许顾客通过Meta的AI代理Muse选购黑色星期五特惠商品</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/24/maple-raises-5-3m-to-build-ai-products-that-protect-your-data-even-from-itself/" target="_blank" rel="noopener" data-cat="keji" data-summary="该初创公司的加密人工智能架构旨在防止即使是公司本身也无法访问用户的私有数据。" data-title="Maple raises $5.3M to build AI products that protect your data, even from itself" data-date="11-25 05:19" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-25 05:19</span>
          <span class="news-item-title">Maple筹集530万美元，用于开发能够保护您的数据（甚至免受AI自身侵害）的AI产品</span>
          <span class="news-item-title-en">Maple raises $5.3M to build AI products that protect your data, even from itself</span>
          <span class="news-value-point">💡 该初创公司的加密人工智能架构旨在防止即使是公司本身也无法访问用户的私有数据</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/24/business/stocks-sp500-huang-nvidia.html" target="_blank" rel="noopener" data-cat="keji" data-summary="受英伟达的戏剧性事件以及Anthropic在轰动一时的首次公开募股之后的股价涨跌的影响，股票价格数日来大幅波动。" data-title="Stock Markets Slip as Nvidia and A.I. Stocks Erase Some of Monday’s Rally" data-date="11-25 05:12" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-25 05:12</span>
          <span class="news-item-title">英伟达和人工智能股抹去周一的部分涨幅，股市走低</span>
          <span class="news-item-title-en">Stock Markets Slip as Nvidia and A.I. Stocks Erase Some of Monday’s Rally</span>
          <span class="news-value-point">💡 受英伟达的戏剧性事件以及Anthropic在轰动一时的首次公开募股之后的股价涨跌的影响，股票价格数日来大幅波动</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/frontier-ai-employees-alarmed-that-unseen-open-ai-and-anthropic-models-are-too-powerful-to-release-report-claims-worry-spreads-that-executives-are-out-of-touch-with-severity-of-risks-will-choose-profit-over-safety" target="_blank" rel="noopener" data-cat="keji" data-summary="研究人员仍在寻找遏制和控制未发布模型的方法，但一位消息人士表示，这些模型能够成功地欺骗人类测试人员。" data-title="Frontier AI employees alarmed that unseen Open AI and Anthropic models are too powerful to release, report claims" data-date="11-25 05:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-25 05:00</span>
          <span class="news-item-title">据报道，Frontier AI的员工担心未公开的Open AI和Anthropic模型过于强大，不宜发布。</span>
          <span class="news-item-title-en">Frontier AI employees alarmed that unseen Open AI and Anthropic models are too powerful to release, report claims</span>
          <span class="news-value-point">💡 研究人员仍在寻找遏制和控制未发布模型的方法，但一位消息人士表示，这些模型能够成功地欺骗人类测试人员</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1041571/jensen-huang-all-hands-nvidia-apology" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道，Nvidia首席执行官黄仁勋在重返公司后的第一次全体员工大会上向员工道歉，同时试图撇清白宫和科技界领袖帮助他重返岗位的说法。" data-title="Jensen Huang reportedly tells Nvidia staff it’s ‘not true’ Trump got him rehired" data-date="11-25 04:02" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-25 04:02</span>
          <span class="news-item-title">据报道，黄仁勋告诉英伟达员工，特朗普让他重返董事会“并非事实”</span>
          <span class="news-item-title-en">Jensen Huang reportedly tells Nvidia staff it’s ‘not true’ Trump got him rehired</span>
          <span class="news-value-point">💡 据报道，Nvidia首席执行官黄仁勋在重返公司后的第一次全体员工大会上向员工道歉，同时试图撇清白宫和科技界领袖帮助他重返岗位的说法</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/24/business/economy/trump-nvidia-national-security-us-economics.html" target="_blank" rel="noopener" data-cat="keji" data-summary="在他之前的历任总统都在国家危难之际出手拯救过企业。特朗普走得更远：他将美国的命运押在一个受宠的首席执行官身上。" data-title="Trump’s Nvidia Push Shows Companies’ Importance in Global Economic War" data-date="11-25 03:54" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-25 03:54</span>
          <span class="news-item-title">特朗普对英伟达的施压表明了企业在全球经济战中的重要性</span>
          <span class="news-item-title-en">Trump’s Nvidia Push Shows Companies’ Importance in Global Economic War</span>
          <span class="news-value-point">💡 在他之前的历任总统都在国家危难之际出手拯救过企业</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/air-cooling/legendary-cooler-master-hyper-212-halo-cpu-air-cooler-drops-to-an-all-time-low-of-usd15-keep-your-amd-or-intel-processor-running-cool-on-the-cheap" target="_blank" rel="noopener" data-cat="keji" data-summary="酷冷至尊的Hyper 212 Halo风冷散热器正在以15美元的特价出售，使其成为目前市面上最实惠的知名品牌塔式CPU散热器之一。" data-title="Legendary Cooler Master Hyper 212 Halo CPU air cooler drops to an all-time low of $15  — keep your AMD or Intel processor running cool on the cheap" data-date="11-25 02:53" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-25 02:53</span>
          <span class="news-item-title">传奇的酷冷至尊Hyper 212 Halo CPU风冷散热器降至历史最低价15美元——以实惠的价格让您的AMD或英特尔处理器保持低温运行</span>
          <span class="news-item-title-en">Legendary Cooler Master Hyper 212 Halo CPU air cooler drops to an all-time low of $15  — keep your AMD or Intel processor running cool on the cheap</span>
          <span class="news-value-point">💡 酷冷至尊的Hyper 212 Halo风冷散热器正在以15美元的特价出售，使其成为目前市面上最实惠的知名品牌塔式CPU散热器之一</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/24/anthropic-shares-fall-below-ipo-price-a-worrying-sign-for-ai-startups/" target="_blank" rel="noopener" data-cat="keji" data-summary="Anthropic上市后的股价暴跌可能会对人工智能初创企业的估值造成压力。" data-title="Anthropic shares fall below IPO price, a worrying sign for AI startups" data-date="11-25 02:30" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-25 02:30</span>
          <span class="news-item-title">Anthropic股价跌破IPO价格，这对人工智能初创企业来说是一个令人担忧的信号</span>
          <span class="news-item-title-en">Anthropic shares fall below IPO price, a worrying sign for AI startups</span>
          <span class="news-value-point">💡 Anthropic上市后的股价暴跌可能会对人工智能初创企业的估值造成压力</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/24/uk-warns-ai-driven-cyberattacks-are-exposing-years-of-weak-security/" target="_blank" rel="noopener" data-cat="keji" data-summary="英国网络安全机构表示，“奠定坚实的基础从未像现在这样重要”，因为人工智能黑客工具依赖于利用简单的安全漏洞。" data-title="UK warns AI-driven cyberattacks are exposing years of weak security" data-date="11-25 02:02" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-25 02:02</span>
          <span class="news-item-title">英国警告称，由人工智能驱动的网络攻击正揭示多年来存在的安全漏洞</span>
          <span class="news-item-title-en">UK warns AI-driven cyberattacks are exposing years of weak security</span>
          <span class="news-value-point">💡 英国网络安全机构表示，“奠定坚实的基础从未像现在这样重要”，因为人工智能黑客工具依赖于利用简单的安全漏洞</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/entertainment/1041362/tidal-ai-music-ban" target="_blank" rel="noopener" data-cat="keji" data-summary="Tidal将于12月9日正式禁止人工智能生成的音乐。Tidal音乐负责人罗伯特·安德森（Robert Andersen）表示，由于这一变化，Tidal将删除约2900万首由人工智能生成的歌曲，并每天拒绝约8万至8.5万首曲目。" data-title="Tidal will start banning AI-generated music next month" data-date="11-25 01:17" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-25 01:17</span>
          <span class="news-item-title">Tidal将于下月开始禁止人工智能生成的音乐</span>
          <span class="news-item-title-en">Tidal will start banning AI-generated music next month</span>
          <span class="news-value-point">💡 Tidal将于12月9日正式禁止人工智能生成的音乐</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqzr5ylmeerlo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联和毛里西奥·波切蒂诺对VAR裁判约翰·布鲁克斯和裁判主管霍华德·韦伯处理莱尼·约罗红牌的方式感到愤怒。" data-title="Pochettino leads Man Utd fury at Yoro red card ruling" data-date="11-25 06:05" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-25 06:05</span>
          <span class="news-item-title">波切蒂诺带头对尤罗的红牌判罚表示不满</span>
          <span class="news-item-title-en">Pochettino leads Man Utd fury at Yoro red card ruling</span>
          <span class="news-value-point">💡 曼联和毛里西奥·波切蒂诺对VAR裁判约翰·布鲁克斯和裁判主管霍华德·韦伯处理莱尼·约罗红牌的方式感到愤怒</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13616134/mauricio-pochettino-man-utd-boss-fumes-at-var-in-liverpool-loss-over-leny-yoro-and-dominik-szoboszlai-calls" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在曼联输给利物浦的比赛中，莱尼·约罗的红牌被撤销，毛里西奥·波切蒂诺对此严厉批评了VAR。这位阿根廷人认为，多米尼克·索博斯洛伊的开场进球本不应算作有效。" data-title="Poch fumes at Yoro red and thinks Szoboszlai goal shouldn&#39;t have stood" data-date="11-25 05:50" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 05:50</span>
          <span class="news-item-title">波切蒂诺对约罗的红牌感到愤怒，并认为索博斯洛伊的进球不应有效</span>
          <span class="news-item-title-en">Poch fumes at Yoro red and thinks Szoboszlai goal shouldn't have stood</span>
          <span class="news-value-point">💡 在曼联输给利物浦的比赛中，莱尼·约罗的红牌被撤销，毛里西奥·波切蒂诺对此严厉批评了VAR</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13616134/mauricio-pochettino-man-utd-boss-fumes-at-var-in-liverpool-loss-over-leny-yoro-and-dominik-szoboszlai-calls" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在曼联输给利物浦的比赛中，莱尼·约罗的红牌被撤销，毛里西奥·波切蒂诺对此严厉批评了VAR。这位阿根廷人认为，多米尼克·索博斯洛伊的开场进球本不应算作有效。" data-title="Poch fumes at Yoro red and thinks Szoboszlai goal shouldn&#39;t have stood" data-date="11-25 05:50" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 05:50</span>
          <span class="news-item-title">波切蒂诺对约罗的红牌感到愤怒，并认为索博斯洛伊的进球不应有效</span>
          <span class="news-item-title-en">Poch fumes at Yoro red and thinks Szoboszlai goal shouldn't have stood</span>
          <span class="news-value-point">💡 在曼联输给利物浦的比赛中，莱尼·约罗的红牌被撤销，毛里西奥·波切蒂诺对此严厉批评了VAR</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/hibernian-vs-dundee/report/558401" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="希伯尼安在伊斯特路球场以 2-1 战胜邓迪，结束了其在英超主场胜利的漫长等待。" data-title="Hibernian finally register home win after battling past Dundee" data-date="11-25 05:35" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 05:35</span>
          <span class="news-item-title">希伯尼安在与邓迪的苦战后终于取得主场胜利</span>
          <span class="news-item-title-en">Hibernian finally register home win after battling past Dundee</span>
          <span class="news-value-point">💡 希伯尼安在伊斯特路球场以 2-1 战胜邓迪，结束了其在英超主场胜利的漫长等待</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/norwich-city-vs-queens-park-rangers/report/560694" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="随着女王公园巡游者队在卡罗路球场与诺维奇队战成 1-1 平局，诺维奇队令人瞩目的连胜势头戛然而止。" data-title="Norwich hit back to hold QPR" data-date="11-25 05:35" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 05:35</span>
          <span class="news-item-title">诺维奇扳平比分，逼平女王公园巡游者队</span>
          <span class="news-item-title-en">Norwich hit back to hold QPR</span>
          <span class="news-value-point">💡 随着女王公园巡游者队在卡罗路球场与诺维奇队战成 1-1 平局，诺维奇队令人瞩目的连胜势头戛然而止</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/wolverhampton-wanderers-vs-derby-county/report/560697" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="亚当·阿姆斯特朗梅开二度，在六场比赛中攻入六球，帮助势不可挡的狼队在莫利纽球场举行的英冠联赛中以 3-0 战胜德比郡。" data-title="Armstrong nets twice in Wolves win" data-date="11-25 05:35" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 05:35</span>
          <span class="news-item-title">阿姆斯特朗梅开二度，帮助狼队取胜</span>
          <span class="news-item-title-en">Armstrong nets twice in Wolves win</span>
          <span class="news-value-point">💡 亚当·阿姆斯特朗梅开二度，在六场比赛中攻入六球，帮助势不可挡的狼队在莫利纽球场举行的英冠联赛中以 3-0 战胜德比郡</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/sheffield-united-vs-southampton/report/560696" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Sydie Peck equalised in the 90th minute as Sheffield United came from behind to secure a 1-1 Championship draw with Southampton at Bramall Lane." data-title="Southampton held at Sheffield United" data-date="11-25 05:35" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 05:35</span>
          <span class="news-item-title">Southampton held at Sheffield United</span>
          <span class="news-value-point">💡 Sydie Peck equalised in the 90th minute as Sheffield United came from be…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/galatasaray-vs-aston-villa/report/577673" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Aston Villa&#39;s winless run extended to six games as a late Deniz Gul&#39;s header saw them beaten 1-0 by Galatasaray in the Champions League league phase." data-title="Villa beaten late on at Galatasaray as winless run continues" data-date="11-25 03:40" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 03:40</span>
          <span class="news-item-title">维拉在比赛后期被加拉塔萨雷击败，不胜纪录仍在延续</span>
          <span class="news-item-title-en">Villa beaten late on at Galatasaray as winless run continues</span>
          <span class="news-value-point">💡 Aston Villa's winless run extended to six games as a late Deniz Gul's he…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/arsenal-vs-borussia-dortmund/live/577669" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Saliba only on bench as Kepa replaces Raya against Dortmund LIVE!" data-title="Saliba only on bench as Kepa replaces Raya against Dortmund LIVE!" data-date="11-25 02:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 02:00</span>
          <span class="news-item-title">对阵多特蒙德的比赛中，萨利巴只能坐板凳，凯帕将替补拉亚上场，敬请观看直播！</span>
          <span class="news-item-title-en">Saliba only on bench as Kepa replaces Raya against Dortmund LIVE!</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13616062/explained-how-did-manchester-united-successfully-appeal-leny-yoros-red-card-picked-up-against-liverpool" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育新闻的卡韦·索尔赫科尔（Kaveh Solhekol）解释了曼联就莱尼·约罗（Leny Yoro）的红牌成功上诉的过程，该后卫是在对阵利物浦的比赛中吃到红牌的。" data-title="Man Utd&#39;s Yoro red card appeal process explained" data-date="11-25 01:16" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 01:16</span>
          <span class="news-item-title">曼联对约罗红牌的上诉流程详解</span>
          <span class="news-item-title-en">Man Utd's Yoro red card appeal process explained</span>
          <span class="news-value-point">💡 天空体育新闻的卡韦·索尔赫科尔（Kaveh Solhekol）解释了曼联就莱尼·约罗（Leny Yoro）的红牌成功上诉的过程，该后卫是在对阵利…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13616058/jurrien-timbers-shirt-pull-on-alexander-isak-ref-chief-howard-webb-admits-quick-check-in-arsenals-win-at-liverpool" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在阿森纳在安菲尔德球场获胜的比赛中，阿森纳后卫尤里恩·廷伯（Jurrien Timber）拉扯利物浦前锋亚历山大·伊萨克（Alexander Isak）的球衣却未受处罚，裁判长霍华德·韦伯（Howard Webb）承认，视频助理裁判（VAR）对此进行了“快速检查”。" data-title="How &#39;quick check&#39; and unseen angle saw Timber&#39;s Isak shirt" data-date="11-25 01:13" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 01:13</span>
          <span class="news-item-title">“快速检查”和隐蔽视角如何发现了Timber的Isak衬衫</span>
          <span class="news-item-title-en">How 'quick check' and unseen angle saw Timber's Isak shirt</span>
          <span class="news-value-point">💡 在阿森纳在安菲尔德球场获胜的比赛中，阿森纳后卫尤里恩·廷伯（Jurrien Timber）拉扯利物浦前锋亚历山大·伊萨克（Alexander I…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13616058/jurrien-timbers-shirt-pull-on-alexander-isak-ref-chief-howard-webb-admits-quick-check-in-arsenals-win-at-liverpool" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在阿森纳在安菲尔德球场获胜的比赛中，阿森纳后卫尤里恩·廷伯（Jurrien Timber）拉扯利物浦前锋亚历山大·伊萨克（Alexander Isak）的球衣却未受处罚，裁判长霍华德·韦伯（Howard Webb）承认，视频助理裁判（VAR）对此进行了“快速检查”。" data-title="How &#39;quick check&#39; and unseen angle saw Timber&#39;s Isak shirt" data-date="11-25 01:13" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 01:13</span>
          <span class="news-item-title">“快速检查”和隐蔽视角如何发现了Timber的Isak衬衫</span>
          <span class="news-item-title-en">How 'quick check' and unseen angle saw Timber's Isak shirt</span>
          <span class="news-value-point">💡 在阿森纳在安菲尔德球场获胜的比赛中，阿森纳后卫尤里恩·廷伯（Jurrien Timber）拉扯利物浦前锋亚历山大·伊萨克（Alexander I…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ck868g93djl5o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联后卫莱尼·约罗（Leny Yoro）周六将出战布伦特福德，因为他在安菲尔德球场的红牌被撤销。" data-title="Yoro red card overturned, but refs&#39; chief Webb backs decision" data-date="11-25 01:00" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-25 01:00</span>
          <span class="news-item-title">约罗的红牌被撤销，但裁判长韦伯支持原判</span>
          <span class="news-item-title-en">Yoro red card overturned, but refs' chief Webb backs decision</span>
          <span class="news-value-point">💡 曼联后卫莱尼·约罗（Leny Yoro）周六将出战布伦特福德，因为他在安菲尔德球场的红牌被撤销</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13616033/leny-yoro-red-card-ref-chief-howard-webb-backs-process-that-saw-man-utd-defender-sent-off-at-liverpool" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="尽管红牌在上诉后被撤销，但裁判长霍华德·韦伯（Howard Webb）仍支持裁判在利物浦对阵曼联的比赛中将曼联后卫莱尼·约罗（Leny Yoro）罚下的决定。" data-title="Ref chief Webb backs process around Yoro sending off despite successful appeal" data-date="11-25 01:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 01:00</span>
          <span class="news-item-title">尽管上诉成功，但裁判长韦伯仍支持对约罗的红牌判罚过程</span>
          <span class="news-item-title-en">Ref chief Webb backs process around Yoro sending off despite successful appeal</span>
          <span class="news-value-point">💡 尽管红牌在上诉后被撤销，但裁判长霍华德·韦伯（Howard Webb）仍支持裁判在利物浦对阵曼联的比赛中将曼联后卫莱尼·约罗（Leny Yoro…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13616021/leny-yoros-red-card-for-manchester-united-against-liverpool-overturned-following-successful-appeal" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在曼联成功上诉后，莱尼·约罗在对阵利物浦的比赛中领到的红牌被撤销。" data-title="Yoro red card overturned after successful Man Utd appeal" data-date="11-25 01:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 01:00</span>
          <span class="news-item-title">曼联上诉成功，约罗的红牌被撤销</span>
          <span class="news-item-title-en">Yoro red card overturned after successful Man Utd appeal</span>
          <span class="news-value-point">💡 在曼联成功上诉后，莱尼·约罗在对阵利物浦的比赛中领到的红牌被撤销</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://techcrunch.com/2026/11/24/jensen-huang-still-thinks-a-succession-plan-creates-unnecessary-hierarchy/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="对于一家在过去两周一直在摸索没有创始人会发生什么情况的公司来说，这是一个非同寻常的立场。" data-title="Jensen Huang still thinks a succession plan creates unnecessary hierarchy" data-date="11-25 06:27" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-25 06:27</span>
          <span class="news-item-title">黄仁勋仍然认为继任计划会造成不必要的层级关系</span>
          <span class="news-item-title-en">Jensen Huang still thinks a succession plan creates unnecessary hierarchy</span>
          <span class="news-value-point">💡 对于一家在过去两周一直在摸索没有创始人会发生什么情况的公司来说，这是一个非同寻常的立场</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/21/climate/what-to-know-about-the-planned-explosion-in-iowa.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="陆军官员周二表示，陆军计划于周三上午在爱荷华州东南部的一处设施引爆一批正在危险地变质的爆炸物。" data-title="What to Know About the Planned Explosion in Middletown, Iowa" data-date="11-25 06:08" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-25 06:08</span>
          <span class="news-item-title">关于爱荷华州米德尔敦计划性爆炸的须知事项</span>
          <span class="news-item-title-en">What to Know About the Planned Explosion in Middletown, Iowa</span>
          <span class="news-value-point">💡 陆军官员周二表示，陆军计划于周三上午在爱荷华州东南部的一处设施引爆一批正在危险地变质的爆炸物</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/news/1041690/grand-theft-auto-6-pc-recompilation-project-leonida-takedown-take-two" target="_blank" rel="noopener" data-cat="zonghe" data-summary="游戏MOD社区正在争先恐后地让《侠盗猎车手6》在PC上运行，但今天Take-Two下架了一个重磅作品。15岁“NotRexed”的粉丝项目Leonida在收到《GTA VI》发行商的DMCA下架通知后已消失。" data-title="GTA VI PC recompilation project shut down by Take" data-date="11-25 05:39" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-25 05:39</span>
          <span class="news-item-title">《GTA VI》PC版重制项目被Take-Two叫停</span>
          <span class="news-item-title-en">GTA VI PC recompilation project shut down by Take</span>
          <span class="news-value-point">💡 游戏MOD社区正在争先恐后地让《侠盗猎车手6》在PC上运行，但今天Take-Two下架了一个重磅作品</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/laptops/gaming-laptops/best-gaming-laptop-deals-dell-msi-alienware-rog" target="_blank" rel="noopener" data-cat="zonghe" data-summary="以下是黑色星期五最超值的游戏笔记本电脑优惠。我们会不断更新此清单，列出所有主要零售商仍在提供的超值优惠。" data-title="Best Black Friday gaming laptop PC deals 2026" data-date="11-25 05:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-25 05:30</span>
          <span class="news-item-title">2026年黑色星期五最佳游戏笔记本电脑优惠</span>
          <span class="news-item-title-en">Best Black Friday gaming laptop PC deals 2026</span>
          <span class="news-value-point">💡 以下是黑色星期五最超值的游戏笔记本电脑优惠</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/24/climate/iowa-army-ammunition-plant-explostion.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Freezing temperatures threaten to make the chemicals even more unstable, while winds could carry a toxic lead plume up to 100 miles away." data-title="Army’s Iowa Ammunition Plant Explosion on Schedule for Wednesday Morning" data-date="11-25 05:13" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-25 05:13</span>
          <span class="news-item-title">陆军爱荷华州弹药厂爆炸按计划将于周三上午发生</span>
          <span class="news-item-title-en">Army’s Iowa Ammunition Plant Explosion on Schedule for Wednesday Morning</span>
          <span class="news-value-point">💡 Freezing temperatures threaten to make the chemicals even more unstable,…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1021621/best-gifts-for-mom-2026" target="_blank" rel="noopener" data-cat="zonghe" data-summary="考虑到妈妈为我们所做的一切，在节日期间回馈她们是一种很好的感觉。但该从哪里开始呢？您如何用实物来表达您对生活中这样一个关键且有影响力的人物的情感？选择似乎无穷无尽。" data-title="The Verge’s 2026 holiday gift guide for moms" data-date="11-25 05:09" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-25 05:09</span>
          <span class="news-item-title">The Verge 2026年送给妈妈的节日礼物指南</span>
          <span class="news-item-title-en">The Verge’s 2026 holiday gift guide for moms</span>
          <span class="news-value-point">💡 考虑到妈妈为我们所做的一切，在节日期间回馈她们是一种很好的感觉</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/laptops/macbooks/512gb-macbook-neo-drops-to-usd699-comes-with-touch-id-but-only-in-pink" target="_blank" rel="noopener" data-cat="zonghe" data-summary="苹果的 MacBook Neo 搭载 512GB 存储空间和 Touch ID，在亚马逊上的售价为 699 美元。" data-title="512GB MacBook Neo drops to $699 — comes with Touch ID, but only in pink" data-date="11-25 04:36" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-25 04:36</span>
          <span class="news-item-title">512GB MacBook Neo降至699美元——配备Touch ID，但仅有粉色款</span>
          <span class="news-item-title-en">512GB MacBook Neo drops to $699 — comes with Touch ID, but only in pink</span>
          <span class="news-value-point">💡 苹果的 MacBook Neo 搭载 512GB 存储空间和 Touch ID，在亚马逊上的售价为 699 美元</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1041618/tiktok-down-outage" target="_blank" rel="noopener" data-cat="zonghe" data-summary="周二早些时候，TikTok 出现了一些问题，视频、搜索结果、收藏夹和其他功能无法像往常一样加载。有时，视频无法在我的iPhone上的“为你推荐”动态中加载，搜索结果也偶尔不会显示。" data-title="TikTok was down" data-date="11-25 04:27" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-25 04:27</span>
          <span class="news-item-title">TikTok 曾出现故障</span>
          <span class="news-item-title-en">TikTok was down</span>
          <span class="news-value-point">💡 周二早些时候，TikTok 出现了一些问题，视频、搜索结果、收藏夹和其他功能无法像往常一样加载</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/24/upshot/midterm-elections-upsets-predictions.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="We found the most unlikely winners of the 2026 midterms." data-title="The Mississippi Senate Race Wasn’t Even This Year’s Biggest Upset" data-date="11-25 04:19" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-25 04:19</span>
          <span class="news-item-title">The Mississippi Senate Race Wasn’t Even This Year’s Biggest Upset</span>
          <span class="news-value-point">💡 We found the most unlikely winners of the 2026 midterms.</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/networking/routers/tp-links-archer-be770-tri-band-wi-fi-7-router-is-usd120-off-10-gbps-lan-ports-and-blazing-fast-wireless-speeds-for-usd280" target="_blank" rel="noopener" data-cat="zonghe" data-summary="TP-Link Archer BE770 三频 Wi-Fi 7 路由器降至 280 美元的低价" data-title="TP-Link&#39;s Archer 770 tri-band Wi-Fi 7 router is $120 off" data-date="11-25 04:10" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-25 04:10</span>
          <span class="news-item-title">TP-Link的Archer 770三频Wi-Fi 7路由器立减120美元</span>
          <span class="news-item-title-en">TP-Link's Archer 770 tri-band Wi-Fi 7 router is $120 off</span>
          <span class="news-value-point">💡 TP-Link Archer BE770 三频 Wi-Fi 7 路由器降至 280 美元的低价</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/rugby-union/news/12040/13616108/ireland-captain-dan-sheehan-to-miss-nations-championship-finale-after-two-game-ban-for-red-card-against-south-africa" target="_blank" rel="noopener" data-cat="zonghe" data-summary="爱尔兰队长丹·希恩（Dan Sheehan）因在对阵南非的比赛中被出示红牌而遭两场禁赛，因此将缺席周五与澳大利亚的国际橄榄球联盟锦标赛第五名争夺战。" data-title="Sheehan to miss Ireland&#39;s Nations Championship finale after two" data-date="11-25 03:55" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 03:55</span>
          <span class="news-item-title">希恩将缺席爱尔兰国家锦标赛决赛两场</span>
          <span class="news-item-title-en">Sheehan to miss Ireland's Nations Championship finale after two</span>
          <span class="news-value-point">💡 爱尔兰队长丹·希恩（Dan Sheehan）因在对阵南非的比赛中被出示红牌而遭两场禁赛，因此将缺席周五与澳大利亚的国际橄榄球联盟锦标赛第五名争夺…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/ram/these-are-the-four-cheapest-32gb-ddr5-memory-kits-weve-found-save-up-to-usd110-on-kits-available-from-patriot-team-group-and-v-color-up-to-ddr5-6400" target="_blank" rel="noopener" data-cat="zonghe" data-summary="DDR5 的价格仍然很高，但我们找到了目前最便宜的四个 DDR5 套件。" data-title="These are the four cheapest 32GB DDR5 memory kits we’ve found" data-date="11-25 03:50" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-25 03:50</span>
          <span class="news-item-title">以下是我们找到的四款最便宜的 32GB DDR5 内存套装</span>
          <span class="news-item-title-en">These are the four cheapest 32GB DDR5 memory kits we’ve found</span>
          <span class="news-value-point">💡 DDR5 的价格仍然很高，但我们找到了目前最便宜的四个 DDR5 套件</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/rtx-5090-equipped-asus-rog-strix-scar-16-laptop-is-usd350-off-snag-a-great-deal-on-a-ridiculously-powerful-2025-model-16-inch-gaming-laptop-with-32gb-of-ram-and-core-ultra-9-275hx-processor-for-only-usd4-149" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Newegg 现正以 4149 美元的价格出售搭载 RTX 5090 的华硕 ROG Strix SCAR 16，优惠 350 美元，这是本周我们看到的搭载 5090 的笔记本电脑中价格最低的之一。" data-title="RTX 5090-equipped Asus ROG Strix SCAR 16 laptop is $350 off" data-date="11-25 03:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-25 03:30</span>
          <span class="news-item-title">搭载RTX 5090的华硕ROG Strix SCAR 16笔记本电脑立减350美元</span>
          <span class="news-item-title-en">RTX 5090-equipped Asus ROG Strix SCAR 16 laptop is $350 off</span>
          <span class="news-value-point">💡 Newegg 现正以 4149 美元的价格出售搭载 RTX 5090 的华硕 ROG Strix SCAR 16，优惠 350 美元，这是本周我…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/3d-printing/anycubics-black-friday-3d-printers-sale-slashes-up-to-usd350-off-a-brand-new-printer-massive-discounts-available-on-the-most-popular-models" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Anycubic的3D打印机系列在Amazon Prime Big Deal Days促销中获得大幅折扣" data-title="Anycubic&#39;s Black Friday 3D Printers sale slashes up to $350 off a brand new printer" data-date="11-25 03:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-25 03:00</span>
          <span class="news-item-title">Anycubic黑色星期五3D打印机促销活动，全新打印机最高立减350美元</span>
          <span class="news-item-title-en">Anycubic's Black Friday 3D Printers sale slashes up to $350 off a brand new printer</span>
          <span class="news-value-point">💡 Anycubic的3D打印机系列在Amazon Prime Big Deal Days促销中获得大幅折扣</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1040046/apple-tv-subscription-streaming-sale-deal-black-friday" target="_blank" rel="noopener" data-cat="zonghe" data-summary="流媒体优惠不再像以前那样多，但如果您知道在哪里找，仍然可以找到。其中一个吸引我们注意的是针对美国亚马逊账户持有者的Apple TV优惠。苹果的流媒体服务通常每月收费 14.99 美元。" data-title="Amazon is knocking almost $50 off six months of Apple TV" data-date="11-25 03:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-25 03:00</span>
          <span class="news-item-title">亚马逊为苹果电视六个月的订阅服务提供近50美元的折扣</span>
          <span class="news-item-title-en">Amazon is knocking almost $50 off six months of Apple TV</span>
          <span class="news-value-point">💡 流媒体优惠不再像以前那样多，但如果您知道在哪里找，仍然可以找到</span>
        </a>
  </div>
</div>
<script defer src="{{ "/assets/js/news-feed.js" | relative_url }}"></script>


<p class="news-updated">🕐 抓取更新于 2026-11-25 06:38（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
