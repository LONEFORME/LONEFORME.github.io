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
      <span>2026-11-19 00:39 抓取更新</span>
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
        <span class="channel-count">55</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('shizheng', this)">
        <span>🏛️ 时政与国际</span>
        <span class="channel-count">14</span>
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
  <div class="ov-item"><span class="ov-num">55</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">4</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">天空体育×15 · 中国新闻网×10</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">按来源聚合 · 最近 24 小时精选</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.nytimes.com/2026/11/18/us/politics/hakeem-jeffries-speaker-of-the-house-democrats.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="经过投票，纽约州众议员哈基姆·杰弗里斯有望成为首位赢得总统继任第二顺位职位的黑人议员。" data-title="Democrats Nominate Hakeem Jeffries for Speaker of the House, Making History" data-date="11-19 00:10" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 11-19 00:10</span>
      </div>
      <h2 class="hero-featured-title">民主党提名哈基姆·杰弗里斯为众议院议长，创造历史</h2>
      <div class="hero-featured-title-en">Democrats Nominate Hakeem Jeffries for Speaker of the House, Making History</div>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://techcrunch.com/2026/11/18/openai-ceo-sam-altman-says-its-hard-to-imagine-the-ai-industry-without-jensen/" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达创始人兼前首席执行官黄仁勋上周因多起丑闻而辞职，其中包括与一名涉嫌为中国间谍的女子有染。" data-title="OpenAI CEO Sam Altman says it’s ‘hard to imagine the AI industry without Jensen’" data-date="11-19 00:14" data-source="TechCrunch">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
      </div>
      <p class="hero-sub-title">OpenAI首席执行官萨姆·阿尔特曼表示，“很难想象没有黄仁勋的AI行业”。</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/cj3vgp36z063o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英超联赛将于周六恢复，水晶宫、桑德兰和曼联目前处于降级区。但现在担心还为时过早吗？" data-title="The tightest survival scrap for years? Why it&#39;s not too early to worry" data-date="11-19 00:09" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">多年来最激烈的保级大战？为什么现在担心并不为时过早</p>
    </a>
    <a class="hero-sub-card" href="https://www.theverge.com/tech/1036494/shelly-neo-smart-home-water-valve-sensor-shut-off" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Shelly 今年早些时候推出了售价 28 美元的漏水传感器，该传感器使用电池供电，可轻松运行两年。现在，Shelly 又宣布推出一款配套的智能阀门，您可以将其安装在家中的主水管上，当其中一个传感器检测到漏水时，该阀门会自动关闭水流。" data-title="Shelly’s new smart valve shuts off your home’s water before a leak becomes a flood" data-date="11-19 00:00" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">在漏水演变成洪灾之前，Shelly的新款智能阀门会关闭您家中的水源</p>
    </a>
  </div>
</div>
<div class="news-grid">
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🏛️</span>
      <span class="news-category-title">时政要闻 & 国际动态</span>
      <span class="news-category-count">14 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/11/18/us/politics/hakeem-jeffries-speaker-of-the-house-democrats.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="经过投票，纽约州众议员哈基姆·杰弗里斯有望成为首位赢得总统继任第二顺位职位的黑人议员。" data-title="Democrats Nominate Hakeem Jeffries for Speaker of the House, Making History" data-date="11-19 00:10" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-19 00:10</span>
          <span class="news-item-title">民主党提名哈基姆·杰弗里斯为众议院议长，创造历史</span>
          <span class="news-item-title-en">Democrats Nominate Hakeem Jeffries for Speaker of the House, Making History</span>
          <span class="news-value-point">💡 经过投票，纽约州众议员哈基姆·杰弗里斯有望成为首位赢得总统继任第二顺位职位的黑人议员</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-19/10734432.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月19日电 (记者 孙自法)直立人是生存年代最长的古人类物种之一，已知在约190万年到10.8万年前分布在整个非洲到欧亚大陆东部。不过，由于此前中国特别是华南地区相关化石记录存在空白，成为古人类演化关键谜题之一，备受关注。" data-title="中国广西新发现直立人化石 将助力破解古人类演化关键谜题" data-date="11-19 00:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-19 00:07</span>
          <span class="news-item-title">中国广西新发现直立人化石 将助力破解古人类演化关键谜题</span>
          <span class="news-value-point">💡 中新网北京11月19日电 (记者 孙自法)直立人是生存年代最长的古人类物种之一，已知在约190万年到10.8万年前分布在整个非洲到欧亚大陆东部</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-18/10734423.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="去餐馆吃家乡菜、进小店给本国车厘子、龙虾“带货”、到大学演讲、和学生互动……" data-title="到大学演讲、给车厘子“带货”、打卡家乡菜……各国领导人在深圳忙不停" data-date="11-18 22:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 22:55</span>
          <span class="news-item-title">到大学演讲、给车厘子“带货”、打卡家乡菜……各国领导人在深圳忙不停</span>
          <span class="news-value-point">💡 去餐馆吃家乡菜、进小店给本国车厘子、龙虾“带货”、到大学演讲、和学生互动……</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-18/10734415.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社深圳11月18日电 (记者 黄钰钦)11月18日晚，中国国家主席习近平和夫人彭丽媛在深圳国际交流中心举行宴会，欢迎出席亚太经合组织第三十三次领导人非正式会议的来宾。" data-title="（深圳APEC）详讯：习近平和彭丽媛为出席亚太经合组织第三十三次领导人非正式会议的来宾举行欢迎宴会" data-date="11-18 22:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 22:42</span>
          <span class="news-item-title">（深圳APEC）详讯：习近平和彭丽媛为出席亚太经合组织第三十三次领导人非正式会议的来宾举行欢迎宴会</span>
          <span class="news-value-point">💡 中新社深圳11月18日电 (记者 黄钰钦)11月18日晚，中国国家主席习近平和夫人彭丽媛在深圳国际交流中心举行宴会，欢迎出席亚太经合组织第三十三…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-18/10734419.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网云南大理11月18日电 (记者 韩帅南)记者18日从大理州委宣传部获悉，近日，在云南省大理白族自治州成立70周年之际，一封跨越重洋的贺信从南半球传来。澳大利亚米尔迪拉市市长海伦·希利议员致信，向大理州送上祝贺。" data-title="从墨累河畔到苍山洱海：一封越洋贺信里的大理开放故事" data-date="11-18 22:38" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 22:38</span>
          <span class="news-item-title">从墨累河畔到苍山洱海：一封越洋贺信里的大理开放故事</span>
          <span class="news-value-point">💡 中新网云南大理11月18日电 (记者 韩帅南)记者18日从大理州委宣传部获悉，近日，在云南省大理白族自治州成立70周年之际，一封跨越重洋的贺信从…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-18/10734411.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="11月18日晚，国家主席习近平和夫人彭丽媛在深圳国际交流中心举行宴会，欢迎出席亚太经合组织第三十三次领导人非正式会议的来宾。习近平在祝酒辞中说——" data-title="习近平：看五十年的中国就来深圳" data-date="11-18 22:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 22:33</span>
          <span class="news-item-title">习近平：看五十年的中国就来深圳</span>
          <span class="news-value-point">💡 11月18日晚，国家主席习近平和夫人彭丽媛在深圳国际交流中心举行宴会，欢迎出席亚太经合组织第三十三次领导人非正式会议的来宾</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-18/10734403.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="11月18日晚，国家主席习近平和夫人彭丽媛在深圳国际交流中心举行宴会，欢迎出席亚太经合组织第三十三次领导人非正式会议的来宾。习近平发表祝酒辞指出——" data-title="【和合共生】习言道丨为了建设亚太共同体，我们跨越山海走到一起" data-date="11-18 22:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 22:32</span>
          <span class="news-item-title">【和合共生】习言道丨为了建设亚太共同体，我们跨越山海走到一起</span>
          <span class="news-value-point">💡 11月18日晚，国家主席习近平和夫人彭丽媛在深圳国际交流中心举行宴会，欢迎出席亚太经合组织第三十三次领导人非正式会议的来宾</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-18/10734405.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="11月18日晚，国家主席习近平和夫人彭丽媛在深圳国际交流中心举行宴会，欢迎出席亚太经合组织第三十三次领导人非正式会议的来宾。" data-title="新华图讯丨习近平和彭丽媛为出席亚太经合组织第三十三次领导人非正式会议的来宾举行欢迎宴会" data-date="11-18 22:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 22:31</span>
          <span class="news-item-title">新华图讯丨习近平和彭丽媛为出席亚太经合组织第三十三次领导人非正式会议的来宾举行欢迎宴会</span>
          <span class="news-value-point">💡 11月18日晚，国家主席习近平和夫人彭丽媛在深圳国际交流中心举行宴会，欢迎出席亚太经合组织第三十三次领导人非正式会议的来宾</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-18/10734388.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社深圳11月18日电 (记者 尹倩芸)11月18日，在深圳举行的2026年亚太经合组织(APEC)工商领导人峰会开幕式上，中国向全球工商界发出一份合作“邀请函”。" data-title="（深圳APEC）中国向全球工商界发出合作“邀请函”" data-date="11-18 22:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 22:30</span>
          <span class="news-item-title">（深圳APEC）中国向全球工商界发出合作“邀请函”</span>
          <span class="news-value-point">💡 中新社深圳11月18日电 (记者 尹倩芸)11月18日，在深圳举行的2026年亚太经合组织(APEC)工商领导人峰会开幕式上，中国向全球工商界发…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cjy5xkw9g1zpo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="这是中国自1980年以来，首次有最高领导人亲赴机场迎接外国元首。1980年前，华国锋、毛泽东都有多次赴机场迎接外国领袖的历史。" data-title="APEC深圳峰会：习近平亲赴机场迎接特朗普，46年来首次中国元首接机" data-date="11-18 21:21" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-18 21:21</span>
          <span class="news-item-title">APEC深圳峰会：习近平亲赴机场迎接特朗普，46年来首次中国元首接机</span>
          <span class="news-value-point">💡 这是中国自1980年以来，首次有最高领导人亲赴机场迎接外国元首</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-18/10734335.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网布里斯班11月18日电 (记者 薄雯雯)中昆“旅游+”对话会17日在澳大利亚昆士兰州首府布里斯班举行。与会嘉宾围绕中国与昆士兰州在旅游、教育、体育等领域的合作展开交流。" data-title="中国驻布里斯班总领馆举办中昆“旅游+”对话会" data-date="11-18 20:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 20:33</span>
          <span class="news-item-title">中国驻布里斯班总领馆举办中昆“旅游+”对话会</span>
          <span class="news-value-point">💡 中新网布里斯班11月18日电 (记者 薄雯雯)中昆“旅游+”对话会17日在澳大利亚昆士兰州首府布里斯班举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-18/10734268.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月18日电 阿布扎比消息：当地时间18日，阿联酋阿布扎比国家石油公司旗下的物流与服务公司表示，该公司一艘船只17日晚途经霍尔木兹海峡时遭到袭击，造成11人受伤、1人失踪。" data-title="阿联酋方面称一船只在霍尔木兹海峡遇袭  致11人伤、1人失踪" data-date="11-18 18:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-18 18:53</span>
          <span class="news-item-title">阿联酋方面称一船只在霍尔木兹海峡遇袭  致11人伤、1人失踪</span>
          <span class="news-value-point">💡 中新社北京11月18日电 阿布扎比消息：当地时间18日，阿联酋阿布扎比国家石油公司旗下的物流与服务公司表示，该公司一艘船只17日晚途经霍尔木兹海…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/18/world/asia/trump-imelda-marcos.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="菲律宾总统表示，特朗普总统和菲律宾前第一夫人彼此非常熟悉。" data-title="Trump Briefly Met an Old Friend in Manila: Imelda Marcos" data-date="11-18 17:52" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-18 17:52</span>
          <span class="news-item-title">特朗普在马尼拉与老友伊梅尔达·马科斯短暂会面</span>
          <span class="news-item-title-en">Trump Briefly Met an Old Friend in Manila: Imelda Marcos</span>
          <span class="news-value-point">💡 菲律宾总统表示，特朗普总统和菲律宾前第一夫人彼此非常熟悉</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cqn0dy4ppxp7o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="麒麟山庄离APEC主会场约30分钟车程，三面环山、一面临水，封闭性和安保条件都很好。它也与习近平的父亲习仲勋有渊源，还接待过已故朝鲜领导人金正日。" data-title="美中俄峰会：为何选在深圳麒麟山庄？习仲勋、金正日都曾下榻" data-date="11-18 16:06" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-18 16:06</span>
          <span class="news-item-title">美中俄峰会：为何选在深圳麒麟山庄？习仲勋、金正日都曾下榻</span>
          <span class="news-value-point">💡 麒麟山庄离APEC主会场约30分钟车程，三面环山、一面临水，封闭性和安保条件都很好</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://techcrunch.com/2026/11/18/openai-ceo-sam-altman-says-its-hard-to-imagine-the-ai-industry-without-jensen/" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达创始人兼前首席执行官黄仁勋上周因多起丑闻而辞职，其中包括与一名涉嫌为中国间谍的女子有染。" data-title="OpenAI CEO Sam Altman says it’s ‘hard to imagine the AI industry without Jensen’" data-date="11-19 00:14" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-19 00:14</span>
          <span class="news-item-title">OpenAI首席执行官萨姆·阿尔特曼表示，“很难想象没有黄仁勋的AI行业”。</span>
          <span class="news-item-title-en">OpenAI CEO Sam Altman says it’s ‘hard to imagine the AI industry without Jensen’</span>
          <span class="news-value-point">💡 英伟达创始人兼前首席执行官黄仁勋上周因多起丑闻而辞职，其中包括与一名涉嫌为中国间谍的女子有染</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/console-gaming/gta-vi-runs-at-1440p-on-ps5-and-xbox-series-x-but-just-720p-with-upscaling-on-series-s-rockstar-details-upscaling-technologies-for-launch" target="_blank" rel="noopener" data-cat="keji" data-summary="《GTA VI》将在PlayStation和Xbox主机上以30FPS为目标帧率，Rockstar将在PS5和Xbox Series X上使用其自研的时间抗锯齿解决方案，在PS5 Pro上使用索尼的PSSR 2，在Xbox Series S上使用AMD的FSR 4。" data-title="GTA VI runs at 1440p on PS5 and Xbox Series X, but just 720p with upscaling on Series S" data-date="11-19 00:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-19 00:00</span>
          <span class="news-item-title">《GTA VI》在PS5和Xbox Series X上以1440p运行，但在Series S上仅以720p运行并进行上采样。</span>
          <span class="news-item-title-en">GTA VI runs at 1440p on PS5 and Xbox Series X, but just 720p with upscaling on Series S</span>
          <span class="news-value-point">💡 《GTA VI》将在PlayStation和Xbox主机上以30FPS为目标帧率，Rockstar将在PS5和Xbox Series X上使用其…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1036549/nvidia-amd-earnings-fall-2026-chips-pause-frontier-models" target="_blank" rel="noopener" data-cat="keji" data-summary="今年夏天，OpenAI的AI代理意外黑进了Hugging Face，且早期证据表明其下一代模型能够独立发现并利用安全漏洞，因此OpenAI暂停了其计划中规模最大的前沿训练。9月，Anthropic首席执行官" data-title="Remember the frontier AI pause? Chip companies don’t either" data-date="11-18 23:44" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-18 23:44</span>
          <span class="news-item-title">还记得尖端人工智能暂停吗？芯片公司也不记得了</span>
          <span class="news-item-title-en">Remember the frontier AI pause? Chip companies don’t either</span>
          <span class="news-value-point">💡 今年夏天，OpenAI的AI代理意外黑进了Hugging Face，且早期证据表明其下一代模型能够独立发现并利用安全漏洞，因此OpenAI暂停了…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/029/121.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 18 日消息，北京时间今天（18 日）晚间，据美国 CNBC 援引知情人士消息称，Anthropic 考虑扩大 IPO 发行规模，并可能将发行价定在远高于 80 美元（IT之家注：现汇率约合 534.4 元人民币）的水平。当地时间 17 日，Anthropic 结束了认购意向征集，汇总了投资者需求，为登陆纳斯达克做准备。知情人士称，机构投资者的认购意向总额约为 4,000 亿美元（现汇率约合 2.67 万亿元人民币），散户认购意向也接近 1,000 亿美元（现汇率约合 6,679.86 亿元人民币）。不过，这些认购意向并不具有约束力，发行方案仍可能调整。知情人士透露，Anthropic 将在当地时间 18 日下午作出最终决定，预计在当天美股收盘后敲定 IPO 发行价。An" data-title="消息称 Anthropic 考虑扩大 IPO 规模，散户认购意向接近千亿美元" data-date="11-18 23:35" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-18 23:35</span>
          <span class="news-item-title">消息称 Anthropic 考虑扩大 IPO 规模，散户认购意向接近千亿美元</span>
          <span class="news-value-point">💡 IT之家 11 月 18 日消息，北京时间今天（18 日）晚间，据美国 CNBC 援引知情人士消息称，Anthropic 考虑扩大 IPO 发行…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/leaked-ohio-bill-could-allow-ai-data-center-companies-to-seize-private-land-for-their-buildouts-using-eminent-domain-law-proposed-law-would-expand-list-of-beneficiaries" target="_blank" rel="noopener" data-cat="keji" data-summary="一份泄露的俄亥俄州法案可能允许数据中心被认定为公共事业，以适用征用权法，从而使公司能够征用私人土地来建造新设施。" data-title="Leaked Ohio bill could allow AI data center companies to seize private land for their buildouts using eminent domain law" data-date="11-18 23:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-18 23:30</span>
          <span class="news-item-title">一份泄露的俄亥俄州法案显示，人工智能数据中心公司可能利用征用权法为其扩建项目征用私人土地。</span>
          <span class="news-item-title-en">Leaked Ohio bill could allow AI data center companies to seize private land for their buildouts using eminent domain law</span>
          <span class="news-value-point">💡 一份泄露的俄亥俄州法案可能允许数据中心被认定为公共事业，以适用征用权法，从而使公司能够征用私人土地来建造新设施</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/18/business/hospitals-java-artificial-intelligence.html" target="_blank" rel="noopener" data-cat="keji" data-summary="人工智能正在加剧医疗卫生系统所面临的威胁，这些系统多年来一直受到黑客的攻击。" data-title="Hospitals Rush to Patch Java Vulnerabilities" data-date="11-18 23:27" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-18 23:27</span>
          <span class="news-item-title">医院争相修补Java漏洞</span>
          <span class="news-item-title-en">Hospitals Rush to Patch Java Vulnerabilities</span>
          <span class="news-value-point">💡 人工智能正在加剧医疗卫生系统所面临的威胁，这些系统多年来一直受到黑客的攻击</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/029/117.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 18 日消息，据蓝鲸汽车从哈啰方面确认，哈啰 Robotaxi 近期完成了一轮内部组织架构调整。原智能车-模型开发、系统方案与评测以及 AI Infra-数据平台等相关团队被整合成立“模型开发与数据闭环部”，由哈啰 CEO 杨磊直接负责。这一部门下设模型开发部与数据闭环部。与此同时，AI 原生车、二代车和量产工程交付的相关业务由 CTO 于乾坤负责。智能车其余部门架构及汇报线保持不变。此前，哈啰 Robotaxi 传出核心算法人才加盟的消息。哈啰方面确认，此前任职于具身智能公司无界动力的李一贤，目前确实已加入了哈啰 Robotaxi。据IT之家此前报道，2025 年 6 月，哈啰宣布进军 Robotaxi 赛道，由哈啰、蚂蚁集团、宁德时代通过旗下投资主体共同发起成立的“造" data-title="哈啰调整 Robotaxi 组织架构：整合成立“模型开发与数据闭环部”，由 CEO 杨磊直接负责" data-date="11-18 23:15" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-18 23:15</span>
          <span class="news-item-title">哈啰调整 Robotaxi 组织架构：整合成立“模型开发与数据闭环部”，由 CEO 杨磊直接负责</span>
          <span class="news-value-point">💡 IT之家 11 月 18 日消息，据蓝鲸汽车从哈啰方面确认，哈啰 Robotaxi 近期完成了一轮内部组织架构调整</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/029/116.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 18 日消息，SpaceX CEO 埃隆 · 马斯克出人意料地透露，公司在业务预测中并未考虑来自 OpenAI 的任何收入。此前，OpenAI CEO 萨姆 · 奥尔特曼谈及半导体行业可能重复计算 AI 芯片需求的问题。两人长期以来一直在 OpenAI 的发展定位上存在分歧。奥尔特曼暗示市场可能存在一定程度的产能过剩，马斯克的回应则表明，他认为 AI 应用的市场需求依然强劲。SpaceX 今年早些时候上市时披露，除建设地面数据中心外，公司还计划部署太空算力卫星星座，进军算力基础设施市场。此前，奥尔特曼曾指出，数据中心建设和算力需求可能存在上限，未必能够消化芯片厂商计划提供的全部产能。对此，马斯克 17 日晚间在 X 上作出尖锐回应，如果 OpenAI 的产品无法带动算力需" data-title="马斯克“怒怼”奥尔特曼：SpaceX 预计不会从 OpenAI 处获得任何收入" data-date="11-18 23:09" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-18 23:09</span>
          <span class="news-item-title">马斯克“怒怼”奥尔特曼：SpaceX 预计不会从 OpenAI 处获得任何收入</span>
          <span class="news-value-point">💡 IT之家 11 月 18 日消息，SpaceX CEO 埃隆 · 马斯克出人意料地透露，公司在业务预测中并未考虑来自 OpenAI 的任何收入</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/cpus/nvidia-says-its-absurd-to-assume-it-predicted-the-agentic-moment-during-veras-development-product-intuition-helped-drive-cpu-design-superior-memory-bandwidth-will-play-critical-role-in-future-ai-agents-cpu-boss-claims" target="_blank" rel="noopener" data-cat="keji" data-summary="AMD批评英伟达（在较小程度上也批评Arm）声称要打造一款专为智能体AI设计的CPU。英伟达对这种说法提出反驳，而是表示Vera的设计基于“基本原则、产品直觉，以及通常" data-title="Nvidia says it’s ‘absurd’ to assume it predicted the agentic moment during Vera’s development" data-date="11-18 23:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-18 23:00</span>
          <span class="news-item-title">Nvidia 表示，认为其在 Vera 的开发过程中预测到了“智能体时刻”是“荒谬的”</span>
          <span class="news-item-title-en">Nvidia says it’s ‘absurd’ to assume it predicted the agentic moment during Vera’s development</span>
          <span class="news-value-point">💡 AMD批评英伟达（在较小程度上也批评Arm）声称要打造一款专为智能体AI设计的CPU</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/elon-musks-spacexai-suffers-chemical-spill-at-mississippi-ai-data-center-up-to-6-000-gallons-of-propylene-glycol-heat-transfer-fluid-lost-environment-agency-says-no-threat-to-residents" target="_blank" rel="noopener" data-cat="keji" data-summary="5,000 至 6,000 加仑的丙二醇从密西西比州绍瑟文的一家 SpaceXAI 工厂泄漏，随后流入附近的排水沟。州环保官员试图缓解当地居民的担忧，表示不会对他们造成任何风险。" data-title="Elon Musk’s SpaceXAI suffers chemical spill at Mississippi AI data center" data-date="11-18 22:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-18 22:30</span>
          <span class="news-item-title">埃隆·马斯克的SpaceXAI在密西西比州的人工智能数据中心发生化学品泄漏</span>
          <span class="news-item-title-en">Elon Musk’s SpaceXAI suffers chemical spill at Mississippi AI data center</span>
          <span class="news-value-point">💡 5,000 至 6,000 加仑的丙二醇从密西西比州绍瑟文的一家 SpaceXAI 工厂泄漏，随后流入附近的排水沟</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/18/us/politics/democrats-cast-investigative-net.html" target="_blank" rel="noopener" data-cat="keji" data-summary="调查的重点将是特朗普总统、他的家人以及其政府的高级官员，并将包括对商务部长霍华德·卢特尼克（Howard Lutnick）以及与英伟达相关的政策的审查。" data-title="House Democrats Cast Wide Net as They Prepare Trump Investigations" data-date="11-18 22:17" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-18 22:17</span>
          <span class="news-item-title">众议院民主党人在准备对特朗普的调查时撒下大网</span>
          <span class="news-item-title-en">House Democrats Cast Wide Net as They Prepare Trump Investigations</span>
          <span class="news-value-point">💡 调查的重点将是特朗普总统、他的家人以及其政府的高级官员，并将包括对商务部长霍华德·卢特尼克（Howard Lutnick）以及与英伟达相关的政策…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/games/1036140/will-wright-mymems-ai-game-interview" target="_blank" rel="noopener" data-cat="keji" data-summary="《模拟城市》和《模拟人生》等传奇系列的缔造者威尔·莱特（Will Wright）正在开发一款新游戏，这款游戏以人工智能为核心。这款以您的记忆为核心的新游戏名为MyMems。与Wright的其他游戏一样，这款游戏听起来野心勃勃，" data-title="Will Wright’s next game uses AI to map your memories" data-date="11-18 22:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-18 22:00</span>
          <span class="news-item-title">威尔·莱特（Will Wright）的下一款游戏将使用人工智能来映射您的记忆</span>
          <span class="news-item-title-en">Will Wright’s next game uses AI to map your memories</span>
          <span class="news-value-point">💡 《模拟城市》和《模拟人生》等传奇系列的缔造者威尔·莱特（Will Wright）正在开发一款新游戏，这款游戏以人工智能为核心</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/nvidia-board-faction-angling-for-jensen-huang-return-as-ceo-report-claims-company-defiant-at-earnings-calls-says-no-possibility-of-reinstatement" target="_blank" rel="noopener" data-cat="keji" data-summary="尽管英伟达董事会表示无意让前首席执行官黄仁勋重返公司，但据报道，一些董事仍在推动此事。" data-title="Nvidia board faction angling for Jensen Huang return as CEO, report claims" data-date="11-18 21:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-18 21:30</span>
          <span class="news-item-title">有报道称，英伟达董事会正谋求让黄仁勋重返首席执行官职位</span>
          <span class="news-item-title-en">Nvidia board faction angling for Jensen Huang return as CEO, report claims</span>
          <span class="news-value-point">💡 尽管英伟达董事会表示无意让前首席执行官黄仁勋重返公司，但据报道，一些董事仍在推动此事</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/18/nvidia-clarifies-when-it-will-and-wont-keep-financing-neoclouds/" target="_blank" rel="noopener" data-cat="keji" data-summary="临时首席执行官科莱特·克雷斯（Colette Kress）解释说，如果英伟达为数据中心贷款提供担保，那么只有在Neocould获得独立融资并建成配备英伟达设备的设施后，英伟达才会承担责任。" data-title="Nvidia clarifies when it will — and won’t —keep financing neoclouds" data-date="11-18 21:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-18 21:00</span>
          <span class="news-item-title">Nvidia澄清了其何时会——以及何时不会——继续为新云提供资金</span>
          <span class="news-item-title-en">Nvidia clarifies when it will — and won’t —keep financing neoclouds</span>
          <span class="news-value-point">💡 临时首席执行官科莱特·克雷斯（Colette Kress）解释说，如果英伟达为数据中心贷款提供担保，那么只有在Neocould获得独立融资并建成…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/nvidias-revenue-hits-usd115-8-billion-as-vera-rubin-generates-usd20-billion-in-another-record-setting-quarter-commitments-increase-to-usd390-billion-fy28-forecast-raised" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达的季度营收飙升至1158亿美元，Vera Rubin实现了创纪录的200亿美元首发，而对供应商和客户的总承诺额攀升至5400亿美元，成本上涨促使公司对2028财年的定价策略进行了调整。" data-title="Nvidia&#39;s revenue hits $115.8 billion as Vera Rubin generates $20 billion in another record" data-date="11-18 21:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-18 21:00</span>
          <span class="news-item-title">英伟达营收达1158亿美元，Vera Rubin再创200亿美元新高</span>
          <span class="news-item-title-en">Nvidia's revenue hits $115.8 billion as Vera Rubin generates $20 billion in another record</span>
          <span class="news-value-point">💡 英伟达的季度营收飙升至1158亿美元，Vera Rubin实现了创纪录的200亿美元首发，而对供应商和客户的总承诺额攀升至5400亿美元，成本上…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">11 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cj3vgp36z063o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英超联赛将于周六恢复，水晶宫、桑德兰和曼联目前处于降级区。但现在担心还为时过早吗？" data-title="The tightest survival scrap for years? Why it&#39;s not too early to worry" data-date="11-19 00:09" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-19 00:09</span>
          <span class="news-item-title">多年来最激烈的保级大战？为什么现在担心并不为时过早</span>
          <span class="news-item-title-en">The tightest survival scrap for years? Why it's not too early to worry</span>
          <span class="news-value-point">💡 英超联赛将于周六恢复，水晶宫、桑德兰和曼联目前处于降级区</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13613285/alex-scott-arsenal-keen-on-chelsea-and-liverpool-target-with-bournemouth-softening-stance-over-potential-sale" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳是英超联赛中对签约伯恩茅斯和英格兰中场球员亚历克斯·斯科特感兴趣的三大俱乐部之一。" data-title="Arsenal willing to make sales to beat Chelsea and Liverpool to Scott signing" data-date="11-18 23:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 23:00</span>
          <span class="news-item-title">阿森纳愿意出售球员，以期在斯科特签约方面击败切尔西和利物浦</span>
          <span class="news-item-title-en">Arsenal willing to make sales to beat Chelsea and Liverpool to Scott signing</span>
          <span class="news-value-point">💡 阿森纳是英超联赛中对签约伯恩茅斯和英格兰中场球员亚历克斯·斯科特感兴趣的三大俱乐部之一</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025492/man-utd-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Man Utd latest: Pochettino&#39;s first words as he arrives at Carrington for first time" data-title="Man Utd latest: Pochettino&#39;s first words as he arrives at Carrington for first time" data-date="11-18 23:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 23:00</span>
          <span class="news-item-title">曼联最新消息：波切蒂诺首次抵达卡灵顿训练基地后的首批言论</span>
          <span class="news-item-title-en">Man Utd latest: Pochettino's first words as he arrives at Carrington for first time</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13613260/man-utd-transfer-news-calvin-bassey-and-jarrad-branthwaite-among-targets-with-mauricio-pochettino-set-to-be-backed-in-january" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联主教练毛里西奥·波切蒂诺预计将在 1 月转会窗口获得支持，因为俱乐部希望扭转本赛季令人失望的开局。" data-title="Man Utd expected to back Poch in January transfer window" data-date="11-18 20:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 20:00</span>
          <span class="news-item-title">曼联预计将在 1 月转会窗口为波切蒂诺提供支持</span>
          <span class="news-item-title-en">Man Utd expected to back Poch in January transfer window</span>
          <span class="news-value-point">💡 曼联主教练毛里西奥·波切蒂诺预计将在 1 月转会窗口获得支持，因为俱乐部希望扭转本赛季令人失望的开局</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13613290/transfer-news-your-premier-league-clubs-unfinished-business-ahead-of-january-window" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Your PL club&#39;s &#39;Unfinished Business&#39; revealed ahead of January window" data-title="Your PL club&#39;s &#39;Unfinished Business&#39; revealed ahead of January window" data-date="11-18 20:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 20:00</span>
          <span class="news-item-title">英超俱乐部“未竟之事”在1月转会窗口开启前揭晓</span>
          <span class="news-item-title-en">Your PL club's 'Unfinished Business' revealed ahead of January window</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13613260/man-utd-transfer-news-calvin-bassey-and-jarrad-branthwaite-among-targets-with-mauricio-pochettino-set-to-be-backed-in-january" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联主教练毛里西奥·波切蒂诺预计将在 1 月转会窗口获得支持，因为俱乐部希望扭转本赛季令人失望的开局。" data-title="Man Utd expected to back Poch in January transfer window" data-date="11-18 20:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 20:00</span>
          <span class="news-item-title">曼联预计将在 1 月转会窗口为波切蒂诺提供支持</span>
          <span class="news-item-title-en">Man Utd expected to back Poch in January transfer window</span>
          <span class="news-value-point">💡 曼联主教练毛里西奥·波切蒂诺预计将在 1 月转会窗口获得支持，因为俱乐部希望扭转本赛季令人失望的开局</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025489/tottenham-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Spurs latest: &#39;Tottenham were one of three clubs in Poch&#39;s USA exit clause&#39;" data-title="Spurs latest: &#39;Tottenham were one of three clubs in Poch&#39;s USA exit clause&#39;" data-date="11-18 17:47" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 17:47</span>
          <span class="news-item-title">热刺最新消息：“热刺是波切蒂诺美国解约条款中提及的三家俱乐部之一”</span>
          <span class="news-item-title-en">Spurs latest: 'Tottenham were one of three clubs in Poch's USA exit clause'</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13613499/mauricio-pochettino-incoming-manchester-united-head-coach-calls-for-time-to-topple-manchester-city-ahead-of-old-trafford-arrival" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="当被问及曼城的主导地位时，毛里西奥·波切蒂诺（Mauricio Pochettino）承诺将让曼联再次成为这座城市的霸主，并坚持表示“你们会看到的”。" data-title="Pochettino vows to make Manchester red again" data-date="11-18 17:21" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 17:21</span>
          <span class="news-item-title">波切蒂诺誓言让曼彻斯特再次变红</span>
          <span class="news-item-title-en">Pochettino vows to make Manchester red again</span>
          <span class="news-value-point">💡 当被问及曼城的主导地位时，毛里西奥·波切蒂诺（Mauricio Pochettino）承诺将让曼联再次成为这座城市的霸主，并坚持表示“你们会看到…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13613478/premier-league-top-25-players-who-is-the-best-player-in-the-premier-league-right-now" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Top 25 Premier League players... 10 to six REVEALED!" data-title="Top 25 Premier League players... 10 to six REVEALED!" data-date="11-18 15:42" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 15:42</span>
          <span class="news-item-title">英超联赛25大球员……第10至第6名揭晓！</span>
          <span class="news-item-title-en">Top 25 Premier League players... 10 to six REVEALED!</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqvg2e4208zmo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在准备可能转会至皇家马德里之际，小将加布里埃尔发布了告别信息，表示曼联将永远是他故事的一部分。" data-title="Madrid-bound Gabriel posts farewell Man Utd message" data-date="11-18 03:35" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-18 03:35</span>
          <span class="news-item-title">即将加盟皇马的加布里埃尔发布告别曼联的讯息</span>
          <span class="news-item-title-en">Madrid-bound Gabriel posts farewell Man Utd message</span>
          <span class="news-value-point">💡 在准备可能转会至皇家马德里之际，小将加布里埃尔发布了告别信息，表示曼联将永远是他故事的一部分</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13613361/jj-gabriel-transfer-news-manchester-united-teenager-announces-departure-from-club-amid-real-madrid-agreement" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="JJ·加布里埃尔宣布他将离开曼联，并期待在皇家马德里开启他的“下一篇章”。" data-title="JJ Gabriel says goodbye to Man Utd with Real Madrid move close" data-date="11-18 02:29" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 02:29</span>
          <span class="news-item-title">随着皇马转会临近，J.J. 加布里埃尔与曼联告别</span>
          <span class="news-item-title-en">JJ Gabriel says goodbye to Man Utd with Real Madrid move close</span>
          <span class="news-value-point">💡 JJ·加布里埃尔宣布他将离开曼联，并期待在皇家马德里开启他的“下一篇章”</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theverge.com/tech/1036494/shelly-neo-smart-home-water-valve-sensor-shut-off" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Shelly 今年早些时候推出了售价 28 美元的漏水传感器，该传感器使用电池供电，可轻松运行两年。现在，Shelly 又宣布推出一款配套的智能阀门，您可以将其安装在家中的主水管上，当其中一个传感器检测到漏水时，该阀门会自动关闭水流。" data-title="Shelly’s new smart valve shuts off your home’s water before a leak becomes a flood" data-date="11-19 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-19 00:00</span>
          <span class="news-item-title">在漏水演变成洪灾之前，Shelly的新款智能阀门会关闭您家中的水源</span>
          <span class="news-item-title-en">Shelly’s new smart valve shuts off your home’s water before a leak becomes a flood</span>
          <span class="news-value-point">💡 Shelly 今年早些时候推出了售价 28 美元的漏水传感器，该传感器使用电池供电，可轻松运行两年</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1036578/8bitdo-gb-bluetooth-gamepad-wireless-controller-nintendo-gamecube-wavebird" target="_blank" rel="noopener" data-cat="zonghe" data-summary="8BitDo 64是对任天堂64那款不寻常的三握式手柄的宽松翻版，取消了该手柄的中央模拟摇杆。但凭借全新的 GC 蓝牙游戏手柄，8BitDo 在忠实于原版设计方面做得更好。" data-title="8BitDo’s new gamepad modernizes the Nintendo GameCube’s WaveBird" data-date="11-19 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-19 00:00</span>
          <span class="news-item-title">8BitDo的新款游戏手柄对任天堂GameCube的WaveBird进行了现代化改造</span>
          <span class="news-item-title-en">8BitDo’s new gamepad modernizes the Nintendo GameCube’s WaveBird</span>
          <span class="news-value-point">💡 8BitDo 64是对任天堂64那款不寻常的三握式手柄的宽松翻版，取消了该手柄的中央模拟摇杆</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/golf/news/12040/13613433/cme-group-tour-championship-field-format-prize-money-as-nelly-korda-charley-hull-lottie-woad-battle-for-win-at-lpga-finale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="谁将加冕LPGA巡回赛CME环球锦标赛冠军？谁能阻止内莉·科达夺冠？英国选手查莉·赫尔和洛蒂·沃德能否夺冠？在 Sky Sports 直播的本周 LPGA 巡回赛 2026 赛季总决赛开赛前，我们为您提供最新资讯。" data-title="CME Group Tour Championship: Can Hull and Woad stop Korda?" data-date="11-19 00:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-19 00:00</span>
          <span class="news-item-title">CME集团巡回锦标赛：Hull和Woad能阻止Korda吗？</span>
          <span class="news-item-title-en">CME Group Tour Championship: Can Hull and Woad stop Korda?</span>
          <span class="news-value-point">💡 谁将加冕LPGA巡回赛CME环球锦标赛冠军</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/029/120.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 18 日消息，据界面新闻今日报道，小米创办人、董事长兼 CEO 雷军在 APEC 圆桌会谈的采访中披露未发布新机小米 18 相关信息。这款机型预计 12 月正式发布，硬件层面沿用小米数字标准版小机身，性能、影像、续航、屏幕等实现升级。报道还提到，有消息称新机起售价为 5699 元。据IT之家此前报道，小米 18 标准版手机已通过 3C 认证，相关页面显示会支持 100W 快充。爆料称，小米 18 会搭载骁龙 8 Elite Gen6 处理器、200MP 相机传感器，并配备 7200mAh 电池。目前，官方暂未确认小米 18 标准版配置信息，一切以官方为准。博主 @数码闲聊站 爆料称，小米 18 标准版定价在 6000 元左右，有超大的影像模组，号称屏幕 / 性能 / 影像" data-title="小米 18 标准版手机预计 12 月发布，消息称起售价 5699 元" data-date="11-18 23:34" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-18 23:34</span>
          <span class="news-item-title">小米 18 标准版手机预计 12 月发布，消息称起售价 5699 元</span>
          <span class="news-value-point">💡 IT之家 11 月 18 日消息，据界面新闻今日报道，小米创办人、董事长兼 CEO 雷军在 APEC 圆桌会谈的采访中披露未发布新机小米 18 …</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/racing/news/12040/13613649/sober-glory-storms-to-victory-over-old-park-star-on-chase-debut" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在Ffos Las赛马场举行的Golwg Gwendraeth初级障碍赛中，Sober Glory反败为胜，击败了Supreme Novices’ Hurdle赛的冠军Old Park Star，完美地完成了障碍赛首秀。" data-title="Sober Glory storms to victory over Old Park Star on chase debut" data-date="11-18 23:25" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 23:25</span>
          <span class="news-item-title">Sober Glory在首次追逐赛中势如破竹，战胜Old Park Star夺得胜利</span>
          <span class="news-item-title-en">Sober Glory storms to victory over Old Park Star on chase debut</span>
          <span class="news-value-point">💡 在Ffos Las赛马场举行的Golwg Gwendraeth初级障碍赛中，Sober Glory反败为胜，击败了Supreme Novices…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/029/119.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 18 日消息，当地时间 17 日，据《纽约时报》报道，美国联邦航空管理局（FAA）宣布，将暂停安装慧与旗下瞻博网络生产的一款路由器。据了解，该设备原本用于美国航空设施的现代化改造，当前被 FAA 认为是 11 月 13 日全美航班暂停起飞的主要原因之一。FAA 不仅叫停了后续安装，还停用了此前部署的 60 多台路由器。美国交通部长肖恩 · 达菲最初将此次大规模停飞归咎于硬件老化，但第二天又透露，故障实际上与美国航空设施的升级改造有关。达菲介绍，事发时，科技公司 L3Harris 的一名承包商工作人员在阿肯色州埃尔多拉多的一处 FAA 设施内，准备将老旧的铜线通信线路更换为光纤，并安装新路由器。但新设备开始向空管系统中的其他路由器大量发送数据，得克萨斯州阿马里洛的另一台路由" data-title="一款路由器故障导致全美航班停飞，FAA 停用 60 余台设备并叫停后续安装" data-date="11-18 23:24" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-18 23:24</span>
          <span class="news-item-title">一款路由器故障导致全美航班停飞，FAA 停用 60 余台设备并叫停后续安装</span>
          <span class="news-value-point">💡 IT之家 11 月 18 日消息，当地时间 17 日，据《纽约时报》报道，美国联邦航空管理局（FAA）宣布，将暂停安装慧与旗下瞻博网络生产的一款…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/029/118.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 18 日消息，数毛社（Digital Foundry）发布了两段视频，对《GTA 6》在不同主机上的性能表现进行了详细分析。其中一段重点测试 PlayStation 5 和 PS5 Pro 版本，另一段则针对 Xbox Series X 和 Series S 版本。IT之家注意到，对于 Xbox Series X 版，数毛社给出了相对积极的评价。该版本的表现与标准版 PS5 比较接近，内部渲染分辨率基本维持在 1440p，目标帧率为 30 FPS，不过在场景较为复杂、负载较高时，仍然会出现掉帧。数毛社分析师奥利弗 · 麦肯齐（Oliver Mackenzie）在视频中表示：“《GTA 6》在常规游戏过程中基本能够达到并维持 30 FPS，即使在激烈战斗和快速移动等高负载场" data-title="数毛社实测《GTA 6》Xbox 版：Series X 稳定 30 帧，Series S 掉帧明显" data-date="11-18 23:16" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-18 23:16</span>
          <span class="news-item-title">数毛社实测《GTA 6》Xbox 版：Series X 稳定 30 帧，Series S 掉帧明显</span>
          <span class="news-value-point">💡 IT之家 11 月 18 日消息，数毛社（Digital Foundry）发布了两段视频，对《GTA 6》在不同主机上的性能表现进行了详细分析</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/029/115.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 18 日消息，据 tom&#39;s hardware 报道，埃隆 · 马斯克（Elon Musk）旗下的 SpaceXAI（SpaceXSI）在美国密西西比州的 AI 数据中心发生化学品泄漏事件。承包商在连接移动储罐时因软管配置错误，导致用于数据中心液冷散热的传热流体（主要成分为低毒性的抑制型丙二醇水溶液，用于数据中心或发电冷却系统）发生泄漏。部分液体流出厂区并进入附近的排水沟。密西西比州环境质量部（MDEQ）介入了此次 SpaceXAI 设施化学品泄漏事件。经确认，泄漏的丙二醇总量在 5000 至 6000 加仑（IT之家注：约合 18.93 – 22.71 m³）之间。由于泄漏物质在 OSHA 标准下属于非危险混合物，且在自然水体和土壤中降解较快（通常数天至一周内分解），加" data-title="SpaceXAI 在美国密西西比州的 AI 数据中心泄漏约 20m³ 丙二醇" data-date="11-18 23:01" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-18 23:01</span>
          <span class="news-item-title">SpaceXAI 在美国密西西比州的 AI 数据中心泄漏约 20m³ 丙二醇</span>
          <span class="news-value-point">💡 IT之家 11 月 18 日消息，据 tom's hardware 报道，埃隆 · 马斯克（Elon Musk）旗下的 SpaceXAI（Spa…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1021917/best-gifts-for-travelers-2026" target="_blank" rel="noopener" data-cat="zonghe" data-summary="每个人的生活中都有这样一个旅行者。这个人宁愿在14小时的火车上度过，也不愿在安静的周日窝在沙发上。他们会说多种语言，胃口好得像山羊，走到哪里都能交到朋友。无论他们是否是您的同类，" data-title="The Verge’s 2026 holiday gift guide for travelers" data-date="11-18 23:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-18 23:00</span>
          <span class="news-item-title">The Verge 2026 年旅行者假日礼品指南</span>
          <span class="news-item-title-en">The Verge’s 2026 holiday gift guide for travelers</span>
          <span class="news-value-point">💡 每个人的生活中都有这样一个旅行者</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1036517/instagram-school-safety-program-project-gryffindor" target="_blank" rel="noopener" data-cat="zonghe" data-summary="据NPR报道，Meta旨在让Instagram对学校更安全的举措源于其增加用户“获取”、“加好友”和“邀请”的努力。作为针对Meta的一系列儿童安全诉讼的一部分，内部文件被披露。" data-title="Instagram’s ‘school safety’ push was also a way to get more teens on the app" data-date="11-18 22:59" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-18 22:59</span>
          <span class="news-item-title">Instagram的“校园安全”推广也是吸引更多青少年使用该应用程序的一种方式</span>
          <span class="news-item-title-en">Instagram’s ‘school safety’ push was also a way to get more teens on the app</span>
          <span class="news-value-point">💡 据NPR报道，Meta旨在让Instagram对学校更安全的举措源于其增加用户“获取”、“加好友”和“邀请”的努力</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/029/114.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 18 日消息，《GTA 6》终于来了，就连一向低调、鲜少公开发言的 R 星联合创始人兼总裁山姆 · 豪瑟，也罕见发表了一份声明，欢迎玩家来到雷奥奈达州，并对玩家表示“无比感激”。豪瑟向外媒 GamesRadar+ 发表的声明提到：“我们从创立之初就相信，游戏可以像其他叙事艺术一样获得认可，成为现代文化不可或缺的一部分，让其中的故事和世界长久留在人们心中。”“本周，GTA 系列重返雷奥奈达州，回到现代的罪恶城。虽然时过境迁，许多事情都变了，但有一点始终如一：我们希望创造超越玩家期待的游戏体验，展现游戏这种媒介究竟能做到什么，以及我们为什么认为游戏如此特别。”据IT之家了解，GTA 系列历代正传作品的执行制作人名单上都有豪瑟的名字。报道指出，作为 R 星创作团队的核心人物，长" data-title="《GTA 6》发售后 R 星总裁山姆 · 豪瑟罕见致谢：愿未来多年与大家同行" data-date="11-18 22:45" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-18 22:45</span>
          <span class="news-item-title">《GTA 6》发售后 R 星总裁山姆 · 豪瑟罕见致谢：愿未来多年与大家同行</span>
          <span class="news-value-point">💡 IT之家 11 月 18 日消息，《GTA 6》终于来了，就连一向低调、鲜少公开发言的 R 星联合创始人兼总裁山姆 · 豪瑟，也罕见发表了一份声…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13613622/watch-sober-glory-slams-rivals-on-chase-debut-at-ffos-las" target="_blank" rel="noopener" data-cat="zonghe" data-summary="备受期待的Supreme 1-2复赛在弗斯拉斯赛马场落下帷幕，Sober Glory以绝对优势胜出。" data-title="WATCH: Sober Glory slams rivals on chase debut" data-date="11-18 22:40" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 22:40</span>
          <span class="news-item-title">观看：Sober Glory在追逐赛首秀中碾压对手</span>
          <span class="news-item-title-en">WATCH: Sober Glory slams rivals on chase debut</span>
          <span class="news-value-point">💡 备受期待的Supreme 1-2复赛在弗斯拉斯赛马场落下帷幕，Sober Glory以绝对优势胜出</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13613617/incredible-footage-see-how-ball-swings-in-match-at-heart-of-cameron-bancroft-sandpaper-claims" target="_blank" rel="noopener" data-cat="zonghe" data-summary="卡梅伦·班克罗夫特声称，在2018年与南非的第二场测试赛中，澳大利亚队在以4-28的成绩获胜时使用了砂纸，而视频似乎也证实了这一说法。英格兰南非巡回赛将于12月17日起在Sky Sports上直播。" data-title="The damning footage that supports Bancroft&#39;s explosive new claims" data-date="11-18 22:31" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 22:31</span>
          <span class="news-item-title">支持班克罗夫特爆炸性新主张的 damning 录像</span>
          <span class="news-item-title-en">The damning footage that supports Bancroft's explosive new claims</span>
          <span class="news-value-point">💡 卡梅伦·班克罗夫特声称，在2018年与南非的第二场测试赛中，澳大利亚队在以4-28的成绩获胜时使用了砂纸，而视频似乎也证实了这一说法</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/f1/news/12040/13613606/oscar-piastri-to-serve-grid-penalty-at-las-vegas-gp-as-mclaren-confirm-addition-of-more-upgrades-to-mcl40" target="_blank" rel="noopener" data-cat="zonghe" data-summary="迈凯伦已确认，奥斯卡·皮亚斯特里（Oscar Piastri）将在本周末的拉斯维加斯大奖赛中被罚退10个发车位，因为他将被迫超出本赛季的引擎使用额度。" data-title="Piastri to serve grid penalty at Las Vegas GP" data-date="11-18 22:30" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 22:30</span>
          <span class="news-item-title">皮亚斯特里将在拉斯维加斯大奖赛中接受发车位处罚</span>
          <span class="news-item-title-en">Piastri to serve grid penalty at Las Vegas GP</span>
          <span class="news-value-point">💡 迈凯伦已确认，奥斯卡·皮亚斯特里（Oscar Piastri）将在本周末的拉斯维加斯大奖赛中被罚退10个发车位，因为他将被迫超出本赛季的引擎使用…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/boxing/news/12040/13613615/rico-verhoeven-could-the-kickboxing-superstar-step-in-to-fight-deontay-wilder-on-the-tyson-fury-vs-anthony-joshua-bill" target="_blank" rel="noopener" data-cat="zonghe" data-summary="德昂泰·怀尔德（Deontay Wilder）目前正在为泰森·富里（Tyson Fury）与安东尼·约书亚（Anthony Joshua）对决的垫场赛寻找新的对手。" data-title="Verhoeven to fight Wilder? &#39;He&#39;s always up for a big fight!&#39;" data-date="11-18 22:20" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-18 22:20</span>
          <span class="news-item-title">Verhoeven将与Wilder对战？“他一直都渴望一场大战！”</span>
          <span class="news-item-title-en">Verhoeven to fight Wilder? 'He's always up for a big fight!'</span>
          <span class="news-value-point">💡 德昂泰·怀尔德（Deontay Wilder）目前正在为泰森·富里（Tyson Fury）与安东尼·约书亚（Anthony Joshua）对决的…</span>
        </a>
  </div>
</div>
<script defer src="{{ "/assets/js/news-feed.js" | relative_url }}"></script>


<p class="news-updated">🕐 抓取更新于 2026-11-19 00:39（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
