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
      <span>2026-10-29 15:43 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×18 · 天空体育×16</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.bbc.com/zhongwen/articles/cqly0rmlde73o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="自1948 年建国以来，该国一直由联合政府执政，但下一届政府是否会包括现任总理内塔尼亚胡？" data-title="以色列大选结束，内塔尼亚胡能否执政为何依然悬而未决？" data-date="10-29 15:36" data-source="BBC">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
        <span class="hero-featured-date">🕒 10-29 15:36</span>
      </div>
      <h2 class="hero-featured-title">以色列大选结束，内塔尼亚胡能否执政为何依然悬而未决？</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/019/551.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 29 日现场消息，在今天的 XHEART 新芯航途发布会上，X7 Ultra 大模型芯片亮相。XHEART 新芯航途 CEO 李宗霖在发布会上阐述了公司的核心技术路线 ——“大模型定义芯片”。随着智能驾驶从多个小模型走向端到端大模型，芯片的设计方式也需要随之改变。这一变化给芯片提出了三道题：算力能否在真实量产模型中充分发挥？今天设计的芯片能否跟上明天的模型？能否在合理能耗下获得所需能力？过去先做芯片、再让模型适配的方式，越来越难以同时回答这些问题。因此，XHEART 在 2023 年创业之初就决定，从真实应用中的模型需求出发，倒推芯片架构，重新组织计算、存储和数据流转，并为未来模型演进预留空间。先理解大模型，再设计芯片，让模型的进步真正转化为产品的进步，是 XHEART" data-title="新芯航途 X7 Ultra 大模型芯片亮相：700 TOPS 算力，量产模型实测 99.99% 对齐" data-date="10-29 15:32" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">新芯航途 X7 Ultra 大模型芯片亮相：700 TOPS 算力，量产模型实测 99.99% 对齐</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/cx05487d6r9vo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="塔里克·穆哈雷莫维奇（ Tarik Muharemovic ）花费了利兹联（ Leeds United ）一笔“令人垂涎的”费用，给人留下了深刻的印象，以至于有些人担心俱乐部会" data-title="Chiellini guidance to Leeds &#39;rock&#39; - could Muharemovic be signing of season?" data-date="10-29 14:27" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">Chiellini guidance to Leeds 'rock' - could Muharemovic be signing of season?</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/019/556.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 29 日消息，爱国者现已在京东上架冰魄 R240PRO 一体式水冷散热器，该产品提供三年质保，支持漏液包赔与个人送保，其中黑色定价为 329 元，白色定价为 339 元。京东爱国者冰魄 R240PRO 一体式水冷散热器 329 元起直达链接该散热器兼容 Intel LGA1851/1700/1200/115X 架构，以及 AMD AM5/AM4 架构。冷头搭载一块 3.95 英寸 LCD 磁吸式面板，冷头尺寸为 82.39 x80.46 x 74.85 mm。其内部采用铜底与微水道锯齿结构。水泵搭配陶瓷轴承，转速为 2900±10% RPM。该水泵最大流量 1.65 L/min，最大扬程 1.92 M。运行最高噪音 28 dBA，最大消耗功率 3.96W。该散热器冷排尺寸" data-title="爱国者推出冰魄 R240PRO 一体式水冷散热器：冷头配备 3.95 英寸磁吸彩屏，三年质保，329 元起" data-date="10-29 15:42" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">爱国者推出冰魄 R240PRO 一体式水冷散热器：冷头配备 3.95 英寸磁吸彩屏，三年质保，329 元起</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-29/10722732.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月29日电(记者 谢雁冰)中国外交部发言人郭嘉昆29日主持例行记者会。" data-title="日本三丽鸥公司取消和一部日剧的合作 中方回应" data-date="10-29 15:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 15:22</span>
          <span class="news-item-title">日本三丽鸥公司取消和一部日剧的合作 中方回应</span>
          <span class="news-value-point">💡 中新网北京10月29日电(记者 谢雁冰)中国外交部发言人郭嘉昆29日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-29/10722729.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="10月29日，外交部发言人郭嘉昆主持例行记者会。有记者问：日本三丽鸥公司取消了和一部日剧的合作，原因是剧中对华人角色的刻画引发公众反感。请问发言人对此有何回应？" data-title="外交部：日本国内始终存在一股势力 企图通过文化产品丑化抹黑中国" data-date="10-29 15:19" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 15:19</span>
          <span class="news-item-title">外交部：日本国内始终存在一股势力 企图通过文化产品丑化抹黑中国</span>
          <span class="news-value-point">💡 10月29日，外交部发言人郭嘉昆主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-29/10722709.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社唐山10月29日电 题：外籍摄影师镜头里的中国：丰富多彩、有温度、变化大" data-title="外籍摄影师镜头里的中国：丰富多彩、有温度、变化大" data-date="10-29 14:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 14:55</span>
          <span class="news-item-title">外籍摄影师镜头里的中国：丰富多彩、有温度、变化大</span>
          <span class="news-value-point">💡 中新社唐山10月29日电 题：外籍摄影师镜头里的中国：丰富多彩、有温度、变化大</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-29/10722675.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月29日电 据所罗门群岛当地媒体《岛屿太阳报》报道，所罗门群岛总理马修·威尔28日被送往澳大利亚接受紧急医疗救治。" data-title="所罗门群岛总理被送往澳大利亚接受紧急治疗" data-date="10-29 14:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 14:08</span>
          <span class="news-item-title">所罗门群岛总理被送往澳大利亚接受紧急治疗</span>
          <span class="news-value-point">💡 中新网10月29日电 据所罗门群岛当地媒体《岛屿太阳报》报道，所罗门群岛总理马修·威尔28日被送往澳大利亚接受紧急医疗救治</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/28/world/americas/flavio-bolsonaro-us-miami-brazil-trump.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="博尔索纳罗在周日的总统选举中失利，在警方因调查而取消了他的护照后，他逃离巴西，通过阿根廷前往美国。" data-title="Flávio Bolsonaro Lands in Miami After Fleeing Brazil" data-date="10-29 14:01" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-29 14:01</span>
          <span class="news-item-title">Flávio Bolsonaro逃离巴西后登陆迈阿密</span>
          <span class="news-item-title-en">Flávio Bolsonaro Lands in Miami After Fleeing Brazil</span>
          <span class="news-value-point">💡 博尔索纳罗在周日的总统选举中失利，在警方因调查而取消了他的护照后，他逃离巴西，通过阿根廷前往美国</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-29/10722670.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月29日电 综合伊朗媒体29日报道，伊朗伊斯兰革命卫队称，其利用先进的防空系统，在霍尔木兹海峡东部上空拦截并击落了一架美军MQ-1无人机，这是其击落的第14架美军MQ-1无人机。" data-title="伊朗宣布：击落美军MQ" data-date="10-29 13:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 13:56</span>
          <span class="news-item-title">伊朗宣布：击落美军MQ</span>
          <span class="news-value-point">💡 中新网10月29日电 综合伊朗媒体29日报道，伊朗伊斯兰革命卫队称，其利用先进的防空系统，在霍尔木兹海峡东部上空拦截并击落了一架美军MQ-1无人…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/28/us/politics/stevens-el-sayed-senate-democrats-michigan.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="众议员海莉·史蒂文斯（ Haley Stevens ）对阿卜杜勒·赛义德（ Abdul El-Sayed ）博士不那么热情，将晚期的党内紧张局势注入了可能决定参议院控制权的竞选中。" data-title="In Michigan, El-Sayed Faces Heat From Former Primary Rival as Election Nears" data-date="10-29 13:21" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-29 13:21</span>
          <span class="news-item-title">在密歇根州， El-Sayed面临前初选对手的热情，因为选举即将到来</span>
          <span class="news-item-title-en">In Michigan, El-Sayed Faces Heat From Former Primary Rival as Election Nears</span>
          <span class="news-value-point">💡 众议员海莉·史蒂文斯（ Haley Stevens ）对阿卜杜勒·赛义德（ Abdul El-Sayed ）博士不那么热情，将晚期的党内紧张局势…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/28/us/politics/trump-hatch-act.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="随着特朗普官员为面临艰难竞选的共和党候选人辩护，道德专家表示，他们在遵守联邦反腐败法“哈奇法案”方面存在松懈。" data-title="Cabinet Officials on the Campaign Trail? Ethics Experts Say Some Are Breaking the Law." data-date="10-29 12:30" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-29 12:30</span>
          <span class="news-item-title">竞选活动中的内阁官员？道德操守专家说，有些人正在违法。</span>
          <span class="news-item-title-en">Cabinet Officials on the Campaign Trail? Ethics Experts Say Some Are Breaking the Law.</span>
          <span class="news-value-point">💡 随着特朗普官员为面临艰难竞选的共和党候选人辩护，道德专家表示，他们在遵守联邦反腐败法“哈奇法案”方面存在松懈</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-29/10722547.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网圣保罗10月28日电 当地时间28日，巴西联邦警察表示，正在调查总统选举落败候选人、自由党参议员弗拉维奥·博索纳罗违反司法禁令离开巴西的具体情况。弗拉维奥携家人当天抵达美国迈阿密，并发表公开信，质疑总统选举结果，感谢美国总统特朗普和阿根廷总统米莱为其离境提供支持。" data-title="弗拉维奥抵美 巴西警方调查其违反离境禁令一事" data-date="10-29 10:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 10:29</span>
          <span class="news-item-title">弗拉维奥抵美 巴西警方调查其违反离境禁令一事</span>
          <span class="news-value-point">💡 中新网圣保罗10月28日电 当地时间28日，巴西联邦警察表示，正在调查总统选举落败候选人、自由党参议员弗拉维奥·博索纳罗违反司法禁令离开巴西的具…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-29/10722539.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网圣保罗10月28日电 巴西科学技术与创新部28日发布消息称，受厄尔尼诺现象影响，2026年11月至2027年1月，巴西大部分地区可能出现异常高温，平均气温预计比常年同期高出1至2摄氏度，部分地区可能出现持续性热浪。与此同时，巴西南部地区降雨偏多，亚马孙地区北部和东部则可能面临降雨不足。" data-title="厄尔尼诺影响加剧 巴西未来三个月或遭遇持续高温和热浪" data-date="10-29 10:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 10:23</span>
          <span class="news-item-title">厄尔尼诺影响加剧 巴西未来三个月或遭遇持续高温和热浪</span>
          <span class="news-value-point">💡 中新网圣保罗10月28日电 巴西科学技术与创新部28日发布消息称，受厄尔尼诺现象影响，2026年11月至2027年1月，巴西大部分地区可能出现异…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-29/10722536.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网布鲁塞尔10月29日电 (记者 德永健)中国对欧免签政策宣介视频27日起在比利时布鲁塞尔国家机场播放，向过往游客宣传中国对欧免签政策。" data-title="中国对欧免签政策宣介视频在比利时布鲁塞尔机场播放" data-date="10-29 10:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 10:22</span>
          <span class="news-item-title">中国对欧免签政策宣介视频在比利时布鲁塞尔机场播放</span>
          <span class="news-value-point">💡 中新网布鲁塞尔10月29日电 (记者 德永健)中国对欧免签政策宣介视频27日起在比利时布鲁塞尔国家机场播放，向过往游客宣传中国对欧免签政策</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/26/world/americas/brazil-election-lula-win-what-to-know.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="路易斯·伊纳西奥·卢拉·达席尔瓦总统的连任结束了拉丁美洲右翼候选人的一系列胜利。他的对手弗拉维奥·博尔索纳罗（ Flávio Bolsonaro ）逃离巴西前往美国。" data-title="What to Know About Brazil’s Election and Flávio Bolsonaro’s Departure" data-date="10-29 01:31" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-29 01:31</span>
          <span class="news-item-title">巴西大选和弗拉维奥·博尔索纳罗离境须知</span>
          <span class="news-item-title-en">What to Know About Brazil’s Election and Flávio Bolsonaro’s Departure</span>
          <span class="news-value-point">💡 路易斯·伊纳西奥·卢拉·达席尔瓦总统的连任结束了拉丁美洲右翼候选人的一系列胜利</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/019/551.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 29 日现场消息，在今天的 XHEART 新芯航途发布会上，X7 Ultra 大模型芯片亮相。XHEART 新芯航途 CEO 李宗霖在发布会上阐述了公司的核心技术路线 ——“大模型定义芯片”。随着智能驾驶从多个小模型走向端到端大模型，芯片的设计方式也需要随之改变。这一变化给芯片提出了三道题：算力能否在真实量产模型中充分发挥？今天设计的芯片能否跟上明天的模型？能否在合理能耗下获得所需能力？过去先做芯片、再让模型适配的方式，越来越难以同时回答这些问题。因此，XHEART 在 2023 年创业之初就决定，从真实应用中的模型需求出发，倒推芯片架构，重新组织计算、存储和数据流转，并为未来模型演进预留空间。先理解大模型，再设计芯片，让模型的进步真正转化为产品的进步，是 XHEART" data-title="新芯航途 X7 Ultra 大模型芯片亮相：700 TOPS 算力，量产模型实测 99.99% 对齐" data-date="10-29 15:32" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 15:32</span>
          <span class="news-item-title">新芯航途 X7 Ultra 大模型芯片亮相：700 TOPS 算力，量产模型实测 99.99% 对齐</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日现场消息，在今天的 XHEART 新芯航途发布会上，X7 Ultra 大模型芯片亮相</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/019/547.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 29 日消息，英伟达解释了调整 Vera Rubin 平台规格参数的原因，称更新后的规格能更好地反映该系统在量产时的实际性能表现。几天前有报道称，英伟达悄然修改了 Vera Rubin 平台的规格参数。本次改动主要涉及 HBM4 显存带宽以及第六代 NVLink 互联带宽。英伟达公司一名代表向 Wccftech 表示，参数调整是为了更贴合当前量产系统的实际表现，并不会影响最终性能。Vera Rubin 研发阶段公布的参数只是初步架构目标。英伟达官网以及 Vera Rubin 数据手册上的最终规格，代表这套系统在通过认证、进入量产后可以稳定维持的指标。IT之家注意到，今年早些时候的 2026 年 GTC 大会上，英伟达首次推出 Vera Rubin 平台时，宣传每一块 Ru" data-title="英伟达回应 Vera Rubin 平台规格变更：新版为量产规格，第三方跑分均是按量产版测的" data-date="10-29 15:31" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 15:31</span>
          <span class="news-item-title">英伟达回应 Vera Rubin 平台规格变更：新版为量产规格，第三方跑分均是按量产版测的</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，英伟达解释了调整 Vera Rubin 平台规格参数的原因，称更新后的规格能更好地反映该系统在量产时的实际性能…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/019/545.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 29 日消息，英伟达昨日（10 月 28 日）宣布推出开放权重语音转录模型 Nemotron 3.5 Transcribe，并同步公开训练数据管线 Granary v2。Nemotron 3.5 Transcribe 模型整合转录、说话人归属、翻译和音频问答，主要面向会议纪要、课堂录像、访谈整理和多语言客服等场景。在架构方面，Nemotron 3.5 Transcribe 采用混合专家（MoE）架构，总参数约 340 亿，激活参数量约 43 亿。它可处理最长 1 小时的录音，支持 40 种语言的转录，其中 31 种语言可与英语互译；在说话人识别方面，最多可区分 8 名说话人，并支持 13 种语言的说话人标注。该模型最大亮点是应对“多人同时说话”的能力。模型在生成文本时即可" data-title="英伟达开源最强转录 AI 模型 Nemotron 3.5 Transcribe：支持 40 种语言，8 人抢话也能精准转录" data-date="10-29 15:31" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 15:31</span>
          <span class="news-item-title">英伟达开源最强转录 AI 模型 Nemotron 3.5 Transcribe：支持 40 种语言，8 人抢话也能精准转录</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，英伟达昨日（10 月 28 日）宣布推出开放权重语音转录模型 Nemotron 3.5 Transcribe，…</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/506281.html" target="_blank" rel="noopener" data-cat="keji" data-summary="10月29日，文远知行披露旗下子公司景烁科技首次融资进展" data-title="文远知行001号员工带队，景烁科技首轮融资数千万美元" data-date="10-29 11:27" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-29 11:27</span>
          <span class="news-item-title">文远知行001号员工带队，景烁科技首轮融资数千万美元</span>
          <span class="news-value-point">💡 10月29日，文远知行披露旗下子公司景烁科技首次融资进展</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/506273.html" target="_blank" rel="noopener" data-cat="keji" data-summary="2026年10月27日，“工业具身智能焊接与检测技术联合实验室”正式揭牌成立。" data-title="小雨智造与国家钢结构质检中心共建实验室，乔忠良：具身智能新质生产力已成事实" data-date="10-29 10:51" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-29 10:51</span>
          <span class="news-item-title">小雨智造与国家钢结构质检中心共建实验室，乔忠良：具身智能新质生产力已成事实</span>
          <span class="news-value-point">💡 2026年10月27日，“工业具身智能焊接与检测技术联合实验室”正式揭牌成立</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/505934.html" target="_blank" rel="noopener" data-cat="keji" data-summary="用扩散模型怎么做做Agent？" data-title="刚刚，扩散模型杀进Agent主场！350亿参数，速度比Jev快一倍" data-date="10-29 10:18" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-29 10:18</span>
          <span class="news-item-title">刚刚，扩散模型杀进Agent主场！350亿参数，速度比Jev快一倍</span>
          <span class="news-value-point">💡 用扩散模型怎么做做Agent</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/28/us/politics/trump-midterms-white-house-mood.html" target="_blank" rel="noopener" data-cat="keji" data-summary="在中期选举中，白宫一直被人员流动和焦虑所震撼。正如一位助手所说，总统正在收紧他的核心圈子，他猛烈抨击批评者，举行蜿蜒的集会，并以新闻剪辑和“人工智能污点”为食。" data-title="As Trump Faces Down the Midterms, a Grim Mood Takes Over the White House" data-date="10-29 09:01" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-29 09:01</span>
          <span class="news-item-title">随着特朗普面临中期选举，一种严峻的情绪接管了白宫</span>
          <span class="news-item-title-en">As Trump Faces Down the Midterms, a Grim Mood Takes Over the White House</span>
          <span class="news-value-point">💡 在中期选举中，白宫一直被人员流动和焦虑所震撼</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/506246.html" target="_blank" rel="noopener" data-cat="keji" data-summary="理想今年最后一场发布会，自研电池芯片全部上车" data-title="24万开卖！理想重造i6，李想：目标全球畅销" data-date="10-29 08:59" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-29 08:59</span>
          <span class="news-item-title">24万开卖！理想重造i6，李想：目标全球畅销</span>
          <span class="news-value-point">💡 理想今年最后一场发布会，自研电池芯片全部上车</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/506227.html" target="_blank" rel="noopener" data-cat="keji" data-summary="能连肝数日修Bug，免疫提示词注入" data-title="刚刚，Gemini 4 Carbon全面超越Opus 5.5！首发Token半价" data-date="10-29 08:03" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-29 08:03</span>
          <span class="news-item-title">刚刚，Gemini 4 Carbon全面超越Opus 5.5！首发Token半价</span>
          <span class="news-value-point">💡 能连肝数日修Bug，免疫提示词注入</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1021644/adam-mosseri-instagram-ai-negativity" target="_blank" rel="noopener" data-cat="keji" data-summary="当被问及人工智能和大学生在毕业典礼上嘘科技CEO的趋势时， Instagram负责人Adam Mosseri在接受采访时承认，很多人真的不喜欢人工智能，而且不仅仅是年轻人和创意人员。" data-title="Adam Mosseri says negativity around AI is ‘going to get worse’" data-date="10-29 07:05" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-29 07:05</span>
          <span class="news-item-title">亚当·莫塞里（ Adam Mosseri ）表示，围绕人工智能的消极情绪“会变得更糟”</span>
          <span class="news-item-title-en">Adam Mosseri says negativity around AI is ‘going to get worse’</span>
          <span class="news-value-point">💡 当被问及人工智能和大学生在毕业典礼上嘘科技CEO的趋势时， Instagram负责人Adam Mosseri在接受采访时承认，很多人真的不喜欢人…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/28/microsoft-recorded-10-billion-in-revenue-from-openai/" target="_blank" rel="noopener" data-cat="keji" data-summary="微软表示，截至9月30日的季度，它从与OpenAI的商业安排中获得了100亿美元的收入，包括收入分成付款。它强调了合作伙伴关系仍然存在巨大的财务依赖性。" data-title="Microsoft recorded $10 billion in revenue from OpenAI" data-date="10-29 05:34" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-29 05:34</span>
          <span class="news-item-title">微软从OpenAI获得了100亿美元的收入</span>
          <span class="news-item-title-en">Microsoft recorded $10 billion in revenue from OpenAI</span>
          <span class="news-value-point">💡 微软表示，截至9月30日的季度，它从与OpenAI的商业安排中获得了100亿美元的收入，包括收入分成付款</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/28/microsoft-hits-10-quarters-of-record-breaking-revenue-in-a-row/" target="_blank" rel="noopener" data-cat="keji" data-summary="无论人工智能的未来如何，目前的情况对微软来说仍然非常有利。这家科技巨头周三公布的季度收入又创纪录： 923亿美元，比去年同期增长19%。" data-title="Microsoft hits 10 quarters of record-breaking revenue in a row" data-date="10-29 05:25" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-29 05:25</span>
          <span class="news-item-title">微软连续10个季度创下收入纪录</span>
          <span class="news-item-title-en">Microsoft hits 10 quarters of record-breaking revenue in a row</span>
          <span class="news-value-point">💡 无论人工智能的未来如何，目前的情况对微软来说仍然非常有利</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1020811/alphabet-google-earnings-q3-2026" target="_blank" rel="noopener" data-cat="keji" data-summary="谷歌母公司Alphabet表示，正如其今天的2026年第三季度收益所示，其人工智能投资正导致搜索量同比大幅增长。“我们的人工智能投资正在推动整个搜索查询的增长，包括商业查询，” CE" data-title="Google says its investments in AI are driving more searches" data-date="10-29 04:22" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-29 04:22</span>
          <span class="news-item-title">谷歌表示，对人工智能的投资正在推动更多的搜索</span>
          <span class="news-item-title-en">Google says its investments in AI are driving more searches</span>
          <span class="news-value-point">💡 谷歌母公司Alphabet表示，正如其今天的2026年第三季度收益所示，其人工智能投资正导致搜索量同比大幅增长</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/28/anthropic-just-launched-tools-to-show-companies-what-their-ai-spending-is-buying/" target="_blank" rel="noopener" data-cat="keji" data-summary="前沿实验室正在解除用户在计划的首次公开募股之前如何在其模型上花钱的帷幕。" data-title="Anthropic just launched tools to show companies what their AI spending is buying" data-date="10-29 03:19" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-29 03:19</span>
          <span class="news-item-title">Anthropic刚刚推出了工具，向公司展示他们的人工智能支出正在购买什么</span>
          <span class="news-item-title-en">Anthropic just launched tools to show companies what their AI spending is buying</span>
          <span class="news-value-point">💡 前沿实验室正在解除用户在计划的首次公开募股之前如何在其模型上花钱的帷幕</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/019/246.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 29 日消息，苹果今天（10 月 29 日）正式公布配备 512GB 统一内存的 Mac Studio 售价。该配置仅面向搭载 M5 Ultra 芯片（ 36 核 CPU 与 80 核 GPU）的顶配机型，相比较 96GB 版本价格上涨 116,250 元。IT之家注：512GB 内存版目前仅适用于 M5 Ultra 芯片（36 核 CPU 与 80 核 GPU）顶配，用户如果选择 M5 Ultra（30 核 CPU 与 64 核 GPU）会跳出相关提示：在内存配置选项，苹果 Mac Studio 从 96GB 升级到 512GB 需要加价 116,250 元人民币。在存储搭配方面，如果用户选择 M5 Ultra 芯片 + 512GB 内存 +1TB 存储，售价为 172" data-title="苹果上架 512GB 内存版 Mac Studio：较 96GB 配置贵 116250 元" data-date="10-29 01:54" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 01:54</span>
          <span class="news-item-title">苹果上架 512GB 内存版 Mac Studio：较 96GB 配置贵 116250 元</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，苹果今天（10 月 29 日）正式公布配备 512GB 统一内存的 Mac Studio 售价</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
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
        <a class="news-item" href="https://www.skysports.com/football/liverpool-vs-chelsea/report/578612" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="韦斯利·福法纳（ Wesley Fofana ）错过了决定性的现场踢球，因为利物浦在点球上击败了切尔西，在对阵安东尼·伊拉奥拉（ Andoni Iraola ）的前球队伯恩茅斯（ Bournemouth ）的比赛中建立了卡拉宝" data-title="Liverpool beat Chelsea on penalties to reach last eight" data-date="10-29 05:50" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 05:50</span>
          <span class="news-item-title">利物浦在点球上击败切尔西，打入八强</span>
          <span class="news-item-title-en">Liverpool beat Chelsea on penalties to reach last eight</span>
          <span class="news-value-point">💡 韦斯利·福法纳（ Wesley Fofana ）错过了决定性的现场踢球，因为利物浦在点球上击败了切尔西，在对阵安东尼·伊拉奥拉（ Andoni …</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025497/chelsea-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Chelsea latest: &#39;He could be happier&#39; - Alonso explains Estevao snub" data-title="Chelsea latest: &#39;He could be happier&#39; - Alonso explains Estevao snub" data-date="10-29 05:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 05:00</span>
          <span class="news-item-title">切尔西最新消息： “他可以更快乐” -阿隆索解释了Estevao的冷落</span>
          <span class="news-item-title-en">Chelsea latest: 'He could be happier' - Alonso explains Estevao snub</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/liverpool-vs-chelsea/live/578612" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Liverpool vs Chelsea LIVE!" data-title="Liverpool vs Chelsea LIVE!" data-date="10-29 01:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 01:00</span>
          <span class="news-item-title">利物浦vs切尔西直播！</span>
          <span class="news-item-title-en">Liverpool vs Chelsea LIVE!</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/manchester-city-vs-brighton-and-hove-albion/live/578614" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Man City change NINE to host Brighton LIVE!" data-title="Man City change NINE to host Brighton LIVE!" data-date="10-29 01:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 01:00</span>
          <span class="news-item-title">曼城改为九号，现场直播布莱顿！</span>
          <span class="news-item-title-en">Man City change NINE to host Brighton LIVE!</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/chelsea-women-vs-roma-women/live/578251" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="WCL: Beever-Jones misses big chance for Chelsea vs Roma LIVE!" data-title="WCL: Beever-Jones misses big chance for Chelsea vs Roma LIVE!" data-date="10-29 01:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 01:00</span>
          <span class="news-item-title">WCL ： Beever-Jones错过了切尔西对罗马直播的大好机会！</span>
          <span class="news-item-title-en">WCL: Beever-Jones misses big chance for Chelsea vs Roma LIVE!</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/12476234/transfer-centre-live-football-transfer-news-updates-and-rumours" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Transfer Centre LIVE! The stats behind Man Utd&#39;s poor recruitment..." data-title="Transfer Centre LIVE! The stats behind Man Utd&#39;s poor recruitment..." data-date="10-29 00:45" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 00:45</span>
          <span class="news-item-title">转会中心现场直播！曼联糟糕的招募背后的统计数据...</span>
          <span class="news-item-title-en">Transfer Centre LIVE! The stats behind Man Utd's poor recruitment...</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13604920/carabao-cup-quarter-final-draw-liverpool-host-bournemouth-as-bradford-and-fleetwood-learn-premier-league-opposition" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦将在卡拉宝杯四分之一决赛中对阵伯恩茅斯，而第一联盟布拉德福德城将主办曼城。" data-title="Liverpool draw Bournemouth in Carabao Cup quarters" data-date="10-29 00:11" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 00:11</span>
          <span class="news-item-title">伯恩茅斯卡拉宝杯四分之一区利物浦平局</span>
          <span class="news-item-title-en">Liverpool draw Bournemouth in Carabao Cup quarters</span>
          <span class="news-value-point">💡 利物浦将在卡拉宝杯四分之一决赛中对阵伯恩茅斯，而第一联盟布拉德福德城将主办曼城</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025486/arsenal-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Arsenal latest: Details of Arteta&#39;s conversation with Dowman revealed" data-title="Arsenal latest: Details of Arteta&#39;s conversation with Dowman revealed" data-date="10-29 00:09" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 00:09</span>
          <span class="news-item-title">阿森纳最新消息：透露了Arteta与Dowman的对话细节</span>
          <span class="news-item-title-en">Arsenal latest: Details of Arteta's conversation with Dowman revealed</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13604803/max-dowman-red-card-arsenals-appeal-against-decision-will-fail-says-former-premier-league-referee-dermot-gallagher" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="前英超联赛裁判德莫特·加拉格尔（ Dermot Gallagher ）认为，阿森纳对马克斯·道曼（ Max Dowman ）在卡拉宝杯（ Carabao Cup ）击败弗利特伍德镇（ Fleetwood Town ）的冲击" data-title="Ref Watch: Arsenal&#39;s red card appeal will fail - Dowman was aggressive" data-date="10-28 21:15" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-28 21:15</span>
          <span class="news-item-title">参考观看：阿森纳的红牌吸引力将失败-道曼咄咄逼人</span>
          <span class="news-item-title-en">Ref Watch: Arsenal's red card appeal will fail - Dowman was aggressive</span>
          <span class="news-value-point">💡 前英超联赛裁判德莫特·加拉格尔（ Dermot Gallagher ）认为，阿森纳对马克斯·道曼（ Max Dowman ）在卡拉宝杯（ Car…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cje36dn5nx36o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联主教练迈克尔·卡里克（ Michael Carrick ）和队长布鲁诺·费尔南德斯（ Bruno Fernandes ）在俱乐部的训练场举行了畅谈。" data-title="Carrick and Fernandes hold clear" data-date="10-28 19:48" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-28 19:48</span>
          <span class="news-item-title">卡里克和费尔南德斯保持清醒</span>
          <span class="news-item-title-en">Carrick and Fernandes hold clear</span>
          <span class="news-value-point">💡 曼联主教练迈克尔·卡里克（ Michael Carrick ）和队长布鲁诺·费尔南德斯（ Bruno Fernandes ）在俱乐部的训练场举行…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13604738/bruno-fernandes-man-utd-head-coach-michael-carrick-and-club-captain-hold-clear-the-air-talks-ahead-of-chelsea-fixture" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联主教练迈克尔·卡里克（ Michael Carrick ）和队长布鲁诺·费尔南德斯（ Bruno Fernandes ）已经面对面会面，以清除空气，两人都发誓要重新专注于扭转俱乐部的赛季。" data-title="Carrick and Fernandes hold clear-the-air talks ahead of Chelsea fixture" data-date="10-28 18:39" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-28 18:39</span>
          <span class="news-item-title">卡里克和费尔南德斯在切尔西比赛前举行了晴空会谈</span>
          <span class="news-item-title-en">Carrick and Fernandes hold clear-the-air talks ahead of Chelsea fixture</span>
          <span class="news-value-point">💡 曼联主教练迈克尔·卡里克（ Michael Carrick ）和队长布鲁诺·费尔南德斯（ Bruno Fernandes ）已经面对面会面，以清…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/019/556.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 29 日消息，爱国者现已在京东上架冰魄 R240PRO 一体式水冷散热器，该产品提供三年质保，支持漏液包赔与个人送保，其中黑色定价为 329 元，白色定价为 339 元。京东爱国者冰魄 R240PRO 一体式水冷散热器 329 元起直达链接该散热器兼容 Intel LGA1851/1700/1200/115X 架构，以及 AMD AM5/AM4 架构。冷头搭载一块 3.95 英寸 LCD 磁吸式面板，冷头尺寸为 82.39 x80.46 x 74.85 mm。其内部采用铜底与微水道锯齿结构。水泵搭配陶瓷轴承，转速为 2900±10% RPM。该水泵最大流量 1.65 L/min，最大扬程 1.92 M。运行最高噪音 28 dBA，最大消耗功率 3.96W。该散热器冷排尺寸" data-title="爱国者推出冰魄 R240PRO 一体式水冷散热器：冷头配备 3.95 英寸磁吸彩屏，三年质保，329 元起" data-date="10-29 15:42" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 15:42</span>
          <span class="news-item-title">爱国者推出冰魄 R240PRO 一体式水冷散热器：冷头配备 3.95 英寸磁吸彩屏，三年质保，329 元起</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，爱国者现已在京东上架冰魄 R240PRO 一体式水冷散热器，该产品提供三年质保，支持漏液包赔与个人送保，其中黑…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-29/10722746.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="截至2025年底，我国已建成地下管网总长度近390万公里。《城市更新“十五五”规划》提出，要开展城市地下管网体检，建设改造城市地下管网约77万公里。在海南海口，每年5到10月是台风季，地下管网怎么才能扛得住“台风季”？海口交出了什么样的答卷？" data-title="海口管线入住地下“宿舍” 更好守护城市安宁" data-date="10-29 15:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 15:37</span>
          <span class="news-item-title">海口管线入住地下“宿舍” 更好守护城市安宁</span>
          <span class="news-value-point">💡 截至2025年底，我国已建成地下管网总长度近390万公里</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/019/536.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 29 日消息，东风汽车宣布旗下奕派 M8 天元激光版将于 11 月 3 日上市。预计新车将是搭载东风自研天元智驾方案的新版本车型，与现有华为干昆版形成区分，同时售价有望进一步下探。作为参考，目前在售的奕派 M8 全系命名均带“干昆版”后缀，完整搭载华为干昆智能六件套，是东风与华为深度合作的车型。目前，东风奕派 M8 共有 5 款车型在售，售价区间为 17.98-21.98 万元。车辆前脸采用封闭式格栅搭配贯穿式 LED 灯带，前包围两侧搭载分体式远近光模组，车身使用半隐藏式门把手，车内使用 10.25 英寸液晶仪表、50 英寸 HUD 抬头显示以及 16.1 英寸 3K 中控屏。规格方面，新车长宽高为 5020/1975/1733mm，轴距达 3025mm。提供纯电、增程" data-title="东风奕派 M8 天元激光版车型将于 11 月 3 日上市，售价有望进一步下探" data-date="10-29 15:28" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 15:28</span>
          <span class="news-item-title">东风奕派 M8 天元激光版车型将于 11 月 3 日上市，售价有望进一步下探</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，东风汽车宣布旗下奕派 M8 天元激光版将于 11 月 3 日上市</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-29/10722740.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="10月29日下午，三丽鸥公司在其日本官网总部发表声明称，取消与日本电视剧《VIVANT》的所有联名合作，并停止相关后续企划及宣传推广活动。" data-title="三丽鸥日本官网道歉：取消与日剧《VIVANT》所有联名合作" data-date="10-29 15:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 15:27</span>
          <span class="news-item-title">三丽鸥日本官网道歉：取消与日剧《VIVANT》所有联名合作</span>
          <span class="news-value-point">💡 10月29日下午，三丽鸥公司在其日本官网总部发表声明称，取消与日本电视剧《VIVANT》的所有联名合作，并停止相关后续企划及宣传推广活动</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/019/529.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 29 日消息，游戏科学创始人兼 CEO、《黑神话：悟空》制作人冯骥今天在微博发文，为今日发售的国产武侠动作游戏《影之刃零》送上祝福，同时回忆与灵游坊创始人梁其伟的相识过往。冯骥表示，他和梁其伟很多年前就认识，那时大家同为刚创业不久的新人，也都在做手游。他记得第一次见面一起吃了烧烤（或是火锅？），席间煞有其事地讨论各种游戏设计的流行理论，比如怎么把叙事、战斗、付费、体力规划结合得更融洽。不过谈话中他隐约感觉，两人平时都不太玩类似产品。后来殊途同归，冯骥和梁其伟都在某个时间点决定去做自己更喜欢的事情，同时放下了其他选择。单机游戏，并非更高级的游戏。选择做单机的人，大约只是因为在自由的空闲时间里，更多在玩单机。IT之家注意到，冯骥还在文中最后为《影之刃零》送上祝福：“我们唯一真" data-title="《黑神话：悟空》制作人冯骥自曝：很多年前就认识《影之刃零》梁其伟，第一次见面吃了顿烧烤" data-date="10-29 15:19" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-29 15:19</span>
          <span class="news-item-title">《黑神话：悟空》制作人冯骥自曝：很多年前就认识《影之刃零》梁其伟，第一次见面吃了顿烧烤</span>
          <span class="news-value-point">💡 IT之家 10 月 29 日消息，游戏科学创始人兼 CEO、《黑神话：悟空》制作人冯骥今天在微博发文，为今日发售的国产武侠动作游戏《影之刃零》送…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-29/10722715.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中国式现代化，民生为大。地下管网改造，修的不只是管道，也是一座城市的温度。" data-title="居民留得住、住得好 山西平遥古城重塑“地下经络”" data-date="10-29 14:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 14:52</span>
          <span class="news-item-title">居民留得住、住得好 山西平遥古城重塑“地下经络”</span>
          <span class="news-value-point">💡 中国式现代化，民生为大</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-29/10722714.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="截至2025年底，我国已建成地下管网总长度近390万公里。《城市更新“十五五”规划》提出，要开展城市地下管网体检，建设改造城市地下管网约77万公里。湖北荆门每年6到8月是主汛期，面对降雨大风，地下管网该如何应对“大考”？" data-title="应对主汛期“大考” 荆门地下筑起“万方水库”" data-date="10-29 14:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 14:50</span>
          <span class="news-item-title">应对主汛期“大考” 荆门地下筑起“万方水库”</span>
          <span class="news-value-point">💡 截至2025年底，我国已建成地下管网总长度近390万公里</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-29/10722710.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网10月29日电 据中国气象局微博消息，预计10月29-31日，黑龙江西北部、内蒙古东北部、西藏西部和南部的部分地区有大到暴雪，西藏南部局地特大暴雪，上述地区农牧业雪灾风险较高，其中西藏日喀则市亚东县、聂拉木县、吉隆县，阿里地区札达县西部等地农牧业雪灾风险高。建议提前做好温室棚舍加固除雪、防寒保暖工作，同时备足草料，防范饲草短缺。" data-title="农业农村部和中国气象局联合发布农牧业雪灾风险预警" data-date="10-29 14:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 14:47</span>
          <span class="news-item-title">农业农村部和中国气象局联合发布农牧业雪灾风险预警</span>
          <span class="news-value-point">💡 中新网10月29日电 据中国气象局微博消息，预计10月29-31日，黑龙江西北部、内蒙古东北部、西藏西部和南部的部分地区有大到暴雪，西藏南部局地…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-29/10722699.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网三亚10月29日电 题：踏访三亚“天涯古道” 寻味千年黎寨文门" data-title="（乡村行·看振兴）踏访三亚“天涯古道” 寻味千年黎寨文门" data-date="10-29 14:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 14:45</span>
          <span class="news-item-title">（乡村行·看振兴）踏访三亚“天涯古道” 寻味千年黎寨文门</span>
          <span class="news-value-point">💡 中新网三亚10月29日电 题：踏访三亚“天涯古道” 寻味千年黎寨文门</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-29/10722711.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="因地制宜推进综合管廊建设，可以更加有效统筹利用城市地下空间，是“十五五”时期我们建设改造地下管网工作的一部分。但有的历史文化街区地下空间相对有限，城市更新该如何进行呢？" data-title="量身打造迷你款施工设备 微管廊助力老城更新" data-date="10-29 14:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 14:40</span>
          <span class="news-item-title">量身打造迷你款施工设备 微管廊助力老城更新</span>
          <span class="news-value-point">💡 因地制宜推进综合管廊建设，可以更加有效统筹利用城市地下空间，是“十五五”时期我们建设改造地下管网工作的一部分</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/golf/news/12040/13605176/maybank-classic-englands-charley-hull-two-shots-off-lead-after-opening-round-of-lpga-tour-event-in-malaysia" target="_blank" rel="noopener" data-cat="zonghe" data-summary="英格兰选手查理·赫尔（ Charley Hull ）在马来西亚吉隆坡举行的LPGA马来亚银行精英赛（ Maybank Classic ）首轮比赛后领先两杆。" data-title="England&#39;s Hull two off lead after LPGA&#39;s Maybank Classic opening round" data-date="10-29 14:34" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 14:34</span>
          <span class="news-item-title">英格兰的赫尔在LPGA的马来亚银行经典赛首轮比赛后两次领先</span>
          <span class="news-item-title-en">England's Hull two off lead after LPGA's Maybank Classic opening round</span>
          <span class="news-value-point">💡 英格兰选手查理·赫尔（ Charley Hull ）在马来西亚吉隆坡举行的LPGA马来亚银行精英赛（ Maybank Classic ）首轮比赛…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/f1/news/12040/13604769/toto-wolff-explains-kimi-antonelli-turnaround-after-tears-in-belgium-2025-to-likely-world-championship-coronation-at-mexico-city-gp" target="_blank" rel="noopener" data-cat="zonghe" data-summary="梅赛德斯车队负责人托托·沃尔夫（ Toto Wolff ）表示，看到基米·安东内利（ Kimi Antonelli ）去年的转机“非常令人满意” ，因为意大利人希望本周末在墨西哥获得2026年一级方程式世界冠军。" data-title="Wolff explains Antonelli turnaround after &#39;tears&#39;" data-date="10-29 14:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 14:00</span>
          <span class="news-item-title">Wolff在“眼泪”后解释了Antonelli的转变</span>
          <span class="news-item-title-en">Wolff explains Antonelli turnaround after 'tears'</span>
          <span class="news-value-point">💡 梅赛德斯车队负责人托托·沃尔夫（ Toto Wolff ）表示，看到基米·安东内利（ Kimi Antonelli ）去年的转机“非常令人满意”…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/boxing/news/12040/13604844/kayla-allen-from-self-taught-boxer-to-star-prospect-it-started-in-a-unique-way-and-itll-finish-in-a-unique-way" target="_blank" rel="noopener" data-cat="zonghe" data-summary="凯拉·艾伦（ Kayla Allen ）几年前才开始拳击，通过YouTube视频自学，并在她的花园里打拳。" data-title="Kayla Allen: From self-taught boxer to star prospect" data-date="10-29 14:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">10-29 14:00</span>
          <span class="news-item-title">凯拉·艾伦（ Kayla Allen ） ：从自学成才的拳击手到明星</span>
          <span class="news-item-title-en">Kayla Allen: From self-taught boxer to star prospect</span>
          <span class="news-value-point">💡 凯拉·艾伦（ Kayla Allen ）几年前才开始拳击，通过YouTube视频自学，并在她的花园里打拳</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/28/us/politics/california-noncitizen-voters-trump.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="法官裁定没有必要立即采取行动，这给政府带来了另一个挫折，因为它开始针对非公民的投票。" data-title="Judge Rejects Trump Officials’ Bid to Set Aside California Ballots" data-date="10-29 11:14" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-29 11:14</span>
          <span class="news-item-title">法官驳回特朗普官员要求搁置加州选票的申请</span>
          <span class="news-item-title-en">Judge Rejects Trump Officials’ Bid to Set Aside California Ballots</span>
          <span class="news-value-point">💡 法官裁定没有必要立即采取行动，这给政府带来了另一个挫折，因为它开始针对非公民的投票</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-29/10722626.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网10月29日电 据日媒援引日本气象厅消息，日本千叶县东北部29日发生5.4级地震。报道称，东京有一定震感。" data-title="日本千叶县东北部发生5.4级地震，东京有震感" data-date="10-29 10:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-29 10:57</span>
          <span class="news-item-title">日本千叶县东北部发生5.4级地震，东京有震感</span>
          <span class="news-value-point">💡 中新网10月29日电 据日媒援引日本气象厅消息，日本千叶县东北部29日发生5.4级地震</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-29 15:43（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
