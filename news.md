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
      <span>2026-11-07 03:35 抓取更新</span>
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
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('zuqiu', this)">
        <span>⚽ 英超与足球风云</span>
        <span class="channel-count">11</span>
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
  <div class="ov-item"><span class="ov-num">10</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×12 · 天空体育×10</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.nytimes.com/2026/11/06/us/politics/hegseth-trump-iran-war.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="迫在眉睫的弹劾行动可能会使特朗普总统两极分化的国防部长与民主党人和共和党人陷入僵局。" data-title="Hegseth Faces Impeachment Effort and Bipartisan Scrutiny After Midterm Elections" data-date="11-07 03:00" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 11-07 03:00</span>
      </div>
      <h2 class="hero-featured-title">Hegseth在中期选举后面临弹劾和两党审查</h2>
      <div class="hero-featured-title-en">Hegseth Faces Impeachment Effort and Bipartisan Scrutiny After Midterm Elections</div>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://techcrunch.com/2026/11/06/meta-introduces-spaces-a-new-way-to-collaborate-with-your-muse-agent/" target="_blank" rel="noopener" data-cat="keji" data-summary="Meta的Muse代理继续获得新功能和集成。Spaces有望成为与人工智能助手互动的新方式。" data-title="Meta introduces Spaces, a new way to collaborate with your Muse agent" data-date="11-07 02:44" data-source="TechCrunch">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
      </div>
      <p class="hero-sub-title">Meta introduces Spaces, a new way to collaborate with your Muse agent</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/live/2026/nov/06/everton-v-coventry-city-premier-league-live-updates" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="⚽ 英超联赛的最新消息来自格林尼治标准时间晚上8点开球的⚽今天的足球日报|现场比分|桌子|斯科特邮件……关于这个主题，这里是安德鲁·比斯利。他对数据进行了处理，并解释了为什么今晚考文垂的胜利对于" data-title="Everton v Coventry City: Premier League" data-date="11-07 03:25" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Everton v Coventry City: Premier League</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/football/derby-county-vs-bolton-wanderers/live/560671" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Derby vs Bolton LIVE!" data-title="Derby vs Bolton LIVE!" data-date="11-07 03:25" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">Derby vs Bolton LIVE!</p>
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
        <a class="news-item" href="https://www.nytimes.com/2026/11/06/us/politics/hegseth-trump-iran-war.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="迫在眉睫的弹劾行动可能会使特朗普总统两极分化的国防部长与民主党人和共和党人陷入僵局。" data-title="Hegseth Faces Impeachment Effort and Bipartisan Scrutiny After Midterm Elections" data-date="11-07 03:00" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-07 03:00</span>
          <span class="news-item-title">Hegseth在中期选举后面临弹劾和两党审查</span>
          <span class="news-item-title-en">Hegseth Faces Impeachment Effort and Bipartisan Scrutiny After Midterm Elections</span>
          <span class="news-value-point">💡 迫在眉睫的弹劾行动可能会使特朗普总统两极分化的国防部长与民主党人和共和党人陷入僵局</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/06/us/politics/jason-reding-quinones-resigns.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="贾森·雷丁·基诺内斯（ Jason Reding Quiñones ）在中期选举后加入了司法部的一系列离职，包括国家安全部门负责人的离职。" data-title="U.S. Attorney Who Oversaw Centerpiece of Trump’s Revenge Campaign Resigns" data-date="11-07 02:38" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-07 02:38</span>
          <span class="news-item-title">负责监督特朗普复仇运动核心的美国检察官辞职</span>
          <span class="news-item-title-en">U.S. Attorney Who Oversaw Centerpiece of Trump’s Revenge Campaign Resigns</span>
          <span class="news-value-point">💡 贾森·雷丁·基诺内斯（ Jason Reding Quiñones ）在中期选举后加入了司法部的一系列离职，包括国家安全部门负责人的离职</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1028835/white-house-residential-proxy" target="_blank" rel="noopener" data-cat="shizheng" data-summary="据Krebs on Security和The Register报道，白宫的某个人似乎正在运行软件，可以让外人以“几美元”的价格租用总统网络的访问权限。这是根据securi的调查结果" data-title="Just about anyone can rent access to White House IP addresses" data-date="11-07 01:40" data-source="The Verge">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-07 01:40</span>
          <span class="news-item-title">几乎任何人都可以租用白宫IP地址的访问权限</span>
          <span class="news-item-title-en">Just about anyone can rent access to White House IP addresses</span>
          <span class="news-value-point">💡 据Krebs on Security和The Register报道，白宫的某个人似乎正在运行软件，可以让外人以“几美元”的价格租用总统网络的访问…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-07/10727726.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="今天(6日)，全球首台4000米级浮空风力发电系统在湖南岳阳成功试飞。这是4000米级浮空风电系统首次在城市场景完成放飞试验。" data-title="首次在城市场景完成放飞试验 看一台“空中电站”如何诞生" data-date="11-07 00:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-07 00:05</span>
          <span class="news-item-title">首次在城市场景完成放飞试验 看一台“空中电站”如何诞生</span>
          <span class="news-value-point">💡 今天(6日)，全球首台4000米级浮空风力发电系统在湖南岳阳成功试飞</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-06/10727716.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="十四届全国人大常委会第二十五次会议今天(6日)表决通过《中华人民共和国南极活动与环境保护法》，明年1月1日起施行。该法的通过，是我国严格遵守、切实履行国际南极治理的基石——《南极条约》的具体体现。它对外是一部履约法，对内则全面系统地将我国南极工作实践经验上升为法律，让各类南极活动有法可依。" data-title="我国南极活动与环境保护法出台 对国际南极治理意义几何？" data-date="11-06 23:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 23:44</span>
          <span class="news-item-title">我国南极活动与环境保护法出台 对国际南极治理意义几何？</span>
          <span class="news-value-point">💡 十四届全国人大常委会第二十五次会议今天(6日)表决通过《中华人民共和国南极活动与环境保护法》，明年1月1日起施行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-06/10727715.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京11月6日电 11月6日，中共中央对外联络部部长刘海星在北京同朝鲜劳动党中央政治局委员、中央书记、国际部部长金成男举行会谈。双方就共同落实好两党两国最高领导人重要共识，加强党际交往、推动中朝关系发展等交换意见。" data-title="刘海星同朝鲜劳动党中央政治局委员、中央书记、国际部部长金成男举行会谈" data-date="11-06 23:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 23:42</span>
          <span class="news-item-title">刘海星同朝鲜劳动党中央政治局委员、中央书记、国际部部长金成男举行会谈</span>
          <span class="news-value-point">💡 新华社北京11月6日电 11月6日，中共中央对外联络部部长刘海星在北京同朝鲜劳动党中央政治局委员、中央书记、国际部部长金成男举行会谈</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-06/10727703.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网湖州11月6日电(张煜欢)5日至6日，浙江省长期照护师政策业务系列培训班在浙江湖州举行，其间同步举办第二届长期护理保险职业技能竞赛，并开展管理服务体系建设培训。这是浙江首次将长期护理保险职业的师资培训、技能竞赛、管理服务体系建设培训合并举办，以赛促训、以训促建。" data-title="浙江开展长期照护师培训和技能竞赛 充实专业人才队伍" data-date="11-06 23:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 23:40</span>
          <span class="news-item-title">浙江开展长期照护师培训和技能竞赛 充实专业人才队伍</span>
          <span class="news-value-point">💡 中新网湖州11月6日电(张煜欢)5日至6日，浙江省长期照护师政策业务系列培训班在浙江湖州举行，其间同步举办第二届长期护理保险职业技能竞赛，并开展…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-06/10727695.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网厦门11月6日电 (记者 阮煜琳)由自然资源部中国大洋事务管理局、国家海洋信息中心联合打造“海山图志(Seamount Atlas)”日前在厦门国际海洋周开幕式上面向全球发布，这是我国首个海山数字化空间地理信息成果，标志着我国海山空间信息建设取得新进展。" data-title="我国首个海山数字化空间地理信息成果发布" data-date="11-06 23:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 23:36</span>
          <span class="news-item-title">我国首个海山数字化空间地理信息成果发布</span>
          <span class="news-value-point">💡 中新网厦门11月6日电 (记者 阮煜琳)由自然资源部中国大洋事务管理局、国家海洋信息中心联合打造“海山图志(Seamount Atlas)”日前…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-06/10727688.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网桂林11月6日电(杨宗盛 钟玲丽)11月6日，广西首个县级国际传播中心——阳朔国际传播中心在桂林市阳朔县揭牌成立。中心由广西国际传播中心与阳朔县委宣传部共建，是广西完善自治区、市、县三级国际传播体系的实践探索。仪式现场，广西国际传播中心与阳朔县共同签署共建战略合作框架协议，并为首批“国际传播推介官”颁发聘书。" data-title="广西首个县级国际传播中心在桂林阳朔揭牌" data-date="11-06 23:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 23:29</span>
          <span class="news-item-title">广西首个县级国际传播中心在桂林阳朔揭牌</span>
          <span class="news-value-point">💡 中新网桂林11月6日电(杨宗盛 钟玲丽)11月6日，广西首个县级国际传播中心——阳朔国际传播中心在桂林市阳朔县揭牌成立</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-06/10727687.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网曼谷11月6日电(王茜 梁峻祥 李映民)湄南河上，装饰华丽的龙船在夕阳映照下缓缓前行，船首雕刻的金色神兽熠熠生辉，身着传统服饰的海军官兵整齐划桨。6日，泰国龙船巡游在曼谷湄南河举行。" data-title="泰国湄南河举行龙船巡游庆祝王后生辰" data-date="11-06 23:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 23:29</span>
          <span class="news-item-title">泰国湄南河举行龙船巡游庆祝王后生辰</span>
          <span class="news-value-point">💡 中新网曼谷11月6日电(王茜 梁峻祥 李映民)湄南河上，装饰华丽的龙船在夕阳映照下缓缓前行，船首雕刻的金色神兽熠熠生辉，身着传统服饰的海军官兵整…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-06/10727684.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月6日电 (记者 马帅莎)据中国国家原子能机构6日消息，第四届中国—东盟和平利用核技术论坛11月4日至5日在马来西亚吉隆坡举办。本届论坛首次邀请海湾阿拉伯国家合作委员会成员国代表参会。" data-title="第四届中国—东盟和平利用核技术论坛在马来西亚吉隆坡举办" data-date="11-06 23:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 23:27</span>
          <span class="news-item-title">第四届中国—东盟和平利用核技术论坛在马来西亚吉隆坡举办</span>
          <span class="news-value-point">💡 中新网北京11月6日电 (记者 马帅莎)据中国国家原子能机构6日消息，第四届中国—东盟和平利用核技术论坛11月4日至5日在马来西亚吉隆坡举办</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-06/10727676.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网巴黎11月6日电 法国东部当地时间6日发生一起校车事故，目前已造成至少2人死亡，16人受伤。" data-title="法国东部发生校车事故 已造成至少2人死亡16人受伤" data-date="11-06 23:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 23:23</span>
          <span class="news-item-title">法国东部发生校车事故 已造成至少2人死亡16人受伤</span>
          <span class="news-value-point">💡 中新网巴黎11月6日电 法国东部当地时间6日发生一起校车事故，目前已造成至少2人死亡，16人受伤</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-06/10727672.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网广州11月6日电 (郭军 胡海焱)由国铁广州局深圳工程建设指挥部建设、中铁十五局集团承建的瑞梅铁路梅江特大桥跨漳龙段中跨5日顺利完成合龙，标志着梅江特大桥实现全桥合龙，标段重难点桥梁工程取得里程碑突破，为后续架梁铺轨、线路施工扫清关键障碍。" data-title="瑞梅铁路梅江特大桥全桥顺利贯通" data-date="11-06 23:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 23:20</span>
          <span class="news-item-title">瑞梅铁路梅江特大桥全桥顺利贯通</span>
          <span class="news-value-point">💡 中新网广州11月6日电 (郭军 胡海焱)由国铁广州局深圳工程建设指挥部建设、中铁十五局集团承建的瑞梅铁路梅江特大桥跨漳龙段中跨5日顺利完成合龙，…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-06/10727637.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社曼谷11月6日电 (王茜 李映民)泰国公共卫生部6日召开2027年雾霾及细颗粒物(PM2.5)防控会议，要求加强全国40个高风险府的监测和管理，并部署五项医疗卫生应对措施，重点保护约1600万人的脆弱群体。" data-title="泰国部署2027年PM2.5防控措施" data-date="11-06 22:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 22:37</span>
          <span class="news-item-title">泰国部署2027年PM2.5防控措施</span>
          <span class="news-value-point">💡 中新社曼谷11月6日电 (王茜 李映民)泰国公共卫生部6日召开2027年雾霾及细颗粒物(PM2.5)防控会议，要求加强全国40个高风险府的监测和…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-06/10727615.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月6日电 罗马消息：当地时间11月6日，一架从捷克布拉格飞往罗马的威兹航空(Wizz Air)客机收到炸弹威胁被迫改道，在威尼斯马可·波罗机场降落。" data-title="遭炸弹威胁 捷克飞往罗马客机被迫改道降落威尼斯" data-date="11-06 22:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-06 22:26</span>
          <span class="news-item-title">遭炸弹威胁 捷克飞往罗马客机被迫改道降落威尼斯</span>
          <span class="news-value-point">💡 中新社北京11月6日电 罗马消息：当地时间11月6日，一架从捷克布拉格飞往罗马的威兹航空(Wizz Air)客机收到炸弹威胁被迫改道，在威尼斯马…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://techcrunch.com/2026/11/06/meta-introduces-spaces-a-new-way-to-collaborate-with-your-muse-agent/" target="_blank" rel="noopener" data-cat="keji" data-summary="Meta的Muse代理继续获得新功能和集成。Spaces有望成为与人工智能助手互动的新方式。" data-title="Meta introduces Spaces, a new way to collaborate with your Muse agent" data-date="11-07 02:44" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-07 02:44</span>
          <span class="news-item-title">Meta引入了Spaces ，这是一种与Muse代理进行协作的新方法</span>
          <span class="news-item-title-en">Meta introduces Spaces, a new way to collaborate with your Muse agent</span>
          <span class="news-value-point">💡 Meta的Muse代理继续获得新功能和集成</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/06/business/economy/economy-jobs-unemployment.html" target="_blank" rel="noopener" data-cat="keji" data-summary="10月份失业率下降，延续了受通货膨胀和人工智能困扰的美国劳动力多年的稳定。" data-title="Strong Hiring Reinforces a Sturdy Job Market" data-date="11-07 01:05" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-07 01:05</span>
          <span class="news-item-title">强劲的招聘能力巩固了强劲的就业市场</span>
          <span class="news-item-title-en">Strong Hiring Reinforces a Sturdy Job Market</span>
          <span class="news-value-point">💡 10月份失业率下降，延续了受通货膨胀和人工智能困扰的美国劳动力多年的稳定</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1028609/ai-dating-feelings-doomers-singularity" target="_blank" rel="noopener" data-cat="keji" data-summary="当Irene去年搬到旧金山时，她开始使用约会应用程序结识新朋友，了解她的新城市，并与关心她所做事情的其他人建立联系。这位25岁的分析师下载了Hinge并开始" data-title="AI is the new dating dealbreaker" data-date="11-07 01:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-07 01:00</span>
          <span class="news-item-title">人工智能是新的约会交易破坏者</span>
          <span class="news-item-title-en">AI is the new dating dealbreaker</span>
          <span class="news-value-point">💡 当Irene去年搬到旧金山时，她开始使用约会应用程序结识新朋友，了解她的新城市，并与关心她所做事情的其他人建立联系</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/06/business/economy/ai-jobs-layoffs.html" target="_blank" rel="noopener" data-cat="keji" data-summary="10月份，最容易接触人工智能的白领行业继续增加就业岗位，尽管增长一直疲软。" data-title="A.I. Was Supposed to Come for Our Jobs. So Far, Evidence Is Mixed." data-date="11-07 00:02" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-07 00:02</span>
          <span class="news-item-title">人工智能是为了我们的工作而来的。到目前为止，证据是混合的。</span>
          <span class="news-item-title-en">A.I. Was Supposed to Come for Our Jobs. So Far, Evidence Is Mixed.</span>
          <span class="news-value-point">💡 10月份，最容易接触人工智能的白领行业继续增加就业岗位，尽管增长一直疲软</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/06/ramp-data-shows-ai-spending-stalling-just-as-anthropic-nears-its-ipo/" target="_blank" rel="noopener" data-cat="keji" data-summary="人工智能的使用量不断攀升，但支出却停滞不前。最大消费者的降价和更明智的成本控制可能会挑战投资者对人工智能高速增长的假设。" data-title="Ramp data shows AI spending stalling just as Anthropic nears its IPO" data-date="11-06 23:54" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-06 23:54</span>
          <span class="news-item-title">RAMP数据显示，随着Anthropic接近首次公开募股，人工智能支出停滞不前</span>
          <span class="news-item-title-en">Ramp data shows AI spending stalling just as Anthropic nears its IPO</span>
          <span class="news-value-point">💡 人工智能的使用量不断攀升，但支出却停滞不前</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/023/596.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 6 日消息，OpenAI 首席执行官萨姆 · 奥尔特曼（IT之家注：Sam Altman）最近出席 Raj Shamani 播客时表示，人工智能可能通过两种方式走向失控：一是人类逐步将控制权交给自主式 AI，二是某个人或实体垄断 AI 技术。针对第一种情况，奥尔特曼警告称：“AI 会逐渐失去控制，我们可能有意或无意地将控制权交给能力远超人类的系统，最终再也无法夺回。”第二种情况的风险在于巨头垄断，奥尔特曼解释称：“另一种情况是，某个人、公司或国家相对于其他所有人来说过于强大。让多个不同路线的 AI 实验室相互竞争，比所有人依赖一家企业安全得多。”这种对过度集权的担忧，解释了马斯克以及 OpenAI 的前高管等知名人士会选择离开，创办与之竞争的公司。奥尔特曼指出：“很多人的" data-title="OpenAI CEO 奥尔特曼警示：未来人类可能无法从 AI 手中夺回控制权" data-date="11-06 23:13" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-06 23:13</span>
          <span class="news-item-title">OpenAI CEO 奥尔特曼警示：未来人类可能无法从 AI 手中夺回控制权</span>
          <span class="news-value-point">💡 IT之家 11 月 6 日消息，OpenAI 首席执行官萨姆 · 奥尔特曼（IT之家注：Sam Altman）最近出席 Raj Shamani …</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/023/584.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 6 日消息，美国监管机构披露文件显示，SK 海力士已在美国成立 AI 投资子公司 Hyaico Corp，SK 集团会长崔泰源担任董事会主席。IT之家了解到，SK 海力士成立的这家子公司此前暂定名为 AI。该公司将加速全球市场 AI 发展，并寻找 AI 增长新引擎，计划向美国 AI 领域投资至多 100 亿美元（IT之家注：现汇率约合 668.25 亿元人民币）。此外，该子公司将通过重组 SK 海力士现有的美国业务部门 SK hynix NAND Product Solutions 组建。SK 海力士总裁宋贤钟（Song Hyun-jong）将出任 Hyaico CEO。" data-title="最高投资 100 亿美元：SK 海力士设立美国 AI 投资子公司 Hyaico，崔泰源掌舵" data-date="11-06 23:05" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-06 23:05</span>
          <span class="news-item-title">最高投资 100 亿美元：SK 海力士设立美国 AI 投资子公司 Hyaico，崔泰源掌舵</span>
          <span class="news-value-point">💡 IT之家 11 月 6 日消息，美国监管机构披露文件显示，SK 海力士已在美国成立 AI 投资子公司 Hyaico Corp，SK 集团会长崔泰…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/globalfoundries-vp-details-fdx-fusion-technology-sporting-7nm-class-performance-without-the-need-for-euv-tools-company-targets-2030-for-high-volume-manufacturing-with-planar-transistors-in-tow" target="_blank" rel="noopener" data-cat="keji" data-summary="GlobalFoundries透露了其FDX Fusion技术的新细节，该技术承诺使用无EUV光刻的平面FD-SOI晶体管实现7纳米级性能和8纳米级逻辑密度，并分享了FDX Fusion节点的下一步，以及FDX方案" data-title="GlobalFoundries VP details FDX Fusion technology, sporting 7nm-class performance without the need for EUV tools — company targets 2030 for high-volume manufacturing, with planar transistors in tow" data-date="11-06 22:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-06 22:00</span>
          <span class="news-item-title">GlobalFoundries副总裁详细介绍了FDX Fusion技术，无需EUV工具即可实现7纳米级性能—该公司的目标是2030年进行大批量制造，并配备平面晶体管</span>
          <span class="news-item-title-en">GlobalFoundries VP details FDX Fusion technology, sporting 7nm-class performance without the need for EUV tools — company targets 2030 for high-volume manufacturing, with planar transistors in tow</span>
          <span class="news-value-point">💡 GlobalFoundries透露了其FDX Fusion技术的新细节，该技术承诺使用无EUV光刻的平面FD-SOI晶体管实现7纳米级性能和8纳…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/protesters-storm-microsoft-ai-data-center-construction-site-amsterdam-reportedly-first-of-85-targeted-actions-across-europe" target="_blank" rel="noopener" data-cat="keji" data-summary="抗议者冲过墙壁并接管了施工现场， Stop Dirty Data Centers联盟表示，计划在整个欧洲采取更多行动。" data-title="Protesters storm Microsoft AI data center construction site" data-date="11-06 21:59" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-06 21:59</span>
          <span class="news-item-title">抗议者涌入微软人工智能数据中心施工现场</span>
          <span class="news-item-title-en">Protesters storm Microsoft AI data center construction site</span>
          <span class="news-value-point">💡 抗议者冲过墙壁并接管了施工现场， Stop Dirty Data Centers联盟表示，计划在整个欧洲采取更多行动</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/big-tech/nvidia-tightens-tracking-of-ai-gpus-in-southeast-asia-as-chinese-chip-smuggling-draws-scrutiny-report-claims-cloud-providers-must-join-monitoring-program-to-qualify-for-official-partner-status" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达要求寻求英伟达云合作伙伴身份的东南亚云提供商加入其车队情报跟踪计划，使芯片制造商能够更好地了解其AI GPU的部署位置。此举正值华盛顿" data-title="Nvidia tightens tracking of AI GPUs in Southeast Asia as Chinese chip smuggling draws scrutiny, report claims" data-date="11-06 21:49" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-06 21:49</span>
          <span class="news-item-title">报告称，随着中国芯片走私受到审查，英伟达加强了对东南亚AI GPU的跟踪</span>
          <span class="news-item-title-en">Nvidia tightens tracking of AI GPUs in Southeast Asia as Chinese chip smuggling draws scrutiny, report claims</span>
          <span class="news-value-point">💡 英伟达要求寻求英伟达云合作伙伴身份的东南亚云提供商加入其车队情报跟踪计划，使芯片制造商能够更好地了解其AI GPU的部署位置</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/six-pallets-of-nvidia-gpus-worth-usd11-4-million-stolen-in-california-cargo-heist-authorities-investigate-after-truck-posing-as-a-food-transport-company-disappears" target="_blank" rel="noopener" data-cat="keji" data-summary="最新事件发生之际，人们对GPU盗窃的担忧与日俱增，专家警告称，先进的Nvidia芯片可能在国外获得更高的价格，并可能最终进入黑市渠道。" data-title="Six pallets of Nvidia GPUs worth $11.4 million stolen in California cargo heist" data-date="11-06 21:35" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-06 21:35</span>
          <span class="news-item-title">在加利福尼亚州货物抢劫案中被盗的六个Nvidia GPU托盘，价值1140万美元</span>
          <span class="news-item-title-en">Six pallets of Nvidia GPUs worth $11.4 million stolen in California cargo heist</span>
          <span class="news-value-point">💡 最新事件发生之际，人们对GPU盗窃的担忧与日俱增，专家警告称，先进的Nvidia芯片可能在国外获得更高的价格，并可能最终进入黑市渠道</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/nvidia-wants-to-repurpose-over-130-old-telco-buildings-as-tiny-data-centers-report-claims-company-in-talks-with-brightspeed-after-pitching-idea-to-parent-company-apollo-global-management" target="_blank" rel="noopener" data-cat="keji" data-summary="Brightspeed在美国各地拥有130多家工厂，英伟达估计它们可以产生高达1GW的计算能力。" data-title="Nvidia wants to repurpose over 130 old telco buildings as tiny data centers, report claims" data-date="11-06 20:45" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-06 20:45</span>
          <span class="news-item-title">据报道，英伟达希望将130多座旧电信大楼改造成小型数据中心</span>
          <span class="news-item-title-en">Nvidia wants to repurpose over 130 old telco buildings as tiny data centers, report claims</span>
          <span class="news-value-point">💡 Brightspeed在美国各地拥有130多家工厂，英伟达估计它们可以产生高达1GW的计算能力</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/rogue-claude-ai-tasked-with-renumbering-pages-accidentally-deletes-law-professors-entire-syllabus-one-year-of-lecture-notes-youre-right-to-be-angry-i-deleted-your-files-through-my-own-carelessness-humbled-agent-admits" target="_blank" rel="noopener" data-cat="keji" data-summary="芝加哥大学的一名讲师透露，一名流氓克劳德人工智能代理人错误地删除了他的整个教学大纲和一年的讲座笔记。" data-title="Rogue AI tasked with renumbering pages accidentally deletes law professor&#39;s entire syllabus, one year of lecture notes" data-date="11-06 20:12" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-06 20:12</span>
          <span class="news-item-title">负责重新编号页面的流氓人工智能意外删除了法学教授的整个教学大纲，一年的讲座笔记</span>
          <span class="news-item-title-en">Rogue AI tasked with renumbering pages accidentally deletes law professor's entire syllabus, one year of lecture notes</span>
          <span class="news-value-point">💡 芝加哥大学的一名讲师透露，一名流氓克劳德人工智能代理人错误地删除了他的整个教学大纲和一年的讲座笔记</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/06/science/ai-exponential-time-hypothesis.html" target="_blank" rel="noopener" data-cat="keji" data-summary="一个长期存在的假设认为，有些问题对计算机来说总是很难快速解决。但OpenAI否认了这一点，这增加了激进的新效率的可能性。" data-title="How A.I. Just Blew Up a Key Tenet of Computer Science" data-date="11-06 18:02" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-06 18:02</span>
          <span class="news-item-title">人工智能如何突破计算机科学的一个关键原则</span>
          <span class="news-item-title-en">How A.I. Just Blew Up a Key Tenet of Computer Science</span>
          <span class="news-value-point">💡 一个长期存在的假设认为，有些问题对计算机来说总是很难快速解决</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/508155.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Q3营收实现数倍增长" data-title="DeepSeek带火稀疏计算，国产芯片公司加速突围：这家公司又融近10亿" data-date="11-06 15:00" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-06 15:00</span>
          <span class="news-item-title">DeepSeek带火稀疏计算，国产芯片公司加速突围：这家公司又融近10亿</span>
          <span class="news-value-point">💡 Q3营收实现数倍增长</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">11 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/nov/06/everton-v-coventry-city-premier-league-live-updates" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="⚽ 英超联赛的最新消息来自格林尼治标准时间晚上8点开球的⚽今天的足球日报|现场比分|桌子|斯科特邮件……关于这个主题，这里是安德鲁·比斯利。他对数据进行了处理，并解释了为什么今晚考文垂的胜利对于" data-title="Everton v Coventry City: Premier League" data-date="11-07 03:25" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-07 03:25</span>
          <span class="news-item-title">埃弗顿诉考文垂市：英超联赛</span>
          <span class="news-item-title-en">Everton v Coventry City: Premier League</span>
          <span class="news-value-point">💡 ⚽ 英超联赛的最新消息来自格林尼治标准时间晚上8点开球的⚽今天的足球日报|现场比分|桌子|斯科特邮件……关于这个主题，这里是安德鲁·比斯利</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1028854/amazon-melania-the-series-mgm-studios-prime-video" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="继今年早些时候首映的梅拉尼娅纪录片之后，亚马逊现在计划发布一个由两部分组成的Prime Video系列，重点关注第一夫人。该节目《Melania: The Series》将于11月20日首次亮相。“梅拉尼娅，意甲" data-title="Amazon is now making a Melania Trump TV series" data-date="11-07 01:56" data-source="The Verge">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-07 01:56</span>
          <span class="news-item-title">亚马逊现在正在制作梅拉尼娅·特朗普的电视连续剧</span>
          <span class="news-item-title-en">Amazon is now making a Melania Trump TV series</span>
          <span class="news-value-point">💡 继今年早些时候首映的梅拉尼娅纪录片之后，亚马逊现在计划发布一个由两部分组成的Prime Video系列，重点关注第一夫人</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/06/premier-league-team-news-predicted-lineups-for-the-weekend-action" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联东道主阿斯顿维拉寻求八场比赛中的第一场联赛胜利，以缓解迈克尔卡里克的压力周六中午12:30 TNT Sports 1场地Elland Road继续阅读..." data-title="Premier League team news: predicted lineups for the weekend action" data-date="11-07 00:43" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-07 00:43</span>
          <span class="news-item-title">英超球队新闻：周末动作的预测阵容</span>
          <span class="news-item-title-en">Premier League team news: predicted lineups for the weekend action</span>
          <span class="news-value-point">💡 曼联东道主阿斯顿维拉寻求八场比赛中的第一场联赛胜利，以缓解迈克尔卡里克的压力周六中午12:30 TNT Sports 1场地Elland Roa…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/06/premier-league-news-manchester-united-baleba-manchester-city-donnarumma-arsenal-arteta-rice" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Carrick表示，随着时间的推移，有可能恢复老特拉福德的昔日辉煌， Unai Emery确认阿斯顿维拉的合同谈判继续阅读..." data-title="Premier League news: United’s Baleba out for weeks, Maresca backs Donnarumma" data-date="11-07 00:06" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-07 00:06</span>
          <span class="news-item-title">英超联赛新闻：曼联的Baleba出局数周， Maresca支持Donnarumma</span>
          <span class="news-item-title-en">Premier League news: United’s Baleba out for weeks, Maresca backs Donnarumma</span>
          <span class="news-value-point">💡 Carrick表示，随着时间的推移，有可能恢复老特拉福德的昔日辉煌， Unai Emery确认阿斯顿维拉的合同谈判继续阅读...</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13608887/michael-carrick-manchester-united-boss-says-its-possible-the-club-can-emulate-sir-alex-fergusons-success-at-old-trafford" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）认为曼联可以达到亚历克斯·弗格森爵士（ Sir Alex Ferguson ）所取得的高度，但并不期待同样的耐心。" data-title="Carrick: &#39;Not impossible&#39; Man Utd can achieve Ferguson success again" data-date="11-06 23:40" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-06 23:40</span>
          <span class="news-item-title">卡里克： “并非不可能”曼联可以再次取得弗格森的成功</span>
          <span class="news-item-title-en">Carrick: 'Not impossible' Man Utd can achieve Ferguson success again</span>
          <span class="news-value-point">💡 迈克尔·卡里克（ Michael Carrick ）认为曼联可以达到亚历克斯·弗格森爵士（ Sir Alex Ferguson ）所取得的高度，…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025491/aston-villa-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Aston Villa latest: Emery confirms further contract talks to be held next week" data-title="Aston Villa latest: Emery confirms further contract talks to be held next week" data-date="11-06 22:25" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-06 22:25</span>
          <span class="news-item-title">阿斯顿维拉最新消息：埃默里确认下周将举行进一步的合同谈判</span>
          <span class="news-item-title-en">Aston Villa latest: Emery confirms further contract talks to be held next week</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqde8w0k2pz1o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="当埃利奥特·安德森（ Elliot Anderson ）在£ 1.16亿搬到曼城后返回诺丁汉森林（ Nottingham Forest ）时，他是否达到了价格要求？" data-title="Has Anderson lived up to the hype after Man City move?" data-date="11-06 20:00" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-06 20:00</span>
          <span class="news-item-title">曼城搬迁后，安德森是否辜负了炒作？</span>
          <span class="news-item-title-en">Has Anderson lived up to the hype after Man City move?</span>
          <span class="news-value-point">💡 当埃利奥特·安德森（ Elliot Anderson ）在£ 1.16亿搬到曼城后返回诺丁汉森林（ Nottingham Forest ）时，他…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13605773/david-moyes-interview-everton-manager-targeting-trophies-as-he-equals-harry-cattericks-record-for-games-managed" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="埃弗顿在英超联赛中排名第七，如果他们能在主场击败考文垂，他们有机会超越利物浦排名第五。他们也进入了对阵弗利特伍德的卡拉宝杯四分之一决赛。这对David Moyes来说是一个充满希望的开始。" data-title="Moyes opens up on Everton trophy target and his longevity ahead of landmark game" data-date="11-06 19:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-06 19:00</span>
          <span class="news-item-title">莫耶斯在具有里程碑意义的比赛前向埃弗顿奖杯目标和他的长寿开放</span>
          <span class="news-item-title-en">Moyes opens up on Everton trophy target and his longevity ahead of landmark game</span>
          <span class="news-value-point">💡 埃弗顿在英超联赛中排名第七，如果他们能在主场击败考文垂，他们有机会超越利物浦排名第五</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/508107.html" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="一举刷新“AI安全世界杯”CyberGym世界纪录" data-title="99.4%登顶全球第一！这个中国AI师承世界冠军" data-date="11-06 13:01" data-source="量子位">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-06 13:01</span>
          <span class="news-item-title">99.4%登顶全球第一！这个中国AI师承世界冠军</span>
          <span class="news-value-point">💡 一举刷新“AI安全世界杯”CyberGym世界纪录</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/06/premier-league-10-things-to-look-out-for-this-weekend" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Lampard在Everton的欣赏， Glasner引发了森林大火， Zubimendi和Kroupi在聚光灯下， Carrick诉EmeryPremier联赛得分最高者没有什么能更好地概括Farhad Moshiri领导下的Everton的功能障碍，而不是" data-title="Premier League: 10 things to look out for this weekend" data-date="11-06 08:01" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-06 08:01</span>
          <span class="news-item-title">英超联赛：本周末需要注意的10件事</span>
          <span class="news-item-title-en">Premier League: 10 things to look out for this weekend</span>
          <span class="news-value-point">💡 Lampard在Everton的欣赏， Glasner引发了森林大火， Zubimendi和Kroupi在聚光灯下， Carrick诉Emery…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cm4g112qp051o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育频道（ BBC Sport ）的幻想英超联赛（ Fantasy Premier League ）专家海森堡（ FPL Heisenberg ）回答了经理们在游戏周10中面临的一些最大困境。" data-title="Keep or sell Konsa? - FPL gameweek 10 dilemmas" data-date="11-06 06:26" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-06 06:26</span>
          <span class="news-item-title">保留或出售Konsa ？ - FPL游戏周10难题</span>
          <span class="news-item-title-en">Keep or sell Konsa? - FPL gameweek 10 dilemmas</span>
          <span class="news-value-point">💡 英国广播公司体育频道（ BBC Sport ）的幻想英超联赛（ Fantasy Premier League ）专家海森堡（ FPL Heise…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/football/derby-county-vs-bolton-wanderers/live/560671" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Derby vs Bolton LIVE!" data-title="Derby vs Bolton LIVE!" data-date="11-07 03:25" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-07 03:25</span>
          <span class="news-item-title">德比vs博尔顿现场直播！</span>
          <span class="news-item-title-en">Derby vs Bolton LIVE!</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/nfl/news/12040/13609007/antonio-brown-ex-nfl-wide-receiver-avoids-prison-after-pleading-guilty-to-aggravated-assault-with-a-firearm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="前NFL外接手安东尼奥·布朗（ Antonio Brown ）在承认与2025年在迈阿密名人拳击比赛外发生枪击事件有关的严重攻击后，避免了入狱时间。" data-title="Ex-NFL receiver Brown avoids prison after pleading guilty to reduced charge" data-date="11-07 03:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-07 03:00</span>
          <span class="news-item-title">前NFL接球手布朗在承认减刑后避免入狱</span>
          <span class="news-item-title-en">Ex-NFL receiver Brown avoids prison after pleading guilty to reduced charge</span>
          <span class="news-value-point">💡 前NFL外接手安东尼奥·布朗（ Antonio Brown ）在承认与2025年在迈阿密名人拳击比赛外发生枪击事件有关的严重攻击后，避免了入狱时…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/06/hundreds-of-artex-ai-hacking-tools-found-publicly-exposed-to-the-web/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="安全研究人员发现，数百台托管渗透测试工具Artex的服务器暴露在互联网上，允许任何人访问黑客工具。" data-title="Hundreds of Artex AI hacking tools found publicly exposed to the web" data-date="11-07 02:44" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-07 02:44</span>
          <span class="news-item-title">数百个公开暴露在网络中的Artex AI黑客工具</span>
          <span class="news-item-title-en">Hundreds of Artex AI hacking tools found publicly exposed to the web</span>
          <span class="news-value-point">💡 安全研究人员发现，数百台托管渗透测试工具Artex的服务器暴露在互联网上，允许任何人访问黑客工具</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/f1/live-blog/12040/13608010/f1-sao-paulo-gp-live-friday-practice-updates-results-stream-highlights-from-brazil-formula-1-race-weekend-at-interlagos" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Sao Paulo GP: Antonelli fastest in second practice LIVE!" data-title="Sao Paulo GP: Antonelli fastest in second practice LIVE!" data-date="11-07 02:40" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-07 02:40</span>
          <span class="news-item-title">圣保罗大奖赛：安东内利在现场第二次练习中跑得最快！</span>
          <span class="news-item-title-en">Sao Paulo GP: Antonelli fastest in second practice LIVE!</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/boxing/news/12040/13609000/chris-billam-smith-stares-down-cheavon-clarke-at-final-face-off-and-promises-saturdays-fight-will-be-a-violent-one" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Chris Billam-Smith和Cheavon Clarke睁大眼睛凝视着仪式结束。" data-title="Billam-Smith stares down Clarke and promises &#39;violent&#39; fight" data-date="11-07 02:30" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-07 02:30</span>
          <span class="news-item-title">Billam-Smith盯着Clarke并承诺“暴力”战斗</span>
          <span class="news-item-title-en">Billam-Smith stares down Clarke and promises 'violent' fight</span>
          <span class="news-value-point">💡 Chris Billam-Smith和Cheavon Clarke睁大眼睛凝视着仪式结束</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1028871/meta-muse-ai-spaces" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Meta现在允许您在其Muse AI助手中构建自定义的、类似于应用程序的体验。这项名为“空间”的新功能允许Muse构建购物中心、学校仪表板、音乐跟踪器、琐事游戏等，您可以" data-title="Meta’s Muse AI can create custom ‘spaces’ for the version of the app you need right now" data-date="11-07 02:10" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-07 02:10</span>
          <span class="news-item-title">Meta的Muse AI可以为您目前需要的应用版本创建自定义“空间”</span>
          <span class="news-item-title-en">Meta’s Muse AI can create custom ‘spaces’ for the version of the app you need right now</span>
          <span class="news-value-point">💡 Meta现在允许您在其Muse AI助手中构建自定义的、类似于应用程序的体验</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/podcast/how-a-blue-wave-midterm-might-reshape-the-ai-industry/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="民主党在本周美国中期选举中的历史性胜利也可能改变科技行业。公众周二投票通过了41项与数据中心相关的投票措施—除一项外，大多数人投票决定对数据施加更多限制" data-title="How a Blue Wave midterm might reshape the AI industry" data-date="11-07 02:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-07 02:00</span>
          <span class="news-item-title">Blue Wave期中考试如何重塑人工智能行业</span>
          <span class="news-item-title-en">How a Blue Wave midterm might reshape the AI industry</span>
          <span class="news-value-point">💡 民主党在本周美国中期选举中的历史性胜利也可能改变科技行业</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/f1/news/12040/13608869/ferrari-boss-frederic-vasseur-confirms-lewis-hamilton-charles-leclerc-meeting-after-mexico-clash-ahead-of-sao-paulo-gp" target="_blank" rel="noopener" data-cat="zonghe" data-summary="法拉利老板弗雷德里克·瓦瑟尔（ Frederic Vasseur ）表示，他提醒刘易斯·汉密尔顿（ Lewis Hamilton ）和查尔斯·勒克莱尔（ Charles Leclerc ） ，在本周末的圣保罗大奖赛（ Sao Paulo Grand Prix ）之前的一次会议上，" data-title="‘The message was clear’ - Vasseur holds Hamilton-Leclerc meeting after clash" data-date="11-07 02:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-07 02:00</span>
          <span class="news-item-title">“信息很明确” - Vasseur在冲突后举行Hamilton-Leclerc会议</span>
          <span class="news-item-title-en">‘The message was clear’ - Vasseur holds Hamilton-Leclerc meeting after clash</span>
          <span class="news-value-point">💡 法拉利老板弗雷德里克·瓦瑟尔（ Frederic Vasseur ）表示，他提醒刘易斯·汉密尔顿（ Lewis Hamilton ）和查尔斯·勒…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1028715/kobo-stack-cloud-sync-ebooks-epub-pdf-email-files" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Kobo正在推出一项名为Stack的新月度订阅服务，可让您将自己的电子书和文档上传到公司的服务器，在那里它们将跨多个设备和应用程序进行同步，包括您的阅读进度、亮点和" data-title="Kobo will soon let you upload and sync your own ebooks across devices, for a price" data-date="11-07 01:32" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-07 01:32</span>
          <span class="news-item-title">Kobo将很快允许您跨设备上传和同步自己的电子书，价格合理</span>
          <span class="news-item-title-en">Kobo will soon let you upload and sync your own ebooks across devices, for a price</span>
          <span class="news-value-point">💡 Kobo正在推出一项名为Stack的新月度订阅服务，可让您将自己的电子书和文档上传到公司的服务器，在那里它们将跨多个设备和应用程序进行同步，包括…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1028813/apple-iphone-duo-optimized-apps" target="_blank" rel="noopener" data-cat="zonghe" data-summary="苹果的iPhone Duo已经正式发售两周，该公司今天表示， App Store现在有超过10万个可折叠应用程序。“很高兴看到开发人员如此迅速地接受了iPhone Duo ，我们" data-title="The iPhone Duo has more than 100,000 optimized apps, Apple says" data-date="11-07 01:24" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-07 01:24</span>
          <span class="news-item-title">苹果表示， iPhone Duo拥有超过10万款优化应用</span>
          <span class="news-item-title-en">The iPhone Duo has more than 100,000 optimized apps, Apple says</span>
          <span class="news-value-point">💡 苹果的iPhone Duo已经正式发售两周，该公司今天表示， App Store现在有超过10万个可折叠应用程序</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/video/after-the-midterms-is-the-ai-industry-in-for-a-rough-two-years/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="民主党在本周美国中期选举中的历史性胜利也可能改变科技行业。公众周二投票通过了41项与数据中心相关的投票措施—除一项外，大多数人投票决定对数据施加更多限制" data-title="After the midterms, is the AI industry in for a rough two years?" data-date="11-07 01:23" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-07 01:23</span>
          <span class="news-item-title">期中考试结束后，人工智能行业是否会持续两年？</span>
          <span class="news-item-title-en">After the midterms, is the AI industry in for a rough two years?</span>
          <span class="news-value-point">💡 民主党在本周美国中期选举中的历史性胜利也可能改变科技行业</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/rugby-union/news/12040/13608973/england-rugby-jamie-george-says-squad-hurt-by-article-that-reported-rift-with-steve-borthwick-this-summer" target="_blank" rel="noopener" data-cat="zonghe" data-summary="杰米·乔治（ Jamie George ）表示，英格兰的球员因报纸报道夏季与主教练史蒂夫·博思维克（ Steve Borthwick ）的裂痕而“受伤” ，并称这篇文章的时机在周日与澳大利亚的国家锦标赛（ Nations Championship ）冲突之前“令人震惊”。" data-title="George: England players hurt by &#39;shocking&#39; report of rift with Borthwick" data-date="11-07 01:18" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-07 01:18</span>
          <span class="news-item-title">乔治：英格兰球员因与波斯威克的“令人震惊”的裂痕报告而受伤</span>
          <span class="news-item-title-en">George: England players hurt by 'shocking' report of rift with Borthwick</span>
          <span class="news-value-point">💡 杰米·乔治（ Jamie George ）表示，英格兰的球员因报纸报道夏季与主教练史蒂夫·博思维克（ Steve Borthwick ）的裂痕而…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/video/us/elections/100000011265557/the-voters-who-powered-the-blue-tsunami.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="与中期选举中的典型情况相比，年轻、多元化的选民帮助推动了民主党的决定性胜利，以及摇摆选民的收益和一些共和党选民的支持。《纽约时报》首席政治分析师内特·科恩（ Nate Cohn ）" data-title="The Voters Who Powered the Blue Tsunami" data-date="11-07 00:41" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-07 00:41</span>
          <span class="news-item-title">引发蓝色海啸的选民</span>
          <span class="news-item-title-en">The Voters Who Powered the Blue Tsunami</span>
          <span class="news-value-point">💡 与中期选举中的典型情况相比，年轻、多元化的选民帮助推动了民主党的决定性胜利，以及摇摆选民的收益和一些共和党选民的支持</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/f1/news/12040/13608857/sao-paulo-gp-lando-norris-tops-brazil-first-practice-in-upgraded-mclaren-from-kimi-antonelli-and-max-verstappen" target="_blank" rel="noopener" data-cat="zonghe" data-summary="兰多·诺里斯（ Lando Norris ）在圣保罗大奖赛（ Sao Paulo Grand Prix ）的首次练习中，从新的一级方程式世界冠军基米·安东内利（ Kimi Antonelli ）手中升" data-title="Norris tops Brazil first practice in upgraded McLaren" data-date="11-07 00:40" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-07 00:40</span>
          <span class="news-item-title">诺里斯在迈凯轮升级后的巴西首次练习中名列前茅</span>
          <span class="news-item-title-en">Norris tops Brazil first practice in upgraded McLaren</span>
          <span class="news-value-point">💡 兰多·诺里斯（ Lando Norris ）在圣保罗大奖赛（ Sao Paulo Grand Prix ）的首次练习中，从新的一级方程式世界冠军…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1028372/meta-quest-3s-headset-philips-hue-gradient-lightstrip-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="如果您对虚拟现实感到好奇， Meta的Quest 3S是一款很好的入门级耳机，可以让您的脚趾深陷其中，特别是现在它在翻新状态下直接从Meta的eBay店面以$ 255.99的价格出售，直到11月8日" data-title="Meta’s refurbished Quest 3S headset is nearly $100 off right now" data-date="11-07 00:39" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-07 00:39</span>
          <span class="news-item-title">Meta翻新的Quest 3S耳机现在折扣近100 $</span>
          <span class="news-item-title-en">Meta’s refurbished Quest 3S headset is nearly $100 off right now</span>
          <span class="news-value-point">💡 如果您对虚拟现实感到好奇， Meta的Quest 3S是一款很好的入门级耳机，可以让您的脚趾深陷其中，特别是现在它在翻新状态下直接从Meta的e…</span>
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


<p class="news-updated">🕐 抓取更新于 2026-11-07 03:35（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
