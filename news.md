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
      <span>2026-10-08 22:46 抓取更新</span>
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
        <span class="channel-count">52</span>
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
        <span class="channel-count">7</span>
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
  <div class="ov-item"><span class="ov-num">52</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×16 · IT之家×8</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gj/2026/10-08/10709383.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月8日电(魏晨曦)2023年10月7日，巴勒斯坦伊斯兰抵抗运动(哈马斯)自加沙地带对以色列境内军民目标发起突袭并扣押大量人员。以军随后空袭加沙地带，切断水、电、燃料等供应。" data-title="三年过去了，巴以冲突中最沉重的问题仍找不到答案" data-date="10-08 21:48" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-08 21:48</span>
      </div>
      <h2 class="hero-featured-title">三年过去了，巴以冲突中最沉重的问题仍找不到答案</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/010/722.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 8 日消息，Cooler Master（酷冷至尊）今日推出了 V8 ACE 3DHP 风冷散热器的银白色版本。其依旧提供 Intel 平台优化和 AMD 平台优化 2 种变体，价格维持在与原版相同的 699 元。V8 ACE 3DHP 整体呈现单塔双风扇结构，拥有 2 根三端 3DHP 热管和 4 根双端 SCCHP 热管，配备 2 颗 12030 外形规格的 LCP 扇叶环形动态轴承风扇。其三维 137×139×168 (mm)，内存模组限高 45mm，拥有 V 型引擎外罩，享受 6 年质保。京东酷冷至尊 V8 ACE 3DHP 银白色 Intel 优化 699 元直达链接京东酷冷至尊 V8 ACE 3DHP 银白色 AMD 优化 699 元直达链接" data-title="酷冷至尊 V8 ACE 3DHP 风冷新增银白款，价格维持 699 元" data-date="10-08 22:41" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">酷冷至尊 V8 ACE 3DHP 风冷新增银白款，价格维持 699 元</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/sport/live/2026/oct/08/football-qa-ask-ed-aarons-your-questions-as-the-premier-league-returns" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在经历了以曼城判决为主导的漫长国际休息之后，英超联赛将于周六回归。足球作家Ed Aarons现在在线回答您的问题登录或注册参加partpapalazaru提问：作为圣徒球迷，在" data-title="Football Q&amp;A: ask Ed Aarons your questions as the Premier League returns" data-date="10-08 22:47" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Football Q&A: ask Ed Aarons your questions as the Premier League returns</p>
    </a>
    <a class="hero-sub-card" href="https://www.nytimes.com/2026/10/08/books/nobel-prize-literature.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这位作家加入了包括托妮·莫里森（ Toni Morrison ）、塞缪尔·贝克特（ Samuel Beckett ）和鲍勃·迪伦（ Bob D" data-title="Canadian Poet Anne Carson Is Awarded Nobel Prize in Literature" data-date="10-08 22:41" data-source="纽约时报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
      </div>
      <p class="hero-sub-title">Canadian Poet Anne Carson Is Awarded Nobel Prize in Literature</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-08/10709383.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月8日电(魏晨曦)2023年10月7日，巴勒斯坦伊斯兰抵抗运动(哈马斯)自加沙地带对以色列境内军民目标发起突袭并扣押大量人员。以军随后空袭加沙地带，切断水、电、燃料等供应。" data-title="三年过去了，巴以冲突中最沉重的问题仍找不到答案" data-date="10-08 21:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-08 21:48</span>
          <span class="news-item-title">三年过去了，巴以冲突中最沉重的问题仍找不到答案</span>
          <span class="news-value-point">💡 中新网10月8日电(魏晨曦)2023年10月7日，巴勒斯坦伊斯兰抵抗运动(哈马斯)自加沙地带对以色列境内军民目标发起突袭并扣押大量人员</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/08/us/maine-senate-collins-jackson-oil.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="缅因州有一半的房屋依赖取暖油。特朗普总统与伊朗的战争导致成本上升，已成为该州参议院竞选的核心。" data-title="In Maine Senate Race, Spiking Heating Oil Costs Put Susan Collins on Defensive" data-date="10-08 21:46" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-08 21:46</span>
          <span class="news-item-title">在缅因州参议院竞选中，飙升的取暖油成本使苏珊·柯林斯处于防守状态</span>
          <span class="news-item-title-en">In Maine Senate Race, Spiking Heating Oil Costs Put Susan Collins on Defensive</span>
          <span class="news-value-point">💡 缅因州有一半的房屋依赖取暖油</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-08/10709367.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京10月8日电(记者邵艺博、赵瀚泽)外交部发言人毛宁8日就村田晃大非法持刀侵闯中国驻日本使馆案首次开庭答记者问时表示，日本自卫队现役官员持刀侵闯中国驻日本使馆，向中方外交人员发出暴力威胁，是国际社会前所未闻的恶性事件，严重违反《维也纳外交关系公约》，严重威胁中方外交人员人身安全和外交馆舍安全，暴露出日本国内右翼势力猖獗、自卫队人员失管失教等诸多深层次问题。" data-title="外交部：再次敦促日方严惩持刀侵闯中国驻日使馆凶犯" data-date="10-08 21:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-08 21:24</span>
          <span class="news-item-title">外交部：再次敦促日方严惩持刀侵闯中国驻日使馆凶犯</span>
          <span class="news-value-point">💡 新华社北京10月8日电(记者邵艺博、赵瀚泽)外交部发言人毛宁8日就村田晃大非法持刀侵闯中国驻日本使馆案首次开庭答记者问时表示，日本自卫队现役官员…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-08/10709306.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社马尼拉10月8日电 (记者 周璟)菲律宾参议院8日三读通过《儿童网络安全与保护法案》，拟限制18岁以下未成年人使用社交媒体。" data-title="菲律宾参议院通过限制未成年人使用社交媒体的法案" data-date="10-08 21:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-08 21:03</span>
          <span class="news-item-title">菲律宾参议院通过限制未成年人使用社交媒体的法案</span>
          <span class="news-value-point">💡 中新社马尼拉10月8日电 (记者 周璟)菲律宾参议院8日三读通过《儿童网络安全与保护法案》，拟限制18岁以下未成年人使用社交媒体</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-08/10709301.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社柏林10月8日电 (记者 马秀秀)根据德国联邦统计局8日公布的初步数据，经工作日和季节性调整，2026年8月德国出口额环比下降0.8%，达到1376亿欧元。这是该数据连续第二个月出现下降。" data-title="德国8月出口额环比下降0.8%" data-date="10-08 20:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-08 20:54</span>
          <span class="news-item-title">德国8月出口额环比下降0.8%</span>
          <span class="news-value-point">💡 中新社柏林10月8日电 (记者 马秀秀)根据德国联邦统计局8日公布的初步数据，经工作日和季节性调整，2026年8月德国出口额环比下降0.8%，达…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-08/10709342.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网拉萨10月8日电 (旦增旺姆 格桑央金 武春燕)8日，中国铁路青藏集团有限公司拉萨车站介绍，2026年国庆假期车站发送旅客10.09万人次。其中10月1日发送旅客1.85万人次，刷新建站以来单日旅客发送历史最高记录。" data-title="单日发送量创历史新高 拉萨车站国庆假期累计发送旅客10.09万人次" data-date="10-08 20:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-08 20:53</span>
          <span class="news-item-title">单日发送量创历史新高 拉萨车站国庆假期累计发送旅客10.09万人次</span>
          <span class="news-value-point">💡 中新网拉萨10月8日电 (旦增旺姆 格桑央金 武春燕)8日，中国铁路青藏集团有限公司拉萨车站介绍，2026年国庆假期车站发送旅客10.09万人次</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-08/10709350.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月8日电 据湖北省纪委监委消息：湖北省随州市人大常委会党组成员汪海涛涉嫌严重违纪违法，目前正接受湖北省纪委监委纪律审查和监察调查。" data-title="湖北省随州市人大常委会党组成员汪海涛接受审查调查" data-date="10-08 20:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-08 20:49</span>
          <span class="news-item-title">湖北省随州市人大常委会党组成员汪海涛接受审查调查</span>
          <span class="news-value-point">💡 中新网10月8日电 据湖北省纪委监委消息：湖北省随州市人大常委会党组成员汪海涛涉嫌严重违纪违法，目前正接受湖北省纪委监委纪律审查和监察调查</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-08/10709338.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月8日电 据国家市场监督管理总局网站消息，近日，市场监管总局批准发布《集装箱铁水联运装载和安全检查技术规范》国家标准(GB/T 48309—2026)，统筹铁路、水路两种运输方式的作业要求，对通用集装箱铁水联运的货物装载、安全检查作出统一规范，为实现集装箱铁水联运“全程不开箱”奠定基础。" data-title="集装箱铁水联运装载和安全检查国家标准发布" data-date="10-08 20:38" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-08 20:38</span>
          <span class="news-item-title">集装箱铁水联运装载和安全检查国家标准发布</span>
          <span class="news-value-point">💡 中新网10月8日电 据国家市场监督管理总局网站消息，近日，市场监管总局批准发布《集装箱铁水联运装载和安全检查技术规范》国家标准(GB/T 483…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-08/10709329.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社广州10月8日电 (方伟彬 史雪晴)记者8日从广州出入境边防检查总站(下称“广州边检总站”)获悉，2026年国庆假期(10月1日至7日)，该总站所辖口岸累计保障出入境人员约40.5万人次，交通运输工具3500余架(艘)次。日均查验量5.8万人次，同比增长14.7%，客流总量创近五年国庆假期新高。" data-title="国庆叠加广交会 广州边检验放40.5万人次创近五年新高" data-date="10-08 20:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-08 20:32</span>
          <span class="news-item-title">国庆叠加广交会 广州边检验放40.5万人次创近五年新高</span>
          <span class="news-value-point">💡 中新社广州10月8日电 (方伟彬 史雪晴)记者8日从广州出入境边防检查总站(下称“广州边检总站”)获悉，2026年国庆假期(10月1日至7日)，…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-08/10709325.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月8日电 (记者 陈杭)记者8日从北京市委教育工委获悉，“永远的长征”主题宣讲在中国石油大学(北京)举办，全国基层理论宣讲先进集体、江西于都“长征源”宣讲团走进校园，以“现场讲述+情景演绎+诗歌朗诵”的复合形式，讲授一堂跨越时空的长征精神“大思政课”。" data-title="北京市大中小学生同上长征精神“大思政课”" data-date="10-08 20:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-08 20:15</span>
          <span class="news-item-title">北京市大中小学生同上长征精神“大思政课”</span>
          <span class="news-value-point">💡 中新网北京10月8日电 (记者 陈杭)记者8日从北京市委教育工委获悉，“永远的长征”主题宣讲在中国石油大学(北京)举办，全国基层理论宣讲先进集体…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-08/10709303.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月8日电 (记者 张素)记者从中国最高人民法院获悉，10月8日，浙江省宁波市中级人民法院一审公开宣判中央巡视组原副部级巡视专员许传智受贿、利用影响力受贿案。" data-title="中央巡视组原副部级巡视专员许传智一审获刑12年" data-date="10-08 20:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-08 20:11</span>
          <span class="news-item-title">中央巡视组原副部级巡视专员许传智一审获刑12年</span>
          <span class="news-value-point">💡 中新社北京10月8日电 (记者 张素)记者从中国最高人民法院获悉，10月8日，浙江省宁波市中级人民法院一审公开宣判中央巡视组原副部级巡视专员许传…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/08/world/middleeast/israel-embassy-milstein-huckabee.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="据《泰晤士报》获得的多名官员和文件显示，大使迈克·赫卡比（ Mike Huckabee ）的一名高级助手歪曲信息，以有利的方式描绘内塔尼亚胡政府。" data-title="How a U.S. Diplomat Suppressed and Altered Reports Critical of Israel" data-date="10-08 17:00" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-08 17:00</span>
          <span class="news-item-title">美国外交官如何压制和篡改批评以色列的报道</span>
          <span class="news-item-title-en">How a U.S. Diplomat Suppressed and Altered Reports Critical of Israel</span>
          <span class="news-value-point">💡 据《泰晤士报》获得的多名官员和文件显示，大使迈克·赫卡比（ Mike Huckabee ）的一名高级助手歪曲信息，以有利的方式描绘内塔尼亚胡政府</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-08/10709165.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中央纪委国家监委网站讯 广东省人大常委会党组成员、副主任张硕辅涉嫌严重违纪违法，目前正接受中央纪委国家监委纪律审查和监察调查。" data-title="广东省人大常委会党组成员、副主任张硕辅接受中央纪委国家监委纪律审查和监察调查" data-date="10-08 16:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-08 16:01</span>
          <span class="news-item-title">广东省人大常委会党组成员、副主任张硕辅接受中央纪委国家监委纪律审查和监察调查</span>
          <span class="news-value-point">💡 中央纪委国家监委网站讯 广东省人大常委会党组成员、副主任张硕辅涉嫌严重违纪违法，目前正接受中央纪委国家监委纪律审查和监察调查</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-08/10709114.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网南昌10月8日电 (记者 吴鹏泉)打卡商圈街区、乐享特色美食、尽赏赣鄱风光......今年国庆假期，江西消费市场人气爆棚、活力迸发。" data-title="国庆假期江西消费市场活力迸发" data-date="10-08 15:58" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-08 15:58</span>
          <span class="news-item-title">国庆假期江西消费市场活力迸发</span>
          <span class="news-value-point">💡 中新网南昌10月8日电 (记者 吴鹏泉)打卡商圈街区、乐享特色美食、尽赏赣鄱风光......今年国庆假期，江西消费市场人气爆棚、活力迸发</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-08/10709159.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月8日电 (记者 黄钰钦 谢雁冰)外交部发言人8日宣布：法国总统外事顾问博纳将于10月9日至13日来华，同中共中央政治局委员、中央外办主任王毅举行新一轮中法战略对话。" data-title="法国总统外事顾问博纳将来华举行中法战略对话 外交部介绍相关安排" data-date="10-08 15:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-08 15:57</span>
          <span class="news-item-title">法国总统外事顾问博纳将来华举行中法战略对话 外交部介绍相关安排</span>
          <span class="news-value-point">💡 中新网北京10月8日电 (记者 黄钰钦 谢雁冰)外交部发言人8日宣布：法国总统外事顾问博纳将于10月9日至13日来华，同中共中央政治局委员、中央…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/010/722.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 8 日消息，Cooler Master（酷冷至尊）今日推出了 V8 ACE 3DHP 风冷散热器的银白色版本。其依旧提供 Intel 平台优化和 AMD 平台优化 2 种变体，价格维持在与原版相同的 699 元。V8 ACE 3DHP 整体呈现单塔双风扇结构，拥有 2 根三端 3DHP 热管和 4 根双端 SCCHP 热管，配备 2 颗 12030 外形规格的 LCP 扇叶环形动态轴承风扇。其三维 137×139×168 (mm)，内存模组限高 45mm，拥有 V 型引擎外罩，享受 6 年质保。京东酷冷至尊 V8 ACE 3DHP 银白色 Intel 优化 699 元直达链接京东酷冷至尊 V8 ACE 3DHP 银白色 AMD 优化 699 元直达链接" data-title="酷冷至尊 V8 ACE 3DHP 风冷新增银白款，价格维持 699 元" data-date="10-08 22:41" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-08 22:41</span>
          <span class="news-item-title">酷冷至尊 V8 ACE 3DHP 风冷新增银白款，价格维持 699 元</span>
          <span class="news-value-point">💡 IT之家 10 月 8 日消息，Cooler Master（酷冷至尊）今日推出了 V8 ACE 3DHP 风冷散热器的银白色版本</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1007904/google-gemini-ai-agent-enterprise" target="_blank" rel="noopener" data-cat="keji" data-summary="谷歌正在推出一款“通用”双子座人工智能代理，可以在后台跨应用和设备工作。该工具是周四Gemini at Work活动的一部分，将在Gemini Enterprise应用程序中提供，允许用户聊天" data-title="Google is launching a one-stop Gemini agent for your work tasks" data-date="10-08 22:28" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-08 22:28</span>
          <span class="news-item-title">谷歌正在为您的工作任务推出一站式Gemini代理</span>
          <span class="news-item-title-en">Google is launching a one-stop Gemini agent for your work tasks</span>
          <span class="news-value-point">💡 谷歌正在推出一款“通用”双子座人工智能代理，可以在后台跨应用和设备工作</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1007732/atari-console-800xl-basic-personal-computer-retro-preorder" target="_blank" rel="noopener" data-cat="keji" data-summary="在复活了2600和美泰的Intellivision等标志性游戏机之后，雅达利重新推出了该品牌最初于43年前推出的一款个人电脑。800XL是对8位一体机PC的忠实再现，" data-title="Atari is bringing back one of its earliest 8" data-date="10-08 22:16" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-08 22:16</span>
          <span class="news-item-title">雅达利正在带回其最早的8款之一</span>
          <span class="news-item-title-en">Atari is bringing back one of its earliest 8</span>
          <span class="news-value-point">💡 在复活了2600和美泰的Intellivision等标志性游戏机之后，雅达利重新推出了该品牌最初于43年前推出的一款个人电脑</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/716.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 8 日消息，格罗方德（格芯，GF）今日宣布与台积电达成一项制造协议，旨在为台积电的 CoWoS® 先进封装生态系统建立基于美国的硅中介层供应。根据协议，GF 将向台积电提供制造服务，并在其位于纽约州马耳他的工厂增加产能。这项为期多年、价值 20 亿美元（IT之家注：现汇率约合 134.25 亿元人民币）的协议将扩大先进封装生态系统的产能，并满足人工智能和高性能计算技术日益增长的需求。该协议为随着客户需求增长而逐步扩大产能奠定了基础。GF 计划扩建其马耳他工厂的产能，并在美国建立首个硅中介层生产基地，以支持包括嵌入式深沟槽电容器组件在内的先进封装技术。新增的制造产能将为跨多代产品提供先进封装解决方案带来更大的规模和灵活性。“先进封装对于实现下一代人工智能系统所需的性能、po" data-title="格芯与台积电签署 20 亿美元协议，在美国建立首个硅中介层生产基地" data-date="10-08 22:15" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-08 22:15</span>
          <span class="news-item-title">格芯与台积电签署 20 亿美元协议，在美国建立首个硅中介层生产基地</span>
          <span class="news-value-point">💡 IT之家 10 月 8 日消息，格罗方德（格芯，GF）今日宣布与台积电达成一项制造协议，旨在为台积电的 CoWoS® 先进封装生态系统建立基于美…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/715.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 8 日消息，Amazon（亚马逊）当地时间今日正式发布了接替此前 Fire Tablet 系列的 Alexa Tablet 平板电脑。这些产品运行 Android 操作系统，可访问完整的 Google Play 商店。首批 Alexa Tablet 包括三款产品：Alexa Tablet 12 Pro、Alexa Tablet 11、Alexa Tablet 8。这些型号均拥有铝合金一体成型机身，都内置 Alexa+ 人工智能助手功能。Alexa Tablet 12 Pro 基于联发科技天玑 8400 处理器，配备 2800×1200 120Hz 屏幕（可选 AG 蚀刻玻璃的 Nanomatte 哑光版），内置 9000mAh 电池，拥有 12MP 后摄、8MP 前摄，支" data-title="亚马逊发布 Alexa Tablet 平板电脑：接替 Fire Tablet，全面支持 Alexa+ AI" data-date="10-08 22:14" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-08 22:14</span>
          <span class="news-item-title">亚马逊发布 Alexa Tablet 平板电脑：接替 Fire Tablet，全面支持 Alexa+ AI</span>
          <span class="news-value-point">💡 IT之家 10 月 8 日消息，Amazon（亚马逊）当地时间今日正式发布了接替此前 Fire Tablet 系列的 Alexa Tablet …</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/software-could-be-the-easiest-fix-for-hyperscalers-ai-power-squeeze-researchers-say-data-center-demand-is-expected-to-rival-japans-electricity-usage-by-2030" target="_blank" rel="noopener" data-cat="keji" data-summary="该行业正在花费数十亿美元用于更高效的芯片、冷却和电网连接。但是，如何让计算机做更少的工作--或者在更好的时间做？" data-title="Software could be the easiest fix for hyperscalers&#39; AI power squeeze, researchers say" data-date="10-08 22:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-08 22:00</span>
          <span class="news-item-title">研究人员表示，软件可能是超大规模人工智能最简单的解决方案</span>
          <span class="news-item-title-en">Software could be the easiest fix for hyperscalers' AI power squeeze, researchers say</span>
          <span class="news-value-point">💡 该行业正在花费数十亿美元用于更高效的芯片、冷却和电网连接</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/podcast/1007408/meta-muse-openai-dots-ai-agent-race-privacy-free" target="_blank" rel="noopener" data-cat="keji" data-summary="我今天的Decoder嘉宾是The Verge的高级AI记者Hayden Field ，我们正在讨论新一波消费者友好型AI代理。如果你一直关注这个领域，你知道人工智能爱好者已经使用智能体一分钟了--" data-title="Can you trust Meta’s Muse or OpenAI’s Dots to run your life?" data-date="10-08 22:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-08 22:00</span>
          <span class="news-item-title">你能相信Meta的Muse或OpenAI的Dots来管理你的生活吗？</span>
          <span class="news-item-title-en">Can you trust Meta’s Muse or OpenAI’s Dots to run your life?</span>
          <span class="news-value-point">💡 我今天的Decoder嘉宾是The Verge的高级AI记者Hayden Field ，我们正在讨论新一波消费者友好型AI代理</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/08/nyregion/mamdani-oct-7-anniversary-nyc-israel.html" target="_blank" rel="noopener" data-cat="keji" data-summary="在一些犹太领导人谴责市长佐赫兰·马姆达尼（ Zohran Mamdani ）关于袭击以色列的言论数小时后，活动人士打断了他的守夜活动，称他为巴勒斯坦事业的叛徒。" data-title="For Mamdani, Oct. 7 Anniversary Sets Off Anger and Bitterness" data-date="10-08 21:51" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-08 21:51</span>
          <span class="news-item-title">对于Mamdani来说， 10月7日的周年纪念掀起了愤怒和痛苦</span>
          <span class="news-item-title-en">For Mamdani, Oct. 7 Anniversary Sets Off Anger and Bitterness</span>
          <span class="news-value-point">💡 在一些犹太领导人谴责市长佐赫兰·马姆达尼（ Zohran Mamdani ）关于袭击以色列的言论数小时后，活动人士打断了他的守夜活动，称他为巴勒…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/ukrainian-drones-hit-russias-yandex-data-centers-housing-two-top-supercomputers-major-outage-follows-retaliatory-strike" target="_blank" rel="noopener" data-cat="keji" data-summary="俄罗斯不再提供人工智能培训？两台英伟达驱动的俄罗斯超级计算机的命运未知，因为无人机袭击了萨索沃的Yandex数据中心。" data-title="Ukrainian drones hit Russia&#39;s Yandex data centers housing two top supercomputers" data-date="10-08 21:46" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-08 21:46</span>
          <span class="news-item-title">乌克兰无人机袭击了俄罗斯的Yandex数据中心，该中心拥有两台顶级超级计算机</span>
          <span class="news-item-title-en">Ukrainian drones hit Russia's Yandex data centers housing two top supercomputers</span>
          <span class="news-value-point">💡 俄罗斯不再提供人工智能培训</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-08/10709332.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新社吉隆坡10月8日电 (记者 刘育英)马来西亚通信部8日披露，2025年1月1日至2026年9月15日期间，网络服务供应商应马来西亚通信和多媒体委员会(MCMC)要求，累计移除713项涉及政党领袖的人工智能(AI)深度伪造内容。" data-title="马来西亚下架713项涉政治人物AI深度伪造内容" data-date="10-08 21:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-08 21:00</span>
          <span class="news-item-title">马来西亚下架713项涉政治人物AI深度伪造内容</span>
          <span class="news-value-point">💡 中新社吉隆坡10月8日电 (记者 刘育英)马来西亚通信部8日披露，2025年1月1日至2026年9月15日期间，网络服务供应商应马来西亚通信和多…</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/502035.html" target="_blank" rel="noopener" data-cat="keji" data-summary="打造便利店“人机协作”运营新模式" data-title="正行创新亮相APRCE 2026，发布全球首个零售物理智能24/7服务解决方案" data-date="10-08 20:43" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-08 20:43</span>
          <span class="news-item-title">正行创新亮相APRCE 2026，发布全球首个零售物理智能24/7服务解决方案</span>
          <span class="news-value-point">💡 打造便利店“人机协作”运营新模式</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/amd-seeks-broader-partnership-with-samsung-as-it-looks-to-secure-memory-supply-samsung-reportedly-hopes-to-turn-its-memory-supply-relationship-with-amd-into-foundry-orders-for-logic-chips" target="_blank" rel="noopener" data-cat="keji" data-summary="AMD正在寻求与三星建立“更广泛的合作伙伴关系” ，因为内存公司希望将先进的内存供应与其代工部门的订单联系起来。" data-title="AMD seeks &#39;broader partnership&#39; with Samsung as it looks to secure memory supply" data-date="10-08 20:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-08 20:30</span>
          <span class="news-item-title">AMD寻求与三星建立“更广泛的合作伙伴关系” ，以确保内存供应</span>
          <span class="news-item-title-en">AMD seeks 'broader partnership' with Samsung as it looks to secure memory supply</span>
          <span class="news-value-point">💡 AMD正在寻求与三星建立“更广泛的合作伙伴关系” ，因为内存公司希望将先进的内存供应与其代工部门的订单联系起来</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/pc-gaming/researcher-develops-method-for-fingerprinting-cheaters-using-counter-strike-mouse-and-keyboard-input-patterns-says-technique-can-be-used-so-bans-follow-users-even-if-they-make-new-accounts" target="_blank" rel="noopener" data-cat="keji" data-summary="u/Magga_构建了一种方法，通过查看玩家如何使用鼠标和键盘来识别玩家。然后，他们可以使用此功能来确保禁令跟随作弊者，即使他们从另一台设备创建新帐户也是如此。" data-title="Researcher develops method for fingerprinting cheaters using Counter-Strike mouse and keyboard input patterns" data-date="10-08 20:10" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-08 20:10</span>
          <span class="news-item-title">研究人员开发了使用Counter-Strike鼠标和键盘输入模式对作弊者进行指纹识别的方法</span>
          <span class="news-item-title-en">Researcher develops method for fingerprinting cheaters using Counter-Strike mouse and keyboard input patterns</span>
          <span class="news-value-point">💡 u/Magga_构建了一种方法，通过查看玩家如何使用鼠标和键盘来识别玩家</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/cpus/amds-epyc-verano-ai-host-cpu-will-reportedly-use-a-special-sb1-socket-zen-6-chip-pairs-72-cores-with-a-24-channel-lpddr5x-memory-subsystem" target="_blank" rel="noopener" data-cat="keji" data-summary="Dynatron悄然推出了针对AI服务器的AMD EPYC “Verano” CPU的空气冷却器。" data-title="AMD&#39;s EPYC Verano AI host CPU will reportedly use a special SB1 socket" data-date="10-08 20:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-08 20:00</span>
          <span class="news-item-title">据报道， AMD的EPYC Verano AI主机CPU将使用特殊的SB1插槽</span>
          <span class="news-item-title-en">AMD's EPYC Verano AI host CPU will reportedly use a special SB1 socket</span>
          <span class="news-value-point">💡 Dynatron悄然推出了针对AI服务器的AMD EPYC “Verano” CPU的空气冷却器</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/502020.html" target="_blank" rel="noopener" data-cat="keji" data-summary="联想YOGA Pro 15 RTX Spark笔记本电脑，于10月8日9:00正式开启全网盲约。" data-title="搭载NVIDIA RTX Spark™ N1X超级芯片：联想YOGA Pro 15开启盲约，重塑个人生产力边界" data-date="10-08 18:23" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-08 18:23</span>
          <span class="news-item-title">搭载NVIDIA RTX Spark™ N1X超级芯片：联想YOGA Pro 15开启盲约，重塑个人生产力边界</span>
          <span class="news-value-point">💡 联想YOGA Pro 15 RTX Spark笔记本电脑，于10月8日9:00正式开启全网盲约</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">7 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/sport/live/2026/oct/08/football-qa-ask-ed-aarons-your-questions-as-the-premier-league-returns" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在经历了以曼城判决为主导的漫长国际休息之后，英超联赛将于周六回归。足球作家Ed Aarons现在在线回答您的问题登录或注册参加partpapalazaru提问：作为圣徒球迷，在" data-title="Football Q&amp;A: ask Ed Aarons your questions as the Premier League returns" data-date="10-08 22:47" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-08 22:47</span>
          <span class="news-item-title">足球问答：在英超回归之际向Ed Aarons提问</span>
          <span class="news-item-title-en">Football Q&A: ask Ed Aarons your questions as the Premier League returns</span>
          <span class="news-value-point">💡 在经历了以曼城判决为主导的漫长国际休息之后，英超联赛将于周六回归</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/video/2026/oct/08/manchester-city-liverpool-eckert-spygate-ban-too-lenient-football-weekly-video" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="马克斯·拉什登（ Max Rushden ）与巴里·格伦登宁（ Barry Glendenning ）、尼基·班迪尼（ Nicky Bandini ）和保罗·沃森（ Paul Watson ）一起，预览了英超联赛的回归，包括曼城自他们有罪判决以来的第一场比赛。" data-title="Manchester City go to Anfield and is Eckert’s Spygate ban too lenient? | Football Weekly video" data-date="10-08 19:56" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-08 19:56</span>
          <span class="news-item-title">曼城去安菲尔德，埃克特的Spygate禁令是否过于宽松？ |《足球周刊》视频</span>
          <span class="news-item-title-en">Manchester City go to Anfield and is Eckert’s Spygate ban too lenient? | Football Weekly video</span>
          <span class="news-value-point">💡 马克斯·拉什登（ Max Rushden ）与巴里·格伦登宁（ Barry Glendenning ）、尼基·班迪尼（ Nicky Bandin…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/audio/2026/oct/08/manchester-city-liverpool-premier-league-tonda-eckert-spygate-football-weekly-podcast" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="巴里·格伦登宁（ Barry Glendenning ）、尼基·班迪尼（ Nicky Bandini ）和保罗·沃森（ Paul Watson ）与马克斯·拉什登（ Max Rushden ）一起预览英超联赛价格的回归，查看、分享苹果播客，并通过电子邮件加入对话。今天的播客；英超联赛回归并解说" data-title="Manchester City’s trip to Anfield and is Eckert’s Spygate ban too lenient? – Football Weekly podcast" data-date="10-08 19:13" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-08 19:13</span>
          <span class="news-item-title">曼城的安菲尔德之旅以及埃克特的Spygate禁令是否过于宽松？ –《足球周刊》播客</span>
          <span class="news-item-title-en">Manchester City’s trip to Anfield and is Eckert’s Spygate ban too lenient? – Football Weekly podcast</span>
          <span class="news-value-point">💡 巴里·格伦登宁（ Barry Glendenning ）、尼基·班迪尼（ Nicky Bandini ）和保罗·沃森（ Paul Watson …</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/08/brighton-contenders-qualify-champions-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="他们是联盟中得分最高的球员，他们的进球差异最大，他们击败了冠军，没有丹尼·韦尔贝克（ Danny Welbeck ） ，在英超联赛中排名第三。布莱顿整个夏天都失去了一些最好的球员；" data-title="Are Brighton genuine contenders to qualify for the Champions League?" data-date="10-08 19:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-08 19:00</span>
          <span class="news-item-title">布莱顿的真正竞争者是否有资格参加欧洲冠军联赛？</span>
          <span class="news-item-title-en">Are Brighton genuine contenders to qualify for the Champions League?</span>
          <span class="news-value-point">💡 他们是联盟中得分最高的球员，他们的进球差异最大，他们击败了冠军，没有丹尼·韦尔贝克（ Danny Welbeck ） ，在英超联赛中排名第三</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/08/premier-league-injuries-kai-havertz-alexander-isak-patrick-dorgu" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英超俱乐部及其欧洲对手在艰苦的国际比赛休息后留下了一长串缺席者。四场比赛的国际比赛休息带来了压力测试。“我认为球队的强度，它的运动能力，真的，" data-title="Havertz, Isak, Dorgu … spate of injuries with national teams leaves sour taste for top clubs" data-date="10-08 16:50" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-08 16:50</span>
          <span class="news-item-title">Havertz、Isak、Dorgu……国家队的一系列伤病给顶级俱乐部留下了酸味</span>
          <span class="news-item-title-en">Havertz, Isak, Dorgu … spate of injuries with national teams leaves sour taste for top clubs</span>
          <span class="news-value-point">💡 英超俱乐部及其欧洲对手在艰苦的国际比赛休息后留下了一长串缺席者</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c9gkvx74je7do?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="消息人士告诉BBC Sport ， Declan Rice即将同意一份新的长期阿森纳合同。" data-title="Rice close to agreeing new Arsenal deal" data-date="10-08 06:21" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-08 06:21</span>
          <span class="news-item-title">赖斯接近达成新的阿森纳交易</span>
          <span class="news-item-title-en">Rice close to agreeing new Arsenal deal</span>
          <span class="news-value-point">💡 消息人士告诉BBC Sport ， Declan Rice即将同意一份新的长期阿森纳合同</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ck1l3gjpzz0qo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="仅仅五场比赛，对英超联赛表格给予太多关注似乎有点过早-但它可能比你想象的更稳定。BBC Sport查看了赛季初积分榜背后的统计数据。" data-title="Is it too early to look at Premier League table?" data-date="10-08 01:28" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-08 01:28</span>
          <span class="news-item-title">现在看英超桌还为时过早吗？</span>
          <span class="news-item-title-en">Is it too early to look at Premier League table?</span>
          <span class="news-value-point">💡 仅仅五场比赛，对英超联赛表格给予太多关注似乎有点过早-但它可能比你想象的更稳定</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/10/08/books/nobel-prize-literature.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这位作家加入了包括托妮·莫里森（ Toni Morrison ）、塞缪尔·贝克特（ Samuel Beckett ）和鲍勃·迪伦（ Bob D" data-title="Canadian Poet Anne Carson Is Awarded Nobel Prize in Literature" data-date="10-08 22:41" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-08 22:41</span>
          <span class="news-item-title">加拿大诗人安妮·卡森荣获诺贝尔文学奖</span>
          <span class="news-item-title-en">Canadian Poet Anne Carson Is Awarded Nobel Prize in Literature</span>
          <span class="news-value-point">💡 这位作家加入了包括托妮·莫里森（ Toni Morrison ）、塞缪尔·贝克特（ Samuel Beckett ）和鲍勃·迪伦（ Bob D</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/08/books/review/anne-carson-best-books.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这位加拿大诗人获得了今年的诺贝尔文学奖。如果您从未读过她的任何作品，这里是开始的地方。" data-title="New to Anne Carson’s Books? Start Here." data-date="10-08 22:40" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-08 22:40</span>
          <span class="news-item-title">不熟悉Anne Carson的书吗？从这里开始。</span>
          <span class="news-item-title-en">New to Anne Carson’s Books? Start Here.</span>
          <span class="news-value-point">💡 这位加拿大诗人获得了今年的诺贝尔文学奖</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/721.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 8 日消息，据界面新闻报道，10 月 8 日，懂车帝实测曝出尊界 V800 三次出现刹车踏板支架断裂，部分网友称节目内容系极端工况，驾驶员脚踩刹车踏板力度过大。懂车帝有关人员表示，百公里刹车实验并非极端工况，很多人在高速驾驶场景下都会遇到，是汽车实测最基本的科目之一。本次节目中出现的相关车型制动踏板支架断裂属首次出现，且连续三次实验在同一位置出现相似断裂现象，存在一定安全隐患。针对三辆测试车刹车踏板支架断裂时显示的踏板力，懂车帝方面表示，网传暴力测试并不存在，而是正常的刹车踏板大力制动。网友关注的“4589N”踏板力数值，实为高速摄像机拍摄实验画面时，因摄像机与检测设备的液晶屏刷新帧率不同，拍摄到的液晶屏数字跳动出现残影，真实峰值数据为 1612N，踏板力在达到峰值后迅速" data-title="懂车帝回应尊界 V800 刹车踏板支架断裂争议：网传暴力测试并不存在，百公里刹车实验并非极端工况" data-date="10-08 22:39" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-08 22:39</span>
          <span class="news-item-title">懂车帝回应尊界 V800 刹车踏板支架断裂争议：网传暴力测试并不存在，百公里刹车实验并非极端工况</span>
          <span class="news-value-point">💡 IT之家 10 月 8 日消息，据界面新闻报道，10 月 8 日，懂车帝实测曝出尊界 V800 三次出现刹车踏板支架断裂，部分网友称节目内容系极…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/720.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 8 日消息，澳大利亚政府公平工作监察员办公室（FWO）昨天在 Instagram 平台发文，教导用完带薪假期的人如何请假玩上《GTA6》。IT之家了解到，这份略带“整活”的指南阐述了澳大利亚无薪休假法律运作方式，并说明员工何时能够依法享有无薪休假权利，以及雇主如何审批这些申请。“假设《侠盗猎车手 VI》明天就要发售，但你已经没有带薪休假可以首发当天玩上。那么，你可以申请无薪休假吗？”该指南写道。根据《国家就业标准》法律，澳大利亚民众确实享有无薪休假权利。考虑申请时，你需要扪心自问：“我为什么需要请假。”该文指出，如果员工已经用完带薪休假，又需要照顾生病或受伤的家庭成员时，可以申请最多两天的无薪照护假。这段说明还配上了一张诙谐图片：一名儿童正在接受体温检查，但孩子的脸被替换" data-title="澳大利亚政府“整活”，教群众怎么申请无薪假期首发玩上《GTA6》" data-date="10-08 22:38" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-08 22:38</span>
          <span class="news-item-title">澳大利亚政府“整活”，教群众怎么申请无薪假期首发玩上《GTA6》</span>
          <span class="news-value-point">💡 IT之家 10 月 8 日消息，澳大利亚政府公平工作监察员办公室（FWO）昨天在 Instagram 平台发文，教导用完带薪假期的人如何请假玩上…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1007804/october-prime-day-leftover-deals" target="_blank" rel="noopener" data-cat="zonghe" data-summary="当如此众多的交易在亚马逊大型销售的“结束”中幸存下来时，总是有点尴尬。尽管如此，我很高兴地说，大多数销售最热门的交易仍然存在—苹果对其Mac Mini ， MacB的折扣" data-title="75 great October Prime Day deals are still happening" data-date="10-08 22:28" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-08 22:28</span>
          <span class="news-item-title">75个很棒的10月黄金日优惠仍在发生</span>
          <span class="news-item-title-en">75 great October Prime Day deals are still happening</span>
          <span class="news-value-point">💡 当如此众多的交易在亚马逊大型销售的“结束”中幸存下来时，总是有点尴尬</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/719.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 8 日消息，KIOXIA（铠侠）当地时间今日发布了其首款采用 EDSFF E1.L“尺”外形规格的固态硬盘产品 —— LD4。该系列基于第八代 (218L) BiCS FLASH QLC NAND 闪存。KIOXIA LD4 系列专为高密度 1U 服务器和读取密集型存储应用而设计，目标用户为超大规模数据中心级工作负载和横向扩展 (scale-out) 环境。其采用 PCIe Gen5 ×4 接口，符合 NVMe 2.0e、OCP 数据中心 NVMe SSD 2.6 规范，当前提供 15.36TB 和 30.72TB 两种容量，未来可扩展至 122.88TB。铠侠现已向特定客户交付 LD4 系列的样品，这款 SSD 也将在本月中旬的 2026 OCP 全球峰会上展出。" data-title="铠侠首款 EDSFF E1.L 外形规格固态硬盘 LD4 发布，采用 BiCS8 QLC 闪存" data-date="10-08 22:27" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-08 22:27</span>
          <span class="news-item-title">铠侠首款 EDSFF E1.L 外形规格固态硬盘 LD4 发布，采用 BiCS8 QLC 闪存</span>
          <span class="news-value-point">💡 IT之家 10 月 8 日消息，KIOXIA（铠侠）当地时间今日发布了其首款采用 EDSFF E1.L“尺”外形规格的固态硬盘产品 —— LD4</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/718.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 8 日消息，华为干昆智能汽车解决方案今日发布了 9 月安全出行报告。数据显示，华为干昆累计辅助驾驶里程 157.85 亿公里、辅助驾驶月活用户占比 94.6%。另外，人驾状态下月度防御性驾驶触发次数 2.64 万次、便捷缴费使用次数 142.3 万次。IT之家查询华为干昆官网获悉，干昆智驾累计辅助驾驶里程截至目前已突破 164 亿公里，搭载干昆智驾车辆累计行驶总里程也已突破 461 亿公里。" data-title="华为干昆 9 月安全出行报告发布，辅助驾驶月活用户占比达 94.6%" data-date="10-08 22:16" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-08 22:16</span>
          <span class="news-item-title">华为干昆 9 月安全出行报告发布，辅助驾驶月活用户占比达 94.6%</span>
          <span class="news-value-point">💡 IT之家 10 月 8 日消息，华为干昆智能汽车解决方案今日发布了 9 月安全出行报告</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-08/10709401.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="当地时间10月8日下午，长春2027第33届世界大学生冬季运动会(以下简称“长春大冬会”)火种采集仪式在意大利北部城市都灵举行，赛事火种成功采集。" data-title="2027长春大冬会火种在意大利都灵成功采集" data-date="10-08 22:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-08 22:13</span>
          <span class="news-item-title">2027长春大冬会火种在意大利都灵成功采集</span>
          <span class="news-value-point">💡 当地时间10月8日下午，长春2027第33届世界大学生冬季运动会(以下简称“长春大冬会”)火种采集仪式在意大利北部城市都灵举行，赛事火种成功采集</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/3d-printing/bambu-labs-3d-printing-patent-application-for-a-new-heatbed-design-may-improve-peeling-issues-replacement-costs-could-possibly-rise-as-a-consequence" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Bambu Lab申请了其新型加热床设计的专利，该设计可能最终解决大型印刷品的床粘附问题。" data-title="Bambu Lab’s 3D printing patent application for a new heatbed design may improve peeling issues" data-date="10-08 22:11" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-08 22:11</span>
          <span class="news-item-title">Bambu Lab针对新型加热床设计的3D打印专利申请可能会改善剥离问题</span>
          <span class="news-item-title-en">Bambu Lab’s 3D printing patent application for a new heatbed design may improve peeling issues</span>
          <span class="news-value-point">💡 Bambu Lab申请了其新型加热床设计的专利，该设计可能最终解决大型印刷品的床粘附问题</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/010/714.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 8 日消息，据科技媒体 Android Headline 今天报道，谷歌似乎在为 Pixel 系列手机开发“Face Active Illumination”功能，可利用屏幕发出的光照亮人脸，改善暗光环境下的人脸解锁体验。据报道，谷歌 Pixel 手机的人脸解锁功能在环境光良好的情况下表现尚可，当用户进入光线昏暗的房间时，它就显得力不从心。如今，Android 17 QPR3 Beta 1 系统已经留下一些代码痕迹，表明谷歌正在优化人脸解锁算法。据悉，该功能可以在屏幕亮起时提高亮度，照亮用户脸部来提升解锁速度，其中还带有一个控制亮度等级的选项。不过由于该功能暂未开发完成，因此没有太多功能可以展示。据此前的传闻，谷歌正在探索红外技术，因此 Pixel 新机未来可能会配备更先" data-title="谷歌为 Pixel 手机开发新人脸解锁算法，改善暗光环境解锁体验" data-date="10-08 22:08" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-08 22:08</span>
          <span class="news-item-title">谷歌为 Pixel 手机开发新人脸解锁算法，改善暗光环境解锁体验</span>
          <span class="news-value-point">💡 IT之家 10 月 8 日消息，据科技媒体 Android Headline 今天报道，谷歌似乎在为 Pixel 系列手机开发“Face Act…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-08/10709391.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网成都10月8日电 (记者 安源)成都市公安局金堂县公安局8日发布警情通报称，网传“金堂县某小区楼顶发现可疑骨头”引发关注。经检验，现场发现的骨骼、牙齿均为非人类骨骼及牙齿；相关传言系小区住户刘某某(男，73岁)虚构捏造，其已被公安机关依法予以行政处罚。" data-title="成都金堂警方通报“小区楼顶可疑骨头”：均非人类骨骼 造谣者被行政处罚" data-date="10-08 22:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-08 22:03</span>
          <span class="news-item-title">成都金堂警方通报“小区楼顶可疑骨头”：均非人类骨骼 造谣者被行政处罚</span>
          <span class="news-value-point">💡 中新网成都10月8日电 (记者 安源)成都市公安局金堂县公安局8日发布警情通报称，网传“金堂县某小区楼顶发现可疑骨头”引发关注</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1007565/amazon-alexa-plus-review-one-year-echo-show-dot-max" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在Alexa Plus可以做的所有事情中，我从未想过它会让我哭泣。自从我儿子上大学以来，我办公室的Echo Show一直在拍摄当时和现在的照片：蹒跚学步的孩子，他的第一个网球拍在他的校队队长旁边" data-title="Alexa Plus is better at running my home, but it’s not ready to run my life" data-date="10-08 22:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-08 22:00</span>
          <span class="news-item-title">Alexa Plus更擅长管理我的房源，但它还没有准备好管理我的生活</span>
          <span class="news-item-title-en">Alexa Plus is better at running my home, but it’s not ready to run my life</span>
          <span class="news-value-point">💡 在Alexa Plus可以做的所有事情中，我从未想过它会让我哭泣</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/08/5-days-to-techcrunch-disrupt-2026-dont-pay-more-at-the-door/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="全球科技生态系统将于10月13日至15日在旧金山Moscone West举行的TechCrunch Disrupt 2026大会上齐聚一堂。立即获取通行证，最多可节省$ 100。获取相同工单类型的第二张，可节省50%。" data-title="5 days to TechCrunch Disrupt 2026: Don’t pay more at the door for your pass" data-date="10-08 22:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-08 22:00</span>
          <span class="news-item-title">距离TechCrunch Disrupt 2026还有5天：不要在门口为通行证支付更多费用</span>
          <span class="news-item-title-en">5 days to TechCrunch Disrupt 2026: Don’t pay more at the door for your pass</span>
          <span class="news-value-point">💡 全球科技生态系统将于10月13日至15日在旧金山Moscone West举行的TechCrunch Disrupt 2026大会上齐聚一堂</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/08/cal-ais-19-year-old-founder-just-raised-10m-for-his-new-ai-startup/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="受欢迎的Cal AI卡路里跟踪应用程序的青少年联合创始人Zach Yadegari推出了一家新的个人AI代理初创公司，与Instinct、Muse和Bee竞争。" data-title="Cal AI’s 19-year-old founder just raised $10M for his new AI startup" data-date="10-08 22:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-08 22:00</span>
          <span class="news-item-title">Cal AI的19岁创始人刚刚为他的新人工智能初创公司筹集了1000万美元$</span>
          <span class="news-item-title-en">Cal AI’s 19-year-old founder just raised $10M for his new AI startup</span>
          <span class="news-value-point">💡 受欢迎的Cal AI卡路里跟踪应用程序的青少年联合创始人Zach Yadegari推出了一家新的个人AI代理初创公司，与Instinct、Mus…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1007786/artificial-is-a-wicked-satire-that-also-sticks-to-the-facts" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在纽约电影节首映的人工，卢卡瓜达尼诺的讽刺山姆奥尔特曼传记片，导演在舞台上说： “[当]有人想扮演上帝，这对我来说非常有趣。“扮演上帝的想法，以及一般的权力-谁" data-title="Artificial is a wicked satire that also sticks to the facts" data-date="10-08 22:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-08 22:00</span>
          <span class="news-item-title">人工讽刺是一种邪恶的讽刺，也坚持事实</span>
          <span class="news-item-title-en">Artificial is a wicked satire that also sticks to the facts</span>
          <span class="news-value-point">💡 在纽约电影节首映的人工，卢卡瓜达尼诺的讽刺山姆奥尔特曼传记片，导演在舞台上说： “[当]有人想扮演上帝，这对我来说非常有趣</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-08 22:46（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
