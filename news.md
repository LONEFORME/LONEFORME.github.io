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
      <span>2026-11-10 01:43 抓取更新</span>
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
        <span class="channel-count">58</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('shizheng', this)">
        <span>🏛️ 时政与国际</span>
        <span class="channel-count">13</span>
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
  <div class="ov-item"><span class="ov-num">58</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×12 · 天空体育×10</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.bbc.com/zhongwen/articles/cj20v0x3ze2no/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="白金汉宫一名幕僚表示，若贝安德首相向王室提议查尔斯三世访华，国王将“小心考虑”。" data-title="白金汉宫幕僚：英王查尔斯“会考虑访华”" data-date="11-10 00:31" data-source="BBC">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
        <span class="hero-featured-date">🕒 11-10 00:31</span>
      </div>
      <h2 class="hero-featured-title">白金汉宫幕僚：英王查尔斯“会考虑访华”</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.theverge.com/ai-artificial-intelligence/1029990/jensen-huang-the-spy-who-loved-me" target="_blank" rel="noopener" data-cat="keji" data-summary="我希望这些人的性生活与我无关，但我想我们必须谈谈Jensen Huang和国家安全事件。谁能想到，在这里签奶的家伙可能没有很好的判断力" data-title="The future of AI hinges on… Jensen Huang’s sex life?" data-date="11-10 01:36" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">The future of AI hinges on… Jensen Huang’s sex life?</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/football/news/12040/13610315/michael-carrick-future-man-utd-will-not-rush-decision-over-head-coachs-tenure-despite-dropping-into-relegation-zone" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在4-4战平阿斯顿维拉之后，曼联的老板们不会急于就迈克尔卡里克的未来做出决定，这让他们处于降级区。" data-title="Man Utd will not rush decision on Carrick future" data-date="11-10 00:52" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">Man Utd will not rush decision on Carrick future</p>
    </a>
    <a class="hero-sub-card" href="https://www.theverge.com/entertainment/1030022/james-gunn-peter-safran-dc-studios-out-leaving" target="_blank" rel="noopener" data-cat="zonghe" data-summary="很快， James Gunn和Peter Safran将不再领导Skydance的DC工作室。在2022年担任DC Studios联合首席执行官后， Gunn和Safran将被前漫威制作和开发高级副总裁Jeremy Latcham所取代，他是Deadline的代表" data-title="James Gunn is out as DC movie leader" data-date="11-10 01:39" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">James Gunn is out as DC movie leader</p>
    </a>
  </div>
</div>
<div class="news-grid">
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🏛️</span>
      <span class="news-category-title">时政要闻 & 国际动态</span>
      <span class="news-category-count">13 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cj20v0x3ze2no/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="白金汉宫一名幕僚表示，若贝安德首相向王室提议查尔斯三世访华，国王将“小心考虑”。" data-title="白金汉宫幕僚：英王查尔斯“会考虑访华”" data-date="11-10 00:31" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-10 00:31</span>
          <span class="news-item-title">白金汉宫幕僚：英王查尔斯“会考虑访华”</span>
          <span class="news-value-point">💡 白金汉宫一名幕僚表示，若贝安德首相向王室提议查尔斯三世访华，国王将“小心考虑”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-09/10729157.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社柏林11月9日电 (记者 马秀秀)当地时间9日，德国基督教民主联盟(基民盟)领导层正式提名61岁的巴伐利亚州议会议长伊尔泽·艾格纳竞选下任德国总统。如最终当选，艾格纳将成为德国历史上首位女性国家元首。" data-title="德国总理默茨正式提名艾格纳竞选总统" data-date="11-09 23:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 23:02</span>
          <span class="news-item-title">德国总理默茨正式提名艾格纳竞选总统</span>
          <span class="news-value-point">💡 中新社柏林11月9日电 (记者 马秀秀)当地时间9日，德国基督教民主联盟(基民盟)领导层正式提名61岁的巴伐利亚州议会议长伊尔泽·艾格纳竞选下任…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-09/10729129.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月9日电 综合消息：伊朗外交部长阿拉格齐、外交部发言人巴加埃9日分别表示，“受够了”无休止的战争，伊方提出的“两日计划”依然有效。霍尔木兹海峡能否开放取决于美国的政治意愿和决策。" data-title="伊朗称“两日计划”依然有效  霍尔木兹海峡能否开放取决于美方" data-date="11-09 21:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 21:42</span>
          <span class="news-item-title">伊朗称“两日计划”依然有效  霍尔木兹海峡能否开放取决于美方</span>
          <span class="news-value-point">💡 中新社北京11月9日电 综合消息：伊朗外交部长阿拉格齐、外交部发言人巴加埃9日分别表示，“受够了”无休止的战争，伊方提出的“两日计划”依然有效</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-09/10729095.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月9日电 当地时间11月9日，中国国家副主席韩正在伊斯坦布尔同土耳其副总统耶尔马兹共同出席中国－土耳其绿色发展商务论坛并致辞。" data-title="韩正同土耳其副总统耶尔马兹共同出席中国－土耳其绿色发展商务论坛并致辞" data-date="11-09 21:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 21:01</span>
          <span class="news-item-title">韩正同土耳其副总统耶尔马兹共同出席中国－土耳其绿色发展商务论坛并致辞</span>
          <span class="news-value-point">💡 中新社北京11月9日电 当地时间11月9日，中国国家副主席韩正在伊斯坦布尔同土耳其副总统耶尔马兹共同出席中国－土耳其绿色发展商务论坛并致辞</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-09/10729097.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社东京11月9日电 (记者 朱晨曦)据日本共同社9日报道，日本执政党自民党当天表示，针对前首相石破茂等4人在消费税减税相关法案表决前离场、未投赞成票，对他们给予警告处分。这是日本首次有前首相受到这一处分。" data-title="日本前首相石破茂受到党内警告处分" data-date="11-09 20:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 20:56</span>
          <span class="news-item-title">日本前首相石破茂受到党内警告处分</span>
          <span class="news-value-point">💡 中新社东京11月9日电 (记者 朱晨曦)据日本共同社9日报道，日本执政党自民党当天表示，针对前首相石破茂等4人在消费税减税相关法案表决前离场、未…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-09/10729065.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="直播海报：国家发改委就增进民生福祉有关情况举行新闻发布会" data-title="直播海报：国家发改委就增进民生福祉有关情况举行新闻发布会" data-date="11-09 20:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 20:22</span>
          <span class="news-item-title">直播海报：国家发改委就增进民生福祉有关情况举行新闻发布会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-09/10729058.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月9日电 据安徽省纪委监委消息：淮北矿业(集团)有限责任公司原副总经理谢道成涉嫌严重违纪违法，目前正接受安徽省纪委监委纪律审查和监察调查。" data-title="淮北矿业（集团）有限责任公司原副总经理谢道成接受审查调查" data-date="11-09 20:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 20:11</span>
          <span class="news-item-title">淮北矿业（集团）有限责任公司原副总经理谢道成接受审查调查</span>
          <span class="news-value-point">💡 中新网11月9日电 据安徽省纪委监委消息：淮北矿业(集团)有限责任公司原副总经理谢道成涉嫌严重违纪违法，目前正接受安徽省纪委监委纪律审查和监察调…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/09/world/africa/trump-deportations-court-orders-refoulement.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="与特朗普政府合作，外国合作伙伴接受被驱逐者，然后将他们运往美国本身将被禁止派遣他们的国家。" data-title="Immigrants Are Being Systematically Returned Home Despite Court Orders" data-date="11-09 20:04" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-09 20:04</span>
          <span class="news-item-title">尽管有法院命令，移民仍被系统地遣返家园</span>
          <span class="news-item-title-en">Immigrants Are Being Systematically Returned Home Despite Court Orders</span>
          <span class="news-value-point">💡 与特朗普政府合作，外国合作伙伴接受被驱逐者，然后将他们运往美国本身将被禁止派遣他们的国家</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-09/10729028.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网沈阳11月9日电 (记者 李𬀪)中共沈阳市委9日召开“中国共产党沈阳市第十五次代表大会”新闻发布会，中共沈阳市委副书记魏红江介绍沈阳市第十五次党代会及市委十五届一次全会的有关情况。" data-title="沈阳不断推动东北亚国际化中心城市建设迈上新台阶" data-date="11-09 20:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 20:00</span>
          <span class="news-item-title">沈阳不断推动东北亚国际化中心城市建设迈上新台阶</span>
          <span class="news-value-point">💡 中新网沈阳11月9日电 (记者 李𬀪)中共沈阳市委9日召开“中国共产党沈阳市第十五次代表大会”新闻发布会，中共沈阳市委副书记魏红江介绍沈阳市第十…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-09/10728994.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网金边11月9日电 (张堰林 杨强)柬埔寨独立73周年庆祝仪式当地时间9日在金边举行。柬埔寨国王诺罗敦·西哈莫尼以及柬参议院主席洪森、国会主席昆索达莉、首相洪玛奈，驻柬外国使节和社会各界民众出席庆祝活动。" data-title="柬埔寨庆祝国家独立73周年" data-date="11-09 18:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 18:29</span>
          <span class="news-item-title">柬埔寨庆祝国家独立73周年</span>
          <span class="news-value-point">💡 中新网金边11月9日电 (张堰林 杨强)柬埔寨独立73周年庆祝仪式当地时间9日在金边举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-09/10728990.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月9日电 据外媒报道，当地时间9日，土耳其西部伊兹密尔一座钢铁厂发生爆炸并引发火灾，已致多名工人受伤。" data-title="突发：土耳其一钢铁厂发生爆炸 已致多名工人受伤" data-date="11-09 18:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 18:14</span>
          <span class="news-item-title">突发：土耳其一钢铁厂发生爆炸 已致多名工人受伤</span>
          <span class="news-value-point">💡 中新网11月9日电 据外媒报道，当地时间9日，土耳其西部伊兹密尔一座钢铁厂发生爆炸并引发火灾，已致多名工人受伤</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-09/10728962.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月9日电(魏晨曦)综合外媒报道，当地时间11月8日，美国总统特朗普在社交媒体“真实社交”上表示，针对伊朗的“铁门”特遣行动在伊朗全面展开。" data-title="特朗普宣布实施“铁门”行动：“几乎没有东西能进出伊朗！”伊朗否认并谴责" data-date="11-09 17:38" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 17:38</span>
          <span class="news-item-title">特朗普宣布实施“铁门”行动：“几乎没有东西能进出伊朗！”伊朗否认并谴责</span>
          <span class="news-value-point">💡 中新网11月9日电(魏晨曦)综合外媒报道，当地时间11月8日，美国总统特朗普在社交媒体“真实社交”上表示，针对伊朗的“铁门”特遣行动在伊朗全面展…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/08/us/politics/trump-60-minutes-republicans-election-immigration.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="总统在周日播出的“60分钟”采访中被问及他的驱逐政策是否走得太远。“我认为这可能太难了，”他说。" data-title="On ‘60 Minutes,’ Trump Says Immigration Crackdown May Have ‘Hurt’ Republicans in Elections" data-date="11-09 11:16" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-09 11:16</span>
          <span class="news-item-title">在“60分钟”中，特朗普表示，移民镇压可能会在选举中“伤害”共和党人</span>
          <span class="news-item-title-en">On ‘60 Minutes,’ Trump Says Immigration Crackdown May Have ‘Hurt’ Republicans in Elections</span>
          <span class="news-value-point">💡 总统在周日播出的“60分钟”采访中被问及他的驱逐政策是否走得太远</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1029990/jensen-huang-the-spy-who-loved-me" target="_blank" rel="noopener" data-cat="keji" data-summary="我希望这些人的性生活与我无关，但我想我们必须谈谈Jensen Huang和国家安全事件。谁能想到，在这里签奶的家伙可能没有很好的判断力" data-title="The future of AI hinges on… Jensen Huang’s sex life?" data-date="11-10 01:36" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-10 01:36</span>
          <span class="news-item-title">AI的未来取决于… Jensen Huang的性生活？</span>
          <span class="news-item-title-en">The future of AI hinges on… Jensen Huang’s sex life?</span>
          <span class="news-value-point">💡 我希望这些人的性生活与我无关，但我想我们必须谈谈Jensen Huang和国家安全事件</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/09/anthropic-joins-ais-natural-gas-frenzy-buys-3-4b-worth-of-turbines/" target="_blank" rel="noopener" data-cat="keji" data-summary="Anthropic购买了价值数十亿美元的天然气涡轮机，这笔交易可能会让买家后悔。" data-title="Anthropic joins AI’s natural gas frenzy, buys $3.4B worth of turbines" data-date="11-10 00:56" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-10 00:56</span>
          <span class="news-item-title">Anthropic加入AI的天然气狂潮，购买价值$ 3.4B的涡轮机</span>
          <span class="news-item-title-en">Anthropic joins AI’s natural gas frenzy, buys $3.4B worth of turbines</span>
          <span class="news-value-point">💡 Anthropic购买了价值数十亿美元的天然气涡轮机，这笔交易可能会让买家后悔</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/09/business/economy/nvidia-megaspeed-investigation-huang.html" target="_blank" rel="noopener" data-cat="keji" data-summary="在Nvidia的一名高管与商务部官员取得联系后，对购买高级Nvidia人工智能芯片的新加坡公司Megaspeed的调查被移交给了司法部。" data-title="U.S. Commerce Dept. Inquiry Into Megaspeed Was Halted After Nvidia Intervention" data-date="11-10 00:47" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-10 00:47</span>
          <span class="news-item-title">美国商务部对Megaspeed的调查在英伟达干预后停止</span>
          <span class="news-item-title-en">U.S. Commerce Dept. Inquiry Into Megaspeed Was Halted After Nvidia Intervention</span>
          <span class="news-value-point">💡 在Nvidia的一名高管与商务部官员取得联系后，对购买高级Nvidia人工智能芯片的新加坡公司Megaspeed的调查被移交给了司法部</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/09/business/nvidia-stock-price-jensen-huang-ceo.html" target="_blank" rel="noopener" data-cat="keji" data-summary="这家芯片制造商的规模和对人工智能贸易的重要性意味着，黄延森承认与一名涉嫌为中国从事间谍活动的女商人的关系可能会在华尔街引起反响。" data-title="Nvidia’s Stock Price Drops After Investigation Into CEO Jensen Huang" data-date="11-10 00:24" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-10 00:24</span>
          <span class="news-item-title">英伟达对首席执行官黄延森进行调查后股价下跌</span>
          <span class="news-item-title-en">Nvidia’s Stock Price Drops After Investigation Into CEO Jensen Huang</span>
          <span class="news-value-point">💡 这家芯片制造商的规模和对人工智能贸易的重要性意味着，黄延森承认与一名涉嫌为中国从事间谍活动的女商人的关系可能会在华尔街引起反响</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/09/mediums-new-tk-app-brings-ai-assistance-directly-into-the-writing-process/" target="_blank" rel="noopener" data-cat="keji" data-summary="Medium的新写作应用程序采用了人工智能辅助写作，尽管人们对该技术在出版中的作用越来越有争议。" data-title="Medium’s new TK app brings AI assistance directly into the writing process" data-date="11-10 00:12" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-10 00:12</span>
          <span class="news-item-title">Medium的新TK应用程序将AI辅助直接带入写作过程</span>
          <span class="news-item-title-en">Medium’s new TK app brings AI assistance directly into the writing process</span>
          <span class="news-value-point">💡 Medium的新写作应用程序采用了人工智能辅助写作，尽管人们对该技术在出版中的作用越来越有争议</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/big-tech/nvidia-ceo-jensen-huang-summoned-to-congressional-committee-over-affair-with-alleged-chinese-spy-says-recent-reports-raise-concerns-over-security-protocols-and-ties-to-chinese-intelligence" target="_blank" rel="noopener" data-cat="keji" data-summary="黄延森已被传唤到国会中共专责委员会出庭。" data-title="Nvidia CEO Jensen Huang summoned to Congress over affair with alleged Chinese spy" data-date="11-09 23:57" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-09 23:57</span>
          <span class="news-item-title">英伟达首席执行官黄延森因涉嫌与中国间谍有关的事件而被传唤到国会</span>
          <span class="news-item-title-en">Nvidia CEO Jensen Huang summoned to Congress over affair with alleged Chinese spy</span>
          <span class="news-value-point">💡 黄延森已被传唤到国会中共专责委员会出庭</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1029802/trump-60-minutes-ai" target="_blank" rel="noopener" data-cat="keji" data-summary="当被问及人工智能高管在60分钟内对其模型安全性的警告时，特朗普说： “我认为风险并不像他们所说的那样真实，我认为风险是可以管理的，而且是可以管理的。“他声称司法部正在管理" data-title="Trump’s 60 Minutes interview touched on AI safety, threat to arrest an AI exec" data-date="11-09 23:50" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-09 23:50</span>
          <span class="news-item-title">特朗普的60分钟采访涉及人工智能安全，威胁要逮捕一名人工智能高管</span>
          <span class="news-item-title-en">Trump’s 60 Minutes interview touched on AI safety, threat to arrest an AI exec</span>
          <span class="news-value-point">💡 当被问及人工智能高管在60分钟内对其模型安全性的警告时，特朗普说： “我认为风险并不像他们所说的那样真实，我认为风险是可以管理的，而且是可以管理…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/deepx-ai-chip-runs-so-cool-that-a-butter-heatsink-doesnt-melt-the-dx-m1-processor-impresses-in-a-bizarre-new-dairy-based-benchmark" target="_blank" rel="noopener" data-cat="keji" data-summary="DEEPX在一个奇怪的基于乳制品的热基准测试中展示了其DX-M1处理器的冷却运行能力。" data-title="Bizarre AI chip demo uses butter to highlight how new chip runs 40 degrees cooler than the competition" data-date="11-09 23:15" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-09 23:15</span>
          <span class="news-item-title">奇怪的人工智能芯片演示使用黄油来突出新芯片的运行温度比竞争对手低40度</span>
          <span class="news-item-title-en">Bizarre AI chip demo uses butter to highlight how new chip runs 40 degrees cooler than the competition</span>
          <span class="news-value-point">💡 DEEPX在一个奇怪的基于乳制品的热基准测试中展示了其DX-M1处理器的冷却运行能力</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/024/565.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 9 日消息，据《连线》报道，英伟达 CEO 黄仁勋早在承认婚外情之前一年，就已开始与一家擅长处理公众丑闻的危机公关公司合作。据两名知情人士透露，至少从 2025 年 10 月起，公关公司 Heller 就一直在幕后负责黄仁勋的相关公关事务。而就在今日，黄仁勋承认与一名女性存在婚外情。Heller 创始人丽莎 · 海勒（Risa Heller）在业内以处理权势人物的性不端指控及其他个人丑闻而闻名。根据《纽约杂志》2023 年的一篇人物报道，她曾为多位陷入争议的知名人士提供公关服务或咨询，包括美国前国会议员安东尼 · 韦纳（Anthony Weiner）、名厨马里奥 · 巴塔利（Mario Batali）以及作家杰弗里 · 图宾（Jeffrey Toobin）。当然，Hell" data-title="英伟达黄仁勋承认出轨，消息称其去年已聘请擅长处理丑闻的危机公关公司" data-date="11-09 23:14" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-09 23:14</span>
          <span class="news-item-title">英伟达黄仁勋承认出轨，消息称其去年已聘请擅长处理丑闻的危机公关公司</span>
          <span class="news-value-point">💡 IT之家 11 月 9 日消息，据《连线》报道，英伟达 CEO 黄仁勋早在承认婚外情之前一年，就已开始与一家擅长处理公众丑闻的危机公关公司合作</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/024/563.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 9 日消息，FEVM（奋微）今日正式展示了其 FNPH1 迷你主机。这一型号采用超薄设计，厚度约 2cm，体积仅 0.4L，质量 450g。IT之家注：FNPH1 实际版本与泄露版本存在差异，规格以实物为准。FNPH1 采用英特尔酷睿 Ultra X7 处理器 358H，支持选配 64GB LPDDR5X-9600 内存，配备 Wi-Fi 7 无线网卡，提供 2 个 USB4、10GbE + 2.5GbE RJ-45、OCuLink 在内的一系列接口。" data-title="FEVM 迷你主机 FNPH1 实物亮相：2cm 超薄，0.4L 体积" data-date="11-09 22:56" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-09 22:56</span>
          <span class="news-item-title">FEVM 迷你主机 FNPH1 实物亮相：2cm 超薄，0.4L 体积</span>
          <span class="news-value-point">💡 IT之家 11 月 9 日消息，FEVM（奋微）今日正式展示了其 FNPH1 迷你主机</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-pro-6000-users-cables-almost-melted-even-when-limited-to-500w-12v-2x6-cables-appear-to-still-cause-problems-show-clear-signs-of-melting" target="_blank" rel="noopener" data-cat="keji" data-summary="12V-2x6连接器几乎取出了两个RTX PRO 6000 Blackwell Workstation GPU ；幸运的是，业主在熔化GPU连接器之前发现了损坏的电缆。" data-title="Nvidia RTX PRO 6000 user’s cables almost melted, even when limited to 500W" data-date="11-09 22:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-09 22:00</span>
          <span class="news-item-title">Nvidia RTX PRO 6000用户电缆几乎熔化，即使限制在500W</span>
          <span class="news-item-title-en">Nvidia RTX PRO 6000 user’s cables almost melted, even when limited to 500W</span>
          <span class="news-value-point">💡 12V-2x6连接器几乎取出了两个RTX PRO 6000 Blackwell Workstation GPU</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/09/technology/jensen-huang-affair-nvidia.html" target="_blank" rel="noopener" data-cat="keji" data-summary="这位首席执行官对他的公司有着严格的控制权，这给英伟达的董事会提出了挑战，该董事会正在调查他与一名据信是中国间谍的女性的婚外情。" data-title="Is Jensen Huang Too Powerful to Be Punished by Nvidia?" data-date="11-09 21:54" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-09 21:54</span>
          <span class="news-item-title">Jensen Huang是否太强大而无法受到Nvidia的惩罚？</span>
          <span class="news-item-title-en">Is Jensen Huang Too Powerful to Be Punished by Nvidia?</span>
          <span class="news-value-point">💡 这位首席执行官对他的公司有着严格的控制权，这给英伟达的董事会提出了挑战，该董事会正在调查他与一名据信是中国间谍的女性的婚外情</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/anthropic-skips-six-year-waitlist-with-massive-usd3-4-billion-gas-turbine-generator-deal-firm-takes-over-onepwrs-orders-secures-1-7gw-of-capacity-to-power-ai-data-centers" target="_blank" rel="noopener" data-cat="keji" data-summary="Anthropic已承诺34亿美元从OnePWR Solutions获得1.7GW的燃气发电机，接管现有的Caterpillar订单，因为漫长的设备交付周期推动人工智能公司建立自己的电力基础设施" data-title="Anthropic skips six-year waitlist with massive $3.4 billion gas turbine generator deal" data-date="11-09 21:45" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-09 21:45</span>
          <span class="news-item-title">Anthropic跳过了六年的等待名单，获得了34亿美元的巨额燃气轮机发电机交易</span>
          <span class="news-item-title-en">Anthropic skips six-year waitlist with massive $3.4 billion gas turbine generator deal</span>
          <span class="news-value-point">💡 Anthropic已承诺34亿美元从OnePWR Solutions获得1.7GW的燃气发电机，接管现有的Caterpillar订单，因为漫长的…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/lawyer-builds-private-ai-server-with-eight-used-nvidia-v100-gpus-up-to-215-tokens-per-second-to-keep-legal-files-offline-costing-about-usd2-400-per-four-gpu-board" target="_blank" rel="noopener" data-cat="keji" data-summary="一位律师在八个二手2018年时代的Nvidia V100 GPU上运行DeepSeek V4.1 Flash ，最高可达215个令牌/秒，将案件文件保存在办公室中。" data-title="Lawyer builds private AI server with eight used Nvidia V100 GPUs" data-date="11-09 21:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-09 21:20</span>
          <span class="news-item-title">律师使用八个二手Nvidia V100显卡构建私有AI服务器</span>
          <span class="news-item-title-en">Lawyer builds private AI server with eight used Nvidia V100 GPUs</span>
          <span class="news-value-point">💡 一位律师在八个二手2018年时代的Nvidia V100 GPU上运行DeepSeek V4.1 Flash ，最高可达215个令牌/秒，将案件…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-09/10729111.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网北京11月9日电 (记者 孙自法)第七届智库科学与工程国际研讨会11月8日至10日在北京举行，记者从会上获悉，由中国科学院科技战略咨询研究院院长潘教峰研究员牵头发起的“从证据到方案：人工智能驱动的政策模拟与情景分析”研究计划，2026年成功入选联合国“2024—2033年科学促进可持续发展国际十年”。" data-title="中国学者发起人工智能赋能政策研究计划入选联合国科学议程" data-date="11-09 21:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 21:14</span>
          <span class="news-item-title">中国学者发起人工智能赋能政策研究计划入选联合国科学议程</span>
          <span class="news-value-point">💡 中新网北京11月9日电 (记者 孙自法)第七届智库科学与工程国际研讨会11月8日至10日在北京举行，记者从会上获悉，由中国科学院科技战略咨询研究…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13610315/michael-carrick-future-man-utd-will-not-rush-decision-over-head-coachs-tenure-despite-dropping-into-relegation-zone" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在4-4战平阿斯顿维拉之后，曼联的老板们不会急于就迈克尔卡里克的未来做出决定，这让他们处于降级区。" data-title="Man Utd will not rush decision on Carrick future" data-date="11-10 00:52" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 00:52</span>
          <span class="news-item-title">曼联不会急于决定卡里克的未来</span>
          <span class="news-item-title-en">Man Utd will not rush decision on Carrick future</span>
          <span class="news-value-point">💡 在4-4战平阿斯顿维拉之后，曼联的老板们不会急于就迈克尔卡里克的未来做出决定，这让他们处于降级区</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13610315/michael-carrick-future-man-utd-will-not-rush-decision-over-head-coachs-tenure-despite-dropping-into-relegation-zone" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在4-4战平阿斯顿维拉之后，曼联的老板们不会急于就迈克尔卡里克的未来做出决定，这让他们处于降级区。" data-title="Man Utd will not rush decision on Carrick future" data-date="11-10 00:52" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 00:52</span>
          <span class="news-item-title">曼联不会急于决定卡里克的未来</span>
          <span class="news-item-title-en">Man Utd will not rush decision on Carrick future</span>
          <span class="news-value-point">💡 在4-4战平阿斯顿维拉之后，曼联的老板们不会急于就迈克尔卡里克的未来做出决定，这让他们处于降级区</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/09/manchester-city-enzo-maresca-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在连续三场失利后，曼城的经理表示，他将利用国际休息时间重新评估。他们的问题可能不仅仅是战术在这里注册我们的免费通讯恩佐·马雷斯卡（ Enzo Maresca ）似乎对他周六击败诺特感到困惑" data-title="Manchester City’s weaknesses under Enzo Maresca are being exposed" data-date="11-10 00:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-10 00:30</span>
          <span class="news-item-title">曼城在恩佐·马雷斯卡（ Enzo Maresca ）领导下的弱点正在暴露</span>
          <span class="news-item-title-en">Manchester City’s weaknesses under Enzo Maresca are being exposed</span>
          <span class="news-value-point">💡 在连续三场失利后，曼城的经理表示，他将利用国际休息时间重新评估</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13610134/manchester-united-the-key-questions-with-michael-carricks-future-still-up-in-the-air-at-old-trafford" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在周日以4比4战平阿斯顿维拉之后，迈克尔·卡里克在曼联的未来仍然是一个谜。" data-title="What now for Man Utd and Carrick?" data-date="11-09 23:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-09 23:00</span>
          <span class="news-item-title">曼联和卡里克现在该怎么办？</span>
          <span class="news-item-title-en">What now for Man Utd and Carrick?</span>
          <span class="news-value-point">💡 在周日以4比4战平阿斯顿维拉之后，迈克尔·卡里克在曼联的未来仍然是一个谜</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13610134/manchester-united-the-key-questions-with-michael-carricks-future-still-up-in-the-air-at-old-trafford" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在周日以4比4战平阿斯顿维拉之后，迈克尔·卡里克在曼联的未来仍然是一个谜。" data-title="What now for Man Utd and Carrick?" data-date="11-09 23:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-09 23:00</span>
          <span class="news-item-title">曼联和卡里克现在该怎么办？</span>
          <span class="news-item-title-en">What now for Man Utd and Carrick?</span>
          <span class="news-value-point">💡 在周日以4比4战平阿斯顿维拉之后，迈克尔·卡里克在曼联的未来仍然是一个谜</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6n9r93dnr9do?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="本周末，英超联赛中几乎每场比赛都有一个有争议的VAR决定。但是，有多少可能会作为错误记录下来？" data-title="Incident-by-incident: Was it a bad weekend for VAR?" data-date="11-09 22:34" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-09 22:34</span>
          <span class="news-item-title">逐个事件：对于VAR来说，这是一个糟糕的周末吗？</span>
          <span class="news-item-title-en">Incident-by-incident: Was it a bad weekend for VAR?</span>
          <span class="news-value-point">💡 本周末，英超联赛中几乎每场比赛都有一个有争议的VAR决定</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/dram/memory-shortage-spurs-smartphone-makers-to-melt-used-memory-off-old-devices-then-re-solder-it-onto-new-products-recycled-memory-to-keep-budget-phones-affordable-reballing-adoption-to-double-by-2027" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="重新包装的内存目前只占智能手机组件的一小部分，但由于制造商正在寻找日益昂贵的DRAM的替代品，到2027年采用率可能会增加近一倍。" data-title="Memory shortage spurs smartphone makers to melt used memory off old devices, then re-solder it onto new products" data-date="11-09 21:40" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-09 21:40</span>
          <span class="news-item-title">内存短缺促使智能手机制造商融化旧设备的废旧内存，然后将其重新焊接到新产品上</span>
          <span class="news-item-title-en">Memory shortage spurs smartphone makers to melt used memory off old devices, then re-solder it onto new products</span>
          <span class="news-value-point">💡 重新包装的内存目前只占智能手机组件的一小部分，但由于制造商正在寻找日益昂贵的DRAM的替代品，到2027年采用率可能会增加近一倍</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025501/liverpool-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Liverpool latest: Szoboszlai undergoing tests after suffering knee issue at Palace" data-title="Liverpool latest: Szoboszlai undergoing tests after suffering knee issue at Palace" data-date="11-09 21:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-09 21:00</span>
          <span class="news-item-title">利物浦最新消息： Szoboszlai在宫殿遭受膝盖问题后接受测试</span>
          <span class="news-item-title-en">Liverpool latest: Szoboszlai undergoing tests after suffering knee issue at Palace</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c98rzr51rlvpo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="切尔西警告工作人员要小心通过幻想英超联赛透露球队新闻，因为Joao Pedro的伤势似乎在球队选择中被无意中透露。" data-title="Chelsea staff warned over Fantasy Premier League use" data-date="11-09 20:41" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-09 20:41</span>
          <span class="news-item-title">切尔西工作人员警告使用Fantasy Premier League</span>
          <span class="news-item-title-en">Chelsea staff warned over Fantasy Premier League use</span>
          <span class="news-value-point">💡 切尔西警告工作人员要小心通过幻想英超联赛透露球队新闻，因为Joao Pedro的伤势似乎在球队选择中被无意中透露</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13610181/alisson-liverpool-goalkeeper-wants-to-stay-at-anfield-beyond-contract-expiry-at-the-end-of-this-season" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦守门员阿利森表示，他希望在合同到期后的赛季结束后继续留在安菲尔德。" data-title="&#39;My will is to stay&#39; - Alisson wants new Liverpool contract" data-date="11-09 20:38" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-09 20:38</span>
          <span class="news-item-title">“我的意愿是留下来” - Alisson想要新的利物浦合同</span>
          <span class="news-item-title-en">'My will is to stay' - Alisson wants new Liverpool contract</span>
          <span class="news-value-point">💡 利物浦守门员阿利森表示，他希望在合同到期后的赛季结束后继续留在安菲尔德</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cw62ypepq2m7o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦守门员阿里森·贝克尔（ Alisson Becker ）希望在赛季结束后继续留在俱乐部，届时他目前的合同即将到期。" data-title="Alisson wants to sign new Liverpool contract" data-date="11-09 20:00" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-09 20:00</span>
          <span class="news-item-title">Alisson想与利物浦签订新合同</span>
          <span class="news-item-title-en">Alisson wants to sign new Liverpool contract</span>
          <span class="news-value-point">💡 利物浦守门员阿里森·贝克尔（ Alisson Becker ）希望在赛季结束后继续留在俱乐部，届时他目前的合同即将到期</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13610133/gary-neville" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="加里·内维尔（ Gary Neville ）质疑最近英超联赛对曼城的关注是否已经开始渗透到球队的表现中。" data-title="Neville: Is Man City charges spotlight seeping into performances?" data-date="11-09 19:55" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-09 19:55</span>
          <span class="news-item-title">内维尔：曼城的收费是否会让聚光灯渗透到表演中？</span>
          <span class="news-item-title-en">Neville: Is Man City charges spotlight seeping into performances?</span>
          <span class="news-value-point">💡 加里·内维尔（ Gary Neville ）质疑最近英超联赛对曼城的关注是否已经开始渗透到球队的表现中</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/rugby-league/news/12040/13610092/rugby-league-world-cup-england-wheelchair-ready-for-australia-showdown-as-defence-on-line-in-semi-finals" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="如果英格兰轮椅想要继续捍卫他们的橄榄球联赛世界杯冠军头衔，任务很简单：在自己的后院的半决赛中击败澳大利亚。" data-title="England Wheelchair ready for Australia showdown in RLWC semis" data-date="11-09 17:38" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-09 17:38</span>
          <span class="news-item-title">英格兰轮椅为澳大利亚RLWC半决赛摊牌做好准备</span>
          <span class="news-item-title-en">England Wheelchair ready for Australia showdown in RLWC semis</span>
          <span class="news-value-point">💡 如果英格兰轮椅想要继续捍卫他们的橄榄球联赛世界杯冠军头衔，任务很简单：在自己的后院的半决赛中击败澳大利亚</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/09/premier-league-10-talking-points-weekend-action" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="德拉普的才华重新浮现，戈麦斯用更多的烟花和埃弗顿的拔毛混乱来取悦布莱顿奥利弗·格拉斯纳很容易对利亚姆·德拉普失去耐心。前锋还只有23岁，但他" data-title="Premier League: 10 talking points from the weekend’s action" data-date="11-09 16:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-09 16:00</span>
          <span class="news-item-title">英超联赛：周末行动的10个谈话要点</span>
          <span class="news-item-title-en">Premier League: 10 talking points from the weekend’s action</span>
          <span class="news-value-point">💡 德拉普的才华重新浮现，戈麦斯用更多的烟花和埃弗顿的拔毛混乱来取悦布莱顿奥利弗·格拉斯纳很容易对利亚姆·德拉普失去耐心</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cked3qjw1q4xo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="这是老特拉福德的英超经典，但曼联与阿斯顿维拉的4-4平局对迈克尔卡里克的未来做了什么？" data-title="Bizarre &amp; thrilling theatre as Carrick in limbo with Man Utd in drop zone" data-date="11-09 05:50" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-09 05:50</span>
          <span class="news-item-title">奇异而惊心动魄的剧院之旅：卡里克（ Carrick ）与曼联（ Man Utd ）在坠落区</span>
          <span class="news-item-title-en">Bizarre & thrilling theatre as Carrick in limbo with Man Utd in drop zone</span>
          <span class="news-value-point">💡 这是老特拉福德的英超经典，但曼联与阿斯顿维拉的4-4平局对迈克尔卡里克的未来做了什么</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theverge.com/entertainment/1030022/james-gunn-peter-safran-dc-studios-out-leaving" target="_blank" rel="noopener" data-cat="zonghe" data-summary="很快， James Gunn和Peter Safran将不再领导Skydance的DC工作室。在2022年担任DC Studios联合首席执行官后， Gunn和Safran将被前漫威制作和开发高级副总裁Jeremy Latcham所取代，他是Deadline的代表" data-title="James Gunn is out as DC movie leader" data-date="11-10 01:39" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-10 01:39</span>
          <span class="news-item-title">詹姆斯·冈恩（ James Gunn ）出任DC电影</span>
          <span class="news-item-title-en">James Gunn is out as DC movie leader</span>
          <span class="news-value-point">💡 很快， James Gunn和Peter Safran将不再领导Skydance的DC工作室</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cw8dzd17n70no/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这名科技业亿万富豪高层陷入一场涉及私人生活与国家安全的丑闻。" data-title="黄仁勋与疑似中国间谍婚外情：目前我们知道什么？" data-date="11-10 01:25" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-10 01:25</span>
          <span class="news-item-title">黄仁勋与疑似中国间谍婚外情：目前我们知道什么？</span>
          <span class="news-value-point">💡 这名科技业亿万富豪高层陷入一场涉及私人生活与国家安全的丑闻</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13610309/fifpro-world-11-ballon-dor-winner-harry-kane-not-voted-by-fellow-professionals-to-be-named-in-team-of-the-year" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Ballon d &#39;Or冠军Harry Kane尚未在FIFPRO World 11中被提名。" data-title="Ballon d&#39;Or winner Kane not named in FIFPRO World 11" data-date="11-10 01:10" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 01:10</span>
          <span class="news-item-title">Ballon d 'Or冠军Kane未入选FIFPRO World 11</span>
          <span class="news-item-title-en">Ballon d'Or winner Kane not named in FIFPRO World 11</span>
          <span class="news-value-point">💡 Ballon d 'Or冠军Harry Kane尚未在FIFPRO World 11中被提名</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/transportation/1029776/uber-parking-launch-spothero-robotaxis" target="_blank" rel="noopener" data-cat="zonghe" data-summary="优步宣布推出优步停车功能，这是一项原生应用内预约功能，可让合作车主提前查找、预订并支付车库和停车位费用。这项新功能是优步最近收购SpotHero的结果，整合了" data-title="Uber wants to park your car now, too" data-date="11-10 01:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-10 01:00</span>
          <span class="news-item-title">优步也想立即为您停车</span>
          <span class="news-item-title-en">Uber wants to park your car now, too</span>
          <span class="news-value-point">💡 优步宣布推出优步停车功能，这是一项原生应用内预约功能，可让合作车主提前查找、预订并支付车库和停车位费用</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/09/science/american-diabetes-association-turmoil.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="它始于美国糖尿病协会会议上的抗议。现在，由此产生的抵制导致了科学发展的放缓，看不到尽头。" data-title="An Anti-Trump Protest. Police Threats. Inside a Rift in Diabetes Research." data-date="11-10 00:41" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-10 00:41</span>
          <span class="news-item-title">反特朗普抗议。警方威胁。糖尿病研究的裂痕之内。</span>
          <span class="news-item-title-en">An Anti-Trump Protest. Police Threats. Inside a Rift in Diabetes Research.</span>
          <span class="news-value-point">💡 它始于美国糖尿病协会会议上的抗议</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/news/1029822/sony-playstation-portal-japan-model-additional-storage" target="_blank" rel="noopener" data-cat="zonghe" data-summary="索尼将于下个月在日本独家推出新版PlayStation Portal。更新后的型号将以我们以前见过的午夜黑色选项推出，并将包括“额外”的内部存储，以实现未来的功能。" data-title="Sony’s new PlayStation Portal handheld includes ‘additional’ internal storage" data-date="11-10 00:23" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-10 00:23</span>
          <span class="news-item-title">索尼新款PlayStation Portal手持设备包含“额外”内部存储空间</span>
          <span class="news-item-title-en">Sony’s new PlayStation Portal handheld includes ‘additional’ internal storage</span>
          <span class="news-value-point">💡 索尼将于下个月在日本独家推出新版PlayStation Portal</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/darts/news/12040/13610177/grand-slam-of-darts-2026-luke-littler-grouped-with-beau-greaves-as-he-looks-to-defend-title-in-wolverhampton" target="_blank" rel="noopener" data-cat="zonghe" data-summary="2026年飞镖大满贯的抽签由Luke Littler与Beau Greaves和Niels Zonneveld一起进行，组成了一个令人垂涎欲滴的A组。" data-title="Grand Slam of Darts 2026: Littler alongside Greaves in mouth" data-date="11-10 00:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 00:00</span>
          <span class="news-item-title">2026年飞镖大满贯： Littler与护腿并肩</span>
          <span class="news-item-title-en">Grand Slam of Darts 2026: Littler alongside Greaves in mouth</span>
          <span class="news-value-point">💡 2026年飞镖大满贯的抽签由Luke Littler与Beau Greaves和Niels Zonneveld一起进行，组成了一个令人垂涎欲滴的…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/024/566.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 9 日消息，备受瞩目的《GTA6》PS5 版现已在亚太地区（GMT+8 区域）开启预载，而 XBOX Series X|S 版将于格林尼治标准时间 11 月 10 日 00:00（对应北京时间 8:00）开始预载，盒装兑换码版本预计将于 11 月 12 日起在各大零售商销售。IT之家经实际测试，PS5 版游戏预载文件体积为 209.758GB，下载速度因网络而异，整体下载时间在 3-5 小时不等。随着游戏开启下载，玩家也能够在 PS5 首页听到《GTA6》背景音乐，这段音乐采用了舒缓的合成器曲风，带有浓厚的 20 世纪 80 年代复古气息。这与此前《GTA 6》宣传素材中出现的音乐风格相吻合，包括游戏预告片以及 Extended Look（加长版预览视频）开头和结尾使用的" data-title="《GTA 6》PS5 版正式开启预载，XBOX Series X｜S 需等到北京时间早上 8 点" data-date="11-09 23:59" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-09 23:59</span>
          <span class="news-item-title">《GTA 6》PS5 版正式开启预载，XBOX Series X｜S 需等到北京时间早上 8 点</span>
          <span class="news-value-point">💡 IT之家 11 月 9 日消息，备受瞩目的《GTA6》PS5 版现已在亚太地区（GMT+8 区域）开启预载，而 XBOX Series X|S …</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1029773/disney-adobe-generative-ai-partnership" target="_blank" rel="noopener" data-cat="zonghe" data-summary="华特迪士尼公司已与Adobe合作开发专有的“艺术家主导”生成式人工智能模型，以支持迪士尼的生产管道。今天在Adobe的MAX大会上宣布了为期多年的合作伙伴关系，它将看到Adobe providin" data-title="Disney and Adobe are building generative AI tools together" data-date="11-09 23:38" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-09 23:38</span>
          <span class="news-item-title">迪士尼和Adobe正在共同构建生成式人工智能工具</span>
          <span class="news-item-title-en">Disney and Adobe are building generative AI tools together</span>
          <span class="news-value-point">💡 华特迪士尼公司已与Adobe合作开发专有的“艺术家主导”生成式人工智能模型，以支持迪士尼的生产管道</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/podcast/1029684/riaa-mitch-glazier-napster-ai-labels-music" target="_blank" rel="noopener" data-cat="zonghe" data-summary="今天，我与RIAA首席执行官兼主席Mitch Glazier进行了交谈。这次谈话对我来说是一个真正的全圆时刻：当Napster上大学时， RIAA因为起诉孩子下载音乐而成为每个人的反派。" data-title="Hold up — I had a great time talking to the RIAA guy" data-date="11-09 23:30" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-09 23:30</span>
          <span class="news-item-title">等一下，我和RIAA的人聊得很开心</span>
          <span class="news-item-title-en">Hold up — I had a great time talking to the RIAA guy</span>
          <span class="news-value-point">💡 今天，我与RIAA首席执行官兼主席Mitch Glazier进行了交谈</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1029676/medium-tk-notes-app" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Medium有史以来第一次不仅仅是一个博客平台。该公司正在推出一款名为TK的新应用程序，该应用程序将笔记和日记与类似于私人社交网络的东西相结合。该应用旨在让您" data-title="Medium is launching a new note-taking app called TK" data-date="11-09 23:04" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-09 23:04</span>
          <span class="news-item-title">Medium正在推出一款名为TK的新笔记应用程序</span>
          <span class="news-item-title-en">Medium is launching a new note-taking app called TK</span>
          <span class="news-value-point">💡 Medium有史以来第一次不仅仅是一个博客平台</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/024/561.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 9 日消息，小鹏汽车官微今天宣布，小鹏 GX 成为第七届世界媒体峰会的智驾用车，在北京为世界各大通讯社及全球权威媒体提供出行服务。随后，小鹏创始人何小鹏转发有关微博并发文：希望明年能够成为第一个在欧洲上线智能辅助驾驶的中国品牌，让更多全球朋友在不同区域都能体验到。今年 10 月，小鹏汽车通用智能中心负责人刘先明接受彭博社采访时透露，该公司成功在约两周时间内，将智驾系统从一个欧洲国家微调适配到另一个欧洲国家。据悉，小鹏目前正与欧洲监管机构紧密沟通，并维持 2027 年在欧洲正式落地智能导航辅助驾驶系统（NGP）的原定规划。刘先明强调，小鹏汽车致力于将全功能版智驾系统带入欧洲，而非妥协推出“阉割版”。除基础的车道保持与自适应巡航外，该技术能应对复杂的城市与高速路况，涵盖交通标" data-title="何小鹏：希望小鹏明年能成为第一个在欧洲上线智能辅助驾驶的中国品牌" data-date="11-09 22:46" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-09 22:46</span>
          <span class="news-item-title">何小鹏：希望小鹏明年能成为第一个在欧洲上线智能辅助驾驶的中国品牌</span>
          <span class="news-value-point">💡 IT之家 11 月 9 日消息，小鹏汽车官微今天宣布，小鹏 GX 成为第七届世界媒体峰会的智驾用车，在北京为世界各大通讯社及全球权威媒体提供出行…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/024/560.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 9 日消息，AOC 旗下“U32U4”31.5 英寸显示器现已在京东发售，该机主打 4K 120Hz QD-OLED，定价为 6499 元。京东 AOC“U32U4”显示器 6499 元直达链接该机配备一块 3840x2160 分辨率 120Hz QD-OLED Penta Tandem 五层堆栈面板，峰值亮度 1000 尼特，对比度 150 万:1，GtG 响应速度 0.03ms，显示器支持原生 10-Bit 色彩，覆盖 99% DCI-P3 色域。该机内置双 5W 扬声器，显示器支架支持升降 / 倾斜 / 旋转，提供 HDMI 2.1、DP 1.4、USB-C 96W、USB-C 15W 等接口。IT之家附显示器参数：京东 11.11 无门槛红包 面额至高 26888" data-title="AOC“U32U4”31.5 英寸显示器发售：4K 120Hz QD-OLED Penta Tandem 五层堆栈面板 + 双扬，6499 元" data-date="11-09 22:38" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-09 22:38</span>
          <span class="news-item-title">AOC“U32U4”31.5 英寸显示器发售：4K 120Hz QD-OLED Penta Tandem 五层堆栈面板 + 双扬，6499 元</span>
          <span class="news-value-point">💡 IT之家 11 月 9 日消息，AOC 旗下“U32U4”31.5 英寸显示器现已在京东发售，该机主打 4K 120Hz QD-OLED，定价为…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/024/558.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 9 日消息，微软现已对 Microsoft Store 微软商店《我的世界》PC 版（Minecraft：Java &amp; Bedrock Edition for PC）进行涨价，国区起售价从 89 元涨至 110.99 元，IT之家附游戏商品页（https://www.xbox.com/zh-CN/games/store/minecraft-java-bedrock-edition-for-pc/9NXP44L49SHJ）。标准版：89 元 ↗ 110.99 元（+24.7%）豪华版：286 元 ↗ 304.99 元（+6.6%）终极版：358 元 ↗ 380.99 元（+6.4%）公开信息显示，《我的世界》由瑞典游戏公司 Mojang Studios 开发，微软于 201" data-title="微软商店 Microsoft Store《我的世界》PC 版游戏涨价，国区 89 元起 → 110.99 元起" data-date="11-09 22:26" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-09 22:26</span>
          <span class="news-item-title">微软商店 Microsoft Store《我的世界》PC 版游戏涨价，国区 89 元起 → 110.99 元起</span>
          <span class="news-value-point">💡 IT之家 11 月 9 日消息，微软现已对 Microsoft Store 微软商店《我的世界》PC 版（Minecraft：Java & Be…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-09/10729148.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社北京11月9日电 题：送别翻译家谢莹莹：明亮的生命之歌将永远回响" data-title="送别翻译家谢莹莹：明亮的生命之歌将永远回响" data-date="11-09 22:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-09 22:14</span>
          <span class="news-item-title">送别翻译家谢莹莹：明亮的生命之歌将永远回响</span>
          <span class="news-value-point">💡 中新社北京11月9日电 题：送别翻译家谢莹莹：明亮的生命之歌将永远回响</span>
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


<p class="news-updated">🕐 抓取更新于 2026-11-10 01:43（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
