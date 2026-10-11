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
      <span>2026-10-12 01:43 抓取更新</span>
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
        <span class="channel-count">55</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('shizheng', this)">
        <span>🏛️ 时政与国际</span>
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('keji', this)">
        <span>🤖 AI模型 & 芯片算力</span>
        <span class="channel-count">12</span>
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
  <div class="ov-item"><span class="ov-num">55</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×15 · 卫报×8</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.nytimes.com/2026/10/11/world/middleeast/saudi-arabia-options-houthis.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="伊朗支持的胡塞武装在也门对沙特首都机场的三次致命袭击凸显了他们与沙特王国冲突的不对称性。" data-title="Saudi Arabia Has Few Options as Houthis Aim at Heart of Its Ambitions" data-date="10-12 01:20" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 10-12 01:20</span>
      </div>
      <h2 class="hero-featured-title">沙特阿拉伯几乎没有选择，因为胡塞武装瞄准其野心的核心</h2>
      <div class="hero-featured-title-en">Saudi Arabia Has Few Options as Houthis Aim at Heart of Its Ambitions</div>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://techcrunch.com/2026/10/11/can-the-ai-industry-persuade-data-center-opponents-by-getting-rid-of-ndas/" target="_blank" rel="noopener" data-cat="keji" data-summary="在Equity上，我们讨论了数据中心暂停的影响以及人工智能行业是否存在通信问题。" data-title="Can the AI industry persuade data center opponents by getting rid of NDAs?" data-date="10-12 00:52" data-source="TechCrunch">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
      </div>
      <p class="hero-sub-title">Can the AI industry persuade data center opponents by getting rid of NDAs?</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/live/2026/oct/11/liverpool-v-manchester-city-premier-league-live-score-updates" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="⚽ 英超联赛在安菲尔德⚽现场比赛得分摊牌后的反应|桌子|最佳射手|您可以给我们发邮件威尔·昂温（ Will Unwin ）的最新消息，他是我们安菲尔德队今天比赛的一员600多名曼城球迷获得了警察Esc" data-title="Liverpool 0-3 Manchester City: Premier League – live" data-date="10-12 01:42" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Liverpool 0-3 Manchester City: Premier League – live</p>
    </a>
    <a class="hero-sub-card" href="https://www.nytimes.com/2026/10/11/us/politics/elections-political-violence-harassment.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="《泰晤士报》的一项调查发现，暴力威胁已成为公职人员的新常态，重塑了私人生活，造成数百万美元的安全损失，并将人们赶下台。" data-title="Threats of Political Violence Have America’s Elected Officials Living in Fear" data-date="10-12 00:28" data-source="纽约时报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
      </div>
      <p class="hero-sub-title">Threats of Political Violence Have America’s Elected Officials Living in Fear</p>
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
        <a class="news-item" href="https://www.nytimes.com/2026/10/11/world/middleeast/saudi-arabia-options-houthis.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="伊朗支持的胡塞武装在也门对沙特首都机场的三次致命袭击凸显了他们与沙特王国冲突的不对称性。" data-title="Saudi Arabia Has Few Options as Houthis Aim at Heart of Its Ambitions" data-date="10-12 01:20" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-12 01:20</span>
          <span class="news-item-title">沙特阿拉伯几乎没有选择，因为胡塞武装瞄准其野心的核心</span>
          <span class="news-item-title-en">Saudi Arabia Has Few Options as Houthis Aim at Heart of Its Ambitions</span>
          <span class="news-value-point">💡 伊朗支持的胡塞武装在也门对沙特首都机场的三次致命袭击凸显了他们与沙特王国冲突的不对称性</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/11/world/europe/trump-zelensky-diesel-energy-russia-.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="特朗普总统猛烈抨击总统弗拉基米尔·泽伦斯基（ Volodymyr Zelensky ）袭击俄罗斯炼油厂。泽伦斯基说，如果俄罗斯也这样做，他会停止。" data-title="Ukraine Shrugs Off Trump Call to Ditch Zelensky for Energy Strikes" data-date="10-12 00:39" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-12 00:39</span>
          <span class="news-item-title">乌克兰耸耸肩特朗普呼吁抛弃泽伦斯基的能源罢工</span>
          <span class="news-item-title-en">Ukraine Shrugs Off Trump Call to Ditch Zelensky for Energy Strikes</span>
          <span class="news-value-point">💡 特朗普总统猛烈抨击总统弗拉基米尔·泽伦斯基（ Volodymyr Zelensky ）袭击俄罗斯炼油厂</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-12/10711157.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="国际移民组织11日表示，一艘载有350人的移民船在吉布提沿海倾覆，造成至少139人死亡，另有84人失踪。" data-title="吉布提沿海移民船只倾覆事故死亡人数升至139人" data-date="10-12 00:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 00:29</span>
          <span class="news-item-title">吉布提沿海移民船只倾覆事故死亡人数升至139人</span>
          <span class="news-value-point">💡 国际移民组织11日表示，一艘载有350人的移民船在吉布提沿海倾覆，造成至少139人死亡，另有84人失踪</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-12/10711156.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="2026年是中国工农红军长征胜利90周年。肯尼亚“首都调频”网站10月10日刊文称，今天的中国拥有现代化的城市和规模庞大的消费市场，但人们很容易忽略，走到这一步的道路有多么漫长和艰难。这正是长征精神的意义所在，这种精神是“值得非洲探讨的国家发展理念”。" data-title="全球媒体聚焦 | “长征是值得非洲探讨的国家发展理念”" data-date="10-12 00:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-12 00:13</span>
          <span class="news-item-title">全球媒体聚焦 | “长征是值得非洲探讨的国家发展理念”</span>
          <span class="news-value-point">💡 2026年是中国工农红军长征胜利90周年</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-11/10711153.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社曼谷10月11日电 (梁峻祥 李映民)2026年国际货币基金组织(IMF)和世界银行集团年会将于10月12日至18日在泰国曼谷举行。随着会议临近，泰国政府进一步加强安保、交通、防洪及城市运行等保障工作，以确保会议顺利举行。" data-title="IMF和世行年会将在曼谷举行 泰国加强安保和城市保障" data-date="10-11 23:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-11 23:56</span>
          <span class="news-item-title">IMF和世行年会将在曼谷举行 泰国加强安保和城市保障</span>
          <span class="news-value-point">💡 中新社曼谷10月11日电 (梁峻祥 李映民)2026年国际货币基金组织(IMF)和世界银行集团年会将于10月12日至18日在泰国曼谷举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-11/10711155.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月11日电 (吴昕妮)波黑前部长会议主席兹拉特科·拉古姆季亚(Zlatko Lagumdzija)11日在北京表示，当前，外界普遍关注中国的发展奇迹。但最让他印象深刻的是，在快速变化的世界中，中国所展现出的长期主义思维。" data-title="波黑前部长会议主席：中国以长远眼光谋划未来" data-date="10-11 23:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-11 23:52</span>
          <span class="news-item-title">波黑前部长会议主席：中国以长远眼光谋划未来</span>
          <span class="news-value-point">💡 中新社北京10月11日电 (吴昕妮)波黑前部长会议主席兹拉特科·拉古姆季亚(Zlatko Lagumdzija)11日在北京表示，当前，外界普遍…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-11/10711147.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月11日电 (刘梦青)澳大利亚前总理陆克文11日在北京表示，亚太地区各成员尽管存在差异与竞争，仍要管控分歧、拓展合作，共建平等开放的亚太共同体。" data-title="澳大利亚前总理陆克文：呼吁共建平等开放的亚太共同体" data-date="10-11 23:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-11 23:41</span>
          <span class="news-item-title">澳大利亚前总理陆克文：呼吁共建平等开放的亚太共同体</span>
          <span class="news-value-point">💡 中新社北京10月11日电 (刘梦青)澳大利亚前总理陆克文11日在北京表示，亚太地区各成员尽管存在差异与竞争，仍要管控分歧、拓展合作，共建平等开放…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-11/10711145.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社深圳10月11日电 (记者 郭超凯)由中国外交学院主办的第三次中柬泰二轨对话会11日在深圳举行。泰国前外长甲西·披龙耶在参会期间接受中新社记者采访时表示，乐见中方调停斡旋泰柬边境冲突，泰柬须尊重中国对两国释放的善意。" data-title="泰国前外长：乐见中方调停斡旋泰柬边境冲突" data-date="10-11 23:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-11 23:31</span>
          <span class="news-item-title">泰国前外长：乐见中方调停斡旋泰柬边境冲突</span>
          <span class="news-value-point">💡 中新社深圳10月11日电 (记者 郭超凯)由中国外交学院主办的第三次中柬泰二轨对话会11日在深圳举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-11/10711149.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间10月11日，沙特阿拉伯主导的多国联军发言人图尔基·马利基发布消息称，一枚不明投射物袭击了沙特首都利雅得哈立德国王国际机场4号旅客航站楼，袭击引发火灾，目前相关地点正由主管部门处置。" data-title="沙特主导联军称利雅得机场航站楼遭袭" data-date="10-11 23:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-11 23:17</span>
          <span class="news-item-title">沙特主导联军称利雅得机场航站楼遭袭</span>
          <span class="news-value-point">💡 当地时间10月11日，沙特阿拉伯主导的多国联军发言人图尔基·马利基发布消息称，一枚不明投射物袭击了沙特首都利雅得哈立德国王国际机场4号旅客航站楼…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-11/10711142.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社深圳10月11日电 (记者 郭超凯)由中国外交学院主办的“落实抚仙会晤共识 夯实持久和平根基”第三次中柬泰二轨对话会11日在深圳举行。来自中国、柬埔寨、泰国三国的智库学者、社会组织和人道机构代表以及高校青年学子等近百人参会。" data-title="第三次中柬泰二轨对话会举行 推动落实抚仙会晤共识" data-date="10-11 23:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-11 23:12</span>
          <span class="news-item-title">第三次中柬泰二轨对话会举行 推动落实抚仙会晤共识</span>
          <span class="news-value-point">💡 中新社深圳10月11日电 (记者 郭超凯)由中国外交学院主办的“落实抚仙会晤共识 夯实持久和平根基”第三次中柬泰二轨对话会11日在深圳举行</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/11/us/politics/democrats-press-pentagon-on-iran-civilian-deaths.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="74名议员的一封新信表明，如果民主党控制国会，平民伤亡将成为调查的焦点。" data-title="Democrats Press Pentagon on Iran Civilian Deaths" data-date="10-11 22:36" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-11 22:36</span>
          <span class="news-item-title">民主党人就伊朗平民死亡事件向五角大楼发表讲话</span>
          <span class="news-item-title-en">Democrats Press Pentagon on Iran Civilian Deaths</span>
          <span class="news-value-point">💡 74名议员的一封新信表明，如果民主党控制国会，平民伤亡将成为调查的焦点</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-11/10711124.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网宁德10月11日电 (记者 叶茂)2026年是中国工农红军长征胜利90周年。11日，《苍穹之剑——纪念无名英雄蔡威百幅画卷》展览在福建省宁德市举办。" data-title="《苍穹之剑——纪念无名英雄蔡威百幅画卷》在福建宁德首展" data-date="10-11 20:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-11 20:57</span>
          <span class="news-item-title">《苍穹之剑——纪念无名英雄蔡威百幅画卷》在福建宁德首展</span>
          <span class="news-value-point">💡 中新网宁德10月11日电 (记者 叶茂)2026年是中国工农红军长征胜利90周年</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-11/10711120.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社东京10月11日电#8195;题：一部纪录片引发的追问：日本政府究竟保护谁？" data-title="一部纪录片引发的追问：日本政府究竟保护谁？" data-date="10-11 20:46" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-11 20:46</span>
          <span class="news-item-title">一部纪录片引发的追问：日本政府究竟保护谁？</span>
          <span class="news-value-point">💡 新华社东京10月11日电#8195;题：一部纪录片引发的追问：日本政府究竟保护谁</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-11/10711109.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社雅加达10月11日电 (记者 李志全)印度尼西亚总统普拉博沃11日与到访的埃及总统塞西举行会谈，双方重申支持建立独立的巴勒斯坦国，强调通过“两国方案”实现地区和平，并呼吁缓和中东地区紧张局势。" data-title="埃及总统塞西访印尼  两国重申支持巴勒斯坦建国" data-date="10-11 20:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-11 20:45</span>
          <span class="news-item-title">埃及总统塞西访印尼  两国重申支持巴勒斯坦建国</span>
          <span class="news-value-point">💡 中新社雅加达10月11日电 (记者 李志全)印度尼西亚总统普拉博沃11日与到访的埃及总统塞西举行会谈，双方重申支持建立独立的巴勒斯坦国，强调通过…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-11/10711087.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网西安10月11日电 (记者 孙自法)记者10月11日从中国科学院地球环境研究所(地环所)获悉，“一带一路”地区极端气候事件及影响国际培训班当天在陕西西安开班，以“极端气候事件重建、预警与影响评估”为核心主题，对来自10多个国家的20余名优秀学员，开展为期14天的培训。" data-title="“一带一路”地区极端气候事件及影响国际培训班在西安开班" data-date="10-11 19:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-11 19:55</span>
          <span class="news-item-title">“一带一路”地区极端气候事件及影响国际培训班在西安开班</span>
          <span class="news-value-point">💡 中新网西安10月11日电 (记者 孙自法)记者10月11日从中国科学院地球环境研究所(地环所)获悉，“一带一路”地区极端气候事件及影响国际培训班…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">12 条</span>
    </div>
        <a class="news-item" href="https://techcrunch.com/2026/10/11/can-the-ai-industry-persuade-data-center-opponents-by-getting-rid-of-ndas/" target="_blank" rel="noopener" data-cat="keji" data-summary="在Equity上，我们讨论了数据中心暂停的影响以及人工智能行业是否存在通信问题。" data-title="Can the AI industry persuade data center opponents by getting rid of NDAs?" data-date="10-12 00:52" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-12 00:52</span>
          <span class="news-item-title">人工智能行业能否通过摆脱保密协议来说服数据中心的对手？</span>
          <span class="news-item-title-en">Can the AI industry persuade data center opponents by getting rid of NDAs?</span>
          <span class="news-value-point">💡 在Equity上，我们讨论了数据中心暂停的影响以及人工智能行业是否存在通信问题</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/714.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 11 日消息，苹果将在本周二举行“欢迎回家”活动，主角预计是 HomeView 智能家庭中枢，除此之外还有新款 HomePod mini 和 Apple TV 4K。据彭博社记者马克 · 古尔曼今日透露，新款 Apple TV 4K 将在 10 月 30 日发售，苹果已在这款新品中测试内置麦克风，用户直接说出 Siri 就能进行语音交互。IT之家了解到，现款 Apple TV 4K 仅在 Siri Remote 中带有麦克风，用户必须对着遥控器或 HomePod 说话，才能使用 Siri。同时，苹果还将重新设计 Siri Remote 遥控器，这款配件将内置扬声器，方便用户找出掉在沙发坐垫的遥控器。此外，新款 HomePod mini 预计将配备 S10 芯片，同样也是" data-title="曝苹果新一代 Apple TV 4K 内置麦克风、Siri Remote 遥控器将配扬声器便于查找" data-date="10-11 23:20" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-11 23:20</span>
          <span class="news-item-title">曝苹果新一代 Apple TV 4K 内置麦克风、Siri Remote 遥控器将配扬声器便于查找</span>
          <span class="news-value-point">💡 IT之家 10 月 11 日消息，苹果将在本周二举行“欢迎回家”活动，主角预计是 HomeView 智能家庭中枢，除此之外还有新款 HomePo…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/711.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 11 日消息，据博主 @体验more 爆料，荣耀 WIN Pad 平板搭载第五代骁龙 8 至尊版处理器，配备 8.4 英寸 240Hz OLED 平板、主动散热风扇，和 iQOO Pad Pro 都是本月发布。据博主 @数码闲聊站 于 9 月 21 日爆料，荣耀 WIN2 系列 +WIN Pad 小平板确定 10 月发布。据其爆料，荣耀 WIN2 系列顶配搭载骁龙 8EE6（第六代骁龙 8 超级至尊版处理器）+ 主动散热风扇 + 超高刷 OLED ，今年唯一万级大电池的 2nm 新机。小平板搭载骁龙 8E5（第五代骁龙 8 至尊版处理器）+ 主动散热风扇 +8 英寸级别超高刷 OLED，没有 5G 通信版本。此外，该博主 @数码闲聊站 后续再爆料，荣耀 WIN Pad 小" data-title="消息称荣耀 WIN Pad 平板搭载 8.4 英寸 240Hz OLED 屏，本月发布" data-date="10-11 22:55" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-11 22:55</span>
          <span class="news-item-title">消息称荣耀 WIN Pad 平板搭载 8.4 英寸 240Hz OLED 屏，本月发布</span>
          <span class="news-value-point">💡 IT之家 10 月 11 日消息，据博主 @体验more 爆料，荣耀 WIN Pad 平板搭载第五代骁龙 8 至尊版处理器，配备 8.4 英寸 …</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/708.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 11 日消息，粤芯半导体技术股份有限公司今日宣布，公司将于 2026 年 10 月 13 日（下周二）在深圳证券交易所创业板上市。本次发行价格为 12.01 元 / 股，发行后总股本为 28.78 亿股（超额配售选择权行使前）。IT之家了解到，粤芯半导体已在 9 月 28 日公开网上摇号中签结果，中签号码共有 358848 个，每个中签号码可认购 500 股粤芯半导体 A 股股票。本次发行最终战略配售数量为 25632.30 万股，网上最终发行数量为 17942.40 万股，网下最终发行数量为 15379.50 万股。网上投资者放弃认购 468976 股，由广发证券包销，包销金额 563.24 万元。互联网公开资料显示，粤芯半导体成立于 2017 年，总部位于广州市黄埔区" data-title="粤芯半导体 10 月 13 日在创业板上市，发行价为 12.01 元 / 股" data-date="10-11 22:27" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-11 22:27</span>
          <span class="news-item-title">粤芯半导体 10 月 13 日在创业板上市，发行价为 12.01 元 / 股</span>
          <span class="news-value-point">💡 IT之家 10 月 11 日消息，粤芯半导体技术股份有限公司今日宣布，公司将于 2026 年 10 月 13 日（下周二）在深圳证券交易所创业板…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/modder-discovers-that-putting-a-gpu-in-the-wrong-place-can-deliver-a-19-degree-cooler-hotspot-breaking-convention-can-produce-great-results-despite-decades-of-pc-diy-evolution" target="_blank" rel="noopener" data-cat="keji" data-summary="在PC DIY中，它可能仍然值得挑战传统，正如TrashBench所展示的那样，他的GPU热点最高可达19摄氏度。" data-title="Modder discovers that putting a GPU in the &#39;wrong place&#39; can deliver a 19 degree cooler hotspot" data-date="10-11 22:23" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-11 22:23</span>
          <span class="news-item-title">Modder发现，将GPU放在“错误的位置”可以提供19度更冷的热点</span>
          <span class="news-item-title-en">Modder discovers that putting a GPU in the 'wrong place' can deliver a 19 degree cooler hotspot</span>
          <span class="news-value-point">💡 在PC DIY中，它可能仍然值得挑战传统，正如TrashBench所展示的那样，他的GPU热点最高可达19摄氏度</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/11/these-execs-think-voice-ai-hasnt-reached-its-chatgpt-moment-yet/" target="_blank" rel="noopener" data-cat="keji" data-summary="语音人工智能经常错过上下文层的重要点，并导致整个管道中断" data-title="These execs think voice AI hasn’t reached its ChatGPT moment yet" data-date="10-11 22:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-11 22:00</span>
          <span class="news-item-title">这些高管认为语音AI尚未达到ChatGPT时刻</span>
          <span class="news-item-title-en">These execs think voice AI hasn’t reached its ChatGPT moment yet</span>
          <span class="news-value-point">💡 语音人工智能经常错过上下文层的重要点，并导致整个管道中断</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1008484/learning-local-ai-hermes-qwen-model-mac-studio-testing-diary-progress" target="_blank" rel="noopener" data-cat="keji" data-summary="我正在踏上一段迄今为止一直犹豫不决的旅程：实际上是定期使用人工智能。将大多数个人数据提供给云服务对我来说是一个主要障碍，但越来越有可能在本地运行强大的模型，以了解" data-title="Learning to use local AI is exciting, overwhelming, and frustrating" data-date="10-11 19:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-11 19:00</span>
          <span class="news-item-title">学习使用本地人工智能是令人兴奋、不知所措和令人沮丧的</span>
          <span class="news-item-title-en">Learning to use local AI is exciting, overwhelming, and frustrating</span>
          <span class="news-value-point">💡 我正在踏上一段迄今为止一直犹豫不决的旅程：实际上是定期使用人工智能</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/502585.html" target="_blank" rel="noopener" data-cat="keji" data-summary="马斯克连横A社，硅谷VC开始囤GPU" data-title="硅谷AI现状：谁有算力谁是爹" data-date="10-11 13:22" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-11 13:22</span>
          <span class="news-item-title">硅谷AI现状：谁有算力谁是爹</span>
          <span class="news-value-point">💡 马斯克连横A社，硅谷VC开始囤GPU</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/502544.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Grok Bot我养不起，ds bot不得高低尝尝咸淡？" data-title="DeepSeek Bot来了！民间版，DSH装个插件就能用" data-date="10-11 11:27" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-11 11:27</span>
          <span class="news-item-title">DeepSeek Bot来了！民间版，DSH装个插件就能用</span>
          <span class="news-value-point">💡 Grok Bot我养不起，ds bot不得高低尝尝咸淡</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1009337/satya-nadella-says-we-should-assume-all-ai-models-are-compromised" target="_blank" rel="noopener" data-cat="keji" data-summary="在X的一篇长文中，微软首席执行官阐述了他对高度先进的人工智能模型带来的危险以及如何应对这些风险的看法。纳德拉说，我们再也不能接受一个将人工智能视为“一组嵌套的黑匣子”的世界，" data-title="Satya Nadella says we should assume all AI models are ‘compromised’" data-date="10-11 06:10" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-11 06:10</span>
          <span class="news-item-title">萨蒂亚·纳德拉（ Satya Nadella ）说，我们应该假设所有的人工智能模型都“</span>
          <span class="news-item-title-en">Satya Nadella says we should assume all AI models are ‘compromised’</span>
          <span class="news-value-point">💡 在X的一篇长文中，微软首席执行官阐述了他对高度先进的人工智能模型带来的危险以及如何应对这些风险的看法</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/10/microsofts-satya-nadella-says-ai-models-need-an-emergency-brake/" target="_blank" rel="noopener" data-cat="keji" data-summary="在周六早上的帖子中，微软首席执行官写道，现在是时候“退一步评估人工智能的信任架构”了。" data-title="Microsoft’s Satya Nadella says AI models need an ‘emergency brake’" data-date="10-11 05:47" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-11 05:47</span>
          <span class="news-item-title">微软的萨蒂亚·纳德拉（ Satya Nadella ）表示，人工智能模型需要“紧急制动”</span>
          <span class="news-item-title-en">Microsoft’s Satya Nadella says AI models need an ‘emergency brake’</span>
          <span class="news-value-point">💡 在周六早上的帖子中，微软首席执行官写道，现在是时候“退一步评估人工智能的信任架构”了</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/10/apple-discloses-deal-to-hire-team-and-license-tech-from-personalized-podcast-startup-huxe/" target="_blank" rel="noopener" data-cat="keji" data-summary="苹果是否希望进入人工智能生成的播客业务？" data-title="Apple discloses deal to hire team and license tech from personalized podcast startup Huxe" data-date="10-11 03:50" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-11 03:50</span>
          <span class="news-item-title">苹果披露从个性化播客初创公司Huxe聘请团队和许可技术的交易</span>
          <span class="news-item-title-en">Apple discloses deal to hire team and license tech from personalized podcast startup Huxe</span>
          <span class="news-value-point">💡 苹果是否希望进入人工智能生成的播客业务</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">13 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/11/liverpool-v-manchester-city-premier-league-live-score-updates" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="⚽ 英超联赛在安菲尔德⚽现场比赛得分摊牌后的反应|桌子|最佳射手|您可以给我们发邮件威尔·昂温（ Will Unwin ）的最新消息，他是我们安菲尔德队今天比赛的一员600多名曼城球迷获得了警察Esc" data-title="Liverpool 0-3 Manchester City: Premier League – live" data-date="10-12 01:42" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-12 01:42</span>
          <span class="news-item-title">利物浦0-3曼城：英超联赛–直播</span>
          <span class="news-item-title-en">Liverpool 0-3 Manchester City: Premier League – live</span>
          <span class="news-value-point">💡 ⚽ 英超联赛在安菲尔德⚽现场比赛得分摊牌后的反应|桌子|最佳射手|您可以给我们发邮件威尔·昂温（ Will Unwin ）的最新消息，他是我们安…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/11/liverpool-manchester-city-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="这是曼城以前听过的配乐，但在比赛期间从未有过如此持续的爆发。它来自利物浦的支持，在开球前先在安菲尔德周围响起，然后定期来。它总是" data-title="Cherki cracker caps Manchester City win at Liverpool in face of Anfield taunts" data-date="10-12 01:42" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-12 01:42</span>
          <span class="news-item-title">面对安菲尔德的嘲讽，切尔基·克拉克（ Cherki Cracker ）在利物浦夺冠</span>
          <span class="news-item-title-en">Cherki cracker caps Manchester City win at Liverpool in face of Anfield taunts</span>
          <span class="news-value-point">💡 这是曼城以前听过的配乐，但在比赛期间从未有过如此持续的爆发</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ck87z1jjynyqo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦和曼城球员在英超比赛后的评分。" data-title="Cherki sparkles but who must do more? - player ratings for Liverpool v Man City" data-date="10-12 01:30" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-12 01:30</span>
          <span class="news-item-title">切尔基闪闪发光，但谁必须做得更多？ -利物浦对曼城的球员评分</span>
          <span class="news-item-title-en">Cherki sparkles but who must do more? - player ratings for Liverpool v Man City</span>
          <span class="news-value-point">💡 利物浦和曼城球员在英超比赛后的评分</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/10/premier-league-top-scorers-2026-27-race-for-golden-boot" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="找出哪位英国顶尖射手正在向进球排行榜射击。继续阅读……" data-title="Premier League top scorers 2026-27: who is leading race for the golden boot?" data-date="10-12 01:26" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-12 01:26</span>
          <span class="news-item-title">2026-27赛季英超联赛最佳射手：谁是金靴赛的领跑者？</span>
          <span class="news-item-title-en">Premier League top scorers 2026-27: who is leading race for the golden boot?</span>
          <span class="news-value-point">💡 找出哪位英国顶尖射手正在向进球排行榜射击</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/11/tension-banners-and-inflatable-bananas-manchester-citys-welcome-to-anfield" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="煽动性的气氛迎接了前英超冠军的第一场比赛，因为他们被判犯有违反金融公平竞争规则的罪行粉丝们在安菲尔德的街道上排队，为曼城队巴士的到来做准备，" data-title="Tension, ‘cheat’ banners and inflatable bananas: Manchester City’s welcome to Anfield" data-date="10-12 00:50" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-12 00:50</span>
          <span class="news-item-title">紧张气氛、“作弊”横幅和充气香蕉：曼城欢迎您来到安菲尔德</span>
          <span class="news-item-title-en">Tension, ‘cheat’ banners and inflatable bananas: Manchester City’s welcome to Anfield</span>
          <span class="news-value-point">💡 煽动性的气氛迎接了前英超冠军的第一场比赛，因为他们被判犯有违反金融公平竞争规则的罪行粉丝们在安菲尔德的街道上排队，为曼城队巴士的到来做准备，</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/11/hull-city-everton-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="自从回到英超联赛以来，赫尔在MKM体育场与埃弗顿进行了一场有趣的平局，保持了他们不败的主场纪录。布伦南·约翰逊在第34分钟发现了球网，但没有得到埃弗顿的第一个英超联赛进球。" data-title="Mohamed Belloumi grabs point for Hull in seesaw draw with Everton" data-date="10-11 23:13" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-11 23:13</span>
          <span class="news-item-title">穆罕默德·贝卢米（ Mohamed Belloumi ）与埃弗顿（ Everton ）在跷跷板平局中</span>
          <span class="news-item-title-en">Mohamed Belloumi grabs point for Hull in seesaw draw with Everton</span>
          <span class="news-value-point">💡 自从回到英超联赛以来，赫尔在MKM体育场与埃弗顿进行了一场有趣的平局，保持了他们不败的主场纪录</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cvy0rp14xz7lo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼城周日访问利物浦，他们身上笼罩着许多不确定性。Phil McNulty着眼于未来。" data-title="Toxicity and uncertainty await Man City - will their season even matter?" data-date="10-11 13:27" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-11 13:27</span>
          <span class="news-item-title">毒性和不确定性等待着曼城-他们的季节重要吗？</span>
          <span class="news-item-title-en">Toxicity and uncertainty await Man City - will their season even matter?</span>
          <span class="news-value-point">💡 曼城周日访问利物浦，他们身上笼罩着许多不确定性</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqn73g3pvezdo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="罗伯托·德·泽尔比（ Roberto de Zerbi ）在对阵曼联的1-1平局中被罚下场后，赞扬了罗德里戈·本坦库尔（ Rodrigo B" data-title="&#39;I kissed Rodrigo and said thanks&#39; - De Zerbi &#39;liked&#39; Spurs red card" data-date="10-11 04:58" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-11 04:58</span>
          <span class="news-item-title">“我吻了罗德里戈并表示感谢” -德泽尔比“喜欢”马刺红牌</span>
          <span class="news-item-title-en">'I kissed Rodrigo and said thanks' - De Zerbi 'liked' Spurs red card</span>
          <span class="news-value-point">💡 罗伯托·德·泽尔比（ Roberto de Zerbi ）在对阵曼联的1-1平局中被罚下场后，赞扬了罗德里戈·本坦库尔（ Rodrigo B</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c62e9g09e781o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="不会再发生了吧？在对阵托特纳姆热刺1-1战平后，又一次未能击败10名男子，增加了曼联老板迈克尔·卡里克的压力。" data-title="Boos, anguish &amp; fading belief - &#39;worrying day&#39; for under-pressure Carrick" data-date="10-11 04:54" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-11 04:54</span>
          <span class="news-item-title">嘘声，痛苦和逐渐消失的信念-压力不足的卡里克的“令人担忧的一天”</span>
          <span class="news-item-title-en">Boos, anguish & fading belief - 'worrying day' for under-pressure Carrick</span>
          <span class="news-value-point">💡 不会再发生了吧</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/10/manchester-united-v-tottenham-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="多米尼克·索兰克（ Dominic Solanke ）为马刺队赢得了应得的积分，尽管罗德里戈·本坦库尔（ Rodrigo Bentancur ）的红牌马刺队他们在上半场向斯特雷特福德尽头踢去。球队出局了。曼联著名的红色、白色和黑色，" data-title="Manchester United 1-1 Tottenham: Premier League – as it happened" data-date="10-11 03:31" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-11 03:31</span>
          <span class="news-item-title">曼联1-1托特纳姆热刺：英超联赛–实际情况</span>
          <span class="news-item-title-en">Manchester United 1-1 Tottenham: Premier League – as it happened</span>
          <span class="news-value-point">💡 多米尼克·索兰克（ Dominic Solanke ）为马刺队赢得了应得的积分，尽管罗德里戈·本坦库尔（ Rodrigo Bentancur ）…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqvgrey535n4o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="富勒姆主帅阿尔瓦罗·阿贝洛亚（ Alvaro Arbeloa ）表示，在伊普斯维奇（ Ipswich ）失利后，他不会“感到恐惧” ，他在六场比赛中失去了胜利，并在英超联赛" data-title="Arbeloa &#39;doesn&#39;t feel fear&#39; but pressure increases after loss" data-date="10-11 03:03" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-11 03:03</span>
          <span class="news-item-title">Arbeloa “不会感到恐惧” ，但损失后压力会增加</span>
          <span class="news-item-title-en">Arbeloa 'doesn't feel fear' but pressure increases after loss</span>
          <span class="news-value-point">💡 富勒姆主帅阿尔瓦罗·阿贝洛亚（ Alvaro Arbeloa ）表示，在伊普斯维奇（ Ipswich ）失利后，他不会“感到恐惧” ，他在六场比…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/10/why-premier-league-in-clutches-of-global-mega-rich" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在一个张开双臂欢迎富裕的国际业主的国家，这种模式几乎不可能改变。足球是世界上最受欢迎的运动，由1863年在伦敦制定的法律进行。英超联赛是英国最大的软实力" data-title="Why we’re stuck with a Premier League in the clutches of the global mega-rich | Jonathan Wilson" data-date="10-11 03:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-11 03:00</span>
          <span class="news-item-title">为什么我们被困在全球超级富豪的魔掌中|乔纳森·威尔逊</span>
          <span class="news-item-title-en">Why we’re stuck with a Premier League in the clutches of the global mega-rich | Jonathan Wilson</span>
          <span class="news-value-point">💡 在一个张开双臂欢迎富裕的国际业主的国家，这种模式几乎不可能改变</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/articles/cw3dj5yx4ej2o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="乔丹·亨德森（ Jordan Henderson ）和莫伊塞斯·凯塞多（ Moises Caicedo ）的表现巩固了周六下午切尔西在主场对伯恩茅斯的5-1胜利。" data-title="The rock behind Chelsea&#39;s entertainers: Midfield duo key for Blues" data-date="10-11 02:09" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-11 02:09</span>
          <span class="news-item-title">切尔西艺人背后的摇滚：蓝调中场二人组关键</span>
          <span class="news-item-title-en">The rock behind Chelsea's entertainers: Midfield duo key for Blues</span>
          <span class="news-value-point">💡 乔丹·亨德森（ Jordan Henderson ）和莫伊塞斯·凯塞多（ Moises Caicedo ）的表现巩固了周六下午切尔西在主场对伯恩…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/10/11/us/politics/elections-political-violence-harassment.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="《泰晤士报》的一项调查发现，暴力威胁已成为公职人员的新常态，重塑了私人生活，造成数百万美元的安全损失，并将人们赶下台。" data-title="Threats of Political Violence Have America’s Elected Officials Living in Fear" data-date="10-12 00:28" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-12 00:28</span>
          <span class="news-item-title">政治暴力的威胁让美国民选官员生活在恐惧之中</span>
          <span class="news-item-title-en">Threats of Political Violence Have America’s Elected Officials Living in Fear</span>
          <span class="news-value-point">💡 《泰晤士报》的一项调查发现，暴力威胁已成为公职人员的新常态，重塑了私人生活，造成数百万美元的安全损失，并将人们赶下台</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/software/linux/cyberleek-threatens-full-gta-6-build-leak-unless-take-two-apologizes-and-his-usd30-million-crypto-memecoin-goal-is-met-leaker-demands-physical-release-while-pumping-solana-memecoin-to-usd30m" target="_blank" rel="noopener" data-cat="zonghe" data-summary="臭名昭著的GTA VI泄密者Cyberleek威胁要发布GTA VI的完整版本，如果Take-Two不发布物理版本，但前提是其memecoin达到3000万美元。" data-title="Cyberleek threatens full GTA 6 build leak unless Take-Two apologizes and his $30 million crypto memecoin goal is met" data-date="10-12 00:10" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-12 00:10</span>
          <span class="news-item-title">Cyberleek威胁要全面泄露GTA 6版本，除非Take-Two道歉并实现其3000万美元的加密memecoin目标</span>
          <span class="news-item-title-en">Cyberleek threatens full GTA 6 build leak unless Take-Two apologizes and his $30 million crypto memecoin goal is met</span>
          <span class="news-value-point">💡 臭名昭著的GTA VI泄密者Cyberleek威胁要发布GTA VI的完整版本，如果Take-Two不发布物理版本，但前提是其memecoin达…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-11/10711148.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社长沙10月11日电 (记者 唐小晴)“袁稻思源”杂交水稻智能育种平台11日在长沙正式上线。这意味着湖南杂交水稻育种告别传统经验模式，迈入数据驱动、智能决策的全新发展阶段。" data-title="“袁稻思源”杂交水稻智能育种平台长沙发布 AI赋能育种创新" data-date="10-11 23:46" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-11 23:46</span>
          <span class="news-item-title">“袁稻思源”杂交水稻智能育种平台长沙发布 AI赋能育种创新</span>
          <span class="news-value-point">💡 中新社长沙10月11日电 (记者 唐小晴)“袁稻思源”杂交水稻智能育种平台11日在长沙正式上线</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/science/1009379/nasa-800gb-artemis-ii-data" target="_blank" rel="noopener" data-cat="zonghe" data-summary="如果你认为你已经看到了阿尔忒弥斯II任务的所有内容，那你就错了。本周， NASA在Artemis II: Sights &amp; Sounds of Science网站上发布了超过800GB的科学数据、图像和视频。档案包括超过11,000页" data-title="NASA dumped over 800GB of Artemis II data online" data-date="10-11 23:34" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-11 23:34</span>
          <span class="news-item-title">美国国家航空航天局在网上倾倒了超过800GB的Artemis II数据</span>
          <span class="news-item-title-en">NASA dumped over 800GB of Artemis II data online</span>
          <span class="news-value-point">💡 如果你认为你已经看到了阿尔忒弥斯II任务的所有内容，那你就错了</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/715.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 11 日消息，一加中国区总裁李杰今日在微博评论区回应关于一加 16 屏幕刷新率相关问题，据其介绍，一加 16 追求体验优先，不是参数优先。要同时兼顾流畅，功耗，发热，屏幕显示效果，现在的屏幕技术暂时做不到全局 185Hz。全局高刷要做到常用常开，目前最佳体验就是全局 165Hz，欢迎大家上手一加 16 去对比其他手机。IT之家注意到，在 10 月 9 日的第四代东方屏技术沟通会上，一加与京东方联合研发的第四代东方屏正式发布。第四代东方屏采用全新 X4 发光材料，宣称“色彩准、高刷稳、画面亮、功耗低、寿命长”；支持真硬件 1nit，夜间看屏幕，柔和不刺眼。第四代东方屏宣称做到行业首个全链路硬件全局超高刷，带来全球首个“日常 165Hz”。日常使用支持全局 165Hz 超高刷" data-title="李杰回应一加 16 不支持全局 185Hz：产品追求体验优先，屏幕暂时做不到" data-date="10-11 23:28" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-11 23:28</span>
          <span class="news-item-title">李杰回应一加 16 不支持全局 185Hz：产品追求体验优先，屏幕暂时做不到</span>
          <span class="news-value-point">💡 IT之家 10 月 11 日消息，一加中国区总裁李杰今日在微博评论区回应关于一加 16 屏幕刷新率相关问题，据其介绍，一加 16 追求体验优先，…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/11/crystal-palace-nottingham-forest-premier-league-match-report" target="_blank" rel="noopener" data-cat="zonghe" data-summary="可以说， Oliver Glasner度过了更愉快的下午。诺丁汉森林队主教练来到伦敦南部，穿着黑色飞行员夹克，打扮得像一个来自All Bar One的保镖，好像他正在预料麻烦，但却得到了一个" data-title="Pino finishes off Nottingham Forest on Glasner’s unhappy Crystal Palace return" data-date="10-11 23:28" data-source="卫报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-11 23:28</span>
          <span class="news-item-title">在格拉斯纳不幸的水晶宫回归中，皮诺完成了诺丁汉森林</span>
          <span class="news-item-title-en">Pino finishes off Nottingham Forest on Glasner’s unhappy Crystal Palace return</span>
          <span class="news-value-point">💡 可以说， Oliver Glasner度过了更愉快的下午</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/entertainment/1009346/george-a-romero-season-of-the-witch-feminist-horror-review" target="_blank" rel="noopener" data-cat="zonghe" data-summary="乔治· A ·罗梅罗（ George A. Romero ）显然是现代僵尸电影之父。但是，在《活死人之夜》和他的爆发恐怖片《疯子》之间，罗梅罗制作了两部鲜为人知的电影：《永远是香草》，" data-title="George A. Romero’s Season of the Witch is a slow-burn feminist occult drama" data-date="10-11 23:15" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-11 23:15</span>
          <span class="news-item-title">乔治· A ·罗梅罗（ George A. Romero ）的《女巫季节》（ Season of the Witch ）是一部缓慢燃</span>
          <span class="news-item-title-en">George A. Romero’s Season of the Witch is a slow-burn feminist occult drama</span>
          <span class="news-value-point">💡 乔治· A ·罗梅罗（ George A. Romero ）显然是现代僵尸电影之父</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/cyber-security/canadian-youtuber-builds-flock-like-camera-to-exclusively-track-police-vehicles-officers-visit-his-home-to-express-privacy-concerns" target="_blank" rel="noopener" data-cat="zonghe" data-summary="加拿大YouTuber安东尼·西斯蒂利（ Anthony Sistilli ）说，警方在他制造了一个旨在追踪警车的ALPR摄像头后对他进行了讯问，引发了一场关于大规模车牌监控隐私风险的讽刺讨论。" data-title="Canadian YouTuber builds &#39;Flock-like&#39; camera to exclusively track police vehicles" data-date="10-11 23:11" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-11 23:11</span>
          <span class="news-item-title">加拿大YouTube用户打造“Flock-like”摄像头，专门追踪警车</span>
          <span class="news-item-title-en">Canadian YouTuber builds 'Flock-like' camera to exclusively track police vehicles</span>
          <span class="news-value-point">💡 加拿大YouTuber安东尼·西斯蒂利（ Anthony Sistilli ）说，警方在他制造了一个旨在追踪警车的ALPR摄像头后对他进行了讯问…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-11/10711141.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社长春10月11日电 题：长春书写生态“立体答卷”：虎豹归林 笑语满河" data-title="长春书写生态“立体答卷”：虎豹归林　笑语满河" data-date="10-11 23:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-11 23:11</span>
          <span class="news-item-title">长春书写生态“立体答卷”：虎豹归林　笑语满河</span>
          <span class="news-value-point">💡 中新社长春10月11日电 题：长春书写生态“立体答卷”：虎豹归林 笑语满河</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-11/10711140.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社杭州10月11日电 题：从一座古城读懂千年吴越" data-title="（文化新纪行）从一座古城读懂千年吴越" data-date="10-11 23:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-11 23:10</span>
          <span class="news-item-title">（文化新纪行）从一座古城读懂千年吴越</span>
          <span class="news-value-point">💡 中新社杭州10月11日电 题：从一座古城读懂千年吴越</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/712.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 11 日消息，彭博社记者马克 · 古尔曼今天在新一期《Power On》通讯透露，苹果正在为其首款折叠屏手机 iPhone Duo 谋划声势浩大的展示活动，让每一位潜在顾客都能充分体验这款新品。古尔曼表示，苹果将在美国各地的 Apple Store 直营店摆出大量样机，供到来的顾客上手体验。预计纽约第五大道的旗舰店将布置超 150 台体验机，分布在上手区和展示设施中。苹果总部 Apple Park 游客中心预计将展出 100 台 iPhone Duo。同时，芝加哥密歇根大街、洛杉矶葛洛夫购物中心和曼哈顿上西城的 Apple Store 预计将提供 30-40 台样机，部分规模较小的门店也将配备约 20 台 iPhone Duo。考虑到这台手机仅有两个配色，这种数量显然是不" data-title="古尔曼：苹果计划在多个直营店举办 iPhone Duo 大型体验活动，最多摆出 150 台以上样机" data-date="10-11 23:01" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-11 23:01</span>
          <span class="news-item-title">古尔曼：苹果计划在多个直营店举办 iPhone Duo 大型体验活动，最多摆出 150 台以上样机</span>
          <span class="news-value-point">💡 IT之家 10 月 11 日消息，彭博社记者马克 · 古尔曼今天在新一期《Power On》通讯透露，苹果正在为其首款折叠屏手机 iPhone …</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/710.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 11 日消息，小岛秀夫近日在 KOJI10 广播节目透露，他已确定客串某部真人电影和某动画。这位游戏制作人曾出演日剧《别班》，还参与过《疯狂动物城 2》日语配音。▲ 小岛秀夫图源：小岛工作室小岛秀夫在节目中表示：“有导演和其他人邀请我出演。其中一部是大型真人电影，另一部则是一部知名动画作品。”据IT之家了解，小岛秀夫正在忙于两个 3A 游戏项目：恐怖游戏《OD》、谍报游戏《PHYSINT》。但根据他本人所述，他自己已幕后为其他项目录制过台词，并客串了一款尚未公布名称的游戏。小岛秀夫认为，演戏只是自己的副业，他不喜欢在荧幕中扮演自己，而是更喜欢尝试其他角色或不同的人物形象。迄今为止，小岛秀夫并没有主动参加电影演员试镜，相反许多知名创作者会直接邀请他出演。迪士尼日本曾表示，《" data-title="小岛秀夫确认客串某大型真人电影、某知名动画，坦言不喜欢扮演自己" data-date="10-11 22:50" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-11 22:50</span>
          <span class="news-item-title">小岛秀夫确认客串某大型真人电影、某知名动画，坦言不喜欢扮演自己</span>
          <span class="news-value-point">💡 IT之家 10 月 11 日消息，小岛秀夫近日在 KOJI10 广播节目透露，他已确定客串某部真人电影和某动画</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/709.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 11 日消息，彭博社记者马克 · 古尔曼今日在新一期《Power On》通讯中透露，苹果首款智能家庭中枢名为“HomeView”，预计将在 10 月 13 日的“欢迎回家”活动正式发布，11 月出货。据介绍，这款产品的外观设计类似 iMac G4“台灯电脑”，采用悬浮式屏幕，下方配有扬声器底座。该设备将搭载 A18 芯片，官方还将推出壁挂安装版本。IT之家从原报道获悉，这款新产品将提供深空灰、银色、星光色和粉色四种配色，壁挂版仅有深空灰、银色两种配色。古尔曼表示，这款产品主要使用语音交互，以 AI Siri 为核心。用户可以在房间另一端查看设备显示内容，并且该产品将运行苹果自家 App，但不支持 App Store。用户或许可以使用 iPhone，将第三方应用的小组件投射" data-title="古尔曼：苹果首款智能家庭中枢定名 HomeView，搭载 A18 芯片、四种配色可选" data-date="10-11 22:36" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-11 22:36</span>
          <span class="news-item-title">古尔曼：苹果首款智能家庭中枢定名 HomeView，搭载 A18 芯片、四种配色可选</span>
          <span class="news-value-point">💡 IT之家 10 月 11 日消息，彭博社记者马克 · 古尔曼今日在新一期《Power On》通讯中透露，苹果首款智能家庭中枢名为“HomeVie…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/russian-disinformation-bot-traffic-nearly-eliminated-overnight-after-ukraine-drone-strikes-cripple-multiple-of-russias-google-data-centers-ukraine-intensifies-bombing-of-yandex-data-centers-in-response-to-moscows-strikes-on-kyiv-data-centers" target="_blank" rel="noopener" data-cat="zonghe" data-summary="随着乌克兰关闭几个Yandex数据中心，俄罗斯机器人流量急剧下降。" data-title="Russia&#39;s Yandex bot traffic nearly eliminated overnight after Ukraine drone strikes cripple multiple of &#39;Russia&#39;s Google&#39; data centers" data-date="10-11 21:15" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-11 21:15</span>
          <span class="news-item-title">在乌克兰无人机袭击多个“俄罗斯谷歌”数据中心后，俄罗斯的Yandex机器人流量几乎在一夜之间消失</span>
          <span class="news-item-title-en">Russia's Yandex bot traffic nearly eliminated overnight after Ukraine drone strikes cripple multiple of 'Russia's Google' data centers</span>
          <span class="news-value-point">💡 随着乌克兰关闭几个Yandex数据中心，俄罗斯机器人流量急剧下降</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/ssds/sandisk-nas-800-1-92tb-ssd-review" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Sandisk NAS 800是专为NAS工作负载构建的高端PCIe 5.0 NVMe SSD ，具有高耐用性、强大的持续写入性能和低4KB随机延迟。它主要受制于其高昂的价格。" data-title="Sandisk NAS 800 1.92TB SSD Review: Endurance at a premium" data-date="10-11 21:05" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-11 21:05</span>
          <span class="news-item-title">Sandisk NAS 800 1.92 TB固态硬盘评测：耐用性溢价</span>
          <span class="news-item-title-en">Sandisk NAS 800 1.92TB SSD Review: Endurance at a premium</span>
          <span class="news-value-point">💡 Sandisk NAS 800是专为NAS工作负载构建的高端PCIe 5.0 NVMe SSD ，具有高耐用性、强大的持续写入性能和低4KB随机…</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-12 01:43（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
