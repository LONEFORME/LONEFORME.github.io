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
      <span>2026-10-18 14:42 抓取更新</span>
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
        <span class="channel-count">57</span>
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
        <span class="channel-count">13</span>
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
  <div class="ov-item"><span class="ov-num">57</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×20 · IT之家×8</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/10-18/10716615.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月18日电 (记者 马帅莎 李纯 周昕)在2026世界传统医药大会上，全球传统医学联盟正式成立。全球传统医学联盟副主席兼秘书长秦怀金18日在北京介绍称，全球传统医学联盟是国际上首个覆盖全球多元传统医学体系的非政府、非营利国际科技组织，联盟秘书处设在中国北京。" data-title="全球传统医学联盟成立 构建传统医学国际共同体" data-date="10-18 14:25" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-18 14:25</span>
      </div>
      <h2 class="hero-featured-title">全球传统医学联盟成立 构建传统医学国际共同体</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/014/492.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 18 日消息，长安启源宣布，2027 款长安启源 Q07 天枢领航版将于 10 月 20 日焕新上市。此外，长安启源 Q07 激光版的天枢领航 Pro 高阶智能驾驶辅助系统陆续开启 OTA 推送升级，升级内容包含城市领航辅助功能。官方随后公布了全新车色“星汉紫”，号称“采天地之色，蕴星河之境”。官方今日宣布，2027 款长安启源 Q07 天枢领航版全系搭载天枢领航 Pro，支持高速领航辅助、记忆泊车辅助、城市领航辅助。作为参考，2025 年 10 月，长安启源 Q07 天枢智能激光版车型上市，搭载天枢驾驶辅助激光版，配备 1 颗激光雷达和地平线 J6M 驾驶芯片，拥有 128TOPS 算力；支持车道巡航辅助、高速 / 快速路领航驾驶辅助、关门泊入、遥控挪泊辅助、自定义车位" data-title="2027 款长安启源 Q07 天枢领航版车型 10 月 20 日上市，新增“星汉紫”车色" data-date="10-18 14:23" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">2027 款长安启源 Q07 天枢领航版车型 10 月 20 日上市，新增“星汉紫”车色</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/c6je5lwxk5l0o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="一位知名律师告诉BBC Sport ，曼城在被判犯有违反英超联赛财务规则的罪行后，如果他们有机会赢得上诉，他们将面临“重大障碍”。" data-title="Do Manchester City have any grounds to win their appeal?" data-date="10-18 14:36" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">Do Manchester City have any grounds to win their appeal?</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/014/502.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 18 日消息，据易车报道，长安猎手 K70 皮卡将在 10 月 23 日上市，新车采用家族化外观，搭载 2.0T 增程系统，拥有 33 英寸越野 AT 胎。从外观来看，长安猎手 K70 前脸延续家族设计，配备黑色的无边界式格栅，两侧是 T 型大灯，前包围预留绞盘安装位，支持用户按需选装，营造越野气场。该车还将搭配 33 英寸越野轮胎，配套 17 英寸轮圈。同时，该车的货箱支持分段开启，后包围拥有拖车方口，拥有合法拖拽资质。车辆离地间隙 245mm，接近角 38 度，离去角 28 度。IT之家注意到，该车将搭载增程动力系统，搭载 2.0T 发动机，最大功率 140kW，前后电机最大功率分别为 110kW、150kW，综合功率 260kW，综合扭矩 550 N·m，提供低速挡" data-title="长安猎手 K70 皮卡 10 月 23 日上市：2.0T 增程，配备越野 AT 轮胎" data-date="10-18 14:42" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">长安猎手 K70 皮卡 10 月 23 日上市：2.0T 增程，配备越野 AT 轮胎</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-18/10716615.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月18日电 (记者 马帅莎 李纯 周昕)在2026世界传统医药大会上，全球传统医学联盟正式成立。全球传统医学联盟副主席兼秘书长秦怀金18日在北京介绍称，全球传统医学联盟是国际上首个覆盖全球多元传统医学体系的非政府、非营利国际科技组织，联盟秘书处设在中国北京。" data-title="全球传统医学联盟成立 构建传统医学国际共同体" data-date="10-18 14:25" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 14:25</span>
          <span class="news-item-title">全球传统医学联盟成立 构建传统医学国际共同体</span>
          <span class="news-value-point">💡 中新社北京10月18日电 (记者 马帅莎 李纯 周昕)在2026世界传统医药大会上，全球传统医学联盟正式成立</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-18/10716623.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月18日电 (记者 谢雁冰)第八届中国反腐倡廉发展史暨廉政文献创新与发展研讨会18日在北京召开。" data-title="第八届中国反腐倡廉发展史暨廉政文献创新与发展研讨会在北京召开" data-date="10-18 14:19" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 14:19</span>
          <span class="news-item-title">第八届中国反腐倡廉发展史暨廉政文献创新与发展研讨会在北京召开</span>
          <span class="news-value-point">💡 中新网北京10月18日电 (记者 谢雁冰)第八届中国反腐倡廉发展史暨廉政文献创新与发展研讨会18日在北京召开</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-18/10716608.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月18日电 综合消息：以色列总理办公室当地时间17日发表声明，回应当天欧洲官员车队在约旦河西岸遭犹太定居者袭击事件，敦促各方谨慎对待有关报道，“切勿妄下结论”。" data-title="以色列回应欧洲官员在约旦河西岸遇袭：“切勿妄下结论”" data-date="10-18 13:58" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 13:58</span>
          <span class="news-item-title">以色列回应欧洲官员在约旦河西岸遇袭：“切勿妄下结论”</span>
          <span class="news-value-point">💡 中新社北京10月18日电 综合消息：以色列总理办公室当地时间17日发表声明，回应当天欧洲官员车队在约旦河西岸遭犹太定居者袭击事件，敦促各方谨慎对…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-18/10716597.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月18日电 综合多家日媒报道，在日本爱媛县西条市17日举行的传统庆典活动上，参与抬运的西条市副市长难波江明广(62岁)被重约3吨的太鼓台压住，不幸身亡。" data-title="日本一副市长参与庆典活动时被重约3吨太鼓台压住 不幸身亡" data-date="10-18 13:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 13:44</span>
          <span class="news-item-title">日本一副市长参与庆典活动时被重约3吨太鼓台压住 不幸身亡</span>
          <span class="news-value-point">💡 中新网10月18日电 综合多家日媒报道，在日本爱媛县西条市17日举行的传统庆典活动上，参与抬运的西条市副市长难波江明广(62岁)被重约3吨的太鼓…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-18/10716537.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月18日电 据印度媒体报道，印度东部西孟加拉邦首府加尔各答一处印度教节日庆祝活动现场17日晚发生踩踏事故，造成至少19人死亡，约35人受伤。事发后，多名印度政界人士表达哀悼，并呼吁追究责任。" data-title="印度踩踏事故致19死35伤 莫迪哀悼" data-date="10-18 13:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 13:43</span>
          <span class="news-item-title">印度踩踏事故致19死35伤 莫迪哀悼</span>
          <span class="news-value-point">💡 中新网10月18日电 据印度媒体报道，印度东部西孟加拉邦首府加尔各答一处印度教节日庆祝活动现场17日晚发生踩踏事故，造成至少19人死亡，约35人…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-18/10716605.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月18日电 题：这场会上，习近平说“今天可能要让你们失望了”" data-title="习言道｜这场会上，习近平说“今天可能要让你们失望了”" data-date="10-18 13:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 13:39</span>
          <span class="news-item-title">习言道｜这场会上，习近平说“今天可能要让你们失望了”</span>
          <span class="news-value-point">💡 中新网10月18日电 题：这场会上，习近平说“今天可能要让你们失望了”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-18/10716607.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社福建厦门10月18日电 题：厦门大学德旺图书馆：“玩”启数学之趣 “修”中触摸传承" data-title="（文化新纪行｜校馆弦歌）厦门大学德旺图书馆：“玩”启数学之趣 “修”中触摸传承" data-date="10-18 13:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 13:36</span>
          <span class="news-item-title">（文化新纪行｜校馆弦歌）厦门大学德旺图书馆：“玩”启数学之趣 “修”中触摸传承</span>
          <span class="news-value-point">💡 中新社福建厦门10月18日电 题：厦门大学德旺图书馆：“玩”启数学之趣 “修”中触摸传承</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-18/10716606.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社海口10月18日电 (记者 阮煜琳)2026海洋保护大会活动16日至18日在海口举行。" data-title="2026海洋保护大会在海口举行" data-date="10-18 13:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 13:34</span>
          <span class="news-item-title">2026海洋保护大会在海口举行</span>
          <span class="news-value-point">💡 中新社海口10月18日电 (记者 阮煜琳)2026海洋保护大会活动16日至18日在海口举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-18/10716601.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月18日电 中国官方18日通报，广西壮族自治区政协原副主席黄日波涉嫌严重职务违法，目前正接受国家监委监察调查。" data-title="广西壮族自治区政协原副主席黄日波接受国家监委监察调查" data-date="10-18 13:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 13:31</span>
          <span class="news-item-title">广西壮族自治区政协原副主席黄日波接受国家监委监察调查</span>
          <span class="news-value-point">💡 中新社北京10月18日电 中国官方18日通报，广西壮族自治区政协原副主席黄日波涉嫌严重职务违法，目前正接受国家监委监察调查</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-18/10716594.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中国新闻周刊记者：曹然" data-title="万米高空惊魂：一次失败的“自杀式袭击”" data-date="10-18 12:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 12:04</span>
          <span class="news-item-title">万米高空惊魂：一次失败的“自杀式袭击”</span>
          <span class="news-value-point">💡 中国新闻周刊记者：曹然</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/18/world/asia/india-gandhi-political-dynasty.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="拉胡尔·甘地是三位总理的后裔。抗议活动的激增可能会给他带来一块跳板，迎战现任国家领导人。" data-title="In India, the Scion of a Political Dynasty Tries to Seize His Moment" data-date="10-18 12:01" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-18 12:01</span>
          <span class="news-item-title">在印度，一个政治王朝的后裔试图抓住他的时机</span>
          <span class="news-item-title-en">In India, the Scion of a Political Dynasty Tries to Seize His Moment</span>
          <span class="news-value-point">💡 拉胡尔·甘地是三位总理的后裔</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-18/10716590.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月18日电 综合巴基斯坦媒体报道，巴基斯坦安全部门消息人士17日表示，阿富汗武装人员当天在巴基斯坦西北部开伯尔－普什图省巴阿边境地带无端开火，巴安全部队已对此作出有效回应。" data-title="巴媒：巴基斯坦打击阿富汗武装边境军营，打死数名阿武装人员" data-date="10-18 11:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 11:59</span>
          <span class="news-item-title">巴媒：巴基斯坦打击阿富汗武装边境军营，打死数名阿武装人员</span>
          <span class="news-value-point">💡 中新网10月18日电 综合巴基斯坦媒体报道，巴基斯坦安全部门消息人士17日表示，阿富汗武装人员当天在巴基斯坦西北部开伯尔－普什图省巴阿边境地带无…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-18/10716568.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网约翰内斯堡10月18日电 非洲高山王国莱索托全国麻醉医师协会近日在中国援建医院马塞卢地区医院学术报告厅举办了一场麻醉学术会议，吸引莱索托麻醉医生、麻醉护士、手术室护士及部分重症医学科、急诊科的专家学者与会。" data-title="中国援外麻醉医生在莱索托开展困难气道培训" data-date="10-18 11:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 11:47</span>
          <span class="news-item-title">中国援外麻醉医生在莱索托开展困难气道培训</span>
          <span class="news-value-point">💡 中新网约翰内斯堡10月18日电 非洲高山王国莱索托全国麻醉医师协会近日在中国援建医院马塞卢地区医院学术报告厅举办了一场麻醉学术会议，吸引莱索托麻…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-18/10716566.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月18日电 据也门胡塞武装控制的萨巴通讯社当地时间18日凌晨报道，沙特主导的多国联军对也门荷台达省发动两次空袭。" data-title="也门媒体报道沙特空袭荷台达 胡塞武装称击落沙特直升机" data-date="10-18 11:46" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 11:46</span>
          <span class="news-item-title">也门媒体报道沙特空袭荷台达 胡塞武装称击落沙特直升机</span>
          <span class="news-value-point">💡 中新社北京10月18日电 据也门胡塞武装控制的萨巴通讯社当地时间18日凌晨报道，沙特主导的多国联军对也门荷台达省发动两次空袭</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-18/10716587.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="晶采观察丨健康中国迈入“十五五” 这场大会释放多重新信号" data-title="健康中国迈入“十五五” 这场大会释放多重新信号" data-date="10-18 11:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 11:44</span>
          <span class="news-item-title">健康中国迈入“十五五” 这场大会释放多重新信号</span>
          <span class="news-value-point">💡 晶采观察丨健康中国迈入“十五五” 这场大会释放多重新信号</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">14 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/014/492.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 18 日消息，长安启源宣布，2027 款长安启源 Q07 天枢领航版将于 10 月 20 日焕新上市。此外，长安启源 Q07 激光版的天枢领航 Pro 高阶智能驾驶辅助系统陆续开启 OTA 推送升级，升级内容包含城市领航辅助功能。官方随后公布了全新车色“星汉紫”，号称“采天地之色，蕴星河之境”。官方今日宣布，2027 款长安启源 Q07 天枢领航版全系搭载天枢领航 Pro，支持高速领航辅助、记忆泊车辅助、城市领航辅助。作为参考，2025 年 10 月，长安启源 Q07 天枢智能激光版车型上市，搭载天枢驾驶辅助激光版，配备 1 颗激光雷达和地平线 J6M 驾驶芯片，拥有 128TOPS 算力；支持车道巡航辅助、高速 / 快速路领航驾驶辅助、关门泊入、遥控挪泊辅助、自定义车位" data-title="2027 款长安启源 Q07 天枢领航版车型 10 月 20 日上市，新增“星汉紫”车色" data-date="10-18 14:23" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-18 14:23</span>
          <span class="news-item-title">2027 款长安启源 Q07 天枢领航版车型 10 月 20 日上市，新增“星汉紫”车色</span>
          <span class="news-value-point">💡 IT之家 10 月 18 日消息，长安启源宣布，2027 款长安启源 Q07 天枢领航版将于 10 月 20 日焕新上市</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/crz65gwv8gv5o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="研究发现越来越多毕业生利用人工智能在求职申请中编造个人资讯。但有人认为他们别无选择。" data-title="“我申请了200份工作”" data-date="10-18 08:32" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-18 08:32</span>
          <span class="news-item-title">“我申请了200份工作”</span>
          <span class="news-value-point">💡 研究发现越来越多毕业生利用人工智能在求职申请中编造个人资讯</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/17/meta-removes-language-that-raised-scraping-and-ai-training-concerns/" target="_blank" rel="noopener" data-cat="keji" data-summary="Meta发言人坚称，更新后的条款并未反映Meta爬网方式的变化。" data-title="Meta removes language that raised scraping and AI training concerns" data-date="10-18 05:31" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-18 05:31</span>
          <span class="news-item-title">Meta删除了引起抓取和人工智能培训问题的语言</span>
          <span class="news-item-title-en">Meta removes language that raised scraping and AI training concerns</span>
          <span class="news-value-point">💡 Meta发言人坚称，更新后的条款并未反映Meta爬网方式的变化</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/17/anthropic-says-its-workforce-has-become-less-junior-and-is-spending-more-time-in-meetings/" target="_blank" rel="noopener" data-cat="keji" data-summary="在过去的一年中， Anthropic的员工构成和工作类型发生了显着变化。" data-title="Anthropic says its workforce has become less junior and is spending more time in meetings" data-date="10-18 04:21" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-18 04:21</span>
          <span class="news-item-title">Anthropic表示，其员工队伍已经变得不那么初级了，并且在会议上花费了更多的时间</span>
          <span class="news-item-title-en">Anthropic says its workforce has become less junior and is spending more time in meetings</span>
          <span class="news-value-point">💡 在过去的一年中， Anthropic的员工构成和工作类型发生了显着变化</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/17/replit-is-no-longer-working-with-anthropic-ceo-says/" target="_blank" rel="noopener" data-cat="keji" data-summary="上周末， Masad澄清说， OpenAI将取代Anthropic作为其默认模型提供商。Claude仍将向平台上的客户提供服务。" data-title="Replit makes OpenAI its default over Anthropic, CEO says" data-date="10-18 02:48" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-18 02:48</span>
          <span class="news-item-title">首席执行官表示， Replit使OpenAI成为Anthropic的默认值</span>
          <span class="news-item-title-en">Replit makes OpenAI its default over Anthropic, CEO says</span>
          <span class="news-value-point">💡 上周末， Masad澄清说， OpenAI将取代Anthropic作为其默认模型提供商</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/quad-8-pin-mod-protects-the-usd8-500-rtx-5090-you-cant-replace-from-melting-modders-custom-power-solution-claims-to-fix-nvidia-16-pin-gpu-meltdowns" target="_blank" rel="noopener" data-cat="keji" data-summary="Redditor展示了用于Nvidia GeForce RTX显卡上16针电源连接器的全新四引脚8针电源转换套件。" data-title="Quad 8-pin mod protects the $8,500 RTX 5090 you can’t replace from melting" data-date="10-17 23:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-17 23:20</span>
          <span class="news-item-title">四引脚8引脚模块保护您无法更换的$ 8,500 RTX 5090</span>
          <span class="news-item-title-en">Quad 8-pin mod protects the $8,500 RTX 5090 you can’t replace from melting</span>
          <span class="news-value-point">💡 Redditor展示了用于Nvidia GeForce RTX显卡上16针电源连接器的全新四引脚8针电源转换套件</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1013409/meta-removes-language-that-may-have-allowed-it-to-scrape-news-sites" target="_blank" rel="noopener" data-cat="keji" data-summary="在强烈反对之后， Meta再次更新其条款，以删除暗示它可以从包括新闻网站在内的网站上抓取内容来训练其人工智能的语言。具体而言，以下语言不再出现在商业条款页面上： …… Meta" data-title="Meta removes language that may have allowed it to scrape news sites" data-date="10-17 23:04" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-17 23:04</span>
          <span class="news-item-title">Meta删除了可能允许其抓取新闻网站的语言</span>
          <span class="news-item-title-en">Meta removes language that may have allowed it to scrape news sites</span>
          <span class="news-value-point">💡 在强烈反对之后， Meta再次更新其条款，以删除暗示它可以从包括新闻网站在内的网站上抓取内容来训练其人工智能的语言</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-insists-the-rtx-5090-isnt-dead-despite-severe-shortages-and-removed-listings-at-multiple-retailers-flagship-gpu-is-missing-from-nvidias-store-and-commands-usd8-500-on-amazon" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达表示， RTX 5090并未停产，只是供应受到限制—但该卡实际上已从店面中消失" data-title="Nvidia reportedly insists the RTX 5090 isn&#39;t dead despite severe shortages and removed listings at multiple retailers" data-date="10-17 22:38" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-17 22:38</span>
          <span class="news-item-title">据报道，英伟达坚称，尽管RTX 5090严重短缺，并在多家零售商处删除了房源，但它并没有死</span>
          <span class="news-item-title-en">Nvidia reportedly insists the RTX 5090 isn't dead despite severe shortages and removed listings at multiple retailers</span>
          <span class="news-value-point">💡 英伟达表示， RTX 5090并未停产，只是供应受到限制—但该卡实际上已从店面中消失</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-lab-offers-free-plumbing-and-hvac-repairs-across-three-cities-to-train-ai-robots-wearable-sensors-record-video-of-repair-work-for-robotics-training-free-services-also-include-electrical-work-air-duct-cleaning-and-carpet-cleaning" target="_blank" rel="noopener" data-cat="keji" data-summary="HUMXN希望为明尼阿波利斯、芝加哥和迈阿密的房屋提供维护和维修服务，以收集数据来训练人工智能模型和机器人。" data-title="AI lab offers free plumbing and HVAC repairs across three cities to train AI robots" data-date="10-17 21:21" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-17 21:21</span>
          <span class="news-item-title">人工智能实验室在三个城市提供免费管道和HVAC维修，以培训人工智能机器人</span>
          <span class="news-item-title-en">AI lab offers free plumbing and HVAC repairs across three cities to train AI robots</span>
          <span class="news-value-point">💡 HUMXN希望为明尼阿波利斯、芝加哥和迈阿密的房屋提供维护和维修服务，以收集数据来训练人工智能模型和机器人</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-october-17-2026-packaging-roadmaps-chinese-dgx-spark-rival-emerges-and-digging-into-asmls-earnings" target="_blank" rel="noopener" data-cat="keji" data-summary="本周， Tom&#39;s Hardware Premium订阅者可以阅读我们的EMIB和Foveros路线图，以及中国在本地人工智能系统领域的最新竞争情况等。" data-title="This week on Tom&#39;s Hardware Premium: October 17, 2026" data-date="10-17 21:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-17 21:00</span>
          <span class="news-item-title">本周Tom's Hardware Premium ： 2026年10月17日</span>
          <span class="news-item-title-en">This week on Tom's Hardware Premium: October 17, 2026</span>
          <span class="news-value-point">💡 本周， Tom's Hardware Premium订阅者可以阅读我们的EMIB和Foveros路线图，以及中国在本地人工智能系统领域的最新竞争…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1013195/ai-agents-blocked-web" target="_blank" rel="noopener" data-cat="keji" data-summary="自主智能体是人工智能中最热门的东西。OpenAI、Meta、Google、Instinct和其他公司承诺，他们的代理可以代表您浏览互联网，从预订晚餐、清理收件箱到购买新鞋，无所不包。Bu" data-title="Websites are closing their doors to AI agents" data-date="10-17 21:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-17 21:00</span>
          <span class="news-item-title">网站正在向人工智能代理敞开大门</span>
          <span class="news-item-title-en">Websites are closing their doors to AI agents</span>
          <span class="news-value-point">💡 自主智能体是人工智能中最热门的东西</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/504067.html" target="_blank" rel="noopener" data-cat="keji" data-summary="新版本V4.1-Flash-1017，还开放了自研搜索API" data-title="突发！DeepSeek新模型发布，超级性价比斩杀一切" data-date="10-17 20:21" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-17 20:21</span>
          <span class="news-item-title">突发！DeepSeek新模型发布，超级性价比斩杀一切</span>
          <span class="news-value-point">💡 新版本V4.1-Flash-1017，还开放了自研搜索API</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/503965.html" target="_blank" rel="noopener" data-cat="keji" data-summary="AI的风还是刮到了法律圈" data-title="智谱新模型，懂法方面全球第一了" data-date="10-17 20:13" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-17 20:13</span>
          <span class="news-item-title">智谱新模型，懂法方面全球第一了</span>
          <span class="news-value-point">💡 AI的风还是刮到了法律圈</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/503910.html" target="_blank" rel="noopener" data-cat="keji" data-summary="谜底指向时间" data-title="Claude半小时解开密码学悬案，学界集体走偏20年" data-date="10-17 20:06" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-17 20:06</span>
          <span class="news-item-title">Claude半小时解开密码学悬案，学界集体走偏20年</span>
          <span class="news-value-point">💡 谜底指向时间</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">13 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6je5lwxk5l0o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="一位知名律师告诉BBC Sport ，曼城在被判犯有违反英超联赛财务规则的罪行后，如果他们有机会赢得上诉，他们将面临“重大障碍”。" data-title="Do Manchester City have any grounds to win their appeal?" data-date="10-18 14:36" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-18 14:36</span>
          <span class="news-item-title">曼城是否有任何理由赢得他们的上诉？</span>
          <span class="news-item-title-en">Do Manchester City have any grounds to win their appeal?</span>
          <span class="news-value-point">💡 一位知名律师告诉BBC Sport ，曼城在被判犯有违反英超联赛财务规则的罪行后，如果他们有机会赢得上诉，他们将面临“重大障碍”</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ck054652mv07o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿斯顿维拉是一支球队，约翰·曼赞比（ Johan Manzambi ）在对阵纽卡斯尔队的比赛中得分，他拒绝转会到维拉公园（ Villa Park ）。" data-title="Villa&#39;s Manzambi shows Newcastle what they missed out on" data-date="10-18 05:18" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-18 05:18</span>
          <span class="news-item-title">别墅的Manzambi向纽卡斯尔展示了他们错过的景点</span>
          <span class="news-item-title-en">Villa's Manzambi shows Newcastle what they missed out on</span>
          <span class="news-value-point">💡 阿斯顿维拉是一支球队，约翰·曼赞比（ Johan Manzambi ）在对阵纽卡斯尔队的比赛中得分，他拒绝转会到维拉公园（ Villa Park…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c9j34rke27zjo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="弗洛里安·维尔茨（ Florian Wirtz ）在利物浦重返英超联赛的胜利之路上发挥了重要作用，但他仍然是老板安东尼·伊拉奥拉（ Andoni Iraola ）的大难题" data-title="Wirtz delivers but remains Liverpool&#39;s conundrum" data-date="10-18 04:07" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-18 04:07</span>
          <span class="news-item-title">Wirtz取得了成功，但仍是利物浦的难题</span>
          <span class="news-item-title-en">Wirtz delivers but remains Liverpool's conundrum</span>
          <span class="news-value-point">💡 弗洛里安·维尔茨（ Florian Wirtz ）在利物浦重返英超联赛的胜利之路上发挥了重要作用，但他仍然是老板安东尼·伊拉奥拉（ Andoni…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/videos/c65yn28p859wo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦队在Gtech社区体育场以2比1击败布伦特福德队，东道主在Yehor Yarmoliuk和Vitaly Janelt的红牌后以9名男子结束比赛。" data-title="Liverpool come from behind to beat nine" data-date="10-18 03:00" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-18 03:00</span>
          <span class="news-item-title">利物浦从后面来到九强</span>
          <span class="news-item-title-en">Liverpool come from behind to beat nine</span>
          <span class="news-value-point">💡 利物浦队在Gtech社区体育场以2比1击败布伦特福德队，东道主在Yehor Yarmoliuk和Vitaly Janelt的红牌后以9名男子结束…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/17/newcastle-v-aston-villa-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="约翰·曼赞比（ Johan Manzambi ）在圣詹姆斯公园（ St James ’Park ）打进了给阿斯顿维拉（ Aston Villa ）应得胜利的唯一进球提醒球队看起来乔·威洛克（ Joe Willock ）将为纽卡斯尔（ Newcastle ）效力，乔林顿（ Joelinton ）与尼科·冈萨雷斯（ Nico Gonzalez ）并列中场。纽卡斯尔" data-title="Newcastle 0-1 Aston Villa: Premier League – as it happened" data-date="10-18 03:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-18 03:00</span>
          <span class="news-item-title">纽卡斯尔0-1阿斯顿维拉：英超联赛–事实如此</span>
          <span class="news-item-title-en">Newcastle 0-1 Aston Villa: Premier League – as it happened</span>
          <span class="news-value-point">💡 约翰·曼赞比（ Johan Manzambi ）在圣詹姆斯公园（ St James ’Park ）打进了给阿斯顿维拉（ Aston Villa …</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/17/newcastle-aston-villa-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿斯顿维拉如此迫切地想要劫持约翰·曼赞比（ Johan Manzambi ）从弗莱堡（ Freiburg ）到纽卡斯尔（ Newcastle ）的夏季搬迁计划是有原因的。这位身材高大、快速、棘手、聪明、完美平衡的21岁瑞士进攻型中场球员看起来物有所值" data-title="Manzambi maintains Aston Villa progress with win to seal dismal week for Newcastle" data-date="10-18 02:38" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-18 02:38</span>
          <span class="news-item-title">曼赞比保持阿斯顿维拉的进步，赢得纽卡斯尔令人沮丧的一周</span>
          <span class="news-item-title-en">Manzambi maintains Aston Villa progress with win to seal dismal week for Newcastle</span>
          <span class="news-value-point">💡 阿斯顿维拉如此迫切地想要劫持约翰·曼赞比（ Johan Manzambi ）从弗莱堡（ Freiburg ）到纽卡斯尔（ Newcastle ）…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/10/premier-league-top-scorers-2026-27-race-for-golden-boot" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="找出哪位英国顶尖射手正在向进球排行榜射击。继续阅读……" data-title="Premier League top scorers 2026-27: who is leading race for the golden boot?" data-date="10-18 02:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-18 02:30</span>
          <span class="news-item-title">2026-27赛季英超联赛最佳射手：谁是金靴赛的领跑者？</span>
          <span class="news-item-title-en">Premier League top scorers 2026-27: who is leading race for the golden boot?</span>
          <span class="news-value-point">💡 找出哪位英国顶尖射手正在向进球排行榜射击</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/17/manchester-city-v-ipswich-brentford-v-liverpool-and-more-football-clockwatch-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="富勒姆赢得了本赛季对阵惨淡的船体的第一场胜利，而利物浦则从后面击败了九人布伦特福德安迪·亨特来自希尔·狄金森的比赛报告在这里，你可以在下面找到它。切尔西已经从国际比赛回来了" data-title="Manchester City 3-2 Ipswich, Brentford 1-2 Liverpool, and more: Football clockwatch - as it happened" data-date="10-18 00:43" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-18 00:43</span>
          <span class="news-item-title">曼城3-2伊普斯维奇，布伦特福德1-2利物浦等：足球钟表-如其所愿</span>
          <span class="news-item-title-en">Manchester City 3-2 Ipswich, Brentford 1-2 Liverpool, and more: Football clockwatch - as it happened</span>
          <span class="news-value-point">💡 富勒姆赢得了本赛季对阵惨淡的船体的第一场胜利，而利物浦则从后面击败了九人布伦特福德安迪·亨特来自希尔·狄金森的比赛报告在这里，你可以在下面找到它</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/17/brentford-liverpool-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="如果利物浦的飞溅前锋最终将此记住为他们的运气转向的那一天，那么他们将欠Yehor Yarmolyuk一大笔感激之情。这是一场前后都非常清晰的比赛。安东尼·伊拉奥拉（ Andoni Iraola ）希望能在" data-title="Isak completes Liverpool’s comeback win as Brentford finish with nine" data-date="10-18 00:21" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-18 00:21</span>
          <span class="news-item-title">伊萨克完成了利物浦的复出胜利，布伦特福德以9分结束</span>
          <span class="news-item-title-en">Isak completes Liverpool’s comeback win as Brentford finish with nine</span>
          <span class="news-value-point">💡 如果利物浦的飞溅前锋最终将此记住为他们的运气转向的那一天，那么他们将欠Yehor Yarmolyuk一大笔感激之情</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/17/manchester-city-ipswich-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在曼城的有罪判决中，除了高薪律师和充气水果行业外，几乎没有赢家。粉丝们遭受了痛苦，被迫质疑他们被告知的一切，同时被贴上“作弊”的标签，但他们" data-title="Haaland helps Maresca achieve record start as Manchester City defeat Ipswich" data-date="10-18 00:08" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-18 00:08</span>
          <span class="news-item-title">哈兰德帮助马雷斯卡取得创纪录的开局，曼城击败伊普斯维奇</span>
          <span class="news-item-title-en">Haaland helps Maresca achieve record start as Manchester City defeat Ipswich</span>
          <span class="news-value-point">💡 在曼城的有罪判决中，除了高薪律师和充气水果行业外，几乎没有赢家</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6rryqq00yp4o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="守门员埃米利亚诺·马丁内斯（ Emiliano Martinez ）被送往医院，因为切尔西周六在埃弗顿（ Everton ）以2比0获胜，这意味着他们在九个月内获得了第一张干净的" data-title="Chelsea&#39;s Martinez taken to hospital for &#39;precautionary tests&#39;" data-date="10-18 00:02" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-18 00:02</span>
          <span class="news-item-title">切尔西的马丁内斯被送往医院进行“预防性测试”</span>
          <span class="news-item-title-en">Chelsea's Martinez taken to hospital for 'precautionary tests'</span>
          <span class="news-value-point">💡 守门员埃米利亚诺·马丁内斯（ Emiliano Martinez ）被送往医院，因为切尔西周六在埃弗顿（ Everton ）以2比0获胜，这意味…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/17/everton-v-chelsea-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="佩德罗·内托（ Pedro Neto ）的进球在下半场结束，为切尔西赢得了埃弗顿-埃弗顿（ Everton ）开球的罕见胜利，并持续了很长时间。马丁内斯声称平底锅。在开球之前，每个人都会膝盖。这是英超联赛两周的第一周" data-title="Everton 0-2 Chelsea: Premier League – as it happened" data-date="10-17 22:13" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-17 22:13</span>
          <span class="news-item-title">埃弗顿0-2切尔西：英超联赛–事实就是这样</span>
          <span class="news-item-title-en">Everton 0-2 Chelsea: Premier League – as it happened</span>
          <span class="news-value-point">💡 佩德罗·内托（ Pedro Neto ）的进球在下半场结束，为切尔西赢得了埃弗顿-埃弗顿（ Everton ）开球的罕见胜利，并持续了很长时间</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c674pzzlz8zlo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="佩德罗·内托在切尔西的两个下半场进球确保了周六在埃弗顿的重要客场胜利。" data-title="Neto stars but who was subdued? - player ratings for Everton v Chelsea" data-date="10-17 21:39" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-17 21:39</span>
          <span class="news-item-title">内托球星，但谁被征服了？ -埃弗顿对切尔西的球员评分</span>
          <span class="news-item-title-en">Neto stars but who was subdued? - player ratings for Everton v Chelsea</span>
          <span class="news-value-point">💡 佩德罗·内托在切尔西的两个下半场进球确保了周六在埃弗顿的重要客场胜利</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/014/502.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 18 日消息，据易车报道，长安猎手 K70 皮卡将在 10 月 23 日上市，新车采用家族化外观，搭载 2.0T 增程系统，拥有 33 英寸越野 AT 胎。从外观来看，长安猎手 K70 前脸延续家族设计，配备黑色的无边界式格栅，两侧是 T 型大灯，前包围预留绞盘安装位，支持用户按需选装，营造越野气场。该车还将搭配 33 英寸越野轮胎，配套 17 英寸轮圈。同时，该车的货箱支持分段开启，后包围拥有拖车方口，拥有合法拖拽资质。车辆离地间隙 245mm，接近角 38 度，离去角 28 度。IT之家注意到，该车将搭载增程动力系统，搭载 2.0T 发动机，最大功率 140kW，前后电机最大功率分别为 110kW、150kW，综合功率 260kW，综合扭矩 550 N·m，提供低速挡" data-title="长安猎手 K70 皮卡 10 月 23 日上市：2.0T 增程，配备越野 AT 轮胎" data-date="10-18 14:42" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-18 14:42</span>
          <span class="news-item-title">长安猎手 K70 皮卡 10 月 23 日上市：2.0T 增程，配备越野 AT 轮胎</span>
          <span class="news-value-point">💡 IT之家 10 月 18 日消息，据易车报道，长安猎手 K70 皮卡将在 10 月 23 日上市，新车采用家族化外观，搭载 2.0T 增程系统，…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/501.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 18 日消息，梅赛德斯-AMG 宣布旗下 GLC 53 4MATIC+ 车型将于 10 月 29 日上市，该车主要换用动力更强的 3.0T 直列六缸涡轮增压发动机，最大功率为 455 马力，峰值扭矩达到 600 牛 · 米。据官方介绍，该车配备的全新 3.0T 直列六缸发动机带有 7.5kW 的电动辅助增压器和传统废气涡轮增压器，最大功率为 455 马力，峰值扭矩达到 600 牛 · 米，在超增压模式下，可以在 10 秒时间内把峰值扭矩提升到 640 牛 · 米。ISG 整合式启动电机可以提供 17kW/205 牛 · 米的动力辅助，可以提升车辆的油门响应性能，同时有利于降低油耗。与发动机匹配的是 9 挡手自一体变速箱。底盘方面，新车将搭载 AMG 专属动态操控系统、AM" data-title="梅赛德斯-AMG GLC 53 4MATIC+ 车型将于 10 月 29 日上市，换用 3.0T 直列六缸涡轮增压发动机" data-date="10-18 14:34" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-18 14:34</span>
          <span class="news-item-title">梅赛德斯-AMG GLC 53 4MATIC+ 车型将于 10 月 29 日上市，换用 3.0T 直列六缸涡轮增压发动机</span>
          <span class="news-value-point">💡 IT之家 10 月 18 日消息，梅赛德斯-AMG 宣布旗下 GLC 53 4MATIC+ 车型将于 10 月 29 日上市，该车主要换用动力更…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/500.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 18 日消息，天文学家借助詹姆斯・韦布空间望远镜（JWST）获取的数据，揭开了一颗奇特、酷热行星的部分大气奥秘，这颗行星质地如同棉花糖一般。这颗被韦布红外望远镜持续观测的系外行星名为 WASP-17b，距离地球约 1300 光年。其质量约为木星的 0.8 倍，但直径却大约是木星的两倍，属于“超蓬松行星”，质地堪比棉花糖。WASP-17b 极其靠近母恒星，不到 4 个地球日就能完成一圈公转；如此近的距离，也让这颗“热木星”温度急剧飙升。这颗系外行星环境极端，大气结构与众不同也就不足为奇。科研团队采用一种名为透射串（transmission strings）的新技术，绘制出 WASP-17b 大气轮廓。研究发现，这颗行星的大气呈环状，环上还有多处凸起的“宝石状”结构。团队成员" data-title="1300 光年外的“棉花糖”系外行星，大气带有凸起的“宝石”结构" data-date="10-18 14:32" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-18 14:32</span>
          <span class="news-item-title">1300 光年外的“棉花糖”系外行星，大气带有凸起的“宝石”结构</span>
          <span class="news-value-point">💡 IT之家 10 月 18 日消息，天文学家借助詹姆斯・韦布空间望远镜（JWST）获取的数据，揭开了一颗奇特、酷热行星的部分大气奥秘，这颗行星质地…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/495.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 18 日消息，荣耀官方今日正持续预热 WIN 2 系列手机，刚刚又介绍了新机的防水性能：荣耀 WIN 2 系列支持整机 IP68+IP69+IP69K 级防尘防水，内置双风扇支持 IPX8+IPX9 级防水。据介绍，荣耀 WIN 2 系列将搭载双子星涡轮散热风扇，将成为行业首款搭载双风扇散热架构的手机。不过爆料显示，荣耀 WIN 2 的中杯会采用单风扇设计，大杯才是双风扇方案。另外，新机还将搭载荣耀鸿燕通信，配备全新自研射频增强芯片 HONOR C3，可强化复杂网络环境通信性能；搭载全新电竞 WIN 键，支持 3 档可调震动、3 档响应灵敏度，搭配 5 种响应光效与无极按键透明度；支持游戏内自由映射键位。海报显示，电竞 WIN 键仅荣耀 WIN2 手机支持。IT之家整理新" data-title="荣耀 WIN 2 系列手机防水性能公布，内置双风扇支持 IPX8+IPX9 级防水" data-date="10-18 14:31" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-18 14:31</span>
          <span class="news-item-title">荣耀 WIN 2 系列手机防水性能公布，内置双风扇支持 IPX8+IPX9 级防水</span>
          <span class="news-value-point">💡 IT之家 10 月 18 日消息，荣耀官方今日正持续预热 WIN 2 系列手机，刚刚又介绍了新机的防水性能：荣耀 WIN 2 系列支持整机 IP…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-18/10716616.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京10月18日电 (记者 周昕 李纯 马帅莎)2026世界传统医药大会“传统医学与现代医学融合论坛—呼吸与传染性疾病专题”18日在北京举行。首都医科大学附属北京中医医院院长刘清泉在接受媒体采访时表示，要以“阵法”思维，融合多元的传统医学智慧，构建全面有效的抗微生物药物耐药性(AMR)防控体系。" data-title="北京中医医院院长刘清泉：以多元手段协同共抗耐药" data-date="10-18 14:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 14:28</span>
          <span class="news-item-title">北京中医医院院长刘清泉：以多元手段协同共抗耐药</span>
          <span class="news-value-point">💡 中新网北京10月18日电 (记者 周昕 李纯 马帅莎)2026世界传统医药大会“传统医学与现代医学融合论坛—呼吸与传染性疾病专题”18日在北京举…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/493.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 18 日消息，维沃移动通信有限公司 iQOO Neo 产品经理罗佳慧发文，谈及了这次 iQOO Neo12 的外观设计。她透露，新机拥有一款与中国美术学院联手共同打造全新配色。作为中国高等艺术教育的奠基者，中国美术学院被誉为“中国现代艺术教育的摇篮”，在艺术与设计领域拥有深厚实力。时至今日，中国美院兼顾艺术底蕴与创新表达，持续推动中国审美的当代表达...这一次，我们将艺术学府的美学造诣，与 Neo 对未来科技的想象相融合，以中国审美，探索设计的新可能！罗佳慧还宣布，新机“周一见”。预计届时会公布外观配色等信息。IT之家整理 iQOO Neo12 手机已公布 / 曝光配置如下：性能：第五代骁龙 8 至尊版处理器 | 自研电竞芯片 Q3 | 全新一代 Monster 超核引擎" data-title="iQOO Neo12 官宣“周一见”，新机拥有与中国美术学院联手打造的全新配色" data-date="10-18 14:26" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-18 14:26</span>
          <span class="news-item-title">iQOO Neo12 官宣“周一见”，新机拥有与中国美术学院联手打造的全新配色</span>
          <span class="news-value-point">💡 IT之家 10 月 18 日消息，维沃移动通信有限公司 iQOO Neo 产品经理罗佳慧发文，谈及了这次 iQOO Neo12 的外观设计</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-18/10716620.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京10月18日电 “紫云承晖——李俊花鸟画作品展”日前京举行。展览展出了中国美术家协会会员、中国书法家协会会员、江苏省花鸟画研究会副会长李俊的近百幅花鸟画佳作。" data-title="近百佳作呈现当代花鸟画紫藤系列新意境" data-date="10-18 14:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 14:22</span>
          <span class="news-item-title">近百佳作呈现当代花鸟画紫藤系列新意境</span>
          <span class="news-value-point">💡 中新网北京10月18日电 “紫云承晖——李俊花鸟画作品展”日前京举行</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/17/world/europe/france-protest-riots-marseille.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="法国几个城市爆发了骚乱，成千上万的人举行了和平游行，抗议生活费用上涨和学校条件恶劣。" data-title="Unrest Mars Day of Protest in France, as Student Movement Turns National" data-date="10-18 14:22" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-18 14:22</span>
          <span class="news-item-title">骚乱法国火星抗议日，学生运动转向全国</span>
          <span class="news-item-title-en">Unrest Mars Day of Protest in France, as Student Movement Turns National</span>
          <span class="news-value-point">💡 法国几个城市爆发了骚乱，成千上万的人举行了和平游行，抗议生活费用上涨和学校条件恶劣</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/490.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 18 日消息，华为智慧生活 App 显示，鸿蒙智联基础服务迎来了 17.0.4.335 版本升级。此次版本升级又一次超前曝光了华为新品的存在。更新说明显示，鸿蒙智联基础服务将新增支持路由 X2 Pro 接入。这表明华为接下来将推出一款路由新品（上市时间待定），预计其定位在 X3 Pro 和 X1 Pro 之间。作为参考，华为路由 X 系列定位“创新旗舰”，目前已推出 X1 / X1 Pro 和 X3 Pro 日照金山三款产品。遗憾的是，虽然此次鸿蒙智联基础服务升级预告了新品的存在，但华为智慧生活 App 却并未像往常一样公开新品配对步骤（华为此前的 IoT 新品常在智慧生活 App 提前“剧透”，并曝光外观和部分功能信息）。IT之家也将持续关注新品信息，并在第一时间带来产" data-title="华为路由 X2 Pro 官宣接入智慧生活 App，新品上市时间待定" data-date="10-18 14:18" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-18 14:18</span>
          <span class="news-item-title">华为路由 X2 Pro 官宣接入智慧生活 App，新品上市时间待定</span>
          <span class="news-value-point">💡 IT之家 10 月 18 日消息，华为智慧生活 App 显示，鸿蒙智联基础服务迎来了 17.0.4.335 版本升级</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/014/489.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 18 日消息，在今年 9 月 7 日的 HarmonyOS 7 | HUAWEI Mate XT 2 及全场景新品发布会上，华为终端 BG CEO 何刚宣布，华为鸿蒙星河互联升级，支持连接苹果 AirPods 无线耳机。IT之家注意到，华为官网现公布了鸿蒙星河互联 AirPods 适配机型。据介绍，当前支持与 AirPods 4、AirPods Pro 3、AirPods 3、AirPods Pro 2、AirPods 2、AirPods Pro 1、AirPods 1、AirPods Max、AirPods 5 等主流型号 AirPods 进行互联。华为手机升级 HarmonyOS 7.0 及以上版本与 AirPods 连接后，可实现 AirPods 连接提醒及电量显示" data-title="华为鸿蒙星河互联 AirPods 适配型号公布，覆盖初代至 Max 等主流机型" data-date="10-18 14:05" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-18 14:05</span>
          <span class="news-item-title">华为鸿蒙星河互联 AirPods 适配型号公布，覆盖初代至 Max 等主流机型</span>
          <span class="news-value-point">💡 IT之家 10 月 18 日消息，在今年 9 月 7 日的 HarmonyOS 7 | HUAWEI Mate XT 2 及全场景新品发布会上，…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-18/10716604.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社兰州10月18日电 题：“中国小杂粮之乡”甘肃会宁的“康养密码”" data-title="（走进中国乡村）“中国小杂粮之乡”甘肃会宁的“康养密码”" data-date="10-18 13:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 13:30</span>
          <span class="news-item-title">（走进中国乡村）“中国小杂粮之乡”甘肃会宁的“康养密码”</span>
          <span class="news-value-point">💡 中新社兰州10月18日电 题：“中国小杂粮之乡”甘肃会宁的“康养密码”</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cq8ez1wny72xo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="法国全国多座城市爆发骚乱，超过50万人参加了反对生活成本上涨的抗议活动。" data-title="法国抗议爆发暴力冲突、抢劫、建筑物起火，逾千人被捕" data-date="10-18 13:12" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-18 13:12</span>
          <span class="news-item-title">法国抗议爆发暴力冲突、抢劫、建筑物起火，逾千人被捕</span>
          <span class="news-value-point">💡 法国全国多座城市爆发骚乱，超过50万人参加了反对生活成本上涨的抗议活动</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-18/10716602.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="央广网北京10月18日消息(记者刘保奇)2024年4月16日，中部某市行政服务中心公共资源交易中心的开标现场，气氛紧张而有序。然而，该市一家混凝土公司负责人夏禹坐在人群中，手里攥着三份投标文件，脸上却没有丝毫忐忑，反而透着一种胸有成竹的平静。" data-title="一条微信打开招标项目“内定”之门" data-date="10-18 13:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 13:09</span>
          <span class="news-item-title">一条微信打开招标项目“内定”之门</span>
          <span class="news-value-point">💡 央广网北京10月18日消息(记者刘保奇)2024年4月16日，中部某市行政服务中心公共资源交易中心的开标现场，气氛紧张而有序</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-18/10716600.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="今天，黑龙江大兴安岭多地气象部门发布暴雪、道路结冰预警。" data-title="黑龙江大兴安岭多地气象部门发布暴雪、道路结冰预警" data-date="10-18 12:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 12:56</span>
          <span class="news-item-title">黑龙江大兴安岭多地气象部门发布暴雪、道路结冰预警</span>
          <span class="news-value-point">💡 今天，黑龙江大兴安岭多地气象部门发布暴雪、道路结冰预警</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-18/10716589.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中国新闻周刊记者：李明子" data-title="5A的金字招牌，过气了吗？" data-date="10-18 11:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-18 11:57</span>
          <span class="news-item-title">5A的金字招牌，过气了吗？</span>
          <span class="news-value-point">💡 中国新闻周刊记者：李明子</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-18 14:42（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
