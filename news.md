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
      <span>2026-11-25 03:00 抓取更新</span>
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
        <span class="channel-count">58</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('shizheng', this)">
        <span>🏛️ 时政与国际</span>
        <span class="channel-count">13</span>
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
  <div class="ov-item"><span class="ov-num">58</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">4</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">天空体育×15 · 中国新闻网×11</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">按来源聚合 · 最近 24 小时精选</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.nytimes.com/2026/11/24/us/politics/tennessee-house-election-results-broderick-wins.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在一位技术支持人员在没有投放任何电视广告的情况下击败了一位连任八届的共和党议员后，民主党在中期选举中的大胜在众议院中继续扩大。" data-title="Broderick Wins Tennessee House Race, Giving Democrats Largest Majority in 30 Years" data-date="11-25 02:34" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 11-25 02:34</span>
      </div>
      <h2 class="hero-featured-title">布罗德里克赢得田纳西州众议院席位，使民主党获得30年来最多的多数席位</h2>
      <div class="hero-featured-title-en">Broderick Wins Tennessee House Race, Giving Democrats Largest Majority in 30 Years</div>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.tomshardware.com/pc-components/air-cooling/legendary-cooler-master-hyper-212-halo-cpu-air-cooler-drops-to-an-all-time-low-of-usd15-keep-your-amd-or-intel-processor-running-cool-on-the-cheap" target="_blank" rel="noopener" data-cat="keji" data-summary="酷冷至尊的Hyper 212 Halo风冷散热器正在以15美元的特价出售，使其成为目前市面上最实惠的知名品牌塔式CPU散热器之一。" data-title="Legendary Cooler Master Hyper 212 Halo CPU air cooler drops to an all-time low of $15  — keep your AMD or Intel processor running cool on the cheap" data-date="11-25 02:53" data-source="Tom's Hardware">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
      </div>
      <p class="hero-sub-title">传奇的酷冷至尊Hyper 212 Halo CPU风冷散热器降至历史最低价15美元——以实惠的价格让您的AMD或英特尔处理器保持低温运行</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/football/arsenal-vs-borussia-dortmund/live/577669" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Saliba only on bench as Kepa replaces Raya against Dortmund LIVE!" data-title="Saliba only on bench as Kepa replaces Raya against Dortmund LIVE!" data-date="11-25 02:00" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">对阵多特蒙德的比赛中，萨利巴只能坐板凳，凯帕将替补拉亚上场，敬请观看直播！</p>
    </a>
    <a class="hero-sub-card" href="https://www.theverge.com/gadgets/1040046/apple-tv-subscription-streaming-sale-deal-black-friday" target="_blank" rel="noopener" data-cat="zonghe" data-summary="流媒体优惠不再像以前那样多，但如果您知道在哪里找，仍然可以找到。其中一个吸引我们注意的是针对美国亚马逊账户持有者的Apple TV优惠。苹果的流媒体服务通常每月收费 14.99 美元。" data-title="Amazon is knocking almost $50 off six months of Apple TV" data-date="11-25 03:00" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">亚马逊为苹果电视六个月的订阅服务提供近50美元的折扣</p>
    </a>
  </div>
</div>
<div class="news-grid">
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🏛️</span>
      <span class="news-category-title">时政要闻 & 国际动态</span>
      <span class="news-category-count">13 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/11/24/us/politics/tennessee-house-election-results-broderick-wins.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在一位技术支持人员在没有投放任何电视广告的情况下击败了一位连任八届的共和党议员后，民主党在中期选举中的大胜在众议院中继续扩大。" data-title="Broderick Wins Tennessee House Race, Giving Democrats Largest Majority in 30 Years" data-date="11-25 02:34" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-25 02:34</span>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-24/10737183.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月24日电 据美国消费者新闻与商业频道(CNBC)当地时间23日播出的采访片段，美国总统特朗普透露，黄仁勋已向妻子洛丽道歉。" data-title="特朗普：黄仁勋已向妻子道歉，“她是一位非常优秀的女性”" data-date="11-24 20:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 20:26</span>
          <span class="news-item-title">特朗普：黄仁勋已向妻子道歉，“她是一位非常优秀的女性”</span>
          <span class="news-value-point">💡 中新网11月24日电 据美国消费者新闻与商业频道(CNBC)当地时间23日播出的采访片段，美国总统特朗普透露，黄仁勋已向妻子洛丽道歉</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-24/10737164.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月24日电 据路透社当地时间23日报道，美国国会参议院国土安全与政府事务委员会主席的民主党籍议员玛吉·哈桑已启动调查，要求副总统万斯提供相关文件，以调查其是否利用职务之便，帮助一名政治捐款人获得委内瑞拉石油销售业务。" data-title="“一场会面引发调查”？美国会民主党人着手调查万斯" data-date="11-24 19:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 19:49</span>
          <span class="news-item-title">“一场会面引发调查”？美国会民主党人着手调查万斯</span>
          <span class="news-value-point">💡 中新网11月24日电 据路透社当地时间23日报道，美国国会参议院国土安全与政府事务委员会主席的民主党籍议员玛吉·哈桑已启动调查，要求副总统万斯提…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-24/10737143.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="印度尼西亚万丹省警方24日证实，该省一家糖果厂21日发生的火灾已造成26人死亡，另有8人失踪。当地官员称，起火点可能是涉事建筑二楼的一台冷却装置。" data-title="印尼糖果厂火灾已致26人死亡 警方展开刑事调查" data-date="11-24 19:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 19:22</span>
          <span class="news-item-title">印尼糖果厂火灾已致26人死亡 警方展开刑事调查</span>
          <span class="news-value-point">💡 印度尼西亚万丹省警方24日证实，该省一家糖果厂21日发生的火灾已造成26人死亡，另有8人失踪</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/512343.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="2026年11月18日，中国深圳——APEC会议期间，比亚迪仰望U8正式交付巴布亚新几内亚市场" data-title="巴新总理见证，仰望U8交付巴布亚新几内亚市场" data-date="11-24 14:12" data-source="量子位">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-24 14:12</span>
          <span class="news-item-title">巴新总理见证，仰望U8交付巴布亚新几内亚市场</span>
          <span class="news-value-point">💡 2026年11月18日，中国深圳——APEC会议期间，比亚迪仰望U8正式交付巴布亚新几内亚市场</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/air-cooling/legendary-cooler-master-hyper-212-halo-cpu-air-cooler-drops-to-an-all-time-low-of-usd15-keep-your-amd-or-intel-processor-running-cool-on-the-cheap" target="_blank" rel="noopener" data-cat="keji" data-summary="酷冷至尊的Hyper 212 Halo风冷散热器正在以15美元的特价出售，使其成为目前市面上最实惠的知名品牌塔式CPU散热器之一。" data-title="Legendary Cooler Master Hyper 212 Halo CPU air cooler drops to an all-time low of $15  — keep your AMD or Intel processor running cool on the cheap" data-date="11-25 02:53" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-25 02:53</span>
          <span class="news-item-title">传奇的酷冷至尊Hyper 212 Halo CPU风冷散热器降至历史最低价15美元——以实惠的价格让您的AMD或英特尔处理器保持低温运行</span>
          <span class="news-item-title-en">Legendary Cooler Master Hyper 212 Halo CPU air cooler drops to an all-time low of $15  — keep your AMD or Intel processor running cool on the cheap</span>
          <span class="news-value-point">💡 酷冷至尊的Hyper 212 Halo风冷散热器正在以15美元的特价出售，使其成为目前市面上最实惠的知名品牌塔式CPU散热器之一</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/24/business/economy/trump-nvidia-national-security-us-economics.html" target="_blank" rel="noopener" data-cat="keji" data-summary="在他之前的历任总统都在国家危难之际出手拯救过企业。特朗普走得更远：他将美国的命运押在一个受宠的首席执行官身上。" data-title="Trump’s Nvidia Push Shows Companies’ Importance in Global Economic War" data-date="11-25 02:34" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-25 02:34</span>
          <span class="news-item-title">特朗普对英伟达的施压表明了企业在全球经济战中的重要性</span>
          <span class="news-item-title-en">Trump’s Nvidia Push Shows Companies’ Importance in Global Economic War</span>
          <span class="news-value-point">💡 在他之前的历任总统都在国家危难之际出手拯救过企业</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/24/technology/jensen-huang-apology-nvidia-ceo.html" target="_blank" rel="noopener" data-cat="keji" data-summary="回到公司一天后，黄先生承认自己违反了英伟达的行为准则，并“犯了一些严重的错误”。" data-title="Jensen Huang Apologizes to Nvidia Employees, Says He Is in Therapy" data-date="11-25 02:34" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-25 02:34</span>
          <span class="news-item-title">黄仁勋向英伟达员工道歉，并表示自己正在接受心理治疗</span>
          <span class="news-item-title-en">Jensen Huang Apologizes to Nvidia Employees, Says He Is in Therapy</span>
          <span class="news-value-point">💡 回到公司一天后，黄先生承认自己违反了英伟达的行为准则，并“犯了一些严重的错误”</span>
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
        <a class="news-item" href="https://www.nytimes.com/2026/11/24/business/stocks-sp500-huang-nvidia.html" target="_blank" rel="noopener" data-cat="keji" data-summary="受英伟达的戏剧性事件以及Anthropic在轰动一时的首次公开募股之后的股价涨跌的影响，股票价格数日来大幅波动。" data-title="Stock Markets Slip as Nvidia and A.I. Stocks Erase Some of Monday’s Rally" data-date="11-25 01:51" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-25 01:51</span>
          <span class="news-item-title">英伟达和人工智能股抹去周一的部分涨幅，股市走低</span>
          <span class="news-item-title-en">Stock Markets Slip as Nvidia and A.I. Stocks Erase Some of Monday’s Rally</span>
          <span class="news-value-point">💡 受英伟达的戏剧性事件以及Anthropic在轰动一时的首次公开募股之后的股价涨跌的影响，股票价格数日来大幅波动</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/entertainment/1041362/tidal-ai-music-ban" target="_blank" rel="noopener" data-cat="keji" data-summary="Tidal将于12月9日正式禁止人工智能生成的音乐。Tidal音乐负责人罗伯特·安德森（Robert Andersen）表示，由于这一变化，Tidal将删除约2900万首由人工智能生成的歌曲，并每天拒绝约8万至8.5万首曲目。" data-title="Tidal will start banning AI-generated music next month" data-date="11-25 01:17" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-25 01:17</span>
          <span class="news-item-title">Tidal将于下月开始禁止人工智能生成的音乐</span>
          <span class="news-item-title-en">Tidal will start banning AI-generated music next month</span>
          <span class="news-value-point">💡 Tidal将于12月9日正式禁止人工智能生成的音乐</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/031/896.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 25 日消息，以“卓越创新、开放共赢”为主题的第七届华为创新和知识产权论坛昨日在北京举办。▲ 华为在北京召开第七届创新和知识产权论坛据介绍，2025 年华为增加了 20 个被许可人，覆盖网络与通信设备、消费电子与计算、物联网、汽车、流媒体和半导体等领域。截至目前，华为对外专利许可协议累计金额超 69 亿美元（IT之家注：现汇率约合 460.87 亿元人民币），其中 2025 年的专利许可收入约为 8 亿美元（现汇率约合 53.43 亿元人民币）。截至 2025 年底，超过 32 亿部 5G 设备、超过 16 亿台 Wi-Fi 消费电子终端及超过 41 亿台多媒体设备获得了华为的专利授权。IT之家从华为官方获悉，在华为持有的有效授权专利中，占比排名前三的技术领域依次为：无线" data-title="华为：截至目前，对外专利许可协议累计金额超 69 亿美元" data-date="11-25 01:06" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-25 01:06</span>
          <span class="news-item-title">华为：截至目前，对外专利许可协议累计金额超 69 亿美元</span>
          <span class="news-value-point">💡 IT之家 11 月 25 日消息，以“卓越创新、开放共赢”为主题的第七届华为创新和知识产权论坛昨日在北京举办</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/best-gaming-graphics-card-gpu-deals-nvidia-amd-intel" target="_blank" rel="noopener" data-cat="keji" data-summary="购买GeForce、Radeon和Arc显卡，享受优惠。我们会不断更新此列表，收录所有零售商所有促销活动中的最佳黑色星期五显卡优惠。" data-title="Best Black Friday gaming GPU deals 2026" data-date="11-25 00:59" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-25 00:59</span>
          <span class="news-item-title">2026年黑色星期五最佳游戏显卡优惠</span>
          <span class="news-item-title-en">Best Black Friday gaming GPU deals 2026</span>
          <span class="news-value-point">💡 购买GeForce、Radeon和Arc显卡，享受优惠</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/24/tidal-to-ban-and-remove-millions-of-ai-generated-tracks-as-ai-slop-inundates-music-streaming/" target="_blank" rel="noopener" data-cat="keji" data-summary="该公司表示，仍将接受在人工智能辅助下创作的歌曲，但不会接受完全由人工智能生成的歌曲。" data-title="Tidal to ban and remove millions of AI-generated tracks as AI slop inundates music streaming" data-date="11-25 00:46" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-25 00:46</span>
          <span class="news-item-title">Tidal将禁用并删除数百万首由人工智能生成的曲目，因为人工智能垃圾正在淹没音乐流媒体平台</span>
          <span class="news-item-title-en">Tidal to ban and remove millions of AI-generated tracks as AI slop inundates music streaming</span>
          <span class="news-value-point">💡 该公司表示，仍将接受在人工智能辅助下创作的歌曲，但不会接受完全由人工智能生成的歌曲</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/policy/1041270/nvidia-megaspeed-commerce-dept-entity-list" target="_blank" rel="noopener" data-cat="keji" data-summary="在特朗普政府的支持下，Jensen Huang重返Nvidia首席执行官的职位，而美国商务部则以国家安全风险为由将Megaspeed列入实体清单，从而禁止与该公司的贸易往来。正如早些时候报道的那样，" data-title="US Commerce Department adds Megaspeed to trade blacklist as Huang retakes control of Nvidia" data-date="11-25 00:37" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-25 00:37</span>
          <span class="news-item-title">美国商务部将Megaspeed列入贸易黑名单，黄仁勋重新掌管英伟达</span>
          <span class="news-item-title-en">US Commerce Department adds Megaspeed to trade blacklist as Huang retakes control of Nvidia</span>
          <span class="news-value-point">💡 在特朗普政府的支持下，Jensen Huang重返Nvidia首席执行官的职位，而美国商务部则以国家安全风险为由将Megaspeed列入实体清单…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/saudi-openai-eavesdropper-who-bugged-company-office-had-hundreds-of-private-recordings-was-in-frequent-communication-with-saudi-government-perp-had-dozens-of-recordings-of-discussions-of-trade-secrets" target="_blank" rel="noopener" data-cat="keji" data-summary="检察官发现了数十段OpenAI会议和谈话的录音，这些录音是从该公司一个会议室内的隐蔽窃听装置中录制的。" data-title="Saudi OpenAI eavesdropper who bugged company office had hundreds of private recordings" data-date="11-25 00:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-25 00:30</span>
          <span class="news-item-title">在公司办公室安装窃听器的沙特OpenAI窃听者拥有数百段私人录音</span>
          <span class="news-item-title-en">Saudi OpenAI eavesdropper who bugged company office had hundreds of private recordings</span>
          <span class="news-value-point">💡 检察官发现了数十段OpenAI会议和谈话的录音，这些录音是从该公司一个会议室内的隐蔽窃听装置中录制的</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1041222/jensen-huang-nvidia-scandal-deepfakes" target="_blank" rel="noopener" data-cat="keji" data-summary="Jensen Huang正在伊比萨岛狂欢。在一则在Instagram上拥有近600万次观看的视频中，英伟达的前首席执行官手持香槟杯，身着他标志性的黑色皮夹克，在拥挤的夜店里翩翩起舞。突然，从他身后，" data-title="Jensen Huang deepfakes are the hot new AI slop" data-date="11-25 00:30" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-25 00:30</span>
          <span class="news-item-title">黄仁勋的深度伪造视频是热门的新型AI垃圾内容</span>
          <span class="news-item-title-en">Jensen Huang deepfakes are the hot new AI slop</span>
          <span class="news-value-point">💡 Jensen Huang正在伊比萨岛狂欢</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cjr4gwxzgyydo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="黄仁勋戏剧性重返英伟达，不仅让北京看到了影响华盛顿的可能，也让习近平进一步了解特朗普的软肋，以及中国在中美科技与贸易博弈中可以利用的筹码。" data-title="黄仁勋重掌Nvidia：习近平从特朗普身上看到了什么？" data-date="11-25 00:15" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-25 00:15</span>
          <span class="news-item-title">黄仁勋重掌Nvidia：习近平从特朗普身上看到了什么？</span>
          <span class="news-value-point">💡 黄仁勋戏剧性重返英伟达，不仅让北京看到了影响华盛顿的可能，也让习近平进一步了解特朗普的软肋，以及中国在中美科技与贸易博弈中可以利用的筹码</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/24/why-a-crusoe-investor-is-betting-on-solar-and-batteries-to-power-future-ai-data-centers/" target="_blank" rel="noopener" data-cat="keji" data-summary="下一代数据中心每年将需要数十吉瓦的电力。Crusoe 的一位投资者认为，太阳能和储能是显而易见的选择。" data-title="Why a Crusoe investor is betting on solar and batteries to power future AI data centers" data-date="11-25 00:10" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-25 00:10</span>
          <span class="news-item-title">为什么Crusoe的投资者押注于太阳能和电池为未来的人工智能数据中心供电</span>
          <span class="news-item-title-en">Why a Crusoe investor is betting on solar and batteries to power future AI data centers</span>
          <span class="news-value-point">💡 下一代数据中心每年将需要数十吉瓦的电力</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
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
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13616058/jurrien-timbers-shirt-pull-on-alexander-isak-ref-chief-howard-webb-admits-quick-check-in-arsenals-win-at-liverpool" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在阿森纳在安菲尔德球场获胜的比赛中，阿森纳后卫尤里恩·廷伯（Jurrien Timber）拉扯利物浦前锋亚历山大·伊萨克（Alexander Isak）的球衣却未受处罚，裁判长霍华德·韦伯（Howard Webb）承认，视频助理裁判（VAR）对此进行了“快速检查”。" data-title="How &#39;quick check&#39; and unseen angle saw Timber&#39;s Isak shirt" data-date="11-25 01:13" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 01:13</span>
          <span class="news-item-title">“快速检查”和隐蔽视角如何发现了Timber的Isak衬衫</span>
          <span class="news-item-title-en">How 'quick check' and unseen angle saw Timber's Isak shirt</span>
          <span class="news-value-point">💡 在阿森纳在安菲尔德球场获胜的比赛中，阿森纳后卫尤里恩·廷伯（Jurrien Timber）拉扯利物浦前锋亚历山大·伊萨克（Alexander I…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13616058/jurrien-timbers-shirt-pull-on-alexander-isak-ref-chief-howard-webb-admits-quick-check-in-arsenals-win-at-liverpool" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在阿森纳在安菲尔德球场获胜的比赛中，阿森纳后卫尤里恩·廷伯（Jurrien Timber）拉扯利物浦前锋亚历山大·伊萨克（Alexander Isak）的球衣却未受处罚，裁判长霍华德·韦伯（Howard Webb）承认，视频助理裁判（VAR）对此进行了“快速检查”。" data-title="How &#39;quick check&#39; and unseen angle saw Timber&#39;s Isak shirt" data-date="11-25 01:13" data-source="天空体育">
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
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13616033/leny-yoro-red-card-ref-chief-howard-webb-backs-process-that-saw-man-utd-defender-sent-off-at-liverpool" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="尽管红牌在上诉后被撤销，但裁判长霍华德·韦伯（Howard Webb）仍支持裁判在利物浦对阵曼联的比赛中将曼联后卫莱尼·约罗（Leny Yoro）罚下的决定。" data-title="Ref chief Webb backs process around Yoro sending off despite successful appeal" data-date="11-25 01:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 01:00</span>
          <span class="news-item-title">尽管上诉成功，但裁判长韦伯仍支持对约罗的红牌判罚过程</span>
          <span class="news-item-title-en">Ref chief Webb backs process around Yoro sending off despite successful appeal</span>
          <span class="news-value-point">💡 尽管红牌在上诉后被撤销，但裁判长霍华德·韦伯（Howard Webb）仍支持裁判在利物浦对阵曼联的比赛中将曼联后卫莱尼·约罗（Leny Yoro…</span>
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
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/12476234/transfer-centre-live-football-transfer-news-updates-and-rumours" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Transfer Centre LIVE! Heaven open to leaving Man Utd in January" data-title="Transfer Centre LIVE! Heaven open to leaving Man Utd in January" data-date="11-25 00:55" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 00:55</span>
          <span class="news-item-title">转会中心直播！埃文可能在 1 月离开曼联</span>
          <span class="news-item-title-en">Transfer Centre LIVE! Heaven open to leaving Man Utd in January</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13615995/man-utd-transfer-spending-to-be-limited-by-new-stadium-plans-in-the-short-term-according-to-chief-executive-omar-berrada" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联首席执行官奥马尔·贝拉达承认，建造一座可容纳 10 万人的新体育场的计划将限制未来转会窗口的转会支出。" data-title="Berrada admits Man Utd transfer spending will be limited by stadium plans" data-date="11-25 00:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 00:00</span>
          <span class="news-item-title">贝拉达承认，曼联的转会支出将受到球场改造计划的限制</span>
          <span class="news-item-title-en">Berrada admits Man Utd transfer spending will be limited by stadium plans</span>
          <span class="news-value-point">💡 曼联首席执行官奥马尔·贝拉达承认，建造一座可容纳 10 万人的新体育场的计划将限制未来转会窗口的转会支出</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13616010/explained-could-manchester-united-really-be-relegated-this-season" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育的罗恩·沃克深入分析了曼联本赛季是否真的有可能降级。" data-title="Could Man Utd really be relegated this season?" data-date="11-24 23:08" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 23:08</span>
          <span class="news-item-title">曼联本赛季真的会降级吗？</span>
          <span class="news-item-title-en">Could Man Utd really be relegated this season?</span>
          <span class="news-value-point">💡 天空体育的罗恩·沃克深入分析了曼联本赛季是否真的有可能降级</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025492/man-utd-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Man Utd latest: Shaw included in squad for Sporting trip" data-title="Man Utd latest: Shaw included in squad for Sporting trip" data-date="11-24 23:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 23:00</span>
          <span class="news-item-title">曼联最新消息：肖入选出征里斯本竞技的阵容</span>
          <span class="news-item-title-en">Man Utd latest: Shaw included in squad for Sporting trip</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/manchester-city-vs-napoli/live/577674" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Man City vs Napoli team news as De Bruyne starts LIVE!" data-title="Man City vs Napoli team news as De Bruyne starts LIVE!" data-date="11-24 20:40" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 20:40</span>
          <span class="news-item-title">曼城对那不勒斯球队最新消息：德布劳内首发！</span>
          <span class="news-item-title-en">Man City vs Napoli team news as De Bruyne starts LIVE!</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c34gn2p5d0zwo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在本赛季英超联赛的每一轮比赛之后，特洛伊·迪尼（ Troy Deeney ）都给了我们本周最佳球队。你同意他的选择吗？" data-title="Who has made Troy&#39;s Premier League team of the week?" data-date="11-24 07:26" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-24 07:26</span>
          <span class="news-item-title">谁入选了特洛伊本周的英超联赛球队？</span>
          <span class="news-item-title-en">Who has made Troy's Premier League team of the week?</span>
          <span class="news-value-point">💡 在本赛季英超联赛的每一轮比赛之后，特洛伊·迪尼（ Troy Deeney ）都给了我们本周最佳球队</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmqx5eynvpqno?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在周一以 0-4 输给布伦特福德的比赛中，埃弗顿队长詹姆斯·塔尔科夫斯基（James Tarkowski）在其英超生涯中首次被罚下场——但这是一项严厉的判罚吗？" data-title="Tarkowski&#39;s first Premier League red ruins Moyes&#39; night" data-date="11-24 06:43" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-24 06:43</span>
          <span class="news-item-title">塔尔科夫斯基在英超联赛中的首张红牌毁了莫耶斯的夜晚</span>
          <span class="news-item-title-en">Tarkowski's first Premier League red ruins Moyes' night</span>
          <span class="news-value-point">💡 在周一以 0-4 输给布伦特福德的比赛中，埃弗顿队长詹姆斯·塔尔科夫斯基（James Tarkowski）在其英超生涯中首次被罚下场——但这是一…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theverge.com/gadgets/1040046/apple-tv-subscription-streaming-sale-deal-black-friday" target="_blank" rel="noopener" data-cat="zonghe" data-summary="流媒体优惠不再像以前那样多，但如果您知道在哪里找，仍然可以找到。其中一个吸引我们注意的是针对美国亚马逊账户持有者的Apple TV优惠。苹果的流媒体服务通常每月收费 14.99 美元。" data-title="Amazon is knocking almost $50 off six months of Apple TV" data-date="11-25 03:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-25 03:00</span>
          <span class="news-item-title">亚马逊为苹果电视六个月的订阅服务提供近50美元的折扣</span>
          <span class="news-item-title-en">Amazon is knocking almost $50 off six months of Apple TV</span>
          <span class="news-value-point">💡 流媒体优惠不再像以前那样多，但如果您知道在哪里找，仍然可以找到</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/24/climate/iowa-army-ammunition-plant-explostion.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="冰点以下的温度可能使正在降解的爆炸物变得更加不稳定，而大风则可能将有毒的铅烟羽带到100英里以外的地方。" data-title="Army’s Iowa Ammunition Plant Explosion on Schedule for Wednesday Morning" data-date="11-25 02:57" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-25 02:57</span>
          <span class="news-item-title">陆军爱荷华州弹药厂爆炸按计划将于周三上午发生</span>
          <span class="news-item-title-en">Army’s Iowa Ammunition Plant Explosion on Schedule for Wednesday Morning</span>
          <span class="news-value-point">💡 冰点以下的温度可能使正在降解的爆炸物变得更加不稳定，而大风则可能将有毒的铅烟羽带到100英里以外的地方</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1041474/firefox-161-vpn-rules-fire-button" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Mozilla 于周二发布了 Firefox 161，其中包含一项新设置，您可以使用该设置选择在浏览器的 VPN 处于活动状态时自动打开哪些页面。使用Firefox VPN面板中的“管理VPN规则”选项，您可以将其设置为“始终开启”或“始终关闭”。" data-title="Now Firefox can select which sites use its VPN, and clear your browsing history with one click" data-date="11-25 02:44" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-25 02:44</span>
          <span class="news-item-title">现在，Firefox 可以选择哪些网站使用其 VPN，并一键清除您的浏览历史记录</span>
          <span class="news-item-title-en">Now Firefox can select which sites use its VPN, and clear your browsing history with one click</span>
          <span class="news-value-point">💡 Mozilla 于周二发布了 Firefox 161，其中包含一项新设置，您可以使用该设置选择在浏览器的 VPN 处于活动状态时自动打开哪些页面</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/3d-printing/3d-printer-tool-changers-are-cheaper-than-ever-now-starting-at-just-usd599-with-multiple-models-at-lowest-ever-pricing-these-game-changing-multi-material-multi-color-filament-saving-printers-are-all-on-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="换头式打印机在打印多色或多材料模型时可以节省大量耗材，而且它们过去非常昂贵。但现在情况不同了，多款型号目前正以历史最低价或接近历史最低价的优惠价格出售。" data-title="3D printer tool changers are cheaper than ever, now starting at just $599 with multiple models at lowest" data-date="11-25 02:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-25 02:30</span>
          <span class="news-item-title">3D打印机刀具更换器比以往任何时候都便宜，现在最低只要599美元起，并且有多款型号可供选择。</span>
          <span class="news-item-title-en">3D printer tool changers are cheaper than ever, now starting at just $599 with multiple models at lowest</span>
          <span class="news-value-point">💡 换头式打印机在打印多色或多材料模型时可以节省大量耗材，而且它们过去非常昂贵</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/cricket/news/12040/13616078/ben-8204stokes-former-england-captain-registers-for-2027-indian-8204premier-league-auction" target="_blank" rel="noopener" data-cat="zonghe" data-summary="据Cricinfo周二报道，英格兰前队长本·斯托克斯（Ben ‌Stokes）已报名参加2027年印度超级联赛拍卖会，这位全能球员名列12月16日在果阿州举行的拍卖会候选名单中。" data-title="Stokes registers for 2027 IPL auction" data-date="11-25 02:25" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 02:25</span>
          <span class="news-item-title">斯托克斯报名参加 2027 年 IPL 拍卖会</span>
          <span class="news-item-title-en">Stokes registers for 2027 IPL auction</span>
          <span class="news-value-point">💡 据Cricinfo周二报道，英格兰前队长本·斯托克斯（Ben ‌Stokes）已报名参加2027年印度超级联赛拍卖会，这位全能球员名列12月16…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/entertainment/1041417/david-fincher-netflix-cliff-booth-ai-interpositive" target="_blank" rel="noopener" data-cat="zonghe" data-summary="尽管大卫·芬奇的粉丝一直热切期待《克里夫·布斯的进一步奇遇》，但布拉德·皮特主演的《好莱坞往事》续集的早期放映引发了人们对该片是否使用了生成式人工智能的疑问。" data-title="David Fincher is being dragged for suspected use of AI in his latest film" data-date="11-25 02:15" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-25 02:15</span>
          <span class="news-item-title">大卫·芬奇因涉嫌在其最新电影中使用人工智能而受到抨击</span>
          <span class="news-item-title-en">David Fincher is being dragged for suspected use of AI in his latest film</span>
          <span class="news-value-point">💡 尽管大卫·芬奇的粉丝一直热切期待《克里夫·布斯的进一步奇遇》，但布拉德·皮特主演的《好莱坞往事》续集的早期放映引发了人们对该片是否使用了生成式人…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/21/climate/what-to-know-about-the-planned-explosion-in-iowa.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="陆军官员周二表示，陆军计划于周三上午在爱荷华州东南部的一处设施引爆一批正在危险地变质的爆炸物。" data-title="What to Know About the Planned Explosion in Middletown, Iowa" data-date="11-25 02:08" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-25 02:08</span>
          <span class="news-item-title">关于爱荷华州米德尔敦计划性爆炸的须知事项</span>
          <span class="news-item-title-en">What to Know About the Planned Explosion in Middletown, Iowa</span>
          <span class="news-value-point">💡 陆军官员周二表示，陆军计划于周三上午在爱荷华州东南部的一处设施引爆一批正在危险地变质的爆炸物</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/gift-guides-seasonal-sales/ram-price-tracking-2026-lowest-price-on-ddr5-and-ddr4-memory-of-all-capacities" target="_blank" rel="noopener" data-cat="zonghe" data-summary="查看不同容量的 DDR5 和 DDR4 内存套件的最佳价格。" data-title="RAM price tracking 2026" data-date="11-25 01:58" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-25 01:58</span>
          <span class="news-item-title">2026 年内存价格跟踪</span>
          <span class="news-item-title-en">RAM price tracking 2026</span>
          <span class="news-value-point">💡 查看不同容量的 DDR5 和 DDR4 内存套件的最佳价格</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/tennis/news/12040/13615618/jannik-sinner-former-world-no-1-undergoes-surgery-on-his-right-knee-casting-doubt-over-australian-open-participation" target="_blank" rel="noopener" data-cat="zonghe" data-summary="前世界排名第一的扬尼克·辛纳（Jannik Sinner）接受了膝盖手术，这使他参加澳网的希望蒙上了阴影。" data-title="Sinner surgery casts doubt over Australian Open appearance" data-date="11-25 01:44" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 01:44</span>
          <span class="news-item-title">辛纳接受手术，其澳网参赛前景蒙上阴影</span>
          <span class="news-item-title-en">Sinner surgery casts doubt over Australian Open appearance</span>
          <span class="news-value-point">💡 前世界排名第一的扬尼克·辛纳（Jannik Sinner）接受了膝盖手术，这使他参加澳网的希望蒙上了阴影</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/the-ssd-crisis-is-being-defeated-with-black-friday-1tb-and-2tb-deals-at-less-than-usd0-15-per-gb-some-pcie-4-0-ssds-are-now-cheaper-than-when-we-reviewed-them" target="_blank" rel="noopener" data-cat="zonghe" data-summary="一些 1TB 和 2TB 的 PCIe 4.0 固态硬盘比我们评测时便宜，每 GB 的价格不到 0.15 美元。" data-title="The SSD crisis is being defeated with Black Friday 1TB and 2TB deals at less than $0.15 per GB" data-date="11-25 01:40" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-25 01:40</span>
          <span class="news-item-title">黑色星期五1TB和2TB固态硬盘优惠价低于每GB 0.15美元，固态硬盘危机正在被攻克</span>
          <span class="news-item-title-en">The SSD crisis is being defeated with Black Friday 1TB and 2TB deals at less than $0.15 per GB</span>
          <span class="news-value-point">💡 一些 1TB 和 2TB 的 PCIe 4.0 固态硬盘比我们评测时便宜，每 GB 的价格不到 0.15 美元</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/handheld-gaming/the-best-nintendo-switch-2-accessories-on-sale-now-for-black-friday-2026-controllers-cameras-cases-screen-protectors-and-more" target="_blank" rel="noopener" data-cat="zonghe" data-summary="使用这些必备配件升级您的Nintendo Switch 2" data-title="The best Switch 2 accessories on sale now" data-date="11-25 01:33" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-25 01:33</span>
          <span class="news-item-title">现在销售的最好的Switch 2配件</span>
          <span class="news-item-title-en">The best Switch 2 accessories on sale now</span>
          <span class="news-value-point">💡 使用这些必备配件升级您的Nintendo Switch 2</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1040315/black-friday-best-early-robot-vacuum-mop-deals-2026" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在布置装饰、招待客人和准备餐食之间，节日已经够忙碌了，无需再为吸尘操心。幸运的是，一台合适的扫地机器人可以代您完成繁琐的清洁工作，让您专注于更有趣的事情。而且，多亏了黑色星期五" data-title="Dreame and Eufy are offering nearly 60 percent off robovacs for Black Friday" data-date="11-25 01:30" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-25 01:30</span>
          <span class="news-item-title">Dreame和Eufy在黑色星期五期间提供近六折的扫地机器人优惠</span>
          <span class="news-item-title-en">Dreame and Eufy are offering nearly 60 percent off robovacs for Black Friday</span>
          <span class="news-value-point">💡 在布置装饰、招待客人和准备餐食之间，节日已经够忙碌了，无需再为吸尘操心</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/darts/news/12040/13616056/luke-humphriess-hopeful-of-playing-in-players-championship-after-suffering-shoulder-injury" target="_blank" rel="noopener" data-cat="zonghe" data-summary="据天空体育新闻了解，卢克·汉弗莱斯（Luke Humphries）有望参加本周的球员锦标赛。" data-title="Humphries hoping to make Players Championship despite shoulder injury" data-date="11-25 01:30" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-25 01:30</span>
          <span class="news-item-title">汉弗莱斯希望克服肩伤，参加球员锦标赛</span>
          <span class="news-item-title-en">Humphries hoping to make Players Championship despite shoulder injury</span>
          <span class="news-value-point">💡 据天空体育新闻了解，卢克·汉弗莱斯（Luke Humphries）有望参加本周的球员锦标赛</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/24/nyregion/graffiti-sane-nyc-david-smith-art.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="一对来自皇后区的夫妇正致力于传承大卫·史密斯（David Smith）的传奇，他以“Sane”的称号更为人所知。在20世纪80年代，他是纽约市最受通缉的涂鸦破坏者之一。" data-title="Sane Was a Prolific Graffiti Tagger in NYC. Now, a Couple is Working to Keep His Legacy Alive." data-date="11-25 01:29" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-25 01:29</span>
          <span class="news-item-title">Sane是纽约市一位多产的涂鸦艺术家。如今，一对夫妇正努力传承他的艺术遗产。</span>
          <span class="news-item-title-en">Sane Was a Prolific Graffiti Tagger in NYC. Now, a Couple is Working to Keep His Legacy Alive.</span>
          <span class="news-value-point">💡 一对来自皇后区的夫妇正致力于传承大卫·史密斯（David Smith）的传奇，他以“Sane”的称号更为人所知</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/24/nyregion/campaign-solicitation-came-with-unusual-offer-can-i-zelle-you-money.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Jasmin Sanchez表示愿意向她的州议会竞选捐款人偿还捐款，因为她希望获得纽约慷慨的配套资金计划。" data-title="‘Can I Zelle You Money?’: How a Candidate Secretly Funded Her Campaign" data-date="11-25 01:08" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-25 01:08</span>
          <span class="news-item-title">“我可以Zelle给你钱吗？”：一位候选人如何秘密资助自己的竞选活动</span>
          <span class="news-item-title-en">‘Can I Zelle You Money?’: How a Candidate Secretly Funded Her Campaign</span>
          <span class="news-value-point">💡 Jasmin Sanchez表示愿意向她的州议会竞选捐款人偿还捐款，因为她希望获得纽约慷慨的配套资金计划</span>
        </a>
  </div>
</div>
<script defer src="{{ "/assets/js/news-feed.js" | relative_url }}"></script>


<p class="news-updated">🕐 抓取更新于 2026-11-25 03:00（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
