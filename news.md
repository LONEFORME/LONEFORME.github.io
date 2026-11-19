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
      <span>2026-11-20 00:42 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">4</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">天空体育×15 · 中国新闻网×12</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">按来源聚合 · 最近 24 小时精选</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.nytimes.com/video/world/asia/100000011287890/inside-a-rohingya-camp-after-a-genocide-ruling.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="周四，国际法院裁定，缅甸政府对罗兴亚族少数民族犯下的暴行构成种族灭绝。在裁决之前，《纽约时报》记者汉娜·比奇（Hannah Beech）在……度过了一周。" data-title="Inside a Rohingya Camp After a Genocide Ruling" data-date="11-20 00:10" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 11-20 00:10</span>
      </div>
      <h2 class="hero-featured-title">种族灭绝裁决后的罗兴亚难民营内部情况</h2>
      <div class="hero-featured-title-en">Inside a Rohingya Camp After a Genocide Ruling</div>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.nytimes.com/2026/11/19/business/anthropic-ipo-washington.html" target="_blank" rel="noopener" data-cat="keji" data-summary="随着技术的迅猛发展，华盛顿的政策制定者一直在努力为可能对工人、企业和经济其他部门造成的冲击做好准备。" data-title="Anthropic’s Trillion-Dollar Debut Is Watershed Moment for A.I.’s Risks and Rewards" data-date="11-20 00:39" data-source="纽约时报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
      </div>
      <p class="hero-sub-title">Anthropic的万亿美元首秀是人工智能风险与回报的分水岭时刻</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/2026/nov/19/premier-league-vote-new-rules-financial-indemnity-lawsuits" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="个人赔偿责任范围扩大至潜在诉讼 关键人物可能被列入针对曼城俱乐部的诉讼 在周四的一次关键投票中，各俱乐部团结在英超联赛领导层周围，以压倒性多数支持旨在保护英超联赛首席执行官的新规则。" data-title="Premier League clubs vote to increase legal protection for executives" data-date="11-20 00:03" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">英超俱乐部投票决定加强对高管的法律保护</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/tennis/live-blog/12040/13523297/jack-draper-tennis-results-next-match-news-ranking-video-and-how-to-watch-on-sky-sports-tennis" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Draper hires new coach to work alongside Murray for upcoming season" data-title="Draper hires new coach to work alongside Murray for upcoming season" data-date="11-20 00:30" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">德雷珀聘请新教练，与穆雷搭档备战新赛季</p>
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
        <a class="news-item" href="https://www.nytimes.com/video/world/asia/100000011287890/inside-a-rohingya-camp-after-a-genocide-ruling.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="周四，国际法院裁定，缅甸政府对罗兴亚族少数民族犯下的暴行构成种族灭绝。在裁决之前，《纽约时报》记者汉娜·比奇（Hannah Beech）在……度过了一周。" data-title="Inside a Rohingya Camp After a Genocide Ruling" data-date="11-20 00:10" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-20 00:10</span>
          <span class="news-item-title">种族灭绝裁决后的罗兴亚难民营内部情况</span>
          <span class="news-item-title-en">Inside a Rohingya Camp After a Genocide Ruling</span>
          <span class="news-value-point">💡 周四，国际法院裁定，缅甸政府对罗兴亚族少数民族犯下的暴行构成种族灭绝</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/19/world/asia/myanmar-rohingya-village-refugee-genocide.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="扎莫纳的被抹杀是针对罗兴亚穆斯林的大规模暴力运动的一部分。一家国际法院裁定，缅甸应对这些暴行负责。" data-title="A Village Burned, Its People Killed or Exiled. A Court Ruled It Was Genocide." data-date="11-19 23:40" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-19 23:40</span>
          <span class="news-item-title">一个村庄被烧毁，村民被杀害或驱逐。法院裁定这是一起种族灭绝事件。</span>
          <span class="news-item-title-en">A Village Burned, Its People Killed or Exiled. A Court Ruled It Was Genocide.</span>
          <span class="news-value-point">💡 扎莫纳的被抹杀是针对罗兴亚穆斯林的大规模暴力运动的一部分</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-19/10734979.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="(共321场)" data-title="中国担任2026年亚太经合组织东道主主办会议和活动清单" data-date="11-19 23:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-19 23:13</span>
          <span class="news-item-title">中国担任2026年亚太经合组织东道主主办会议和活动清单</span>
          <span class="news-value-point">💡 (共321场)</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-19/10734978.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="(共75项)" data-title="中国担任2026年亚太经合组织东道主成果清单" data-date="11-19 23:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-19 23:11</span>
          <span class="news-item-title">中国担任2026年亚太经合组织东道主成果清单</span>
          <span class="news-value-point">💡 (共75项)</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/podcast/1036484/jon-favreau-pod-save-america-offline-crooked-media-trump-big-tech-ai-2028-election" target="_blank" rel="noopener" data-cat="shizheng" data-summary="今天，我将与政治评论员兼 Crooked Media 联合创始人 Jon Favreau 对话。您可能最熟悉的是 Jon 主持的一档名为《Pod Save America》的小节目，这是 Jon 在唐纳德·特朗普当选总统后与一群奥巴马政府的同事一起创办的。" data-title="How Silicon Valley lost the public, with Crooked Media’s Jon Favreau" data-date="11-19 23:00" data-source="The Verge">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-19 23:00</span>
          <span class="news-item-title">硅谷是如何失去公众支持的，Crooked Media的Jon Favreau为您揭秘</span>
          <span class="news-item-title-en">How Silicon Valley lost the public, with Crooked Media’s Jon Favreau</span>
          <span class="news-value-point">💡 今天，我将与政治评论员兼 Crooked Media 联合创始人 Jon Favreau 对话</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-19/10734976.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="“四周一片漆黑，新加坡看起来就像一团火。许多船被击沉了，海面上都是残骸。”这是1942年新加坡沦陷后，来自乘船逃难者的口述。空袭、肃清、占领、酷刑……火光之下，映照出的是日本军国主义曾给地区人民带来的战争伤痛。" data-title="难忘二战记忆" data-date="11-19 22:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-19 22:56</span>
          <span class="news-item-title">难忘二战记忆</span>
          <span class="news-value-point">💡 “四周一片漆黑，新加坡看起来就像一团火</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-19/10734972.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社深圳11月19日电" data-title="亚太经合组织互联互通蓝图" data-date="11-19 22:51" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-19 22:51</span>
          <span class="news-item-title">亚太经合组织互联互通蓝图</span>
          <span class="news-value-point">💡 新华社深圳11月19日电</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-19/10734968.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月19日电 (记者 张杨彬 刘大炜)围绕中美元首19日深圳会晤涉台表述，多位学者当天接受中新社采访时指出，相关对话反映出双方建构中美建设性战略稳定关系的积极意愿，美方表态释放出对台政策更趋审慎的信号。" data-title="学者：中美建构建设性战略稳定关系 不支持“台独”表态具积极意义" data-date="11-19 22:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-19 22:50</span>
          <span class="news-item-title">学者：中美建构建设性战略稳定关系 不支持“台独”表态具积极意义</span>
          <span class="news-value-point">💡 中新社北京11月19日电 (记者 张杨彬 刘大炜)围绕中美元首19日深圳会晤涉台表述，多位学者当天接受中新社采访时指出，相关对话反映出双方建构中…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-19/10734952.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="11月19日，国家主席习近平在深圳同俄罗斯总统普京、美国总统特朗普举行中俄美元首会晤。三国元首围绕“维护世界和平，促进大国关系战略稳定”主题进行深入讨论。习近平指出——" data-title="【和合共生】习言道丨“修昔底德陷阱”绝不是宿命" data-date="11-19 22:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-19 22:24</span>
          <span class="news-item-title">【和合共生】习言道丨“修昔底德陷阱”绝不是宿命</span>
          <span class="news-value-point">💡 11月19日，国家主席习近平在深圳同俄罗斯总统普京、美国总统特朗普举行中俄美元首会晤</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-19/10734898.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月19日电 乌兰巴托消息：蒙古国国家大呼拉尔(议会)19日召开全体会议，表决批准呼日勒苏赫辞去总统职务。蒙古国国家大呼拉尔主席宾巴朝格特将代行总统职权。" data-title="蒙古国总统辞职申请获议会批准" data-date="11-19 20:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-19 20:57</span>
          <span class="news-item-title">蒙古国总统辞职申请获议会批准</span>
          <span class="news-value-point">💡 中新社北京11月19日电 乌兰巴托消息：蒙古国国家大呼拉尔(议会)19日召开全体会议，表决批准呼日勒苏赫辞去总统职务</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/19/world/asia/xi-putin-trump-meeting-china-russia.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="尽管这两位独裁者正试图扭转美国在冷战中的胜利，但特朗普总统仍与中俄两国领导人一同出席了在深圳举行的峰会。" data-title="Behind Trump Meeting, Xi and Putin Share a Vision of Usurping U.S. Power" data-date="11-19 20:41" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-19 20:41</span>
          <span class="news-item-title">特朗普会晤背后，习近平和普京有着篡夺美国权力的共同愿景</span>
          <span class="news-item-title-en">Behind Trump Meeting, Xi and Putin Share a Vision of Usurping U.S. Power</span>
          <span class="news-value-point">💡 尽管这两位独裁者正试图扭转美国在冷战中的胜利，但特朗普总统仍与中俄两国领导人一同出席了在深圳举行的峰会</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/19/world/asia/trump-summit-china-media-bloomberg-reporter-nvidia.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="这位记者在向特朗普总统大声提问后被请出场，这正是中国试图严密掌控活动的一个例子。" data-title="China Bars Bloomberg Reporter From Trilateral Talks for Asking a Question" data-date="11-19 20:08" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-19 20:08</span>
          <span class="news-item-title">中国因彭博社记者提问而禁止其参加三方会谈</span>
          <span class="news-item-title-en">China Bars Bloomberg Reporter From Trilateral Talks for Asking a Question</span>
          <span class="news-value-point">💡 这位记者在向特朗普总统大声提问后被请出场，这正是中国试图严密掌控活动的一个例子</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-19/10734843.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月19日电 伊斯兰堡消息：当地时间11月19日，巴基斯坦三军新闻局发表声明说，巴安全部队日前在该国西北部开伯尔－普什图省开展多次反恐行动，共打死22名恐怖分子。" data-title="巴基斯坦在反恐行动中打死22名恐怖分子" data-date="11-19 19:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-19 19:15</span>
          <span class="news-item-title">巴基斯坦在反恐行动中打死22名恐怖分子</span>
          <span class="news-value-point">💡 中新社北京11月19日电 伊斯兰堡消息：当地时间11月19日，巴基斯坦三军新闻局发表声明说，巴安全部队日前在该国西北部开伯尔－普什图省开展多次反…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-19/10734729.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月19日电(记者 孙自法)国际学术期刊《自然》北京时间11月19日凌晨在线发表一篇动物学论文称，布冈夜蛾(Bogong moths)利用一种地磁罗盘帮助它们进行季节性的迁徙，连同此前研究证明这些蛾子还会利用星光导航，表明此类昆虫使用地磁和星光两种内在罗盘来寻找方向。" data-title="夜蛾如何辨识方向？国际最新研究发现利用地磁和星光两种罗盘导航" data-date="11-19 17:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-19 17:44</span>
          <span class="news-item-title">夜蛾如何辨识方向？国际最新研究发现利用地磁和星光两种罗盘导航</span>
          <span class="news-value-point">💡 中新网北京11月19日电(记者 孙自法)国际学术期刊《自然》北京时间11月19日凌晨在线发表一篇动物学论文称，布冈夜蛾(Bogong moths…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-19/10734676.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月19日电 当地时间18日，牧师克里斯蒂安·埃马纽埃尔·萨农(Christian Emmanuel Sanon)因涉嫌刺杀海地总统若弗内尔·莫伊兹(Jovenel Moise)，被迈阿密法官裁定有罪，可能面临终身监禁。" data-title="涉嫌参与海地总统遇刺案 美国牧师或面临终身监禁" data-date="11-19 17:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-19 17:43</span>
          <span class="news-item-title">涉嫌参与海地总统遇刺案 美国牧师或面临终身监禁</span>
          <span class="news-value-point">💡 中新社北京11月19日电 当地时间18日，牧师克里斯蒂安·埃马纽埃尔·萨农(Christian Emmanuel Sanon)因涉嫌刺杀海地总统…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/11/19/business/anthropic-ipo-washington.html" target="_blank" rel="noopener" data-cat="keji" data-summary="随着技术的迅猛发展，华盛顿的政策制定者一直在努力为可能对工人、企业和经济其他部门造成的冲击做好准备。" data-title="Anthropic’s Trillion-Dollar Debut Is Watershed Moment for A.I.’s Risks and Rewards" data-date="11-20 00:39" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-20 00:39</span>
          <span class="news-item-title">Anthropic的万亿美元首秀是人工智能风险与回报的分水岭时刻</span>
          <span class="news-item-title-en">Anthropic’s Trillion-Dollar Debut Is Watershed Moment for A.I.’s Risks and Rewards</span>
          <span class="news-value-point">💡 随着技术的迅猛发展，华盛顿的政策制定者一直在努力为可能对工人、企业和经济其他部门造成的冲击做好准备</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/19/at-nasdaq-opening-bell-anthropic-ceo-recommits-to-pacing-ai-development/" target="_blank" rel="noopener" data-cat="keji" data-summary="在纳斯达克开盘钟声致辞中，Dario Amodei重申了Anthropic对稳步推进人工智能发展的承诺，不受商业或政治压力的影响。" data-title="At Nasdaq opening bell, Anthropic CEO recommits to pacing AI development" data-date="11-20 00:19" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-20 00:19</span>
          <span class="news-item-title">在纳斯达克开市钟声响起之际，Anthropic首席执行官再次承诺稳步推进人工智能发展</span>
          <span class="news-item-title-en">At Nasdaq opening bell, Anthropic CEO recommits to pacing AI development</span>
          <span class="news-value-point">💡 在纳斯达克开盘钟声致辞中，Dario Amodei重申了Anthropic对稳步推进人工智能发展的承诺，不受商业或政治压力的影响</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/029/708.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 19 日消息，北京时间今天（19 日）深夜，AI 初创企业 Anthropic 正式登陆美股，以 813 亿美元（IT之家注：现汇率约合 5,431.47 亿元人民币）的募资额创下 IPO 历史纪录。公司 CEO 达里奥 · 阿莫代伊在纳斯达克敲响开市钟。“今天的上市让公司的财务基础更加稳固，也让我们更加坚定了做正确事情的决心。”Anthropic 的发行价定为每股 83 美元（现汇率约合 554.5 元人民币），高于上周公布的预期区间，完全稀释后市值达到 1.5 万亿美元（现汇率约合 10.02 万亿元人民币）。彭博社和路透社报道称，预计正式开盘后，Anthropic 股价还将上涨约 20%，达到每股 100 美元（现汇率约合 668.1 元人民币）左右。当地时间 18" data-title="Anthropic 完成史上最大规模 IPO，上市估值达 1.5 万亿美元" data-date="11-19 23:50" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-19 23:50</span>
          <span class="news-item-title">Anthropic 完成史上最大规模 IPO，上市估值达 1.5 万亿美元</span>
          <span class="news-value-point">💡 IT之家 11 月 19 日消息，北京时间今天（19 日）深夜，AI 初创企业 Anthropic 正式登陆美股，以 813 亿美元（IT之家注…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/029/707.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 19 日消息，ChatGPT 今天宣布新增“实时听写”功能，用户对着麦克风说话时，语音就能同步转换成文字，不必等录音结束后再转写，让 ChatGPT 更快接收到语音指令。该功能将陆续向全球所有 ChatGPT 用户开放，覆盖网页版、桌面客户端及 iOS 和 Android 应用。使用时，用户只需点击音频波形，就能查看实时转写的文字，录音结束后还可以直接在输入框中编辑。OpenAI 还宣布，取消 ChatGPT 语音听写原有的 10 分钟时长限制，并进一步提高转写的可靠性。今年早些时候，ChatGPT 的双向语音对话模式曾迎来全面改版。OpenAI 去年还推出了用于转写语音笔记和会议内容的“录制模式”，不过仍处于测试阶段，仅面向 Plus、Enterprise、Edu、Bu" data-title="ChatGPT 新增“实时听写”功能：对着麦克风说话，语音能即时变文字" data-date="11-19 23:28" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-19 23:28</span>
          <span class="news-item-title">ChatGPT 新增“实时听写”功能：对着麦克风说话，语音能即时变文字</span>
          <span class="news-value-point">💡 IT之家 11 月 19 日消息，ChatGPT 今天宣布新增“实时听写”功能，用户对着麦克风说话时，语音就能同步转换成文字，不必等录音结束后再…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1037634/openai-chatgpt-live-dictation" target="_blank" rel="noopener" data-cat="keji" data-summary="现在，ChatGPT 可以更快地接收来自麦克风的语音提示，因为实时听写功能可以在您说话时进行转录，而不是等到您完成录音。该功能现已在全球范围内在网页版、桌面版应用的所有ChatGPT套餐中推出，" data-title="ChatGPT can transcribe as you speak now with Live Dictation" data-date="11-19 23:16" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-19 23:16</span>
          <span class="news-item-title">现在，ChatGPT 可以使用实时听写功能为您转录语音</span>
          <span class="news-item-title-en">ChatGPT can transcribe as you speak now with Live Dictation</span>
          <span class="news-value-point">💡 现在，ChatGPT 可以更快地接收来自麦克风的语音提示，因为实时听写功能可以在您说话时进行转录，而不是等到您完成录音</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/029/702.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 19 日消息，据蓝鲸新闻报道，在阿里巴巴今天（19 日）召开的 2027 财年第二季度业绩电话会上，阿里巴巴集团 CEO 吴泳铭表示，全球各个区域的算力政策出现了非常大的变化，将对阿里云的数据中心建设产生影响。吴泳铭透露，根据目前的初步评估，阿里此前制定的到 2032 年全球数据中心规模超过 20GW 的目标有可能下调，资本开支可能有一定程度降低。同时，阿里将在国产算力及相关供应链上投入更积极，推进整体计划。基于平头哥的算力供应链持续放量节奏，2027 年和 2028 年上半年将是阿里最大的一个持续投资阶段。吴泳铭另表示，对于长期的现金流规划非常有信心。据IT之家此前报道，吴泳铭表示，2027 年和 2028 年，将是中国算力最紧缺的两年。2027 年以后，阿里云的芯片供" data-title="吴泳铭：阿里“2032 年全球数据中心规模超 20GW”目标或下调" data-date="11-19 23:03" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-19 23:03</span>
          <span class="news-item-title">吴泳铭：阿里“2032 年全球数据中心规模超 20GW”目标或下调</span>
          <span class="news-value-point">💡 IT之家 11 月 19 日消息，据蓝鲸新闻报道，在阿里巴巴今天（19 日）召开的 2027 财年第二季度业绩电话会上，阿里巴巴集团 CEO 吴…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/cpus/intel-continues-layoffs-with-cuts-to-its-it-department-hundreds-of-employees-reportedly-affected-companys-workforce-reduced-by-27-800-under-lip-bu-tan" target="_blank" rel="noopener" data-cat="keji" data-summary="英特尔继续裁员，此次IT部门受到影响。" data-title="Intel continues layoffs with cuts to its IT department, hundreds of employees reportedly affected" data-date="11-19 22:58" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-19 22:58</span>
          <span class="news-item-title">英特尔继续裁员，削减IT部门，据报道数百名员工受到影响</span>
          <span class="news-item-title-en">Intel continues layoffs with cuts to its IT department, hundreds of employees reportedly affected</span>
          <span class="news-value-point">💡 英特尔继续裁员，此次IT部门受到影响</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/19/anthropics-ipo-puts-ais-circular-financing-boom-to-the-test/" target="_blank" rel="noopener" data-cat="keji" data-summary="Anthropic在上市之际面临着巨大的算力承诺，但即使Anthropic失去领先地位，其最大的基础设施合作伙伴（包括亚马逊和谷歌）仍可能继续从人工智能中获利。" data-title="Anthropic’s IPO puts AI’s circular financing boom to the test" data-date="11-19 22:54" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-19 22:54</span>
          <span class="news-item-title">Anthropic的IPO对人工智能的循环融资热潮提出了考验</span>
          <span class="news-item-title-en">Anthropic’s IPO puts AI’s circular financing boom to the test</span>
          <span class="news-value-point">💡 Anthropic在上市之际面临着巨大的算力承诺，但即使Anthropic失去领先地位，其最大的基础设施合作伙伴（包括亚马逊和谷歌）仍可能继续从…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1037459/anthropic-ipo-safe-ai-reputation-power-structure" target="_blank" rel="noopener" data-cat="keji" data-summary="今天是Anthropic的一个新起点：经过多年筹备的IPO超越了SpaceX，成为有史以来市值最高的新上市公司，募资额达813亿美元，为其他即将上市的人工智能实验室树立了重要先例。但这不仅仅是财务上的事情。" data-title="With the biggest IPO of all time, Anthropic’s ‘good guy’ reputation is on the line" data-date="11-19 22:25" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-19 22:25</span>
          <span class="news-item-title">随着有史以来规模最大的IPO即将到来，Anthropic的“好人”声誉岌岌可危</span>
          <span class="news-item-title-en">With the biggest IPO of all time, Anthropic’s ‘good guy’ reputation is on the line</span>
          <span class="news-value-point">💡 今天是Anthropic的一个新起点：经过多年筹备的IPO超越了SpaceX，成为有史以来市值最高的新上市公司，募资额达813亿美元，为其他即将…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/big-tech/supermicro-sued-by-shareholders-over-claims-nvidia-executives-wife-must-have-known-about-illicit-china-sales-former-chief-growth-officer-cenly-chen-is-married-to-outgoing-nvidia-vp-jay-puri" target="_blank" rel="noopener" data-cat="keji" data-summary="一项民事诉讼称，“Cenly Chen不可能不知道公司的非法销售行为。”" data-title="Supermicro sued by shareholders over claims Nvidia executive’s wife knew about illicit China sales" data-date="11-19 22:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-19 22:00</span>
          <span class="news-item-title">Supermicro因股东指控Nvidia高管妻子知悉非法对华销售而被起诉</span>
          <span class="news-item-title-en">Supermicro sued by shareholders over claims Nvidia executive’s wife knew about illicit China sales</span>
          <span class="news-value-point">💡 一项民事诉讼称，“Cenly Chen不可能不知道公司的非法销售行为</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/software/windows/developer-vibe-codes-windows-11-alternative-operating-system-for-amd64-arm64-and-riscv64-hardware-libernt-is-a-free-64-bit-clone-promising-reliable-stable-and-efficient-performance" target="_blank" rel="noopener" data-cat="keji" data-summary="一款名为LiberNT的新型氛围操作系统已然面世。" data-title="Developer vibe codes Windows 11 alternative operating system for amd64, arm64, and riscv64 hardware" data-date="11-19 21:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-19 21:30</span>
          <span class="news-item-title">开发者为 amd64、arm64 和 riscv64 硬件编写 Windows 11 替代操作系统的代码</span>
          <span class="news-item-title-en">Developer vibe codes Windows 11 alternative operating system for amd64, arm64, and riscv64 hardware</span>
          <span class="news-value-point">💡 一款名为LiberNT的新型氛围操作系统已然面世</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/19/business/anthropic-ipo-dustin-moskovitz.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Facebook联合创始人达斯汀·莫斯科维茨（Dustin Moskovitz）对Anthropic的早期投资正在获得回报。但这并没有让他感到高兴。" data-title="Dustin Moskovitz, an Early Anthropic Investor, Feels a Bit Uneasy About the IPO" data-date="11-19 21:28" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-19 21:28</span>
          <span class="news-item-title">Anthropic 的早期投资者达斯汀·莫斯科维茨（Dustin Moskovitz）对 IPO 感到有些不安</span>
          <span class="news-item-title-en">Dustin Moskovitz, an Early Anthropic Investor, Feels a Bit Uneasy About the IPO</span>
          <span class="news-value-point">💡 Facebook联合创始人达斯汀·莫斯科维茨（Dustin Moskovitz）对Anthropic的早期投资正在获得回报</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/intel-18a-yields-hit-70-percent-as-company-signs-microsoft-as-emib-customer-the-first-company-to-publicly-commit-to-intels-new-packaging-technology" target="_blank" rel="noopener" data-cat="keji" data-summary="英特尔的 18A 产出达到了一个重要的里程碑，该公司与微软签署了长期至强供应协议和 EMIB 使用协议。" data-title="Intel 18A yields hit 70% as company signs Microsoft as EMIB customer" data-date="11-19 21:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-19 21:00</span>
          <span class="news-item-title">英特尔18A工艺良率达到70%，并与微软签约成为EMIB客户</span>
          <span class="news-item-title-en">Intel 18A yields hit 70% as company signs Microsoft as EMIB customer</span>
          <span class="news-value-point">💡 英特尔的 18A 产出达到了一个重要的里程碑，该公司与微软签署了长期至强供应协议和 EMIB 使用协议</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/19/us/anthropic-ipo-spending-wealth-san-francisco.html" target="_blank" rel="noopener" data-cat="keji" data-summary="旧金山并没有为Anthropic的员工在公司首次公开募股后获得新财富后的购物狂潮做好准备。" data-title="Anthropic Employees Work Hard, but Don’t Expect Them to Play Hard" data-date="11-19 20:11" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-19 20:11</span>
          <span class="news-item-title">Anthropic 的员工工作很努力，但不要指望他们玩得很尽兴</span>
          <span class="news-item-title-en">Anthropic Employees Work Hard, but Don’t Expect Them to Play Hard</span>
          <span class="news-value-point">💡 旧金山并没有为Anthropic的员工在公司首次公开募股后获得新财富后的购物狂潮做好准备</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/cpus/intel-diamond-rapids-shows-signs-of-life-in-sc26-demo-running-live-server-next-gen-xeon-7-cpu-breaks-cover-at-partner-booths-no-showcase-from-intel" target="_blank" rel="noopener" data-cat="keji" data-summary="英特尔的下一代至强Diamond Rapids处理器在SC26的两个展位上亮相，其中一个展位展示了一台正在运行的服务器，但这两个展位都不是英特尔直接参展的。" data-title="Intel Diamond Rapids shows signs of life in SC26 demo running live server" data-date="11-19 19:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-19 19:30</span>
          <span class="news-item-title">英特尔 Diamond Rapids 在 SC26 演示中运行实时服务器，显示出活力迹象</span>
          <span class="news-item-title-en">Intel Diamond Rapids shows signs of life in SC26 demo running live server</span>
          <span class="news-value-point">💡 英特尔的下一代至强Diamond Rapids处理器在SC26的两个展位上亮相，其中一个展位展示了一台正在运行的服务器，但这两个展位都不是英特尔…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/19/premier-league-vote-new-rules-financial-indemnity-lawsuits" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="个人赔偿责任范围扩大至潜在诉讼 关键人物可能被列入针对曼城俱乐部的诉讼 在周四的一次关键投票中，各俱乐部团结在英超联赛领导层周围，以压倒性多数支持旨在保护英超联赛首席执行官的新规则。" data-title="Premier League clubs vote to increase legal protection for executives" data-date="11-20 00:03" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-20 00:03</span>
          <span class="news-item-title">英超俱乐部投票决定加强对高管的法律保护</span>
          <span class="news-item-title-en">Premier League clubs vote to increase legal protection for executives</span>
          <span class="news-value-point">💡 个人赔偿责任范围扩大至潜在诉讼
关键人物可能被列入针对曼城俱乐部的诉讼
在周四的一次关键投票中，各俱乐部团结在英超联赛领导层周围，以压倒性多数支…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/12040/13279286/bournemouth-transfers-latest-news-rumours-and-gossip-live-updates-goals-and-highlights" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Rose says Scott will start one of next three games - but not drawn on transfer links" data-title="Rose says Scott will start one of next three games - but not drawn on transfer links" data-date="11-19 23:55" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-19 23:55</span>
          <span class="news-item-title">罗斯表示，斯科特将在接下来的三场比赛中首发一场，但未提及转会传闻</span>
          <span class="news-item-title-en">Rose says Scott will start one of next three games - but not drawn on transfer links</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/nov/19/will-pochettino-fix-manchester-united-put-your-questions-to-will-unwin" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在毛里西奥·波切蒂诺备战他在安菲尔德的首场执教比赛之际，《卫报》的威尔·安温回答了大家关于曼联新任主教练、董事会、青训营以及弗兰克·伊莱特是否会理发的问题。tetters 提问：" data-title="‘Should Manchester United fans be hoping for relegation?’ Will Unwin answered your questions" data-date="11-19 23:31" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-19 23:31</span>
          <span class="news-item-title">“曼联球迷应该希望球队降级吗？” 威尔·安温回答了您的问题</span>
          <span class="news-item-title-en">‘Should Manchester United fans be hoping for relegation?’ Will Unwin answered your questions</span>
          <span class="news-value-point">💡 在毛里西奥·波切蒂诺备战他在安菲尔德的首场执教比赛之际，《卫报》的威尔·安温回答了大家关于曼联新任主教练、董事会、青训营以及弗兰克·伊莱特是否会…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13614031/premier-league-clubs-vote-to-cover-legal-costs-if-man-city-sponsors-sue-competitions-board-members" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英超联赛俱乐部已投票决定，如果曼城俱乐部的赞助商对英超联赛的五名董事会成员提起个人诉讼，将由英超联赛承担他们的法律费用。" data-title="PL clubs vote to cover legal costs of board members if Man City sponsors sue" data-date="11-19 23:26" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-19 23:26</span>
          <span class="news-item-title">英超俱乐部投票决定，如果曼城赞助商提起诉讼，将承担董事会成员的法律费用</span>
          <span class="news-item-title-en">PL clubs vote to cover legal costs of board members if Man City sponsors sue</span>
          <span class="news-value-point">💡 英超联赛俱乐部已投票决定，如果曼城俱乐部的赞助商对英超联赛的五名董事会成员提起个人诉讼，将由英超联赛承担他们的法律费用</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/12040/13353569/leeds-united-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Leeds latest: &#39;I’m a bit bored,&#39; jokes Farke after Trafford frenzy" data-title="Leeds latest: &#39;I’m a bit bored,&#39; jokes Farke after Trafford frenzy" data-date="11-19 23:20" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-19 23:20</span>
          <span class="news-item-title">利兹联最新消息：法尔克在特拉福德的疯狂胜利后开玩笑说：“我有点无聊。”</span>
          <span class="news-item-title-en">Leeds latest: 'I’m a bit bored,' jokes Farke after Trafford frenzy</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13613832/man-utd-latest-financial-results-revealed-as-revenue-and-wages-increase" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联发布了最新的财务业绩，收入和薪资均有所增长。" data-title="Man Utd announce financial results as revenue and wages rise" data-date="11-19 22:35" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-19 22:35</span>
          <span class="news-item-title">曼联公布财务业绩，营收和薪资均有所增长</span>
          <span class="news-item-title-en">Man Utd announce financial results as revenue and wages rise</span>
          <span class="news-value-point">💡 曼联发布了最新的财务业绩，收入和薪资均有所增长</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13613832/man-utd-latest-financial-results-revealed-as-revenue-and-wages-increase" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联发布了最新的财务业绩，收入和薪资均有所增长。" data-title="Man Utd announce financial results as revenue and wages rise" data-date="11-19 22:35" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-19 22:35</span>
          <span class="news-item-title">曼联公布财务业绩，营收和薪资均有所增长</span>
          <span class="news-item-title-en">Man Utd announce financial results as revenue and wages rise</span>
          <span class="news-value-point">💡 曼联发布了最新的财务业绩，收入和薪资均有所增长</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqy4jvdw7jdlo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英超联赛俱乐部投票决定，如果曼城俱乐部的赞助商起诉英超联赛的五名董事会成员，将为他们提供法律保护。" data-title="Premier League clubs to cover legal costs if Man City sponsors sue" data-date="11-19 21:29" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-19 21:29</span>
          <span class="news-item-title">如果曼城的赞助商提起诉讼，英超俱乐部将承担法律费用</span>
          <span class="news-item-title-en">Premier League clubs to cover legal costs if Man City sponsors sue</span>
          <span class="news-value-point">💡 英超联赛俱乐部投票决定，如果曼城俱乐部的赞助商起诉英超联赛的五名董事会成员，将为他们提供法律保护</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13613875/andoni-iraolas-liverpool-start-assessed-creating-chaos-going-direct-and-fixing-leaky-defence" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦主教练安多尼·伊拉奥拉要求在11月的国际比赛日之后再对他的执教表现进行评判。在周日英超联赛中利物浦迎战曼联之前，我们来评估这位巴斯克教练迄今为止在新职位上的表现。" data-title="Assessing Iraola&#39;s Liverpool start" data-date="11-19 21:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-19 21:00</span>
          <span class="news-item-title">评估伊拉奥拉在利物浦的开局表现</span>
          <span class="news-item-title-en">Assessing Iraola's Liverpool start</span>
          <span class="news-value-point">💡 利物浦主教练安多尼·伊拉奥拉要求在11月的国际比赛日之后再对他的执教表现进行评判</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13613937/premier-league-fixtures-on-sky-sports-man-city-vs-arsenal-and-man-utd-vs-liverpool-live-in-january" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳客场挑战曼城，以及曼联在老特拉福德主场迎战利物浦，是 1 月份 Sky Sports 直播的两场焦点赛事。" data-title="Man City vs Arsenal and Man Utd vs Liverpool live on Sky in January" data-date="11-19 20:50" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-19 20:50</span>
          <span class="news-item-title">1 月，曼城对阵阿森纳、曼联对阵利物浦的比赛将在 Sky 体育频道直播</span>
          <span class="news-item-title-en">Man City vs Arsenal and Man Utd vs Liverpool live on Sky in January</span>
          <span class="news-value-point">💡 阿森纳客场挑战曼城，以及曼联在老特拉福德主场迎战利物浦，是 1 月份 Sky Sports 直播的两场焦点赛事</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025492/man-utd-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Man Utd latest: Pochettino reveals 1999 Treble connection and Fergie dream" data-title="Man Utd latest: Pochettino reveals 1999 Treble connection and Fergie dream" data-date="11-19 20:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-19 20:00</span>
          <span class="news-item-title">曼联最新消息：波切蒂诺透露与1999年三冠王的渊源以及对弗格森的憧憬</span>
          <span class="news-item-title-en">Man Utd latest: Pochettino reveals 1999 Treble connection and Fergie dream</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13613821/mauricio-pochettino-at-manchester-united-new-boss-vows-to-change-situation-at-old-trafford-in-first-interview" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在担任曼联主帅后的首次采访中，毛里西奥·波切蒂诺充满自信地誓言要在老特拉福德“改变现状”。" data-title="Pochettino vows to &#39;change things&#39; at Man Utd" data-date="11-19 19:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-19 19:00</span>
          <span class="news-item-title">波切蒂诺誓言在曼联“有所改变”</span>
          <span class="news-item-title-en">Pochettino vows to 'change things' at Man Utd</span>
          <span class="news-value-point">💡 在担任曼联主帅后的首次采访中，毛里西奥·波切蒂诺充满自信地誓言要在老特拉福德“改变现状”</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13612583/mauricio-pochettino-at-man-utd-seven-years-on-from-the-sack-at-spurs-what-sort-of-coach-is-he-now-we-will-soon-find-out" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="毛里西奥·波切蒂诺在过去十年里带领托特纳姆热刺取得的成就，现在看来比当时还要令人印象深刻。曼联真应该早在几年前就聘请这位备受欢迎的阿根廷教练。" data-title="Seven years on from the sack at Spurs what sort of coach is Pochettino now?" data-date="11-19 18:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-19 18:00</span>
          <span class="news-item-title">被热刺解雇七年后，波切蒂诺现在是怎样的教练？</span>
          <span class="news-item-title-en">Seven years on from the sack at Spurs what sort of coach is Pochettino now?</span>
          <span class="news-value-point">💡 毛里西奥·波切蒂诺在过去十年里带领托特纳姆热刺取得的成就，现在看来比当时还要令人印象深刻</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13613208/mauricio-pochettino-begins-man-utd-tenure-with-testing-trip-to-liverpool-premier-league-talking-points" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英超联赛在最近的国际比赛日后回归，在又一个繁忙的周末赛事开始前，天空体育的足球撰稿人对所有主要热点进行了深入分析。" data-title="Premier League talking points: Trial by Anfield as Poch begins Man Utd tenure" data-date="11-19 16:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-19 16:00</span>
          <span class="news-item-title">英超联赛热点话题：波切蒂诺开启曼联执教生涯，安菲尔德将成为试金石</span>
          <span class="news-item-title-en">Premier League talking points: Trial by Anfield as Poch begins Man Utd tenure</span>
          <span class="news-value-point">💡 英超联赛在最近的国际比赛日后回归，在又一个繁忙的周末赛事开始前，天空体育的足球撰稿人对所有主要热点进行了深入分析</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6x28e93zv3jo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英超联赛本赛季已进行十轮比赛，前五名被六大俱乐部占据。这并不令人意外，因为他们拥有数亿英镑的不断增长的优势。" data-title="How Premier League&#39;s big six keep getting richer" data-date="11-19 15:38" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-19 15:38</span>
          <span class="news-item-title">英超联赛的“六大豪门”是如何变得越来越富有的</span>
          <span class="news-item-title-en">How Premier League's big six keep getting richer</span>
          <span class="news-value-point">💡 英超联赛本赛季已进行十轮比赛，前五名被六大俱乐部占据</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/tennis/live-blog/12040/13523297/jack-draper-tennis-results-next-match-news-ranking-video-and-how-to-watch-on-sky-sports-tennis" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Draper hires new coach to work alongside Murray for upcoming season" data-title="Draper hires new coach to work alongside Murray for upcoming season" data-date="11-20 00:30" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-20 00:30</span>
          <span class="news-item-title">德雷珀聘请新教练，与穆雷搭档备战新赛季</span>
          <span class="news-item-title-en">Draper hires new coach to work alongside Murray for upcoming season</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1037558/microsoft-to-do-shutdown-planner" target="_blank" rel="noopener" data-cat="zonghe" data-summary="2015年，微软收购了一款名为Wunderlist的待办事项应用，传闻收购价格高达2亿美元。Wunderlist的粉丝们担心微软会让他们心爱的应用变得毫无生气、过于商业化，或者更糟的是，把它藏在一些复杂的" data-title="Microsoft is killing its great tasks app in favor of its worse tasks app" data-date="11-20 00:28" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-20 00:28</span>
          <span class="news-item-title">微软正在弃用其出色的任务应用，转而使用更差的任务应用</span>
          <span class="news-item-title-en">Microsoft is killing its great tasks app in favor of its worse tasks app</span>
          <span class="news-value-point">💡 2015年，微软收购了一款名为Wunderlist的待办事项应用，传闻收购价格高达2亿美元</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1036229/paramount-plus-black-friday-deal-2026-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在黑色星期五之前，您只需每月 $2.99 即可订阅 Paramount Plus，前两个月享受此优惠价格。优惠期结束后，您可以取消订阅，也可以按当时的费率自动续订，目前该费率为 $8.99。" data-title="You can grab two months of Paramount Plus for just $2.99 for Black Friday" data-date="11-20 00:15" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-20 00:15</span>
          <span class="news-item-title">黑色星期五期间，您只需2.99美元即可订阅Paramount Plus两个月</span>
          <span class="news-item-title-en">You can grab two months of Paramount Plus for just $2.99 for Black Friday</span>
          <span class="news-value-point">💡 在黑色星期五之前，您只需每月 $2.99 即可订阅 Paramount Plus，前两个月享受此优惠价格</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1037695/jpmorgan-chase-cyberattack" target="_blank" rel="noopener" data-cat="zonghe" data-summary="摩根大通表示，其第三方供应商遭遇网络攻击，导致客户姓名和电子邮件地址等营销数据泄露。这一确认是在Cybernews的一篇报道之后发布的，该报道称，一个勒索软件团伙泄露了属于……的电子邮件地址。" data-title="JPMorgan Chase reveals data breach, but says it’s unrelated to this week’s banking outage" data-date="11-20 00:14" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-20 00:14</span>
          <span class="news-item-title">摩根大通披露数据泄露事件，但表示与本周的银行系统中断无关</span>
          <span class="news-item-title-en">JPMorgan Chase reveals data breach, but says it’s unrelated to this week’s banking outage</span>
          <span class="news-value-point">💡 摩根大通表示，其第三方供应商遭遇网络攻击，导致客户姓名和电子邮件地址等营销数据泄露</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/029/710.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 20 日消息，Epic 本周送出的游戏是《深渊之印》，下周送出的游戏是《火之石 – 放置点击英雄 RPG》，《Bread and Fred》。领取链接：《Mark of the Deep》IT之家附游戏简介：深渊之印是一款史诗般的海盗冒险游戏，拥有强烈的叙事性，并融合了广受好评的银河恶魔城游戏与魂系游戏的惊险元素。深渊之印是一款史诗般的海盗冒险游戏，拥有强烈的叙事性，并融合了广受好评的银河恶魔城游戏与魂系游戏的惊险元素。以海盗刘琦的身份踏上旅程，探索受诅咒岛屿的奥秘，寻找失踪的海盗船员！踏上这场史诗般的海盗冒险！一艘海盗船在一个神秘岛屿失事，直到那时只有神话故事才知道。扮演小小刘琦，探索这个被神秘诅咒包围的岛屿的阴森地区，寻找失踪的他们：愤怒人鱼号船员！击败受诅咒的生物以" data-title="Epic 喜加一：《深渊之印》免费领取" data-date="11-20 00:05" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-20 00:05</span>
          <span class="news-item-title">Epic 喜加一：《深渊之印》免费领取</span>
          <span class="news-value-point">💡 IT之家 11 月 20 日消息，Epic 本周送出的游戏是《深渊之印》，下周送出的游戏是《火之石 – 放置点击英雄 RPG》，《Bread a…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1021241/best-fitness-wellness-gifts-2026" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在更加关注自身健康和健身方面，我们都需要一些帮助。节假日为我们提供了许多关注身心健康的理由，而一份好的礼物恰好可以激发新的爱好或支持健康习惯。" data-title="The Verge’s 2026 fitness and wellness gift guide" data-date="11-20 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-20 00:00</span>
          <span class="news-item-title">The Verge的2026年健身和健康礼品指南</span>
          <span class="news-item-title-en">The Verge’s 2026 fitness and wellness gift guide</span>
          <span class="news-value-point">💡 在更加关注自身健康和健身方面，我们都需要一些帮助</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/golf/news/12040/12950625/golf-leaderboards-pga-tour-lpga-tour-liv-golf-dp-world-tour-ladies-european-tour-major-championships-and-more" target="_blank" rel="noopener" data-cat="zonghe" data-summary="来自世界各地的最新高尔夫球赛得分和结果，包括DP世界巡回锦标赛、PGA巡回赛、LPGA巡回赛等。" data-title="Golf leaderboards: LPGA Tour&#39;s CME Group Tour Championship and more" data-date="11-20 00:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-20 00:00</span>
          <span class="news-item-title">高尔夫排行榜：LPGA巡回赛CME集团巡回锦标赛等</span>
          <span class="news-item-title-en">Golf leaderboards: LPGA Tour's CME Group Tour Championship and more</span>
          <span class="news-value-point">💡 来自世界各地的最新高尔夫球赛得分和结果，包括DP世界巡回锦标赛、PGA巡回赛、LPGA巡回赛等</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/boxing/news/12040/13613969/wbc-open-door-for-canelo-alvarez-to-challenge-britains-willy-hutchinson-for-light-heavyweight-world-championship" target="_blank" rel="noopener" data-cat="zonghe" data-summary="卡内洛·阿尔瓦雷斯有机会重返轻重量级，向新晋世界冠军威利·哈钦森发起挑战。" data-title="WBC open door for Canelo to fight Hutchinson for light" data-date="11-20 00:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-20 00:00</span>
          <span class="news-item-title">WBC 为“卡内洛”与“哈钦森”争夺轻量级冠军头衔敞开大门</span>
          <span class="news-item-title-en">WBC open door for Canelo to fight Hutchinson for light</span>
          <span class="news-value-point">💡 卡内洛·阿尔瓦雷斯有机会重返轻重量级，向新晋世界冠军威利·哈钦森发起挑战</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/029/706.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 19 日消息，此前在小米有品众筹的米家扫振电动牙刷 2 Pro，现已在京东平台开启预约，将于明日 0 点开售，价格为 199.75 元。IT之家从商品页面获悉，这款电动牙刷支持声波扫振马达 2.0，可高效清洁牙菌斑；支持智能分面扫振，可匹配不同清洁方案；配备全效缓震刷头，软胶升级不打牙，弹性结构更贴合。此外，它还配备动态交互彩屏，实现可视化洁牙；支持双向过压提醒，力大力小亮灯提醒，用力过度自动降频；配备 Type-C 接口，支持 190 天长续航；支持 IPX8 级防水。京东小米米家扫振电动牙刷 2 Pro 199.75 元直达链接" data-title="小米米家扫振电动牙刷 2 Pro 开售：动态彩屏交互、190 天长续航，199.75 元" data-date="11-19 23:19" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-19 23:19</span>
          <span class="news-item-title">小米米家扫振电动牙刷 2 Pro 开售：动态彩屏交互、190 天长续航，199.75 元</span>
          <span class="news-value-point">💡 IT之家 11 月 19 日消息，此前在小米有品众筹的米家扫振电动牙刷 2 Pro，现已在京东平台开启预约，将于明日 0 点开售，价格为 199…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/029/705.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 19 日消息，瑞典 EDM 组合 Swedish House Mafia 成员 Sebastian Ingrosso 最近在 X 平台发文，分享一款神秘设备并 @nothing。从他公布的图片我们可以看到，这款设备大概巴掌大小，外形类似录音笔，完全没有显示屏幕。机身带有两个实体按键，其中一个标有红色录音圆点，另一个则标注了“Talk”，旁边还带有状态指示灯。IT之家注意到，该设备样貌类似 Nothing CEO 裴宇此前晒出的 AI 设备局部外观。消息人士 Yogesh Brar 随后透露，这款产品是 Nothing 旗下首款 AI 设备，但他并没有公布设备的具体用途。" data-title="Nothing 首款 AI 设备外观流出：无屏设计，形似录音笔" data-date="11-19 23:17" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-19 23:17</span>
          <span class="news-item-title">Nothing 首款 AI 设备外观流出：无屏设计，形似录音笔</span>
          <span class="news-value-point">💡 IT之家 11 月 19 日消息，瑞典 EDM 组合 Swedish House Mafia 成员 Sebastian Ingrosso 最近在…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/029/704.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 19 日消息，此前有消息称，《GTA 6》在玩家通关主线剧情之前无法使用作弊码。不仅如此，启用作弊码还会锁定剧情进度，并关闭游戏存档功能。这意味着，玩家只能通过作弊码短暂体验一番疯狂犯罪的乐趣，随后就必须回归正常游戏流程。这一改动让部分玩家颇有微词。不过，对于希望降低游戏难度、又不想偏离开发团队原本设计体验的玩家来说，还有一个好消息：《GTA 6》实际上提供了两个设置，可以让游戏变得更加容易。据IT之家了解，玩家只需打开游戏设置菜单，进入“Gameplay”（游戏玩法）选项，就能找到“Accessible Combat”（无障碍战斗）和“Reduced Vehicle Damage”（降低车辆损伤）两个开关。开启这两项功能后，游戏中一些难度较高的环节就会变得容易应对。其中" data-title="《GTA 6》藏有两个“简单模式”开关：降低敌人血量、减少车辆受损" data-date="11-19 23:11" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-19 23:11</span>
          <span class="news-item-title">《GTA 6》藏有两个“简单模式”开关：降低敌人血量、减少车辆受损</span>
          <span class="news-value-point">💡 IT之家 11 月 19 日消息，此前有消息称，《GTA 6》在玩家通关主线剧情之前无法使用作弊码</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/029/703.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 19 日消息，据 Circana 调研数据，2026 年 10 月，美国游戏硬件整体支出同比增长 2%。其中 PS5 主机销售额较去年同比增长 20%；微软 XBOX Series X|S 大幅增长 42%。IT之家注意到，Circana 分析师对此表示，XBOX 主机销售额能够在美国出现大幅增长，有多重因素助推。首当其冲的是价格上涨，其次是 XBOX Series X|S 主机最近的销量已经很差，基数越低，实现更高的百分比增长就越容易。不过，美国消费者选购 XBOX Series X|S 的重要因素还有《GTA6》《战争机器：事变日》等大作。这些现象级游戏，让游戏玩家们选择购买游戏主机。" data-title="今年 10 月，微软 XBOX Series X|S 游戏主机美国销量大幅增长 42%" data-date="11-19 23:05" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-19 23:05</span>
          <span class="news-item-title">今年 10 月，微软 XBOX Series X|S 游戏主机美国销量大幅增长 42%</span>
          <span class="news-value-point">💡 IT之家 11 月 19 日消息，据 Circana 调研数据，2026 年 10 月，美国游戏硬件整体支出同比增长 2%</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/rugby-union/news/12040/13614004/rassie-erasmus-eddie-jones-says-south-africa-coach-overstepped-the-mark-with-criticism-of-match-officials" target="_blank" rel="noopener" data-cat="zonghe" data-summary="埃迪·琼斯（Eddie Jones）认为，拉西·埃拉斯莫斯（Rassie Erasmus）对比赛裁判的严厉批评“越界了”，导致这位南非队主教练被禁赛六场。" data-title="Jones: Erasmus overstepped the mark with officials comments" data-date="11-19 22:54" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-19 22:54</span>
          <span class="news-item-title">琼斯：埃拉斯莫斯在官方评论中越界了</span>
          <span class="news-item-title-en">Jones: Erasmus overstepped the mark with officials comments</span>
          <span class="news-value-point">💡 埃迪·琼斯（Eddie Jones）认为，拉西·埃拉斯莫斯（Rassie Erasmus）对比赛裁判的严厉批评“越界了”，导致这位南非队主教练被…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-19/10734966.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网丽水11月19日电(周健)初冬时节，浙江丽水空气清新、阳光明媚。19日，云和梯田旁的民宿内，一批来自江苏的职工赏山水、品香茶，享受疗休养的惬意时光。而在相隔10多公里的云和县城，“我在丽水疗休养”第七届秀山丽水疗休养区域协作暨丽水全域旅游联盟资源对接活动启幕，氛围火热。" data-title="浙江文旅观察：秀山丽水缘何看重“疗休养”？" data-date="11-19 22:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-19 22:41</span>
          <span class="news-item-title">浙江文旅观察：秀山丽水缘何看重“疗休养”？</span>
          <span class="news-value-point">💡 中新网丽水11月19日电(周健)初冬时节，浙江丽水空气清新、阳光明媚</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-19/10734963.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网西昌11月19日电 (程兆)四川省司法厅今年启动“法治蜀光”支持大小凉山做强公共法律服务三年行动，配套25项举措。19日，四川省人民政府新闻办公室在老成昆线西昌站举行第八期《发言人在现场》新闻发布活动，介绍相关部署及慢火车普法实践。" data-title="四川推出25项举措提升大小凉山公共法律服务 慢火车成为“流动法治课堂”" data-date="11-19 22:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-19 22:37</span>
          <span class="news-item-title">四川推出25项举措提升大小凉山公共法律服务 慢火车成为“流动法治课堂”</span>
          <span class="news-value-point">💡 中新网西昌11月19日电 (程兆)四川省司法厅今年启动“法治蜀光”支持大小凉山做强公共法律服务三年行动，配套25项举措</span>
        </a>
  </div>
</div>
<script defer src="{{ "/assets/js/news-feed.js" | relative_url }}"></script>


<p class="news-updated">🕐 抓取更新于 2026-11-20 00:42（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
