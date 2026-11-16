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
      <span>2026-11-17 06:23 抓取更新</span>
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
        <span class="channel-count">53</span>
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
      <button class="channel-btn" onclick="filterNewsChannel('meimei', this)">
        <span>🌍 西方媒体视角</span>
        <span class="channel-count">1</span>
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
  <div class="ov-item"><span class="ov-num">53</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×13 · 纽约时报×7</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">按来源聚合 · 最近 24 小时精选</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/11-17/10733163.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社德黑兰11月16日电(记者刁慧琳 沙达提)据伊朗伊斯兰共和国广播电视台16日报道，伊中部伊斯法罕省政府安全事务副省长阿克巴尔·萨利希否认当天有关伊斯法罕地区防空系统启动的消息，称在该省领空未发现、也没有出现任何敌方飞行器。" data-title="伊朗官方否认伊斯法罕省启动防空系统" data-date="11-17 05:53" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 11-17 05:53</span>
      </div>
      <h2 class="hero-featured-title">伊朗官方否认伊斯法罕省启动防空系统</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.tomshardware.com/tech-industry/supercomputers/china-retains-fastest-supercomputer-in-the-world-crown-as-ai-data-centers-soak-up-new-hardware-top500-records-fewest-new-systems-in-33-years" target="_blank" rel="noopener" data-cat="keji" data-summary="The Top 500 list records the fewest new entrants in its history amid a massive shift in compute infrastructure investments towards AI factories." data-title="China retains fastest supercomputer in the world crown as AI data centers soak up new hardware" data-date="11-17 06:17" data-source="Tom's Hardware">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
      </div>
      <p class="hero-sub-title">China retains fastest supercomputer in the world crown as AI data centers soak up new hardware</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/football/news/12040/13612986/declan-rice-contract-arsenal-midfielder-verbally-agrees-new-320000-a-week-deal-with-the-premier-league-champions" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Declan Rice has verbally agreed terms on a new long-term contract at Arsenal, Sky Sports News can reveal." data-title="Rice verbally agrees new Arsenal contract" data-date="11-17 05:12" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">Rice verbally agrees new Arsenal contract</p>
    </a>
    <a class="hero-sub-card" href="https://www.tomshardware.com/gift-guides-seasonal-sales/15-retro-tech-gift-ideas-for-the-nostalgic-gamer-or-builder-in-your-life-old-school-designs-packed-with-modern-hardware-from-game-controllers-to-desk-accessories" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Pick up a retro tech gift for yourself or a loved one this holiday season, from mini PCs to old-school controllers." data-title="15 retro tech gift ideas for the nostalgic gamer or builder in your life" data-date="11-17 06:20" data-source="Tom's Hardware">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
      </div>
      <p class="hero-sub-title">15 retro tech gift ideas for the nostalgic gamer or builder in your life</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-17/10733163.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社德黑兰11月16日电(记者刁慧琳 沙达提)据伊朗伊斯兰共和国广播电视台16日报道，伊中部伊斯法罕省政府安全事务副省长阿克巴尔·萨利希否认当天有关伊斯法罕地区防空系统启动的消息，称在该省领空未发现、也没有出现任何敌方飞行器。" data-title="伊朗官方否认伊斯法罕省启动防空系统" data-date="11-17 05:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 05:53</span>
          <span class="news-item-title">伊朗官方否认伊斯法罕省启动防空系统</span>
          <span class="news-value-point">💡 新华社德黑兰11月16日电(记者刁慧琳 沙达提)据伊朗伊斯兰共和国广播电视台16日报道，伊中部伊斯法罕省政府安全事务副省长阿克巴尔·萨利希否认当…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-17/10733162.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中国常驻联合国代表傅聪16日在安理会叙利亚问题公开会上发言，敦促叙过渡政府推进包容治理进程。" data-title="中方敦促推进叙利亚包容治理进程" data-date="11-17 05:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 05:52</span>
          <span class="news-item-title">中方敦促推进叙利亚包容治理进程</span>
          <span class="news-value-point">💡 中国常驻联合国代表傅聪16日在安理会叙利亚问题公开会上发言，敦促叙过渡政府推进包容治理进程</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-17/10733161.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间11月16日，波黑新一届主席团在首都萨拉热窝举行宣誓就职典礼。" data-title="波黑新一届主席团成员宣誓就职" data-date="11-17 00:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 00:36</span>
          <span class="news-item-title">波黑新一届主席团成员宣誓就职</span>
          <span class="news-value-point">💡 当地时间11月16日，波黑新一届主席团在首都萨拉热窝举行宣誓就职典礼</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-17/10733160.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间16日，俄罗斯总统助理乌沙科夫称，下一轮乌克兰问题俄美乌三方会谈将继续在阿布扎比举行，时间待定。" data-title="俄称下轮俄美乌三方会谈仍在阿布扎比举行 时间待定" data-date="11-17 00:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 00:36</span>
          <span class="news-item-title">俄称下轮俄美乌三方会谈仍在阿布扎比举行 时间待定</span>
          <span class="news-value-point">💡 当地时间16日，俄罗斯总统助理乌沙科夫称，下一轮乌克兰问题俄美乌三方会谈将继续在阿布扎比举行，时间待定</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-17/10733158.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京11月16日电 题：第十四届中部博览会开幕在即 助力中部地区加快崛起" data-title="第十四届中部博览会开幕在即 助力中部地区加快崛起" data-date="11-17 00:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 00:24</span>
          <span class="news-item-title">第十四届中部博览会开幕在即 助力中部地区加快崛起</span>
          <span class="news-value-point">💡 新华社北京11月16日电 题：第十四届中部博览会开幕在即 助力中部地区加快崛起</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-16/10733157.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社布鲁塞尔11月16日电 (记者 德永健)欧盟16日对俄罗斯发起新一轮制裁，将145名个人和实体列为制裁对象。" data-title="欧盟对俄罗斯发起新一轮制裁列单145名个人和实体" data-date="11-16 23:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-16 23:54</span>
          <span class="news-item-title">欧盟对俄罗斯发起新一轮制裁列单145名个人和实体</span>
          <span class="news-value-point">💡 中新社布鲁塞尔11月16日电 (记者 德永健)欧盟16日对俄罗斯发起新一轮制裁，将145名个人和实体列为制裁对象</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/16/world/europe/iran-dams-missile-sites-environmentalists.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="长期以来，环保人士一直对一个庞大的水利项目网络感到困惑，因为这些项目缺乏任何明显的合理性。随后，这些区域成为空袭的目标。" data-title="Airstrikes on Iran Missile Sites May Shed Light on Justification for Dams" data-date="11-16 23:39" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-16 23:39</span>
          <span class="news-item-title">对伊朗导弹基地的空袭或可为大坝的合理性提供佐证</span>
          <span class="news-item-title-en">Airstrikes on Iran Missile Sites May Shed Light on Justification for Dams</span>
          <span class="news-value-point">💡 长期以来，环保人士一直对一个庞大的水利项目网络感到困惑，因为这些项目缺乏任何明显的合理性</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cwe85djzkkv5o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中国、俄罗斯和美国领导人正筹备首次三方会晤，引发欧洲忧虑。一些人认为，这令人联想到第二次世界大战后，大国将世界划分为不同势力范围的历史。" data-title="习近平、特朗普与普京历史性会晤，将对世界意味什么？" data-date="11-16 22:38" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-16 22:38</span>
          <span class="news-item-title">习近平、特朗普与普京历史性会晤，将对世界意味什么？</span>
          <span class="news-value-point">💡 中国、俄罗斯和美国领导人正筹备首次三方会晤，引发欧洲忧虑</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-16/10733137.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社深圳11月16日电 题：从大雁到大鹏 十二载后APEC再回中国" data-title="（深圳APEC）从大雁到大鹏 十二载后APEC再回中国" data-date="11-16 22:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-16 22:35</span>
          <span class="news-item-title">（深圳APEC）从大雁到大鹏 十二载后APEC再回中国</span>
          <span class="news-value-point">💡 中新社深圳11月16日电 题：从大雁到大鹏 十二载后APEC再回中国</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-16/10733104.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社深圳11月16日电 题：习近平眼中“亚太的成功”" data-title="（近观中国）习近平眼中“亚太的成功”" data-date="11-16 22:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-16 22:12</span>
          <span class="news-item-title">（近观中国）习近平眼中“亚太的成功”</span>
          <span class="news-value-point">💡 中新社深圳11月16日电 题：习近平眼中“亚太的成功”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-16/10733126.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社深圳11月16日电(记者赵瀚泽、杨深深)加拿大总理卡尼16日抵达深圳，将出席亚太经合组织第三十三次领导人非正式会议。" data-title="聚焦APEC｜加拿大总理卡尼抵达深圳" data-date="11-16 22:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-16 22:10</span>
          <span class="news-item-title">聚焦APEC｜加拿大总理卡尼抵达深圳</span>
          <span class="news-value-point">💡 新华社深圳11月16日电(记者赵瀚泽、杨深深)加拿大总理卡尼16日抵达深圳，将出席亚太经合组织第三十三次领导人非正式会议</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-16/10733062.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网约翰内斯堡11月16日电 “在地缘政治格局深刻演变的当下，不断发展的中非关系已成为全球南方国家合作的重要支撑。”南非公共行政领域学者拉索迪·胡索·马尼亚卡(Rasodi Khutso Manyaka)在“全球南方·中国方案”研讨会上指出。" data-title="南非学者：“中国方案”走向全球南方应更重视文化维度" data-date="11-16 22:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-16 22:02</span>
          <span class="news-item-title">南非学者：“中国方案”走向全球南方应更重视文化维度</span>
          <span class="news-value-point">💡 中新网约翰内斯堡11月16日电 “在地缘政治格局深刻演变的当下，不断发展的中非关系已成为全球南方国家合作的重要支撑</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-16/10733046.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="“亚太发展前景取决于今天的决断和行动。我们有责任为本地区人民创造和实现亚太梦想。”" data-title="聚焦APEC·视频画报｜同舟共济 共创亚太美好未来" data-date="11-16 21:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-16 21:52</span>
          <span class="news-item-title">聚焦APEC·视频画报｜同舟共济 共创亚太美好未来</span>
          <span class="news-value-point">💡 “亚太发展前景取决于今天的决断和行动</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-16/10733093.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京11月16日电 题：凝聚四海侨心侨力 砥砺爱国强国之志——习近平总书记致暨南大学建校120周年的贺信激发团结奋进新征程强大力量" data-title="总书记致暨南大学贺信激发团结奋进新征程强大力量" data-date="11-16 21:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-16 21:50</span>
          <span class="news-item-title">总书记致暨南大学贺信激发团结奋进新征程强大力量</span>
          <span class="news-value-point">💡 新华社北京11月16日电 题：凝聚四海侨心侨力 砥砺爱国强国之志——习近平总书记致暨南大学建校120周年的贺信激发团结奋进新征程强大力量</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-16/10733103.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="APEC领导人会议周相关活动正在密集展开。2026年APEC工商咨询理事会第四次会议将于今天闭幕。2026年APEC领导人会议周新闻中心今天下午举办两场发布会，介绍APEC工商咨询理事会全年工作成果及第四次会议情况、APEC“中国年”经贸合作有关情况。" data-title="在这里看见未来丨世界目光聚焦中国 亚太同心共赴未来" data-date="11-16 21:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-16 21:48</span>
          <span class="news-item-title">在这里看见未来丨世界目光聚焦中国 亚太同心共赴未来</span>
          <span class="news-value-point">💡 APEC领导人会议周相关活动正在密集展开</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/supercomputers/china-retains-fastest-supercomputer-in-the-world-crown-as-ai-data-centers-soak-up-new-hardware-top500-records-fewest-new-systems-in-33-years" target="_blank" rel="noopener" data-cat="keji" data-summary="The Top 500 list records the fewest new entrants in its history amid a massive shift in compute infrastructure investments towards AI factories." data-title="China retains fastest supercomputer in the world crown as AI data centers soak up new hardware" data-date="11-17 06:17" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-17 06:17</span>
          <span class="news-item-title">China retains fastest supercomputer in the world crown as AI data centers soak up new hardware</span>
          <span class="news-value-point">💡 The Top 500 list records the fewest new entrants in its history amid a m…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/16/all-the-questions-nvidia-should-answer-on-tuesday-but-probably-wont/" target="_blank" rel="noopener" data-cat="keji" data-summary="Nvidia interim CEO and long-time CFO Colette Kress is about to have one of the biggest days of her career on Tuesday when the company reports its third quarter results. Given the turmoil Nvidia is in, there are a number of questions that Nvidia should answer." data-title="All the questions Nvidia should answer on Tuesday" data-date="11-17 06:03" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-17 06:03</span>
          <span class="news-item-title">All the questions Nvidia should answer on Tuesday</span>
          <span class="news-value-point">💡 Nvidia interim CEO and long-time CFO Colette Kress is about to have one …</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/new-us-rules-aim-to-restrict-remote-access-to-ai-servers-and-infrastructure-seeks-to-combat-cloud-rental-workarounds-to-gpu-export-controls" target="_blank" rel="noopener" data-cat="keji" data-summary="The Bureau of Industry and Security has announced a new interim final rule to ensure restrictions on the export of physical AI hardware cannot be bypassed by accessing it remotely in data centers around the world." data-title="New US rules aim to restrict Chinese firms’ remote access to AI servers and infrastructure" data-date="11-17 05:50" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-17 05:50</span>
          <span class="news-item-title">New US rules aim to restrict Chinese firms’ remote access to AI servers and infrastructure</span>
          <span class="news-value-point">💡 The Bureau of Industry and Security has announced a new interim final ru…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/supercomputers/researchers-recognize-that-ai-will-never-replace-hpc-says-amd-executive-high-precision-workloads-will-exist-for-a-very-long-time-even-as-ai-usage-expands" target="_blank" rel="noopener" data-cat="keji" data-summary="The emergence of AI has seemingly posed a threat to high-precision FP64 computation, but AMD doesn&#39;t think the HPC world is moving away from those complex calculations in the wake of AI." data-title="Researchers ‘recognize that AI will never replace HPC,’ says AMD executive — high-precision workloads will ‘exist for a very long time’ even as AI usage expands" data-date="11-17 05:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-17 05:30</span>
          <span class="news-item-title">Researchers ‘recognize that AI will never replace HPC,’ says AMD executive — high-precision workloads will ‘exist for a very long time’ even as AI usage expands</span>
          <span class="news-value-point">💡 The emergence of AI has seemingly posed a threat to high-precision FP64 …</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/supercomputers/amd-grabs-over-40-percent-of-new-top500-list-for-supercomputers-up-14-percent-since-last-year-new-lux-system-developed-between-amd-and-department-of-energy-debuts-at-no-14-with-epyc-cpus-and-instinct-mi355x-gpus" target="_blank" rel="noopener" data-cat="keji" data-summary="AMD&#39;s Lux supercomputer debuted at position 14 on the new TOP500 list published during SC26. It&#39;s one of two machines AMD is developing as part of a $1 billion deal with the U.S. Department of Energy." data-title="AMD grabs over 40% of new TOP500 list for supercomputers, up 14% since last year" data-date="11-17 05:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-17 05:00</span>
          <span class="news-item-title">AMD grabs over 40% of new TOP500 list for supercomputers, up 14% since last year</span>
          <span class="news-value-point">💡 AMD's Lux supercomputer debuted at position 14 on the new TOP500 list pu…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1034815/california-openai-hugging-face-lawsuit" target="_blank" rel="noopener" data-cat="keji" data-summary="California is suing OpenAI after its AI agents broke out of their testing environment and hacked other companies, including Hugging Face. In a lawsuit on Monday, Attorney General Rob Bonta accuses OpenAI of violating consumer safety law by knowingly developing a &quot;dangerous product without proper oversight,&quot; as reported earlier by Reuters. The lawsu" data-title="California sues OpenAI over rogue AI hacking incidents" data-date="11-17 04:46" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-17 04:46</span>
          <span class="news-item-title">California sues OpenAI over rogue AI hacking incidents</span>
          <span class="news-value-point">💡 California is suing OpenAI after its AI agents broke out of their testin…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1034787/sam-altman-ram-shortage-semafor" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI CEO Sam Altman is once again addressing his controversial comments on PC RAM purchases. &quot;I want to be clear, I want people to have a lot of RAM, I think everybody should be able to buy a lot of RAM for their own computer,&quot; Altman said today. &quot;I think the home tinkering is great.&quot; […]" data-title="Sam Altman says he wants everyone ‘to have a lot of RAM’" data-date="11-17 04:41" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-17 04:41</span>
          <span class="news-item-title">Sam Altman says he wants everyone ‘to have a lot of RAM’</span>
          <span class="news-value-point">💡 OpenAI CEO Sam Altman is once again addressing his controversial comment…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1034668/data-centers-electricity-climate-pollution-study-harvard" target="_blank" rel="noopener" data-cat="keji" data-summary="Fossil fuels are still the biggest source of electricity for hyperscale data centers in the US, a new paper published in the journal Nature Sustainability shows. They likely burn through more electricity collectively than many countries do, resulting in a serious amount of greenhouse gas emissions. The study homes in on hyperscale facilities - the" data-title="US data centers now burn more electricity than a midsized country" data-date="11-17 04:27" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-17 04:27</span>
          <span class="news-item-title">US data centers now burn more electricity than a midsized country</span>
          <span class="news-value-point">💡 Fossil fuels are still the biggest source of electricity for hyperscale …</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/16/california-state-ag-sues-openai-over-rogue-agent-incidents/" target="_blank" rel="noopener" data-cat="keji" data-summary="The California lawsuit represents one of the first attempts to hold an AI lab legally accountable for a rogue agent incident" data-title="California state AG sues OpenAI over rogue agent incidents" data-date="11-17 04:07" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-17 04:07</span>
          <span class="news-item-title">California state AG sues OpenAI over rogue agent incidents</span>
          <span class="news-value-point">💡 The California lawsuit represents one of the first attempts to hold an A…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/16/trump-says-ex-nvidia-ceo-jensen-huangs-affair-with-an-alleged-chinese-spy-did-not-threaten-national-security/" target="_blank" rel="noopener" data-cat="keji" data-summary="Trump contradicted his own government&#39;s intelligence officials, who reportedly concluded that Alice Huang is a Chinese spy." data-title="Trump says ex-Nvidia CEO Jensen Huang’s affair with an alleged Chinese spy did not threaten national security" data-date="11-17 03:12" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-17 03:12</span>
          <span class="news-item-title">Trump says ex-Nvidia CEO Jensen Huang’s affair with an alleged Chinese spy did not threaten national security</span>
          <span class="news-value-point">💡 Trump contradicted his own government's intelligence officials, who repo…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/nvidia-announces-rubin-hpc-gpu-with-record-number-of-cuda-cores-at-supercomputing-2026-new-chip-accelerates-agentic-hpc-workloads-arrives-in-2028" target="_blank" rel="noopener" data-cat="keji" data-summary="Nvidia took the wraps off its Rubin HPC GPU at Supercomputing 2026. This new GPU will give scientists, engineers, and analysts over 50,000 CUDA cores to speed up agentic HPC workloads when it arrives in 2028." data-title="Nvidia announces Rubin HPC GPU with &#39;record number of CUDA cores&#39; at Supercomputing 2026" data-date="11-17 03:05" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-17 03:05</span>
          <span class="news-item-title">Nvidia announces Rubin HPC GPU with 'record number of CUDA cores' at Supercomputing 2026</span>
          <span class="news-value-point">💡 Nvidia took the wraps off its Rubin HPC GPU at Supercomputing 2026. This…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/trump-calls-for-jensen-huang-reinstatement-as-nvidia-ceo-nvidia-board-reportedly-refuses-to-reinstate-disgraced-ceo-due-to-ongoing-national-security-investigation-into-jensen" target="_blank" rel="noopener" data-cat="keji" data-summary="President Trump has called for Jensen Huang to return as Nvidia CEO, but a new report says the board is not considering the move." data-title="Trump calls for Jensen Huang reinstatement as Nvidia CEO" data-date="11-17 02:24" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-17 02:24</span>
          <span class="news-item-title">Trump calls for Jensen Huang reinstatement as Nvidia CEO</span>
          <span class="news-value-point">💡 President Trump has called for Jensen Huang to return as Nvidia CEO, but…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/16/sam-altman-on-nvidia-without-jensen-huang-the-industry-will-be-fine/" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI CEO Sam Altman acknowledged the special role Nvidia CEO Jensen Huang has played in the AI boom, but ultimately thinks the industry will be “fine” without him at the helm." data-title="Sam Altman on Nvidia without Jensen Huang: the industry will be ‘fine’" data-date="11-17 02:11" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-17 02:11</span>
          <span class="news-item-title">Sam Altman on Nvidia without Jensen Huang: the industry will be ‘fine’</span>
          <span class="news-value-point">💡 OpenAI CEO Sam Altman acknowledged the special role Nvidia CEO Jensen Hu…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/16/us/politics/trump-jensen-huang-nvidia.html" target="_blank" rel="noopener" data-cat="keji" data-summary="在准备访问中国之际，总统淡化了黄先生与一名女性的关系所造成的影响，官员们已确认该女性是北京的情报人员。" data-title="Trump Says He’s Open to Reinstatement of Jensen Huang as Nvidia Chief" data-date="11-17 01:48" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-17 01:48</span>
          <span class="news-item-title">特朗普表示，他愿意让黄仁勋重返英伟达首席执行官职位</span>
          <span class="news-item-title-en">Trump Says He’s Open to Reinstatement of Jensen Huang as Nvidia Chief</span>
          <span class="news-value-point">💡 在准备访问中国之际，总统淡化了黄先生与一名女性的关系所造成的影响，官员们已确认该女性是北京的情报人员</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/16/openai-will-embed-apollo-researchers-to-investigate-ai-subversion/" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI将嵌入六名Apollo Research评估员，以调查其人工智能模型是否从事颠覆性行为，但对访问和披露的限制引发了对其独立性的质疑。" data-title="OpenAI will embed Apollo researchers to investigate AI subversion" data-date="11-17 01:02" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-17 01:02</span>
          <span class="news-item-title">OpenAI 将聘请 Apollo 研究人员来调查人工智能颠覆行为</span>
          <span class="news-item-title-en">OpenAI will embed Apollo researchers to investigate AI subversion</span>
          <span class="news-value-point">💡 OpenAI将嵌入六名Apollo Research评估员，以调查其人工智能模型是否从事颠覆性行为，但对访问和披露的限制引发了对其独立性的质疑</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">7 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13612986/declan-rice-contract-arsenal-midfielder-verbally-agrees-new-320000-a-week-deal-with-the-premier-league-champions" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Declan Rice has verbally agreed terms on a new long-term contract at Arsenal, Sky Sports News can reveal." data-title="Rice verbally agrees new Arsenal contract" data-date="11-17 05:12" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-17 05:12</span>
          <span class="news-item-title">Rice verbally agrees new Arsenal contract</span>
          <span class="news-value-point">💡 Declan Rice has verbally agreed terms on a new long-term contract at Ars…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmge3y2qjlyro?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Will Thomas Frank - now confirmed as the new manager of Crystal Palace - rebuild his reputation at Selhurst Park after a bruising time at Tottenham?" data-title="How Frank can restore reputation and save Crystal Palace" data-date="11-17 01:46" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-17 01:46</span>
          <span class="news-item-title">弗兰克如何挽回声誉并拯救水晶宫</span>
          <span class="news-item-title-en">How Frank can restore reputation and save Crystal Palace</span>
          <span class="news-value-point">💡 Will Thomas Frank - now confirmed as the new manager of Crystal Palace -…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13610988/thomas-frank-crystal-palace-appoint-former-spurs-and-brentford-boss-as-pierre-sages-successor-at-selhurst-park" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="水晶宫任命托马斯·弗兰克为新任主教练。" data-title="Frank appointed Crystal Palace manager" data-date="11-17 01:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-17 01:00</span>
          <span class="news-item-title">弗兰克被任命为水晶宫主教练</span>
          <span class="news-item-title-en">Frank appointed Crystal Palace manager</span>
          <span class="news-value-point">💡 水晶宫任命托马斯·弗兰克为新任主教练</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13610988/thomas-frank-crystal-palace-appoint-former-spurs-and-brentford-boss-as-pierre-sages-successor-at-selhurst-park" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="水晶宫任命托马斯·弗兰克为新任主教练。" data-title="Frank appointed Crystal Palace manager" data-date="11-17 01:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-17 01:00</span>
          <span class="news-item-title">弗兰克被任命为水晶宫主教练</span>
          <span class="news-item-title-en">Frank appointed Crystal Palace manager</span>
          <span class="news-value-point">💡 水晶宫任命托马斯·弗兰克为新任主教练</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025492/man-utd-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Man Utd latest: Pochettino staff arrive in Manchester early to prepare for Liverpool" data-title="Man Utd latest: Pochettino staff arrive in Manchester early to prepare for Liverpool" data-date="11-16 23:30" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-16 23:30</span>
          <span class="news-item-title">曼联最新消息：波切蒂诺的团队提前抵达曼彻斯特，为对阵利物浦的比赛做准备</span>
          <span class="news-item-title-en">Man Utd latest: Pochettino staff arrive in Manchester early to prepare for Liverpool</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/12476234/transfer-centre-live-football-transfer-news-updates-and-rumours" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Transfer Centre LIVE! Vini Jr admits to feeling overwhelmed by Arsenal speculation" data-title="Transfer Centre LIVE! Vini Jr admits to feeling overwhelmed by Arsenal speculation" data-date="11-16 21:50" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-16 21:50</span>
          <span class="news-item-title">转会中心直播！维尼修斯承认对阿森纳的绯闻感到不知所措</span>
          <span class="news-item-title-en">Transfer Centre LIVE! Vini Jr admits to feeling overwhelmed by Arsenal speculation</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/12507208/football-latest-news-gossip" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Kaveh Q&amp;A LIVE! YOUR questions answered here - and nothing off limits!" data-title="Kaveh Q&amp;A LIVE! YOUR questions answered here - and nothing off limits!" data-date="11-16 21:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-16 21:00</span>
          <span class="news-item-title">Kaveh 问答直播！您的疑问将在这里得到解答——没有任何禁忌！</span>
          <span class="news-item-title-en">Kaveh Q&A LIVE! YOUR questions answered here - and nothing off limits!</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.tomshardware.com/gift-guides-seasonal-sales/15-retro-tech-gift-ideas-for-the-nostalgic-gamer-or-builder-in-your-life-old-school-designs-packed-with-modern-hardware-from-game-controllers-to-desk-accessories" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Pick up a retro tech gift for yourself or a loved one this holiday season, from mini PCs to old-school controllers." data-title="15 retro tech gift ideas for the nostalgic gamer or builder in your life" data-date="11-17 06:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-17 06:20</span>
          <span class="news-item-title">15 retro tech gift ideas for the nostalgic gamer or builder in your life</span>
          <span class="news-value-point">💡 Pick up a retro tech gift for yourself or a loved one this holiday seaso…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/16/us/bank-outages-down.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="After technical problems grounded flights nationwide and Microsoft products failed, the banking issues added to a sense of doom about the systems underpinning daily life." data-title="Chase Bank Transactions Disrupted by ‘Technical Issue’ Amid Outage Reports" data-date="11-17 06:12" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-17 06:12</span>
          <span class="news-item-title">Chase Bank Transactions Disrupted by ‘Technical Issue’ Amid Outage Reports</span>
          <span class="news-value-point">💡 After technical problems grounded flights nationwide and Microsoft produ…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/16/movies/james-bond-robert-pattinson.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这一公告结束了多年来关于丹尼尔·克雷格（Daniel Craig）在出演五部电影后，谁将接替其角色的猜测。" data-title="Robert Pattinson Named as the Next James Bond" data-date="11-17 06:10" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-17 06:10</span>
          <span class="news-item-title">罗伯特·帕丁森被选为下一任詹姆斯·邦德</span>
          <span class="news-item-title-en">Robert Pattinson Named as the Next James Bond</span>
          <span class="news-value-point">💡 这一公告结束了多年来关于丹尼尔·克雷格（Daniel Craig）在出演五部电影后，谁将接替其角色的猜测</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/16/movies/robert-pattinson-new-bond.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Robert Pattinson’s gift for portraying petulant losers would seem at odds with the requirements for 007. But the actor may be just what the franchise needs." data-title="Why Robert Pattinson Could Be a Great James Bond" data-date="11-17 06:03" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-17 06:03</span>
          <span class="news-item-title">Why Robert Pattinson Could Be a Great James Bond</span>
          <span class="news-value-point">💡 Robert Pattinson’s gift for portraying petulant losers would seem at odd…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/16/movies/james-bond-actors-reviews.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="007 的选角不可避免地引发了争议，而最初的反应并不一定与最终的评价相符。" data-title="There’s a New James Bond, Again. How Did the Last Ones Fare?" data-date="11-17 05:54" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-17 05:54</span>
          <span class="news-item-title">又一位新詹姆斯·邦德诞生了。前几任表现如何？</span>
          <span class="news-item-title-en">There’s a New James Bond, Again. How Did the Last Ones Fare?</span>
          <span class="news-value-point">💡 007 的选角不可避免地引发了争议，而最初的反应并不一定与最终的评价相符</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/entertainment/1033466/hulu-disney-plus-get-huge-looksmaxxing-to-death" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Before Clavicular and other manosphere streamers were introducing young guys to the concept of breaking their facial bones to become more attractive, there was an older generation of creators building massive followings with content focused on chemical biohacking. Were it not for steroid-obsessed influencers like Anthony &quot;Tony Huge&quot; Hughes launchin" data-title="In Get Huge, the manosphere is here to make friends — with deadly consequences" data-date="11-17 05:41" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-17 05:41</span>
          <span class="news-item-title">In Get Huge, the manosphere is here to make friends — with deadly consequences</span>
          <span class="news-value-point">💡 Before Clavicular and other manosphere streamers were introducing young …</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/16/us/politics/trump-china-ai-chip-loophole.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这些规则一直是行政部门激烈争论的话题，并将削弱为中国公司提供服务的蓬勃发展的数据中心业务。" data-title="Trump Administration Moves to Close A.I. Chip Loophole Ahead of China Trip" data-date="11-17 05:07" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-17 05:07</span>
          <span class="news-item-title">特朗普政府在访华前采取行动，以堵住人工智能芯片的漏洞</span>
          <span class="news-item-title-en">Trump Administration Moves to Close A.I. Chip Loophole Ahead of China Trip</span>
          <span class="news-value-point">💡 这些规则一直是行政部门激烈争论的话题，并将削弱为中国公司提供服务的蓬勃发展的数据中心业务</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1034339/sony-black-friday-game-sale-2026-deals" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Black Friday is approaching, and some companies are already rolling out the discounts ahead of the big day. If you’re hunting for PlayStation 5 accessories, we’ve already rounded up some of our favorite controllers and headsets from Sony’s ongoing promotion. However, if you’re looking to expand your library, some of the PS5’s biggest titles are […]" data-title="Some of our favorite PlayStation games are steeply discounted for Black Friday" data-date="11-17 04:36" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-17 04:36</span>
          <span class="news-item-title">Some of our favorite PlayStation games are steeply discounted for Black Friday</span>
          <span class="news-value-point">💡 Black Friday is approaching, and some companies are already rolling out …</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/tennis/news/12040/13612925/henry-patten-british-doubles-no-1-takes-swipe-at-atp-chairman-and-ceo-for-absence-from-trophy-presentation" target="_blank" rel="noopener" data-cat="zonghe" data-summary="British doubles No 1 Henry Patten has taken a swipe at ATP bosses for their absence from a trophy presentation in Turin on Monday." data-title="British doubles No 1 criticises ATP bosses at trophy presentation absence" data-date="11-17 04:05" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-17 04:05</span>
          <span class="news-item-title">British doubles No 1 criticises ATP bosses at trophy presentation absence</span>
          <span class="news-value-point">💡 British doubles No 1 Henry Patten has taken a swipe at ATP bosses for th…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1034512/apple-watch-series-12-black-friday-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="If you’re still sporting an Apple Watch that launched five or so years ago, now is a good time to upgrade. Apple’s latest smartwatch, the 42mm Apple Watch Series 12 with Wi-Fi and GPS connectivity, has dropped to a new all-time low of $329 at Amazon, Best Buy, and Walmart, beating the October Prime Day […]" data-title="The Apple Watch Series 12 is cheaper than ever ahead of Black Friday" data-date="11-17 03:50" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-17 03:50</span>
          <span class="news-item-title">The Apple Watch Series 12 is cheaper than ever ahead of Black Friday</span>
          <span class="news-value-point">💡 If you’re still sporting an Apple Watch that launched five or so years a…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/transportation/1034321/mercedes-benz-mb-drive-assist-pro-hands-free-highway-assist-2027" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Mercedes-Benz is tossing its hat into the partial autonomy ring with the launch of two new features next year: hands-free highway driving and a point-to-point city navigation system. The new features will put the German automaker in competition with Tesla, which is currently leading the auto industry in the development of hands-free systems. Merced" data-title="Mercedes-Benz takes on Tesla FSD with new point-to-point city driving assist" data-date="11-17 03:49" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-17 03:49</span>
          <span class="news-item-title">Mercedes-Benz takes on Tesla FSD with new point-to-point city driving assist</span>
          <span class="news-value-point">💡 Mercedes-Benz is tossing its hat into the partial autonomy ring with the…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/028/016.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="【点此直达升级教程】 IT之家 11 月 17 日消息，苹果今日向 Apple Watch 用户推送了 watchOS 27.3 开发者预览版 Beta 2 更新（内部版本号：24S5296d），本次更新距离上次发布 Beta/RC 间隔 13 天。 如何升级 iOS / iPadOS / watchOS / macOS 开发版和公测版？• 公开测试版：需注册 Apple Beta 版软件计划，之后通过【设置】【通用】【软件更新】【Beta 版更新】来升级；• 开发预览版：需登录注册苹果开发者计划，之后通过【设置】【通用】【软件更新】来升级。附苹果 iOS 历史固件下载大全：《苹果 iOS / iPadOS / macOS 固件下载 / 更新日志大全》 本文由机器人发布，IT之家稍后将为大家" data-title="苹果 watchOS 27.3 开发者预览版 Beta 2 发布" data-date="11-17 03:19" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-17 03:19</span>
          <span class="news-item-title">苹果 watchOS 27.3 开发者预览版 Beta 2 发布</span>
          <span class="news-value-point">💡 【点此直达升级教程】 IT之家 11 月 17 日消息，苹果今日向 Apple Watch 用户推送了 watchOS 27.3 开发者预览版 …</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/028/015.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 17 日消息，苹果今日向 Vision Pro 用户推送了 visionOS 27.3 开发者预览版 Beta 2 更新（内部版本号：24N5298d），本次更新距离上次发布 Beta/RC 间隔 13 天。 需要注意的是，因苹果各区域节点服务器配置缓存问题，可能有些地方探测到升级更新的时间略有延迟，一般半小时内，不会太久。 本文由机器人发布，IT之家稍后将为大家带来具体更新内容。 附 visionOS 27 发布历史： 2026-11-10：visionOS 27.2.1 (24N124) 2026-10-27：visionOS 27.2 (24N120) 2026-10-20：visionOS 27.2 RC (24N118) 2026-10-14：visionOS" data-title="苹果 visionOS 27.3 开发者预览版 Beta 2 发布" data-date="11-17 03:19" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-17 03:19</span>
          <span class="news-item-title">苹果 visionOS 27.3 开发者预览版 Beta 2 发布</span>
          <span class="news-value-point">💡 IT之家 11 月 17 日消息，苹果今日向 Vision Pro 用户推送了 visionOS 27.3 开发者预览版 Beta 2 更新（内…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/028/014.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 17 日消息，苹果今日向 Mac 电脑用户推送了 macOS 27.3 开发者预览版 Beta 2 更新（内部版本号：26C5047e），本次更新距离上次发布 Beta/RC 间隔 13 天。 如何升级 iOS / iPadOS / watchOS / macOS 开发版和公测版？• 公开测试版：需注册 Apple Beta 版软件计划，之后通过【设置】【通用】【软件更新】【Beta 版更新】来升级；• 开发预览版：需登录注册苹果开发者计划，之后通过【设置】【通用】【软件更新】来升级。附苹果 iOS 历史固件下载大全：《苹果 iOS / iPadOS / macOS 固件下载 / 更新日志大全》 本文由机器人发布，IT之家稍后将为大家带来具体更新内容。 附 macOS 2" data-title="苹果 macOS 27.3 开发者预览版 Beta 2 发布" data-date="11-17 03:19" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-17 03:19</span>
          <span class="news-item-title">苹果 macOS 27.3 开发者预览版 Beta 2 发布</span>
          <span class="news-value-point">💡 IT之家 11 月 17 日消息，苹果今日向 Mac 电脑用户推送了 macOS 27.3 开发者预览版 Beta 2 更新（内部版本号：26C…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/028/013.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="【点此直达升级教程】 IT之家 11 月 17 日消息，苹果今日向 iPhone 和 iPad 用户推送了 iOS/iPadOS 27.3 开发者预览版 Beta 2 更新（内部版本号：24C5049d），本次更新距离上次发布 Beta/RC 间隔 13 天。 如何升级 iOS / iPadOS / watchOS / macOS 开发版和公测版？• 公开测试版：需注册 Apple Beta 版软件计划，之后通过【设置】【通用】【软件更新】【Beta 版更新】来升级；• 开发预览版：需登录注册苹果开发者计划，之后通过【设置】【通用】【软件更新】来升级。附苹果 iOS 历史固件下载大全：《苹果 iOS / iPadOS / macOS 固件下载 / 更新日志大全》 本文由机器人发布，IT之家稍" data-title="苹果 iOS/iPadOS 27.3 开发者预览版 Beta 2 发布" data-date="11-17 03:19" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-17 03:19</span>
          <span class="news-item-title">苹果 iOS/iPadOS 27.3 开发者预览版 Beta 2 发布</span>
          <span class="news-value-point">💡 【点此直达升级教程】 IT之家 11 月 17 日消息，苹果今日向 iPhone 和 iPad 用户推送了 iOS/iPadOS 27.3 开发…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🌍</span>
      <span class="news-category-title">西方媒体视角 (外媒看中国 · 奇葩言论集锦)</span>
      <span class="news-category-count">1 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cr7428z1wx74o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="meimei" data-summary="台湾“九合一”地方选举进入倒数，北京试图介入台湾选举的相关活动再受关注。台湾《反渗透法》施行后，尽管近年相关案件数量快速增加，但查办近600人，只有5人被定罪，使现行法律规范与执法标准受到外界检视。" data-title="里长赴中旅游：台湾《反渗透法》为何“查办多、定罪少”？" data-date="11-16 17:03" data-source="BBC">
          <span class="news-cat-tag cat-meimei">🌍 外媒视角</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-16 17:03</span>
          <span class="news-item-title">里长赴中旅游：台湾《反渗透法》为何“查办多、定罪少”？</span>
          <span class="news-value-point">💡 台湾“九合一”地方选举进入倒数，北京试图介入台湾选举的相关活动再受关注</span>
        </a>
  </div>
</div>
<script defer src="{{ "/assets/js/news-feed.js" | relative_url }}"></script>


<p class="news-updated">🕐 抓取更新于 2026-11-17 06:23（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
