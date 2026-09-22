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
      <span>2026-09-22 20:45 抓取更新</span>
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
        <span class="channel-count">54</span>
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
        <span class="channel-count">9</span>
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
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/09-22/10701719.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京9月22日电 (记者 庞无忌)9月22日，2026年世界城市日全球主场活动暨第四届全球可持续发展城市奖(上海奖)颁奖活动新闻发布会在北京举行。住房和城乡建设部副部长陈绍旺，联合国人居署执行主任特别代表、全球解决方案司司长拉夫·图茨，福建省副省长王金福，福州市市长吴贤德出席新闻发布会，介绍有关情况并回答记者提问。" data-title="2026年世界城市日全球主场活动将在福州举行" data-date="09-22 20:39" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 09-22 20:39</span>
      </div>
      <h2 class="hero-featured-title">2026年世界城市日全球主场活动将在福州举行</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/gj/2026/09-22/10701786.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网北京9月22日电 据加拿大通讯社报道，加拿大不列颠哥伦比亚省政府于当地时间21日起诉美国开放人工智能研究中心(OpenAI)及其首席执行官萨姆·奥尔特曼，指控该公司未将塔布勒岭枪击案凶手在ChatGPT上的异常对话报告给当地警方。" data-title="加拿大一省政府就校园枪击案起诉OpenAI" data-date="09-22 20:27" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">加拿大一省政府就校园枪击案起诉OpenAI</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/ckd68e40ze3jo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="米克尔·阿尔特塔同意与英超冠军阿森纳签订一份经过改进的新合同。" data-title="阿尔特塔同意与阿森纳冠军达成新协议" data-date="09-22 19:48" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">阿尔特塔同意与阿森纳冠军达成新协议</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/005/948.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 22 日消息，OPPO 33W 口袋充超级闪充移动电源 10000 现已开售，容量 10000mAh，售价 149 元。这款移动电源重约 204g，尺寸为 110.6×70.6×18.1mm，有卡其香氛和轻盈粉两种颜色可选；获得 2026 新国标认证，支持 ColorOS 系统级互联生态，可查看移动电源的剩余电量、电池健康度、实时温度等信息。这款移动电源配备 A + C 双口输出，兼容 SUPERVOOC、PD、PPS、QC、UFCS 等协议；USB-C 单口和 USB-A 单口最大功率均为 33W ，双口同时输出时最高为 5V 4A；支持自动识别小电流设备，可为智能手表、耳机、手环等小设备稳定充电。这款产品附赠了一条长度 0.2m 的 3A 手提充电线，采用高密度编织材质" data-title="OPPO 33W 口袋充移动电源 10000 开售：新国标、A+C 双口，149 元" data-date="09-22 20:44" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">OPPO 33W 口袋充移动电源 10000 开售：新国标、A+C 双口，149 元</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-22/10701719.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京9月22日电 (记者 庞无忌)9月22日，2026年世界城市日全球主场活动暨第四届全球可持续发展城市奖(上海奖)颁奖活动新闻发布会在北京举行。住房和城乡建设部副部长陈绍旺，联合国人居署执行主任特别代表、全球解决方案司司长拉夫·图茨，福建省副省长王金福，福州市市长吴贤德出席新闻发布会，介绍有关情况并回答记者提问。" data-title="2026年世界城市日全球主场活动将在福州举行" data-date="09-22 20:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 20:39</span>
          <span class="news-item-title">2026年世界城市日全球主场活动将在福州举行</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/22/us/politics/aoc-2028-presidential-race.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在一次广泛的采访中，这位纽约女议员就她如何考虑可能的总统竞选提出了迄今为止最详细的见解。" data-title="Alexandria Ocasio-Cortez是否会竞选2028年的总统？这是她说的话。" data-date="09-22 20:30" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-22 20:30</span>
          <span class="news-item-title">Alexandria Ocasio-Cortez是否会竞选2028年的总统？这是她说的话。</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-22/10701640.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社哈萨克斯坦阿拉木图9月22日电 (记者 单璐)“山与歌的和鸣：中国—哈萨克斯坦高原生态文明交流对话”活动22日在哈萨克斯坦阿拉木图举行，中哈政界、学界、文化艺术界人士及高校学生代表等120余人出席。" data-title="中哈高原生态文明交流对话活动在阿拉木图举行" data-date="09-22 20:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 20:26</span>
          <span class="news-item-title">中哈高原生态文明交流对话活动在阿拉木图举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-22/10701796.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月22日电 据外媒当地时间9月22日报道，西班牙首相桑切斯在美国纽约举行的“多边主义伙伴”活动发表讲话，强调捍卫普遍且包容的多边主义，反对任何试图瓦解多边主义的企图。" data-title="西班牙首相桑切斯：反对任何试图瓦解多边主义的企图" data-date="09-22 20:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 20:21</span>
          <span class="news-item-title">西班牙首相桑切斯：反对任何试图瓦解多边主义的企图</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-22/10701673.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京9月22日电 (记者 徐婧 陈杭 吕少威)由中共中央宣传部、中共北京市委、北京市人民政府共同主办的2026北京文化论坛22日下午在北京开幕。" data-title="聚焦文化遗产与文明互鉴 2026北京文化论坛开幕" data-date="09-22 20:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 20:15</span>
          <span class="news-item-title">聚焦文化遗产与文明互鉴 2026北京文化论坛开幕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-22/10701791.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月22日电 据路透社当地时间9月22日援引一名伊朗高级官员消息称，如果美国减轻军事压力并解除对伊朗港口的封锁，伊朗可以在7天之内重新开放霍尔木兹海峡。" data-title="伊朗称美国若减轻军事压力并解除港口封锁 可7天内重开霍尔木兹海峡" data-date="09-22 20:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 20:15</span>
          <span class="news-item-title">伊朗称美国若减轻军事压力并解除港口封锁 可7天内重开霍尔木兹海峡</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-22/10701678.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网宁德9月22日电 (记者 叶茂)陈祥榕烈士事迹展陈室22日在陈祥榕的家乡——福建省宁德市屏南县甘棠乡下山口村揭牌。" data-title="陈祥榕烈士事迹展陈室在福建屏南揭牌" data-date="09-22 20:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 20:09</span>
          <span class="news-item-title">陈祥榕烈士事迹展陈室在福建屏南揭牌</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-22/10701485.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="习近平主席对美国进行国事访问前夕，外交部与人民日报社联合发布重磅视频。从北京到华盛顿，期待中美关系继续沿着建设性战略稳定的正确航向，乘风破浪、不断前行。" data-title="人民日报重磅视频｜建设性战略稳定" data-date="09-22 19:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 19:47</span>
          <span class="news-item-title">人民日报重磅视频｜建设性战略稳定</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/22/podcasts/the-headlines/xi-jinping-dc-white-house-press-ban.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="另外，还有那个帮忙在菜单上放虫子的人。" data-title="习近平为何来到华盛顿，白宫电视转播却一片漆黑" data-date="09-22 18:00" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-22 18:00</span>
          <span class="news-item-title">习近平为何来到华盛顿，白宫电视转播却一片漆黑</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-22/10701577.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网悉尼9月22日电 由中国驻墨尔本总领事馆主办的“中国文化日”活动日前在澳大利亚维多利亚州吉朗学院举行。中国驻墨尔本总领事房新文、驻墨尔本总领馆副总领事刘东源，吉朗学院校长西蒙·扬、吉朗华人协会主席袁茜敏、侨界代表等800余人出席。" data-title="2026“中国文化日”活动在澳大利亚举行" data-date="09-22 17:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 17:53</span>
          <span class="news-item-title">2026“中国文化日”活动在澳大利亚举行</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/22/us/politics/kamala-harris-el-sayed-michigan-midterms.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="这位前副总统希望在中期选举中帮助她的政党，但没有多少人接受她的提议。除了密歇根州的参议院提名人，他将于周二与她一起出现。" data-title="许多民主党人正在避开卡马拉·哈里斯。Abdul El-Sayed欢迎她。" data-date="09-22 17:02" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-22 17:02</span>
          <span class="news-item-title">许多民主党人正在避开卡马拉·哈里斯。Abdul El-Sayed欢迎她。</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/22/us/charlie-kirk-trump-free-speech.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="白宫将批评者列为恐怖分子，将暴力归咎于左翼阴谋，并在一场争夺言论自由的斗争中调查了工会、非营利组织和其他团体。" data-title="自查理·柯克被杀以来，特朗普如何打击异议" data-date="09-22 17:01" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-22 17:01</span>
          <span class="news-item-title">自查理·柯克被杀以来，特朗普如何打击异议</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-22/10701428.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月22日电 (记者 吴辛茹)近日，“2026世界市长对话·武汉”活动举办。多国嘉宾走进长江江豚繁育保护中心，近距离邂逅被誉为“微笑天使”的长江江豚，实地感受武汉守护长江生态的实践与探索。" data-title="在武汉邂逅“微笑天使”江豚，中外代表问出一个引人深思的问题 | 中国不一样" data-date="09-22 16:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 16:54</span>
          <span class="news-item-title">在武汉邂逅“微笑天使”江豚，中外代表问出一个引人深思的问题 | 中国不一样</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-22/10701545.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社华盛顿9月21日电(记者颜亮)美国芝加哥全球事务委员会21日公布的调查报告显示，57%的美国民众认为美国应该同中国开展友好合作与接触，延续了自2024年以来美国民众逐渐转向支持对华接触的趋势。" data-title="调查显示57%美国民众支持对华友好合作" data-date="09-22 16:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 16:50</span>
          <span class="news-item-title">调查显示57%美国民众支持对华友好合作</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-22/10701490.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月22日电 综合外媒报道，美国白宫当地时间21日宣布推出“特朗普电视”。美国媒体称之为“一个在优兔平台全天候24小时播放特朗普政府过往活动的流媒体频道”。" data-title="白宫宣布推出“特朗普电视”：24小时播放、实时更新" data-date="09-22 16:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 16:02</span>
          <span class="news-item-title">白宫宣布推出“特朗普电视”：24小时播放、实时更新</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-22/10701786.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网北京9月22日电 据加拿大通讯社报道，加拿大不列颠哥伦比亚省政府于当地时间21日起诉美国开放人工智能研究中心(OpenAI)及其首席执行官萨姆·奥尔特曼，指控该公司未将塔布勒岭枪击案凶手在ChatGPT上的异常对话报告给当地警方。" data-title="加拿大一省政府就校园枪击案起诉OpenAI" data-date="09-22 20:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 20:27</span>
          <span class="news-item-title">加拿大一省政府就校园枪击案起诉OpenAI</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/22/nscales-ipo-will-test-wall-streets-appetite-for-concentrated-ai-bets-once-again/" target="_blank" rel="noopener" data-cat="keji" data-summary="这家英国人工智能数据中心开发商的大部分收入都依赖于科技巨头微软和Anthropic。" data-title="Nscale的IPO将再次测试华尔街对集中人工智能押注的兴趣" data-date="09-22 20:23" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-22 20:23</span>
          <span class="news-item-title">Nscale的IPO将再次测试华尔街对集中人工智能押注的兴趣</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/998272/peloton-tread-flex-fitness-treadmills" target="_blank" rel="noopener" data-cat="keji" data-summary="去年， Peloton对其硬件进行了全面更新，增加了摄像头、风扇和名为Peloton IQ的人工智能软件。今年，它将专注于其跑步机产品阵容-更新其现有的两款踏板，并将新的，更实惠的Tread Flex添加到折叠中。在纽约市的一次发布会上， Peloton首席执行官[…]" data-title="Peloton带着“更便宜”的折叠跑步机回来了" data-date="09-22 20:10" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-22 20:10</span>
          <span class="news-item-title">Peloton带着“更便宜”的折叠跑步机回来了</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/report/998501/apple-mac-mini-m6-price-mac-neo-concept" target="_blank" rel="noopener" data-cat="keji" data-summary="Mac Mini是一款很棒的小型台式电脑，当它的售价为599 $时，很容易推荐给任何想要快速、简单和便宜的东西的人。新的M6型号更好，但它的起价为$ 899 ，它的12核CPU和12核GPU实际上可能对那些[…]" data-title="是时候推出Mac NEO了" data-date="09-22 20:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-22 20:00</span>
          <span class="news-item-title">是时候推出Mac NEO了</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/desktops/gaming-pcs/gaming-pc-with-rtx-5060-32gb-of-ram-and-1tb-of-storage-gets-usd500-discount-neweggs-capable-abs-cyclone-aqua-prebuilt-is-usd1-199-with-code" target="_blank" rel="noopener" data-cat="keji" data-summary="Newegg预先构建的ABS Cyclone Aqua将英特尔的20核酷睿i7-14700F与英伟达的RTX 5060 8GB和32GB DDR4内存相结合，成本低于构建同类系统的成本" data-title="配备RTX 5060、32GB RAM和1TB存储空间的游戏PC可享受500 $的折扣— Newegg预建的ABS Cyclone Aqua功能为1,199 $ ，带代码" data-date="09-22 19:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-22 19:30</span>
          <span class="news-item-title">配备RTX 5060、32GB RAM和1TB存储空间的游戏PC可享受500 $的折扣— Newegg预建的ABS Cyclone Aqua功能为1,199 $ ，带代码</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/dram/dram-is-now-more-expensive-than-compute-chips-on-per-area-basis-ai-demand-drives-memory-die-value-past-leading-edge-silicon" target="_blank" rel="noopener" data-cat="keji" data-summary="与台积电的N3晶圆相比， DRAM制造商可能会获得更多的钱。" data-title="从每个区域来看，内存芯片现在比计算芯片更昂贵—人工智能需求推动DRAM芯片价值超过领先的硅" data-date="09-22 19:12" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-22 19:12</span>
          <span class="news-item-title">从每个区域来看，内存芯片现在比计算芯片更昂贵—人工智能需求推动DRAM芯片价值超过领先的硅</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/raspberry-pi/raspberry-pi-locks-boards-to-factory-ram-capacities-in-firmware-engineer-tells-diy-modders-dont-waste-your-time-trying-repairs-or-upgrades-company-cites-shady-reseller-scams" target="_blank" rel="noopener" data-cat="keji" data-summary="Raspberry Pi用户的固件被阻止更换其SBC上的RAM芯片以进行维修或升级。" data-title="Raspberry Pi将主板锁定到固件的工厂RAM容量—工程师告诉DIY改装商“不要浪费你的时间”尝试维修或升级，公司引用了阴暗的经销商骗局" data-date="09-22 19:07" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-22 19:07</span>
          <span class="news-item-title">Raspberry Pi将主板锁定到固件的工厂RAM容量—工程师告诉DIY改装商“不要浪费你的时间”尝试维修或升级，公司引用了阴暗的经销商骗局</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/494120.html" target="_blank" rel="noopener" data-cat="keji" data-summary="9月22日，在2026杭州云栖大会企业级Agent实践峰会上，基元律动联合创始人兼CTO韩凯发表演讲《从Harness到RSI飞轮》。" data-title="基元律动韩凯：从多模型调度到反馈闭环，探索Agent持续进化" data-date="09-22 18:06" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-22 18:06</span>
          <span class="news-item-title">基元律动韩凯：从多模型调度到反馈闭环，探索Agent持续进化</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/dram/chinas-cxmt-hits-12nm-class-dram-milestone-new-5th-gen-dram-tech-uses-quadruple-patterning-to-boost-die-capacity-by-50-percent" target="_blank" rel="noopener" data-cat="keji" data-summary="中国DRAM冠军CXMT已开始使用其第五代GEB DRAM工艺技术进行批量生产" data-title="中国的CXMT达到12纳米级DRAM里程碑—新的第5代DRAM技术使用四重图案将芯片容量提高50 ％" data-date="09-22 18:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-22 18:00</span>
          <span class="news-item-title">中国的CXMT达到12纳米级DRAM里程碑—新的第5代DRAM技术使用四重图案将芯片容量提高50 ％</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/openai-and-anthropic-are-reportedly-seeking-out-smaller-data-center-deals-to-meet-current-demand-20-30-mw-facilities-to-provide-capacity-as-mega-structures-undergo-construction" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI和Anthropic正在寻求通过规模较小的数据中心交易来确保即时容量，以满足当前的需求，尽管在其他地方的大规模交易上花费了数十亿美元。" data-title="随着大规模千兆瓦项目的滞后， OpenAI和Anthropic争夺较小的数据中心— 20-30兆瓦的设施，以提供大型结构正在建设中的容量" data-date="09-22 17:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-22 17:30</span>
          <span class="news-item-title">随着大规模千兆瓦项目的滞后， OpenAI和Anthropic争夺较小的数据中心— 20-30兆瓦的设施，以提供大型结构正在建设中的容量</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/493865.html" target="_blank" rel="noopener" data-cat="keji" data-summary="9月22日，在2026云栖大会“AI+文化传媒”技术发展论坛上，虎鲸文娱集团推出行业首个AI影视制作与管理平台“鲸锐AI”" data-title="虎鲸文娱推出“鲸锐AI”影视制作与管理平台，打造文娱产业新基建" data-date="09-22 16:49" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-22 16:49</span>
          <span class="news-item-title">虎鲸文娱推出“鲸锐AI”影视制作与管理平台，打造文娱产业新基建</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/493819.html" target="_blank" rel="noopener" data-cat="keji" data-summary="9月21日，首届中央企业量子人才科创空间产业应用创新大赛发布会在合肥举行" data-title="首届中央企业量子人才科创空间产业应用创新大赛在合肥举办 中央企业发布真实业务场景需求" data-date="09-22 16:35" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-22 16:35</span>
          <span class="news-item-title">首届中央企业量子人才科创空间产业应用创新大赛在合肥举办 中央企业发布真实业务场景需求</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/005/705.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 22 日消息，已经升级最新版 FSD（监督版）更新的特斯拉车主，在中控屏幕上遇到了一个恼人的异常问题。在升级至 14.3.9 版本之后，大量车主反馈车辆会频繁弹出警示，提示前置 FSD 摄像头脏污，要求车主前往服务中心检修；然而此时挡风玻璃与摄像头外壳实际上干干净净，没有任何污渍。所幸问题并非硬件损坏，摄像头本身并没有脏。用户 @CARN0N 在 X 平台发帖反映该现象，并且晒出特斯拉客服人员的回复，证实这类弹窗属于软件漏洞，特斯拉方面已经知晓该问题。报错背后的程序漏洞IT之家注意到，该故障是特斯拉本月早些时候推送 FSD v14.3.9 之后随即出现的。这一版本虽然新增了全新的自动碰撞避险功能，但同时引入了一个视觉编码器过度敏感的程序缺陷。该版本软件让神经网络的摄像头可视" data-title="误报摄像头脏污，特斯拉 FSD v14.3.9 出现软件漏洞" data-date="09-22 14:50" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-22 14:50</span>
          <span class="news-item-title">误报摄像头脏污，特斯拉 FSD v14.3.9 出现软件漏洞</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/493629.html" target="_blank" rel="noopener" data-cat="keji" data-summary="未来Qwen4.5、Qwen5等版本将扩展至5-10T参数。" data-title="阿里研究员透露Qwen4.5后模型将扩展至5" data-date="09-22 11:48" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-22 11:48</span>
          <span class="news-item-title">阿里研究员透露Qwen4.5后模型将扩展至5</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/493625.html" target="_blank" rel="noopener" data-cat="keji" data-summary="9月22日， 2026云栖大会开幕，阿里巴巴公布大模型最新进展。" data-title="阿里公布全模态模型新进展，Qwen4和下代视频模型均在训练中" data-date="09-22 11:42" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-22 11:42</span>
          <span class="news-item-title">阿里公布全模态模型新进展，Qwen4和下代视频模型均在训练中</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">9 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ckd68e40ze3jo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="米克尔·阿尔特塔同意与英超冠军阿森纳签订一份经过改进的新合同。" data-title="阿尔特塔同意与阿森纳冠军达成新协议" data-date="09-22 19:48" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-22 19:48</span>
          <span class="news-item-title">阿尔特塔同意与阿森纳冠军达成新协议</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/005/713.htm" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="IT之家 9 月 22 日消息，宝马集团今日宣布为旗下电动 MINI 品牌推出一款全新特别版车型，定名为“酷不列颠”版。MINI 酷不列颠特别版共推出 4 款车型，售价 20.88-32.08 万元。其中，MINI 酷不列颠收藏版限量 3 台，限时礼遇价 298888 元。该版本最大亮点在于将英国米字旗图案完整喷涂于整车车身，以此展现鲜明的英伦文化特征。据官方介绍，“酷不列颠”（Cool Britannia）源自 20 世纪 90 年代的英国文化浪潮。音乐、艺术、电影与时尚重新诠释传统英国元素，米字旗也由此成为鲜明的流行文化符号。MINI 将它铺展在车身上，既致敬英伦文化，也表达打破常规的个性。该车型车身采用不对称设计，一面完整的米字旗覆盖整个车体表面。喷涂工艺需在全车范围内进行三次喷漆作业" data-title="宝马 MINI 酷不列颠系列车型正式上市：20.88 万元起，手工打磨 74 条分色线" data-date="09-22 14:55" data-source="IT之家">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-22 14:55</span>
          <span class="news-item-title">宝马 MINI 酷不列颠系列车型正式上市：20.88 万元起，手工打磨 74 条分色线</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c51kxgj43n89o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="亚历杭德罗·加纳乔（ Alejandro Garnacho ）从切尔西（ Chelsea ）租借到阿斯顿维拉（ Aston Villa ） ，以开启他的职业生涯，但他在米德兰兹（ Midlands ）的最初几周一直" data-title="加纳乔（ Garnacho ）是否已经处于别墅的十字路口？" data-date="09-22 14:19" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-22 14:19</span>
          <span class="news-item-title">加纳乔（ Garnacho ）是否已经处于别墅的十字路口？</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c51kxgj43n89o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="亚历杭德罗·加纳乔（ Alejandro Garnacho ）从切尔西（ Chelsea ）租借到阿斯顿维拉（ Aston Villa ） ，以开启他的职业生涯，但他在米德兰兹（ Midlands ）的最初几周一直" data-title="切尔西在别墅板凳上挣扎-加纳乔面临着决定性的赛季" data-date="09-22 14:19" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-22 14:19</span>
          <span class="news-item-title">切尔西在别墅板凳上挣扎-加纳乔面临着决定性的赛季</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/21/premier-league-mega-product-brighton-arsenal-international-break" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="布莱顿本赛季的开局令人印象深刻，在一个仍然是一个残酷强大的吸引力的联赛中，为多巴胺崩溃做好准备。而这一个真的是一个真正的秋季暴跌。过去17天（包括周日截止日期）为我们带来了30场英超比赛和79个进球。如果你把马刺队排除在外，这是公平的，因为马刺队现在是后进球，一个与进球甚至足球无关的娱乐概念" data-title="很快回归英超联赛，无休止的超级产品| Barney Ronay" data-date="09-22 04:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-22 04:30</span>
          <span class="news-item-title">很快回归英超联赛，无休止的超级产品| Barney Ronay</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/21/long-range-hits-goals-galore-inside-premier-league-chaos" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="随着英超联赛的端到端足球接管分部，球队正在进一步发展，定位球罢工正在减少。混乱又回来了，端到端的足球又回来了。该部门在更多方面更加开放。数据显示，从上赛季的每场比赛2.75个进球上升到今年迄今为止的2.82个，这是一个小的平均增长–但可以很容易地扩大。每场比赛的进球率至少高出0.21个AC" data-title="各种远程命中和进球：英超联赛重返混乱|安德鲁·比斯利" data-date="09-22 00:45" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-22 00:45</span>
          <span class="news-item-title">各种远程命中和进球：英超联赛重返混乱|安德鲁·比斯利</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqrl6pe56348o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="加里·内维尔（ Gary Neville ）在周日富勒姆（ Fulham ）的1-1平局中称曼联“缺乏努力”是否正确？" data-title="内维尔指责曼联“缺乏努力”是正确的吗？" data-date="09-21 23:39" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-21 23:39</span>
          <span class="news-item-title">内维尔指责曼联“缺乏努力”是正确的吗？</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/21/tottenham-hotspur-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="对于Roberto De Zerbi的团队来说，季前赛对欧洲资格的想法已经开始显得令人困惑地乐观在这里注册我们的免费通讯3月，托特纳姆热刺担心可能降级，花费巨资引进Roberto De Zerbi ，他可能永远不会以更强大的手势进行谈判。有明显的改善，他们在赛季的最后一天熬夜。从那时起，马刺花费了净£ 1.75亿（ $ 2.34亿）" data-title="过去两个赛季对马刺来说是严峻的。这和以往一样糟糕|乔纳森·威尔逊" data-date="09-21 23:20" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-21 23:20</span>
          <span class="news-item-title">过去两个赛季对马刺来说是严峻的。这和以往一样糟糕|乔纳森·威尔逊</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/21/to-minimise-the-risks-to-young-football-players-we-should-ban-agents-recruiting-under-18s" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Phil Murray responds to articles about the precarious path talented young athletes faceJonathan Liew’s piece (Raheem Sterling’s bleak tale a reminder of absurd path young footballers face, 17 September) is informative and timely, particularly when set against Jacob Steinberg’s report (‘They are very similar’: Arsenal’s Dowman reminds Merino of Lami" data-title="为了最大限度地减少年轻足球运动员的风险，我们应该禁止代理商招募" data-date="09-21 23:01" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-21 23:01</span>
          <span class="news-item-title">为了最大限度地减少年轻足球运动员的风险，我们应该禁止代理商招募</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/005/948.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 22 日消息，OPPO 33W 口袋充超级闪充移动电源 10000 现已开售，容量 10000mAh，售价 149 元。这款移动电源重约 204g，尺寸为 110.6×70.6×18.1mm，有卡其香氛和轻盈粉两种颜色可选；获得 2026 新国标认证，支持 ColorOS 系统级互联生态，可查看移动电源的剩余电量、电池健康度、实时温度等信息。这款移动电源配备 A + C 双口输出，兼容 SUPERVOOC、PD、PPS、QC、UFCS 等协议；USB-C 单口和 USB-A 单口最大功率均为 33W ，双口同时输出时最高为 5V 4A；支持自动识别小电流设备，可为智能手表、耳机、手环等小设备稳定充电。这款产品附赠了一条长度 0.2m 的 3A 手提充电线，采用高密度编织材质" data-title="OPPO 33W 口袋充移动电源 10000 开售：新国标、A+C 双口，149 元" data-date="09-22 20:44" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-22 20:44</span>
          <span class="news-item-title">OPPO 33W 口袋充移动电源 10000 开售：新国标、A+C 双口，149 元</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/005/947.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 22 日消息，OPPO 今晚召开新品发布会，推出 Find X10 系列新品。除手机产品以外，OPPO 还在发布会带来了 Watch S2 和 Watch X3 手表。新品可选多种配色，采用超薄机身，首次搭载超燃脂模式，升级旗舰健康传感器，定价 1599 元起，9 月 24 日开售。IT之家附 OPPO 新品手表定价如下：OPPO Watch S2：建议零售价 1599 元，首销 1499 元，国补到手价 1274.15 元OPPO Watch X3：建议零售价 2799 元，首销优惠价 2599 元，国补到手价 2209.15 元据介绍，这款手表采用 8.9mm 轻薄设计，可选跃动橙、薄雾粉、山影灰三种配色，拥有竹节运动表带，贴合度提升 15%，厚度减少 19%。运动方面" data-title="1599 元起：OPPO Watch S2/X3 手表发布，8.9mm 轻薄设计、首次搭载超燃脂模式" data-date="09-22 20:43" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-22 20:43</span>
          <span class="news-item-title">1599 元起：OPPO Watch S2/X3 手表发布，8.9mm 轻薄设计、首次搭载超燃脂模式</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/005/946.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 22 日消息，在今晚的 OPPO Find X10 系列新品发布会上，OPPO 还发布了 OPPO Enco X4 耳机，建议零售价 1199 元，首销优惠价 1099 元。据IT之家在发布会现场了解到，OPPO 携手北欧丹拿调音大师联合调音，带来首款“无损丹拿音质”耳机，支持至高 2.3Mbps 高保真无损传输，支持 48kHz/24bit 无损音源规格。OPPO Enco X4 采用第四代同轴双单元结构，双 DAC 分频驱动，音乐层次更分明，超瞬态高分子振膜，鼓点有力不拖沓，同心圆对称磁路，弦乐清透又细腻，全频段低失真，全链路真无损。OPPO Enco X4 芯片制程由上代 12nm 提升至 6nm，全频段降噪及人声降噪能力相较上代全面提升，并采用全新发泡硅胶耳帽，支持" data-title="OPPO Enco X4 耳机发布：无损丹拿音质，首销价 1099 元" data-date="09-22 20:42" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-22 20:42</span>
          <span class="news-item-title">OPPO Enco X4 耳机发布：无损丹拿音质，首销价 1099 元</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-22/10701716.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网银川9月22日电 (记者 李佩珊)金秋时节，宁夏银川市永宁县李俊镇3000余亩麦后复种油葵次第绽放，连片金色花海随风摇曳，勾勒出诗意盎然的田园画卷，成为秋日乡村独特景致。不少市民、游客慕名前来，漫步田间步道，沉浸式欣赏田园风光，驻足拍照打卡，惬意尽享秋日乡村美景。" data-title="宁夏永宁：金色花海映乡野 走出农旅融合新路径" data-date="09-22 20:38" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 20:38</span>
          <span class="news-item-title">宁夏永宁：金色花海映乡野 走出农旅融合新路径</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/005/944.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 22 日消息，OPPO 今晚召开新品发布会，推出 Find X10 标准版手机。新品搭载联发科天玑 9600M 旗舰芯片，配备 8000mAh 冰川电池，拥有新一代 1nit 明眸护眼屏，采用双 2 亿镜头群方案，定价 5499 元起，9 月 24 日起开售。IT之家附 OPPO Find X10 手机各版本定价如下：12+256GB：5499 元12+512GB：5999 元16+512GB：6499 元16+1TB：7499 元IT之家在发布会现场了解到，OPPO Find X10 手机可选冰蓝、清橙、浅钛三种配色，正面拥有 0.99mm 极窄四等边屏幕，带来更沉浸的视觉感受。侧面采用微光金属中框，拥有细腻触感。背面配备绒光玻璃材质，带来通透视觉感受及亲肤触感。支持 I" data-title="5499 元起：OPPO Find X10 标准版手机发布，天玑 9600M 芯片、双 2 亿镜头群" data-date="09-22 20:38" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-22 20:38</span>
          <span class="news-item-title">5499 元起：OPPO Find X10 标准版手机发布，天玑 9600M 芯片、双 2 亿镜头群</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/005/943.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 22 日消息，在今晚的 OPPO Find X10 系列新品发布会上，OPPO Find X10 Pro Max 正式发布，OPPO 称这不只是 Find 的第一台 Pro Max，更是一台大家前所未见的相机。OPPO Find X10 Pro Max 售价 6799 元起。IT之家附具体售价如下：12+256GB 售价 6799 元12+512GB 售价 7499 元16+512GB 售价 7999 元16GB+1TB 售价 8999 元据IT之家在发布会现场了解到，外观方面，OPPO Find X10 Pro Max 背板拥有哈苏影像印迹，汲取经典相机材质分区灵感，呈现金属平纹与立体编织两种质感，让视觉层次更丰富。贯穿镜头模组的橙光印记，灵感源自经典哈苏相机。银色金属齿" data-title="OPPO Find X10 Pro Max 发布：首发三 2 亿像素镜头群，售价 6799 元起" data-date="09-22 20:37" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-22 20:37</span>
          <span class="news-item-title">OPPO Find X10 Pro Max 发布：首发三 2 亿像素镜头群，售价 6799 元起</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/005/942.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 22 日消息，OPPO 今天召开新品发布会，除了推出 Find X10 系列手机新品以外，OPPO 本次还带来了全新品类穿戴产品“AI 心力球”。新品体验价为 499 元，主打卖点是“AI 成长教练”，能够帮助用户思考，把事情做成。即日起开启用户招募。IT之家在发布会现场了解到，OPPO AI 心力球是一款别在衣服领口的穿戴产品。其重量为 9.8g，支持 24 小时全天续航、5 米远距离收音。" data-title="OPPO 推出“AI 心力球”可穿戴新品，体验价 499 元" data-date="09-22 20:35" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-22 20:35</span>
          <span class="news-item-title">OPPO 推出“AI 心力球”可穿戴新品，体验价 499 元</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/005/941.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 22 日消息，岚图梦想家 9 于今天（22 日）晚间正式上市，新车定位“新时代旗舰 MPV”，售价区间为 41.99 万元至 51.99 万元，提供 Ultra、Ultra+ 和礼尊版三个版型，涵盖插混和纯电两种动力形式，共计 6 个配置。礼尊版：PHEV 51.99 万元，EV 52.99 万元Ultra+ 版：PHEV 45.99 万元，EV 46.99 万元Ultra 版：PHEV 41.99 万元，EV 42.99 万元IT之家附上官方介绍如下图：外观方面，梦想家 9 延续家族直瀑式中网设计，配备全球首款可升降发光立标 —— 由 2520 组精密切割工艺打造，支持自行调节升降及发光，配合 HUAWEI XPIXEL 双百万像素全彩智慧大灯（双侧总像素达 260 万，" data-title="岚图梦想家 9“新时代旗舰 MPV”上市，41.99 万" data-date="09-22 20:34" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-22 20:34</span>
          <span class="news-item-title">岚图梦想家 9“新时代旗舰 MPV”上市，41.99 万</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-22/10701715.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网大同9月22日电 (白杨 刘小红)近日，山西大同灵丘县一合作社开展西兰花集中采收工作，田间地头有序开展采摘、装筐、转运作业。本地种植的西兰花经统一加工处理，批量发往海外市场，带动村民就近务工增收。" data-title="（乡村行·看振兴）山西灵丘西兰花远销海外促增收" data-date="09-22 20:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 20:30</span>
          <span class="news-item-title">（乡村行·看振兴）山西灵丘西兰花远销海外促增收</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-22/10701710.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网合肥9月22日电 (赵强 许乃见)2026年安徽省无人机测绘职业技能竞赛22日在合肥开幕。这是安徽省首次举办以实际应用为主的无人机测绘职业技能竞赛，来自全省各地及中铁四局重点建设工程的20支代表队、80名选手同台竞技。" data-title="安徽省首办无人机测绘职业技能竞赛 80名选手合肥同台竞技" data-date="09-22 20:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 20:29</span>
          <span class="news-item-title">安徽省首办无人机测绘职业技能竞赛 80名选手合肥同台竞技</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/998688/oppo-find-x10-pro-max-200-megapixel-cameras-china" target="_blank" rel="noopener" data-cat="zonghe" data-summary="今天在中国推出的OPPO全新Find X10 Pro Max旗舰手机是首款在所有三个后置摄像头上使用2亿像素传感器的手机。主摄像头的17档动态范围，得益于Oppo所谓的“DeepPix传感器技术” ，表明百万像素计数将不是这款摄像头唯一的[…]" data-title="OPPO的新手机是第一款有三个200" data-date="09-22 20:18" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-22 20:18</span>
          <span class="news-item-title">OPPO的新手机是第一款有三个200</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-22/10701684.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="新闻发布会现场。张钰佳 摄 中新网晋中9月22日电(高雨晴)“此次中秋国庆，我们以乔家大院、昭余古城两大核心景区为主阵地，精心策划了一系列形式多样、内涵丰富的主题活动，致力于为游客打造一场穿越古今、融汇文脉的沉浸式文旅体验。”山西晋中祁县文旅局旅游工作负责人白云22日介绍。" data-title="山西祁县中秋国庆文旅活动发布 乔家大院、昭余古城联动迎客" data-date="09-22 20:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 20:17</span>
          <span class="news-item-title">山西祁县中秋国庆文旅活动发布 乔家大院、昭余古城联动迎客</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-22/10701781.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社北京9月22日电 (记者 陈杭)第四次全国文物普查进入省域验收、成果总结收官阶段，不可移动文物数量有望突破90万处；全国老城文物等专项调查全面完成，文物资源家底基本摸清。" data-title="中国国家文物局：中国不可移动文物数量有望突破90万处" data-date="09-22 20:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 20:17</span>
          <span class="news-item-title">中国国家文物局：中国不可移动文物数量有望突破90万处</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-22/10701675.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网永州9月22日电(蒋军君 周林凤 谢欣怡)中秋节、国庆节临近，在湖南省新田县新隆镇城塘溪村，某秋葵面业公司门前晒场铺开一片“绿金”：几千斤秋葵整齐排列，秋日阳光洒下，空气里混着麦香与秋葵清香。厂房内，负责人谢艳军带着工人赶制5000余斤秋葵面订单，压面、切面、上架、晾晒，一派忙碌的景象。" data-title="七分熟秋葵“入面” 湖南新田晒出乡村振兴好“钱”景" data-date="09-22 20:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 20:10</span>
          <span class="news-item-title">七分熟秋葵“入面” 湖南新田晒出乡村振兴好“钱”景</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-22/10701774.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社西宁9月22日电 (祁增蓓)青海、西藏、四川、云南、甘肃五省区22日联合在青海省西宁市发布《五省区野生冬虫夏草资源保护行动宣言》，划定五条行动红线，协同守护青藏高原高寒草甸生态与野生冬虫夏草种质资源。" data-title="中国五省区联合发布野生冬虫夏草资源保护行动宣言" data-date="09-22 20:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-22 20:10</span>
          <span class="news-item-title">中国五省区联合发布野生冬虫夏草资源保护行动宣言</span>
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


<p class="news-updated">🕐 抓取更新于 2026-09-22 20:45（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
