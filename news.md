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
      <span>2026-10-04 15:31 抓取更新</span>
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
        <span class="channel-count">47</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('shizheng', this)">
        <span>🏛️ 时政与国际</span>
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('keji', this)">
        <span>🤖 AI模型 & 芯片算力</span>
        <span class="channel-count">14</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('zuqiu', this)">
        <span>⚽ 英超与足球风云</span>
        <span class="channel-count">3</span>
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
  <div class="ov-item"><span class="ov-num">47</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×24 · IT之家×5</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/10-04/10707805.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="2021年5月，在河南省淅川县九重镇邹庄村，习近平总书记走进移民户邹新曾家。通过种田、务工和电商直播，这家的日子红红火火。" data-title="总书记治国理政故事｜“人民就是江山”" data-date="10-04 15:01" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-04 15:01</span>
      </div>
      <h2 class="hero-featured-title">总书记治国理政故事｜“人民就是江山”</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.qbitai.com/2026/10/501605.html" target="_blank" rel="noopener" data-cat="keji" data-summary="一种混搭的可能：英特尔继续供先进工艺，即前端用14A；后端再接台积电，来补工厂运营、良率、封装这些能力。" data-title="AI算力硬合作，马斯克还是更相信中国制造" data-date="10-04 14:12" data-source="量子位">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-techcrunch">🧠 量子位</span>
      </div>
      <p class="hero-sub-title">AI算力硬合作，马斯克还是更相信中国制造</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/2026/oct/03/blank-instead-manchester-city-name-trophies-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="这些空间既是对贪婪时代的谴责，也是对英超联赛追求正义的致敬在2014年联赛杯决赛中场休息时，桑德兰以1比0领先曼城。Yaya Touré与休闲明亮的30码相媲美" data-title="Let there be blanks instead of Manchester City’s name on trophies: there was no honour there | Jonathan Wilson" data-date="10-04 03:00" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Let there be blanks instead of Manchester City’s name on trophies: there was no honour there | Jonathan Wilson</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/10-04/10707819.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="头顶是新疆艾德莱斯绸铺展出的斑斓色彩，" data-title="星巴克来到新疆，成为“星巴扎”" data-date="10-04 15:24" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">星巴克来到新疆，成为“星巴扎”</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707805.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="2021年5月，在河南省淅川县九重镇邹庄村，习近平总书记走进移民户邹新曾家。通过种田、务工和电商直播，这家的日子红红火火。" data-title="总书记治国理政故事｜“人民就是江山”" data-date="10-04 15:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 15:01</span>
          <span class="news-item-title">总书记治国理政故事｜“人民就是江山”</span>
          <span class="news-value-point">💡 2021年5月，在河南省淅川县九重镇邹庄村，习近平总书记走进移民户邹新曾家</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707803.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月4日电 据日媒报道，日本首相高市早苗4日就驻日美军涉嫌杀人案在社交平台上发帖称，发生如此残忍、恶劣的案件，令人感到极为遗憾。" data-title="高市早苗就驻日美军涉嫌杀人案表示“极为遗憾” 小泉进次郎怒斥“不可容忍”" data-date="10-04 14:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 14:33</span>
          <span class="news-item-title">高市早苗就驻日美军涉嫌杀人案表示“极为遗憾” 小泉进次郎怒斥“不可容忍”</span>
          <span class="news-value-point">💡 中新网10月4日电 据日媒报道，日本首相高市早苗4日就驻日美军涉嫌杀人案在社交平台上发帖称，发生如此残忍、恶劣的案件，令人感到极为遗憾</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707785.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社柏林10月4日电 德国埃森消息：当地时间10月3日，2026年中德青少年交流音乐会暨“唱歌学中文”夏令营汇报演出在德国埃森举行。40名中德学生登台表演，近200名观众到场观看。" data-title="2026年中德青少年交流音乐会在德国埃森举行" data-date="10-04 13:46" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 13:46</span>
          <span class="news-item-title">2026年中德青少年交流音乐会在德国埃森举行</span>
          <span class="news-value-point">💡 中新社柏林10月4日电 德国埃森消息：当地时间10月3日，2026年中德青少年交流音乐会暨“唱歌学中文”夏令营汇报演出在德国埃森举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707766.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月4日电 据法新社援引美国方面当地时间3日消息，美国官员透露，出席纽约联合国大会的伊朗代表团两名成员于3日被“驱逐”出境，此前几天他们已被要求离开美国。" data-title="美官员称两名伊朗代表团成员被“驱逐”出境 二人曾出席纽约联合国大会" data-date="10-04 12:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 12:36</span>
          <span class="news-item-title">美官员称两名伊朗代表团成员被“驱逐”出境 二人曾出席纽约联合国大会</span>
          <span class="news-value-point">💡 中新网10月4日电 据法新社援引美国方面当地时间3日消息，美国官员透露，出席纽约联合国大会的伊朗代表团两名成员于3日被“驱逐”出境，此前几天他们…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707765.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="视频：方志里的长征故事 | 方向是一步步走出来的来源：中国社会科学网" data-title="方志里的长征故事 | 方向是一步步走出来的" data-date="10-04 12:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 12:32</span>
          <span class="news-item-title">方志里的长征故事 | 方向是一步步走出来的</span>
          <span class="news-value-point">💡 视频：方志里的长征故事 | 方向是一步步走出来的来源：中国社会科学网</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707759.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="视频：听英雄后代讲长征故事|孙继先之子回望强渡大渡河来源：新华网" data-title="听英雄后代讲长征故事|孙继先之子回望强渡大渡河" data-date="10-04 11:58" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 11:58</span>
          <span class="news-item-title">听英雄后代讲长征故事|孙继先之子回望强渡大渡河</span>
          <span class="news-value-point">💡 视频：听英雄后代讲长征故事|孙继先之子回望强渡大渡河来源：新华网</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707757.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="视频：【红星照耀中国】胜利的方向丨从泸定桥的摇晃里，读懂十三根铁索上的浴血冲锋来源：中国军网" data-title="【红星照耀中国】胜利的方向丨从泸定桥的摇晃里，读懂十三根铁索上的浴血冲锋" data-date="10-04 11:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 11:52</span>
          <span class="news-item-title">【红星照耀中国】胜利的方向丨从泸定桥的摇晃里，读懂十三根铁索上的浴血冲锋</span>
          <span class="news-value-point">💡 视频：【红星照耀中国】胜利的方向丨从泸定桥的摇晃里，读懂十三根铁索上的浴血冲锋来源：中国军网</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707756.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="历经4年建设，平陆运河近日全线通航。这是新中国成立以来第一条国家层面统筹建设的通江达海的大运河，其工程规模、创新技术、重大意义等引发外媒热议。" data-title="外媒热议平陆运河全线通航" data-date="10-04 11:51" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 11:51</span>
          <span class="news-item-title">外媒热议平陆运河全线通航</span>
          <span class="news-value-point">💡 历经4年建设，平陆运河近日全线通航</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707751.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网济南10月4日电 (刘驰原)在济南市莱芜区凤城街道便民服务中心，65岁的王秀花指尖轻触政务服务自助终端，在现场工作人员“一对一”的细致引导下，原本让她“头疼”的社会保险待遇资格认证在几分钟内便顺利办结。过去，为了这项认证，她远在外地工作的儿子往往需要专门请假赶回。如今，这种“折腾”已成为历史。" data-title="山东深化数字政府建设 推动政务服务“好办易办”" data-date="10-04 11:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 11:44</span>
          <span class="news-item-title">山东深化数字政府建设 推动政务服务“好办易办”</span>
          <span class="news-value-point">💡 中新网济南10月4日电 (刘驰原)在济南市莱芜区凤城街道便民服务中心，65岁的王秀花指尖轻触政务服务自助终端，在现场工作人员“一对一”的细致引导…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707753.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="国庆假期，太空出差三人组——神二十三乘组航天员朱杨柱、张志远、黎家盈仍在中国空间站值守。三名航天员在轨驻留已四月有余，中秋国庆期间，他们将站内环境布置得温馨喜庆，同时，空间科学实(试)验、空间站组合体平台照料、健康管理等各项工作有序推进。" data-title="神二十三乘组太空过双节 科学实验、健康管理等工作正推进" data-date="10-04 11:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 11:44</span>
          <span class="news-item-title">神二十三乘组太空过双节 科学实验、健康管理等工作正推进</span>
          <span class="news-value-point">💡 国庆假期，太空出差三人组——神二十三乘组航天员朱杨柱、张志远、黎家盈仍在中国空间站值守</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707736.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月4日电 据外媒当地时间3日援引巴西方面消息，巴西总统卢拉的竞选团队已请求巴西最高选举法院，将美国驻巴西使领馆2日暂停线下领事服务一事，纳入正在进行的外部势力干预巴西选举相关调查。" data-title="卢拉竞选团队请求巴西最高选举法院调查美使领馆暂停服务一事" data-date="10-04 11:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 11:09</span>
          <span class="news-item-title">卢拉竞选团队请求巴西最高选举法院调查美使领馆暂停服务一事</span>
          <span class="news-value-point">💡 中新网10月4日电 据外媒当地时间3日援引巴西方面消息，巴西总统卢拉的竞选团队已请求巴西最高选举法院，将美国驻巴西使领馆2日暂停线下领事服务一事…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707731.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="记者日前从司法部获悉，目前全国共有人民调解委员会69.7万个，其中村(社区)调委会61.2万个，乡镇(街道)调委会4万个；行业性专业性调委会和工作室5.4万个；全国共有人民调解员310.2万人，其中专职调解员56万人，基本形成覆盖城乡社区和重点领域、单位的调解组织网络。2025年，共调解各类案件1653.7万件，调解成功率96.5%，调解协议履行率94%。" data-title="司法部：2025年共调解各类案件1653.7万件" data-date="10-04 11:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 11:02</span>
          <span class="news-item-title">司法部：2025年共调解各类案件1653.7万件</span>
          <span class="news-value-point">💡 记者日前从司法部获悉，目前全国共有人民调解委员会69.7万个，其中村(社区)调委会61.2万个，乡镇(街道)调委会4万个</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707718.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月4日电 据日媒4日报道，3日那霸市一家酒店发生了一起女性遇害、随身物品被抢走的案件。" data-title="日媒：涉嫌抢劫杀人 一名驻日美军士兵被日本警方逮捕" data-date="10-04 10:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 10:11</span>
          <span class="news-item-title">日媒：涉嫌抢劫杀人 一名驻日美军士兵被日本警方逮捕</span>
          <span class="news-value-point">💡 中新网10月4日电 据日媒4日报道，3日那霸市一家酒店发生了一起女性遇害、随身物品被抢走的案件</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/03/us/trump-tom-cotton-cellphone-number.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="总统敦促人们打电话给阿肯色州参议员汤姆·科顿（ Tom Cotton ） ，并指责他阻止了一项旨在巩固夏令时的法案。" data-title="Here’s Senator Cotton’s Cell Number, Trump Says, in Dispute Over Daylight Saving Bill" data-date="10-04 09:59" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-04 09:59</span>
          <span class="news-item-title">特朗普说，这是参议员棉花的手机号码，在夏令时法案的争议中</span>
          <span class="news-item-title-en">Here’s Senator Cotton’s Cell Number, Trump Says, in Dispute Over Daylight Saving Bill</span>
          <span class="news-value-point">💡 总统敦促人们打电话给阿肯色州参议员汤姆·科顿（ Tom Cotton ） ，并指责他阻止了一项旨在巩固夏令时的法案</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707705.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="日本多个民间团体3日在东京江户川区联合举办“战争展”，展示日本在二战期间发动侵略战争的历史资料，呼吁日本社会坚守和平，反对高市政府扩军修宪动向。主办方表示，希望这些展示，能够让日本民众正确了解历史，阻止日本再次走上战争道路。" data-title="日本民间团体展示侵略战争史料 呼吁日本社会坚守和平" data-date="10-04 09:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 09:29</span>
          <span class="news-item-title">日本民间团体展示侵略战争史料 呼吁日本社会坚守和平</span>
          <span class="news-value-point">💡 日本多个民间团体3日在东京江户川区联合举办“战争展”，展示日本在二战期间发动侵略战争的历史资料，呼吁日本社会坚守和平，反对高市政府扩军修宪动向</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">14 条</span>
    </div>
        <a class="news-item" href="https://www.qbitai.com/2026/10/501605.html" target="_blank" rel="noopener" data-cat="keji" data-summary="一种混搭的可能：英特尔继续供先进工艺，即前端用14A；后端再接台积电，来补工厂运营、良率、封装这些能力。" data-title="AI算力硬合作，马斯克还是更相信中国制造" data-date="10-04 14:12" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-04 14:12</span>
          <span class="news-item-title">AI算力硬合作，马斯克还是更相信中国制造</span>
          <span class="news-value-point">💡 一种混搭的可能：英特尔继续供先进工艺，即前端用14A</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/501506.html" target="_blank" rel="noopener" data-cat="keji" data-summary="什么是FDE？它会一直存在吗？" data-title="最火AI岗位FDE：月薪5万，都干这些…" data-date="10-04 14:05" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-04 14:05</span>
          <span class="news-item-title">最火AI岗位FDE：月薪5万，都干这些…</span>
          <span class="news-value-point">💡 什么是FDE</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/501451.html" target="_blank" rel="noopener" data-cat="keji" data-summary="专业3D模型反而更稀缺了" data-title="GPT-6要“吃掉”3D公司？这家公司不到2年ARR翻百倍，破1亿美元" data-date="10-04 08:53" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-04 08:53</span>
          <span class="news-item-title">GPT-6要“吃掉”3D公司？这家公司不到2年ARR翻百倍，破1亿美元</span>
          <span class="news-value-point">💡 专业3D模型反而更稀缺了</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/service-providers/streaming/7-year-old-nvidia-shield-tv-pro-gets-shocking-50-percent-price-hike-driven-by-ai-memory-shortage-chipmaker-axes-entry-level-shield-tv-as-component-prices-soar" target="_blank" rel="noopener" data-cat="keji" data-summary="Shield TV Pro仍然是英伟达运行时间最长的消费设备之一，但其299.99 $的价格标签现在使流媒体盒比推出时贵得多。" data-title="7-year-old Nvidia Shield TV Pro gets shocking 50% price hike driven by AI memory shortage" data-date="10-04 00:59" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-04 00:59</span>
          <span class="news-item-title">7年历史的Nvidia Shield TV Pro在人工智能内存短缺的推动下，价格上涨了50% ，令人震惊</span>
          <span class="news-item-title-en">7-year-old Nvidia Shield TV Pro gets shocking 50% price hike driven by AI memory shortage</span>
          <span class="news-value-point">💡 Shield TV Pro仍然是英伟达运行时间最长的消费设备之一，但其299.99 $的价格标签现在使流媒体盒比推出时贵得多</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/games/1004418/capcom-ai-game-development" target="_blank" rel="noopener" data-cat="keji" data-summary="Capcom的Pragmata可能完全是关于人工智能的恐怖，但在实践中，工作室似乎并不那么低调。在CAPCOM公开会议RE: 2026期间，程序员Satoshi Ishida发表了一篇演讲，题目是： “The Outlook a" data-title="Capcom is preparing for a ‘future where we create games together with AI’" data-date="10-04 00:49" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-04 00:49</span>
          <span class="news-item-title">Capcom正在为“我们与人工智能一起创造游戏的未来”做准备</span>
          <span class="news-item-title-en">Capcom is preparing for a ‘future where we create games together with AI’</span>
          <span class="news-value-point">💡 Capcom的Pragmata可能完全是关于人工智能的恐怖，但在实践中，工作室似乎并不那么低调</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/03/openai-safety-employee-resigns-claiming-the-companys-culture-is-broken/" target="_blank" rel="noopener" data-cat="keji" data-summary="大卫·罗宾逊（ David Robinson ）自己承认，他“有些陈词滥调” ：一家领先的人工智能公司的员工在辞职时发出可怕的警告。" data-title="OpenAI safety employee resigns, claiming the company’s ‘culture is broken’" data-date="10-04 00:30" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-04 00:30</span>
          <span class="news-item-title">OpenAI安全员工辞职，声称公司的“文化被打破”</span>
          <span class="news-item-title-en">OpenAI safety employee resigns, claiming the company’s ‘culture is broken’</span>
          <span class="news-value-point">💡 大卫·罗宾逊（ David Robinson ）自己承认，他“有些陈词滥调” ：一家领先的人工智能公司的员工在辞职时发出可怕的警告</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/580.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 4 日消息，在 10 月 1 日的华为 Mate 90 系列及全场景新品发布会上，华为年度旗舰 Mate 90 系列手机正式发布。其中，Mate 90 Pro Max / RS 非凡大师搭载的是首款逻辑折叠 τ 芯片 —— 麒麟 9050 Pro。根据华为官方介绍，麒麟 9050 Pro 是麒麟性能新巅峰，通过软硬芯云垂直整合，整机性能提升 31%。这枚芯片 CPU 还支持 9 核 16 线程超线程技术，多核性能提升 23%、GPU 渲染性能提升 40%、NPU 性能提升 140%。极客湾发布了一期针对华为 Mate 90 Pro Max 的性能分析报告，讲解了麒麟 9050 Pro 的逻辑折叠是如何实现，并公开了 Mate 90 Pro Max 的实际性能续航表现。需要" data-title="华为 Mate 90 Pro Max 性能解禁：搭载麒麟 9050 Pro，部分游戏能效优于第五代骁龙 8 至尊版机型" data-date="10-04 00:20" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-04 00:20</span>
          <span class="news-item-title">华为 Mate 90 Pro Max 性能解禁：搭载麒麟 9050 Pro，部分游戏能效优于第五代骁龙 8 至尊版机型</span>
          <span class="news-value-point">💡 IT之家 10 月 4 日消息，在 10 月 1 日的华为 Mate 90 系列及全场景新品发布会上，华为年度旗舰 Mate 90 系列手机正式…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/elon-musk-confirms-discussions-with-tsmc-about-terafab-chipmaking-collaboration-intel-is-the-only-other-named-partner-terafab-to-exclusively-supply-tesla-spacex-and-xai" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道， Elon Musk和台积电讨论了Terafab项目中的多个合作机会。" data-title="Elon Musk confirms discussions with TSMC about Terafab chipmaking collaboration" data-date="10-03 22:50" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-03 22:50</span>
          <span class="news-item-title">Elon Musk确认与台积电就Terafab芯片制造合作进行讨论</span>
          <span class="news-item-title-en">Elon Musk confirms discussions with TSMC about Terafab chipmaking collaboration</span>
          <span class="news-value-point">💡 据报道， Elon Musk和台积电讨论了Terafab项目中的多个合作机会</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/576.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 3 日消息，海马云 (haimacloud) 近日推出了 haimacloud GEAR 端云混合掌机。其本地采用高通骁龙 865 移动平台，运行 Android 13 操作系统，支持海马云的云游戏服务。该掌机拥有 8GB + 128GB 的存储器组合，搭配 7&quot; FHD 144Hz 2ms 800nits OLED 屏幕，内置 8000mAh 电池，具备主动散热、TMR 摇杆、霍尔扳机、机械微动按键、六轴体感，ABXY 为模块化设计，支持 Wi-Fi 6 &amp; BT 5.1，质量 450g。IT之家获悉，配套的云游戏服务基于英特尔酷睿 i7-12700KF 处理器、&quot;70&quot; 级 NVIDIA GeForce RTX 显卡，支持 1080p 144FPS。haimaclou" data-title="海马云推出 haimacloud GEAR 端云混合掌机：高通骁龙 865，硬件首发价 3149 元" data-date="10-03 22:47" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-03 22:47</span>
          <span class="news-item-title">海马云推出 haimacloud GEAR 端云混合掌机：高通骁龙 865，硬件首发价 3149 元</span>
          <span class="news-value-point">💡 IT之家 10 月 3 日消息，海马云 (haimacloud) 近日推出了 haimacloud GEAR 端云混合掌机</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1004408/openai-safety-quits-sounding-the-alarm" target="_blank" rel="noopener" data-cat="keji" data-summary="大卫·罗宾逊（ David Robinson ）曾在OpenAI的每个主要模型版本中撰写安全报告。本周，他辞去了职务，现在正在《大西洋月刊》的一篇社论中发表讲话。如果你觉得有点愤世嫉俗是可以理解的" data-title="An OpenAI safety employee has quit and is sounding the alarm" data-date="10-03 22:31" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-03 22:31</span>
          <span class="news-item-title">OpenAI安全员工已辞职并正在敲响警钟</span>
          <span class="news-item-title-en">An OpenAI safety employee has quit and is sounding the alarm</span>
          <span class="news-value-point">💡 大卫·罗宾逊（ David Robinson ）曾在OpenAI的每个主要模型版本中撰写安全报告</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/03/all-the-ai-agents-that-can-live-in-your-text-messages/" target="_blank" rel="noopener" data-cat="keji" data-summary="我们创建了一个列表，列出了可以在短信中出现的最著名的人工智能客服代表，从一般助理到专为家庭、旅行和工作而设计的客服代表。" data-title="All the AI agents that can live in your text messages" data-date="10-03 22:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-03 22:00</span>
          <span class="news-item-title">所有可以存在于您的短信中的人工智能代理</span>
          <span class="news-item-title-en">All the AI agents that can live in your text messages</span>
          <span class="news-value-point">💡 我们创建了一个列表，列出了可以在短信中出现的最著名的人工智能客服代表，从一般助理到专为家庭、旅行和工作而设计的客服代表</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/this-week-on-toms-hardware-premium-october-3-2026-ai-chip-design-week-openai-interview-and-ai-agent-safety" target="_blank" rel="noopener" data-cat="keji" data-summary="本周在Tom&#39;s Hardware Premium上，我们通过免费访问的芯片设计周打开了闸门，包括专家访谈、与OpenAI坐下来讨论其定制ASIC等等。" data-title="This week on Tom&#39;s Hardware Premium: October 3, 2026" data-date="10-03 22:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-03 22:00</span>
          <span class="news-item-title">本周Tom's Hardware Premium ： 2026年10月3日</span>
          <span class="news-item-title-en">This week on Tom's Hardware Premium: October 3, 2026</span>
          <span class="news-value-point">💡 本周在Tom's Hardware Premium上，我们通过免费访问的芯片设计周打开了闸门，包括专家访谈、与OpenAI坐下来讨论其定制ASI…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/futurum-ceo-says-agents-use-ai-5x-more-than-humans-number-will-eventually-hit-10x-but-agents-are-mostly-rereading-what-theyve-already-seen" target="_blank" rel="noopener" data-cat="keji" data-summary="Daniel Newman的数据来自OpenRouter数据，其中代理商在2月份超过了人类，并在8月份增长了14倍。" data-title="AI agents use 5x more tokens than humans as cached prompts explode, headed for 10x" data-date="10-03 21:10" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-03 21:10</span>
          <span class="news-item-title">随着缓存提示爆炸，人工智能代理使用的代币数量比人类多5倍，达到10倍</span>
          <span class="news-item-title-en">AI agents use 5x more tokens than humans as cached prompts explode, headed for 10x</span>
          <span class="news-value-point">💡 Daniel Newman的数据来自OpenRouter数据，其中代理商在2月份超过了人类，并在8月份增长了14倍</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/501381.html" target="_blank" rel="noopener" data-cat="keji" data-summary="岗位JD甩了篇技术报告" data-title="DeepSeek扩招！弹性计算团队大量HC，尤其需要资深工程师" data-date="10-03 15:54" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-03 15:54</span>
          <span class="news-item-title">DeepSeek扩招！弹性计算团队大量HC，尤其需要资深工程师</span>
          <span class="news-value-point">💡 岗位JD甩了篇技术报告</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">3 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/03/blank-instead-manchester-city-name-trophies-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="这些空间既是对贪婪时代的谴责，也是对英超联赛追求正义的致敬在2014年联赛杯决赛中场休息时，桑德兰以1比0领先曼城。Yaya Touré与休闲明亮的30码相媲美" data-title="Let there be blanks instead of Manchester City’s name on trophies: there was no honour there | Jonathan Wilson" data-date="10-04 03:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-04 03:00</span>
          <span class="news-item-title">让奖杯上有空白而不是曼城的名字：那里没有荣誉|乔纳森·威尔逊</span>
          <span class="news-item-title-en">Let there be blanks instead of Manchester City’s name on trophies: there was no honour there | Jonathan Wilson</span>
          <span class="news-value-point">💡 这些空间既是对贪婪时代的谴责，也是对英超联赛追求正义的致敬在2014年联赛杯决赛中场休息时，桑德兰以1比0领先曼城</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/577.htm" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="IT之家 10 月 3 日消息，2026 爱知-名古屋亚运会男足三四名决赛，中国队在常规时间内 2 比 2 战平乌兹别克斯坦队。点球大战中，中国队 4 比 3 取胜，获得本次亚运会男足比赛铜牌。上半场，中国队胡荷韬破门。半场结束，中国男足与对手 1-1 战平。下半场，中国队王钰栋破门。90 分钟双方战成 2-2。这也是中国队时隔 28 年再次获得亚运会男足比赛铜牌！也是亚运会男足项目实行 U23 年龄限制后，中国队首次获得奖牌。IT之家查询获悉，中国男足曾在 1994 年广岛亚运会上获得银牌，并于 1978 年、1998 年两次获得铜牌。本届比赛，中国队时隔 28 年再次闯入亚运会男足四强，并最终登上领奖台。另外，今年 1 月，在 2026 年 U23 亚洲杯半决赛中，中国 U23 男足以" data-title="点球大战制胜！国足击败乌兹别克斯坦队，时隔 28 年再夺亚运会男足比赛铜牌" data-date="10-03 22:51" data-source="IT之家">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-03 22:51</span>
          <span class="news-item-title">点球大战制胜！国足击败乌兹别克斯坦队，时隔 28 年再夺亚运会男足比赛铜牌</span>
          <span class="news-value-point">💡 IT之家 10 月 3 日消息，2026 爱知-名古屋亚运会男足三四名决赛，中国队在常规时间内 2 比 2 战平乌兹别克斯坦队</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/03/manchester-city-whistleblower-rui-pinto-ready-to-help-uk-authorities-in-return-for-protection" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Rui Pinto在葡萄牙面临证人保护的损失有关城市事务的更多文件可能会提供Rui Pinto ，他的泄密有助于引发英超对曼城金融事务的调查，他准备帮助" data-title="Manchester City whistleblower ready to help UK authorities in return for protection" data-date="10-03 19:12" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-03 19:12</span>
          <span class="news-item-title">曼城举报人随时准备为英国当局提供帮助，以换取保护</span>
          <span class="news-item-title-en">Manchester City whistleblower ready to help UK authorities in return for protection</span>
          <span class="news-value-point">💡 Rui Pinto在葡萄牙面临证人保护的损失有关城市事务的更多文件可能会提供Rui Pinto ，他的泄密有助于引发英超对曼城金融事务的调查，他…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707819.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="头顶是新疆艾德莱斯绸铺展出的斑斓色彩，" data-title="星巴克来到新疆，成为“星巴扎”" data-date="10-04 15:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 15:24</span>
          <span class="news-item-title">星巴克来到新疆，成为“星巴扎”</span>
          <span class="news-value-point">💡 头顶是新疆艾德莱斯绸铺展出的斑斓色彩，</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/657.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 4 日消息，10 月 3 日晚间，一乘客被小马智行无人驾驶车门夹住手指的视频流出，引发广泛关注。▲ 网传视频截图对此，小马智行方面回应新浪科技称：“10 月 3 日，一位乘客在上车时，被同行人手动关闭车门不慎夹住手指。事发后我们第一时间协助处置并配合交警调查。交警在查看过我司提供的事件完整视频后，认定属意外事件，非交通事故。”“我们协助乘客及时就医，经检查乘客并无大碍，现已返家休息。我们将持续跟进，并提供必要支持。”小马智行方面表示。IT之家注意到，小马智行核心业务包括自动驾驶出行服务（Robotaxi）、自动驾驶卡车服务（Robotruck）以及智能解决方案三大板块，目前已在中国、美国、欧洲等多个市场推进商业化落地。公司目标 2026 年底前将自动驾驶出租车车队规模扩大" data-title="小马智行回应乘客被夹手事件：已配合交警调查，属意外而非交通事故" data-date="10-04 15:20" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-04 15:20</span>
          <span class="news-item-title">小马智行回应乘客被夹手事件：已配合交警调查，属意外而非交通事故</span>
          <span class="news-value-point">💡 IT之家 10 月 4 日消息，10 月 3 日晚间，一乘客被小马智行无人驾驶车门夹住手指的视频流出，引发广泛关注</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/653.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 4 日消息，特斯拉一项巧妙的全新灯光功能已经开始向用户车辆推送。在海外近期的软件更新（包括 2026.38 版本）当中，特斯拉悄然开启了一项尚未对外正式发布的功能测试：动态大灯水平调节（Dynamic Headlight Leveling）。经追踪发现，该功能目前仅向极少数车辆推送，覆盖美国、阿联酋等多个地区。本次推送并不限定单一车型，Model 3 以及 Cybertruck 上都已经出现这项新功能。特斯拉对该功能的说明文字如下：近光灯将会根据行驶工况以及周边车流自动调整照射角度，尽可能提升驾驶者视野，同时避免对其他道路使用者造成眩光。动态大灯水平调节的工作原理传统车型的大灯照射角度一般需要人工设置。不少欧洲车型的仪表台上或者拨杆处配有滚轮旋钮；当后备箱装载重物之后，驾" data-title="特斯拉悄然测试动态大灯水平调节功能：近光灯可根据车身姿态自动修正照射角度" data-date="10-04 15:07" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-04 15:07</span>
          <span class="news-item-title">特斯拉悄然测试动态大灯水平调节功能：近光灯可根据车身姿态自动修正照射角度</span>
          <span class="news-value-point">💡 IT之家 10 月 4 日消息，特斯拉一项巧妙的全新灯光功能已经开始向用户车辆推送</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707801.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网青岛10月4日电 (王禹)国庆假期，山东省胶州市洋河镇曹家庄里游人往来穿梭。恰逢当地慢生活体验季，这座有着近300年历史的古村落迎来客流高峰，丰收市集的吆喝声、民宿院落的欢笑声交织成一片，晒秋拼豆、非遗手作轮番上演，乡村慢生活体验游悄然兴起。" data-title="山东百年古村落焕新颜 乡村慢生活体验游兴起" data-date="10-04 14:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 14:16</span>
          <span class="news-item-title">山东百年古村落焕新颜 乡村慢生活体验游兴起</span>
          <span class="news-value-point">💡 中新网青岛10月4日电 (王禹)国庆假期，山东省胶州市洋河镇曹家庄里游人往来穿梭</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707793.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="10月4日20时29分，将迎来2026年度的土星冲日。从地球上看，这是土星最亮、视面最大的时刻。傍晚时分，天文爱好者看向东方，肉眼能找到这颗金黄色的亮星。" data-title="今晚抬头 看土星冲日！“指环王”的风采别错过" data-date="10-04 13:51" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 13:51</span>
          <span class="news-item-title">今晚抬头 看土星冲日！“指环王”的风采别错过</span>
          <span class="news-value-point">💡 10月4日20时29分，将迎来2026年度的土星冲日</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707763.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社浙江丽水10月4日电 题：“乡创客”进山大显身手 浙江古村稻海飘香迎新颜" data-title="（走进中国乡村）“乡创客”进山大显身手 浙江古村稻海飘香迎新颜" data-date="10-04 12:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 12:40</span>
          <span class="news-item-title">（走进中国乡村）“乡创客”进山大显身手 浙江古村稻海飘香迎新颜</span>
          <span class="news-value-point">💡 中新社浙江丽水10月4日电 题：“乡创客”进山大显身手 浙江古村稻海飘香迎新颜</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707762.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="视频：【理响中国·理论打卡点】老手艺，火起来！非遗经济正当红来源：人民论坛网" data-title="【理响中国·理论打卡点】老手艺，火起来！非遗经济正当红" data-date="10-04 12:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 12:27</span>
          <span class="news-item-title">【理响中国·理论打卡点】老手艺，火起来！非遗经济正当红</span>
          <span class="news-value-point">💡 视频：【理响中国·理论打卡点】老手艺，火起来</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707760.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="视频：先生︱他花23年，为祖国山河“钉”下“金钉子”来源：央广网" data-title="先生︱他花23年，为祖国山河“钉”下“金钉子”" data-date="10-04 12:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 12:04</span>
          <span class="news-item-title">先生︱他花23年，为祖国山河“钉”下“金钉子”</span>
          <span class="news-value-point">💡 视频：先生︱他花23年，为祖国山河“钉”下“金钉子”来源：央广网</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c6pwg8wkk951o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="周六，由于政府未能使紧急立法在议会获得通过，爆发了 50 多起抗议活动。" data-title="西班牙数万人上街游行：抗议住房危机 扎营占领马德里市中心" data-date="10-04 12:01" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-04 12:01</span>
          <span class="news-item-title">西班牙数万人上街游行：抗议住房危机 扎营占领马德里市中心</span>
          <span class="news-value-point">💡 周六，由于政府未能使紧急立法在议会获得通过，爆发了 50 多起抗议活动</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707740.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="新华社福州10月3日电(记者韦晓睿、郭圻)凉爽的海风拂过木麻黄林，木栈道尽头，视线豁然开朗，大海、沙滩和蓝天尽收眼底。浙江游客雷婉婷举起手机拍下这一幕说：“幽静得很，有种回到大自然的感觉。”" data-title="奔“县”游丨在海岛小城，体验“靠山面海”慢生活" data-date="10-04 11:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 11:17</span>
          <span class="news-item-title">奔“县”游丨在海岛小城，体验“靠山面海”慢生活</span>
          <span class="news-value-point">💡 新华社福州10月3日电(记者韦晓睿、郭圻)凉爽的海风拂过木麻黄林，木栈道尽头，视线豁然开朗，大海、沙滩和蓝天尽收眼底</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707737.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="央视网消息：如果说馆藏典籍是读懂中国的钥匙，那么中央民族大学图书馆的万千文献就藏着中华民族多元一体、交融共生的历史密码，实证着各民族休戚与共、同心报国的千年脉络。" data-title="校馆弦歌·此间读中国 | 万卷藏珍续文脉 青春接力育新人" data-date="10-04 11:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 11:13</span>
          <span class="news-item-title">校馆弦歌·此间读中国 | 万卷藏珍续文脉 青春接力育新人</span>
          <span class="news-value-point">💡 央视网消息：如果说馆藏典籍是读懂中国的钥匙，那么中央民族大学图书馆的万千文献就藏着中华民族多元一体、交融共生的历史密码，实证着各民族休戚与共、同…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707733.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社北京10月4日电 题：演员许文广：冀以更多承载民族记忆、饱含家国情怀的作品联结两岸" data-title="演员许文广：冀以更多承载民族记忆、饱含家国情怀的作品联结两岸" data-date="10-04 11:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 11:10</span>
          <span class="news-item-title">演员许文广：冀以更多承载民族记忆、饱含家国情怀的作品联结两岸</span>
          <span class="news-value-point">💡 中新社北京10月4日电 题：演员许文广：冀以更多承载民族记忆、饱含家国情怀的作品联结两岸</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/ck20w70p4n5wo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="多家媒体报道称，试图劫持飞往以色列的飞机的男子名叫哈马姆·哈马米。" data-title="迪拜航空劫机案：阿联酋官员称副驾驶用应急斧头砍伤机长" data-date="10-04 10:44" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-04 10:44</span>
          <span class="news-item-title">迪拜航空劫机案：阿联酋官员称副驾驶用应急斧头砍伤机长</span>
          <span class="news-value-point">💡 多家媒体报道称，试图劫持飞往以色列的飞机的男子名叫哈马姆·哈马米</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/03/nyregion/cornell-men-university-discipline.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="《纽约时报》获得的摘要详细介绍了被指控对康奈尔大学同学进行性侵犯的男子受到的纪律处分。" data-title="How Cornell Punished Each of the 7 Men Accused of Sexual Assault" data-date="10-04 10:43" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-04 10:43</span>
          <span class="news-item-title">康奈尔大学如何惩罚7名被控性侵犯的男子</span>
          <span class="news-item-title-en">How Cornell Punished Each of the 7 Men Accused of Sexual Assault</span>
          <span class="news-value-point">💡 《纽约时报》获得的摘要详细介绍了被指控对康奈尔大学同学进行性侵犯的男子受到的纪律处分</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707715.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="国庆假期，云南省德宏傣族景颇族自治州梁河县备好了一场民族文化的盛宴：热烈奔放的目瑙纵歌、穿越时光的庭院剧、充满野趣的稻花鱼体验、烟火氤氲的古镇美食、惬意畅快的山野徒步……" data-title="“甜蜜业态”婚旅：让新人把“我愿意”说给山海听" data-date="10-04 09:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 09:57</span>
          <span class="news-item-title">“甜蜜业态”婚旅：让新人把“我愿意”说给山海听</span>
          <span class="news-value-point">💡 国庆假期，云南省德宏傣族景颇族自治州梁河县备好了一场民族文化的盛宴：热烈奔放的目瑙纵歌、穿越时光的庭院剧、充满野趣的稻花鱼体验、烟火氤氲的古镇美…</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-04 15:31（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
