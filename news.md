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
      <span>2026-11-08 16:11 抓取更新</span>
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
        <span class="channel-count">56</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('shizheng', this)">
        <span>🏛️ 时政与国际</span>
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('keji', this)">
        <span>🤖 AI模型 & 芯片算力</span>
        <span class="channel-count">11</span>
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
  <div class="ov-item"><span class="ov-num">56</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×17 · IT之家×9</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/11-08/10728361.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="编者按" data-title="红色中华报：跨越95年的回响｜一张布告 人民江山" data-date="11-08 15:40" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 11-08 15:40</span>
      </div>
      <h2 class="hero-featured-title">红色中华报：跨越95年的回响｜一张布告 人民江山</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/023/911.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 8 日消息，11 月 6 日，国家发展改革委举行奋进“十五五”系列新闻发布会，介绍筑牢安全底座有关情况。国家能源局发展规划司副司长葛炬在发布会上表示，“十五五”时期，在算力等新兴产业带动下，我国用电需求仍将刚性增长，预计年均增量将达到 6000 亿度左右，相当于每年新增 3 个上海市的用电量。为做好电力保供，我们建立了电力供应充裕度预警机制，提出 2030 年电力供应充裕度大于 1.1，也就是在用电负荷最高峰时刻，仍然有 10% 的保供能力余量，确保关键时刻能够“顶住峰、兜住底”。具体来说，将从源网荷储协同发力，加强电力保供能力建设。IT之家获悉，今年迎峰度夏期间，全国用电负荷 4 次刷新历史极值，最大值比去年增加 5000 万千瓦，华北、东北、华东等 6 个区域电网用电" data-title="国家能源局：在算力等新兴产业带动下，我国用电需求仍将刚性增长、预计相当于每年新增 3 个上海市的用电量" data-date="11-08 15:34" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">国家能源局：在算力等新兴产业带动下，我国用电需求仍将刚性增长、预计相当于每年新增 3 个上海市的用电量</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/boxing/news/12040/13609513/ramla-ali-and-skye-nicolson-could-be-on-a-collision-course-if-they-win-their-world-title-fights-in-texas" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="如果Ramla Ali和Skye Nicolson都赢得冠军争夺战，他们可能会在明年初的统一比赛中相遇，他们将在周一凌晨在天空体育上直播。" data-title="Ali and Nicolson on a collision course?" data-date="11-08 15:00" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">Ali and Nicolson on a collision course?</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/023/918.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 8 日消息，比亚迪旗下超豪华行政旗舰轿车 —— 仰望鼎曜于北京时间 7 日晚间迎来全球首秀，IT之家已在现场进行详细报道。随后，仰望汽车通过小程序公布了仰望鼎曜“山河鼎韵”限量版车型的价格：208 万元。该车定金为 30 万元。小程序页面显示，新车拥有“棕岩白玉”主题的专属内外饰，不排除后续开放更多个性化定制的可能。仰望鼎曜车身尺寸为 5600×2030×1590mm，轴距 3500mm；采用礼宾级中轴对开门设计，前门最大开启角 80°，后门最大开启角 90°。仰望鼎曜“山河鼎韵”限量版拥有专属外观内饰及高定配置，包含琥珀金双腰线、限量版专属印记、专属云纹图案、出风口宝石 · 和田玉、金色扬声器面罩、车门内置芳纶纤维等。相关阅读：《比亚迪超豪华行政旗舰轿车登场！仰望鼎曜行" data-title="208 万元！比亚迪仰望鼎曜“山河鼎韵”限量版车型价格揭晓" data-date="11-08 16:10" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">208 万元！比亚迪仰望鼎曜“山河鼎韵”限量版车型价格揭晓</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-08/10728361.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="编者按" data-title="红色中华报：跨越95年的回响｜一张布告 人民江山" data-date="11-08 15:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 15:40</span>
          <span class="news-item-title">红色中华报：跨越95年的回响｜一张布告 人民江山</span>
          <span class="news-value-point">💡 编者按</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-08/10728356.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="河北邱县政务服务中心“事办不成找我”窗口——" data-title="以更优服务解决群众急难愁盼（贯彻五中全会精神一线见闻）" data-date="11-08 15:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 15:23</span>
          <span class="news-item-title">以更优服务解决群众急难愁盼（贯彻五中全会精神一线见闻）</span>
          <span class="news-value-point">💡 河北邱县政务服务中心“事办不成找我”窗口——</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-08/10728352.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京11月7日电#8195;综述｜从亲历到读懂：国际媒体人士共话真实中国" data-title="综述｜从亲历到读懂：国际媒体人士共话真实中国" data-date="11-08 15:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 15:01</span>
          <span class="news-item-title">综述｜从亲历到读懂：国际媒体人士共话真实中国</span>
          <span class="news-value-point">💡 新华社北京11月7日电#8195;综述｜从亲历到读懂：国际媒体人士共话真实中国</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-08/10728351.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="央视网消息：2026年11月9日是第35个全国消防日，11月也是全国消防宣传月。11月6日，国务院安委会办公室、应急管理部、国家消防救援局在北京启动了2026年全国消防宣传月活动。" data-title="全国消防日 | 火灾调查行家说：冷静判断、科学逃生是保命根本" data-date="11-08 14:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 14:52</span>
          <span class="news-item-title">全国消防日 | 火灾调查行家说：冷静判断、科学逃生是保命根本</span>
          <span class="news-value-point">💡 央视网消息：2026年11月9日是第35个全国消防日，11月也是全国消防宣传月</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-08/10728308.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月8日电 综合消息：以色列总统赫尔佐格当地时间7日宣布，将组建下一届政府的授权交给正直党领导人、前国防军总参谋长加迪·埃森科特，正式授权仪式定于8日下午举行。" data-title="以色列总统决定授权正直党领导人埃森科特组建新政府" data-date="11-08 13:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 13:32</span>
          <span class="news-item-title">以色列总统决定授权正直党领导人埃森科特组建新政府</span>
          <span class="news-value-point">💡 中新社北京11月8日电 综合消息：以色列总统赫尔佐格当地时间7日宣布，将组建下一届政府的授权交给正直党领导人、前国防军总参谋长加迪·埃森科特，正…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-08/10728275.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月8日电 波哥大消息：据哥伦比亚军方通报，该国北部玻利瓦尔省一处军事基地当地时间7日遭携带爆炸装置的无人机袭击，造成3名军人死亡、8名军人重伤，另有多人受不同程度伤害。" data-title="哥伦比亚一军事基地遇袭 致3死8伤" data-date="11-08 11:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 11:10</span>
          <span class="news-item-title">哥伦比亚一军事基地遇袭 致3死8伤</span>
          <span class="news-value-point">💡 中新社北京11月8日电 波哥大消息：据哥伦比亚军方通报，该国北部玻利瓦尔省一处军事基地当地时间7日遭携带爆炸装置的无人机袭击，造成3名军人死亡、…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-08/10728276.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月8日电 华沙消息：波兰克拉科夫当地时间7日发生一起枪击事件，已造成6人死亡、16人受伤，伤者包括2名警察。枪手被警方打伤后被捕，其家中另外发现3具遗体。" data-title="波兰克拉科夫枪击事件已致6死 枪手家中另发现3具遗体" data-date="11-08 11:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 11:01</span>
          <span class="news-item-title">波兰克拉科夫枪击事件已致6死 枪手家中另发现3具遗体</span>
          <span class="news-value-point">💡 中新社北京11月8日电 华沙消息：波兰克拉科夫当地时间7日发生一起枪击事件，已造成6人死亡、16人受伤，伤者包括2名警察</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-08/10728269.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社东京11月7日电(记者李子越#8195;陈泽安)日本共同社7日援引相关人士消息称，日本政府正考虑在拟于年底修订的《国家防卫战略》中，明确写入强化“持续作战能力”的内容。相关动向在日本政府内外引发担忧。" data-title="日媒：日本新版防卫战略或强化“持续作战能力”" data-date="11-08 10:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 10:49</span>
          <span class="news-item-title">日媒：日本新版防卫战略或强化“持续作战能力”</span>
          <span class="news-value-point">💡 新华社东京11月7日电(记者李子越#8195;陈泽安)日本共同社7日援引相关人士消息称，日本政府正考虑在拟于年底修订的《国家防卫战略》中，明确写…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-08/10728268.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="11月7日，原乌鲁木齐军区副司令员王扶之走完一个多世纪的人生征程，病逝于辽宁大连，享年104岁。自1955年我军首次授衔，历经十年补授、晋升，开国将军至此已全部走进历史。" data-title="最后一位开国将军王扶之逝世" data-date="11-08 10:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 10:43</span>
          <span class="news-item-title">最后一位开国将军王扶之逝世</span>
          <span class="news-value-point">💡 11月7日，原乌鲁木齐军区副司令员王扶之走完一个多世纪的人生征程，病逝于辽宁大连，享年104岁</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-08/10728243.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月8日电 (记者 孙自法)施普林格·自然旗下专业学术期刊《通讯-地球与环境》最新发表一篇环境研究论文称，研究人员通过分析卫星监测数据发现，2002至2022年间，在太平洋垃圾带内，部分太平洋海域的颜色似乎发生了变化，一些区域明显变得更蓝、更绿。究其原因，可能是海水中微塑料浓度增加所致。" data-title="太平洋部分海域为何更蓝更绿？最新研究称或是微塑料浓度增加所致" data-date="11-08 10:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 10:23</span>
          <span class="news-item-title">太平洋部分海域为何更蓝更绿？最新研究称或是微塑料浓度增加所致</span>
          <span class="news-value-point">💡 中新网北京11月8日电 (记者 孙自法)施普林格·自然旗下专业学术期刊《通讯-地球与环境》最新发表一篇环境研究论文称，研究人员通过分析卫星监测数…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-08/10728261.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月8日电 综合美媒报道，美国总统特朗普当地时间7日在其社交平台“真实社交”(Truth Social)上发文说，他已邀请美国终极格斗冠军赛总裁达纳·怀特担任白宫新闻秘书一职。" data-title="特朗普称邀请达纳·怀特担任白宫新闻秘书" data-date="11-08 10:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 10:15</span>
          <span class="news-item-title">特朗普称邀请达纳·怀特担任白宫新闻秘书</span>
          <span class="news-value-point">💡 中新网11月8日电 综合美媒报道，美国总统特朗普当地时间7日在其社交平台“真实社交”(Truth Social)上发文说，他已邀请美国终极格斗冠…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/07/world/middleeast/israel-eisenkot-government.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="前军事首领加迪·艾森科特（ Gadi Eisenkot ）希望在选举无结果后通过组建联盟来接替本雅明·内塔尼亚胡（ Benjamin Netanyahu ）担任总理。" data-title="Eisenkot, Netanyahu Rival and Opposition Leader, Tapped to Try to Form Government" data-date="11-08 07:03" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-08 07:03</span>
          <span class="news-item-title">内塔尼亚胡的竞争对手和反对党领袖艾森科特试图组建政府</span>
          <span class="news-item-title-en">Eisenkot, Netanyahu Rival and Opposition Leader, Tapped to Try to Form Government</span>
          <span class="news-value-point">💡 前军事首领加迪·艾森科特（ Gadi Eisenkot ）希望在选举无结果后通过组建联盟来接替本雅明·内塔尼亚胡（ Benjamin Netan…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/07/world/middleeast/eisenkot-israel-new-government.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="加迪·艾森科特（ Gadi Eisenkot ）有机会组建新政府，取代本雅明·内塔尼亚胡（ Benjamin Netanyahu ）担任总理。但障碍是巨大的。" data-title="Eisenkot Seeks to Oust Netanyahu as Prime Minister. Here’s How." data-date="11-08 05:52" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-08 05:52</span>
          <span class="news-item-title">Eisenkot寻求将内塔尼亚胡赶下台担任总理。具体操作方法如下。</span>
          <span class="news-item-title-en">Eisenkot Seeks to Oust Netanyahu as Prime Minister. Here’s How.</span>
          <span class="news-value-point">💡 加迪·艾森科特（ Gadi Eisenkot ）有机会组建新政府，取代本雅明·内塔尼亚胡（ Benjamin Netanyahu ）担任总理</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/07/upshot/senators-midterm-elections-age.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="即将上任的参议员平均比即将离任的参议员年轻近15岁。但房间的整体年龄变化不大。" data-title="After the Midterms, the Average Age in the Senate Falls to 63" data-date="11-08 04:17" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-08 04:17</span>
          <span class="news-item-title">中期选举后，参议院的平均年龄降至63岁</span>
          <span class="news-item-title-en">After the Midterms, the Average Age in the Senate Falls to 63</span>
          <span class="news-value-point">💡 即将上任的参议员平均比即将离任的参议员年轻近15岁</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/07/us/politics/stephen-miller-midterm-elections.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="总统的新参谋长已经表明了他打算推进许多选民拒绝的议程。" data-title="For Stephen Miller, Election Defeat Is No Reason to Back Down on Immigration Crackdown" data-date="11-08 02:29" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-08 02:29</span>
          <span class="news-item-title">对于斯蒂芬·米勒（ Stephen Miller ）来说，选举失败并不是放弃移民镇压的理由</span>
          <span class="news-item-title-en">For Stephen Miller, Election Defeat Is No Reason to Back Down on Immigration Crackdown</span>
          <span class="news-value-point">💡 总统的新参谋长已经表明了他打算推进许多选民拒绝的议程</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">11 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/023/911.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 8 日消息，11 月 6 日，国家发展改革委举行奋进“十五五”系列新闻发布会，介绍筑牢安全底座有关情况。国家能源局发展规划司副司长葛炬在发布会上表示，“十五五”时期，在算力等新兴产业带动下，我国用电需求仍将刚性增长，预计年均增量将达到 6000 亿度左右，相当于每年新增 3 个上海市的用电量。为做好电力保供，我们建立了电力供应充裕度预警机制，提出 2030 年电力供应充裕度大于 1.1，也就是在用电负荷最高峰时刻，仍然有 10% 的保供能力余量，确保关键时刻能够“顶住峰、兜住底”。具体来说，将从源网荷储协同发力，加强电力保供能力建设。IT之家获悉，今年迎峰度夏期间，全国用电负荷 4 次刷新历史极值，最大值比去年增加 5000 万千瓦，华北、东北、华东等 6 个区域电网用电" data-title="国家能源局：在算力等新兴产业带动下，我国用电需求仍将刚性增长、预计相当于每年新增 3 个上海市的用电量" data-date="11-08 15:34" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-08 15:34</span>
          <span class="news-item-title">国家能源局：在算力等新兴产业带动下，我国用电需求仍将刚性增长、预计相当于每年新增 3 个上海市的用电量</span>
          <span class="news-value-point">💡 IT之家 11 月 8 日消息，11 月 6 日，国家发展改革委举行奋进“十五五”系列新闻发布会，介绍筑牢安全底座有关情况</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/this-rtx-5060-gaming-pc-costs-less-than-the-steam-machine-grab-the-ibuypower-slate-prebuilt-pc-with-massive-usd500-discount" target="_blank" rel="noopener" data-cat="keji" data-summary="百思买iBUYPOWER Slate降价500 $ ，这款RTX 5060驱动的游戏台式机降至899 $ ，配备Ryzen 5处理器、16GB DDR5内存和1TB SSD" data-title="This RTX 5060 gaming PC costs less than the Steam Machine — grab the iBuyPower Slate prebuilt PC with massive $500 discount" data-date="11-08 05:27" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-08 05:27</span>
          <span class="news-item-title">这款RTX 5060游戏PC的成本低于Steam Machine —以500 $的大幅折扣购买iBuyPower Slate预制PC</span>
          <span class="news-item-title-en">This RTX 5060 gaming PC costs less than the Steam Machine — grab the iBuyPower Slate prebuilt PC with massive $500 discount</span>
          <span class="news-value-point">💡 百思买iBUYPOWER Slate降价500 $ ，这款RTX 5060驱动的游戏台式机降至899 $ ，配备Ryzen 5处理器、16GB …</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/07/chinese-exec-was-recruited-to-spy-on-nvidia-ceo-according-to-us-intelligence-memo/" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道，今年早些时候分发的一份备忘录声称，中国国家安全部聘请了一名女性技术高管来监视英伟达的首席执行官。" data-title="Megaspeed exec was recruited to spy on Nvidia CEO, according to US intelligence memo" data-date="11-08 05:17" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-08 05:17</span>
          <span class="news-item-title">根据美国情报备忘录， Megaspeed高管被招募来监视Nvidia首席执行官</span>
          <span class="news-item-title-en">Megaspeed exec was recruited to spy on Nvidia CEO, according to US intelligence memo</span>
          <span class="news-value-point">💡 据报道，今年早些时候分发的一份备忘录声称，中国国家安全部聘请了一名女性技术高管来监视英伟达的首席执行官</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1029483/nvidia-ai-chips-china-blacklist-government" target="_blank" rel="noopener" data-cat="keji" data-summary="有人担心，在审查获准处理该公司H200人工智能芯片的中国公司时，商务部和英伟达都没有进行尽职调查。据《纽约时报》报道， New Matrix在" data-title="The US let Nvidia sell chips to an empty office in China" data-date="11-07 23:43" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-07 23:43</span>
          <span class="news-item-title">美国允许英伟达向中国一间空置办公室出售芯片</span>
          <span class="news-item-title-en">The US let Nvidia sell chips to an empty office in China</span>
          <span class="news-value-point">💡 有人担心，在审查获准处理该公司H200人工智能芯片的中国公司时，商务部和英伟达都没有进行尽职调查</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/podcast/1029038/ai-cybersecurity-hackers-data-breach-dark-age-alex-stamos" target="_blank" rel="noopener" data-cat="keji" data-summary="今天，我正在与Cognition首席安全官兼长期网络安全专家Alex Stamos谈论网络安全目前的混乱局面。本集是关于现实生活中的人工智能的特别系列的一部分。我一直很喜欢聊天" data-title="AI broke the cybersecurity world. What’s next?" data-date="11-07 23:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-07 23:00</span>
          <span class="news-item-title">人工智能打破了网络安全的世界。下一步是什么？</span>
          <span class="news-item-title-en">AI broke the cybersecurity world. What’s next?</span>
          <span class="news-value-point">💡 今天，我正在与Cognition首席安全官兼长期网络安全专家Alex Stamos谈论网络安全目前的混乱局面</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/023/824.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 7 日消息，美国联邦治安法官谢文辉（Alex Tse）裁定，Anthropic 必须继续应对 Claude Max 套餐使用额度涉嫌误导消费者的主要指控。据 Courthouse News 报道，谢文辉周五驳回了案件中的其他几项诉求。Anthropic 宣传称，月费 100 美元（IT之家注：现汇率约合 668.6 元人民币）和 200 美元（现汇率约合 1,337 元人民币）的 Max 套餐，使用额度分别是 Pro 套餐的 5 倍和 20 倍。但今年 6 月提起诉讼的消费者指控，如果按整周计算，实际额度远远达不到宣传中的倍数。两名原告卡尔 · 卡恩和所罗门 · 史密斯计算发现，以 Claude 的一款模型为例，200 美元（现汇率约合 1,337 元人民币）套餐的每周额" data-title="Claude Max 订阅套餐使用额度被指“虚标”，Anthropic 辩词未获法官采纳" data-date="11-07 22:57" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-07 22:57</span>
          <span class="news-item-title">Claude Max 订阅套餐使用额度被指“虚标”，Anthropic 辩词未获法官采纳</span>
          <span class="news-value-point">💡 IT之家 11 月 7 日消息，美国联邦治安法官谢文辉（Alex Tse）裁定，Anthropic 必须继续应对 Claude Max 套餐使用…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/023/823.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 7 日消息，当地时间 11 月 5 日，GitHub 发布博文，称上周在 GitHub Universe 大会上，正式公布了全新的 Git 存储架构，代号“Rubicon”。官方表示，该架构不仅具备每秒处理数千次写入的能力，还能实现读取按需水平扩展。经内部压力测试验证，新架构能够在保持极低读取延迟的同时，支持单个代码仓库容纳 5000 个智能体（Agent）并发协作，并承受每秒高达 7200 次的代码推送。IT之家获悉，该架构目前已经开启小范围定向内测（limited private preview），并计划于明年初逐步扩大开放范围。据介绍，如今 GitHub 上最繁忙的代码仓库，其单秒写入峰值最多也不过数十次，且往往呈现短暂脉冲式的突发状态。然而，随着越来越多的研发工作" data-title="GitHub 推出新 Git 存储架构：内部测试单个代码仓库支持 5000 个智能体同时协作，每秒处理 7200 次推送" data-date="11-07 22:57" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-07 22:57</span>
          <span class="news-item-title">GitHub 推出新 Git 存储架构：内部测试单个代码仓库支持 5000 个智能体同时协作，每秒处理 7200 次推送</span>
          <span class="news-value-point">💡 IT之家 11 月 7 日消息，当地时间 11 月 5 日，GitHub 发布博文，称上周在 GitHub Universe 大会上，正式公布了…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/023/822.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 7 日消息，据 RT今日俄罗斯报道，当地时间 11 月 6 日，特斯拉 CEO 埃隆 · 马斯克接受投资者罗恩 · 巴伦采访时表示，他热爱中国，并高度评价中国汽车工业的竞争力。“中国令人惊叹。顺便说一句，我爱中国。去那里旅行令人深受鼓舞，”马斯克在采访中说。他同时指出，在上海生产的特斯拉 Model Y 是中国最畅销的电动汽车，但强调实现这一成绩“并不容易”。马斯克特别补充道：“中国汽车公司非常厉害。”据IT之家此前报道，今年 9 月，马斯克接受了央视财经专访。当谈及 AI，他表示中国的 AI 大模型整体而言非常出色，单位算力产出的性能几乎全球顶尖。他认为，中国解决算力问题的速度会比大多数人预想更快。粗略估计，大概两到三年内，中国就能依靠光刻技术与芯片制造补齐算力缺口。图" data-title="马斯克再次表白中国，称赞中国汽车工业水平高" data-date="11-07 22:51" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-07 22:51</span>
          <span class="news-item-title">马斯克再次表白中国，称赞中国汽车工业水平高</span>
          <span class="news-value-point">💡 IT之家 11 月 7 日消息，据 RT今日俄罗斯报道，当地时间 11 月 6 日，特斯拉 CEO 埃隆 · 马斯克接受投资者罗恩 · 巴伦采访…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/us-intelligence-believes-jensen-huang-had-romantic-relationship-with-chinese-spy-in-honeypot-operation-spy-suspect-linked-to-company-accused-of-smuggling-usd2-billion-in-ai-chips" target="_blank" rel="noopener" data-cat="keji" data-summary="美国情报人士表示， Nvidia首席执行官黄延森(Jensen Huang)在涉及Megaspeed高管黄爱丽丝(Alice Huang)的“蜜罐”行动中成为中国情报部门的目标。" data-title="US intelligence believes Jensen Huang had affair with Chinese spy in honeypot operation" data-date="11-07 22:47" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-07 22:47</span>
          <span class="news-item-title">美国情报部门认为Jensen Huang在蜜罐操作中与中国间谍有染</span>
          <span class="news-item-title-en">US intelligence believes Jensen Huang had affair with Chinese spy in honeypot operation</span>
          <span class="news-value-point">💡 美国情报人士表示， Nvidia首席执行官黄延森(Jensen Huang)在涉及Megaspeed高管黄爱丽丝(Alice Huang)的“蜜…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/big-tech/nvidias-jensen-huang-officially-called-to-congress-due-to-reports-of-a-chinese-spy-plot-officials-mention-growing-concerns-over-national-security" target="_blank" rel="noopener" data-cat="keji" data-summary="由于有关中国阴谋的报道，英伟达的Jensen Huang正式致电国会—官员们提到对国家安全的担忧日益增加" data-title="Nvidia&#39;s Jensen Huang officially called to Congress due to reports of a Chinese spy plot" data-date="11-07 21:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-07 21:30</span>
          <span class="news-item-title">由于有关中国间谍阴谋的报道，英伟达的Jensen Huang正式被召集到国会</span>
          <span class="news-item-title-en">Nvidia's Jensen Huang officially called to Congress due to reports of a Chinese spy plot</span>
          <span class="news-value-point">💡 由于有关中国阴谋的报道，英伟达的Jensen Huang正式致电国会—官员们提到对国家安全的担忧日益增加</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/dram/tsmc-denies-exploring-3d-dram-at-nvidias-request-advanced-memory-tech-is-still-years-from-market-viability" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道，英伟达要求台积电生产“3D DRAM”来解决内存短缺问题。" data-title="TSMC denies exploring 3D DRAM at Nvidia&#39;s request" data-date="11-07 21:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-07 21:00</span>
          <span class="news-item-title">台积电否认应英伟达要求探索3D DRAM</span>
          <span class="news-item-title-en">TSMC denies exploring 3D DRAM at Nvidia's request</span>
          <span class="news-value-point">💡 据报道，英伟达要求台积电生产“3D DRAM”来解决内存短缺问题</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/boxing/news/12040/13609513/ramla-ali-and-skye-nicolson-could-be-on-a-collision-course-if-they-win-their-world-title-fights-in-texas" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="如果Ramla Ali和Skye Nicolson都赢得冠军争夺战，他们可能会在明年初的统一比赛中相遇，他们将在周一凌晨在天空体育上直播。" data-title="Ali and Nicolson on a collision course?" data-date="11-08 15:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-08 15:00</span>
          <span class="news-item-title">阿里和尼科尔森在碰撞路线上？</span>
          <span class="news-item-title-en">Ali and Nicolson on a collision course?</span>
          <span class="news-value-point">💡 如果Ramla Ali和Skye Nicolson都赢得冠军争夺战，他们可能会在明年初的统一比赛中相遇，他们将在周一凌晨在天空体育上直播</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ckj0l542v7pvo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联主教练迈克尔·卡里克（ Michael Carrick ）表示，队长布鲁诺·费尔南德斯（ Bruno Fernandes ）对俱乐部的承诺“毫无疑问” ，这位中场球员“一如既往”。" data-title="&#39;Bruno&#39;s as good as ever&#39; - Carrick backs Man Utd captain" data-date="11-08 06:44" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-08 06:44</span>
          <span class="news-item-title">“布鲁诺一如既往的好” -卡里克支持曼联队长</span>
          <span class="news-item-title-en">'Bruno's as good as ever' - Carrick backs Man Utd captain</span>
          <span class="news-value-point">💡 曼联主教练迈克尔·卡里克（ Michael Carrick ）表示，队长布鲁诺·费尔南德斯（ Bruno Fernandes ）对俱乐部的承诺“…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cvy0red8yl69o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="奥利弗·格拉斯纳（ Oliver Glasner ）的庆祝活动和利亚姆·德拉普（ Liam Delap ）的两个进球对一支希望在本赛季首次主场英超联赛获胜后继续前进的诺丁汉森林队来说是个" data-title="Glasner glee and Delap double - win could be lift-off for Forest" data-date="11-08 05:42" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-08 05:42</span>
          <span class="news-item-title">Glasner glee和Delap双胜可能是Forest的起飞</span>
          <span class="news-item-title-en">Glasner glee and Delap double - win could be lift-off for Forest</span>
          <span class="news-value-point">💡 奥利弗·格拉斯纳（ Oliver Glasner ）的庆祝活动和利亚姆·德拉普（ Liam Delap ）的两个进球对一支希望在本赛季首次主场英…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/07/enzo-maresca-nottingham-forest-manchester-city-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="“你需要欲望和强度……我们没有匹配他们”曼城现在已经连续输掉了三场联赛恩佐·马雷斯卡（ Enzo Maresca ）指责他的球队缺乏欲望，以及他们在决斗中被击败的方式，连续第三次击败英超联赛。赢得比赛后" data-title="Enzo Maresca rues Manchester City’s lack of desire after defeat at Nottingham Forest" data-date="11-08 05:17" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-08 05:17</span>
          <span class="news-item-title">恩佐·马雷斯卡（ Enzo Maresca ）在诺丁汉森林（ Nottingham Forest ）失利后对曼城缺乏欲望感到后悔</span>
          <span class="news-item-title-en">Enzo Maresca rues Manchester City’s lack of desire after defeat at Nottingham Forest</span>
          <span class="news-value-point">💡 “你需要欲望和强度……我们没有匹配他们”曼城现在已经连续输掉了三场联赛恩佐·马雷斯卡（ Enzo Maresca ）指责他的球队缺乏欲望，以及他…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13609559/noni-madueke-has-become-a-different-player-says-mikel-arteta-as-winger-finds-new-level-of-creativity-and-efficiency" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="诺尼·马杜埃克（ Noni Madueke ）躺在草坪上，双手抱头，紧随阿森纳1-0战胜赫尔（ Hull ）的一对一失误。即使在终场哨响后，他的沮丧情绪仍在继续。" data-title="&#39;A different Noni?&#39; Madueke finding a new level for Arsenal" data-date="11-08 04:55" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-08 04:55</span>
          <span class="news-item-title">“不一样的诺妮？” Madueke为阿森纳寻找新的水平</span>
          <span class="news-item-title-en">'A different Noni?' Madueke finding a new level for Arsenal</span>
          <span class="news-value-point">💡 诺尼·马杜埃克（ Noni Madueke ）躺在草坪上，双手抱头，紧随阿森纳1-0战胜赫尔（ Hull ）的一对一失误</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cm93z0l03n8vo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="恩佐·马雷斯卡（ Enzo Maresca ）在周六晚上离开曼城球场时，耳边响起了“我们能每周都和你比赛吗？”的歌声--这位意大利人的梦想开始了，因为曼城主教练正在迅速变成一场噩梦。" data-title="Maresca&#39;s dream start turns into nightmare as title hopes hit" data-date="11-08 04:54" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-08 04:54</span>
          <span class="news-item-title">马雷斯卡的梦想开始变成了噩梦，因为冠军希望击中</span>
          <span class="news-item-title-en">Maresca's dream start turns into nightmare as title hopes hit</span>
          <span class="news-value-point">💡 恩佐·马雷斯卡（ Enzo Maresca ）在周六晚上离开曼城球场时，耳边响起了“我们能每周都和你比赛吗</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/nov/07/nottingham-forest-v-manchester-city-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利亚姆·德拉普（ Liam Delap ）打进了两个令人惊叹的进球，诺丁汉森林（ Nottingham Forest ）在主场以令人印象深刻的击败曼城（ Manchester City ）结束了他们的荒芜比赛。我们在城市广场（ City Ground ）出发。在开球之前，我们将听到The Last Post。Remembrance Sunday is tomorrow. Continue r" data-title="Nottingham Forest 3-1 Manchester City: Premier League – as it happened" data-date="11-08 04:04" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-08 04:04</span>
          <span class="news-item-title">诺丁汉森林3-1曼城：英超联赛–事实如此</span>
          <span class="news-item-title-en">Nottingham Forest 3-1 Manchester City: Premier League – as it happened</span>
          <span class="news-value-point">💡 利亚姆·德拉普（ Liam Delap ）打进了两个令人惊叹的进球，诺丁汉森林（ Nottingham Forest ）在主场以令人印象深刻的击…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13609523/nottingham-forest-3-1-manchester-city-premier-league-highlights" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="免费观看：诺丁汉森林和曼城之间英超比赛的亮点。" data-title="Delightful Delap stars as Forest shock Man City" data-date="11-08 03:37" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-08 03:37</span>
          <span class="news-item-title">令人愉快的德拉普之星：森林震撼曼城</span>
          <span class="news-item-title-en">Delightful Delap stars as Forest shock Man City</span>
          <span class="news-value-point">💡 免费观看：诺丁汉森林和曼城之间英超比赛的亮点</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6rmyg7xpnj1o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在击败赫尔城后，阿森纳在英超联赛的顶端得到6分-但是马丁·奥德加德的进球是否挽救了瓦尔的脸红？" data-title="Another 1-0 for relentless Arsenal - but did Odegaard spare VAR blushes?" data-date="11-08 03:34" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-08 03:34</span>
          <span class="news-item-title">对于无情的阿森纳来说，又是1-0 -但是奥德加多余的VAR脸红了吗？</span>
          <span class="news-item-title-en">Another 1-0 for relentless Arsenal - but did Odegaard spare VAR blushes?</span>
          <span class="news-value-point">💡 在击败赫尔城后，阿森纳在英超联赛的顶端得到6分-但是马丁·奥德加德的进球是否挽救了瓦尔的脸红</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/10/premier-league-top-scorers-2026-27-race-for-golden-boot" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="找出哪位英国顶尖射手正在向进球排行榜射击。继续阅读……" data-title="Premier League top scorers 2026-27: who is leading race for the golden boot?" data-date="11-08 03:32" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-08 03:32</span>
          <span class="news-item-title">2026-27赛季英超联赛最佳射手：谁是金靴赛的领跑者？</span>
          <span class="news-item-title-en">Premier League top scorers 2026-27: who is leading race for the golden boot?</span>
          <span class="news-value-point">💡 找出哪位英国顶尖射手正在向进球排行榜射击</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/07/nottingham-forest-manchester-city-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="等待足够长的时间，结果将反映出表现。曼城可能已经赢得了本赛季的前七场联赛，但他们看起来总是很脆弱，现在已经连续三场失利。诺丁汉森林可能是第二瓶" data-title="Delap’s Nottingham Forest stunners hand Manchester City third league defeat in a row" data-date="11-08 03:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-08 03:30</span>
          <span class="news-item-title">德拉普的诺丁汉森林惊艳之手曼城连续第三场联赛失利</span>
          <span class="news-item-title-en">Delap’s Nottingham Forest stunners hand Manchester City third league defeat in a row</span>
          <span class="news-value-point">💡 等待足够长的时间，结果将反映出表现</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c8wy9512p2yvo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="诺丁汉森林和曼城的球员在他们在曼城球场的英超比赛后是如何评分的。" data-title="Delightful Delap and outfought Anderson - Forest v Man City player ratings" data-date="11-08 03:26" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-08 03:26</span>
          <span class="news-item-title">令人愉快的Delap和出局的Anderson - Forest v Man City球员评分</span>
          <span class="news-item-title-en">Delightful Delap and outfought Anderson - Forest v Man City player ratings</span>
          <span class="news-value-point">💡 诺丁汉森林和曼城的球员在他们在曼城球场的英超比赛后是如何评分的</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13609399/arsenal-1-0-hull-premier-league-highlights" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="免费观看：阿森纳与赫尔在英超联赛中的比赛亮点。" data-title="Odegaard earns Arsenal narrow win over Hull to extend gap at the top" data-date="11-08 01:16" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-08 01:16</span>
          <span class="news-item-title">奥德加尔赢得了阿森纳对赫尔的狭隘胜利，以扩大顶部的差距</span>
          <span class="news-item-title-en">Odegaard earns Arsenal narrow win over Hull to extend gap at the top</span>
          <span class="news-value-point">💡 免费观看：阿森纳与赫尔在英超联赛中的比赛亮点</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13609257/leeds-1-0-tottenham-hotspur-premier-league-highlights" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="免费观看：利兹队在英超联赛中对阵托特纳姆热刺队的比赛亮点。" data-title="Leeds end Spurs’ winning run in VAR controversy filled match" data-date="11-08 01:15" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-08 01:15</span>
          <span class="news-item-title">利兹结束马刺队在VAR争议充满比赛中的胜利</span>
          <span class="news-item-title-en">Leeds end Spurs’ winning run in VAR controversy filled match</span>
          <span class="news-value-point">💡 免费观看：利兹队在英超联赛中对阵托特纳姆热刺队的比赛亮点</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13609384/fulham-1-1-newcastle-premier-league-highlights" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="免费观看：富勒姆和纽卡斯尔联队之间英超比赛的亮点。" data-title="Late goals as Fulham draw with Newcastle" data-date="11-08 01:10" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-08 01:10</span>
          <span class="news-item-title">与纽卡斯尔队一起打进富勒姆队的近期进球</span>
          <span class="news-item-title-en">Late goals as Fulham draw with Newcastle</span>
          <span class="news-value-point">💡 免费观看：富勒姆和纽卡斯尔联队之间英超比赛的亮点</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/023/918.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 8 日消息，比亚迪旗下超豪华行政旗舰轿车 —— 仰望鼎曜于北京时间 7 日晚间迎来全球首秀，IT之家已在现场进行详细报道。随后，仰望汽车通过小程序公布了仰望鼎曜“山河鼎韵”限量版车型的价格：208 万元。该车定金为 30 万元。小程序页面显示，新车拥有“棕岩白玉”主题的专属内外饰，不排除后续开放更多个性化定制的可能。仰望鼎曜车身尺寸为 5600×2030×1590mm，轴距 3500mm；采用礼宾级中轴对开门设计，前门最大开启角 80°，后门最大开启角 90°。仰望鼎曜“山河鼎韵”限量版拥有专属外观内饰及高定配置，包含琥珀金双腰线、限量版专属印记、专属云纹图案、出风口宝石 · 和田玉、金色扬声器面罩、车门内置芳纶纤维等。相关阅读：《比亚迪超豪华行政旗舰轿车登场！仰望鼎曜行" data-title="208 万元！比亚迪仰望鼎曜“山河鼎韵”限量版车型价格揭晓" data-date="11-08 16:10" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-08 16:10</span>
          <span class="news-item-title">208 万元！比亚迪仰望鼎曜“山河鼎韵”限量版车型价格揭晓</span>
          <span class="news-value-point">💡 IT之家 11 月 8 日消息，比亚迪旗下超豪华行政旗舰轿车 —— 仰望鼎曜于北京时间 7 日晚间迎来全球首秀，IT之家已在现场进行详细报道</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/023/917.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 8 日消息，上纬新材启元机器人第 10,000 台个人机器人正式下线。上纬新材启元机器人联席总裁、Q 业务部总裁刘东方介绍：当前启元机器人的月活超过 98%，日均在线峰值超过 40%，日均在线时长 3 小时，平均每位用户每天交互 100 多次。IT之家注意到，在量产现场，刘东方将编号为“NO.10000”的启元 Q1 交付给代表用户吴晓波。据介绍，3 天前，启元机器人完成了对启元 Q1、启元 T1 上市后的首次 OTA 版本升级：启元 Q1 新增了如故事魔法师、科学探险家等 6 大官方角色，升级了英语口语陪练和 AI 启蒙课两大学习体验。启元 T1 新增了智能识别地形、自动变形跟随；远程音视频查看机器人视⻆并操控移动等多项功能，持续丰富家庭场景服务。相关阅读：《“全球首个" data-title="上纬新材刘东方：当前启元机器人的月活超过 98%，平均每位用户每天交互 100 多次" data-date="11-08 16:02" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-08 16:02</span>
          <span class="news-item-title">上纬新材刘东方：当前启元机器人的月活超过 98%，平均每位用户每天交互 100 多次</span>
          <span class="news-value-point">💡 IT之家 11 月 8 日消息，上纬新材启元机器人第 10,000 台个人机器人正式下线</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-08/10728371.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网哈尔滨11月8日电 (记者 王琳)由黑龙江省文化和旅游厅倾力打造的一站式智慧文旅服务平台——“一键玩龙江”小程序于11月8日正式焕新上线，立足智慧旅游、宠客服务、文化赋能定位，打通游前决策、游中体验、游后回味的全旅行链条，以数字科技赋能冰雪文旅。" data-title="黑龙江“一键玩龙江”智慧文旅小程序焕新上线" data-date="11-08 16:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 16:02</span>
          <span class="news-item-title">黑龙江“一键玩龙江”智慧文旅小程序焕新上线</span>
          <span class="news-value-point">💡 中新网哈尔滨11月8日电 (记者 王琳)由黑龙江省文化和旅游厅倾力打造的一站式智慧文旅服务平台——“一键玩龙江”小程序于11月8日正式焕新上线，…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/023/916.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 8 日消息，据外媒 Gamesradar 当地时间 7 日报道，前索尼 SIE 总裁肖恩 · 莱登认为，PS6 没必要继续堆性能。随着新一代主机带来的技术跨越越来越小，下一代主机真正值得追求的创新，是降低售价，让更多玩家买得起。他解释道，过去但凡有新一代主机推出，总会有令人眼前一亮的升级。“PS1 到 PS2 的进步非常惊人，从 CD 到 DVD 的跨越也是如此。”即使是 PS4，索尼也在实现全面联网的同时，将售价定在了 399 美元。关于 PS6 的传闻，焦点则集中在更强的光线追踪和更高的浮点运算性能上。对技术发烧友来说，这些升级听起来或许很厉害，但在莱登和普通玩家看来，“这些差别恐怕只有狗才听得出来”。莱登认为，现有主机的性能已经足够。真正的创新不是推出一台售价 1," data-title="前索尼 SIE 总裁肖恩 · 莱登：PS6 没必要继续堆性能，价格亲民更重要" data-date="11-08 15:53" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-08 15:53</span>
          <span class="news-item-title">前索尼 SIE 总裁肖恩 · 莱登：PS6 没必要继续堆性能，价格亲民更重要</span>
          <span class="news-value-point">💡 IT之家 11 月 8 日消息，据外媒 Gamesradar 当地时间 7 日报道，前索尼 SIE 总裁肖恩 · 莱登认为，PS6 没必要继续堆…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-08/10728363.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社福州11月8日电 (郑江洛)福州港客运站8日通报，受气象条件影响，福州马尾至马祖“小三通”客运航线9日将双向停航。" data-title="受气象条件影响 “两马”航线9日双向停航" data-date="11-08 15:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 15:53</span>
          <span class="news-item-title">受气象条件影响 “两马”航线9日双向停航</span>
          <span class="news-value-point">💡 中新社福州11月8日电 (郑江洛)福州港客运站8日通报，受气象条件影响，福州马尾至马祖“小三通”客运航线9日将双向停航</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/023/915.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 8 日消息，据博板堂 / 视讯堂旗下“ChannelGate 视博合聚”爆料，有传言称 AOC 显示器内部发布了重要通知，大促结束后（预计这里指“双十一”）部分机型将面临大幅上涨。据报道，AOC 内部会议通知，由于成本变化，第四季度和明年第一季度，27 寸 QHD 相关的电竞以及高分（高分辨率）机型整体涨幅将高达 50-150 元，部分机型涨幅近 200 元。因此大促结束后，相关机型的价格政策将立即面临成本上涨。" data-title="消息称 AOC 显示器“大促后部分机型将面临大幅涨价”" data-date="11-08 15:52" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-08 15:52</span>
          <span class="news-item-title">消息称 AOC 显示器“大促后部分机型将面临大幅涨价”</span>
          <span class="news-value-point">💡 IT之家 11 月 8 日消息，据博板堂 / 视讯堂旗下“ChannelGate 视博合聚”爆料，有传言称 AOC 显示器内部发布了重要通知，大…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/023/912.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 8 日消息，索尼宣布，原定面向全球市场发售的 PlayStation Pulse Elevate 无线音箱将延期上市，目前官方尚未公布新的发售时间。索尼表示，官方在持续进行 Pulse Elevate 音箱质量测试期间“发现产品存在一项生产问题”，因此决定推迟上市计划。索尼称，延期能够为产品争取更多时间，确保最终交付的体验符合预期，并对给消费者带来的不便表示歉意。索尼于 2025 年 9 月首次公布 Pulse Elevate，国行定价 1,748 元，这款音箱主打沉浸式桌面音效，它搭载两个喇叭，每个喇叭内置平面振膜单元和低音扬声器，平面振膜单元受录音室启发，号称能够以高精度呈现广阔频响动态范围内的所有声音；内置低音扬声器提供层次丰富的低音音色。同时，该耳机搭载 Play" data-title="索尼：PlayStation PULSE Elevate 无线音箱出现“生产问题”，产品将延期上市" data-date="11-08 15:36" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-08 15:36</span>
          <span class="news-item-title">索尼：PlayStation PULSE Elevate 无线音箱出现“生产问题”，产品将延期上市</span>
          <span class="news-value-point">💡 IT之家 11 月 8 日消息，索尼宣布，原定面向全球市场发售的 PlayStation Pulse Elevate 无线音箱将延期上市，目前官…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c6r7yg9xkdy8o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="随着人们对这些收藏玩具的兴趣减弱，其母公司泡泡玛特（Pop Mart）的收入也随之下降。" data-title="销量急挫，Labubu热潮正在退烧吗？" data-date="11-08 15:35" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-08 15:35</span>
          <span class="news-item-title">销量急挫，Labubu热潮正在退烧吗？</span>
          <span class="news-value-point">💡 随着人们对这些收藏玩具的兴趣减弱，其母公司泡泡玛特（Pop Mart）的收入也随之下降</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-08/10728357.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="眼下，全国各地都在推进一刻钟便民生活圈建设，对准居民家门口的“小事、实事、急事”精准发力。湖北荆州的洪垸社区七成以上居民是老年人，社区紧扣银发群体的日常刚需，把医养、助餐、邻里互助资源全部整合起来，为老人们提供暖心的适老服务。" data-title="口袋绿地、便民工坊 群众家门口有了“幸福圈”" data-date="11-08 15:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 15:27</span>
          <span class="news-item-title">口袋绿地、便民工坊 群众家门口有了“幸福圈”</span>
          <span class="news-value-point">💡 眼下，全国各地都在推进一刻钟便民生活圈建设，对准居民家门口的“小事、实事、急事”精准发力</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-08/10728353.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="眼下，内蒙古已全面进入供暖季，在呼和浩特市和林格尔新区，一家数据中心把服务器运算产生的热量收集起来，通过高效的余热回收系统，为园区供暖。" data-title="数据中心回收服务器余热 为供暖提供“热源”" data-date="11-08 15:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 15:05</span>
          <span class="news-item-title">数据中心回收服务器余热 为供暖提供“热源”</span>
          <span class="news-value-point">💡 眼下，内蒙古已全面进入供暖季，在呼和浩特市和林格尔新区，一家数据中心把服务器运算产生的热量收集起来，通过高效的余热回收系统，为园区供暖</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/cricket/news/12040/13609615/australia-cricket-usman-khawaja-says-he-has-not-thrown-anyone-under-the-bus-with-claims-about-ball-tampering-scandal" target="_blank" rel="noopener" data-cat="zonghe" data-summary="乌斯曼·卡瓦贾（ Usman Khawaja ）坚称他没有“把任何人扔到公共汽车下面” ，因为他的自传摘录声称整个澳大利亚队都知道2018年南非巡回赛上的球篡改计划。" data-title="Khawaja: I haven&#39;t &#39;thrown anyone under the bus&#39; with &#39;Sandpapergate&#39; claims" data-date="11-08 15:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-08 15:00</span>
          <span class="news-item-title">Khawaja ：我没有因为“Sandpapergate”声称而“把任何人扔到公共汽车下面”</span>
          <span class="news-item-title-en">Khawaja: I haven't 'thrown anyone under the bus' with 'Sandpapergate' claims</span>
          <span class="news-value-point">💡 乌斯曼·卡瓦贾（ Usman Khawaja ）坚称他没有“把任何人扔到公共汽车下面” ，因为他的自传摘录声称整个澳大利亚队都知道2018年南非…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/boxing/news/12040/13609610/dana-white-chris-billam-smith-stopped-too-soon-in-shock-defeat-to-cheavon-clarke" target="_blank" rel="noopener" data-cat="zonghe" data-summary="克里斯·比拉姆-史密斯（ Chris Billam-Smith ）用脚完成了比赛，摇摇头表示抗议，裁判李·埃弗（ Lee Every ）在对阵谢文·克拉克（ Cheavon Clarke ）的第七轮比赛中" data-title="White: Billam-Smith was stopped too soon" data-date="11-08 15:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-08 15:00</span>
          <span class="news-item-title">White ： Billam-Smith被拦得太早了</span>
          <span class="news-item-title-en">White: Billam-Smith was stopped too soon</span>
          <span class="news-value-point">💡 克里斯·比拉姆-史密斯（ Chris Billam-Smith ）用脚完成了比赛，摇摇头表示抗议，裁判李·埃弗（ Lee Every ）在对阵谢…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-08/10728344.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="居民住宅楼起火如何逃生？许多人认为应该往楼下跑，跑到室外才安全，真是这样的吗？" data-title="住宅楼起火如何正确逃生？2个避险误区要警惕" data-date="11-08 14:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 14:30</span>
          <span class="news-item-title">住宅楼起火如何正确逃生？2个避险误区要警惕</span>
          <span class="news-value-point">💡 居民住宅楼起火如何逃生</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c64g1n74j259o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="六人在波兰第二大城市克拉科夫主要广场发生的一宗随机枪击案中丧生，其后警方在袭击者家中发现另外三具遗体。" data-title="波兰克拉科夫“极右翼”枪击案致六人死亡 我们所知多少" data-date="11-08 14:29" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-08 14:29</span>
          <span class="news-item-title">波兰克拉科夫“极右翼”枪击案致六人死亡 我们所知多少</span>
          <span class="news-value-point">💡 六人在波兰第二大城市克拉科夫主要广场发生的一宗随机枪击案中丧生，其后警方在袭击者家中发现另外三具遗体</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-08/10728321.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网福建清流11月8日电 题：全国119消防奖先进个人阳剑华：一只“蓝色背包”把安全背进村里" data-title="全国119消防奖先进个人阳剑华：一只“蓝色背包”把安全背进村里" data-date="11-08 14:25" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-08 14:25</span>
          <span class="news-item-title">全国119消防奖先进个人阳剑华：一只“蓝色背包”把安全背进村里</span>
          <span class="news-value-point">💡 中新网福建清流11月8日电 题：全国119消防奖先进个人阳剑华：一只“蓝色背包”把安全背进村里</span>
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


<p class="news-updated">🕐 抓取更新于 2026-11-08 16:11（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
