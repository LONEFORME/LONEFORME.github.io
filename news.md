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
      <span>2026-11-10 06:34 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×13 · 天空体育×12</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gj/2026/11-10/10729169.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="土耳其总统埃尔多安9日晚表示，当天伊兹密尔省阿利亚阿区一家钢铁厂发生的爆炸事故已造成16人死亡，13人受伤，其中2人伤势严重。" data-title="土耳其西部一钢铁厂发生爆炸 死亡人数升至16人" data-date="11-10 05:57" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 11-10 05:57</span>
      </div>
      <h2 class="hero-featured-title">土耳其西部一钢铁厂发生爆炸 死亡人数升至16人</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://techcrunch.com/2026/11/09/the-race-is-on-to-sue-nvidia/" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达董事会对Jensen Huang与一名中国间谍嫌疑人的关系展开调查后，英伟达股价下跌超过4% ，一名证券法专家表示，该公司早些时候坚持认为这一切都是“正常的” ，这可能会变成一个" data-title="The race is on to sue Nvidia" data-date="11-10 06:23" data-source="TechCrunch">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
      </div>
      <p class="hero-sub-title">The race is on to sue Nvidia</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/cw4g1g7z2mdgo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联董事会尚未对迈克尔·卡里克的未来做出最终决定，尽管这是俱乐部40年来最糟糕的一场比赛。" data-title="Man Utd yet to make decision on Carrick&#39;s future" data-date="11-10 01:49" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">Man Utd yet to make decision on Carrick's future</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/gj/2026/11-10/10729167.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="当地时间11月9日，塞内加尔有关部门当天公布的最新搜救情况显示，该国北部卢加大区凯贝梅尔省附近海域发生的沉船事故已造成39人死亡，目前仅发现一名幸存者，搜救工作仍在继续。" data-title="塞内加尔北部沉船事故死亡人数升至39人" data-date="11-10 05:55" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">塞内加尔北部沉船事故死亡人数升至39人</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-10/10729169.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="土耳其总统埃尔多安9日晚表示，当天伊兹密尔省阿利亚阿区一家钢铁厂发生的爆炸事故已造成16人死亡，13人受伤，其中2人伤势严重。" data-title="土耳其西部一钢铁厂发生爆炸 死亡人数升至16人" data-date="11-10 05:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 05:57</span>
          <span class="news-item-title">土耳其西部一钢铁厂发生爆炸 死亡人数升至16人</span>
          <span class="news-value-point">💡 土耳其总统埃尔多安9日晚表示，当天伊兹密尔省阿利亚阿区一家钢铁厂发生的爆炸事故已造成16人死亡，13人受伤，其中2人伤势严重</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-10/10729168.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间11月9日，坦桑尼亚警方表示，当天在该国伊林加省，一辆客车与一辆卡车相撞，造成至少21人死亡、5人受伤。" data-title="坦桑尼亚一客车与卡车相撞致21人死亡" data-date="11-10 05:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 05:56</span>
          <span class="news-item-title">坦桑尼亚一客车与卡车相撞致21人死亡</span>
          <span class="news-value-point">💡 当地时间11月9日，坦桑尼亚警方表示，当天在该国伊林加省，一辆客车与一辆卡车相撞，造成至少21人死亡、5人受伤</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-10/10729166.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间11月9日，美国肯塔基州共和党籍联邦众议员托马斯·梅西向众议院提交决议，试图推动全院就弹劾国防部长皮特·赫格塞思进行表决。此举意在向共和党同僚施压，要求他们就是否罢免特朗普政府中最引人注目的人物之一作出抉择。此前，共和党在选举中遭遇全面失利。" data-title="美众议员向众议院提交决议 要求弹劾国防部长赫格塞思" data-date="11-10 05:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 05:54</span>
          <span class="news-item-title">美众议员向众议院提交决议 要求弹劾国防部长赫格塞思</span>
          <span class="news-value-point">💡 当地时间11月9日，美国肯塔基州共和党籍联邦众议员托马斯·梅西向众议院提交决议，试图推动全院就弹劾国防部长皮特·赫格塞思进行表决</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-10/10729165.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="美国总统特朗普11月9日在其社交媒体上发帖，质疑美国中期选举，但没有提供证据支持。" data-title="特朗普质疑美国中期选举结果 称提前投票数据异常" data-date="11-10 05:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 05:53</span>
          <span class="news-item-title">特朗普质疑美国中期选举结果 称提前投票数据异常</span>
          <span class="news-value-point">💡 美国总统特朗普11月9日在其社交媒体上发帖，质疑美国中期选举，但没有提供证据支持</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-10/10729164.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间11月9日，美国财政部发布数据称，在截至9月30日的2026财年，美国联邦预算赤字总额为2.0万亿美元，较上一财年的赤字增加了2170亿美元，增幅为12%。" data-title="美国2026财年联邦预算赤字达2万亿美元" data-date="11-10 05:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 05:50</span>
          <span class="news-item-title">美国2026财年联邦预算赤字达2万亿美元</span>
          <span class="news-value-point">💡 当地时间11月9日，美国财政部发布数据称，在截至9月30日的2026财年，美国联邦预算赤字总额为2.0万亿美元，较上一财年的赤字增加了2170亿…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-10/10729163.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间11月9日，俄罗斯常驻联合国代表涅边贾当天在联合国安理会乌克兰问题会议上说，俄方不接受“冻结”乌克兰冲突，这种方案将使俄罗斯面临的现有安全威胁继续存在并为新一轮冲突升级创造条件。俄方这一立场“坚定不移”。" data-title="俄常驻联合国代表称不接受“冻结”乌克兰冲突" data-date="11-10 05:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 05:49</span>
          <span class="news-item-title">俄常驻联合国代表称不接受“冻结”乌克兰冲突</span>
          <span class="news-value-point">💡 当地时间11月9日，俄罗斯常驻联合国代表涅边贾当天在联合国安理会乌克兰问题会议上说，俄方不接受“冻结”乌克兰冲突，这种方案将使俄罗斯面临的现有安…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-10/10729162.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间9日，埃及总检察院下令成立一个由开罗大学工程学院教授组成的委员会，负责审查埃及国家铁路的运营系统以及设备、人员监控和信号系统的安全与运营状况。同时，由总检察院人员组成的事故调查小组前往事故现场进行实地调查，并对相关责任人展开询问。调查显示，多方在这起列车相撞事故中存在玩忽职守行为。" data-title="埃及列车相撞死伤超百人 调查显示多方存在玩忽职守" data-date="11-10 05:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 05:48</span>
          <span class="news-item-title">埃及列车相撞死伤超百人 调查显示多方存在玩忽职守</span>
          <span class="news-value-point">💡 当地时间9日，埃及总检察院下令成立一个由开罗大学工程学院教授组成的委员会，负责审查埃及国家铁路的运营系统以及设备、人员监控和信号系统的安全与运营…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/09/us/hegseth-impeachment-massie.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="肯塔基州共和党众议员托马斯·马西（ Thomas Massie ）发起了一项必须在两天内进行的投票。" data-title="Thomas Massie Moves to Force Vote on Impeaching Pete Hegseth" data-date="11-10 05:11" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-10 05:11</span>
          <span class="news-item-title">托马斯·马西（ Thomas Massie ）动议对弹劾皮特·赫格塞斯（ Pete Hegseth</span>
          <span class="news-item-title-en">Thomas Massie Moves to Force Vote on Impeaching Pete Hegseth</span>
          <span class="news-value-point">💡 肯塔基州共和党众议员托马斯·马西（ Thomas Massie ）发起了一项必须在两天内进行的投票</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/09/us/politics/trump-election-fraud-rigging-midterms.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="特朗普总统最初表示他将接受中期结果，但他再次毫无根据地声称投票被操纵。" data-title="Trump Veers Back Into Claims of Rigged Election, Questioning Midterm Results" data-date="11-10 02:37" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-10 02:37</span>
          <span class="news-item-title">特朗普转而声称选举被操纵，质疑中期结果</span>
          <span class="news-item-title-en">Trump Veers Back Into Claims of Rigged Election, Questioning Midterm Results</span>
          <span class="news-value-point">💡 特朗普总统最初表示他将接受中期结果，但他再次毫无根据地声称投票被操纵</span>
        </a>
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
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://techcrunch.com/2026/11/09/the-race-is-on-to-sue-nvidia/" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达董事会对Jensen Huang与一名中国间谍嫌疑人的关系展开调查后，英伟达股价下跌超过4% ，一名证券法专家表示，该公司早些时候坚持认为这一切都是“正常的” ，这可能会变成一个" data-title="The race is on to sue Nvidia" data-date="11-10 06:23" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-10 06:23</span>
          <span class="news-item-title">起诉英伟达的竞赛即将开始</span>
          <span class="news-item-title-en">The race is on to sue Nvidia</span>
          <span class="news-value-point">💡 英伟达董事会对Jensen Huang与一名中国间谍嫌疑人的关系展开调查后，英伟达股价下跌超过4% ，一名证券法专家表示，该公司早些时候坚持认为…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/09/business/nvidia-stock-price-jensen-huang-ceo.html" target="_blank" rel="noopener" data-cat="keji" data-summary="在首席执行官黄延森(Jensen Huang)承认与一名涉嫌为中国从事间谍活动的女商人发生关系后，这家芯片制造商的股价大幅下跌。" data-title="Nvidia’s Stock Price Drops After Investigation Into CEO Jensen Huang" data-date="11-10 05:23" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-10 05:23</span>
          <span class="news-item-title">英伟达对首席执行官黄延森进行调查后股价下跌</span>
          <span class="news-item-title-en">Nvidia’s Stock Price Drops After Investigation Into CEO Jensen Huang</span>
          <span class="news-value-point">💡 在首席执行官黄延森(Jensen Huang)承认与一名涉嫌为中国从事间谍活动的女商人发生关系后，这家芯片制造商的股价大幅下跌</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/science/1030252/ai-data-center-climate-pledge-united-nations-cop31" target="_blank" rel="noopener" data-cat="keji" data-summary="在这一点上，阅读最新的引人注目的使用人工智能造福环境的承诺，感觉就像喝了一杯不含酒精的啤酒。诚然，我从一开始就怀疑。这怎么可能好呢？但我喜欢啤酒和我们的星球，足以给" data-title="The global pledge to use AI for climate good is a cruel joke" data-date="11-10 05:13" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-10 05:13</span>
          <span class="news-item-title">全球承诺将人工智能用于气候公益是一个残酷的笑话</span>
          <span class="news-item-title-en">The global pledge to use AI for climate good is a cruel joke</span>
          <span class="news-value-point">💡 在这一点上，阅读最新的引人注目的使用人工智能造福环境的承诺，感觉就像喝了一杯不含酒精的啤酒</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/09/us/politics/democrats-trump-ai-nvidia.html" target="_blank" rel="noopener" data-cat="keji" data-summary="在英伟达(Nvidia)调查其首席执行官与一名中国间谍嫌疑人的婚外情时，国会领导人在一封信中提出了担忧。" data-title="Democrats Demand Answers on Trump’s A.I. Policy Amid Spy Plot" data-date="11-10 04:10" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-10 04:10</span>
          <span class="news-item-title">民主党人要求在间谍阴谋中回答特朗普的人工智能政策</span>
          <span class="news-item-title-en">Democrats Demand Answers on Trump’s A.I. Policy Amid Spy Plot</span>
          <span class="news-value-point">💡 在英伟达(Nvidia)调查其首席执行官与一名中国间谍嫌疑人的婚外情时，国会领导人在一封信中提出了担忧</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/09/jensen-huang-pulls-out-of-elevenlabs-summit-amid-nvidia-controversy/" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达首席执行官早些时候也退出了人类活动。" data-title="Jensen Huang pulls out of ElevenLabs Summit amid Nvidia controversy" data-date="11-10 04:09" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-10 04:09</span>
          <span class="news-item-title">在英伟达争议中， Jensen Huang退出ElevenLabs峰会</span>
          <span class="news-item-title-en">Jensen Huang pulls out of ElevenLabs Summit amid Nvidia controversy</span>
          <span class="news-value-point">💡 英伟达首席执行官早些时候也退出了人类活动</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/09/anthropic-releases-new-mythos-and-fable-models-amid-rsi-concerns/" target="_blank" rel="noopener" data-cat="keji" data-summary="Anthropic表示，新模型“显示了编码、推理和视觉等领域的改进” ，以及与用户进行更清晰的沟通。" data-title="Anthropic releases new Mythos and Fable models amid RSI concerns" data-date="11-10 03:24" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-10 03:24</span>
          <span class="news-item-title">由于RSI的担忧， Anthropic发布了新的Mythos和Fable模型</span>
          <span class="news-item-title-en">Anthropic releases new Mythos and Fable models amid RSI concerns</span>
          <span class="news-value-point">💡 Anthropic表示，新模型“显示了编码、推理和视觉等领域的改进” ，以及与用户进行更清晰的沟通</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1030084/apple-intelligence-usage-packs-ai-features-creator-studio-logic-pro" target="_blank" rel="noopener" data-cat="keji" data-summary="在9月初发布了一篇概述某些Apple Intelligence功能使用限制的支持文章之后，该公司更新了Logic Pro ，提供了一次性购买价格为$ 49.99的“购买更多使用”选项，正如9to5Mac所发现的那样。它" data-title="Apple’s $50 Intelligence Usage Packs extend access to some AI features" data-date="11-10 03:09" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-10 03:09</span>
          <span class="news-item-title">Apple的$ 50智能使用包扩展了对某些人工智能功能的访问权限</span>
          <span class="news-item-title-en">Apple’s $50 Intelligence Usage Packs extend access to some AI features</span>
          <span class="news-value-point">💡 在9月初发布了一篇概述某些Apple Intelligence功能使用限制的支持文章之后，该公司更新了Logic Pro ，提供了一次性购买价格…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1030005/anthropic-claude-fable-mythos-5-2" target="_blank" rel="noopener" data-cat="keji" data-summary="Anthropic今天宣布推出两款新机型： Claude Fable 5.2和Claude Mythos 5.2 ，据称它们旨在应对“令人生畏”的技术挑战。该公司声称，新型号在编码、推理和愿景方面有所改进，可以" data-title="Anthropic launches new Claude Fable and Mythos 5.2 models" data-date="11-10 03:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-10 03:00</span>
          <span class="news-item-title">Anthropic推出全新Claude Fable和Mythos 5.2车型</span>
          <span class="news-item-title-en">Anthropic launches new Claude Fable and Mythos 5.2 models</span>
          <span class="news-value-point">💡 Anthropic今天宣布推出两款新机型： Claude Fable 5.2和Claude Mythos 5.2 ，据称它们旨在应对“令人生畏”…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/09/business/economy/nvidia-megaspeed-investigation-huang.html" target="_blank" rel="noopener" data-cat="keji" data-summary="在Nvidia的一名高管与商务部官员取得联系后，对购买高级Nvidia人工智能芯片的新加坡公司Megaspeed的调查被移交给了司法部。" data-title="U.S. Commerce Dept. Inquiry Into Megaspeed Was Halted After Nvidia Intervention" data-date="11-10 02:38" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-10 02:38</span>
          <span class="news-item-title">美国商务部对Megaspeed的调查在英伟达干预后停止</span>
          <span class="news-item-title-en">U.S. Commerce Dept. Inquiry Into Megaspeed Was Halted After Nvidia Intervention</span>
          <span class="news-value-point">💡 在Nvidia的一名高管与商务部官员取得联系后，对购买高级Nvidia人工智能芯片的新加坡公司Megaspeed的调查被移交给了司法部</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/09/jensen-huangs-affair-with-alleged-chinese-spy-puts-nvidias-china-ambitions-under-scrutiny/" target="_blank" rel="noopener" data-cat="keji" data-summary="Jensen Huang涉嫌与一名涉嫌中国间谍发生关系，这可能会使英伟达放松美国芯片出口限制并保持进入中国利润丰厚的人工智能市场的游说努力复杂化。" data-title="Jensen Huang’s affair with alleged Chinese spy puts Nvidia’s China ambitions under scrutiny" data-date="11-10 02:09" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-10 02:09</span>
          <span class="news-item-title">黄延森与涉嫌中国间谍的婚外情使英伟达的中国野心受到严格审查</span>
          <span class="news-item-title-en">Jensen Huang’s affair with alleged Chinese spy puts Nvidia’s China ambitions under scrutiny</span>
          <span class="news-value-point">💡 Jensen Huang涉嫌与一名涉嫌中国间谍发生关系，这可能会使英伟达放松美国芯片出口限制并保持进入中国利润丰厚的人工智能市场的游说努力复杂化</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/09/technology/jensen-huang-nvidia-ai-chips-scandal.html" target="_blank" rel="noopener" data-cat="keji" data-summary="随着芯片成为人工智能的重要组成部分，英伟达的Jensen Huang等高管看到他们的个人财富和个人资料以前所未有的方式飙升。" data-title="A.I. Fueled Nvidia CEO Jensen Huang’s Elite Status, but Scandal Followed" data-date="11-10 01:58" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-10 01:58</span>
          <span class="news-item-title">人工智能推动了英伟达首席执行官黄延森的精英地位，但丑闻随之而来</span>
          <span class="news-item-title-en">A.I. Fueled Nvidia CEO Jensen Huang’s Elite Status, but Scandal Followed</span>
          <span class="news-value-point">💡 随着芯片成为人工智能的重要组成部分，英伟达的Jensen Huang等高管看到他们的个人财富和个人资料以前所未有的方式飙升</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/policy/nvidia-cracks-down-on-overseas-cloud-ai-gpu-rentals-for-china-partners-face-51-percent-non-chinese-quota-as-black-market-b300-rack-prices-surge-to-usd2-8-million" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达可能会将云合作伙伴的中国业务限制在49% ，因为中国公司购买了100多万个游戏和工作站GPU。" data-title="Nvidia cracks down on overseas cloud AI GPU rentals for China" data-date="11-10 01:48" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-10 01:48</span>
          <span class="news-item-title">英伟达严厉打击中国海外云AI GPU租赁</span>
          <span class="news-item-title-en">Nvidia cracks down on overseas cloud AI GPU rentals for China</span>
          <span class="news-value-point">💡 英伟达可能会将云合作伙伴的中国业务限制在49% ，因为中国公司购买了100多万个游戏和工作站GPU</span>
        </a>
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
        <a class="news-item" href="https://techcrunch.com/2026/11/09/mediums-new-tk-app-brings-ai-assistance-directly-into-the-writing-process/" target="_blank" rel="noopener" data-cat="keji" data-summary="Medium的新写作应用程序采用了人工智能辅助写作，尽管人们对该技术在出版中的作用越来越有争议。" data-title="Medium’s new TK app brings AI assistance directly into the writing process" data-date="11-10 00:12" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-10 00:12</span>
          <span class="news-item-title">Medium的新TK应用程序将AI辅助直接带入写作过程</span>
          <span class="news-item-title-en">Medium’s new TK app brings AI assistance directly into the writing process</span>
          <span class="news-value-point">💡 Medium的新写作应用程序采用了人工智能辅助写作，尽管人们对该技术在出版中的作用越来越有争议</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cw4g1g7z2mdgo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联董事会尚未对迈克尔·卡里克的未来做出最终决定，尽管这是俱乐部40年来最糟糕的一场比赛。" data-title="Man Utd yet to make decision on Carrick&#39;s future" data-date="11-10 01:49" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-10 01:49</span>
          <span class="news-item-title">曼联尚未就卡里克的未来做出决定</span>
          <span class="news-item-title-en">Man Utd yet to make decision on Carrick's future</span>
          <span class="news-value-point">💡 曼联董事会尚未对迈克尔·卡里克的未来做出最终决定，尽管这是俱乐部40年来最糟糕的一场比赛</span>
        </a>
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
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13610134/manchester-united-the-key-questions-with-michael-carricks-future-still-up-in-the-air-at-old-trafford" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在周日以4比4战平阿斯顿维拉之后，迈克尔·卡里克在曼联的未来仍然是一个谜。" data-title="The key questions for Man Utd and Carrick after history" data-date="11-09 23:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-09 23:00</span>
          <span class="news-item-title">曼联和卡里克历史上的关键问题</span>
          <span class="news-item-title-en">The key questions for Man Utd and Carrick after history</span>
          <span class="news-value-point">💡 在周日以4比4战平阿斯顿维拉之后，迈克尔·卡里克在曼联的未来仍然是一个谜</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13610134/manchester-united-the-key-questions-with-michael-carricks-future-still-up-in-the-air-at-old-trafford" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在周日以4比4战平阿斯顿维拉之后，迈克尔·卡里克在曼联的未来仍然是一个谜。" data-title="What now for Man Utd and Carrick?" data-date="11-09 23:00" data-source="天空体育">
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
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025501/liverpool-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Liverpool latest: Van Dijk pulls out of Netherlands squad" data-title="Liverpool latest: Van Dijk pulls out of Netherlands squad" data-date="11-09 21:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-09 21:00</span>
          <span class="news-item-title">利物浦最新消息：范迪克退出荷兰队</span>
          <span class="news-item-title-en">Liverpool latest: Van Dijk pulls out of Netherlands squad</span>
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
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-10/10729167.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="当地时间11月9日，塞内加尔有关部门当天公布的最新搜救情况显示，该国北部卢加大区凯贝梅尔省附近海域发生的沉船事故已造成39人死亡，目前仅发现一名幸存者，搜救工作仍在继续。" data-title="塞内加尔北部沉船事故死亡人数升至39人" data-date="11-10 05:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 05:55</span>
          <span class="news-item-title">塞内加尔北部沉船事故死亡人数升至39人</span>
          <span class="news-value-point">💡 当地时间11月9日，塞内加尔有关部门当天公布的最新搜救情况显示，该国北部卢加大区凯贝梅尔省附近海域发生的沉船事故已造成39人死亡，目前仅发现一名…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1030262/msi-mag-272qp-qd-oled-x24-monitor-woot-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="您可以对PC游戏设置进行的最佳升级之一是OLED显示器。幸运的是， MSI出厂翻新的MAG 272QP X24在Woot上销售至11月18日，制造商保修期为180天，价格为290.99美元，超过10美元" data-title="MSI’s refurbished QD-OLED gaming monitor is on sale for under $300" data-date="11-10 05:43" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-10 05:43</span>
          <span class="news-item-title">微星翻新的QD-OLED游戏显示器售价不到300 $</span>
          <span class="news-item-title-en">MSI’s refurbished QD-OLED gaming monitor is on sale for under $300</span>
          <span class="news-value-point">💡 您可以对PC游戏设置进行的最佳升级之一是OLED显示器</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13610387/tom-brady-leaves-birmingham-nfl-legend-and-minority-owner-makes-shock-departure-after-three-years" target="_blank" rel="noopener" data-cat="zonghe" data-summary="伯明翰宣布， NFL传奇人物汤姆·布雷迪（ Tom Brady ）作为少数族裔老板震惊地离开， Bluenoses坐在冠军桌的顶端。" data-title="Birmingham announce shock Brady departure" data-date="11-10 05:26" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 05:26</span>
          <span class="news-item-title">伯明翰宣布震惊布雷迪离开</span>
          <span class="news-item-title-en">Birmingham announce shock Brady departure</span>
          <span class="news-value-point">💡 伯明翰宣布， NFL传奇人物汤姆·布雷迪（ Tom Brady ）作为少数族裔老板震惊地离开， Bluenoses坐在冠军桌的顶端</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/tennis/news/12040/13610366/wta-finals-aryna-sabalenka-battles-past-karolina-muchova-in-her-opening-match-at-indian-wells" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Aryna Sabalenka在印第安维尔斯的WTA总决赛中取得了胜利，在周一第2组的首场比赛中以7-6 (7-2) 7-5战胜了Karolina Muchova。" data-title="Sabalenka starts pursuit of WTA Finals title with opening win" data-date="11-10 04:19" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 04:19</span>
          <span class="news-item-title">Sabalenka以首场胜利开始追求WTA总决赛冠军</span>
          <span class="news-item-title-en">Sabalenka starts pursuit of WTA Finals title with opening win</span>
          <span class="news-value-point">💡 Aryna Sabalenka在印第安维尔斯的WTA总决赛中取得了胜利，在周一第2组的首场比赛中以7-6 (7-2) 7-5战胜了Karolin…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/09/magazine/congress-trump-oversight-investigations-presidency.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="历史告诉我们，如果运用得当，宪法监督可以是一个强有力的工具。" data-title="Congress Has Reined In the Presidency Before. Here’s How to Do It." data-date="11-10 03:22" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-10 03:22</span>
          <span class="news-item-title">国会此前曾控制过总统职位。以下是操作方法。</span>
          <span class="news-item-title-en">Congress Has Reined In the Presidency Before. Here’s How to Do It.</span>
          <span class="news-value-point">💡 历史告诉我们，如果运用得当，宪法监督可以是一个强有力的工具</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/cryptocurrency/ethereum-foundation-sued-after-firing-employee-over-mandatory-source-seppuku-suicide-pact-crypto-firm-demanded-employees-pledge-to-take-their-own-lives-with-a-sword-to-protect-open-source-code-founder-vitalik-claims-1-000-year-mandate-just-artwork" target="_blank" rel="noopener" data-cat="zonghe" data-summary="以太坊基金会的一名前雇员因拒绝签署“Source Seppuku许可证”而被解雇后，正在起诉该非营利组织。" data-title="Ethereum Foundation sued after firing employee over mandatory &#39;Source Seppuku&#39; suicide pact" data-date="11-10 02:43" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-10 02:43</span>
          <span class="news-item-title">以太坊基金会因强制性“Source Seppuku”自杀协议而解雇员工后提起诉讼</span>
          <span class="news-item-title-en">Ethereum Foundation sued after firing employee over mandatory 'Source Seppuku' suicide pact</span>
          <span class="news-value-point">💡 以太坊基金会的一名前雇员因拒绝签署“Source Seppuku许可证”而被解雇后，正在起诉该非营利组织</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1029998/game-pass-ultimate-three-months-lego-pokemon-pikachu-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="去年， Xbox Game Pass Ultimate的价格在每月20美元至30美元之间波动，但您可以以每月约19美元的价格获得三个月的顶级套餐。在Newegg ，结账时使用优惠券代码BNWF2656可节省11美元" data-title="You can grab three months of Game Pass Ultimate for under $20 per month" data-date="11-10 02:35" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-10 02:35</span>
          <span class="news-item-title">您可以每月不到$ 20获取三个月的终极游戏通行证</span>
          <span class="news-item-title-en">You can grab three months of Game Pass Ultimate for under $20 per month</span>
          <span class="news-value-point">💡 去年， Xbox Game Pass Ultimate的价格在每月20美元至30美元之间波动，但您可以以每月约19美元的价格获得三个月的顶级套餐</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1030061/instagram-ai-effect-builder-filters" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在上周将其编辑应用程序扩展到macOS之后， Instagram的下一步是推出此效果生成器，它可以使用AI为您的故事帖子生成自定义过滤器。它现在适用于18岁以上的美国居民，有一个提示框用于描述" data-title="Instagram’s Effect Builder makes new filters from AI prompts" data-date="11-10 02:07" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-10 02:07</span>
          <span class="news-item-title">Instagram的效果生成器根据人工智能提示制作新的过滤器</span>
          <span class="news-item-title-en">Instagram’s Effect Builder makes new filters from AI prompts</span>
          <span class="news-value-point">💡 在上周将其编辑应用程序扩展到macOS之后， Instagram的下一步是推出此效果生成器，它可以使用AI为您的故事帖子生成自定义过滤器</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/09/meta-releases-muse-ember-a-new-lightweight-model-for-agent-execution/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Ember以每百万个输入代币10美分的价格，比Haiku和Luna等前沿竞争对手便宜得多。" data-title="Meta releases Muse Ember, a new lightweight model for agent execution" data-date="11-10 02:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-10 02:00</span>
          <span class="news-item-title">Meta发布Muse Ember ，一种新的轻量级代理执行模型</span>
          <span class="news-item-title-en">Meta releases Muse Ember, a new lightweight model for agent execution</span>
          <span class="news-value-point">💡 Ember以每百万个输入代币10美分的价格，比Haiku和Luna等前沿竞争对手便宜得多</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/rugby-union/news/12040/13610326/nations-championship-englands-immanuel-feyi-waboso-and-tom-curry-ruled-out-of-rest-of-tournament" target="_blank" rel="noopener" data-cat="zonghe" data-summary="英格兰队将没有伊曼纽尔·费伊-瓦博索（ Immanuel Feyi-Waboso ）和汤姆·库里（ Tom Curry ）参加他们的国家锦标赛的剩余比赛，因为两名球员" data-title="England duo ruled out of rest of Nations Championship" data-date="11-10 02:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 02:00</span>
          <span class="news-item-title">英格兰二人组被排除在国家锦标赛之外</span>
          <span class="news-item-title-en">England duo ruled out of rest of Nations Championship</span>
          <span class="news-value-point">💡 英格兰队将没有伊曼纽尔·费伊-瓦博索（ Immanuel Feyi-Waboso ）和汤姆·库里（ Tom Curry ）参加他们的国家锦标赛的…</span>
        </a>
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


<p class="news-updated">🕐 抓取更新于 2026-11-10 06:34（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
