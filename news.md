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
      <span>2026-10-15 01:23 抓取更新</span>
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
        <span class="channel-count">50</span>
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
        <span class="channel-count">5</span>
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
  <div class="ov-item"><span class="ov-num">50</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×16 · The Verge×8</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.nytimes.com/2026/10/14/world/europe/ukraine-starlink-energy.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="一次大规模的袭击使基辅60万人的电力中断，五角大楼资助的卫星互联网计划似乎在没有任何警告的情况下受到遏制。" data-title="Ukraine’s Vulnerability Grows as Starlink Is Restricted and Russia Escalates" data-date="10-15 01:11" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 10-15 01:11</span>
      </div>
      <h2 class="hero-featured-title">随着Starlink受限和俄罗斯升级，乌克兰的脆弱性加剧</h2>
      <div class="hero-featured-title-en">Ukraine’s Vulnerability Grows as Starlink Is Restricted and Russia Escalates</div>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.nytimes.com/2026/10/14/world/europe/ukraine-intelligence-sharing-zelensky-uk.html" target="_blank" rel="noopener" data-cat="keji" data-summary="乌克兰总统弗拉基米尔·泽伦斯基（ Volodymyr Zelensky ）表示，乌克兰“没有从我们的伙伴那里得到关于俄罗斯袭击的早期特朗普总统曾表示，华盛顿仍在“分享情报”。" data-title="Zelensky Visits U.K. as Ukraine Presses Allies on Intelligence Sharing" data-date="10-15 01:13" data-source="纽约时报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
      </div>
      <p class="hero-sub-title">Zelensky Visits U.K. as Ukraine Presses Allies on Intelligence Sharing</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/cvp8g57ne53xo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利桑德罗·马丁内斯（ Lisandro Martinez ）在曼联冠军联赛被马德里竞技（ Atletico Madrid ）击败后发表的爆炸性评论让足球总监杰森·威尔科克斯（ Jason Wilcox ）" data-title="Wilcox the target again in another damaging Man Utd fallout" data-date="10-14 23:30" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">Wilcox the target again in another damaging Man Utd fallout</p>
    </a>
    <a class="hero-sub-card" href="https://www.nytimes.com/2026/10/14/business/starshield-spacex-ukraine-starlink-satellites-musk.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="多年来，乌克兰武装部队一直依赖埃隆·马斯克（ Elon Musk ）的SpaceX开发的卫星通信服务。最近的限制阻碍了其战争努力。" data-title="What Is Starshield, SpaceX’s Military-Grade Satellite Internet Service Ukraine Relies On?" data-date="10-15 01:06" data-source="纽约时报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
      </div>
      <p class="hero-sub-title">What Is Starshield, SpaceX’s Military-Grade Satellite Internet Service Ukraine Relies On?</p>
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
        <a class="news-item" href="https://www.nytimes.com/2026/10/14/world/europe/ukraine-starlink-energy.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="一次大规模的袭击使基辅60万人的电力中断，五角大楼资助的卫星互联网计划似乎在没有任何警告的情况下受到遏制。" data-title="Ukraine’s Vulnerability Grows as Starlink Is Restricted and Russia Escalates" data-date="10-15 01:11" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-15 01:11</span>
          <span class="news-item-title">随着Starlink受限和俄罗斯升级，乌克兰的脆弱性加剧</span>
          <span class="news-item-title-en">Ukraine’s Vulnerability Grows as Starlink Is Restricted and Russia Escalates</span>
          <span class="news-value-point">💡 一次大规模的袭击使基辅60万人的电力中断，五角大楼资助的卫星互联网计划似乎在没有任何警告的情况下受到遏制</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-14/10714746.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间14日，以色列国防军发表声明称，以色列国防军总参谋长扎米尔在中央司令部举行局势评估和行动简报会时表示，鉴于各战线面临的袭击预警数量增加，地区局势升级风险上升，以军已向约旦河西岸增派兵力，以加强该地区的战略安全与稳定。" data-title="以军称已向约旦河西岸增兵 处于高级别战备状态" data-date="10-14 23:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 23:56</span>
          <span class="news-item-title">以军称已向约旦河西岸增兵 处于高级别战备状态</span>
          <span class="news-value-point">💡 当地时间14日，以色列国防军发表声明称，以色列国防军总参谋长扎米尔在中央司令部举行局势评估和行动简报会时表示，鉴于各战线面临的袭击预警数量增加，…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-14/10714745.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社新加坡10月14日电(记者舒畅 毛鹏飞)新加坡海事及港务管理局14日晚发表声明说，两艘在新加坡注册的集装箱船据报在通过霍尔木兹海峡时被不明投射物击中，其中一艘着火后沉没。" data-title="两艘新加坡籍船只在霍尔木兹海峡遭袭" data-date="10-14 23:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 23:54</span>
          <span class="news-item-title">两艘新加坡籍船只在霍尔木兹海峡遭袭</span>
          <span class="news-value-point">💡 新华社新加坡10月14日电(记者舒畅 毛鹏飞)新加坡海事及港务管理局14日晚发表声明说，两艘在新加坡注册的集装箱船据报在通过霍尔木兹海峡时被不明…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-14/10714737.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月14日电 (记者 余湛奕)甘肃省白银市会宁县是红军长征三大主力会师的红色圣地。10月14日，“重走长征路 书香悟初心”全国职工红色主题阅读活动走进甘肃会宁，引导广大职工在红色阅读中传承红色基因，汲取奋进力量。" data-title="全国职工红色主题阅读活动走进甘肃会宁" data-date="10-14 23:25" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 23:25</span>
          <span class="news-item-title">全国职工红色主题阅读活动走进甘肃会宁</span>
          <span class="news-value-point">💡 中新网北京10月14日电 (记者 余湛奕)甘肃省白银市会宁县是红军长征三大主力会师的红色圣地</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-14/10714734.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月14日电 (魏之强)“我们正在倒计时，等待美国军舰靠近霍尔木兹海峡入口的那一天。”" data-title="倒计时击沉美舰：伊朗在海峡摆下非对称口袋，沙特阿美总部14日再度起火" data-date="10-14 23:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 23:03</span>
          <span class="news-item-title">倒计时击沉美舰：伊朗在海峡摆下非对称口袋，沙特阿美总部14日再度起火</span>
          <span class="news-value-point">💡 中新网北京10月14日电 (魏之强)“我们正在倒计时，等待美国军舰靠近霍尔木兹海峡入口的那一天</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-14/10714689.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社浙江衢州10月14日电 (张斌 吴怡婧 童彤)“期待不仅是我们访问这片土地，未来也会有更多美国人来到这里，了解这段历史。”美国杜立特突袭者子女协会代表托马斯·马西亚(Thomas Evan Macia)14日在浙江衢州受访时说。" data-title="美国杜立特突袭者子女协会代表在华寻历史“拼图”" data-date="10-14 22:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 22:04</span>
          <span class="news-item-title">美国杜立特突袭者子女协会代表在华寻历史“拼图”</span>
          <span class="news-value-point">💡 中新社浙江衢州10月14日电 (张斌 吴怡婧 童彤)“期待不仅是我们访问这片土地，未来也会有更多美国人来到这里，了解这段历史</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-14/10714666.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社东京10月14日电 (记者 朱晨曦)据日本广播协会报道，日本农林水产大臣梁和生14日向首相高市早苗提交辞呈。他此前因自身失言等丑闻引发巨大争议。" data-title="日本农林水产大臣梁和生因失言等丑闻辞职" data-date="10-14 22:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 22:04</span>
          <span class="news-item-title">日本农林水产大臣梁和生因失言等丑闻辞职</span>
          <span class="news-value-point">💡 中新社东京10月14日电 (记者 朱晨曦)据日本广播协会报道，日本农林水产大臣梁和生14日向首相高市早苗提交辞呈</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-14/10714647.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月14日电 德黑兰消息：伊朗伊斯兰革命卫队海军当地时间14日发表声明说，一艘集装箱船当日试图穿过霍尔木兹海峡一条“未经授权且危险”的航线时触碰水雷，该船随后发生爆炸并起火沉没。" data-title="伊朗称一艘集装箱船在霍尔木兹海峡触雷沉没" data-date="10-14 22:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 22:02</span>
          <span class="news-item-title">伊朗称一艘集装箱船在霍尔木兹海峡触雷沉没</span>
          <span class="news-value-point">💡 中新社北京10月14日电 德黑兰消息：伊朗伊斯兰革命卫队海军当地时间14日发表声明说，一艘集装箱船当日试图穿过霍尔木兹海峡一条“未经授权且危险”…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-14/10714723.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社广州10月14日电" data-title="李强在第140届中国进出口商品交易会开幕式上的主旨演讲（全文）" data-date="10-14 21:58" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 21:58</span>
          <span class="news-item-title">李强在第140届中国进出口商品交易会开幕式上的主旨演讲（全文）</span>
          <span class="news-value-point">💡 新华社广州10月14日电</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-14/10714688.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月14日电 全国人大常委会委员长赵乐际14日在北京集体会见出席2026年国际议员友好交流论坛的各国代表。" data-title="赵乐际集体会见出席2026年国际议员友好交流论坛的各国代表" data-date="10-14 21:58" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 21:58</span>
          <span class="news-item-title">赵乐际集体会见出席2026年国际议员友好交流论坛的各国代表</span>
          <span class="news-value-point">💡 中新社北京10月14日电 全国人大常委会委员长赵乐际14日在北京集体会见出席2026年国际议员友好交流论坛的各国代表</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-14/10714722.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月14日电(记者 李京泽)中国社会科学院第二届青年学术大会13日在北京召开。中国社会科学院院长、党组书记高翔出席会议并作学术报告。中央纪委国家监委驻院纪检监察组组长、院党组成员杭元祥，副院长、党组成员李雪松，院党组成员、当代中国研究所所长金民卿，秘书长、党组成员薛松岩出席会议。" data-title="中国社会科学院第二届青年学术大会在北京召开" data-date="10-14 21:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 21:54</span>
          <span class="news-item-title">中国社会科学院第二届青年学术大会在北京召开</span>
          <span class="news-value-point">💡 中新网北京10月14日电(记者 李京泽)中国社会科学院第二届青年学术大会13日在北京召开</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-14/10714721.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网甘肃甘南10月14日电 (记者 冯志军)在甘肃甘南藏族自治州迭部县腊子口镇的腊子口战役遗址，至今仍保留着91年前红军长征北上时原始的峡谷峭壁、战役旧址地貌，“一夫当关，万夫莫开”的峡谷地形，直观还原了当年战斗的险峻环境。时至今日，“读万卷书，不如走一遍天险”也成为众多实地探访者的共鸣。" data-title="（长征胜利90周年）“天险”腊子口的“红绿交辉”" data-date="10-14 21:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 21:54</span>
          <span class="news-item-title">（长征胜利90周年）“天险”腊子口的“红绿交辉”</span>
          <span class="news-value-point">💡 中新网甘肃甘南10月14日电 (记者 冯志军)在甘肃甘南藏族自治州迭部县腊子口镇的腊子口战役遗址，至今仍保留着91年前红军长征北上时原始的峡谷峭…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-14/10714717.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网张家界10月14日电 (张雪盈)“睡到那半夜过，门口嘛在过兵……门口嘛挂盏灯，照在个大路上，同志们好行军。”秋日午后，湖南桑植县刘家坪白族乡干田坝誓师广场上，这首传唱数十年的《门口挂盏灯》桑植民歌再度响起。" data-title="（长征胜利90周年）湖南桑植“火把”新传：从长征夜路到振兴征途" data-date="10-14 21:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 21:54</span>
          <span class="news-item-title">（长征胜利90周年）湖南桑植“火把”新传：从长征夜路到振兴征途</span>
          <span class="news-value-point">💡 中新网张家界10月14日电 (张雪盈)“睡到那半夜过，门口嘛在过兵……门口嘛挂盏灯，照在个大路上，同志们好行军</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-14/10714709.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月14日电 (记者 马帅莎)据中国民营火箭公司蓝箭航天消息，北京时间10月14日19时40分，朱雀二号改进型遥四运载火箭在东风商业航天创新试验区发射升空，将搭载的国星宇航星时代-39、44~50星，光传-03、04星共10颗卫星顺利送入预定轨道，飞行试验任务取得圆满成功。" data-title="一箭十星 朱雀二号改进型遥四运载火箭发射成功" data-date="10-14 21:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 21:40</span>
          <span class="news-item-title">一箭十星 朱雀二号改进型遥四运载火箭发射成功</span>
          <span class="news-value-point">💡 中新社北京10月14日电 (记者 马帅莎)据中国民营火箭公司蓝箭航天消息，北京时间10月14日19时40分，朱雀二号改进型遥四运载火箭在东风商业…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/14/us/politics/susan-collins-trump-maine-senate.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="缅因州的竞选可能会决定参议院的控制权，这场竞选正在考验柯林斯在急剧两极分化的总统任期内是否仍然有温和的空间。" data-title="A Trump Backlash Endangers Susan Collins in the Maine Senate Race" data-date="10-14 20:26" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-14 20:26</span>
          <span class="news-item-title">在缅因州参议院竞选中，特朗普的强烈反对危及苏珊·柯林斯</span>
          <span class="news-item-title-en">A Trump Backlash Endangers Susan Collins in the Maine Senate Race</span>
          <span class="news-value-point">💡 缅因州的竞选可能会决定参议院的控制权，这场竞选正在考验柯林斯在急剧两极分化的总统任期内是否仍然有温和的空间</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/10/14/world/europe/ukraine-intelligence-sharing-zelensky-uk.html" target="_blank" rel="noopener" data-cat="keji" data-summary="乌克兰总统弗拉基米尔·泽伦斯基（ Volodymyr Zelensky ）表示，乌克兰“没有从我们的伙伴那里得到关于俄罗斯袭击的早期特朗普总统曾表示，华盛顿仍在“分享情报”。" data-title="Zelensky Visits U.K. as Ukraine Presses Allies on Intelligence Sharing" data-date="10-15 01:13" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-15 01:13</span>
          <span class="news-item-title">泽伦斯基访问英国，乌克兰就情报共享向盟国施压</span>
          <span class="news-item-title-en">Zelensky Visits U.K. as Ukraine Presses Allies on Intelligence Sharing</span>
          <span class="news-value-point">💡 乌克兰总统弗拉基米尔·泽伦斯基（ Volodymyr Zelensky ）表示，乌克兰“没有从我们的伙伴那里得到关于俄罗斯袭击的早期特朗普总统曾…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1011276/openai-employee-unreleased-product-plans" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI声称，一名前员工在加入苹果之前，拿走了100多份与其产品计划相关的文件。在周三提交的一份文件中， OpenAI指控这名未透露姓名的员工将此信息发送到个人账户，然后将其呈现" data-title="OpenAI claims an ex-employee took its product plans and presented them to Apple" data-date="10-15 00:43" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-15 00:43</span>
          <span class="news-item-title">OpenAI声称，一名前员工拿走了其产品计划并将其提交给苹果</span>
          <span class="news-item-title-en">OpenAI claims an ex-employee took its product plans and presented them to Apple</span>
          <span class="news-value-point">💡 OpenAI声称，一名前员工在加入苹果之前，拿走了100多份与其产品计划相关的文件</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/networking/routers/gfiber-and-qualcomm-announce-wi-fi-8-gateway-20-gig-customers-to-be-first-to-receive-next-gen-wireless-upgrade" target="_blank" rel="noopener" data-cat="keji" data-summary="Wi-Fi 8尚未获得IEEE认证，但硬件公告仍在不断增加" data-title="GFiber and Qualcomm announce Wi" data-date="10-15 00:28" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-15 00:28</span>
          <span class="news-item-title">GFiber和高通宣布Wi</span>
          <span class="news-item-title-en">GFiber and Qualcomm announce Wi</span>
          <span class="news-value-point">💡 Wi-Fi 8尚未获得IEEE认证，但硬件公告仍在不断增加</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/science/1011127/ai-weather-forecast-microsoft" target="_blank" rel="noopener" data-cat="keji" data-summary="基于老派物理的天气预报，甚至新的人工智能模型通常在两周后变得不那么可靠，微软声称已经使用机器学习解决了这个问题。该公司的研究人员表示，他们发现了一种新的、具有成本效益的" data-title="Microsoft has a new machine learning tool to improve weather forecasts" data-date="10-15 00:05" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-15 00:05</span>
          <span class="news-item-title">微软推出全新机器学习工具，改善天气预报</span>
          <span class="news-item-title-en">Microsoft has a new machine learning tool to improve weather forecasts</span>
          <span class="news-value-point">💡 基于老派物理的天气预报，甚至新的人工智能模型通常在两周后变得不那么可靠，微软声称已经使用机器学习解决了这个问题</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1009086/square-kiosk" target="_blank" rel="noopener" data-cat="keji" data-summary="Square正在推出新硬件：一个大型信息亭，用于订购带有触摸屏的东西，并让您与人工智能交谈。它被称为Square Kiosk。Square说， Kiosk有一个大的药丸形状，有一个“代理的对话语音层” ，" data-title="Square’s new kiosk lets you talk to AI for help with your order" data-date="10-15 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-15 00:00</span>
          <span class="news-item-title">Square的新信息亭可让您与人工智能联系，以获取订单帮助</span>
          <span class="news-item-title-en">Square’s new kiosk lets you talk to AI for help with your order</span>
          <span class="news-value-point">💡 Square正在推出新硬件：一个大型信息亭，用于订购带有触摸屏的东西，并让您与人工智能交谈</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-14/10714735.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网临汾10月14日电 (任丽娜)10月14日，2026临汾市“人工智能+”产业生态暨招商引资交流会举行。这场以“智汇临汾·数创未来”为主题的大会，正悄然改写着这座传统资源型城市的产业底色。" data-title="从“煤焦重镇”到“智算高地”：解读山西临汾产业跃迁密码" data-date="10-14 23:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 23:21</span>
          <span class="news-item-title">从“煤焦重镇”到“智算高地”：解读山西临汾产业跃迁密码</span>
          <span class="news-value-point">💡 中新网临汾10月14日电 (任丽娜)10月14日，2026临汾市“人工智能+”产业生态暨招商引资交流会举行</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1011108/anthropic-self-replicating-ai-smart-devices-risk" target="_blank" rel="noopener" data-cat="keji" data-summary="大量的智能设备--冰箱、烤箱、吸尘器、割草机、监控摄像头和电视--正在密谋接管互联网吗？不会。但他们可能很快就会不知不觉地让主机自我复制AI模型，从一个设备传播到另一个设备，" data-title="Anthropic’s self-replicating AI warning is alarming deja vu" data-date="10-14 23:19" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-14 23:19</span>
          <span class="news-item-title">Anthropic的自我复制AI警告令人担忧似曾相识</span>
          <span class="news-item-title-en">Anthropic’s self-replicating AI warning is alarming deja vu</span>
          <span class="news-value-point">💡 大量的智能设备--冰箱、烤箱、吸尘器、割草机、监控摄像头和电视--正在密谋接管互联网吗</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/013/130.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 14 日消息，英特尔今日宣布推出 Intel Inference Microservices 服务，这是一套面向大语言模型推理的容器化微服务方案，目标是让企业在已有的至强处理器上直接获得经过调优的模型推理能力，无需再花费数天时间进行手动硬件优化。在该模式下，每个微服务都是一个独立容器，通过 OpenAI 兼容 API 对外提供单个模型的服务，并在启动时自动检测所在的英特尔处理器型号，应用英特尔针对该模型和该硬件预先验证过的配置参数。英特尔指出，让大语言模型给出回复并不困难，难的是在既有硬件上稳定、高质量地重复这一过程。精度设置、计算任务在核心之间的分配方式、内存跨 NUMA 节点的布局，以及推理引擎使用哪些指令集，都取决于模型本身和底层处理器。更换模型，合适的参数就变了；" data-title="英特尔面向四至六代至强处理器推出推理微服务：自动检测硬件并配置 vLLM 参数" data-date="10-14 23:13" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-14 23:13</span>
          <span class="news-item-title">英特尔面向四至六代至强处理器推出推理微服务：自动检测硬件并配置 vLLM 参数</span>
          <span class="news-value-point">💡 IT之家 10 月 14 日消息，英特尔今日宣布推出 Intel Inference Microservices 服务，这是一套面向大语言模型推…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/14/save-50-on-your-techcrunch-disrupt-2026-ticket-and-join-the-last-two-days-in-san-francisco/" target="_blank" rel="noopener" data-cat="keji" data-summary="10月14日至15日在旧金山举行的TechCrunch Disrupt 2026的最后两天活动可享受50%的折扣。立即注册，加入创业生态系统的其余部分。如今，这一切都与物理和软件人工智能有关。" data-title="Save 50% on your TechCrunch Disrupt 2026 ticket and join the last 2 days in San Francisco’s Moscone West" data-date="10-14 23:13" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-14 23:13</span>
          <span class="news-item-title">节省50%的TechCrunch Disrupt 2026门票，加入旧金山Moscone West的最后2天</span>
          <span class="news-item-title-en">Save 50% on your TechCrunch Disrupt 2026 ticket and join the last 2 days in San Francisco’s Moscone West</span>
          <span class="news-value-point">💡 10月14日至15日在旧金山举行的TechCrunch Disrupt 2026的最后两天活动可享受50%的折扣</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/013/129.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 14 日消息，今日，IBM 与西门子宣布达成一项新的研究合作，旨在推进 IBM 今年早些时候发布的纳米堆叠（nanostack）晶体管架构。据 IBM 官方新闻稿，此次合作将结合 IBM 在半导体器件创新领域的领导地位与西门子在电子设计自动化（EDA）、工艺仿真、光刻优化及先进制造软件方面的专业能力，以加速纳米堆叠技术的开发。据介绍，双方合作内容包括开发纳米堆叠的先进虚拟模型，以便在芯片制造之前对性能进行建模、优化设计并解决制造难题。IBM 在今年 6 月首次发布了纳米堆叠架构，并称其为业界首个已知的三维纳米片设计。与当前将晶体管平铺在二维平面上并不断缩小间距的思路不同，纳米堆叠将晶体管垂直堆叠并错位排列，从而在相同面积内容纳更多晶体管。在当前的 7 埃（0.7 纳米）节" data-title="IBM 与西门子合作推进纳米堆叠架构，加速 3D 晶体管量产进程" data-date="10-14 23:12" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-14 23:12</span>
          <span class="news-item-title">IBM 与西门子合作推进纳米堆叠架构，加速 3D 晶体管量产进程</span>
          <span class="news-value-point">💡 IT之家 10 月 14 日消息，今日，IBM 与西门子宣布达成一项新的研究合作，旨在推进 IBM 今年早些时候发布的纳米堆叠（nanostac…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/14/floqers-ai-agents-help-b2b-revenue-teams-research-customers/" target="_blank" rel="noopener" data-cat="keji" data-summary="Floqer试图解决的问题对于任何从事销售或收入运营的人来说都是熟悉的。" data-title="Floqer’s AI agents research sales prospects so teams don’t have to" data-date="10-14 23:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-14 23:00</span>
          <span class="news-item-title">Floqer的人工智能代理研究销售前景，因此团队不必</span>
          <span class="news-item-title-en">Floqer’s AI agents research sales prospects so teams don’t have to</span>
          <span class="news-value-point">💡 Floqer试图解决的问题对于任何从事销售或收入运营的人来说都是熟悉的</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/14/techcrunch-disrupt-2026-day-2/" target="_blank" rel="noopener" data-cat="keji" data-summary="TechCrunch Disrupt 2026的第2天，充满了人工智能的所有主题，仅限投资者的会议，更多的圆桌会议等等。注册即可享受通行证五折优惠。" data-title="TechCrunch Disrupt 2026: Day 2" data-date="10-14 22:30" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-14 22:30</span>
          <span class="news-item-title">TechCrunch Disrupt 2026 ：第2天</span>
          <span class="news-item-title-en">TechCrunch Disrupt 2026: Day 2</span>
          <span class="news-value-point">💡 TechCrunch Disrupt 2026的第2天，充满了人工智能的所有主题，仅限投资者的会议，更多的圆桌会议等等</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/ssds/sk-hynix-to-place-custom-tiny-cpu-cores-in-its-ssd-controllers-to-ease-arm-load-as-drive-speeds-rocket-each-h-tpu-reportedly-draws-2-5-percent-of-a-cpu-cores-power" target="_blank" rel="noopener" data-cat="keji" data-summary="SK海力士详细介绍了H-TPU ，这是一个微小的内部内核，可以从其下一代企业级SSD控制器的Arm CPU中卸载例行I/O。" data-title="SK hynix to place custom tiny CPU cores in its SSD controllers to ease Arm load as drive speeds rocket" data-date="10-14 22:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-14 22:00</span>
          <span class="news-item-title">SK海力士将在其固态硬盘控制器中放置定制的微型CPU内核，以缓解ARM负载</span>
          <span class="news-item-title-en">SK hynix to place custom tiny CPU cores in its SSD controllers to ease Arm load as drive speeds rocket</span>
          <span class="news-value-point">💡 SK海力士详细介绍了H-TPU ，这是一个微小的内部内核，可以从其下一代企业级SSD控制器的Arm CPU中卸载例行I/O</span>
        </a>
        <a class="news-item" href="https://arstechnica.com/security/2026/10/anthropic-warns-small-ai-models-could-self-replicate-through-iot-devices/" target="_blank" rel="noopener" data-cat="keji" data-summary="“基于体重的小型复制器”可能会引入新一代的计算机蠕虫。" data-title="Anthropic warns small AI models could self-replicate through IoT devices" data-date="10-14 20:55" data-source="Ars Technica">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-arstechnica">🔬 Ars Technica</span>
          <span class="news-item-date">10-14 20:55</span>
          <span class="news-item-title">Anthropic警告小型人工智能模型可能会通过物联网设备自我复制</span>
          <span class="news-item-title-en">Anthropic warns small AI models could self-replicate through IoT devices</span>
          <span class="news-value-point">💡 “基于体重的小型复制器”可能会引入新一代的计算机蠕虫</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/analyzing-intels-emib-and-foveros-advanced-packaging-roadmaps-how-intel-plans-to-scale-chips-in-every-direction" target="_blank" rel="noopener" data-cat="keji" data-summary="英特尔是第一家在2017 – 2019年开始使用先进封装方法的大型芯片制造商。但英特尔的EMIB和Foveros技术如今在哪里，它们的发展方向又在哪里？" data-title="Analyzing Intel&#39;s EMIB and Foveros advanced packaging roadmaps" data-date="10-14 20:50" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-14 20:50</span>
          <span class="news-item-title">分析英特尔的EMIB和Foveros高级封装路线图</span>
          <span class="news-item-title-en">Analyzing Intel's EMIB and Foveros advanced packaging roadmaps</span>
          <span class="news-value-point">💡 英特尔是第一家在2017 – 2019年开始使用先进封装方法的大型芯片制造商</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">5 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cvp8g57ne53xo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利桑德罗·马丁内斯（ Lisandro Martinez ）在曼联冠军联赛被马德里竞技（ Atletico Madrid ）击败后发表的爆炸性评论让足球总监杰森·威尔科克斯（ Jason Wilcox ）" data-title="Wilcox the target again in another damaging Man Utd fallout" data-date="10-14 23:30" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-14 23:30</span>
          <span class="news-item-title">威尔科克斯在另一次曼联破坏性影响中再次成为目标</span>
          <span class="news-item-title-en">Wilcox the target again in another damaging Man Utd fallout</span>
          <span class="news-value-point">💡 利桑德罗·马丁内斯（ Lisandro Martinez ）在曼联冠军联赛被马德里竞技（ Atletico Madrid ）击败后发表的爆炸性评…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/news/articles/c83vq9vpwwr1o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="自从俱乐部因违反英超联赛规则而被判有罪以来，总理一直承受着越来越大的压力。" data-title="Burnham had two hospitality dinners with Man City chairman, deleted records show" data-date="10-14 20:47" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-14 20:47</span>
          <span class="news-item-title">伯纳姆与曼城主席共进了两顿招待晚餐，删除了记录显示</span>
          <span class="news-item-title-en">Burnham had two hospitality dinners with Man City chairman, deleted records show</span>
          <span class="news-value-point">💡 自从俱乐部因违反英超联赛规则而被判有罪以来，总理一直承受着越来越大的压力</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ckwy4nj4842qo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="延长三周的休息时间可能比英超联赛中任何其他球队都更能让切尔西受益。" data-title="Did Chelsea benefit most from extended international break?" data-date="10-14 18:43" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-14 18:43</span>
          <span class="news-item-title">切尔西是否从延长的国际休息中获益最多？</span>
          <span class="news-item-title-en">Did Chelsea benefit most from extended international break?</span>
          <span class="news-value-point">💡 延长三周的休息时间可能比英超联赛中任何其他球队都更能让切尔西受益</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cx054n684g7do?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="由于别墅公园的北展台目前因建筑工程而关闭，容量减少是否会影响阿斯顿维拉的表现？" data-title="&#39;No excuses&#39; - but is Villa&#39;s stadium rebuild affecting team?" data-date="10-14 13:41" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-14 13:41</span>
          <span class="news-item-title">“没有借口” -但维拉的体育场重建是否会影响球队？</span>
          <span class="news-item-title-en">'No excuses' - but is Villa's stadium rebuild affecting team?</span>
          <span class="news-value-point">💡 由于别墅公园的北展台目前因建筑工程而关闭，容量减少是否会影响阿斯顿维拉的表现</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ck9qzwp9ejgro?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在上个月被排除在托特纳姆热刺的英超球队之外之后，理查利森被留给了21岁以下球队。" data-title="Goal crisis &amp; in drop zone - so why is Spurs&#39; £60m striker stuck in U21s?" data-date="10-14 04:39" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-14 04:39</span>
          <span class="news-item-title">进球危机和落后区-那么为什么马刺队的£ 6000万前锋被困在U21中？</span>
          <span class="news-item-title-en">Goal crisis & in drop zone - so why is Spurs' £60m striker stuck in U21s?</span>
          <span class="news-value-point">💡 在上个月被排除在托特纳姆热刺的英超球队之外之后，理查利森被留给了21岁以下球队</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/10/14/business/starshield-spacex-ukraine-starlink-satellites-musk.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="多年来，乌克兰武装部队一直依赖埃隆·马斯克（ Elon Musk ）的SpaceX开发的卫星通信服务。最近的限制阻碍了其战争努力。" data-title="What Is Starshield, SpaceX’s Military-Grade Satellite Internet Service Ukraine Relies On?" data-date="10-15 01:06" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-15 01:06</span>
          <span class="news-item-title">什么是SpaceX的军用级卫星互联网服务Starshield乌克兰依赖？</span>
          <span class="news-item-title-en">What Is Starshield, SpaceX’s Military-Grade Satellite Internet Service Ukraine Relies On?</span>
          <span class="news-value-point">💡 多年来，乌克兰武装部队一直依赖埃隆·马斯克（ Elon Musk ）的SpaceX开发的卫星通信服务</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/14/science/pope-leo-lung-cancer-therapies-genetic-mutations.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="肺癌仍然是癌症死亡的主要原因，但这一比率是20世纪90年代的一半，部分原因是新开发的治疗方法正在发挥作用。" data-title="A New World of Lung Cancer Therapy Awaits Pope Leo" data-date="10-15 01:02" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-15 01:02</span>
          <span class="news-item-title">肺癌治疗的新世界等待着教皇利奥</span>
          <span class="news-item-title-en">A New World of Lung Cancer Therapy Awaits Pope Leo</span>
          <span class="news-value-point">💡 肺癌仍然是癌症死亡的主要原因，但这一比率是20世纪90年代的一半，部分原因是新开发的治疗方法正在发挥作用</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/14/world/europe/pope-leo-xiv-cancer-diagnosis.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="教皇利奥十四世被诊断出患有一种常见的肺癌。梵蒂冈表示，他正在行走，并在手术切除癌性结节后接受治疗。" data-title="Pope Leo’s Cancer Diagnosis: What Happens Next" data-date="10-15 00:32" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-15 00:32</span>
          <span class="news-item-title">教皇利奥的癌症诊断：接下来会发生什么</span>
          <span class="news-item-title-en">Pope Leo’s Cancer Diagnosis: What Happens Next</span>
          <span class="news-value-point">💡 教皇利奥十四世被诊断出患有一种常见的肺癌</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1011245/iphone-duo-repair-costs-applecare" target="_blank" rel="noopener" data-cat="zonghe" data-summary="如果您没有购买适用于iPhone Duo的AppleCare Plus ，任何维修都将非常昂贵。据MacRumors报道，苹果今天公布了没有AppleCare Plus的iPhone Duo的估计维修费用，这些费用可能很高：电池服务器" data-title="Repairing the iPhone Duo’s folding screen costs as much as a new iPhone" data-date="10-15 00:21" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-15 00:21</span>
          <span class="news-item-title">维修iPhone Duo的折叠屏幕的成本与新iPhone一样高</span>
          <span class="news-item-title-en">Repairing the iPhone Duo’s folding screen costs as much as a new iPhone</span>
          <span class="news-value-point">💡 如果您没有购买适用于iPhone Duo的AppleCare Plus ，任何维修都将非常昂贵</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/news/1011216/xbox-nano-controller-release-date-pricing" target="_blank" rel="noopener" data-cat="zonghe" data-summary="微软今天正式宣布推出其Xbox Nano控制器，这是一款更小、更便宜的控制器，专为放入您的口袋而设计。更紧凑的控制器也专为“年轻玩家、小手或任何寻求东西的人”而设计" data-title="Honey, Xbox shrunk its controller" data-date="10-15 00:16" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-15 00:16</span>
          <span class="news-item-title">亲爱的， Xbox缩小了它的控制器</span>
          <span class="news-item-title-en">Honey, Xbox shrunk its controller</span>
          <span class="news-value-point">💡 微软今天正式宣布推出其Xbox Nano控制器，这是一款更小、更便宜的控制器，专为放入您的口袋而设计</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1011202/meta-whatsapp-guest-calls" target="_blank" rel="noopener" data-cat="zonghe" data-summary="WhatsApp的全新访客通话功能允许您邀请任何人进行通话，而无需他们先创建账号。他们也不需要该应用程序，因为Meta今年早些时候还增加了对WhatsApp网络版通话的支持。您" data-title="Now you can call anyone with WhatsApp, even if they don’t have WhatsApp" data-date="10-15 00:03" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-15 00:03</span>
          <span class="news-item-title">现在，您可以通过WhatsApp致电任何人，即使他们没有WhatsApp</span>
          <span class="news-item-title-en">Now you can call anyone with WhatsApp, even if they don’t have WhatsApp</span>
          <span class="news-value-point">💡 WhatsApp的全新访客通话功能允许您邀请任何人进行通话，而无需他们先创建账号</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1010928/android-scam-protection-enhanced-protection-google-messages" target="_blank" rel="noopener" data-cat="zonghe" data-summary="安卓推出了新的诈骗防御功能，旨在让用户更轻松地规避移动欺诈，包括加强Google消息中的防护和其他防护工具。以Google消息中的诈骗检测功能为基础" data-title="Android is using AI to suss out scammers in Google Messages" data-date="10-15 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-15 00:00</span>
          <span class="news-item-title">安卓正在使用人工智能来识别谷歌消息中的诈骗者</span>
          <span class="news-item-title-en">Android is using AI to suss out scammers in Google Messages</span>
          <span class="news-value-point">💡 安卓推出了新的诈骗防御功能，旨在让用户更轻松地规避移动欺诈，包括加强Google消息中的防护和其他防护工具</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/pc-gaming/epic-games-vibe-codes-new-launcher-because-programming-is-hard-starts-46-percent-faster-than-steam-preview-is-available-now-but-not-recommended-for-competitive-players" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Epic Games在预览版中引入了一个重新设计的启动器，该公司表示，这是因为“编程很难”。" data-title="Epic Games vibe codes new launcher because &#39;programming is hard,&#39; claims it starts 46% faster than Steam" data-date="10-14 23:44" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-14 23:44</span>
          <span class="news-item-title">Epic Games vibe对新启动器进行编码，因为“编程很难” ，声称它的启动速度比Steam快46%</span>
          <span class="news-item-title-en">Epic Games vibe codes new launcher because 'programming is hard,' claims it starts 46% faster than Steam</span>
          <span class="news-value-point">💡 Epic Games在预览版中引入了一个重新设计的启动器，该公司表示，这是因为“编程很难”</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/013/134.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 14 日消息，赛力斯集团董事、副总裁康波今日分享了一篇《华尔街日报》的报道，其中提到中国车如今主导了欧洲最大的车展。康波透露自己也接受了《华尔街日报》的采访，而自己在采访中也提到，面对欧洲豪华车市场的严苛标准，要让当地消费者认可中国品牌的豪华车需要时间，但相信我们终将做到。据IT之家此前报道，赛力斯集团旗下豪华电动汽车品牌问界 10 月 12 日在巴黎车展宣布，计划 2027 年秋季进军欧洲市场，为欧洲用户带来全新智能出行体验。相关阅读：《问界官宣 2027 年秋季进军欧洲市场，力争年内获得 Euro NCAP 五星评级》" data-title="赛力斯康波：面对欧洲豪华车市场严苛标准，要让当地消费者认可中国品牌需要时间" data-date="10-14 23:28" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-14 23:28</span>
          <span class="news-item-title">赛力斯康波：面对欧洲豪华车市场严苛标准，要让当地消费者认可中国品牌需要时间</span>
          <span class="news-value-point">💡 IT之家 10 月 14 日消息，赛力斯集团董事、副总裁康波今日分享了一篇《华尔街日报》的报道，其中提到中国车如今主导了欧洲最大的车展</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/013/133.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 14 日消息，据 Steam Frame Hub 今天报道，Valve 的 VR 头显 Steam Frame 近期发售。不过V社如今可能已在开发后续产品，带来分辨率等方面升级。公开的 Linux 内核源码显示，新款 Steam Frame 代号为“Plano”，配备 Micro-OLED 显示屏，单眼原生分辨率为 3552*3840。作为对比，现款产品配备两块 LCD 屏幕，分辨率为 2160*2160。如果上述数据准确，新款 Steam Frame 的单眼像素数将达到老款的 3 倍，OLED 面板也能带来更高对比度。值得注意的是，这款头显的显示屏规格与三星 Galaxy XR 几乎一致。后者同样采用分辨率为 3552*3840、刷新率最高为 90Hz 的 Micro-" data-title="消息称 Steam Frame OLED 头显正在开发：代号 Plano，单眼原生分辨率 3552*3840" data-date="10-14 23:23" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-14 23:23</span>
          <span class="news-item-title">消息称 Steam Frame OLED 头显正在开发：代号 Plano，单眼原生分辨率 3552*3840</span>
          <span class="news-value-point">💡 IT之家 10 月 14 日消息，据 Steam Frame Hub 今天报道，Valve 的 VR 头显 Steam Frame 近期发售</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/013/132.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 14 日消息，据深蓝财经报道，赛力斯汽车有限公司对外披露，已对一名抖音平台短视频用户提起民事诉讼。该用户借助 AI 工具合成问界车辆行驶中车身塌陷的虚假画面，发布到网络抹黑车辆安全性能。案件将于 10 月 23 日在重庆市两江新区人民法院开庭审理。该用户使用 AI 生成虚假视频，伪造问界车辆行驶过程中车身塌陷的画面，视频标注问界品牌，暗示车辆存在严重安全缺陷，发布于抖音平台。赛力斯要求对方删除侵权言论、公开书面赔礼道歉、支付 100 万元侵权损害赔偿，并承担案件相关诉讼费用。该用户被告收到传票后在社群称，这只是“阴阳视频”，并表示自己不会购买鸿蒙智行车辆，后续自行删除了这条 AI 造假视频。报道提到，该用户为抖音普通短视频用户，账号有 57 个粉丝，非专业汽车自媒体，其视" data-title="男子发布 AI 视频造谣问界，赛力斯起诉索赔百万元" data-date="10-14 23:20" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-14 23:20</span>
          <span class="news-item-title">男子发布 AI 视频造谣问界，赛力斯起诉索赔百万元</span>
          <span class="news-value-point">💡 IT之家 10 月 14 日消息，据深蓝财经报道，赛力斯汽车有限公司对外披露，已对一名抖音平台短视频用户提起民事诉讼</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/14/deezer-will-soon-let-you-filter-out-ai-generated-music/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Deezer表示，新开关将在今年年底前推出。" data-title="Deezer will soon let you filter out AI" data-date="10-14 23:16" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-14 23:16</span>
          <span class="news-item-title">Deezer将很快让您过滤掉AI</span>
          <span class="news-item-title-en">Deezer will soon let you filter out AI</span>
          <span class="news-value-point">💡 Deezer表示，新开关将在今年年底前推出</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/14/zenzap-raises-44m-for-its-ai-chat-app-that-aims-to-replace-whatsapp-in-the-workplace/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Zenzap被包括星巴克和Taco Bell在内的组织使用。" data-title="Zenzap raises $44M for its AI chat app that aims to replace WhatsApp in the workplace" data-date="10-14 23:08" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-14 23:08</span>
          <span class="news-item-title">Zenzap为其旨在取代工作场所WhatsApp的人工智能聊天应用程序筹集了4400万$</span>
          <span class="news-item-title-en">Zenzap raises $44M for its AI chat app that aims to replace WhatsApp in the workplace</span>
          <span class="news-value-point">💡 Zenzap被包括星巴克和Taco Bell在内的组织使用</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-14/10714740.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京10月14日电 (记者 孙自法)“鸟类的起源和早期演化始终以适应飞行为主”这一传统认知，最近被中国的化石新发现和中国科研团队的研究成果所打破。" data-title="中国发现侏罗纪不会飞鸟类杨源𬸚𬸦 颠覆鸟类早期演化传统认知" data-date="10-14 23:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 23:07</span>
          <span class="news-item-title">中国发现侏罗纪不会飞鸟类杨源𬸚𬸦 颠覆鸟类早期演化传统认知</span>
          <span class="news-value-point">💡 中新网北京10月14日电 (记者 孙自法)“鸟类的起源和早期演化始终以适应飞行为主”这一传统认知，最近被中国的化石新发现和中国科研团队的研究成果…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-14/10714733.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网广州10月14日电 (程景伟 林荫)据广东省林业局14日消息，广东省近日发布2026年第3号总林长令——《关于加强森林防灭火与鸟类保护工作的令》，强调10月起该省将进入森林特别防护期，也是候鸟迁徙过境、越冬栖息的关键时期。总林长令要求各级林长要一体谋划、一体落实森林防灭火和候鸟保护工作。" data-title="广东发布总林长令加强森林防灭火与鸟类保护工作" data-date="10-14 23:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-14 23:01</span>
          <span class="news-item-title">广东发布总林长令加强森林防灭火与鸟类保护工作</span>
          <span class="news-value-point">💡 中新网广州10月14日电 (程景伟 林荫)据广东省林业局14日消息，广东省近日发布2026年第3号总林长令——《关于加强森林防灭火与鸟类保护工作…</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-15 01:23（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
