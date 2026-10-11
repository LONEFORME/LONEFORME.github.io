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
      <span>2026-10-11 22:17 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×14 · IT之家×13</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.nytimes.com/2026/10/11/world/middleeast/saudi-arabia-options-houthis.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="伊朗支持的胡塞武装在也门对沙特首都机场的三次致命袭击凸显了他们与沙特王国冲突的不对称性。" data-title="Saudi Arabia Has Few Options as Houthis Aim at Heart of Its Ambitions" data-date="10-11 21:23" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 10-11 21:23</span>
      </div>
      <h2 class="hero-featured-title">沙特阿拉伯几乎没有选择，因为胡塞武装瞄准其野心的核心</h2>
      <div class="hero-featured-title-en">Saudi Arabia Has Few Options as Houthis Aim at Heart of Its Ambitions</div>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://techcrunch.com/2026/10/11/these-execs-think-voice-ai-hasnt-reached-its-chatgpt-moment-yet/" target="_blank" rel="noopener" data-cat="keji" data-summary="语音人工智能经常错过上下文层的重要点，并导致整个管道中断" data-title="These execs think voice AI hasn’t reached its ChatGPT moment yet" data-date="10-11 22:00" data-source="TechCrunch">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
      </div>
      <p class="hero-sub-title">These execs think voice AI hasn’t reached its ChatGPT moment yet</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/2026/sep/10/premier-league-top-scorers-2026-27-race-for-golden-boot" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="找出哪位英国顶尖射手正在向进球排行榜射击。继续阅读……" data-title="Premier League top scorers 2026-27: who is leading race for the golden boot?" data-date="10-11 21:53" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Premier League top scorers 2026-27: who is leading race for the golden boot?</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/011/706.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 11 日消息，2026 世界超级摩托车锦标赛（WSBK）第十一站 WorldSSP 组别第二回合在葡萄牙的埃斯托里尔举行。中国摩托车制造商“张雪机车”旗下车手瓦伦丁 · 德比斯拿下季军，队友费德里科 · 卡里卡苏洛赢得第十二名。本轮比赛中， 川崎世界超级运动车队车手杰里米 · 阿尔科巴（Jeremy Alcoba Ferrer）夺得第一名，这是他本赛季的第三次冠军。第二名则是 VFT Racing 的菲利普 · 法里奥利（Filippo Farioli）。IT之家注意到，德比斯在本场比赛重启后一度落至第 10 位，最后三圈终于迎头赶上，他拼尽全力追至季军位置，凭借经验和策略再度站上领奖台。" data-title="2026 WSBK 葡萄牙站第二回合：张雪机车德比斯第三名" data-date="10-11 22:12" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">2026 WSBK 葡萄牙站第二回合：张雪机车德比斯第三名</p>
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
        <a class="news-item" href="https://www.nytimes.com/2026/10/11/world/middleeast/saudi-arabia-options-houthis.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="伊朗支持的胡塞武装在也门对沙特首都机场的三次致命袭击凸显了他们与沙特王国冲突的不对称性。" data-title="Saudi Arabia Has Few Options as Houthis Aim at Heart of Its Ambitions" data-date="10-11 21:23" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-11 21:23</span>
          <span class="news-item-title">沙特阿拉伯几乎没有选择，因为胡塞武装瞄准其野心的核心</span>
          <span class="news-item-title-en">Saudi Arabia Has Few Options as Houthis Aim at Heart of Its Ambitions</span>
          <span class="news-value-point">💡 伊朗支持的胡塞武装在也门对沙特首都机场的三次致命袭击凸显了他们与沙特王国冲突的不对称性</span>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-11/10711117.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="2026年是中国工农红军长征胜利90周年。肯尼亚“首都调频”网站10月10日刊文称，今天的中国拥有现代化的城市和规模庞大的消费市场，但人们很容易忽略，走到这一步的道路有多么漫长和艰难。这正是长征精神的意义所在，这种精神是“值得非洲探讨的国家发展理念”。" data-title="全球媒体聚焦 | “长征是值得非洲探讨的国家发展理念”" data-date="10-11 20:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-11 20:41</span>
          <span class="news-item-title">全球媒体聚焦 | “长征是值得非洲探讨的国家发展理念”</span>
          <span class="news-value-point">💡 2026年是中国工农红军长征胜利90周年</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-11/10711087.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网西安10月11日电 (记者 孙自法)记者10月11日从中国科学院地球环境研究所(地环所)获悉，“一带一路”地区极端气候事件及影响国际培训班当天在陕西西安开班，以“极端气候事件重建、预警与影响评估”为核心主题，对来自10多个国家的20余名优秀学员，开展为期14天的培训。" data-title="“一带一路”地区极端气候事件及影响国际培训班在西安开班" data-date="10-11 19:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-11 19:55</span>
          <span class="news-item-title">“一带一路”地区极端气候事件及影响国际培训班在西安开班</span>
          <span class="news-value-point">💡 中新网西安10月11日电 (记者 孙自法)记者10月11日从中国科学院地球环境研究所(地环所)获悉，“一带一路”地区极端气候事件及影响国际培训班…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-11/10711086.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网广州10月11日电 (记者 程景伟)为纪念中国工农红军长征胜利90周年，广东推出形式多样、内容丰富的展览展示、展演展映，并举办系列群众活动，团结动员广大南粤儿女弘扬伟大长征精神，走好新时代的长征路，为奋力推进中国式现代化的广东实践凝心聚力。" data-title="广东围绕纪念中国工农红军长征胜利90周年开展系列活动" data-date="10-11 19:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-11 19:54</span>
          <span class="news-item-title">广东围绕纪念中国工农红军长征胜利90周年开展系列活动</span>
          <span class="news-value-point">💡 中新网广州10月11日电 (记者 程景伟)为纪念中国工农红军长征胜利90周年，广东推出形式多样、内容丰富的展览展示、展演展映，并举办系列群众活动…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-11/10711084.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网香港10月11日电 (记者 邱兆翔)今年是孙中山先生诞辰160周年。香港黄埔军校后代亲友联谊会11日在香港举行系列活动，以“孙中山先生与中华民族复兴”为主题，多位革命先烈的后代走访中山纪念公园、孙中山史迹径等地，纪念孙中山先生诞辰160周年。" data-title="香港黄埔军校后代亲友联谊会在港举行系列活动 传承弘扬中山精神" data-date="10-11 19:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-11 19:53</span>
          <span class="news-item-title">香港黄埔军校后代亲友联谊会在港举行系列活动 传承弘扬中山精神</span>
          <span class="news-value-point">💡 中新网香港10月11日电 (记者 邱兆翔)今年是孙中山先生诞辰160周年</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-11/10711074.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月11日电 据法新社等媒体报道，当地时间10月11日，国际移民组织表示，10月8日至9日夜间，一艘移民船在吉布提海岸附近沉没，造成至少109人死亡，其中包括15名儿童，另有约116人失踪。" data-title="一移民船在吉布提沿海倾覆致至少109人死亡，包括15名儿童" data-date="10-11 19:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-11 19:05</span>
          <span class="news-item-title">一移民船在吉布提沿海倾覆致至少109人死亡，包括15名儿童</span>
          <span class="news-value-point">💡 中新网10月11日电 据法新社等媒体报道，当地时间10月11日，国际移民组织表示，10月8日至9日夜间，一艘移民船在吉布提海岸附近沉没，造成至少…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-11/10711045.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网约翰内斯堡10月11日电 “治国理政读书会：中国实践与中非合作”近日在南非行政首都比勒陀利亚举行。南非政、学、媒体人士发言，来自南非部分高校学生、教授以及各界人士共计240余人参加了读书会。" data-title="“治国理政读书会：中国实践与中非合作”在南非比陀举行" data-date="10-11 18:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-11 18:17</span>
          <span class="news-item-title">“治国理政读书会：中国实践与中非合作”在南非比陀举行</span>
          <span class="news-value-point">💡 中新网约翰内斯堡10月11日电 “治国理政读书会：中国实践与中非合作”近日在南非行政首都比勒陀利亚举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-11/10711026.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="10月6日，日本共同社援引日本政府多名相关人士的话披露：在年内修订的《国家安全保障战略》等“安保三文件”中，日本政府考虑写入“探讨引进核动力潜艇”的相关内容，不承诺“拥有”，但白纸黑字写进“研究”。从战后被摁了半个世纪的禁忌，到即将摆上国家安保文件的桌面，日本这一步，等了多久？又想走多远？一起来看专家分析。" data-title="“核” “潜” “艇”，三个词写尽日本步步为营的危险试探" data-date="10-11 17:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-11 17:02</span>
          <span class="news-item-title">“核” “潜” “艇”，三个词写尽日本步步为营的危险试探</span>
          <span class="news-value-point">💡 10月6日，日本共同社援引日本政府多名相关人士的话披露：在年内修订的《国家安全保障战略》等“安保三文件”中，日本政府考虑写入“探讨引进核动力潜艇…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-11/10711025.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="日本多个民间团体10日在东京举行全国联合交流集会，围绕长射程导弹部署、弹药库建设、军事基地扩建等问题展开交流，表达反对日本政府军事扩张、维护地区和平与民众安全的诉求。" data-title="日本民间团体举行集会 反对政府军事扩张" data-date="10-11 17:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-11 17:02</span>
          <span class="news-item-title">日本民间团体举行集会 反对政府军事扩张</span>
          <span class="news-value-point">💡 日本多个民间团体10日在东京举行全国联合交流集会，围绕长射程导弹部署、弹药库建设、军事基地扩建等问题展开交流，表达反对日本政府军事扩张、维护地区…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/11/us/politics/white-house-manufactured-narrative-solomon.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="从机密文件查询中发布选定的记录是一个案例研究，说明省略上下文如何创造政治弹药。" data-title="How the White House Manufactured a Narrative About a Trump Aide’s Call Logs" data-date="10-11 17:01" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-11 17:01</span>
          <span class="news-item-title">白宫如何制作关于特朗普助手通话记录的叙述</span>
          <span class="news-item-title-en">How the White House Manufactured a Narrative About a Trump Aide’s Call Logs</span>
          <span class="news-value-point">💡 从机密文件查询中发布选定的记录是一个案例研究，说明省略上下文如何创造政治弹药</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/11/us/arizona-alma-hernandez-threats-violence.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="威胁改变了国家众议员阿尔玛·埃尔南德斯（ Alma Hernandez ）及其家人、朋友和邻居的生活。他们甚至改变了她的政策制定。" data-title="After Many Threats, an Arizona Lawmaker Asks: ‘Is It Really Worth It?’" data-date="10-11 17:00" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-11 17:00</span>
          <span class="news-item-title">在经历了多次威胁之后，一位亚利桑那州议员问道： “这真的值得吗？”</span>
          <span class="news-item-title-en">After Many Threats, an Arizona Lawmaker Asks: ‘Is It Really Worth It?’</span>
          <span class="news-value-point">💡 威胁改变了国家众议员阿尔玛·埃尔南德斯（ Alma Hernandez ）及其家人、朋友和邻居的生活</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-11/10710999.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社广州10月11日电 (记者 王坚)为期两天的第十一届海峡两岸暨港澳地区高校现代书院制教育论坛11日在香港科技大学(广州)落幕。该论坛是中国现代书院教育领域极具影响力的高层次交流协作平台。" data-title="海峡两岸暨港澳地区高校现代书院制教育论坛在广州举行" data-date="10-11 15:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-11 15:42</span>
          <span class="news-item-title">海峡两岸暨港澳地区高校现代书院制教育论坛在广州举行</span>
          <span class="news-value-point">💡 中新社广州10月11日电 (记者 王坚)为期两天的第十一届海峡两岸暨港澳地区高校现代书院制教育论坛11日在香港科技大学(广州)落幕</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://techcrunch.com/2026/10/11/these-execs-think-voice-ai-hasnt-reached-its-chatgpt-moment-yet/" target="_blank" rel="noopener" data-cat="keji" data-summary="语音人工智能经常错过上下文层的重要点，并导致整个管道中断" data-title="These execs think voice AI hasn’t reached its ChatGPT moment yet" data-date="10-11 22:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-11 22:00</span>
          <span class="news-item-title">这些高管认为语音AI尚未达到ChatGPT时刻</span>
          <span class="news-item-title-en">These execs think voice AI hasn’t reached its ChatGPT moment yet</span>
          <span class="news-value-point">💡 语音人工智能经常错过上下文层的重要点，并导致整个管道中断</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/700.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 11 日消息，据科技媒体 Phoronix 今天报道，微软为即将发布的 Linux 7.4 贡献全新内核驱动。目前该驱动已进入 IOMMU 子系统的 -next 分支，可在 Hyper-V 的 Linux 客户机虚拟机使用。据介绍，这款半虚拟化 IOMMU 驱动可通过 HYPERV_PVIOMMU Kconfig 配置选项启用。可让 Hyper-V 上的 Linux 客户机为分配给虚拟机的设备，提供内核级 DMA 保护。IT之家从原报道获悉，该驱动同时适用于 Intel VT-d 和 AMD IOMMU 系统。如果进展顺利，Linux 7.4 正式版预计将在 12 月底发布。" data-title="微软为 Linux 7.4 贡献 Hyper-V 半虚拟化 IOMMU 驱动，已进入-next 分支" data-date="10-11 21:32" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-11 21:32</span>
          <span class="news-item-title">微软为 Linux 7.4 贡献 Hyper-V 半虚拟化 IOMMU 驱动，已进入-next 分支</span>
          <span class="news-value-point">💡 IT之家 10 月 11 日消息，据科技媒体 Phoronix 今天报道，微软为即将发布的 Linux 7.4 贡献全新内核驱动</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/cyber-security/cryptomining-malware-used-poetry-to-infect-more-than-3-400-servers-researchers-say-four-words-in-the-poellm-verse-changed-11-times-point-the-botnet-to-new-servers" target="_blank" rel="noopener" data-cat="keji" data-summary="Lumen的Black Lotus Labs表示， PoeLLM恶意软件已经攻击了3,400多台服务器，其中大多数都暴露了LiteLLM和Ollama等人工智能工具。" data-title="Cryptomining malware used poetry to infect more than 3,400 servers, researchers say" data-date="10-11 19:45" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-11 19:45</span>
          <span class="news-item-title">研究人员表示，加密恶意软件使用POETRY感染了3,400多台服务器</span>
          <span class="news-item-title-en">Cryptomining malware used poetry to infect more than 3,400 servers, researchers say</span>
          <span class="news-value-point">💡 Lumen的Black Lotus Labs表示， PoeLLM恶意软件已经攻击了3,400多台服务器，其中大多数都暴露了LiteLLM和Oll…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1008484/learning-local-ai-hermes-qwen-model-mac-studio-testing-diary-progress" target="_blank" rel="noopener" data-cat="keji" data-summary="我正在踏上一段迄今为止一直犹豫不决的旅程：实际上是定期使用人工智能。将大多数个人数据提供给云服务对我来说是一个主要障碍，但越来越有可能在本地运行强大的模型，以了解" data-title="Learning to use local AI is exciting, overwhelming, and frustrating" data-date="10-11 19:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-11 19:00</span>
          <span class="news-item-title">学习使用本地人工智能是令人兴奋、不知所措和令人沮丧的</span>
          <span class="news-item-title-en">Learning to use local AI is exciting, overwhelming, and frustrating</span>
          <span class="news-value-point">💡 我正在踏上一段迄今为止一直犹豫不决的旅程：实际上是定期使用人工智能</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/618.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 11 日消息，红魔游戏手机官方今日继续预热 12 系列新机。据介绍，红魔 12 Pro+ 搭载 1115E 立体对称式扬声器，将支持杜比全景声，号称迄今为止音效最好的红魔旗舰。红魔 12 Pro+ 号称“迄今为止手感最好的红魔旗舰”，主打“更轻、更薄、更窄、更圆润”。预热图显示，新机相比前代厚度更薄、重量更轻，同时屏幕黑边、边框圆角都有优化，其中 12 Pro+ 的屏幕黑边由前代的 1.25mm 减小到了 0.96mm。此外，红魔 12 Pro+ 手机将搭载高通第六代骁龙 8 超级至尊版芯片。根据官方预热，红魔 12 Pro+ 还将搭载行业首款 RGB 水冷散热技术，支持自定义 RGB 灯效；采用全新双环流道设计，水冷面积覆盖风道、芯片、电池等核心部件；采用 AI 服务器" data-title="红魔 12 Pro+ 手机官宣支持杜比全景声，号称迄今为止音效最好的红魔旗舰" data-date="10-11 15:41" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-11 15:41</span>
          <span class="news-item-title">红魔 12 Pro+ 手机官宣支持杜比全景声，号称迄今为止音效最好的红魔旗舰</span>
          <span class="news-value-point">💡 IT之家 10 月 11 日消息，红魔游戏手机官方今日继续预热 12 系列新机</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/617.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 11 日消息，努比亚今日宣布 NaviX Ultra“内测实验室”计划即将开启，面向尝鲜用户开放内测资格，抢先体验最新版本能力。10 月 14 日 19:00，首场进化直播。IT之家注意到，“第二代豆包手机”努比亚 NaviX Ultra 于 9 月 16 日发布，号称“全球首款 AI 智能体手机”，由中兴通讯努比亚全链路主导打造，实现一句话让 AI 跨应用执行复杂任务，豆包手机助手主导 AI 助手体验，售价 5999 元起。努比亚 NaviX Ultra 搭载行业首个集成指纹识别的独立 AI 按键，支持方言识别能力、语音唤醒能力，并内置 Seed 最新全双工语音大模型，按键位置也进行了优化，更方便操作。硬件配置上，努比亚 NaviX Ultra 搭载第五代骁龙 8 至尊" data-title="“第二代豆包手机”努比亚 NaviX Ultra“内测实验室”计划即将开启，10 月 14 日直播" data-date="10-11 15:39" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-11 15:39</span>
          <span class="news-item-title">“第二代豆包手机”努比亚 NaviX Ultra“内测实验室”计划即将开启，10 月 14 日直播</span>
          <span class="news-value-point">💡 IT之家 10 月 11 日消息，努比亚今日宣布 NaviX Ultra“内测实验室”计划即将开启，面向尝鲜用户开放内测资格，抢先体验最新版本能…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/616.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 11 日消息，xAI 首席执行官埃隆 · 马斯克今日发文称：“买东西时，你只需要拍一张信用卡照片发到聊天框，Grok Bot 就会在网上搜索最佳优惠然后下单。”IT之家注意到，OpenAI Codex&amp;ChatGPT 团队负责人蒂博 · 索蒂奥回应道：“那我干脆直接把卡放这儿得了。”并附上一张 AI 生成的虚构信用卡照片，持卡人名字就是他本人“Thibault Sottiaux”，暗示该功能的安全风险性。另外一名用户表示，亚马逊如今已经屏蔽 Grok Bot 访问。马斯克回复道，Grok 自己会找别的方式买东西，他刚刚买了乐高，Grok 是直接从乐高官网下单的。" data-title="马斯克称给信用卡拍照就能用 Grok Bot 购物，OpenAI 蒂博调侃“不如直接把卡发网上”" data-date="10-11 15:39" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-11 15:39</span>
          <span class="news-item-title">马斯克称给信用卡拍照就能用 Grok Bot 购物，OpenAI 蒂博调侃“不如直接把卡发网上”</span>
          <span class="news-value-point">💡 IT之家 10 月 11 日消息，xAI 首席执行官埃隆 · 马斯克今日发文称：“买东西时，你只需要拍一张信用卡照片发到聊天框，Grok Bot…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/613.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 11 日消息，据彭博社报道，埃隆 · 马斯克（Elon Musk）表示，鉴于其旗下公司在制造定制设备方面的专长，他相信自己的公司很可能会“找到比任何人都更好地制造芯片的方法”。在得克萨斯州奥斯汀的特斯拉超级工厂外，马斯克向到场的客户与投资人坦言，尽管自己目前“不知道如何制造微芯片，但我们（一定）会弄清楚”。在周六通过线上直播参与 X Takeover 活动时，他特别提到，此前在参观竞争对手的设施时，并没有看到多少定制化设备；而他的企业在制造这些设备方面拥有丰富经验，这使他们能够改进制造流程。“我认为可以说，这（指芯片制造）是世界上最难做的事情之一”马斯克表示，“我绝非盲目自大或自命不凡，但我认为我们很可能会找到比任何人都更好地制造芯片的方法。坦白讲，我不确定这需要多久，可" data-title="马斯克称尽管自己目前不知道如何制造微芯片，但一定会弄清楚" data-date="10-11 15:36" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-11 15:36</span>
          <span class="news-item-title">马斯克称尽管自己目前不知道如何制造微芯片，但一定会弄清楚</span>
          <span class="news-value-point">💡 IT之家 10 月 11 日消息，据彭博社报道，埃隆 · 马斯克（Elon Musk）表示，鉴于其旗下公司在制造定制设备方面的专长，他相信自己的…</span>
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
        <a class="news-item" href="https://www.ithome.com/1/011/536.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 10 日消息，今日，据彭博社援引知情人士消息，半导体公司 Cirrus Logic Inc. 上个月向 Synaptics Inc. 提出了一项未经请求的收购要约，试图破坏后者此前已公布的、与安森美半导体的并购交易。知情人士表示，Synaptics 周四更新的股东委托文件中提及的“甲方”，正是 Cirrus Logic。知情人士补充，目前尚不清楚 Cirrus Logic 是否仍有意推进这笔收购。据悉，Cirrus Logic 的报价采用现金 + 股票形式，促使安森美在上周修改了与 Synaptics 的协议条款。安森美将交易结构从全股票改为全现金，每股报价调整至 123 美元。安森美在一份声明中称，此次调整源于第三方提出的“竞争性非邀约收购提案”，但当时并未披露竞购方身" data-title="阻击安森美，Cirrus Logic 抢购 Synaptics" data-date="10-10 23:41" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-10 23:41</span>
          <span class="news-item-title">阻击安森美，Cirrus Logic 抢购 Synaptics</span>
          <span class="news-value-point">💡 IT之家 10 月 10 日消息，今日，据彭博社援引知情人士消息，半导体公司 Cirrus Logic Inc. 上个月向 Synaptics …</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/softbank-seeks-usd100-billion-for-ai-refined-projects-from-middle-eastern-investors-fund-would-be-used-to-acquire-companies-and-improve-their-operations-using-artificial-intelligence-and-robotics" target="_blank" rel="noopener" data-cat="keji" data-summary="软银计划收购不使用人工智能或机器人的公司，然后应用新技术来改善其运营和估值。" data-title="SoftBank seeks $100 billion for AI-refined projects from Middle Eastern investors" data-date="10-10 23:40" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-10 23:40</span>
          <span class="news-item-title">软银向中东投资者寻求1000亿美元的人工智能精炼项目</span>
          <span class="news-item-title-en">SoftBank seeks $100 billion for AI-refined projects from Middle Eastern investors</span>
          <span class="news-value-point">💡 软银计划收购不使用人工智能或机器人的公司，然后应用新技术来改善其运营和估值</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/10/premier-league-top-scorers-2026-27-race-for-golden-boot" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="找出哪位英国顶尖射手正在向进球排行榜射击。继续阅读……" data-title="Premier League top scorers 2026-27: who is leading race for the golden boot?" data-date="10-11 21:53" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-11 21:53</span>
          <span class="news-item-title">2026-27赛季英超联赛最佳射手：谁是金靴赛的领跑者？</span>
          <span class="news-item-title-en">Premier League top scorers 2026-27: who is leading race for the golden boot?</span>
          <span class="news-value-point">💡 找出哪位英国顶尖射手正在向进球排行榜射击</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/11/liverpool-v-manchester-city-premier-league-live-score-updates" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="⚽ 英超联赛的最新消息来自英国夏令时下午4:30的开球⚽现场比分|桌面|最佳射手|您可以给我们发邮件四场比赛的国际比赛已经进行了压力测试。“球队的强度，它的运动能力，真的，我认为这是设计" data-title="Liverpool v Manchester City: Premier League" data-date="10-11 21:43" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-11 21:43</span>
          <span class="news-item-title">利物浦v曼城：英超联赛</span>
          <span class="news-item-title-en">Liverpool v Manchester City: Premier League</span>
          <span class="news-value-point">💡 ⚽ 英超联赛的最新消息来自英国夏令时下午4:30的开球⚽现场比分|桌面|最佳射手|您可以给我们发邮件四场比赛的国际比赛已经进行了压力测试</span>
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
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/10/manchester-united-tottenham-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联得分为6分，这是自1986年以来最差的开局，托特纳姆热刺少了3分，仍然被困在降级区：迈克尔·卡里克和罗伯托·德泽比的测试时间，他们必须以某种方式复兴他们的球队。" data-title="Solanke strikes late as 10-man Spurs salvage point at Manchester United" data-date="10-11 02:50" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-11 02:50</span>
          <span class="news-item-title">索兰克在曼联10人马刺队打捞点时罢工较晚</span>
          <span class="news-item-title-en">Solanke strikes late as 10-man Spurs salvage point at Manchester United</span>
          <span class="news-value-point">💡 曼联得分为6分，这是自1986年以来最差的开局，托特纳姆热刺少了3分，仍然被困在降级区：迈克尔·卡里克和罗伯托·德泽比的测试时间，他们必须以某种…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/10/ipswich-fulham-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿尔瓦罗·阿贝洛亚（ Álvaro Arbeloa ）对富勒姆（ Fulham ）在伊普斯维奇（ Ipswich ）将英超联赛的无胜开局延长至六场比赛的建议感到愤怒，他无法应对压力。这位前皇家马德里主教练距离" data-title="Ipswich stun Fulham with last-gasp comeback to increase heat on Arbeloa" data-date="10-11 02:29" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-11 02:29</span>
          <span class="news-item-title">伊普斯维奇眩晕富勒姆，最后一击卷土重来，增加阿尔贝洛亚的热量</span>
          <span class="news-item-title-en">Ipswich stun Fulham with last-gasp comeback to increase heat on Arbeloa</span>
          <span class="news-value-point">💡 阿尔瓦罗·阿贝洛亚（ Álvaro Arbeloa ）对富勒姆（ Fulham ）在伊普斯维奇（ Ipswich ）将英超联赛的无胜开局延长至六…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/articles/cw3dj5yx4ej2o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="乔丹·亨德森（ Jordan Henderson ）和莫伊塞斯·凯塞多（ Moises Caicedo ）的表现巩固了周六下午切尔西在主场对伯恩茅斯的5-1胜利。" data-title="The rock behind Chelsea&#39;s entertainers: Midfield duo key for Blues" data-date="10-11 02:09" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-11 02:09</span>
          <span class="news-item-title">切尔西艺人背后的摇滚：蓝调中场二人组关键</span>
          <span class="news-item-title-en">The rock behind Chelsea's entertainers: Midfield duo key for Blues</span>
          <span class="news-value-point">💡 乔丹·亨德森（ Jordan Henderson ）和莫伊塞斯·凯塞多（ Moises Caicedo ）的表现巩固了周六下午切尔西在主场对伯恩…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cq1j427zze5xo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育频道（ BBC Sport ）被评为9月份英超联赛本月最佳球员，关注布莱顿球星帕斯卡尔·格罗斯（ Pascal Gross ）本赛季以及过去9年在俱乐部的两段时间的影响。" data-title="Timely recognition or long overdue? How Gross is proving all" data-date="10-11 01:07" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-11 01:07</span>
          <span class="news-item-title">及时表彰还是长期逾期？ Gross如何证明所有</span>
          <span class="news-item-title-en">Timely recognition or long overdue? How Gross is proving all</span>
          <span class="news-value-point">💡 英国广播公司体育频道（ BBC Sport ）被评为9月份英超联赛本月最佳球员，关注布莱顿球星帕斯卡尔·格罗斯（ Pascal Gross ）本…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/10/chelsea-v-bournemouth-sunderland-v-brighton-and-more-football-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="切尔西、布莱顿和伊普斯维奇获得胜利，而维拉和布伦特福德获得平局狮子队昨晚在世界杯资格赛附加赛的第一回合以3比1击败希腊，我们自己的Suzy Wrack分析了表现： Rayo Valle" data-title="Chelsea 5-1 Bournemouth, Sunderland 0-2 Brighton, and more: football – as it happened" data-date="10-11 00:22" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-11 00:22</span>
          <span class="news-item-title">切尔西5-1伯恩茅斯，桑德兰0-2布莱顿和更多：足球–因为它发生了</span>
          <span class="news-item-title-en">Chelsea 5-1 Bournemouth, Sunderland 0-2 Brighton, and more: football – as it happened</span>
          <span class="news-value-point">💡 切尔西、布莱顿和伊普斯维奇获得胜利，而维拉和布伦特福德获得平局狮子队昨晚在世界杯资格赛附加赛的第一回合以3比1击败希腊，我们自己的Suzy Wr…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/10/chelsea-bournemouth-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="注意学习，孩子们。这一天开始时，科尔·帕尔默（ Cole Palmer ）出现在直播中，向青年观众解释了他最新的合同延期背后的想法。它以BlueCo时代偷窃期间加入切尔西的最年长的球员结束" data-title="Henderson and João Pedro lead Chelsea charge against Bournemouth" data-date="10-11 00:18" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-11 00:18</span>
          <span class="news-item-title">亨德森和若昂·佩德罗领导切尔西对伯恩茅斯的指控</span>
          <span class="news-item-title-en">Henderson and João Pedro lead Chelsea charge against Bournemouth</span>
          <span class="news-value-point">💡 注意学习，孩子们</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/10/aston-villa-brentford-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="克里斯托弗·阿杰尔（ Kristoffer Ajer ）花了大量的时间来回答有关挪威队友埃尔林·哈兰德（ Erling Haaland ）心态的问题，也许最近几周他也学到了一些最后的技巧。约翰·麦金（ John McGinn ）的鞋子两分钟后" data-title="Aston Villa’s wait for home win goes on after Ajer hits back for Brentford" data-date="10-11 00:09" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-11 00:09</span>
          <span class="news-item-title">阿斯顿维拉在Ajer回击布伦特福德后继续等待主场胜利</span>
          <span class="news-item-title-en">Aston Villa’s wait for home win goes on after Ajer hits back for Brentford</span>
          <span class="news-value-point">💡 克里斯托弗·阿杰尔（ Kristoffer Ajer ）花了大量的时间来回答有关挪威队友埃尔林·哈兰德（ Erling Haaland ）心态的…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/011/706.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 11 日消息，2026 世界超级摩托车锦标赛（WSBK）第十一站 WorldSSP 组别第二回合在葡萄牙的埃斯托里尔举行。中国摩托车制造商“张雪机车”旗下车手瓦伦丁 · 德比斯拿下季军，队友费德里科 · 卡里卡苏洛赢得第十二名。本轮比赛中， 川崎世界超级运动车队车手杰里米 · 阿尔科巴（Jeremy Alcoba Ferrer）夺得第一名，这是他本赛季的第三次冠军。第二名则是 VFT Racing 的菲利普 · 法里奥利（Filippo Farioli）。IT之家注意到，德比斯在本场比赛重启后一度落至第 10 位，最后三圈终于迎头赶上，他拼尽全力追至季军位置，凭借经验和策略再度站上领奖台。" data-title="2026 WSBK 葡萄牙站第二回合：张雪机车德比斯第三名" data-date="10-11 22:12" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-11 22:12</span>
          <span class="news-item-title">2026 WSBK 葡萄牙站第二回合：张雪机车德比斯第三名</span>
          <span class="news-value-point">💡 IT之家 10 月 11 日消息，2026 世界超级摩托车锦标赛（WSBK）第十一站 WorldSSP 组别第二回合在葡萄牙的埃斯托里尔举行</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/705.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 11 日消息，街电现已在京东上架一款 55W 挂包充电宝，该机采用 2C 设计，内置 10000mAh 电芯，定价为 298 元，首发价 273 元，同时号称还赠送给消费者“一年共享充电宝免费使用权益”。京东街电 55W 挂包充电宝券后 273 元领 25 元券该产品尺寸为 52x38.5x84mm，重量 235g，提供暖金黄、茉莉白、樱花粉、晨雾蓝四种配色，顶部配备可开合挂环，可直接悬挂在背包、挎包等随身物品上，兼顾便携性与外观设计。机身配备 70cm USB-C 55W 伸缩线与独立 USB-C 55W 接口，支持 UFCS、PD、PPS、QC 等充电协议。此外，该产品搭载全周期智能安全监测系统，通过 USB 数据线连接电脑后，可在街电智慧充电监控平台网页端查询电池健" data-title="街电推出 55W 挂包充电宝：2C 设计、10000mAh 电芯，273 元赠“一年共享移动电源免费使用权益”" data-date="10-11 22:03" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-11 22:03</span>
          <span class="news-item-title">街电推出 55W 挂包充电宝：2C 设计、10000mAh 电芯，273 元赠“一年共享移动电源免费使用权益”</span>
          <span class="news-value-point">💡 IT之家 10 月 11 日消息，街电现已在京东上架一款 55W 挂包充电宝，该机采用 2C 设计，内置 10000mAh 电芯，定价为 298…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/704.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="小米首款 NAS 产品“Xiaomi 智能存储”今年 8 月 27 日开售，官方定价如下：4T 定价 2699 元，今日国补后 2384 元：京东小米 智能存储 4TB 国补后 2384.1 元领 250 元券8T 定价 3499 元，今日超级补贴价 3194 元：京东小米 智能存储 8TB 超级秒杀 3194 元领 196 元券16T 定价 5499 元，今日国补后 5084 元：京东小米 智能存储 16TB 国补后 5084.1 元领 250 元券官方 3 年质保，今日京东加赠 1 年延保 + 5 年数据恢复服务。据IT之家了解，小米智能存储采用双盘位设计，最大支持 60TB（30TBx2），适配 3.5/2.5 英寸个人硬盘，支持双盘模式下的动态备份 / 双备份功能，提供 1 个 US" data-title="上市 1 月京东直降：小米 NAS 智能存储 2699 → 2384 元 4 年质保" data-date="10-11 21:58" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-11 21:58</span>
          <span class="news-item-title">上市 1 月京东直降：小米 NAS 智能存储 2699 → 2384 元 4 年质保</span>
          <span class="news-value-point">💡 小米首款 NAS 产品“Xiaomi 智能存储”今年 8 月 27 日开售，官方定价如下：4T 定价 2699 元，今日国补后 2384 元：京…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/11/us/politics/elections-political-violence-harassment.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="《泰晤士报》的一项调查发现，暴力威胁已成为公职人员的新常态，重塑了私人生活，造成数百万美元的安全损失，并将人们赶下台。" data-title="Threats of Political Violence Have America’s Elected Officials Living in Fear" data-date="10-11 21:55" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-11 21:55</span>
          <span class="news-item-title">政治暴力的威胁让美国民选官员生活在恐惧之中</span>
          <span class="news-item-title-en">Threats of Political Violence Have America’s Elected Officials Living in Fear</span>
          <span class="news-value-point">💡 《泰晤士报》的一项调查发现，暴力威胁已成为公职人员的新常态，重塑了私人生活，造成数百万美元的安全损失，并将人们赶下台</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/703.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 11 日消息，据充电头网报道，美团旗下共享充电宝新国标版本近期已开始进入线下投放阶段，相应产品延续标志性黄色外观，侧面设有四颗电量指示灯，机身印有“22.5W 超级快充”字样，并标注 CCC 认证标识及 GB 47372-2026《移动电源安全技术规范》执行标准。▲ 图源充电头网具体规格方面，IT之家获悉相应产品型号为 MT-E-8BDY1，内置 7500mAh 电芯，额定能量 27.75Wh，最高支持 22.5W 快充输出。机身配备 USB-C、Lightning 双自带线，兼容不同接口手机。新国标将于 2027 年 4 月 1 日正式实施，对电芯安全、循环老化、异常记录和产品追溯等提出更高要求。随着新版本逐步投放，共享充电宝的安全升级也将进一步深入日常消费场景。" data-title="消息称美团共享充电宝开始投放新国标 3C 认证版本：配 7500mAh 电芯、自带双线支持 22.5W 输出" data-date="10-11 21:53" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-11 21:53</span>
          <span class="news-item-title">消息称美团共享充电宝开始投放新国标 3C 认证版本：配 7500mAh 电芯、自带双线支持 22.5W 输出</span>
          <span class="news-value-point">💡 IT之家 10 月 11 日消息，据充电头网报道，美团旗下共享充电宝新国标版本近期已开始进入线下投放阶段，相应产品延续标志性黄色外观，侧面设有四…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/702.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 11 日消息，闪极现已在京东上架一款 Vision Mag 磁吸充电宝，该产品支持 15W 无线充电和 20W 有线充电，内置 5000mAh 电芯，定价为 199 元。京东闪极 Vision Mag 磁吸充电宝 199 元直达链接该机整体重量 140g，尺寸为 102x72x11.7mm，采用银色金属机身，正面下方嵌有 TFT 彩屏模组（支持显示 iPhone 机型信息 / 充电功率），右下角配备编织挂绳，底部配备 USB-C 接口（支持 20W 输出/ 15W 输入，兼容 QC3+、FCP、SCP、AFC、PD3.0/PPS、DCP 以及 Apple 2.4A 等协议），背面无线充电模组可提供 15W 无线充电。该产品内置一块通过针刺测试的 5000mAh 的豪鹏电芯" data-title="闪极推出 Vision Mag 带屏磁吸充电宝：15W 无线充 + 20W 有线充，5000mAh 电芯售 199 元" data-date="10-11 21:48" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-11 21:48</span>
          <span class="news-item-title">闪极推出 Vision Mag 带屏磁吸充电宝：15W 无线充 + 20W 有线充，5000mAh 电芯售 199 元</span>
          <span class="news-value-point">💡 IT之家 10 月 11 日消息，闪极现已在京东上架一款 Vision Mag 磁吸充电宝，该产品支持 15W 无线充电和 20W 有线充电，内…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/701.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 11 日消息，阿维塔 T09 概念版今晚迎来全球首秀。新车作为阿维塔与华为干昆联合设计的首款高端旗舰车型，新车设计灵感源于 VISION XPECTRA，配备四激光雷达。外观方面，该车带入全新的阿维塔设计语言，晶钻阵列大灯搭配雕塑格栅。“绛红”与“棉白”营造出刻意为之的纵横分界，重塑色彩布局方式，全新的 D 柱发光徽标与整体架构融为一体，车尾则配备修长的一体式晶钻尾灯。该车采用全新内饰设计，互动屏幕向外拓展延伸至车门一体化布局，拓宽视觉边界的同时，让驾驶者可以用更好的视角看清信息。据IT之家此前报道，阿维塔 T09 已完成申报，提供两种动力版本，长宽高分别为 5285/2025/1810 或 1820mm，轴距 3150mm，前轮距 1726mm，后轮距 1740mm，额" data-title="阿维塔 T09 概念版全球首秀：定位全新旗舰 SUV，配备四激光雷达" data-date="10-11 21:35" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-11 21:35</span>
          <span class="news-item-title">阿维塔 T09 概念版全球首秀：定位全新旗舰 SUV，配备四激光雷达</span>
          <span class="news-value-point">💡 IT之家 10 月 11 日消息，阿维塔 T09 概念版今晚迎来全球首秀</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/699.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 11 日消息，Square Enix 旗下《王国之心》系列游戏现已在 Steam 平台开启永降，IT之家附游戏国区价格如下：《KINGDOM HEARTS -HD 1.5+2.5 ReMIX》原价格 298 元，新价格 198 元《王国之心 HD 1.5+2.5 ReMIX》是 Square Enix 推出的一部大规模高清重制合集，其核心目的是将系列早期的关键剧情整合到现代主机平台上。该合集包含了六部作品的内容：四款动作角色扮演游戏（《王国之心最终混合版》、《王国之心记忆之链重制版》、《王国之心 2 最终混合版》、《王国之心梦中降生最终混合版》），以及两部以高清 CG 影像呈现的剧情电影（《358/2 天》与《编码重制版》）。在游戏机制上，玩家主要扮演主角索拉，穿越各大迪" data-title="Square Enix《王国之心》系列游戏 Steam 价格永降：国区各作调整至 198 元" data-date="10-11 21:30" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-11 21:30</span>
          <span class="news-item-title">Square Enix《王国之心》系列游戏 Steam 价格永降：国区各作调整至 198 元</span>
          <span class="news-value-point">💡 IT之家 10 月 11 日消息，Square Enix 旗下《王国之心》系列游戏现已在 Steam 平台开启永降，IT之家附游戏国区价格如下：…</span>
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
        <a class="news-item" href="https://www.nytimes.com/2026/10/11/world/asia/india-cockroach-dipke-new-delhi-protests.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="印度青年运动Cockroach Janta Party的领导人周六被警方拘留，之后他们可以领导投票权抗议活动。" data-title="India’s ‘Cockroach’ Leaders Released as Small Protests Go On in Delhi" data-date="10-11 21:03" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-11 21:03</span>
          <span class="news-item-title">印度“蟑螂”领导人在德里举行小规模抗议活动后获释</span>
          <span class="news-item-title-en">India’s ‘Cockroach’ Leaders Released as Small Protests Go On in Delhi</span>
          <span class="news-value-point">💡 印度青年运动Cockroach Janta Party的领导人周六被警方拘留，之后他们可以领导投票权抗议活动</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-11/10711131.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网新疆新星10月11日电 (史玉江)新疆生产建设兵团第十三师新星市“戈壁奇石·丝路新星”奇石文化旅游活动10日启幕。活动汇聚全国200多家集市展商，玛瑙、泥石、戈壁石、火山岩、沉积岩等上百类奇石亮相，将开展为期10天的交易展示。" data-title="新疆新星市举办奇石文化旅游活动" data-date="10-11 21:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-11 21:01</span>
          <span class="news-item-title">新疆新星市举办奇石文化旅游活动</span>
          <span class="news-value-point">💡 中新网新疆新星10月11日电 (史玉江)新疆生产建设兵团第十三师新星市“戈壁奇石·丝路新星”奇石文化旅游活动10日启幕</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/entertainment/1008720/vurt-microdramas-verticals-interview-hilmon-sorey" target="_blank" rel="noopener" data-cat="zonghe" data-summary="从Disney Plus到HBO Max ，几乎所有主流流媒体服务都在尝试进入垂直内容的方法。很明显，这些公司将TikTok和Instagram等以视频为中心的社交媒体平台视为" data-title="Vurt wants you to look at vertical videos as a genre of their own" data-date="10-11 21:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-11 21:00</span>
          <span class="news-item-title">Vurt希望您将垂直视频视为自己的流派</span>
          <span class="news-item-title-en">Vurt wants you to look at vertical videos as a genre of their own</span>
          <span class="news-value-point">💡 从Disney Plus到HBO Max ，几乎所有主流流媒体服务都在尝试进入垂直内容的方法</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1009317/apple-what-to-expect-welcome-home" target="_blank" rel="noopener" data-cat="zonghe" data-summary="我们很快就要参加苹果的“欢迎回家”发布会，届时我们将发布一系列与智能家居相关的公告。我们期待Apple TV和HomePod Mini的更新，以及全新的智能家居中心。我们还可以看到首次亮相" data-title="What to expect from Apple’s ‘Welcome Home’ event" data-date="10-11 21:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-11 21:00</span>
          <span class="news-item-title">从Apple的“欢迎回家”活动中可以期待什么</span>
          <span class="news-item-title-en">What to expect from Apple’s ‘Welcome Home’ event</span>
          <span class="news-value-point">💡 我们很快就要参加苹果的“欢迎回家”发布会，届时我们将发布一系列与智能家居相关的公告</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-11/10711125.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网广州10月11日电 (记者 程景伟)全球航空业界约600名嘉宾代表11日下午走进广州永庆坊，在青砖镬耳墙之间交错穿行，感受岭南园林艺术之美；在粤剧艺术博物馆欣赏粤语歌曲及醒狮表演、品尝特色美食，体验广府人文风情。" data-title="全球数百名航空代表走进广州永庆坊 领略广府文化魅力" data-date="10-11 20:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-11 20:57</span>
          <span class="news-item-title">全球数百名航空代表走进广州永庆坊 领略广府文化魅力</span>
          <span class="news-value-point">💡 中新网广州10月11日电 (记者 程景伟)全球航空业界约600名嘉宾代表11日下午走进广州永庆坊，在青砖镬耳墙之间交错穿行，感受岭南园林艺术之美</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-11 22:17（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
