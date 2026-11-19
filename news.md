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
      <span>2026-11-20 04:50 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">天空体育×15 · The Verge×11</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">按来源聚合 · 最近 24 小时精选</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.nytimes.com/2026/11/19/world/asia/trump-xi-putin.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="President Trump called Russia’s leader his “friend” and marveled at China’s warm welcome for his first-ever trilateral summit. But there were no breakthroughs on nuclear control, the war in Ukraine or A.I." data-title="Trump Flaunts Camaraderie With Xi and Putin but Has Little to Show for It" data-date="11-20 03:07" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 11-20 03:07</span>
      </div>
      <h2 class="hero-featured-title">Trump Flaunts Camaraderie With Xi and Putin but Has Little to Show for It</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://techcrunch.com/2026/11/19/nvidia-ceo-jensen-huangs-affair-with-alleged-chinese-spy-a-timeline/" target="_blank" rel="noopener" data-cat="keji" data-summary="Jensen Huang在曝出婚外情后已从Nvidia辞职，鉴于美国和中国正在竞相开发最先进的人工智能基础设施，此事可能对国家安全产生影响。" data-title="The unfolding Jensen Huang scandal: a timeline" data-date="11-20 04:18" data-source="TechCrunch">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
      </div>
      <p class="hero-sub-title">正在发酵的黄仁勋丑闻：时间线</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/cje3900n0vvro?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="托马斯·弗兰克在以水晶宫主帅身份首次出席新闻发布会后表示，很高兴“重回江湖”。" data-title="Frank happy to be &#39;back in the circus&#39; at Palace" data-date="11-20 04:16" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">弗兰克很高兴“重返帕拉蒂的舞台”</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/f1/news/12040/13614150/fia-announce-introduction-of-full-time-f1-stewards-from-2027-ahead-of-las-vegas-grand-prix" target="_blank" rel="noopener" data-cat="zonghe" data-summary="国际汽联（FIA）宣布，从2027年起将引入全职F1赛事干事，旨在“使决策更加一致”。" data-title="FIA to introduce full" data-date="11-20 04:37" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">国际汽联将推出全套</p>
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
        <a class="news-item" href="https://www.nytimes.com/2026/11/19/world/asia/trump-xi-putin.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="President Trump called Russia’s leader his “friend” and marveled at China’s warm welcome for his first-ever trilateral summit. But there were no breakthroughs on nuclear control, the war in Ukraine or A.I." data-title="Trump Flaunts Camaraderie With Xi and Putin but Has Little to Show for It" data-date="11-20 03:07" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-20 03:07</span>
          <span class="news-item-title">Trump Flaunts Camaraderie With Xi and Putin but Has Little to Show for It</span>
          <span class="news-value-point">💡 President Trump called Russia’s leader his “friend” and marveled at Chin…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-20/10734985.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="11月19日下午，国家主席习近平在深圳同俄罗斯总统普京、美国总统特朗普举行中俄美元首会晤。习近平指出——" data-title="习近平：大国和则世界安，大国斗则世界乱" data-date="11-20 00:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-20 00:13</span>
          <span class="news-item-title">习近平：大国和则世界安，大国斗则世界乱</span>
          <span class="news-value-point">💡 11月19日下午，国家主席习近平在深圳同俄罗斯总统普京、美国总统特朗普举行中俄美元首会晤</span>
        </a>
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
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://techcrunch.com/2026/11/19/nvidia-ceo-jensen-huangs-affair-with-alleged-chinese-spy-a-timeline/" target="_blank" rel="noopener" data-cat="keji" data-summary="Jensen Huang在曝出婚外情后已从Nvidia辞职，鉴于美国和中国正在竞相开发最先进的人工智能基础设施，此事可能对国家安全产生影响。" data-title="The unfolding Jensen Huang scandal: a timeline" data-date="11-20 04:18" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-20 04:18</span>
          <span class="news-item-title">正在发酵的黄仁勋丑闻：时间线</span>
          <span class="news-item-title-en">The unfolding Jensen Huang scandal: a timeline</span>
          <span class="news-value-point">💡 Jensen Huang在曝出婚外情后已从Nvidia辞职，鉴于美国和中国正在竞相开发最先进的人工智能基础设施，此事可能对国家安全产生影响</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/19/business/anthropic-ipo-dustin-moskovitz.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Facebook联合创始人达斯汀·莫斯科维茨（Dustin Moskovitz）对Anthropic的早期投资正在获得回报。但这并没有让他感到高兴。" data-title="Dustin Moskovitz, an Early Anthropic Investor, Feels a Bit Uneasy About the IPO" data-date="11-20 03:30" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-20 03:30</span>
          <span class="news-item-title">Anthropic 的早期投资者达斯汀·莫斯科维茨（Dustin Moskovitz）对 IPO 感到有些不安</span>
          <span class="news-item-title-en">Dustin Moskovitz, an Early Anthropic Investor, Feels a Bit Uneasy About the IPO</span>
          <span class="news-value-point">💡 Facebook联合创始人达斯汀·莫斯科维茨（Dustin Moskovitz）对Anthropic的早期投资正在获得回报</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/19/anthropics-ipo-could-deliver-156-billion-to-charity/" target="_blank" rel="noopener" data-cat="keji" data-summary="当股价为95美元时，Frontier Lab的公益基金会、其员工捐款以及公司的配捐总额高达1560亿美元。" data-title="Anthropic’s IPO could deliver $156 billion to charity" data-date="11-20 03:10" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-20 03:10</span>
          <span class="news-item-title">Anthropic的IPO可能为慈善事业带来1560亿美元</span>
          <span class="news-item-title-en">Anthropic’s IPO could deliver $156 billion to charity</span>
          <span class="news-value-point">💡 当股价为95美元时，Frontier Lab的公益基金会、其员工捐款以及公司的配捐总额高达1560亿美元</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1037902/google-gemini-macos-ai-computer-use" target="_blank" rel="noopener" data-cat="keji" data-summary="Google 表示，适用于 macOS 的 Gemini 应用现已具备计算机使用功能，这意味着它可以帮助您“在本地文件、桌面应用和网络上完成多步任务”。Google表示，该功能可能有助于加快工作进度等。" data-title="Gemini on Mac can now use your computer" data-date="11-20 02:21" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-20 02:21</span>
          <span class="news-item-title">Mac 版 Gemini 现在可以使用您的电脑了</span>
          <span class="news-item-title-en">Gemini on Mac can now use your computer</span>
          <span class="news-value-point">💡 Google 表示，适用于 macOS 的 Gemini 应用现已具备计算机使用功能，这意味着它可以帮助您“在本地文件、桌面应用和网络上完成多步…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/19/google-gives-gemini-the-ability-to-use-your-mac-for-you/" target="_blank" rel="noopener" data-cat="keji" data-summary="Google 对 Gemini 的最新更新为 Mac 带来了 AI 代理，它可以整理文件、填写表单并处理多步工作流程。" data-title="Google gives Gemini the ability to use your Mac for you" data-date="11-20 02:09" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-20 02:09</span>
          <span class="news-item-title">Google让Gemini能够代您使用Mac</span>
          <span class="news-item-title-en">Google gives Gemini the ability to use your Mac for you</span>
          <span class="news-value-point">💡 Google 对 Gemini 的最新更新为 Mac 带来了 AI 代理，它可以整理文件、填写表单并处理多步工作流程</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/19/metas-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report-says/" target="_blank" rel="noopener" data-cat="keji" data-summary="在其中一些情况下，员工表示Muse显示了他们从未提出的托儿申请、他们从未征询的职业建议、他们从未下过的产品订单以及不属于他们的银行账户余额。" data-title="Meta’s AI agent Muse is mixing up conversations and could be exposing private data, report says" data-date="11-20 01:38" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-20 01:38</span>
          <span class="news-item-title">据报道，Meta的AI代理Muse正在混淆对话，并可能泄露私人数据</span>
          <span class="news-item-title-en">Meta’s AI agent Muse is mixing up conversations and could be exposing private data, report says</span>
          <span class="news-value-point">💡 在其中一些情况下，员工表示Muse显示了他们从未提出的托儿申请、他们从未征询的职业建议、他们从未下过的产品订单以及不属于他们的银行账户余额</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/19/anthropic-hits-nasdaq-exchanges-at-110-27-above-ipo-price/" target="_blank" rel="noopener" data-cat="keji" data-summary="Anthropic的IPO价格定为83美元，这意味着将筹集超过800亿美元的新资本。" data-title="Anthropic hits Nasdaq exchanges at $111, 33% above IPO price" data-date="11-20 00:59" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-20 00:59</span>
          <span class="news-item-title">Anthropic在纳斯达克交易所上市，股价为111美元，比IPO价格高出33%</span>
          <span class="news-item-title-en">Anthropic hits Nasdaq exchanges at $111, 33% above IPO price</span>
          <span class="news-value-point">💡 Anthropic的IPO价格定为83美元，这意味着将筹集超过800亿美元的新资本</span>
        </a>
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
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cje3900n0vvro?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="托马斯·弗兰克在以水晶宫主帅身份首次出席新闻发布会后表示，很高兴“重回江湖”。" data-title="Frank happy to be &#39;back in the circus&#39; at Palace" data-date="11-20 04:16" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-20 04:16</span>
          <span class="news-item-title">弗兰克很高兴“重返帕拉蒂的舞台”</span>
          <span class="news-item-title-en">Frank happy to be 'back in the circus' at Palace</span>
          <span class="news-value-point">💡 托马斯·弗兰克在以水晶宫主帅身份首次出席新闻发布会后表示，很高兴“重回江湖”</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/arsenal-women-vs-olympiques-lyon-women/live/578272" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="WCL: Dominant Lyon take the lead at Arsenal through Brand LIVE!" data-title="WCL: Dominant Lyon take the lead at Arsenal through Brand LIVE!" data-date="11-20 03:03" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-20 03:03</span>
          <span class="news-item-title">WCL：里昂占据主导，通过布兰德的进球在阿森纳取得领先！</span>
          <span class="news-item-title-en">WCL: Dominant Lyon take the lead at Arsenal through Brand LIVE!</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c50mdnxy3ry0o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="BBC体育足球专家克里斯·萨顿（Chris Sutton）将与世界冠军拳击手劳伦·普莱斯（Lauren Price）、BBC读者以及人工智能一较高下，预测本周末英超联赛的赛果。" data-title="Sutton&#39;s predictions v world champion boxer Lauren Price" data-date="11-20 02:52" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-20 02:52</span>
          <span class="news-item-title">萨顿的预测与世界冠军拳手劳伦·普莱斯</span>
          <span class="news-item-title-en">Sutton's predictions v world champion boxer Lauren Price</span>
          <span class="news-value-point">💡 BBC体育足球专家克里斯·萨顿（Chris Sutton）将与世界冠军拳击手劳伦·普莱斯（Lauren Price）、BBC读者以及人工智能一较…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13611640/premier-league-predictions-jones-knows-best-bets-newcastle-vs-arsenal-liverpool-vs-manchester-united-and-much-more" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="随着英超联赛在国际比赛日后回归，我们的顶级投注专家Lewis Jones（又名Jones Knows）将提供他的分析和投注见解。" data-title="PL Predictions: How will your club fare this weekend?" data-date="11-20 02:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-20 02:00</span>
          <span class="news-item-title">英超预测：您的俱乐部本周末表现如何？</span>
          <span class="news-item-title-en">PL Predictions: How will your club fare this weekend?</span>
          <span class="news-value-point">💡 随着英超联赛在国际比赛日后回归，我们的顶级投注专家Lewis Jones（又名Jones Knows）将提供他的分析和投注见解</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13611640/premier-league-predictions-jones-knows-best-bets-newcastle-vs-arsenal-liverpool-vs-manchester-united-and-much-more" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="随着英超联赛在国际比赛日后回归，我们的顶级投注专家Lewis Jones（又名Jones Knows）将提供他的分析和投注见解。" data-title="PL Predictions: How will your club fare this weekend?" data-date="11-20 02:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-20 02:00</span>
          <span class="news-item-title">英超预测：您的俱乐部本周末表现如何？</span>
          <span class="news-item-title-en">PL Predictions: How will your club fare this weekend?</span>
          <span class="news-value-point">💡 随着英超联赛在国际比赛日后回归，我们的顶级投注专家Lewis Jones（又名Jones Knows）将提供他的分析和投注见解</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/12040/13279295/brighton-transfers-latest-news-rumours-and-gossip-live-updates-goals-and-highlights" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Brighton latest: Hurzeler not leaving for a long time, says Bloom" data-title="Brighton latest: Hurzeler not leaving for a long time, says Bloom" data-date="11-20 01:23" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-20 01:23</span>
          <span class="news-item-title">布莱顿最新消息：布卢姆表示，许策尔不会在很长一段时间内离开</span>
          <span class="news-item-title-en">Brighton latest: Hurzeler not leaving for a long time, says Bloom</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/12040/13025489/tottenham-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Spurs latest: &#39;You only know a tenth of the truth,&#39; says Frank" data-title="Spurs latest: &#39;You only know a tenth of the truth,&#39; says Frank" data-date="11-20 01:20" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-20 01:20</span>
          <span class="news-item-title">热刺最新消息：弗兰克表示：“你只知道十分之一的真相。”</span>
          <span class="news-item-title-en">Spurs latest: 'You only know a tenth of the truth,' says Frank</span>
        </a>
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
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/f1/news/12040/13614150/fia-announce-introduction-of-full-time-f1-stewards-from-2027-ahead-of-las-vegas-grand-prix" target="_blank" rel="noopener" data-cat="zonghe" data-summary="国际汽联（FIA）宣布，从2027年起将引入全职F1赛事干事，旨在“使决策更加一致”。" data-title="FIA to introduce full" data-date="11-20 04:37" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-20 04:37</span>
          <span class="news-item-title">国际汽联将推出全套</span>
          <span class="news-item-title-en">FIA to introduce full</span>
          <span class="news-value-point">💡 国际汽联（FIA）宣布，从2027年起将引入全职F1赛事干事，旨在“使决策更加一致”</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1038087/meta-muse-charm-ai-price" target="_blank" rel="noopener" data-cat="zonghe" data-summary="据《The Information》报道，Meta计划将Muse Charm的售价定为300美元。Muse Charm是一款带屏幕的小型设备，可让您与Muse AI智能助手聊天。首席执行官马克·扎克伯格今年早些时候展示了这款小工具，并表示公司预计将发货。" data-title="Meta’s Muse Charm might cost $300" data-date="11-20 04:22" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-20 04:22</span>
          <span class="news-item-title">Meta 的 Muse 智能眼镜可能售价 300 美元</span>
          <span class="news-item-title-en">Meta’s Muse Charm might cost $300</span>
          <span class="news-value-point">💡 据《The Information》报道，Meta计划将Muse Charm的售价定为300美元</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1038059/google-search-homepage-ai-chats" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Google 正在更新其主页，以纳入 AI 搜索功能。在X上的一篇帖子中，谷歌产品副总裁Robby Stein展示了如何打开可折叠的侧边栏，以查看并继续您的AI聊天。根据斯坦分享的GIF图，看起来……" data-title="Google is putting AI chats right on the homepage" data-date="11-20 04:05" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-20 04:05</span>
          <span class="news-item-title">谷歌正在将AI聊天功能直接置于主页上</span>
          <span class="news-item-title-en">Google is putting AI chats right on the homepage</span>
          <span class="news-value-point">💡 Google 正在更新其主页，以纳入 AI 搜索功能</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/policy/1037987/fcc-prison-cellphone-signal-jamming" target="_blank" rel="noopener" data-cat="zonghe" data-summary="美国联邦通信委员会（FCC）一致投票通过，允许州立和地方监狱干扰手机信号。FCC在周四的公告中表示，该规定将有助于打击用于在监狱中实施犯罪的“违禁手机大量涌入”现象。" data-title="FCC greenlights rule allowing prisons to jam cellphone signals" data-date="11-20 03:40" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-20 03:40</span>
          <span class="news-item-title">美国联邦通信委员会（FCC）批准允许监狱屏蔽手机信号的规定</span>
          <span class="news-item-title-en">FCC greenlights rule allowing prisons to jam cellphone signals</span>
          <span class="news-value-point">💡 美国联邦通信委员会（FCC）一致投票通过，允许州立和地方监狱干扰手机信号</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1037790/sony-wh-1000xm5-black-friday-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在我那个年代，“开门抢购”促销活动只在实体零售店进行。但现在，无论您是想在实体店还是网上购物，都可以在黑色星期五之前享受超低价。其中一款引人注目的产品是上一代索尼 WH-1000XM5 降噪耳机。" data-title="Sony’s WH-1000XM5 are cheaper than ever for Black Friday" data-date="11-20 03:35" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-20 03:35</span>
          <span class="news-item-title">索尼WH-1000XM5在黑色星期五期间比以往任何时候都便宜</span>
          <span class="news-item-title-en">Sony’s WH-1000XM5 are cheaper than ever for Black Friday</span>
          <span class="news-value-point">💡 在我那个年代，“开门抢购”促销活动只在实体零售店进行</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/games/1038010/valve-steam-machine-waitlist-supply" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Valve今天宣布了有关Steam Machine供应情况的一些最新消息，其中包括如果您想立即购买一台的好消息，以及由于RAMaggedon（内存危机）而可能出现的未来供应坏消息。好消息是：您现在可以购买512GB的Steam Machine，无需" data-title="You can now buy a Steam Machine without getting on a waitlist" data-date="11-20 03:33" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-20 03:33</span>
          <span class="news-item-title">您现在可以购买Steam Machine，无需加入等候名单</span>
          <span class="news-item-title-en">You can now buy a Steam Machine without getting on a waitlist</span>
          <span class="news-value-point">💡 Valve今天宣布了有关Steam Machine供应情况的一些最新消息，其中包括如果您想立即购买一台的好消息，以及由于RAMaggedon（内…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/news/1037951/instagram-amazon-affiliate-links-influencers-ads" target="_blank" rel="noopener" data-cat="zonghe" data-summary="多年来，网红们一直在社交媒体上想方设法地寻找与粉丝分享联盟营销链接的变通方案。本月早些时候，Instagram 和亚马逊宣布了一项新的整合，旨在为网红提供便利。" data-title="Some creators are skeptical of Instagram’s new affiliate program" data-date="11-20 03:12" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-20 03:12</span>
          <span class="news-item-title">一些创作者对 Instagram 的新联盟计划持怀疑态度</span>
          <span class="news-item-title-en">Some creators are skeptical of Instagram’s new affiliate program</span>
          <span class="news-value-point">💡 多年来，网红们一直在社交媒体上想方设法地寻找与粉丝分享联盟营销链接的变通方案</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/darts/news/12040/13613983/the-world-darts-championship-is-now-the-incentive-for-luke-littler-after-grand-slam-of-darts-loss-says-wayne-mardle" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在飞镖大满贯赛的16强阶段，卢克·利特勒（Luke Littler）爆冷以10-8不敌杰尔梅恩·瓦蒂梅纳（Jermaine Wattimena）。天空体育飞镖频道的韦恩·马德尔（Wayne Mardle）认为，这位世界排名第一的选手现在必须全力以赴，为世界飞镖锦标赛做好准备。" data-title="Mardle: The Worlds is now the &#39;incentive&#39; for Littler" data-date="11-20 03:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-20 03:00</span>
          <span class="news-item-title">马德尔：世锦赛现在是利特勒的“激励”</span>
          <span class="news-item-title-en">Mardle: The Worlds is now the 'incentive' for Littler</span>
          <span class="news-value-point">💡 在飞镖大满贯赛的16强阶段，卢克·利特勒（Luke Littler）爆冷以10-8不敌杰尔梅恩·瓦蒂梅纳（Jermaine Wattimena）</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1037042/sonos-black-friday-2026-speaker-soundbar-deals-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Sonos音箱和条形音箱并不算便宜，但幸运的是，该公司的黑色星期五促销活动已经开始，截至11月30日，所有产品都变得更加实惠。最值得一提的是，您可以以史低价入手Arc Ultra条形音箱。" data-title="Sonos is taking up to 30 percent off speakers and soundbars right now" data-date="11-20 02:33" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-20 02:33</span>
          <span class="news-item-title">Sonos现正推出音箱和条形音箱最高七折优惠</span>
          <span class="news-item-title-en">Sonos is taking up to 30 percent off speakers and soundbars right now</span>
          <span class="news-value-point">💡 Sonos音箱和条形音箱并不算便宜，但幸运的是，该公司的黑色星期五促销活动已经开始，截至11月30日，所有产品都变得更加实惠</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/darts/live-blog/12040/13613976/grand-slam-of-darts-commentary-updates-scores-analysis-with-luke-humphries-michael-van-gerwen-nathan-aspinall-in-action" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Grand Slam of Darts LIVE! Van Veen in action as Aspinall wins, Humphries, MVG to come" data-title="Grand Slam of Darts LIVE! Van Veen in action as Aspinall wins, Humphries, MVG to come" data-date="11-20 02:30" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-20 02:30</span>
          <span class="news-item-title">镖神大满贯直播！范·文出战，阿斯皮纳尔获胜，汉弗莱斯、MVG即将登场</span>
          <span class="news-item-title-en">Grand Slam of Darts LIVE! Van Veen in action as Aspinall wins, Humphries, MVG to come</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/19/world/europe/myanmar-genocide-icj-decision-.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="In a decision with potentially broad implications, the International Court of Justice found a state culpable of genocide for the first time." data-title="Myanmar Committed Genocide Against the Rohingya, Top Global Court Finds" data-date="11-20 02:27" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-20 02:27</span>
          <span class="news-item-title">Myanmar Committed Genocide Against the Rohingya, Top Global Court Finds</span>
          <span class="news-value-point">💡 In a decision with potentially broad implications, the International Cou…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/19/former-alibaba-execs-everful-raises-48-5m-to-connect-retailers-with-chinese-factories/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Everful已筹集4850万美元，用于拓展其工厂直采平台，帮助零售商从海外制造商处采购产品。" data-title="Former Alibaba exec’s Everful raises $48.5M to connect retailers with Chinese factories" data-date="11-20 01:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-20 01:00</span>
          <span class="news-item-title">前阿里巴巴高管的Everful筹集4850万美元，旨在将零售商与中国工厂联系起来</span>
          <span class="news-item-title-en">Former Alibaba exec’s Everful raises $48.5M to connect retailers with Chinese factories</span>
          <span class="news-value-point">💡 Everful已筹集4850万美元，用于拓展其工厂直采平台，帮助零售商从海外制造商处采购产品</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/golf/news/12040/13614051/tiger-woods-former-world-no-1-hails-special-opportunity-to-design-new-course-in-northern-ireland-with-tgr-design" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Tiger Woods has revealed he will design the first championship-standard links golf course built in Northern Ireland for more than 100 years, describing the project as a &quot;special opportunity&quot;." data-title="Woods given &#39;special opportunity&#39; to design new course in Northern Ireland" data-date="11-20 00:30" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-20 00:30</span>
          <span class="news-item-title">伍兹获得“特殊机会”，将在北爱尔兰设计新球场</span>
          <span class="news-item-title-en">Woods given 'special opportunity' to design new course in Northern Ireland</span>
          <span class="news-value-point">💡 Tiger Woods has revealed he will design the first championship-standard …</span>
        </a>
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
  </div>
</div>
<script defer src="{{ "/assets/js/news-feed.js" | relative_url }}"></script>


<p class="news-updated">🕐 抓取更新于 2026-11-20 04:50（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
