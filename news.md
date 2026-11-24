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
      <span>2026-11-24 19:43 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×21 · 天空体育×13</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">按来源聚合 · 最近 24 小时精选</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/11-24/10737069.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月24日电 据甘肃省纪委监委消息：日前，经甘肃省委批准，甘肃省纪委监委对甘肃省人大环境资源保护委员会原副主任委员苏跃华严重违纪违法问题进行了立案审查调查。" data-title="甘肃省人大环境资源保护委员会原副主任委员苏跃华被“双开”" data-date="11-24 19:39" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 11-24 19:39</span>
      </div>
      <h2 class="hero-featured-title">甘肃省人大环境资源保护委员会原副主任委员苏跃华被“双开”</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/031/818.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 24 日消息，随着 2026 年小鹏科技日临近，小鹏汽车于今日公布了旗下人形机器人 IRON 的最新预热视频。短片重点展现了该机器人在无人工遥控状态下，独立完成多项贴近日常生活的精细化任务，为即将召开的科技日提前造势。IT之家注意到，根据此次公开的画面，IRON 在模拟居家环境中成功执行了抓取书籍、向杯中斟酒以及自主连接电源充电等一系列操作。据介绍，上述操作并非依赖预设程序或后台人工干预，而是完全依托大模型的驱动，由机器人自主完成对指令的理解、环境判断与动作执行。2026 年小鹏科技日定于 11 月 25 日 14:00 举办，本届活动以“原点 Origin”为核心主题，小鹏将在会上集中阐述其对物理 AI 未来演进阶段的战略研判。届时，升级后的机器人 IRON 也将登台亮" data-title="小鹏放出 IRON 人形机器人预热视频：可自主拿起书本、倒酒、充电" data-date="11-24 19:46" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">小鹏放出 IRON 人形机器人预热视频：可自主拿起书本、倒酒、充电</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/football/news/12040/13615599/wolves-hit-their-stride-stoke-continue-to-dream-but-can-they-last-the-course-and-are-qpr-dark-horses-of-championship" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Wolves are clicking, Stoke are dreaming - but could QPR be dark horses?" data-title="Wolves are clicking, Stoke are dreaming - but could QPR be dark horses?" data-date="11-24 15:00" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">Wolves are clicking, Stoke are dreaming - but could QPR be dark horses?</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/11-24/10737137.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="开幕式现场。大会主办方供图 中新网杭州11月24日电(王逸飞 吴君毅)24日，“2026中外青年商界菁英大会”在浙江省杭州市开幕。" data-title="“2026中外青年商界菁英大会”在杭州开幕" data-date="11-24 19:41" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">“2026中外青年商界菁英大会”在杭州开幕</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-24/10737069.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月24日电 据甘肃省纪委监委消息：日前，经甘肃省委批准，甘肃省纪委监委对甘肃省人大环境资源保护委员会原副主任委员苏跃华严重违纪违法问题进行了立案审查调查。" data-title="甘肃省人大环境资源保护委员会原副主任委员苏跃华被“双开”" data-date="11-24 19:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 19:39</span>
          <span class="news-item-title">甘肃省人大环境资源保护委员会原副主任委员苏跃华被“双开”</span>
          <span class="news-value-point">💡 中新网11月24日电 据甘肃省纪委监委消息：日前，经甘肃省委批准，甘肃省纪委监委对甘肃省人大环境资源保护委员会原副主任委员苏跃华严重违纪违法问题…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-24/10737132.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网广州11月24日电 (记者 方伟彬)记者24日从广州南沙法院获悉，日前，广州国际商事法庭巡回审判首案在南沙法院涉外和商事审判中心开庭审理并当庭宣判。这是继广州知识产权法院南沙法庭进驻后，又一专业司法资源集聚南沙的标志性成果。" data-title="广州国际商事法庭巡回审判“首槌”落定南沙" data-date="11-24 19:38" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 19:38</span>
          <span class="news-item-title">广州国际商事法庭巡回审判“首槌”落定南沙</span>
          <span class="news-value-point">💡 中新网广州11月24日电 (记者 方伟彬)记者24日从广州南沙法院获悉，日前，广州国际商事法庭巡回审判首案在南沙法院涉外和商事审判中心开庭审理并…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-24/10737144.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京11月24日电#8195;中央政治局委员、上海市委书记陈吉宁涉嫌严重违纪违法，目前正接受中央纪委国家监委审查调查。" data-title="陈吉宁涉嫌严重违纪违法正接受中央纪委国家监委审查调查" data-date="11-24 19:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 19:31</span>
          <span class="news-item-title">陈吉宁涉嫌严重违纪违法正接受中央纪委国家监委审查调查</span>
          <span class="news-value-point">💡 新华社北京11月24日电#8195;中央政治局委员、上海市委书记陈吉宁涉嫌严重违纪违法，目前正接受中央纪委国家监委审查调查</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-24/10737143.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="印度尼西亚万丹省警方24日证实，该省一家糖果厂21日发生的火灾已造成26人死亡，另有8人失踪。当地官员称，起火点可能是涉事建筑二楼的一台冷却装置。" data-title="印尼糖果厂火灾已致26人死亡 警方展开刑事调查" data-date="11-24 19:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 19:22</span>
          <span class="news-item-title">印尼糖果厂火灾已致26人死亡 警方展开刑事调查</span>
          <span class="news-value-point">💡 印度尼西亚万丹省警方24日证实，该省一家糖果厂21日发生的火灾已造成26人死亡，另有8人失踪</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-24/10737139.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="11月24日，中央纪委国家监委公布了2026年10月全国查处违反中央八项规定精神问题汇总情况。当月，全国共查处违反中央八项规定精神问题28934起，批评教育和处理35193人，其中党纪政务处分23996人，这是连续第158个月公布月报数据。" data-title="2026年10月全国查处违反中央八项规定精神问题28934起" data-date="11-24 19:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 19:05</span>
          <span class="news-item-title">2026年10月全国查处违反中央八项规定精神问题28934起</span>
          <span class="news-value-point">💡 11月24日，中央纪委国家监委公布了2026年10月全国查处违反中央八项规定精神问题汇总情况</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-24/10737028.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月24日电(记者 刁炜)第十六届珠海航展开幕在即，据有关方面介绍，阿联酋空军“骑士”飞行表演队将来华参展。" data-title="L-15E即将“回娘家”，这款中国造教练机何以享誉世界" data-date="11-24 18:51" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 18:51</span>
          <span class="news-item-title">L-15E即将“回娘家”，这款中国造教练机何以享誉世界</span>
          <span class="news-value-point">💡 中新网11月24日电(记者 刁炜)第十六届珠海航展开幕在即，据有关方面介绍，阿联酋空军“骑士”飞行表演队将来华参展</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-24/10737115.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社柏林11月24日电 德国国防部长皮斯托里乌斯23日在柏林表示，德国未来将在本国为乌克兰生产无人机，并将提供约3400万欧元支持相关生产能力建设。这是德乌两国进一步深化军事合作的新举措。" data-title="德国防长：德国未来将在本国为乌克兰生产无人机" data-date="11-24 18:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 18:49</span>
          <span class="news-item-title">德国防长：德国未来将在本国为乌克兰生产无人机</span>
          <span class="news-value-point">💡 中新社柏林11月24日电 德国国防部长皮斯托里乌斯23日在柏林表示，德国未来将在本国为乌克兰生产无人机，并将提供约3400万欧元支持相关生产能力…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-24/10737116.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月24日电 (记者 张素)记者从中国最高人民法院获悉，11月24日，山东省淄博市中级人民法院一审公开宣判贵州省委原常委、毕节市委原书记吴胜华受贿案。" data-title="贵州省委原常委、毕节市委原书记吴胜华一审被判无期徒刑" data-date="11-24 18:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 18:48</span>
          <span class="news-item-title">贵州省委原常委、毕节市委原书记吴胜华一审被判无期徒刑</span>
          <span class="news-value-point">💡 中新社北京11月24日电 (记者 张素)记者从中国最高人民法院获悉，11月24日，山东省淄博市中级人民法院一审公开宣判贵州省委原常委、毕节市委原…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-24/10737067.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社广州11月24日电 (记者 陈建新)全国人大常委会委员、全国台联会长郑建闽24日在广州呼吁广大台胞乡亲在推进中国式现代化建设中发挥更大作用，在融入祖国大陆发展大局中实现自身更好发展。" data-title="台湾省全国人大代表赴广东调研" data-date="11-24 17:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 17:28</span>
          <span class="news-item-title">台湾省全国人大代表赴广东调研</span>
          <span class="news-value-point">💡 中新社广州11月24日电 (记者 陈建新)全国人大常委会委员、全国台联会长郑建闽24日在广州呼吁广大台胞乡亲在推进中国式现代化建设中发挥更大作用…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-24/10737070.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月24日电 据路透社23日报道，印度食品安全与标准局在印度知名瓶装饮用水生产商比斯莱里国际公司的产品样本中检出不符合安全标准的物质，将对这家公司启动法律程序并扩大抽检范围。" data-title="印度知名瓶装水品牌曝出安全问题" data-date="11-24 17:18" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 17:18</span>
          <span class="news-item-title">印度知名瓶装水品牌曝出安全问题</span>
          <span class="news-value-point">💡 中新网11月24日电 据路透社23日报道，印度食品安全与标准局在印度知名瓶装饮用水生产商比斯莱里国际公司的产品样本中检出不符合安全标准的物质，将…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-24/10737038.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网东京11月24日电 (记者 朱晨曦)据日本广播协会报道，日本立宪民主党、国民民主党等在参议院拥有席位的在野党24日举行会谈后决定，针对文部科学大臣关芳弘向参议院提交问责决议案，要求其辞职。" data-title="日本在野党决定问责并要求文部科学大臣辞职" data-date="11-24 17:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 17:12</span>
          <span class="news-item-title">日本在野党决定问责并要求文部科学大臣辞职</span>
          <span class="news-value-point">💡 中新网东京11月24日电 (记者 朱晨曦)据日本广播协会报道，日本立宪民主党、国民民主党等在参议院拥有席位的在野党24日举行会谈后决定，针对文部…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-24/10737017.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月24日电 阿布扎比消息：阿联酋内政部24日发表声明称，该国哈伊马角酋长国发生一起客运巴士与卡车相撞事故，已造成11人死亡。" data-title="阿联酋哈伊马角酋长国发生车祸已致11死" data-date="11-24 17:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 17:12</span>
          <span class="news-item-title">阿联酋哈伊马角酋长国发生车祸已致11死</span>
          <span class="news-value-point">💡 中新社北京11月24日电 阿布扎比消息：阿联酋内政部24日发表声明称，该国哈伊马角酋长国发生一起客运巴士与卡车相撞事故，已造成11人死亡</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-24/10737043.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月24日电 综合伊朗媒体报道，一名伊朗司法部门官员表示，伊朗法院已裁定美国须支付2900亿美元赔偿金，以弥补美以联合对伊朗发动军事行动期间以及更早时期造成的损失。" data-title="伊媒：伊朗法院已裁定，美国须支付2900亿美元赔偿金" data-date="11-24 16:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 16:49</span>
          <span class="news-item-title">伊媒：伊朗法院已裁定，美国须支付2900亿美元赔偿金</span>
          <span class="news-value-point">💡 中新网11月24日电 综合伊朗媒体报道，一名伊朗司法部门官员表示，伊朗法院已裁定美国须支付2900亿美元赔偿金，以弥补美以联合对伊朗发动军事行动…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-24/10736745.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="据中国载人航天工程办公室介绍，空间站应用与发展阶段飞行任务总指挥部定于北京时间11月24日上午9时，在酒泉卫星发射中心召开神舟二十四号载人飞行任务新闻发布会，通报此次任务有关情况。" data-title="神舟二十四号载人飞行任务新闻发布会将于今天上午召开" data-date="11-24 08:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 08:01</span>
          <span class="news-item-title">神舟二十四号载人飞行任务新闻发布会将于今天上午召开</span>
          <span class="news-value-point">💡 据中国载人航天工程办公室介绍，空间站应用与发展阶段飞行任务总指挥部定于北京时间11月24日上午9时，在酒泉卫星发射中心召开神舟二十四号载人飞行任…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-24/10736742.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月24日电 据路透社报道，当地时间23日，美国总统特朗普表示，已命令美军暂停推进在艾奥瓦州引爆68桶有毒含铅化合物的计划。" data-title="特朗普下令：暂停美军在艾奥瓦州引爆有毒化学物质" data-date="11-24 07:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 07:48</span>
          <span class="news-item-title">特朗普下令：暂停美军在艾奥瓦州引爆有毒化学物质</span>
          <span class="news-value-point">💡 中新网11月24日电 据路透社报道，当地时间23日，美国总统特朗普表示，已命令美军暂停推进在艾奥瓦州引爆68桶有毒含铅化合物的计划</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/031/818.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 24 日消息，随着 2026 年小鹏科技日临近，小鹏汽车于今日公布了旗下人形机器人 IRON 的最新预热视频。短片重点展现了该机器人在无人工遥控状态下，独立完成多项贴近日常生活的精细化任务，为即将召开的科技日提前造势。IT之家注意到，根据此次公开的画面，IRON 在模拟居家环境中成功执行了抓取书籍、向杯中斟酒以及自主连接电源充电等一系列操作。据介绍，上述操作并非依赖预设程序或后台人工干预，而是完全依托大模型的驱动，由机器人自主完成对指令的理解、环境判断与动作执行。2026 年小鹏科技日定于 11 月 25 日 14:00 举办，本届活动以“原点 Origin”为核心主题，小鹏将在会上集中阐述其对物理 AI 未来演进阶段的战略研判。届时，升级后的机器人 IRON 也将登台亮" data-title="小鹏放出 IRON 人形机器人预热视频：可自主拿起书本、倒酒、充电" data-date="11-24 19:46" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-24 19:46</span>
          <span class="news-item-title">小鹏放出 IRON 人形机器人预热视频：可自主拿起书本、倒酒、充电</span>
          <span class="news-value-point">💡 IT之家 11 月 24 日消息，随着 2026 年小鹏科技日临近，小鹏汽车于今日公布了旗下人形机器人 IRON 的最新预热视频</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/dram/shared-cxl-memory-pools-come-with-steep-software-tax-that-could-stall-multi-server-scaling-ut-arlington-shares-real-world-test-that-measured-four-servers-sharing-the-same-pool-at-sc26" target="_blank" rel="noopener" data-cat="keji" data-summary="德州大学阿灵顿分校和英特尔在一个真实的四主机共享CXL内存池上测量了软件同步成本，因为供应商正在关注CXL用于AI KV缓存。" data-title="Shared CXL memory comes with a software tax — a real four-server test found locks cost 3–5 µs each" data-date="11-24 19:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-24 19:30</span>
          <span class="news-item-title">共享 CXL 内存附带软件开销——一项真正的四服务器测试发现，每次锁定的开销为 3–5 微秒</span>
          <span class="news-item-title-en">Shared CXL memory comes with a software tax — a real four-server test found locks cost 3–5 µs each</span>
          <span class="news-value-point">💡 德州大学阿灵顿分校和英特尔在一个真实的四主机共享CXL内存池上测量了软件同步成本，因为供应商正在关注CXL用于AI KV缓存</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/japan-puts-chipmaking-labs-inside-trucks-with-mobilefab-trucks-pack-30-cm-lithography-gear-to-tackle-a-10-year-semiconductor-engineer-shortage" target="_blank" rel="noopener" data-cat="keji" data-summary="日本的芯片制造教育计划借助mobileFab得以推进——车载光刻机让各地的学生都能进行芯片布线图案化" data-title="Japan puts chipmaking labs inside trucks with mobileFab" data-date="11-24 19:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-24 19:30</span>
          <span class="news-item-title">日本将芯片制造实验室装入卡车，打造mobileFab</span>
          <span class="news-item-title-en">Japan puts chipmaking labs inside trucks with mobileFab</span>
          <span class="news-value-point">💡 日本的芯片制造教育计划借助mobileFab得以推进——车载光刻机让各地的学生都能进行芯片布线图案化</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/desktops/gaming-pcs/grab-a-4k-ready-cyberpowerpc-gaming-rig-with-a-7800x3d-and-rtx-5070-for-usd2-099-99-newegg-knocks-usd130-off-this-liquid-cooled-desktop-with-32gb-ddr5-and-a-1tb-ssd" target="_blank" rel="noopener" data-cat="keji" data-summary="Grab this powerful CyberPowerPC gaming rig with an AMD Ryzen 7 7800X3D and Nvidia GeForce RTX 5070 for $2,099.99." data-title="Grab a 4K-ready CyberPowerPC gaming rig with a 7800X3D and RTX 5070 for $2,099.99" data-date="11-24 19:21" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-24 19:21</span>
          <span class="news-item-title">Grab a 4K-ready CyberPowerPC gaming rig with a 7800X3D and RTX 5070 for $2,099.99</span>
          <span class="news-value-point">💡 Grab this powerful CyberPowerPC gaming rig with an AMD Ryzen 7 7800X3D a…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/031/811.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 24 日消息，据 Axios 报道，二十多名熟悉内部讨论的消息人士透露，Anthropic 和 OpenAI 正面临一个愈发紧迫的难题：公司内部尚未对外发布的模型能力已经强到让不少员工认为，这些模型无法安全向公众开放。消息人士表示，这件事的影响不容小觑。顶尖人工智能系统的能力和人类的管控能力之间的差距持续拉大，很可能大幅放缓人工智能的发展热潮。研究人员至今还没有找到管控最强模型的技术方案。部分内部人员认为这个问题有解决办法，也有人并不看好，提出企业应当彻底停止训练新模型。头部人工智能企业的负责人早就预判，这项技术终有一天会在几乎所有领域远超人类智力。虽然内部模型还没有抵达这个临界点，但 OpenAI 和 Anthropic 近期取得的突破已经让研究人员感到震惊。消息人士称" data-title="消息称 OpenAI 与 Anthropic 员工警告：内部 AI 模型能力过于强大，无法安全发布" data-date="11-24 19:18" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-24 19:18</span>
          <span class="news-item-title">消息称 OpenAI 与 Anthropic 员工警告：内部 AI 模型能力过于强大，无法安全发布</span>
          <span class="news-value-point">💡 IT之家 11 月 24 日消息，据 Axios 报道，二十多名熟悉内部讨论的消息人士透露，Anthropic 和 OpenAI 正面临一个愈发…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/nvidia-engineer-that-quit-in-response-to-jensen-huang-resignation-welcomes-ceo-back-i-may-have-moved-too-quickly-says-robotics-engineer-who-made-viral-post" target="_blank" rel="noopener" data-cat="keji" data-summary="An Nvidia robotics engineer that quit in response to Jensen Huang&#39;s resignation says he &quot;may have moved too quickly&quot; now that CEO is back in charge." data-title="Nvidia engineer who quit over Jensen Huang&#39;s exit says he &#39;may have moved too quickly&#39;" data-date="11-24 19:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-24 19:00</span>
          <span class="news-item-title">Nvidia engineer who quit over Jensen Huang's exit says he 'may have moved too quickly'</span>
          <span class="news-value-point">💡 An Nvidia robotics engineer that quit in response to Jensen Huang's resi…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-24/10737136.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网11月24日电(管娜)短短11天，黄仁勋实现了“东山再起”。当地时间11月23日，英伟达宣布恢复黄仁勋总裁、首席执行官及董事会成员职务。消息公布后，美国消费者新闻与商业频道(CNBC)连线美国总统特朗普，就此事进行采访。" data-title="11天大反转：特朗普专访谈黄仁勋回归，事件走向还有哪些内幕？" data-date="11-24 18:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 18:54</span>
          <span class="news-item-title">11天大反转：特朗普专访谈黄仁勋回归，事件走向还有哪些内幕？</span>
          <span class="news-value-point">💡 中新网11月24日电(管娜)短短11天，黄仁勋实现了“东山再起”</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/512451.html" target="_blank" rel="noopener" data-cat="keji" data-summary="蚂蚁刚刚发布医疗健康模型全家桶" data-title="蚂蚁开源医疗健康预测模型，根据睡眠数据可预测未来六年150种疾病风险" data-date="11-24 18:15" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-24 18:15</span>
          <span class="news-item-title">蚂蚁开源医疗健康预测模型，根据睡眠数据可预测未来六年150种疾病风险</span>
          <span class="news-value-point">💡 蚂蚁刚刚发布医疗健康模型全家桶</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/24/business/nvidia-alice-huang-china.html" target="_blank" rel="noopener" data-cat="keji" data-summary="The woman whose role has become a focus of the Nvidia spying saga grew up in a small town built around a weapons factory. Her jump to finance and the tech world paralleled China’s own." data-title="From Chinese Factory Town to the Nvidia Scandal: The Rise of Alice Huang" data-date="11-24 18:03" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-24 18:03</span>
          <span class="news-item-title">From Chinese Factory Town to the Nvidia Scandal: The Rise of Alice Huang</span>
          <span class="news-value-point">💡 The woman whose role has become a focus of the Nvidia spying saga grew u…</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/512362.html" target="_blank" rel="noopener" data-cat="keji" data-summary="端侧老炮辛米尔，打通物理AI规模化落地之路" data-title="业界首提“端侧超节点”，让端侧AI组队计算：AI效率暴涨270%，不用换芯片或模型" data-date="11-24 14:35" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-24 14:35</span>
          <span class="news-item-title">业界首提“端侧超节点”，让端侧AI组队计算：AI效率暴涨270%，不用换芯片或模型</span>
          <span class="news-value-point">💡 端侧老炮辛米尔，打通物理AI规模化落地之路</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/512354.html" target="_blank" rel="noopener" data-cat="keji" data-summary="文心 5.5 Flash Preview正式开源，采用 Apache 2.0 协议" data-title="文心 5.5 Flash Preview正式开源，采用 Apache 2.0 协议" data-date="11-24 14:22" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-24 14:22</span>
          <span class="news-item-title">文心 5.5 Flash Preview正式开源，采用 Apache 2.0 协议</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/23/us/politics/trump-nvidia-national-security.html" target="_blank" rel="noopener" data-cat="keji" data-summary="President Trump’s move to put Jensen Huang back at the helm of Nvidia caps his indifference to the warnings of his own intelligence agencies." data-title="Trump’s Extraordinary Nvidia Intervention Sidelines National Security Concerns" data-date="11-24 08:55" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-24 08:55</span>
          <span class="news-item-title">Trump’s Extraordinary Nvidia Intervention Sidelines National Security Concerns</span>
          <span class="news-value-point">💡 President Trump’s move to put Jensen Huang back at the helm of Nvidia ca…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cvwy0jx7nj84o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="黄仁勋离职仅11天便重掌英伟达，凸显他对人工智能产业及美国经济的重要性。他本人和这家芯片巨头究竟有多大影响力？" data-title="Nvidia和黄仁勋对美国经济有多重要？" data-date="11-24 08:24" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-24 08:24</span>
          <span class="news-item-title">Nvidia和黄仁勋对美国经济有多重要？</span>
          <span class="news-value-point">💡 黄仁勋离职仅11天便重掌英伟达，凸显他对人工智能产业及美国经济的重要性</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/031/258.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 24 日消息，据《首尔经济日报》今日报道，三星电子计划将位于中国陕西西安的半导体工厂打造成面向人工智能（AI）数据中心企业级固态硬盘（eSSD）的核心生产基地，重点扩大第九代垂直 NAND 闪存（V9）产能。截至今年第二季度，三星西安一厂（X1）和二厂（X2）的晶圆月投入能力均为 5 万片，合计达到 10 万片（IT之家注：单位为 300mm 晶圆）。这相当于三星平泽四座工厂月产能总和（20 万片）的一半。三星两地 NAND 工厂的晶圆月产能合计约为 30 万片，其中西安工厂占比约 33%。消息人士称，三星计划升级 X2 洁净室内的电镀工艺设备，并将生产线调整为以最新第九代垂直 NAND（V9）工艺为主。除了在 X2 新增一条月产能约 2 万片的生产线外，三星还打算将现有" data-title="三星拟扩大西安工厂先进 NAND 产能、升级 V9 闪存产线，扩大面向 AI 数据中心的 eSSD 供应" data-date="11-24 07:52" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-24 07:52</span>
          <span class="news-item-title">三星拟扩大西安工厂先进 NAND 产能、升级 V9 闪存产线，扩大面向 AI 数据中心的 eSSD 供应</span>
          <span class="news-value-point">💡 IT之家 11 月 24 日消息，据《首尔经济日报》今日报道，三星电子计划将位于中国陕西西安的半导体工厂打造成面向人工智能（AI）数据中心企业级…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/031/257.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 24 日消息，据科技媒体 TechCrunch 昨天报道，Anthropic 现已推出 Claude Ship Beta 测试版。这是一套 AI 智能体组成的工具，可自动完成代码审查、修复和批准等工作。IT之家从原报道获悉，Claude Ship 包含 Code Review、PR Steward 和 Claude Approvals 三项功能。其中 Code Review 已正式开放使用，另外两项目前处于 Beta 测试阶段。在这些工具中，PR Steward 主要负责处理 CI 检查失败、合并冲突，以及 Code Review 提出的反馈问题。每次代码推送完成后，它会在评论说明自己修改了哪些内容，以及在必要时如何撤销这些修改。Claude Approvals 可根据开" data-title="Anthropic 推出 Claude Ship 测试版：AI 可自动审查、修复及批准代码" data-date="11-24 07:49" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-24 07:49</span>
          <span class="news-item-title">Anthropic 推出 Claude Ship 测试版：AI 可自动审查、修复及批准代码</span>
          <span class="news-value-point">💡 IT之家 11 月 24 日消息，据科技媒体 TechCrunch 昨天报道，Anthropic 现已推出 Claude Ship Beta 测…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13615599/wolves-hit-their-stride-stoke-continue-to-dream-but-can-they-last-the-course-and-are-qpr-dark-horses-of-championship" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Wolves are clicking, Stoke are dreaming - but could QPR be dark horses?" data-title="Wolves are clicking, Stoke are dreaming - but could QPR be dark horses?" data-date="11-24 15:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 15:00</span>
          <span class="news-item-title">Wolves are clicking, Stoke are dreaming - but could QPR be dark horses?</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c34gn2p5d0zwo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在本赛季英超联赛的每一轮比赛之后，特洛伊·迪尼（ Troy Deeney ）都给了我们本周最佳球队。你同意他的选择吗？" data-title="Who has made Troy&#39;s Premier League team of the week?" data-date="11-24 07:26" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-24 07:26</span>
          <span class="news-item-title">谁入选了特洛伊本周的英超联赛球队？</span>
          <span class="news-item-title-en">Who has made Troy's Premier League team of the week?</span>
          <span class="news-value-point">💡 在本赛季英超联赛的每一轮比赛之后，特洛伊·迪尼（ Troy Deeney ）都给了我们本周最佳球队</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13279303/everton-transfers-latest-news-rumours-and-gossip-live-updates-goals-and-highlights" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Everton latest: Moyes unsure over Tarkowski appeal with Liverpool up next" data-title="Everton latest: Moyes unsure over Tarkowski appeal with Liverpool up next" data-date="11-24 07:02" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 07:02</span>
          <span class="news-item-title">埃弗顿最新消息：莫耶斯对塔尔科夫斯基的上诉持不确定态度，下一场将对阵利物浦</span>
          <span class="news-item-title-en">Everton latest: Moyes unsure over Tarkowski appeal with Liverpool up next</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13279280/brentford-transfers-latest-news-rumours-and-gossip-live-updates-goals-and-highlights" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Brentford latest: &#39;Get real&#39; - Andrews pushes back against rising expectations" data-title="Brentford latest: &#39;Get real&#39; - Andrews pushes back against rising expectations" data-date="11-24 07:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 07:00</span>
          <span class="news-item-title">布伦特福德最新消息：“清醒一点”——安德鲁斯对不断升高的期望表示反对</span>
          <span class="news-item-title-en">Brentford latest: 'Get real' - Andrews pushes back against rising expectations</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmqx5eynvpqno?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在周一以 0-4 输给布伦特福德的比赛中，埃弗顿队长詹姆斯·塔尔科夫斯基（James Tarkowski）在其英超生涯中首次被罚下场——但这是一项严厉的判罚吗？" data-title="Tarkowski&#39;s first Premier League red ruins Moyes&#39; night" data-date="11-24 06:43" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-24 06:43</span>
          <span class="news-item-title">塔尔科夫斯基在英超联赛中的首张红牌毁了莫耶斯的夜晚</span>
          <span class="news-item-title-en">Tarkowski's first Premier League red ruins Moyes' night</span>
          <span class="news-value-point">💡 在周一以 0-4 输给布伦特福德的比赛中，埃弗顿队长詹姆斯·塔尔科夫斯基（James Tarkowski）在其英超生涯中首次被罚下场——但这是一…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13615837/man-utd-transfer-news-brentford-defender-nathan-collins-emerges-as-january-target-paper-talk" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="周二报纸的热门报道和转移谣言……" data-title="Papers: Brentford defender emerges as Man Utd target as January budget revealed" data-date="11-24 06:40" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 06:40</span>
          <span class="news-item-title">报纸：随着1月转会预算的披露，布伦特福德后卫成为曼联的目标</span>
          <span class="news-item-title-en">Papers: Brentford defender emerges as Man Utd target as January budget revealed</span>
          <span class="news-value-point">💡 周二报纸的热门报道和转移谣言……</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13615837/man-utd-transfer-news-brentford-defender-nathan-collins-emerges-as-january-target-paper-talk" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="周二报纸的热门报道和转移谣言……" data-title="Papers: Brentford defender emerges as Man Utd target as January budget revealed" data-date="11-24 06:40" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 06:40</span>
          <span class="news-item-title">报纸：随着1月转会预算的披露，布伦特福德后卫成为曼联的目标</span>
          <span class="news-item-title-en">Papers: Brentford defender emerges as Man Utd target as January budget revealed</span>
          <span class="news-value-point">💡 周二报纸的热门报道和转移谣言……</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13615825/goal-v-janelt-67-brentford-3-0-everton" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="詹尔特远射破门，为布伦特福德在英超对阵埃弗顿的比赛中攻入第三球" data-title="WHAT A STRIKE! Janelt rifles rocket for Brentford’s third" data-date="11-24 05:41" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 05:41</span>
          <span class="news-item-title">真是一记精彩的射门！詹尔特劲射破门，为布伦特福德攻入第三球。</span>
          <span class="news-item-title-en">WHAT A STRIKE! Janelt rifles rocket for Brentford’s third</span>
          <span class="news-value-point">💡 詹尔特远射破门，为布伦特福德在英超对阵埃弗顿的比赛中攻入第三球</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/brentford-vs-everton/report/559546" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="基恩·刘易斯-波特在上半场梅开二度，帮助布伦特福德在英超联赛中以 4-0 的大比分完胜 10 人应战的埃弗顿。" data-title="Lewis-Potter scores twice as Brentford thump four past 10-man Everton" data-date="11-24 05:30" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 05:30</span>
          <span class="news-item-title">布伦特福德以 4-0 大胜 10 人应战的埃弗顿，刘易斯-波特梅开二度</span>
          <span class="news-item-title-en">Lewis-Potter scores twice as Brentford thump four past 10-man Everton</span>
          <span class="news-value-point">💡 基恩·刘易斯-波特在上半场梅开二度，帮助布伦特福德在英超联赛中以 4-0 的大比分完胜 10 人应战的埃弗顿</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025499/man-city-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Man City latest: De Bruyne speaks for first time on club&#39;s guilty verdict" data-title="Man City latest: De Bruyne speaks for first time on club&#39;s guilty verdict" data-date="11-24 05:10" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 05:10</span>
          <span class="news-item-title">曼城最新消息：德布劳内首次就俱乐部的有罪判决发表看法</span>
          <span class="news-item-title-en">Man City latest: De Bruyne speaks for first time on club's guilty verdict</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13615787/off-j-tarkowski-40-brentford-2-0-everton" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在埃弗顿与布伦特福德的英超联赛中，塔科夫斯基在VAR回放后被罚下场，引发了VAR争议。" data-title="RED CARD! VAR controversy as Tarkowski sent off after review" data-date="11-24 04:46" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 04:46</span>
          <span class="news-item-title">红牌！塔科夫斯基在VAR回放后被罚下场，引发争议</span>
          <span class="news-item-title-en">RED CARD! VAR controversy as Tarkowski sent off after review</span>
          <span class="news-value-point">💡 在埃弗顿与布伦特福德的英超联赛中，塔科夫斯基在VAR回放后被罚下场，引发了VAR争议</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13615552/are-manchester-united-in-a-relegation-battle-gary-neville-and-jamie-carragher-assess-their-survival-chances" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="最初只是一个小插曲，如今却演变成了曼联一个更加系统性的问题。" data-title="Are Man Utd genuinely in a relegation battle?" data-date="11-24 03:45" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 03:45</span>
          <span class="news-item-title">曼联真的在为保级而战吗？</span>
          <span class="news-item-title-en">Are Man Utd genuinely in a relegation battle?</span>
          <span class="news-value-point">💡 最初只是一个小插曲，如今却演变成了曼联一个更加系统性的问题</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13615552/are-manchester-united-in-a-relegation-battle-gary-neville-and-jamie-carragher-assess-their-survival-chances" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="最初只是一个小插曲，如今却演变成了曼联一个更加系统性的问题。" data-title="Are Man Utd genuinely in a relegation battle?" data-date="11-24 03:45" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 03:45</span>
          <span class="news-item-title">曼联真的在为保级而战吗？</span>
          <span class="news-item-title-en">Are Man Utd genuinely in a relegation battle?</span>
          <span class="news-value-point">💡 最初只是一个小插曲，如今却演变成了曼联一个更加系统性的问题</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/brentford-vs-everton/live/559546" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Grealish on bench for Everton as Wilson starts for Brentford LIVE!" data-title="Grealish on bench for Everton as Wilson starts for Brentford LIVE!" data-date="11-24 02:30" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 02:30</span>
          <span class="news-item-title">格拉利什在对阵埃弗顿的比赛中替补上场，威尔逊在对阵布伦特福德的比赛中首发，敬请观看直播！</span>
          <span class="news-item-title-en">Grealish on bench for Everton as Wilson starts for Brentford LIVE!</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/12040/12476234/transfer-centre-live-football-transfer-news-updates-and-rumours" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Transfer Centre LIVE! Williams-Barnett agrees long-term Spurs contract" data-title="Transfer Centre LIVE! Williams-Barnett agrees long-term Spurs contract" data-date="11-24 01:30" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-24 01:30</span>
          <span class="news-item-title">转会中心直播！威廉姆斯-巴尼特同意与热刺签下长期合同</span>
          <span class="news-item-title-en">Transfer Centre LIVE! Williams-Barnett agrees long-term Spurs contract</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-24/10737137.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="开幕式现场。大会主办方供图 中新网杭州11月24日电(王逸飞 吴君毅)24日，“2026中外青年商界菁英大会”在浙江省杭州市开幕。" data-title="“2026中外青年商界菁英大会”在杭州开幕" data-date="11-24 19:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 19:41</span>
          <span class="news-item-title">“2026中外青年商界菁英大会”在杭州开幕</span>
          <span class="news-value-point">💡 开幕式现场</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-24/10737134.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京11月24日电 题：技术骨干走进新疆艾古斯乡 携手赋能乡村振兴" data-title="技术骨干走进新疆艾古斯乡 携手赋能乡村振兴" data-date="11-24 19:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 19:41</span>
          <span class="news-item-title">技术骨干走进新疆艾古斯乡 携手赋能乡村振兴</span>
          <span class="news-value-point">💡 中新网北京11月24日电 题：技术骨干走进新疆艾古斯乡 携手赋能乡村振兴</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/031/817.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 24 日消息，国家医保局今日发文公布数据：截至 2026 年 10 月底，全国医保码激活使用人数突破 13 亿。据介绍，医保码的诞生，源于“全国一盘棋”的顶层设计。全国统一的医保信息平台全面建成，贯通 31 个省（区、市）和新疆生产建设兵团，搭建起一条纵横东西、联通南北的医保服务“网络高速公路”。2019 年 11 月 24 日，全国首张医保码在山东济南签发。据IT之家此前报道，今年 9 月底，医保钱包 2.0 版正式上线，职工医保个人账户共济通过医保码即可便捷办理。至此，医保个人账户资金跨省共济给近亲属已在全国全面落地。医保钱包 2.0 版破解了被共济人使用共济资金的区域限制，由过去省内使用扩展到支持跨省使用，从就医购药扩展到城乡居民的医保和长期护理保险参保缴费，进一步" data-title="国家医保局：截至 2026 年 10 月底，全国医保码激活使用人数突破 13 亿" data-date="11-24 19:36" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-24 19:36</span>
          <span class="news-item-title">国家医保局：截至 2026 年 10 月底，全国医保码激活使用人数突破 13 亿</span>
          <span class="news-value-point">💡 IT之家 11 月 24 日消息，国家医保局今日发文公布数据：截至 2026 年 10 月底，全国医保码激活使用人数突破 13 亿</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-24/10737140.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网杭州11月24日电(王逸飞 鲍梦妮)在“六小龙”之后，杭州正用一场新的发力，证明“培育更多‘科技新小龙’”不是一句虚言。" data-title="杭州为创新栽下千棵“好苗子”" data-date="11-24 19:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 19:29</span>
          <span class="news-item-title">杭州为创新栽下千棵“好苗子”</span>
          <span class="news-value-point">💡 中新网杭州11月24日电(王逸飞 鲍梦妮)在“六小龙”之后，杭州正用一场新的发力，证明“培育更多‘科技新小龙’”不是一句虚言</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-24/10737129.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网广州11月24日电 (记者 王坚)2026年美国犹他州“青年友好大使”广州行活动近日在广州举行。23日，美国犹他州代表团师生一行走进广州市中黄港澳子弟学校、广州市黄埔区中黄外国语实验学校开展参访交流，通过校园参观、结对交流、中华文化体验等形式，近距离了解广州中小学教育实践，在面对面交流中增进理解、缔结友谊。" data-title="美国青年走进广州校园体验中华文化" data-date="11-24 19:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 19:28</span>
          <span class="news-item-title">美国青年走进广州校园体验中华文化</span>
          <span class="news-value-point">💡 中新网广州11月24日电 (记者 王坚)2026年美国犹他州“青年友好大使”广州行活动近日在广州举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-24/10737131.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京11月24日电 (记者 应妮)“升维·生生 首届北京数字化雕塑协会实验展”日前在北京侨福当代美术馆开幕。展览分为传统文化的数字化转译与人文自然精神的数字化表达两个单元，呈现了26件/组风格各异的数字化雕塑实验作品。" data-title="首届北京数字化雕塑协会实验展探索数字雕塑的赋能潜力" data-date="11-24 19:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-24 19:28</span>
          <span class="news-item-title">首届北京数字化雕塑协会实验展探索数字雕塑的赋能潜力</span>
          <span class="news-value-point">💡 中新网北京11月24日电 (记者 应妮)“升维·生生 首届北京数字化雕塑协会实验展”日前在北京侨福当代美术馆开幕</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/031/814.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 24 日消息，浩鑫（Shuttle）宣布推出一款型号为 NW10U 的紧凑型迷你主机，该机基于英特尔“Wildcat Lake”平台打造，面向商务市场。该机整体尺寸为 103 x 97 x 36.5 mm，体积 0.4L，可安装至 75 x 75 mm 和 100 x 100 mm 标准的 VESA 支架上。其正面配备双 USB-A 3.2 Gen2 接口和 3.5mm 耳机插孔；后置双 USB-C 3.2 Gen2 接口、一个 HDMI 2.1 接口、双 USB-A 2.0 接口、一个千兆网口。规格方面，该机可选英特尔 Core 3 304 / Core 5 320 / Core 7 350 处理器，TDP 为 15W，最高睿频为 4.8GHz，核显配备最多 2 个 X" data-title="浩鑫推出 0.4L 体积商务迷你主机 NW10U，基于英特尔 Wildcat Lake 平台打造" data-date="11-24 19:24" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-24 19:24</span>
          <span class="news-item-title">浩鑫推出 0.4L 体积商务迷你主机 NW10U，基于英特尔 Wildcat Lake 平台打造</span>
          <span class="news-value-point">💡 IT之家 11 月 24 日消息，浩鑫（Shuttle）宣布推出一款型号为 NW10U 的紧凑型迷你主机，该机基于英特尔“Wildcat Lak…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/031/813.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 24 日消息，小米互联网官方微博今日宣布，小米浏览器手机、Pad 现已支持扩展程序：广告拦截、网页翻译、AI 助手、脚本管理菜单里一点即开。IT之家注意到，在今年 6 月，小米员工 @劣人潘 曾发文预告过该功能，当时曾表示会在未来合适的时机发布支持插件的浏览器版本。延伸阅读小米浏览器手机端需升级至 20.32 及以上版本、Pad 端需升级至 20.6 及以上版本，才能体验扩展程序功能。除扩展程序外，此次更新中，小米浏览器的 AI 搜索还同步新增了“互动广场”功能，无需下载即可使用。实际上，浏览器插件能力最早是随小米澎湃 HyperOS 4 系统与用户见面的，并非此次才首次出现。2026 年 8 月中旬，有数码博主分享称 HyperOS 4 的浏览器已支持插件功能，用户可从" data-title="小米浏览器手机、Pad 官宣支持扩展程序：广告拦截、网页翻译、AI 助手、脚本管理" data-date="11-24 19:22" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-24 19:22</span>
          <span class="news-item-title">小米浏览器手机、Pad 官宣支持扩展程序：广告拦截、网页翻译、AI 助手、脚本管理</span>
          <span class="news-value-point">💡 IT之家 11 月 24 日消息，小米互联网官方微博今日宣布，小米浏览器手机、Pad 现已支持扩展程序：广告拦截、网页翻译、AI 助手、脚本管理…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/031/812.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="就在今天（11 月 24 日）14:30，华为 Mate X8 及全场景新品发布会准时启幕。前段时间刚先后看完问界新 M8、享界 V8、星芒 O1 Pro 轮番登场，这回华为又甩出新一轮全家桶。重头戏不用多说，主角就是 Mate X8，八年八代的大折叠旗舰，这次直接全面焕新；除此之外，还有小折叠电脑、超薄手表一众狠货同步登场。废话不多说，华为这波全场景新品都藏了哪些硬活，IT之家小编这就挨个扒一遍。一、Mate X8在大折叠手机全球发货量突破 1200 万台后，华为 Mate X8 如期而至。这一代在设计上玩起了焕新新花样，把织金云锦、钇晶宝石和鎏光腰线埋进机身细节里。背板以金丝为脉络，渐色工艺搭配织金工艺再度升级；镜头模组延续 Mate X 家族标志性的寰宇星环，点缀钇晶宝石；就连铰链轴盖" data-title="华为 Mate X8 及全场景新品发布会一文汇总：轻薄、折叠“双响炮”，鸿蒙破亿“发钱”了" data-date="11-24 19:20" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-24 19:20</span>
          <span class="news-item-title">华为 Mate X8 及全场景新品发布会一文汇总：轻薄、折叠“双响炮”，鸿蒙破亿“发钱”了</span>
          <span class="news-value-point">💡 就在今天（11 月 24 日）14:30，华为 Mate X8 及全场景新品发布会准时启幕</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/peripherals/wearable-tech/gamer-hijacks-plane-in-gta-6-using-just-mind-control-and-eye-tracking-xbox-controller-mapped-to-read-brain-signals-using-eeg" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Perri Karyal programmed an EEG device to read her brainwaves and translate it to actions on her Xbox controller." data-title="Gamer hijacks plane in GTA 6 using just mind control and eye tracking" data-date="11-24 18:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-24 18:30</span>
          <span class="news-item-title">Gamer hijacks plane in GTA 6 using just mind control and eye tracking</span>
          <span class="news-value-point">💡 Perri Karyal programmed an EEG device to read her brainwaves and transla…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cw8dv46pv125o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="宏福苑大火一周年前夕，港府官员称“政府绝对容许”合法活动，但有遗属表示悼念活动受压，也有新闻工作者向BBC中文透露，相关周年报导在制作完成后突然“被抽起”。" data-title="宏福苑大火一周年：居民受压、媒体噤声，为何悼念变得小心翼翼？" data-date="11-24 18:13" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-24 18:13</span>
          <span class="news-item-title">宏福苑大火一周年：居民受压、媒体噤声，为何悼念变得小心翼翼？</span>
          <span class="news-value-point">💡 宏福苑大火一周年前夕，港府官员称“政府绝对容许”合法活动，但有遗属表示悼念活动受压，也有新闻工作者向BBC中文透露，相关周年报导在制作完成后突然…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/24/us/harvard-maga-class.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="The Make America Great Again movement wants to remake Harvard. Harvard has a class for that." data-title="MAGA Attacked Harvard. So Harvard Taught a Class About It." data-date="11-24 18:00" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-24 18:00</span>
          <span class="news-item-title">MAGA Attacked Harvard. So Harvard Taught a Class About It.</span>
          <span class="news-value-point">💡 The Make America Great Again movement wants to remake Harvard. Harvard h…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/24/us/haitians-deportations-canada-immigration.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Driven to Canada by deportation fears, some members of Haitian families are being denied entry, turned back and detained by U.S. authorities." data-title="Some Haitian Families Fleeing the U.S. for Canada Are Being Separated at the Border" data-date="11-24 18:00" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-24 18:00</span>
          <span class="news-item-title">Some Haitian Families Fleeing the U.S. for Canada Are Being Separated at the Border</span>
          <span class="news-value-point">💡 Driven to Canada by deportation fears, some members of Haitian families …</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/pc-gaming/enthusiast-gets-gta-v-running-on-a-2007-radeon-with-just-64mb-of-vram-config-edits-windows-8-and-an-overclock-lift-it-from-1-fps-to-20-fps-but-most-cars-stop-rendering" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Budget-Builds Official ran GTA V on a 2007 ATI Radeon HD 2350 with 64MB of DDR2 VRAM at 13 to 20 FPS." data-title="Enthusiast gets GTA V running on a 2007 Radeon with just 64MB of VRAM" data-date="11-24 18:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-24 18:00</span>
          <span class="news-item-title">Enthusiast gets GTA V running on a 2007 Radeon with just 64MB of VRAM</span>
          <span class="news-value-point">💡 Budget-Builds Official ran GTA V on a 2007 ATI Radeon HD 2350 with 64MB …</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/sharges-disk-pro-2-usb-hub-and-actively-cooled-m-2-enclosure-drops-to-its-lowest-ever-price-one-of-my-favorite-products-of-2026-now-starts-at-just-usd66" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Sharge&#39;s see-through hub with the ports you need and up to 8TB of storage is now on sale for $66.51 for the Lite model, or $80.91 for the Ultra model that supports up to 8K and faster card reader speeds." data-title="Sharge&#39;s Disk Pro 2 USB hub and actively cooled M.2 enclosure drops to its lowest" data-date="11-24 17:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-24 17:30</span>
          <span class="news-item-title">Sharge's Disk Pro 2 USB hub and actively cooled M.2 enclosure drops to its lowest</span>
          <span class="news-value-point">💡 Sharge's see-through hub with the ports you need and up to 8TB of storag…</span>
        </a>
  </div>
</div>
<script defer src="{{ "/assets/js/news-feed.js" | relative_url }}"></script>


<p class="news-updated">🕐 抓取更新于 2026-11-24 19:43（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
