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
      <span>2026-11-09 16:47 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×17 · 纽约时报×8</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/11-09/10728874.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月9日电 (记者 黄钰钦)中国外交部发言人郭嘉昆9日主持例行记者会。" data-title="中方谈奥地利总理访华：为中欧坚持伙伴定位、深挖合作潜力提供积极示范" data-date="11-09 15:54" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 11-09 15:54</span>
      </div>
      <h2 class="hero-featured-title">中方谈奥地利总理访华：为中欧坚持伙伴定位、深挖合作潜力提供积极示范</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.bbc.com/zhongwen/articles/c6rmym2gg9z1o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="辉达（英伟达）总裁黄仁勋承认婚外情并向公众致歉，为何引发国安及舆论风暴？新加坡的角色又是如何？会影响台湾的产业链吗？中国为何严厉否认相关指控。" data-title="黄仁勋婚外情掀起国安风暴：拆解五大看点" data-date="11-09 16:39" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">黄仁勋婚外情掀起国安风暴：拆解五大看点</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/2026/nov/09/premier-league-10-talking-points-weekend-action" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="德拉普的才华重新浮现，戈麦斯用更多的烟花和埃弗顿的拔毛混乱来取悦布莱顿奥利弗·格拉斯纳很容易对利亚姆·德拉普失去耐心。前锋还只有23岁，但他" data-title="Premier League: 10 talking points from the weekend’s action" data-date="11-09 16:00" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Premier League: 10 talking points from the weekend’s action</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/024/363.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="小米 17 Pro 手机 2025 年 9 月 25 日发布，16+512G 定价 5599 元。京东 11.11 大促期间，活动价 5199 元；PLUS 会员下单立减 25.99 元；领取 9 折优惠券：点此领取；国家补贴立减 500 元；商品详情页右上角直播间可领 200 元优惠券：到手价为 4173.01 元：京东小米 17 Pro 手机 16GB+512GB 4173.01 元直达链接下单赠送复古掌机保护壳。京东 11.11 红包至高 26888 元无门槛可用，每天可抽一次：点此抽取。京东小米 17 Pro 手机 16GB+512GB 4173.01 元直达链接京东 11.11 无门槛红包 面额至高 26888 元，每天抽 3 次：点此抽红包。淘宝 11.11 无门槛红包 面额至高" data-title="赠复古掌机保护壳：小米 17 Pro 手机 16+512G 版国补后 5599 → 4173 元" data-date="11-09 16:45" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">赠复古掌机保护壳：小米 17 Pro 手机 16+512G 版国补后 5599 → 4173 元</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-09/10728874.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月9日电 (记者 黄钰钦)中国外交部发言人郭嘉昆9日主持例行记者会。" data-title="中方谈奥地利总理访华：为中欧坚持伙伴定位、深挖合作潜力提供积极示范" data-date="11-09 15:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 15:54</span>
          <span class="news-item-title">中方谈奥地利总理访华：为中欧坚持伙伴定位、深挖合作潜力提供积极示范</span>
          <span class="news-value-point">💡 中新网北京11月9日电 (记者 黄钰钦)中国外交部发言人郭嘉昆9日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-09/10728868.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="11月3日，是日本现行宪法公布80周年纪念日，当天国会议事堂前出现万人规模的集会，呼吁守护和平宪法。高市政府上台以来，不断搅动修宪风浪，图谋突破作为二战后日本重返国际社会前提的“和平宪法”。东京上智大学政治学教授中野晃一注意到，越来越多的日本人感到有必要守住“和平宪法”第九条，因为这是抵御战争的最后一道防线。" data-title="世界周刊丨高市政府高调掀起修宪风浪 80年“和平之盾”还能守住吗" data-date="11-09 15:46" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 15:46</span>
          <span class="news-item-title">世界周刊丨高市政府高调掀起修宪风浪 80年“和平之盾”还能守住吗</span>
          <span class="news-value-point">💡 11月3日，是日本现行宪法公布80周年纪念日，当天国会议事堂前出现万人规模的集会，呼吁守护和平宪法</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-09/10728866.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月9日电 (记者 黄钰钦 李京泽)中国外交部发言人9日宣布：应中共中央政治局委员、外交部长王毅邀请，斯洛伐克外交部长布拉纳尔将于11月10日至11日访华。" data-title="斯洛伐克外交部长将访华 中方：延续双边关系高水平发展势头" data-date="11-09 15:46" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 15:46</span>
          <span class="news-item-title">斯洛伐克外交部长将访华 中方：延续双边关系高水平发展势头</span>
          <span class="news-value-point">💡 中新网北京11月9日电 (记者 黄钰钦 李京泽)中国外交部发言人9日宣布：应中共中央政治局委员、外交部长王毅邀请，斯洛伐克外交部长布拉纳尔将于1…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-09/10728867.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月9日电 (记者 黄钰钦)中国外交部发言人郭嘉昆9日主持例行记者会。" data-title="中方：美伊战事延宕不符合当事方和国际社会共同利益" data-date="11-09 15:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 15:44</span>
          <span class="news-item-title">中方：美伊战事延宕不符合当事方和国际社会共同利益</span>
          <span class="news-value-point">💡 中新网北京11月9日电 (记者 黄钰钦)中国外交部发言人郭嘉昆9日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-09/10728846.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月9日电 (记者 黄钰钦)中国外交部发言人郭嘉昆9日主持例行记者会。" data-title="中国空间站将首次迎来外籍航天员到访 外交部回应" data-date="11-09 15:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 15:36</span>
          <span class="news-item-title">中国空间站将首次迎来外籍航天员到访 外交部回应</span>
          <span class="news-value-point">💡 中新网北京11月9日电 (记者 黄钰钦)中国外交部发言人郭嘉昆9日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-09/10728826.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月9日电 当地时间11月8日，印度迎来重要传统节日排灯节。然而，节日到来前，德里的空气质量已持续恶化，长期困扰当地居民的空气污染问题再次凸显。" data-title="迎来排灯节，印度德里空气污染却冲上全球第一！民众不满情绪升温" data-date="11-09 15:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 15:03</span>
          <span class="news-item-title">迎来排灯节，印度德里空气污染却冲上全球第一！民众不满情绪升温</span>
          <span class="news-value-point">💡 中新网11月9日电 当地时间11月8日，印度迎来重要传统节日排灯节</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-09/10728820.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月9日电 综合美媒9日报道，美国国会众议院民主党领袖杰弗里斯表示，他“坚决支持”弹劾国防部长赫格塞思。" data-title="美国众院民主党领袖：防长赫格塞思“必须走人”" data-date="11-09 14:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 14:54</span>
          <span class="news-item-title">美国众院民主党领袖：防长赫格塞思“必须走人”</span>
          <span class="news-value-point">💡 中新网11月9日电 综合美媒9日报道，美国国会众议院民主党领袖杰弗里斯表示，他“坚决支持”弹劾国防部长赫格塞思</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-09/10728800.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月9日电 新德里消息：印度中央邦当地时间9日发生两起火灾，造成12人死亡，另有多人受伤。" data-title="印度中央邦排灯节期间发生两起火灾 致12人死亡" data-date="11-09 14:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 14:34</span>
          <span class="news-item-title">印度中央邦排灯节期间发生两起火灾 致12人死亡</span>
          <span class="news-value-point">💡 中新网北京11月9日电 新德里消息：印度中央邦当地时间9日发生两起火灾，造成12人死亡，另有多人受伤</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/08/us/politics/trump-immigration-crackdown-republicans-midterms.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="总统在周日播出的“60分钟”采访中被问及他的驱逐政策是否走得太远。“我认为这可能太难了，”他说。" data-title="Trump Says Immigration Crackdown May Have ‘Hurt’ Republicans in Midterms" data-date="11-09 11:16" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-09 11:16</span>
          <span class="news-item-title">特朗普表示，在中期选举中，移民镇压可能会“伤害”共和党人</span>
          <span class="news-item-title-en">Trump Says Immigration Crackdown May Have ‘Hurt’ Republicans in Midterms</span>
          <span class="news-value-point">💡 总统在周日播出的“60分钟”采访中被问及他的驱逐政策是否走得太远</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/08/us/politics/trump-joke-dana-white-press-secretary.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="总统周日表示，这位UFC首席执行官“喜欢”成为白宫发言人的想法，但他公开提供这份工作“只是有点好玩”。" data-title="Trump Was ‘Only Kidding’ in Asking Dana White to Be His Press Secretary" data-date="11-09 08:43" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-09 08:43</span>
          <span class="news-item-title">特朗普要求Dana White担任他的新闻秘书只是“开玩笑”</span>
          <span class="news-item-title-en">Trump Was ‘Only Kidding’ in Asking Dana White to Be His Press Secretary</span>
          <span class="news-value-point">💡 总统周日表示，这位UFC首席执行官“喜欢”成为白宫发言人的想法，但他公开提供这份工作“只是有点好玩”</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/08/us/politics/trump-iran-options.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在特朗普总统试图找到摆脱极不受欢迎的冲突的方法时，他面临着没有好的选择。但也有选择的余地。" data-title="Here Are the Difficult Options Trump Is Weighing to Resolve the War in Iran" data-date="11-09 07:49" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-09 07:49</span>
          <span class="news-item-title">以下是特朗普为解决伊朗战争而权衡的艰难选择</span>
          <span class="news-item-title-en">Here Are the Difficult Options Trump Is Weighing to Resolve the War in Iran</span>
          <span class="news-value-point">💡 在特朗普总统试图找到摆脱极不受欢迎的冲突的方法时，他面临着没有好的选择</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/08/us/politics/pete-hegseth-impeachment-hakeem-jeffries.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="民主党已开始为针对特朗普政府的积极监督议程奠定基础。但政治清算可能会在新一届国会开始之前进行。" data-title="Jeffries Backs Impeaching Hegseth as Democrats Push for Accountability" data-date="11-09 03:22" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-09 03:22</span>
          <span class="news-item-title">Jeffries支持弹劾Hegseth ，因为民主党人正在推动问责制</span>
          <span class="news-item-title-en">Jeffries Backs Impeaching Hegseth as Democrats Push for Accountability</span>
          <span class="news-value-point">💡 民主党已开始为针对特朗普政府的积极监督议程奠定基础</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/08/world/middleeast/israel-eisenkot-netanyahu-what-to-know.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="Eisenkot先生是一名职业将领，也是以色列总理本雅明·内塔尼亚胡（ Benjamin Netanyahu ）的主要竞争对手，现在将有长达六周的时间组建联盟。" data-title="Who Is Gadi Eisenkot, Israel’s Opposition Leader?" data-date="11-09 01:46" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-09 01:46</span>
          <span class="news-item-title">以色列反对党领袖加迪·艾森科特（ Gadi Eisenkot ）是谁？</span>
          <span class="news-item-title-en">Who Is Gadi Eisenkot, Israel’s Opposition Leader?</span>
          <span class="news-value-point">💡 Eisenkot先生是一名职业将领，也是以色列总理本雅明·内塔尼亚胡（ Benjamin Netanyahu ）的主要竞争对手，现在将有长达六周…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/08/us/politics/trump-midterm-election-america-future.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="随着美国人吸收了一个惊人的新政治现实，他们面临着他们实际决定与总统完成的时间和他实际完成的时间之间的差距。" data-title="For Trump and America, a Clear Election Verdict but a Murky Future" data-date="11-09 00:25" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-09 00:25</span>
          <span class="news-item-title">对于特朗普和美国来说，一个明确的选举裁决，但一个模糊的未来</span>
          <span class="news-item-title-en">For Trump and America, a Clear Election Verdict but a Murky Future</span>
          <span class="news-value-point">💡 随着美国人吸收了一个惊人的新政治现实，他们面临着他们实际决定与总统完成的时间和他实际完成的时间之间的差距</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/08/ipswich-bournemouth-premier-league-match-report" target="_blank" rel="noopener" data-cat="shizheng" data-summary="埃文尼尔森的另一个进球帮助马可·罗斯（ Marco Rose ）的伯恩茅斯（ Bournemouth ）连续第八场胜利，在伊普斯维奇（ Ipswich ）以2-1艰难获胜。埃文尼尔森在本赛季的前六场比赛中未能得分，但连续第五次获得总理利亚（ Premier Lea ）的净胜利" data-title="Evanilson launches eighth straight Bournemouth win at blundering Ipswich" data-date="11-09 00:14" data-source="卫报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-09 00:14</span>
          <span class="news-item-title">伊万尼尔森在浮躁的伊普斯维奇连续第八次赢得伯恩茅斯</span>
          <span class="news-item-title-en">Evanilson launches eighth straight Bournemouth win at blundering Ipswich</span>
          <span class="news-value-point">💡 埃文尼尔森的另一个进球帮助马可·罗斯（ Marco Rose ）的伯恩茅斯（ Bournemouth ）连续第八场胜利，在伊普斯维奇（ Ipsw…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c6rmym2gg9z1o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="辉达（英伟达）总裁黄仁勋承认婚外情并向公众致歉，为何引发国安及舆论风暴？新加坡的角色又是如何？会影响台湾的产业链吗？中国为何严厉否认相关指控。" data-title="黄仁勋婚外情掀起国安风暴：拆解五大看点" data-date="11-09 16:39" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-09 16:39</span>
          <span class="news-item-title">黄仁勋婚外情掀起国安风暴：拆解五大看点</span>
          <span class="news-value-point">💡 辉达（英伟达）总裁黄仁勋承认婚外情并向公众致歉，为何引发国安及舆论风暴</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/024/358.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 9 日消息，极狐汽车宣布旗下极狐贝塔 S3 535ULTRA+ 激光换电版将于 11 月 13 日上市。外观方面，该车采用“ARC-FLOW 极智源流”设计，车头使用锋行冰璨贯穿式大灯，车身匹配水滴韵动无边框后视镜，车尾采用数字几何尾灯。座舱方面，新车将配备 15.6 英寸悬浮式中控屏与 8.8 英寸液晶仪表，搭载高通骁龙 8,155 芯片，座舱支持四音区语音识别。新车搭载元境智能驾驶辅助系统，配备 1 颗 192 线激光雷达与地平线征程 J6M 芯片，支持高速 NOA 领航、城区 NOA、自动泊车。动力方面，极狐贝塔 S3 全系采用前置前驱布局，搭载永磁同步电机，最大功率 159kW，峰值扭矩 250N·m，0-100km/h 加速 7.1 秒，最高车速 165km/h" data-title="极狐贝塔 S3 535ULTRA+ 激光换电版将于 11 月 13 日上市，支持 99 秒极速换电" data-date="11-09 16:37" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-09 16:37</span>
          <span class="news-item-title">极狐贝塔 S3 535ULTRA+ 激光换电版将于 11 月 13 日上市，支持 99 秒极速换电</span>
          <span class="news-value-point">💡 IT之家 11 月 9 日消息，极狐汽车宣布旗下极狐贝塔 S3 535ULTRA+ 激光换电版将于 11 月 13 日上市</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/508694.html" target="_blank" rel="noopener" data-cat="keji" data-summary="11月9日，千问办公发布2.0版本" data-title="千问办公2.0发布，首个支持多人与Agent协作的Team Agent来了" data-date="11-09 16:34" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-09 16:34</span>
          <span class="news-item-title">千问办公2.0发布，首个支持多人与Agent协作的Team Agent来了</span>
          <span class="news-value-point">💡 11月9日，千问办公发布2.0版本</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-09/10728890.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="“太空云”是指在轨协同的天基云服务系统，它改变传统卫星“单星观测、数据回传地面处理”模式，让天基资源可以按需调用、即连即用。在今天(9日)举办的2026太空云产业生态大会上，“星云星座计划”等我国太空云产业化成果发布，标志着我国“太空云”生态建设迈出了从技术验证走向产业化布局的关键一步。" data-title="“星云星座计划”发布 我国太空算力网加快部署" data-date="11-09 16:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 16:28</span>
          <span class="news-item-title">“星云星座计划”发布 我国太空算力网加快部署</span>
          <span class="news-value-point">💡 “太空云”是指在轨协同的天基云服务系统，它改变传统卫星“单星观测、数据回传地面处理”模式，让天基资源可以按需调用、即连即用</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/024/354.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 9 日消息，据央视新闻报道，在今天（9 日）举办的 2026 太空云产业生态大会上，“星云星座计划”等我国太空云产业化成果发布，标志着我国“太空云”生态建设迈出了从技术验证走向产业化布局的关键一步。IT之家从报道中获悉，“太空云”是指在轨协同的天基云服务系统，它改变传统卫星“单星观测、数据回传地面处理”模式，让天基资源可以按需调用、即连即用。本次发布的“星云星座计划”是中国科学院空天信息创新研究院与国内科创企业联合研发的全栈国产化太空算力网，是太空云生态产业化落地的重点项目。该计划覆盖从国产算力芯片到卫星应用的全产业链条。未来，项目将依托国内计算芯片、服务器整机、卫星制造、卫星应用等研发单位，构建从“核心器部件研制”到“星座组网与应用”的全栈国产化自主技术体系。分布形成“" data-title="“星云星座计划”发布，覆盖从国产算力芯片到卫星应用的全产业链条" data-date="11-09 16:25" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-09 16:25</span>
          <span class="news-item-title">“星云星座计划”发布，覆盖从国产算力芯片到卫星应用的全产业链条</span>
          <span class="news-value-point">💡 IT之家 11 月 9 日消息，据央视新闻报道，在今天（9 日）举办的 2026 太空云产业生态大会上，“星云星座计划”等我国太空云产业化成果发…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-09/10728877.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网北京11月9日电 (记者 黄钰钦)中国外交部发言人郭嘉昆9日主持例行记者会。" data-title="中方：欢迎并期待更多国家加入世界人工智能合作组织" data-date="11-09 16:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 16:07</span>
          <span class="news-item-title">中方：欢迎并期待更多国家加入世界人工智能合作组织</span>
          <span class="news-value-point">💡 中新网北京11月9日电 (记者 黄钰钦)中国外交部发言人郭嘉昆9日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-09/10728872.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网北京11月9日电 (记者 黄钰钦)中国外交部发言人郭嘉昆9日主持例行记者会。" data-title="外交部：中方在美国输华芯片问题上的立场是一贯的" data-date="11-09 15:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 15:49</span>
          <span class="news-item-title">外交部：中方在美国输华芯片问题上的立场是一贯的</span>
          <span class="news-value-point">💡 中新网北京11月9日电 (记者 黄钰钦)中国外交部发言人郭嘉昆9日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/508607.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Worker不够了主管Agent还能自己招！" data-title="AI接管一家8万Star开源公司，写代码、派任务、查Bug全包了" data-date="11-09 13:47" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-09 13:47</span>
          <span class="news-item-title">AI接管一家8万Star开源公司，写代码、派任务、查Bug全包了</span>
          <span class="news-value-point">💡 Worker不够了主管Agent还能自己招</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/08/is-jensen-huangs-job-on-the-line-yales-jeffrey-sonnenfeld-estimates-its-about-a-50-50/" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达董事会正在调查Jensen Huang与中国间谍嫌疑人的关系，耶鲁大学的Jeffrey Sonnenfeld认为，无论Huang是否继续担任首席执行官，这大概是一个硬币翻转。" data-title="Is Jensen Huang’s job on the line? Yale’s Jeffrey Sonnenfeld estimates it’s “about a 50" data-date="11-09 13:26" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-09 13:26</span>
          <span class="news-item-title">Jensen Huang的工作在线吗？耶鲁大学的杰弗里·索南菲尔德（ Jeffrey Sonnenfeld ）估计， “大约50</span>
          <span class="news-item-title-en">Is Jensen Huang’s job on the line? Yale’s Jeffrey Sonnenfeld estimates it’s “about a 50</span>
          <span class="news-value-point">💡 英伟达董事会正在调查Jensen Huang与中国间谍嫌疑人的关系，耶鲁大学的Jeffrey Sonnenfeld认为，无论Huang是否继续担…</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/508603.html" target="_blank" rel="noopener" data-cat="keji" data-summary="11月5日，基元律动（TokenRhythm）发布Agent原生模型NeoHorse-1.5-Flash Preview。" data-title="基元律动发布NeoHorse-1.5-Flash Preview，Agent模型RSI进入第二轮迭代" data-date="11-09 13:09" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-09 13:09</span>
          <span class="news-item-title">基元律动发布NeoHorse-1.5-Flash Preview，Agent模型RSI进入第二轮迭代</span>
          <span class="news-value-point">💡 11月5日，基元律动（TokenRhythm）发布Agent原生模型NeoHorse-1.5-Flash Preview</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/508586.html" target="_blank" rel="noopener" data-cat="keji" data-summary="“让人放心，把人放大。”" data-title="当AI在加速狂奔，什么反而应该“慢”下来？" data-date="11-09 11:47" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-09 11:47</span>
          <span class="news-item-title">当AI在加速狂奔，什么反而应该“慢”下来？</span>
          <span class="news-value-point">💡 “让人放心，把人放大</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/508566.html" target="_blank" rel="noopener" data-cat="keji" data-summary="11月6日，清华大学举行“新技术激发文化新活力，用AI讲好中国故事”鲸锐AI创作大赛大咖对谈活动" data-title="寻找最会讲故事的AI创作者，虎鲸文娱鲸锐AI创作大赛走进清华大学" data-date="11-09 10:19" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-09 10:19</span>
          <span class="news-item-title">寻找最会讲故事的AI创作者，虎鲸文娱鲸锐AI创作大赛走进清华大学</span>
          <span class="news-value-point">💡 11月6日，清华大学举行“新技术激发文化新活力，用AI讲好中国故事”鲸锐AI创作大赛大咖对谈活动</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/508498.html" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达暗盘跌2%" data-title="黄仁勋承认出轨发全员信道歉！英伟达启动紧急调查" data-date="11-09 08:40" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-09 08:40</span>
          <span class="news-item-title">黄仁勋承认出轨发全员信道歉！英伟达启动紧急调查</span>
          <span class="news-value-point">💡 英伟达暗盘跌2%</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/08/technology/nvidia-investigation-jensen-huang-china.html" target="_blank" rel="noopener" data-cat="keji" data-summary="该公司首席执行官黄忠周日承认，他与一位美国官员认定为中国情报部门工作的企业高管关系密切。" data-title="Nvidia Opens Investigation Into Jensen Huang’s Relationship With Chinese Spy" data-date="11-09 08:33" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-09 08:33</span>
          <span class="news-item-title">英伟达对黄延森与中国间谍的关系展开调查</span>
          <span class="news-item-title-en">Nvidia Opens Investigation Into Jensen Huang’s Relationship With Chinese Spy</span>
          <span class="news-value-point">💡 该公司首席执行官黄忠周日承认，他与一位美国官员认定为中国情报部门工作的企业高管关系密切</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/08/us/politics/rubio-nvidia-ceo-chinese-spy.html" target="_blank" rel="noopener" data-cat="keji" data-summary="这位国务卿在起草一份秘密备忘录方面的作用凸显了高级官员对今年春天黄延森与一名与中国情报有关的女性的关系的担忧。" data-title="Rubio Warned Officials About Nvidia Chief’s Entanglement With Chinese Spy" data-date="11-09 08:27" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-09 08:27</span>
          <span class="news-item-title">卢比奥警告官员英伟达首席执行官与中国间谍纠缠不清</span>
          <span class="news-item-title-en">Rubio Warned Officials About Nvidia Chief’s Entanglement With Chinese Spy</span>
          <span class="news-value-point">💡 这位国务卿在起草一份秘密备忘录方面的作用凸显了高级官员对今年春天黄延森与一名与中国情报有关的女性的关系的担忧</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/09/premier-league-10-talking-points-weekend-action" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="德拉普的才华重新浮现，戈麦斯用更多的烟花和埃弗顿的拔毛混乱来取悦布莱顿奥利弗·格拉斯纳很容易对利亚姆·德拉普失去耐心。前锋还只有23岁，但他" data-title="Premier League: 10 talking points from the weekend’s action" data-date="11-09 16:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-09 16:00</span>
          <span class="news-item-title">英超联赛：周末行动的10个谈话要点</span>
          <span class="news-item-title-en">Premier League: 10 talking points from the weekend’s action</span>
          <span class="news-value-point">💡 德拉普的才华重新浮现，戈麦斯用更多的烟花和埃弗顿的拔毛混乱来取悦布莱顿奥利弗·格拉斯纳很容易对利亚姆·德拉普失去耐心</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025492/man-utd-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Is Villa comeback enough to save Man Utd boss?" data-title="Is Villa comeback enough to save Man Utd boss?" data-date="11-09 15:39" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-09 15:39</span>
          <span class="news-item-title">别墅复出是否足以拯救曼联老板？</span>
          <span class="news-item-title-en">Is Villa comeback enough to save Man Utd boss?</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cked3qjw1q4xo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="这是老特拉福德的英超经典，但曼联与阿斯顿维拉的4-4平局对迈克尔卡里克的未来做了什么？" data-title="Bizarre &amp; thrilling theatre as Carrick in limbo with Man Utd in drop zone" data-date="11-09 05:50" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-09 05:50</span>
          <span class="news-item-title">奇异而惊心动魄的剧院之旅：卡里克（ Carrick ）与曼联（ Man Utd ）在坠落区</span>
          <span class="news-item-title-en">Bizarre & thrilling theatre as Carrick in limbo with Man Utd in drop zone</span>
          <span class="news-value-point">💡 这是老特拉福德的英超经典，但曼联与阿斯顿维拉的4-4平局对迈克尔卡里克的未来做了什么</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cw98z7vdg546o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在本赛季英超联赛的每一轮比赛之后，特洛伊·迪尼（ Troy Deeney ）都给了我们本周最佳球队。你同意他的选择吗？" data-title="Who has made Troy&#39;s Premier League team of the week?" data-date="11-09 04:18" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-09 04:18</span>
          <span class="news-item-title">谁入选了特洛伊本周的英超联赛球队？</span>
          <span class="news-item-title-en">Who has made Troy's Premier League team of the week?</span>
          <span class="news-value-point">💡 在本赛季英超联赛的每一轮比赛之后，特洛伊·迪尼（ Troy Deeney ）都给了我们本周最佳球队</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cy47wj05xgqo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联4-4阿斯顿维拉在英超最伟大的比赛中排名如何？" data-title="Where does Man Utd 4-4 Villa rank among best Premier League games?" data-date="11-09 04:05" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-09 04:05</span>
          <span class="news-item-title">曼联4-4别墅在英超最佳比赛中排名如何？</span>
          <span class="news-item-title-en">Where does Man Utd 4-4 Villa rank among best Premier League games?</span>
          <span class="news-value-point">💡 曼联4-4阿斯顿维拉在英超最伟大的比赛中排名如何</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13609927/michael-carrick-manchester-united-boss-expects-to-stay-on-despite-club-sitting-in-relegation-zone-after-aston-villa-draw" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="压力不足的曼联老板迈克尔·卡里克（ Michael Carrick ） “希望”在周日对阵阿斯顿维拉（ Aston Villa ）的戏剧性4-4主场平局后继续留在降级区。" data-title="Man Utd in relegation zone but Carrick &#39;expects&#39; to stay on" data-date="11-09 03:40" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-09 03:40</span>
          <span class="news-item-title">曼联在降级区，但卡里克“希望”留在</span>
          <span class="news-item-title-en">Man Utd in relegation zone but Carrick 'expects' to stay on</span>
          <span class="news-value-point">💡 压力不足的曼联老板迈克尔·卡里克（ Michael Carrick ） “希望”在周日对阵阿斯顿维拉（ Aston Villa ）的戏剧性4-4…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cjx23rwxdn64o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在英超联赛中排名第二之后，布莱顿真的能成为阿森纳的主要挑战者吗？" data-title="Are &#39;outstanding&#39; Brighton now Arsenal&#39;s main title challengers?" data-date="11-09 03:24" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-09 03:24</span>
          <span class="news-item-title">“杰出”的布莱顿现在是阿森纳的主要挑战者吗？</span>
          <span class="news-item-title-en">Are 'outstanding' Brighton now Arsenal's main title challengers?</span>
          <span class="news-value-point">💡 在英超联赛中排名第二之后，布莱顿真的能成为阿森纳的主要挑战者吗</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/nov/08/man-utd-v-aston-villa-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联从两个进球中落后–两次–在老特拉福德的阿斯顿维拉挽救了4-4的平局桑德兰队以1-0击败切尔西队，这对他们来说是一个很好的结果。这对曼联来说又是一个尴尬。他们现在几乎没有" data-title="Manchester United 4-4 Aston Villa: Premier League – as it happened" data-date="11-09 03:14" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-09 03:14</span>
          <span class="news-item-title">曼联4-4阿斯顿维拉：英超联赛</span>
          <span class="news-item-title-en">Manchester United 4-4 Aston Villa: Premier League – as it happened</span>
          <span class="news-value-point">💡 曼联从两个进球中落后–两次–在老特拉福德的阿斯顿维拉挽救了4-4的平局桑德兰队以1-0击败切尔西队，这对他们来说是一个很好的结果</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ck5yn1zzyr2jo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利兹联队谴责在周六1-0战胜托特纳姆热刺后，针对后卫杰登·博格尔的“恶心”在线种族主义虐待。" data-title="Leeds condemn racist abuse of Bogle after Tel incident" data-date="11-09 03:12" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-09 03:12</span>
          <span class="news-item-title">利兹谴责在电话事件后对博格尔的种族主义虐待</span>
          <span class="news-item-title-en">Leeds condemn racist abuse of Bogle after Tel incident</span>
          <span class="news-value-point">💡 利兹联队谴责在周六1-0战胜托特纳姆热刺后，针对后卫杰登·博格尔的“恶心”在线种族主义虐待</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/10/premier-league-top-scorers-2026-27-race-for-golden-boot" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="找出哪位英国顶尖射手正在向进球排行榜射击。继续阅读……" data-title="Premier League top scorers 2026-27: who is leading race for the golden boot?" data-date="11-09 03:08" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-09 03:08</span>
          <span class="news-item-title">2026-27赛季英超联赛最佳射手：谁是金靴赛的领跑者？</span>
          <span class="news-item-title-en">Premier League top scorers 2026-27: who is leading race for the golden boot?</span>
          <span class="news-value-point">💡 找出哪位英国顶尖射手正在向进球排行榜射击</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/08/manchester-united-aston-villa-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="这么晚，这么晚的复出平局让迈克尔·卡里克继续他的工作吗？他敦促曼联通过建立势头来支持他们在周二气喘吁吁的罗马复出胜利，他们通过避免失败的方式做到了这一点。帕特里克·多古（ Patrick Dorgu ）的第96分钟均衡器" data-title="Dorgu rescues point for Manchester United in eight-goal thriller against Aston Villa" data-date="11-09 02:54" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-09 02:54</span>
          <span class="news-item-title">在对阵阿斯顿维拉的八球惊悚片中，多尔古为曼联抢救了一分</span>
          <span class="news-item-title-en">Dorgu rescues point for Manchester United in eight-goal thriller against Aston Villa</span>
          <span class="news-value-point">💡 这么晚，这么晚的复出平局让迈克尔·卡里克继续他的工作吗</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13609907/manchester-united-4-4-aston-villa-premier-league-highlights" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="免费观看：曼联和阿斯顿维拉之间英超比赛的亮点。" data-title="Man Utd rescue draw in EIGHT-goal thriller against Villa" data-date="11-09 02:49" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-09 02:49</span>
          <span class="news-item-title">曼联对别墅的EIGHT目标惊悚片救援抽签</span>
          <span class="news-item-title-en">Man Utd rescue draw in EIGHT-goal thriller against Villa</span>
          <span class="news-value-point">💡 免费观看：曼联和阿斯顿维拉之间英超比赛的亮点</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cwj34k7k54veo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联在4-4战平阿斯顿维拉的比赛中两次进球失利，但谁表现出色，谁在球员评分中没有表现出色？" data-title="Dorgu makes dramatic impact - Man Utd v Aston Villa ratings" data-date="11-09 02:46" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-09 02:46</span>
          <span class="news-item-title">多尔古产生了戏剧性的影响-曼联对阿斯顿维拉的评分</span>
          <span class="news-item-title-en">Dorgu makes dramatic impact - Man Utd v Aston Villa ratings</span>
          <span class="news-value-point">💡 曼联在4-4战平阿斯顿维拉的比赛中两次进球失利，但谁表现出色，谁在球员评分中没有表现出色</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/manchester-united-vs-aston-villa/report/559541" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联在停赛时间得分两次，挽救了老特拉福德阿斯顿维拉令人难以置信的4-4平局，这仍然使他们处于降级区。" data-title="Man Utd score two in stoppage-time to salvage 4-4 draw with Villa" data-date="11-09 02:30" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-09 02:30</span>
          <span class="news-item-title">曼联在停赛时间得分2分，用别墅打捞4-4平局</span>
          <span class="news-item-title-en">Man Utd score two in stoppage-time to salvage 4-4 draw with Villa</span>
          <span class="news-value-point">💡 曼联在停赛时间得分两次，挽救了老特拉福德阿斯顿维拉令人难以置信的4-4平局，这仍然使他们处于降级区</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c5m2ddz437nzo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="哈比·阿隆索（ Xabi Alonso ）的沮丧情绪显而易见，因为切尔西（ Chelsea ）在1-0击败桑德兰（ Sunderland ）的情况下继续为身份而斗争。" data-title="&#39;Tinkerman&#39; Alonso&#39;s Chelsea side still searching for identity" data-date="11-09 02:20" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-09 02:20</span>
          <span class="news-item-title">“小叮当”阿隆索的切尔西球队仍在寻找身份</span>
          <span class="news-item-title-en">'Tinkerman' Alonso's Chelsea side still searching for identity</span>
          <span class="news-value-point">💡 哈比·阿隆索（ Xabi Alonso ）的沮丧情绪显而易见，因为切尔西（ Chelsea ）在1-0击败桑德兰（ Sunderland ）的情…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/024/363.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="小米 17 Pro 手机 2025 年 9 月 25 日发布，16+512G 定价 5599 元。京东 11.11 大促期间，活动价 5199 元；PLUS 会员下单立减 25.99 元；领取 9 折优惠券：点此领取；国家补贴立减 500 元；商品详情页右上角直播间可领 200 元优惠券：到手价为 4173.01 元：京东小米 17 Pro 手机 16GB+512GB 4173.01 元直达链接下单赠送复古掌机保护壳。京东 11.11 红包至高 26888 元无门槛可用，每天可抽一次：点此抽取。京东小米 17 Pro 手机 16GB+512GB 4173.01 元直达链接京东 11.11 无门槛红包 面额至高 26888 元，每天抽 3 次：点此抽红包。淘宝 11.11 无门槛红包 面额至高" data-title="赠复古掌机保护壳：小米 17 Pro 手机 16+512G 版国补后 5599 → 4173 元" data-date="11-09 16:45" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-09 16:45</span>
          <span class="news-item-title">赠复古掌机保护壳：小米 17 Pro 手机 16+512G 版国补后 5599 → 4173 元</span>
          <span class="news-value-point">💡 小米 17 Pro 手机 2025 年 9 月 25 日发布，16+512G 定价 5599 元</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/024/361.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 9 日消息，微信支付宣布已接入冰岛多家当地商户，覆盖机场交通、免税购物、餐饮住宿以及温泉等多个消费场景。微信表示，微信支付已能够在 Flybus 机场快线使用，游客抵达机场后，可以使用微信支付购买机场交通服务。用户还可在机场 Island Duty Free 免税店、Point 便利店、Food Court / Elda 等餐饮场所快捷支付。除此之外，微信支付“全球有礼”冰岛专区已经上线，游客在 Island Duty Free 免税店消费满 500 元可以减 50 元。在参与活动的冰岛本地品牌购物，还有机会获得随机立减优惠。对于准备去冰岛旅行的人来说，以后在机场买票、免税店购物、蓝湖温泉打卡时，又多了一种熟悉的付款选择。" data-title="微信支付宣布接入冰岛多家当地商户，同步上线“全球有礼”冰岛专区" data-date="11-09 16:40" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-09 16:40</span>
          <span class="news-item-title">微信支付宣布接入冰岛多家当地商户，同步上线“全球有礼”冰岛专区</span>
          <span class="news-value-point">💡 IT之家 11 月 9 日消息，微信支付宣布已接入冰岛多家当地商户，覆盖机场交通、免税购物、餐饮住宿以及温泉等多个消费场景</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/024/359.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 9 日消息，捷豹路虎中国今天（9 日）下午通过公众号发布《关于警惕冒用捷豹路虎名义发送虚假车辆召回信息的声明》称，近日关注到有不法分子冒用国家市场监督总局及捷豹路虎品牌名义，通过短信、电话、社交媒体等渠道向部分客户发送所谓“车辆召回通知”、“安全隐患整改通知”、“召回补偿通知”等信息，诱导客户点击不明链接或提供个人敏感信息。捷豹路虎中国向用户发出提醒：认准官方渠道发布的召回信息、警惕以“召回”为名实施的诈骗行为、妥善保护个人信息和财产安全。一、请认准官方渠道发布的召回信息捷豹路虎车辆召回信息将严格按照相关法律法规要求，通过官方渠道进行发布和通知。客户可通过以下官方渠道获取和核实相关信息：国家市场监督管理总局及相关主管部门官方公告渠道；捷豹路虎官方客户服务热线 400-82" data-title="捷豹路虎提醒：警惕不法分子发送虚假车辆召回信息" data-date="11-09 16:39" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-09 16:39</span>
          <span class="news-item-title">捷豹路虎提醒：警惕不法分子发送虚假车辆召回信息</span>
          <span class="news-value-point">💡 IT之家 11 月 9 日消息，捷豹路虎中国今天（9 日）下午通过公众号发布《关于警惕冒用捷豹路虎名义发送虚假车辆召回信息的声明》称，近日关注到…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/024/357.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 9 日消息，据《连线》（WIRED）报道，上周三下午，杰米 · 罗宾斯（Jamie Robins）来到谷歌位于英国伦敦国王十字区的总部。他手中拿着一封信，里面附有一份由近 5.5 万人签署的请愿书，要求谷歌放弃在伦敦以东约 24 公里的瑟罗克（Thurrock）建设大型数据中心的计划。罗宾斯是野生动物保护组织 Buglife 的工作人员。该组织目前与多个背景各异的团体组成了一个不太寻常的联盟，共同反对谷歌的数据中心项目。Buglife 和当地野生动物保护团体担心，项目建设将破坏濒危植物、稀有大黄蜂以及其他无脊椎动物的栖息地。非营利组织 Foxglove 则认为，数据中心将产生过多污染。当地的瑟罗克哈默斯摩托车俱乐部（Thurrock Hammers）希望重新获得这块场地，" data-title="谷歌英国数据中心遭近 5.5 万人联名反对，包括摩托骑手和昆虫保护者" data-date="11-09 16:35" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-09 16:35</span>
          <span class="news-item-title">谷歌英国数据中心遭近 5.5 万人联名反对，包括摩托骑手和昆虫保护者</span>
          <span class="news-value-point">💡 IT之家 11 月 9 日消息，据《连线》（WIRED）报道，上周三下午，杰米 · 罗宾斯（Jamie Robins）来到谷歌位于英国伦敦国王十…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/024/356.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 9 日消息，OPPO 官方今日公开了 OPPO Watch 5 智能手表的外观，并宣布新品将在 11 月 16 日 19:00 发布。IT之家注意到，OPPO 官方刚刚公布了这款新手表的核心配置信息，其采用 9.2mm 厚度 + 25g 轻量化设计，支持全场景流体云、灵感表盘 DIY、FatMax 超燃脂模式、13 项睡眠监测，拥有最长 10 天续航能力。" data-title="OPPO Watch 5 智能手表核心亮点公布：全场景流体云、最长 10 天续航，11 月 16 日发布" data-date="11-09 16:32" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-09 16:32</span>
          <span class="news-item-title">OPPO Watch 5 智能手表核心亮点公布：全场景流体云、最长 10 天续航，11 月 16 日发布</span>
          <span class="news-value-point">💡 IT之家 11 月 9 日消息，OPPO 官方今日公开了 OPPO Watch 5 智能手表的外观，并宣布新品将在 11 月 16 日 19:0…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-09/10728885.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="央视网消息：中央气象台9日早6点继续发布大风蓝色预警：预计，9日8点到10日8点，新疆东部、内蒙古中西部、山东半岛、云南东部、广东南部等地的部分地区有5—6级风；黄海中西部和南部海域、东海大部海域、台湾海峡、巴士海峡、南海北部和中部海域、北部湾、琼州海峡将有7—8级、阵风9—10级的大风。" data-title="全力以赴应对寒潮 多地多部门织密织牢“安全网”保出行、保生产、保民生" data-date="11-09 16:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 16:22</span>
          <span class="news-item-title">全力以赴应对寒潮 多地多部门织密织牢“安全网”保出行、保生产、保民生</span>
          <span class="news-value-point">💡 央视网消息：中央气象台9日早6点继续发布大风蓝色预警：预计，9日8点到10日8点，新疆东部、内蒙古中西部、山东半岛、云南东部、广东南部等地的部分…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/golf/news/12040/13610069/world-wide-technology-championship-teenager-blades-brown-becomes-youngest-pga-tour-tournament-winner-in-95-years" target="_blank" rel="noopener" data-cat="zonghe" data-summary="自1931年以来，刀锋布朗已经成为最年轻的PGA巡回赛冠军，此前这位19岁的球员在世界技术锦标赛中以9杆低于63杆击败本·詹姆斯。" data-title="Brown becomes youngest PGA Tour winner in 95 years" data-date="11-09 16:04" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-09 16:04</span>
          <span class="news-item-title">布朗成为95年来最年轻的美巡赛冠军</span>
          <span class="news-item-title-en">Brown becomes youngest PGA Tour winner in 95 years</span>
          <span class="news-value-point">💡 自1931年以来，刀锋布朗已经成为最年轻的PGA巡回赛冠军，此前这位19岁的球员在世界技术锦标赛中以9杆低于63杆击败本·詹姆斯</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-09/10728870.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="近段时间以来，“China Haul(中国购物开箱)”成为海外热词。很多外国游客来华采购，空箱而来、满载而归，再把开箱视频分享到社交平台。从无人机、运动相机、智能穿戴设备等科技潮流新品，到丝绸、瓷器、国潮文创、非遗手作等中式传统好物，一条条视频分享获得无数点赞，弹幕更是被“求链接”刷屏。" data-title="从“想来看看”到“多待多买”，入境游已是next level" data-date="11-09 15:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 15:47</span>
          <span class="news-item-title">从“想来看看”到“多待多买”，入境游已是next level</span>
          <span class="news-value-point">💡 近段时间以来，“China Haul(中国购物开箱)”成为海外热词</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-09/10728869.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="2026年秋季校园招聘正在进行，广大毕业生正处于求职关键阶段。一些不法分子受利益驱使，冒用用人单位名义散布虚假招聘信息，制造、贩卖焦虑，巧立名目收取费用，甚至诱导办理贷款，严重损害毕业生切身利益，扰乱人力资源市场秩序。为此，教育部梳理汇总了近年来出现的求职诈骗典型案例和惯用话术，提醒广大毕业生和家长提高警惕、明辨真伪，通过正规渠道求职。" data-title="教育部发布秋招季求职预警信息" data-date="11-09 15:46" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 15:46</span>
          <span class="news-item-title">教育部发布秋招季求职预警信息</span>
          <span class="news-value-point">💡 2026年秋季校园招聘正在进行，广大毕业生正处于求职关键阶段</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-09/10728849.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网马尼拉11月9日电 菲律宾大气地球物理天文局9日发布公告称，台风“查帕卡”(Cempaka)当天上午8时40分进入菲律宾责任区，并被当地命名为“塞缪尔”(Samuel)。" data-title="台风“查帕卡”进入菲律宾责任区 东北季风将致多地出现强风" data-date="11-09 15:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 15:43</span>
          <span class="news-item-title">台风“查帕卡”进入菲律宾责任区 东北季风将致多地出现强风</span>
          <span class="news-value-point">💡 中新网马尼拉11月9日电 菲律宾大气地球物理天文局9日发布公告称，台风“查帕卡”(Cempaka)当天上午8时40分进入菲律宾责任区，并被当地命…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-09/10728851.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网中山11月9日电 (张璐 张靖可)“这是我第一次近距离现场观演，小演员们都很努力，不少细节令我感动，希望今后有更多演出机会走出去，让更多海内外同胞，通过这部剧，了解孙中山少年时期的成长经历”。孙中山先生玄侄孙孙伟勇8日晚表示，“我为家乡感到骄傲，也希望小演员和广大中山青少年传承正能量，把中山美好、有活力的一面更好呈现出来。”" data-title="首部以少年孙中山为题材的大型原创儿童歌舞剧上演" data-date="11-09 15:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 15:42</span>
          <span class="news-item-title">首部以少年孙中山为题材的大型原创儿童歌舞剧上演</span>
          <span class="news-value-point">💡 中新网中山11月9日电 (张璐 张靖可)“这是我第一次近距离现场观演，小演员们都很努力，不少细节令我感动，希望今后有更多演出机会走出去，让更多海…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13610068/boxing-caroline-dubois-crashes-alycia-baumgardners-post-fight-interview" target="_blank" rel="noopener" data-cat="zonghe" data-summary="WBC轻量级冠军卡罗琳·杜波依斯（ Caroline Dubois ）在鲍姆加德纳（ Baumgardner ）击败埃利夫·努尔·图尔汉（ Elif Nur Turhan ）获得IBF冠军后，呼吁Alycia Baumg" data-title="&#39;Are we going to fight?!&#39; - Dubois crashes Baumgardner&#39;s post-fight interview!" data-date="11-09 15:41" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-09 15:41</span>
          <span class="news-item-title">（我们要打架吗？ ！ '- Dubois撞上了Baumgardner的战后采访！</span>
          <span class="news-item-title-en">'Are we going to fight?!' - Dubois crashes Baumgardner's post-fight interview!</span>
          <span class="news-value-point">💡 WBC轻量级冠军卡罗琳·杜波依斯（ Caroline Dubois ）在鲍姆加德纳（ Baumgardner ）击败埃利夫·努尔·图尔汉（ El…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13610067/elif-nur-turhan-vs-alycia-baumgardner-fight-highlights" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Elif Nur Turhan和Alycia Baumgardner之间的IBF轻量级世界冠军争夺战的亮点。" data-title="Turhan vs Baumgardner - Lightweight world title fight highlights" data-date="11-09 15:38" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-09 15:38</span>
          <span class="news-item-title">Turhan vs Baumgardner -轻量级世界冠军争夺战亮点</span>
          <span class="news-item-title-en">Turhan vs Baumgardner - Lightweight world title fight highlights</span>
          <span class="news-value-point">💡 Elif Nur Turhan和Alycia Baumgardner之间的IBF轻量级世界冠军争夺战的亮点</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-09/10728845.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="光是什么？" data-title="青春红岩 | 做自己的光" data-date="11-09 15:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 15:35</span>
          <span class="news-item-title">青春红岩 | 做自己的光</span>
          <span class="news-value-point">💡 光是什么</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/508629.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="最早量产的亲自泼冷水" data-title="L3大撤退！奔驰宝马官宣不玩了：还没L2好用" data-date="11-09 15:02" data-source="量子位">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-09 15:02</span>
          <span class="news-item-title">L3大撤退！奔驰宝马官宣不玩了：还没L2好用</span>
          <span class="news-value-point">💡 最早量产的亲自泼冷水</span>
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


<p class="news-updated">🕐 抓取更新于 2026-11-09 16:47（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
