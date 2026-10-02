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
      <span>2026-10-02 15:38 抓取更新</span>
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
        <span class="channel-count">51</span>
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
        <span class="channel-count">6</span>
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
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/10-02/10707127.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月2日电 题：从真实出发，以《过海》讲述跨越海峡的归乡之路" data-title="从真实出发，以《过海》讲述跨越海峡的归乡之路" data-date="10-02 14:09" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-02 14:09</span>
      </div>
      <h2 class="hero-featured-title">从真实出发，以《过海》讲述跨越海峡的归乡之路</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/009/306.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 2 日消息，《战争机器：事变日（Gears of War：E-Day）》开发商 The Coalition 现已公布游戏发售宣传片，本作将于北京时间 10 月 7 日正式发售，登陆 XBOX Series X|S 与 PC 平台（包括 Steam 与 Microsoft Store），首发加入 XBOX Game Pass。游戏在 PC 平台首发支持英伟达 DLSS 4.5 技术以及硬件光线追踪功能。价格方面，本作标准版 298 元，预购高级版（428 元）的玩家可提前最多 5 天抢先体验，并可在游戏发售时解锁“Exfil Dom”角色皮肤与“Exfil”武器皮肤套装。IT之家附游戏商品页（https://store.steampowered.com/app/301085" data-title="《战争机器：事变日》游戏发售宣传片公开：首发支持 DLSS 4.5 及光追，10 月 7 日正式发售" data-date="10-02 15:33" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">《战争机器：事变日》游戏发售宣传片公开：首发支持 DLSS 4.5 及光追，10 月 7 日正式发售</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/politics/2026/oct/01/success-manchester-city-helped-put-andy-burnham-in-power" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="PM称赞阿布扎比集团是重塑曼彻斯特的“巨大合作伙伴” ，但批评人士表示，这忽视了城市转型的公共成本。2016年7月，曼城球员YayaTouré漫步在北京工人体育场附近的一个小酒吧里，当数十名中国球迷冲向他时，他露出了困惑的微笑。曼城刚刚在Sheikh Mansour的阿布扎比联合集团和" data-title="曼城的成功如何帮助Andy Burnham掌权" data-date="10-02 02:53" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">曼城的成功如何帮助Andy Burnham掌权</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/009/303.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 2 日消息，交通运输部今日公布的最新数据显示，2026 年 10 月 1 日（国庆假期第 1 日），全社会跨区域人员流动量 32949.5 万人次，环比增长 50.2%，比 2025 年同期（10 月 1 日，中秋国庆假期第 1 日，下同）下降 1.9%。IT之家附 2026 年 10 月 1 日具体数据如下：铁路客运量 2520.4 万人次，环比增长 29.0%，同比增长 9.0%公路人员流动量 30036 万人次，环比增长 52.8%，同比下降 2.8%公路营业性客运量 4471 万人次，环比增长 22.2%，同比增长 8.5%高速公路及普通国省道非营业性小客车人员出行量 25565 万人次，环比增长 59.8%，同比下降 4.5%水路客运量 141.6 万人次，环比" data-title="交通运输部：10 月 1 日全社会跨区域人员流动量 32949.5 万人次，同比下降 1.9%" data-date="10-02 15:28" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">交通运输部：10 月 1 日全社会跨区域人员流动量 32949.5 万人次，同比下降 1.9%</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-02/10707136.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京10月2日电(记者胡璐)记者2日从农业农村部了解到，截至10月1日，全国秋粮收获过三成。" data-title="全国秋粮收获过三成" data-date="10-02 14:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 14:14</span>
          <span class="news-item-title">全国秋粮收获过三成</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-02/10707127.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月2日电 题：从真实出发，以《过海》讲述跨越海峡的归乡之路" data-title="从真实出发，以《过海》讲述跨越海峡的归乡之路" data-date="10-02 14:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 14:09</span>
          <span class="news-item-title">从真实出发，以《过海》讲述跨越海峡的归乡之路</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-02/10707094.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月2日电 (记者 孙自法)记者从中国科学院科技创新发展中心获悉，由中国科学院学部科学普及与教育工作委员会主办、该中心承办的“科学与中国”科普助力乡村振兴行动，国庆节前夕在中国科学院对口支援的江西省赣州市大余县顺利举办。" data-title="“科学与中国”科普助力乡村振兴行动走进江西大余活动顺利举办" data-date="10-02 14:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 14:03</span>
          <span class="news-item-title">“科学与中国”科普助力乡村振兴行动走进江西大余活动顺利举办</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-02/10707119.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月2日电 据中国驻日本大使馆微信公众号10月1日消息，中国驻日本大使馆发言人就村田晃大非法持刀侵闯中国驻日本大使馆案首次开庭答记者问。" data-title="中国驻日使馆：村田晃大侵闯使馆案不容任何抵赖" data-date="10-02 13:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 13:44</span>
          <span class="news-item-title">中国驻日使馆：村田晃大侵闯使馆案不容任何抵赖</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-02/10707066.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社华盛顿10月1日电 中国驻美大使谢锋近日在接受美国《新闻周刊》专访时说，中国国家主席习近平访美最重要的政治成果之一，就是两国元首进一步拓展了中美关系新定位的内涵，同意构建“基于尊重、公平、对等的中美建设性战略稳定关系”。" data-title="中国驻美大使阐述中美关系新定位内涵" data-date="10-02 13:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 13:31</span>
          <span class="news-item-title">中国驻美大使阐述中美关系新定位内涵</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-02/10707065.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社华盛顿10月1日电 中国驻美大使谢锋近日在接受美媒专访时表示，中国国家主席习近平对美国事访问创造了中美交往的历史，具有里程碑意义。这是习近平主席时隔11年再次对美国进行国事访问，是双方对新时期中美关系战略价值的再确认。" data-title="中国驻美大使：习近平主席对美国事访问创造中美交往的历史" data-date="10-02 13:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 13:31</span>
          <span class="news-item-title">中国驻美大使：习近平主席对美国事访问创造中美交往的历史</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-02/10707075.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社河南平顶山10月2日电 题：“台湾哥”在大陆的田园生活" data-title="“台湾哥”在大陆的田园生活" data-date="10-02 13:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 13:30</span>
          <span class="news-item-title">“台湾哥”在大陆的田园生活</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-02/10707079.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社马尼拉10月2日电(记者 周璟)据菲律宾媒体2日报道，菲律宾北部本格特省伊托贡镇一处矿井隧道日前发生疑似有害气体中毒事件，造成7名男子死亡。" data-title="菲律宾一矿井发生疑似有害气体中毒事件  致7人死亡" data-date="10-02 13:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 13:24</span>
          <span class="news-item-title">菲律宾一矿井发生疑似有害气体中毒事件  致7人死亡</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-02/10707073.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月2日电 近日，中国驻外使领馆使团在全球多地举办招待会等活动，隆重庆祝中华人民共和国成立77周年。多国政要出席活动，向中国政府和人民致以诚挚祝贺，高度评价中国发展成就，期待与中国加深互利合作。" data-title="多国政要祝贺新中国成立77周年：盛赞中国发展成就 期待与中国加深互利合作" data-date="10-02 13:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 13:09</span>
          <span class="news-item-title">多国政要祝贺新中国成立77周年：盛赞中国发展成就 期待与中国加深互利合作</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-02/10707069.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月2日电 据美国阿克西奥斯新闻网站10月1日报道，两名美国官员和一名地区消息人士透露，近几周，美军向沙特阿拉伯和卡塔尔增派了两套“爱国者”导弹系统，以保护当地石油和天然气设施。" data-title="美媒：美国向沙特和卡塔尔增派“爱国者”导弹系统，以保护当地能源设施" data-date="10-02 12:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 12:06</span>
          <span class="news-item-title">美媒：美国向沙特和卡塔尔增派“爱国者”导弹系统，以保护当地能源设施</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/02/world/europe/latvia-immigration-russia.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="该计划是俄罗斯在西方播下不和的大战略的一部分，如果比最近指责克里姆林宫的其他行动更微妙的话。" data-title="边境前线：俄罗斯如何利用移民作为对抗欧洲的武器" data-date="10-02 12:01" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-02 12:01</span>
          <span class="news-item-title">边境前线：俄罗斯如何利用移民作为对抗欧洲的武器</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/01/us/politics/trump-puts-on-a-midterms-show-for-an-audience-thats-already-sold.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="President Trump spent the day preaching to his most fervent fans, not the voters he will need to help elect or re-elect a slate of Republicans fighting in states from Alaska to Maine." data-title="Trump Puts on a Midterms Show for an Audience That’s Already Sold" data-date="10-02 11:58" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-02 11:58</span>
          <span class="news-item-title">Trump Puts on a Midterms Show for an Audience That’s Already Sold</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-02/10707061.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月2日电 喀土穆消息：当地时间10月1日，苏丹民间机构“苏丹医生网”发布消息称，苏丹准军事组织快速支援部队(RSF)当日对苏丹北科尔多凡州的一所大学发动无人机袭击，造成5人死亡，47人受伤。" data-title="苏丹一大学遭无人机袭击 致5死47伤" data-date="10-02 11:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 11:33</span>
          <span class="news-item-title">苏丹一大学遭无人机袭击 致5死47伤</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-02/10707027.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月2日电 阿斯马拉消息：当地时间10月1日，厄立特里亚外交部发布声明，宣布与埃塞俄比亚断绝所有外交关系。" data-title="厄立特里亚宣布与埃塞俄比亚断交" data-date="10-02 11:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 11:24</span>
          <span class="news-item-title">厄立特里亚宣布与埃塞俄比亚断交</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-02/10707038.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月2日电 综合《华尔街日报》、美联社等美媒10月1日报道，美国官员透露，五角大楼正向中东派遣第三个航母打击群和更多海军陆战队舰艇，此举将为该地区增加9千至1万名兵力。" data-title="美媒爆料：美国向中东增派第三个航母打击群和至多1万名兵力" data-date="10-02 10:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 10:55</span>
          <span class="news-item-title">美媒爆料：美国向中东增派第三个航母打击群和至多1万名兵力</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/009/306.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 2 日消息，《战争机器：事变日（Gears of War：E-Day）》开发商 The Coalition 现已公布游戏发售宣传片，本作将于北京时间 10 月 7 日正式发售，登陆 XBOX Series X|S 与 PC 平台（包括 Steam 与 Microsoft Store），首发加入 XBOX Game Pass。游戏在 PC 平台首发支持英伟达 DLSS 4.5 技术以及硬件光线追踪功能。价格方面，本作标准版 298 元，预购高级版（428 元）的玩家可提前最多 5 天抢先体验，并可在游戏发售时解锁“Exfil Dom”角色皮肤与“Exfil”武器皮肤套装。IT之家附游戏商品页（https://store.steampowered.com/app/301085" data-title="《战争机器：事变日》游戏发售宣传片公开：首发支持 DLSS 4.5 及光追，10 月 7 日正式发售" data-date="10-02 15:33" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-02 15:33</span>
          <span class="news-item-title">《战争机器：事变日》游戏发售宣传片公开：首发支持 DLSS 4.5 及光追，10 月 7 日正式发售</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/304.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 2 日消息，OpenAI 宣布进一步升级 ChatGPT 的购物功能，新增虚拟试穿和 Favorites（收藏）两项功能，用户现在可以上传自己的照片，让 ChatGPT 生成穿着特定服饰或配饰后的效果图，同时也可以将感兴趣的商品保存下来，方便之后继续查看。IT之家注意到，去年 OpenAI 曾为 ChatGPT 推出专门的 Shopping Research 购物研究功能，主要面向较为复杂的购物需求。其不仅仅局限于“简单提供商品链接”，用户可以通过自然语言告知 ChatGPT 自己预算和需求，之后 ChatGPT 便会在全网搜索相关商品，并根据不同产品的优缺点生成个性化购买指南，同时提供购买链接。而如今，OpenAI 为 ChatGPT 新增的虚拟试穿功能将以“Try o" data-title="OpenAI 升级 ChatGPT 购物体验，新增 AI 衣服虚拟试穿体验" data-date="10-02 15:28" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-02 15:28</span>
          <span class="news-item-title">OpenAI 升级 ChatGPT 购物体验，新增 AI 衣服虚拟试穿体验</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/299.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 2 日消息，AOC 宣布推出一款型号为“U27G4FD”的裸眼 3D 显示器，该机为 4K 180Hz 规格，国行将于近期上市。该产品采用 27 英寸 4K UHD 分辨率 180Hz 刷新率氧化物制程 Fast IPS 面板，提供 0.5ms（MPRT）、1ms GtG 响应时间，搭配 MBR / MBR Sync 低运动模糊技术，拥有英伟达 G-SYNC Compatible、AMD FreeSync Premium 双重认证，同时支持 Adaptive-Sync 智能同步技术。显示器覆盖 100% sRGB、95% DCI-P3，支持色彩 6 轴调整与 HDR10。官方表示，用户只需在电脑端安装官方 Windows 3D 配套软件，即可解锁显示器裸眼 3D 相关功能" data-title="AOC 推出“U27G4FD”27 英寸裸眼 3D 显示器：4K 180Hz、配双 5W 扬声器" data-date="10-02 15:15" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-02 15:15</span>
          <span class="news-item-title">AOC 推出“U27G4FD”27 英寸裸眼 3D 显示器：4K 180Hz、配双 5W 扬声器</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/01/musks-ai-chatbot-grok-reportedly-encouraged-trump-to-capture-venezuelas-president/" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道，特朗普总统在入侵委内瑞拉并抓获尼古拉斯·马杜罗之前征求了格罗克的意见。" data-title="据报道，马斯克的人工智能聊天机器人Grok鼓励特朗普抓捕委内瑞拉总统" data-date="10-02 05:08" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-02 05:08</span>
          <span class="news-item-title">据报道，马斯克的人工智能聊天机器人Grok鼓励特朗普抓捕委内瑞拉总统</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1003756/google-gemini-live-guided-vision" target="_blank" rel="noopener" data-cat="keji" data-summary="Guided Vision今天在兼容的Android设备上推出Gemini Live ，使用人工智能为您对准手机摄像头的任何内容提供实时音频描述。通过在Gemini Live中共享相机，您可以让Google的人工智能帮助您阅读小文本、描述周围环境、查找或识别[…]周围的物体" data-title="谷歌的新引导视觉功能可以帮助您阅读" data-date="10-02 03:47" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-02 03:47</span>
          <span class="news-item-title">谷歌的新引导视觉功能可以帮助您阅读</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/01/chatgpt-can-now-virtually-try-on-clothes-for-you/" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI正在为ChatGPT推出新的购物功能，允许用户使用自己的照片虚拟试穿服装和配饰，并将他们喜欢的产品保存到收藏夹库。" data-title="ChatGPT现在可以虚拟地为您试穿衣服" data-date="10-02 03:21" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-02 03:21</span>
          <span class="news-item-title">ChatGPT现在可以虚拟地为您试穿衣服</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/01/google-thinks-spacexs-starship-has-to-launch-1600-times-before-space-data-centers-get-off-the-ground/" target="_blank" rel="noopener" data-cat="keji" data-summary="谷歌推出了首个进入轨道的先进芯片，为太空数据中心铺平了道路。" data-title="谷歌认为SpaceX的星际飞船必须发射1800次才能让太空数据中心起飞" data-date="10-02 03:18" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-02 03:18</span>
          <span class="news-item-title">谷歌认为SpaceX的星际飞船必须发射1800次才能让太空数据中心起飞</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/games/1003593/steam-deck-2-is-amd-gainsborough-the-chip-valves-been-waiting-for" target="_blank" rel="noopener" data-cat="keji" data-summary="Steam Deck已有四年半的历史，手持游戏玩家热切期待Steam Deck 2 ，但Valve一直表示，在构建续集之前，它需要一款性能和效率“跨越一代”的新芯片。有理由相信芯片现在已经打破了封面： AMD […]" data-title="蒸汽甲板2 ： AMD Gainsborough是Valve一直在等待的芯片吗？" data-date="10-02 02:52" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-02 02:52</span>
          <span class="news-item-title">蒸汽甲板2 ： AMD Gainsborough是Valve一直在等待的芯片吗？</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/01/openai-cuts-ties-with-three-safety-researchers-wsj-reports/" target="_blank" rel="noopener" data-cat="keji" data-summary="报告称， OpenAI已与三名安全研究人员分道扬镳，此前内部调查发现他们对敏感的公司信息处理不当。" data-title="据《华尔街日报》报道， OpenAI与3名安全研究人员断绝了联系" data-date="10-02 02:14" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-02 02:14</span>
          <span class="news-item-title">据《华尔街日报》报道， OpenAI与3名安全研究人员断绝了联系</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/01/opus-5-5-loves-to-tell-you-this-matters-and-other-ai-writing-tells/" target="_blank" rel="noopener" data-cat="keji" data-summary="Opus 5.5最能说明问题的是“可靠”这个词，它出现的频率是人类样本的23倍。" data-title="Opus 5.5喜欢告诉你“这很重要” （以及其他人工智能写作讲述）" data-date="10-02 01:50" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-02 01:50</span>
          <span class="news-item-title">Opus 5.5喜欢告诉你“这很重要” （以及其他人工智能写作讲述）</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1003589/google-ai-overviews-chegg-penske-lawsuits-dismissed" target="_blank" rel="noopener" data-cat="keji" data-summary="正如路透社早些时候报道的那样，一名联邦法官驳回了Chegg和Rolling Stone母公司Penske Media Corporation提起的两起反垄断诉讼，该诉讼指控谷歌利用其人工智能驱动的搜索功能驱散了网络流量。美国地方法院法官阿米特·梅塔（ Amit Mehta ）在周三的裁决中支持谷歌，他写道， PMC […]" data-title="法官驳回谷歌人工智能概览的反垄断诉讼" data-date="10-02 01:12" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-02 01:12</span>
          <span class="news-item-title">法官驳回谷歌人工智能概览的反垄断诉讼</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/games/1003549/sony-ps5-quick-spectral-super-resolution-qssr" target="_blank" rel="noopener" data-cat="keji" data-summary="索尼专门为常规PS5推出了一种新的人工智能升级技术。根据一篇博客文章，这项名为快速光谱超分辨率（ QSSR ）的新技术是一种“人工智能升级的新性能层” ，这是索尼紫水晶项目与AMD合作的结果。索尼表示， PlayStation Spectral Super Resolution (PSSR) […]" data-title="索尼将AI图形升级到常规PS5" data-date="10-02 00:53" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-02 00:53</span>
          <span class="news-item-title">索尼将AI图形升级到常规PS5</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1003365/microsoft-copilot-os-for-work-notepad" target="_blank" rel="noopener" data-cat="keji" data-summary="上周，微软首席执行官萨蒂亚·纳德拉（ Satya Nadella ）为其一些主要企业客户的领导者举办了一场仅限受邀者参加的私密活动。纳德拉没有举办华丽的媒体活动，而是直接向微软真正关心的客户概述了Copilot的未来，并将其最新的人工智能助手重新思考为“工作操作系统”。“微软是[…]" data-title="在微软的Copilot内部重新思考" data-date="10-02 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-02 00:00</span>
          <span class="news-item-title">在微软的Copilot内部重新思考</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/169.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 1 日消息，英伟达于当地时间 30 日推出 GeForce 安全更新驱动程序 582.78，适用于 Maxwell、Pascal 和 Volta 架构显卡，涵盖 GTX 700 系、GTX 900 系、GTX 10 系显卡及 Tesla V100、Titan V 等专业卡。据IT之家了解，英伟达已经不会为上述显卡发布常规 Game Ready 驱动更新，但仍然会不时推出安全更新。该更新支持 Windows 10 和 Windows 11 操作系统，大小为 912.74 MB。同时，该更新修复了显示驱动程序和 vGPU 的 114 个漏洞，其中大多数漏洞直接影响显卡驱动程序，包括 76 个高危漏洞和 37 个中危漏洞。此外，此次驱动更新适用于 GeForce GTX 745" data-title="英伟达为 GTX 700-10 系显卡发布 582.78 安全更新，修复 114 个漏洞" data-date="10-01 23:35" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-01 23:35</span>
          <span class="news-item-title">英伟达为 GTX 700-10 系显卡发布 582.78 安全更新，修复 114 个漏洞</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/desktops/mini-pcs/first-intel-panther-lake-mini-pc-cooled-with-solid-state-airjet-tech-operates-at-less-than-21-dba-aaeon-claims-its-fanless-up-xtreme-ptl-edge-air-is-also-slimmer-lighter-than-actively-cooled-rivals" target="_blank" rel="noopener" data-cat="keji" data-summary="Aaeon的UP Xtreme PTL Edge Air是我们见过的第一款采用AirJet技术的Panther Lake迷你个人电脑，用于超低噪音主动冷却。" data-title="首款采用固态AirJet技术冷却的英特尔Panther Lake迷你个人电脑，工作分贝低于21分贝" data-date="10-01 23:27" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-01 23:27</span>
          <span class="news-item-title">首款采用固态AirJet技术冷却的英特尔Panther Lake迷你个人电脑，工作分贝低于21分贝</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">6 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/politics/2026/oct/01/success-manchester-city-helped-put-andy-burnham-in-power" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="PM称赞阿布扎比集团是重塑曼彻斯特的“巨大合作伙伴” ，但批评人士表示，这忽视了城市转型的公共成本。2016年7月，曼城球员YayaTouré漫步在北京工人体育场附近的一个小酒吧里，当数十名中国球迷冲向他时，他露出了困惑的微笑。曼城刚刚在Sheikh Mansour的阿布扎比联合集团和" data-title="曼城的成功如何帮助Andy Burnham掌权" data-date="10-02 02:53" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-02 02:53</span>
          <span class="news-item-title">曼城的成功如何帮助Andy Burnham掌权</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/01/fears-manchester-city-whistleblower-rui-pinto-loses-protected-witness-status" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="一名男子的私人文件泄露促使对城市的调查被建议不要回家，联系家人或访问拥挤的地方。Rui Pinto在2015年国际足联丑闻引发的十字军东征中建立了Football Leaks网站十多年后，他发现自己正处于日益严重的风暴之中。这位前历史系学生有着标志性的尖刺头发，曾经赚取额外的现金出售有关第二次世界大战的书籍" data-title="犯罪分子还是救世主？ Rui Pinto在曼城泄密后被葡萄牙当局遗弃" data-date="10-02 02:40" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-02 02:40</span>
          <span class="news-item-title">犯罪分子还是救世主？ Rui Pinto在曼城泄密后被葡萄牙当局遗弃</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cjkg7g93y5yno?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="负责监督HMRC的财政委员会已敦促该机构仔细审查曼城判决的税务影响。" data-title="HMRC敦促审查曼城案件的税务影响" data-date="10-02 02:21" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-02 02:21</span>
          <span class="news-item-title">HMRC敦促审查曼城案件的税务影响</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/01/fears-manchester-city-whistleblower-rui-pinto-loses-protected-witness-status" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Pinto的私人文件泄露引发了对曼城的调查，据了解，他担心自己的安全。Rui Pinto在2015年国际足联丑闻引发的十字军东征中建立了Football Leaks网站十多年后，他发现自己正处于日益严重的风暴之中。这位前历史系学生曾经是商标，头发尖刺，曾经赚取额外的现金出售有关第二次世界大战的书籍，他的统计数据并没有阻止他" data-title="城市举报人Rui Pinto失去受保护证人身份后的恐惧" data-date="10-02 02:20" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-02 02:20</span>
          <span class="news-item-title">城市举报人Rui Pinto失去受保护证人身份后的恐惧</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/01/andy-burnhams-manchester-city-comments-stir-fresh-tensions-with-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="据说政府对缺乏警告感到不满财政委员会主席希望HMRC参与城市案件安迪·伯纳姆（ Andy Burnham ）在曼城辩论中的干预重新引发了英超联赛与首相之间的紧张关系。据了解，政府官员感到不满的是，他们没有得到通知，独立委员会对9亿英镑金融操纵和“虚假合同”的诅咒判决将于本周公布，" data-title="安迪·伯纳姆（ Andy Burnham ）的曼城评论引发了英超联赛的新紧张局势" data-date="10-02 02:10" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-02 02:10</span>
          <span class="news-item-title">安迪·伯纳姆（ Andy Burnham ）的曼城评论引发了英超联赛的新紧张局势</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/01/manchester-city-premier-league-financial-rule-breaches-fans-anger-owners" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在阿布扎比政权下取得的成功让支持者感到自豪，但他们只能在新监护人的领导下真正恢复这些感受。在写作和谈到曼城被判犯有严重违反英超联赛规则的数十万字中，罗伯托·曼奇尼（ Roberto Mancini ）在宣布“不关我的事”时可能是最尖锐的。为什么会这样？他从其中一份“虚假合同”中赚了数百万美元，并享受了他的" data-title="曼城球迷感到愤怒是正确的–现在他们需要直接向老板| Will Unwin" data-date="10-01 22:04" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-01 22:04</span>
          <span class="news-item-title">曼城球迷感到愤怒是正确的–现在他们需要直接向老板| Will Unwin</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/009/303.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 2 日消息，交通运输部今日公布的最新数据显示，2026 年 10 月 1 日（国庆假期第 1 日），全社会跨区域人员流动量 32949.5 万人次，环比增长 50.2%，比 2025 年同期（10 月 1 日，中秋国庆假期第 1 日，下同）下降 1.9%。IT之家附 2026 年 10 月 1 日具体数据如下：铁路客运量 2520.4 万人次，环比增长 29.0%，同比增长 9.0%公路人员流动量 30036 万人次，环比增长 52.8%，同比下降 2.8%公路营业性客运量 4471 万人次，环比增长 22.2%，同比增长 8.5%高速公路及普通国省道非营业性小客车人员出行量 25565 万人次，环比增长 59.8%，同比下降 4.5%水路客运量 141.6 万人次，环比" data-title="交通运输部：10 月 1 日全社会跨区域人员流动量 32949.5 万人次，同比下降 1.9%" data-date="10-02 15:28" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-02 15:28</span>
          <span class="news-item-title">交通运输部：10 月 1 日全社会跨区域人员流动量 32949.5 万人次，同比下降 1.9%</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-02/10707167.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网东莞10月2日电 (记者 许青青)由东莞市“百千万工程”指挥部办公室牵头组织的2026东莞沿东江引领区碧道骑行嘉年华于1日举行。随着这条沿东江碧道全线启用，东莞碧道总长度突破1000里，基本实现全域碧道无缝衔接。" data-title="东莞碧道总长度突破1000里 基本实现无缝衔接" data-date="10-02 15:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 15:28</span>
          <span class="news-item-title">东莞碧道总长度突破1000里 基本实现无缝衔接</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-02/10707169.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网10月2日电 据“中国铁路”微信公众号消息，10月1日全国铁路发送旅客2520.4万人次，创单日旅客发送量历史新高，运输安全平稳有序。10月2日，全国铁路预计发送旅客2039万人次，加开列车1462列。" data-title="10月1日全国铁路发送旅客2520.4万人次" data-date="10-02 15:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 15:27</span>
          <span class="news-item-title">10月1日全国铁路发送旅客2520.4万人次</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/302.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 2 日消息，极米记得 AI 显示眼镜 MemoMind One 明日登陆全国 56 家线下门店、INNO100 全球创新旗舰店。10 月 3 日到 10 月 14 日，到店预付 100 元定金预定，即可获赠价值 199 元墨镜夹片 1 副。据官方介绍，它是一副可以长期佩戴的专业 AI 眼镜，也是一副能帮你“记得”的专业 AI 眼镜，AI 能记忆、能导航、能提词。目前，官方暂未公布这款新品的配置信息。官方预热显示，“极米记得 AI 显示眼镜 MemoMind One”是一副可以长期佩戴的专业 AI 眼镜，它集极米显示、蔡司光学、哈曼声学于一体，可以将所有重要信息，第一时间自然呈现在用户眼前，帮助用户从容应对多线程任务，把专注留给更重要的事。" data-title="极米记得 AI 显示眼镜 MemoMind One 明日登陆线下门店，开启定金预定" data-date="10-02 15:26" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-02 15:26</span>
          <span class="news-item-title">极米记得 AI 显示眼镜 MemoMind One 明日登陆线下门店，开启定金预定</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-02/10707171.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="记者从新疆维吾尔自治区交通运输厅了解到，经交通运输、公安、文旅、气象等部门联合研判，预计10月上旬G217线独库公路全线进入冬季。沿线山区路段将出现降雪天气，路面积雪结冰，通行存在较大安全隐患。" data-title="新疆G217线独库公路10月8日20时起实施冬季封闭" data-date="10-02 15:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 15:26</span>
          <span class="news-item-title">新疆G217线独库公路10月8日20时起实施冬季封闭</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-02/10707147.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网台州10月2日电(奚金燕 王莹莹)金秋送爽，一年一度的国庆长假如期而至，万家奔赴团圆、畅游山海，浙江交通集团金温铁道公司临海南站也迎来客流高峰。熙熙攘攘的候车大厅、往来不息的行人、穿梭驰骋的列车，勾勒出假期最热闹的图景。" data-title="浙江铁道一线国庆守归途：愿每一场团圆都不负期许" data-date="10-02 15:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 15:23</span>
          <span class="news-item-title">浙江铁道一线国庆守归途：愿每一场团圆都不负期许</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/300.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 2 日消息，沃尔沃汽车今日公布数据显示，2026 年第三季度，其全球销量为 141,609 辆，同比下降 10.7%。沃尔沃汽车首席商务官埃里克 · 塞维林森（Erik Severinson）表示，中国市场的低迷态势未见任何缓解，而美国豪华车细分市场的复苏步伐也慢于此前预期。这直接冲击了我们第三季度的销量表现。面对同样严峻的市场环境，第三方分析机构也已纷纷下调 2026 年豪华车市场的整体销量预期。本季度，沃尔沃纯电动车型销量同比增长 29%，在总销量中占比达 32%。若包含纯电动与插电式混合动力在内的电气化车型，占当季总销量的 53%。IT之家附各区域市场表现如下：欧洲及世界其他地区：零售交付表现平稳，销量达 90,548 辆，同比增长 2%。其中纯电动汽车销量大涨 5" data-title="沃尔沃汽车 2026 年第三季度全球销量同比下降 10.7%，大中华区暴降 40.6%" data-date="10-02 15:18" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-02 15:18</span>
          <span class="news-item-title">沃尔沃汽车 2026 年第三季度全球销量同比下降 10.7%，大中华区暴降 40.6%</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-02/10707152.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网银川10月2日电 (记者 李佩珊)国庆假期，不少游客的休闲选择更加多元，不再将奔波打卡景点当作出游的首选。10月2日，在宁夏银川阅彩城举办的“举杯贺兰山”2026银川文旅拼豆嘉年华，将这股流行的手作热潮引入城市文旅消费场景，也呈现出当下国内旅游市场的新动向，越来越多年轻群体更加看重旅行过程中的亲身参与感与情绪体验。" data-title="宁夏银川：拼豆手作带来假日新体验 在地文化邂逅青年潮流" data-date="10-02 15:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 15:16</span>
          <span class="news-item-title">宁夏银川：拼豆手作带来假日新体验 在地文化邂逅青年潮流</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c6x2z2dqv080o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这名被定罪的杀人犯在两次致命注射后仍然生还，目前正在田纳西州的医院接受治疗。这是当地半年内第二宗死刑执行失败事件，引发许多疑问。" data-title="美国女囚死刑执行失败：注射两剂药物仍存活，接下来将如何发展？" data-date="10-02 15:14" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-02 15:14</span>
          <span class="news-item-title">美国女囚死刑执行失败：注射两剂药物仍存活，接下来将如何发展？</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-02/10707158.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网杭州10月2日电(记者 王逸飞)当下，“沉浸式、情绪化”“愿意为自然深度体验买单”等成为中国年轻人出游的鲜明特征。今年国庆假期，在浙江，多座江南古镇纷纷推出新玩法，以重体验、重潮流的全新形象吸引年轻游客“打卡”。" data-title="江南古镇假日“上新”拥抱年轻人" data-date="10-02 15:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 15:14</span>
          <span class="news-item-title">江南古镇假日“上新”拥抱年轻人</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-02/10707155.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网湖州10月2日电(黄彦君 姚国琴)陆羽古道的茶园石阶上，背包客三五成群；义皋古村内实景游戏上演，游客沉浸式“入戏”；夜幕低垂，铁花飞溅点亮古村夜空……国庆假期期间，浙江省湖州市吴兴区深挖山野与古村资源，以多元创意“唤醒”乡村文旅活力。" data-title="（乡村行·看振兴）从观光到沉浸 浙江吴兴乡村玩法焕新引客来" data-date="10-02 15:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 15:09</span>
          <span class="news-item-title">（乡村行·看振兴）从观光到沉浸 浙江吴兴乡村玩法焕新引客来</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-02/10707154.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网杭州10月2日电 (钱晨菲)国庆期间，杭州西湖水域迎来一位特殊的“巡逻员”，由杭州市公安局西湖景区分局联合中国科学院自动化研究所研发的仿生机器鱼“西湖青鱼”正式下水，投入西湖水域的生态警务实战。" data-title="杭州西湖仿生青鱼下水 守护国庆水域平安" data-date="10-02 15:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 15:07</span>
          <span class="news-item-title">杭州西湖仿生青鱼下水 守护国庆水域平安</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-02/10707077.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社贵州遵义10月2日电 (记者 杨茜)“比个耶(两根手指成V字形)！”在遵义会议纪念馆的老槐树下，这是络绎不绝的游客留影时最常用的一种手势。" data-title="（长征胜利90周年）遵义会议纪念馆：一棵“活文物”承载历史" data-date="10-02 13:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-02 13:40</span>
          <span class="news-item-title">（长征胜利90周年）遵义会议纪念馆：一棵“活文物”承载历史</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cx9808vgjy09o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="全球局势动荡之际，西班牙与中国意外走近，但这并非唯一不寻常的伙伴关系。" data-title="西班牙与中国愈走愈近，欧盟多方为何不满？" data-date="10-02 13:09" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-02 13:09</span>
          <span class="news-item-title">西班牙与中国愈走愈近，欧盟多方为何不满？</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/02/world/europe/russia-ukraine-winter.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="乌克兰向欧洲合作伙伴展示了它所说的俄罗斯今年冬天切断主要城市供电、供暖和供水的计划。" data-title="俄罗斯正计划以迄今为止最强大的打击来试图冻结乌克兰" data-date="10-02 12:00" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-02 12:00</span>
          <span class="news-item-title">俄罗斯正计划以迄今为止最强大的打击来试图冻结乌克兰</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-02 15:38（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
