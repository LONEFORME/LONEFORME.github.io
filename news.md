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
      <span>2026-09-11 20:18 抓取更新</span>
    </div>
  </div>

  <div class="news-search-bar" style="margin: 12px 0 8px; display: flex; align-items: center; gap: 8px; background: rgba(127,127,127,0.08); border: 1px solid rgba(127,127,127,0.2); border-radius: 8px; padding: 7px 14px;">
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="opacity: 0.65;"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
    <input type="text" id="news-search-input" placeholder="🔍 实时搜索今日全天新闻（输入关键词、球队、公司、人物、信源）..." oninput="onNewsSearch(this.value)" style="flex: 1; background: transparent; border: none; outline: none; color: inherit; font-size: 13px;">
    <span id="news-search-count" style="font-size: 12px; opacity: 0.7; font-weight: 500;"></span>
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
      <button class="channel-btn" onclick="filterNewsChannel('meimei', this)">
        <span>🌍 西方媒体视角</span>
        <span class="channel-count">0</span>
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
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.nytimes.com/video/us/politics/100000011133866/how-trump-is-using-the-postal-service-to-intervene-in-elections.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="我们的政治记者里德·爱泼斯坦（ Reid Epstein ）解释了特朗普政府如何利用邮政服务干预州选举的邮寄投票。" data-title="特朗普如何利用邮政服务干预选举" data-date="09-11 20:14" data-source="纽约时报">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
        <span class="hero-featured-date">🕒 09-11 20:14</span>
      </div>
      <h2 class="hero-featured-title">特朗普如何利用邮政服务干预选举</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.nytimes.com/2026/09/10/science/ai-humanity-risk.html" target="_blank" rel="noopener" data-cat="keji" data-summary="这项技术远非我们物种面临的唯一生存风险。但是，权衡这种宇宙恐惧可能成为一种令人难以置信的练习。" data-title="人工智能有可能终结人类。人类应该如何处理这种情况？" data-date="09-11 20:17" data-source="纽约时报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
      </div>
      <p class="hero-sub-title">人工智能有可能终结人类。人类应该如何处理这种情况？</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/c1j4zydzk2zo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联在一次门票宣传调查后禁止了685个球迷账户，并坚称无辜的球迷没有受到惩罚。" data-title="曼联在兜售调查后禁止了 685 个球迷账户" data-date="09-11 19:33" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">曼联在兜售调查后禁止了 685 个球迷账户</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/09-11/10694941.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网哈尔滨9月11日电 (史轶夫 王迎春)在我们国家长护险制度从局部试点转向全国推行的大背景下，近日，黑龙江省出台了《黑龙江省建立长期护理保险制度实施方案》。9月11日，黑龙江省人民政府新闻办公室召开专题发布会，介绍和解读建立长期护理保险制度的相关政策和配套措施。" data-title="黑龙江全面推开长期护理保险制度 破解失能家庭“照护难”" data-date="09-11 20:05" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">黑龙江全面推开长期护理保险制度 破解失能家庭“照护难”</p>
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
        <a class="news-item" href="https://www.nytimes.com/video/us/politics/100000011133866/how-trump-is-using-the-postal-service-to-intervene-in-elections.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="我们的政治记者里德·爱泼斯坦（ Reid Epstein ）解释了特朗普政府如何利用邮政服务干预州选举的邮寄投票。" data-title="特朗普如何利用邮政服务干预选举" data-date="09-11 20:14" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-11 20:14</span>
          <span class="news-item-title">特朗普如何利用邮政服务干预选举</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-11/10694947.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社西宁9月11日电 题：青海基层立法联系点：立法“直通车”助“石榴籽”抱得更紧" data-title="青海基层立法联系点：立法“直通车”助“石榴籽”抱得更紧" data-date="09-11 20:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 20:07</span>
          <span class="news-item-title">青海基层立法联系点：立法“直通车”助“石榴籽”抱得更紧</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-11/10694943.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网广州9月11日电 (记者 孙秋霞)“赓续红色血脉 传承南梁精神：革命主题绘画艺术作品巡展”广州站11日在广州人民艺术中心开幕。作为全国巡展的重要一站也是最后一站，该展览以艺术为载体、以历史为纽带，与观众共同回望革命峥嵘岁月，赓续红色血脉，传承革命精神。" data-title="70幅革命主题艺术精品亮相广州人民艺术中心" data-date="09-11 20:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 20:05</span>
          <span class="news-item-title">70幅革命主题艺术精品亮相广州人民艺术中心</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-11/10694955.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月11日电 中央纪委国家监委11日通报，甘肃省委原常委、省政府原副省长雷思维，新疆生产建设兵团原党委常委、副司令员李旭，分别被开除党籍和公职。" data-title="甘肃省原副省长雷思维、新疆生产建设兵团原副司令员李旭均获处分" data-date="09-11 20:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 20:03</span>
          <span class="news-item-title">甘肃省原副省长雷思维、新疆生产建设兵团原副司令员李旭均获处分</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-11/10694917.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京9月11日电 题：破坏民族团结、煽动民族仇恨 必受严惩" data-title="评论：破坏民族团结、煽动民族仇恨 必受严惩" data-date="09-11 19:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 19:59</span>
          <span class="news-item-title">评论：破坏民族团结、煽动民族仇恨 必受严惩</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-11/10694948.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="李强主持召开国务院常务会议" data-title="李强主持召开国务院常务会议" data-date="09-11 19:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 19:53</span>
          <span class="news-item-title">李强主持召开国务院常务会议</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-11/10694894.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网贵阳9月11日电 (记者 张伟)记者11日从贵州省民政厅举行的新闻发布会上获悉，为贯彻落实《中华人民共和国社会救助法》和中国民政部、中国财政部《关于进一步健全完善临时救助制度的意见》、健全完善分层分类社会救助体系的具体举措，更好保障困难民众基本生活，贵州省民政厅、贵州省财政厅日前联合印发了《关于加强和改进临时救助工作的通知》(以下简称，《通知》)。" data-title="贵州：加强和改进临时救助工作 “急难能救、救得及时”" data-date="09-11 19:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 19:21</span>
          <span class="news-item-title">贵州：加强和改进临时救助工作 “急难能救、救得及时”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-11/10694876.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月11日电 伯尔尼消息：瑞士格劳宾登州警方当地时间11日说，一辆荷兰旅游巴士10日在该州发生侧翻，已造成5人死亡、40人受伤。" data-title="一辆荷兰旅游巴士在瑞士侧翻致5死40伤" data-date="09-11 19:19" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 19:19</span>
          <span class="news-item-title">一辆荷兰旅游巴士在瑞士侧翻致5死40伤</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-11/10694778.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社加德满都9月11日电 (记者 崔楠)当地时间9月11日下午，中国对尼泊尔第五批紧急援助物资由中国空军运—20大型运输机运抵尼泊尔首都加德满都特里布万国际机场。" data-title="中国对尼泊尔第五批紧急援助物资运抵加德满都" data-date="09-11 17:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 17:11</span>
          <span class="news-item-title">中国对尼泊尔第五批紧急援助物资运抵加德满都</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-11/10694753.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="第十八届金砖国家领导人峰会将于9月12日至13日在印度新德里举行。本届峰会恰逢金砖合作机制创立20周年，也是扩员后的“大金砖合作”深化发展的关键一年。连日来，印度、南非、阿联酋、印尼等多国媒体密集发声，共同勾勒出金砖合作机制作为新兴市场国家团结合作重要平台的成长轨迹，并特别关注中国在其中的贡献与引领作用。" data-title="全球媒体聚焦 |“金砖峰会已成为捍卫世界多极化的重要力量”" data-date="09-11 16:58" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 16:58</span>
          <span class="news-item-title">全球媒体聚焦 |“金砖峰会已成为捍卫世界多极化的重要力量”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-11/10694737.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月11日电 近日，伊朗捕获了美国的大装备。伊朗伊斯兰革命卫队8日高调宣布，在霍尔木兹海峡入口处捕获一艘潜水-LD型无人潜航器，并称是美军“最先进的无人化智能化潜艇之一”。" data-title="伊朗捕获美军先进无人潜航器 美方辩解：老旧型号 不涉及机密" data-date="09-11 16:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 16:39</span>
          <span class="news-item-title">伊朗捕获美军先进无人潜航器 美方辩解：老旧型号 不涉及机密</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/11/us/politics/republican-midterm-convention-vance-takeaways.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在达拉斯共和党集会的第二天晚上，副总统JD万斯成为头条新闻。但特朗普总统又回到了舞台的中心。" data-title="共和党中期大会的7个要点" data-date="09-11 16:22" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-11 16:22</span>
          <span class="news-item-title">共和党中期大会的7个要点</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-11/10694708.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月11日电 据韩联社报道，韩国法院11日对前总统尹锡悦涉嫌帮助前国防部长官李钟燮潜逃海外案进行一审宣判，判定尹锡悦无罪。首尔中央地方法院刑事审判第22合议庭当天作出如上判决。" data-title="涉帮助前防长潜逃案 尹锡悦一审被判无罪" data-date="09-11 16:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 16:05</span>
          <span class="news-item-title">涉帮助前防长潜逃案 尹锡悦一审被判无罪</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-11/10694590.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社首尔9月11日电(记者张粲#8195;孙一然)韩国首尔中央地方法院11日对前总统尹锡悦涉嫌使犯罪嫌疑人逃避司法追究等一案作出一审判决，判处尹锡悦无罪。(完)" data-title="尹锡悦涉嫌使犯罪嫌疑人逃避司法追究案一审被判无罪" data-date="09-11 14:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 14:16</span>
          <span class="news-item-title">尹锡悦涉嫌使犯罪嫌疑人逃避司法追究案一审被判无罪</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-11/10694581.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月11日电 金砖国家领导人第十八次会晤将于9月12日至13日在印度新德里举行。此次会晤恰逢金砖合作机制创立20周年，备受国际瞩目。多家外媒指出，金砖合作机制已发展成为表达全球南方国家关切的重要平台，影响力持续提升。国际形势变乱交织的当下，金砖合作机制的重要性不断凸显。" data-title="外媒聚焦金砖合作：中国发挥重要作用 助力全球南方共同发展繁荣" data-date="09-11 14:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 14:00</span>
          <span class="news-item-title">外媒聚焦金砖合作：中国发挥重要作用 助力全球南方共同发展繁荣</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/09/10/science/ai-humanity-risk.html" target="_blank" rel="noopener" data-cat="keji" data-summary="这项技术远非我们物种面临的唯一生存风险。但是，权衡这种宇宙恐惧可能成为一种令人难以置信的练习。" data-title="人工智能有可能终结人类。人类应该如何处理这种情况？" data-date="09-11 20:17" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-11 20:17</span>
          <span class="news-item-title">人工智能有可能终结人类。人类应该如何处理这种情况？</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/441.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 11 日消息，小米米家夜灯 4 现已在小米有品开启众筹，支持暗光感应、8 个月长续航，单只装 59 元，两只装 115 元，活动截止时间为 9 月 16 日 10 点（点击前往）。IT之家从商品页面获悉，小米米家夜灯 4 主要是升级了 24GHz 雷达，拥有 120° 大广角，在正前方 3m、侧方 2.5m 范围内可精准识别人体细微动作。黑暗环境下，可实现人来灯亮，人离开后 10 秒后自动关灯。小米米家夜灯 4 采用背面出光，经墙面充分反射打散光线，支持 1lm、3lm、5lm、15lm 亮度 4 挡可调，无可视频闪，RGO 无蓝光危害，舒适暖光不刺眼。这款产品搭载 800mAh 锂电池，采用 Type-C 充电设计，搭载低功耗算法，满电续航 8 个月（最高亮度 3 个月）" data-title="小米米家夜灯 4 开启众筹：暗光感应、8 个月长续航，59 元" data-date="09-11 20:10" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-11 20:10</span>
          <span class="news-item-title">小米米家夜灯 4 开启众筹：暗光感应、8 个月长续航，59 元</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-11/10694927.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网北京9月11日电 题：中外专家话司法应用AI：行稳方能致远" data-title="中外专家话司法应用AI：行稳方能致远" data-date="09-11 20:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 20:00</span>
          <span class="news-item-title">中外专家话司法应用AI：行稳方能致远</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/science/993522/water-chip-semiconductor-manufacturing-colorado-river" target="_blank" rel="noopener" data-cat="keji" data-summary="亚利桑那州是两党推动振兴美国芯片制造业的中心，它将失去每年通常从科罗拉多河抽取的四分之一以上的水。这条长达1,400英里的水道是该地区和其他西部各州的重要生命线。最近关于如何管理其[…]的联邦决定" data-title="亚利桑那州芯片制造的生命线正在枯竭" data-date="09-11 20:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-11 20:00</span>
          <span class="news-item-title">亚利桑那州芯片制造的生命线正在枯竭</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/440.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 11 日消息，比亚迪方程豹今日新一期钛系列答网友问，同步最新交付进度。公告称，当前钛 7 EV 闪充版车型交付工作正平稳有序推进，其中选装四驱版本的产能已提升，交付周期较此前有所缩短；同时，钛 7 DM 长续航版、钛 3 510KM 后驱闪充版已于 8 月底正式开启交付，不同车型因配置复杂度和关键零部件、地区物流等差异影响，各车型最新预计等待周期如下：在生产安排上，团队严格遵循用户锁单顺序进行排产。但在实际交付过程中，最终的提车顺序会受到多重客观因素影响，具体包括：定金支付与合同签署的完成时效、所选配置 (如特定颜色或选装包) 的排产批次以及不同区域的物流发运计划。这些因素交织作用，可能导致个别订单的实际交付顺序与锁单顺序存在细微差异。IT之家注意到，方程豹钛 7 EV 闪" data-title="比亚迪方程豹公布钛系列车型交付进度，钛 7 EV 闪充版已批量交付" data-date="09-11 19:52" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-11 19:52</span>
          <span class="news-item-title">比亚迪方程豹公布钛系列车型交付进度，钛 7 EV 闪充版已批量交付</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/439.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="8 月 14 日，石头科技正式推出了 G 系列最新滚筒扫拖旗舰 G30S Ultra，以及全新的 P30 Pro。其中，P30 Pro 水箱版与上下水版分别售价 4299 元和 4699 元；而定位旗舰的 G30S Ultra，水箱版售价 5499 元，上下水版则达到了 5999 元。目前，IT之家已经拿到了这款售价 5999 元的 G30S Ultra 上下水版。坦白说，拿到一台 5999 元的扫地机器人，大家的第一反应通常是先看配置：41000Pa 吸力、75℃ 热活水洗地、100℃ 高温洗布、8.98cm 机身、8.8cm 双层越障…… 单看参数，这套配置确实够漂亮。但如今的扫地机器人市场早已进入了“深水区”，现在的旗舰比拼的，是谁能真正解决那些顽固的“长尾痛点”—— 比如低矮家具底部" data-title="石头 G30S Ultra 体验：41000Pa、75℃ 活水与 8.98cm 机身，年度旗舰答卷" data-date="09-11 19:49" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-11 19:49</span>
          <span class="news-item-title">石头 G30S Ultra 体验：41000Pa、75℃ 活水与 8.98cm 机身，年度旗舰答卷</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/438.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 11 日消息，长城汽车今天（11 日）晚间公布了魏牌二代蓝山的“曜石黑”车色，新车采用原创设计，主打“东方豪华”，定位为智慧豪华方盒子 SUV。此前，官方公布了该车的浅蓝外观配色，新车也已经在工信部完成申报。其尺寸为 5300×2050×1960mm、轴距 3010mm，轮胎规格 275/50 R21。新车正面配备直瀑式镀铬格栅，前大灯是复古风的圆形设计，尾部印有“蓝山”标识，采用平开式尾门，尾灯为双圆形组合，此次公布的影像中，新车用上了大饼轮毂，豪华气息又增加了不少。据IT之家了解，新车搭载 2.0T 混动专用发动机，匹配 4 挡混动专用变速箱，电机功率为前 110kW、后 220kW，内置 66.6kWh（1/3C）电池。按照魏牌 CEO 赵永坡的消息，今年第四季度将推" data-title="长城公布魏牌二代蓝山“曜石黑”车色，复古圆灯、直瀑格栅、大饼轮毂吸睛" data-date="09-11 19:44" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-11 19:44</span>
          <span class="news-item-title">长城公布魏牌二代蓝山“曜石黑”车色，复古圆灯、直瀑格栅、大饼轮毂吸睛</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/437.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 11 日消息，苹果在 2026 年秋季发布会上发布了 iPhone 18 Pro 和 iPhone 18 Pro Max 手机，起售价分别为 9999 元和 10999 元。IT之家注意到，苹果官网现已公布了 iPhone 18 Pro 和 iPhone 18 Pro Max 手机的维修预估费用。iPhone 18 Pro电池服务：1,048 元背面玻璃损坏：1,298 元后置相机损坏：1,949 元屏幕损坏：2,698 元屏幕和背面玻璃损坏：3,429 元其他损坏：6,898 元iPhone 18 Pro Max电池服务：1,048 元背面玻璃损坏：1,298 元后置相机损坏：1,949 元屏幕损坏：3,198 元屏幕和背面玻璃损坏：3,929 元其他损坏：7,298 元" data-title="苹果公布 iPhone 18 Pro 系列手机维修预估费用：电池服务 1048 元，较前代上涨 79 元" data-date="09-11 19:32" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-11 19:32</span>
          <span class="news-item-title">苹果公布 iPhone 18 Pro 系列手机维修预估费用：电池服务 1048 元，较前代上涨 79 元</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/retro-gaming/neogeo-aes-console-remake-delayed-for-nearly-a-year-decision-driven-by-ram-shortage-and-unexpected-popularity" target="_blank" rel="noopener" data-cat="keji" data-summary="NeoGeo AES +控制台翻拍推迟了近一年—决定是由RAM短缺和意外流行推动的" data-title="由于内存短缺，硬件精确的NeoGeo AES +推迟到2027年底—由需求激增和人工智能驱动的RAM紧缩驱动的决策" data-date="09-11 19:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-11 19:30</span>
          <span class="news-item-title">由于内存短缺，硬件精确的NeoGeo AES +推迟到2027年底—由需求激增和人工智能驱动的RAM紧缩驱动的决策</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/436.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 11 日消息，长城旗下魏牌今日宣布，MPV 标杆新一代，高山 8/9 PHEV 新版型 9 月 14 日开启下订。IT之家注意到，根据规划，新成员将与现款车型并行销售，两种风格、两种定位满足不同用户需求，现款限时权益价 26.58 万元起。高山 9 PHEV 新版型标配二三排共轨、双零重力旋转座椅，空间更灵活，场景更丰富；标配 CoffeeOS4 座舱系统、高通 8797 芯片、双 500 万像素超广角座舱摄像头、29.6 英寸超大一体智慧屏，智能有情感，空间有陪伴；标配 Coffee Pilot 4 辅助驾驶系统、英伟达 Thor-U 芯片、前后双激光雷达，懂路更懂你，越开越好开；标配 2.0T 发动机 +Hi4 性能版智能四驱、全铝悬架 + 灵动转向，性能强劲又灵动。高" data-title="长城魏牌高山 8/9 PHEV 新版型 9 月 14 日开启下订，号称“MPV 标杆新一代”" data-date="09-11 19:26" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-11 19:26</span>
          <span class="news-item-title">长城魏牌高山 8/9 PHEV 新版型 9 月 14 日开启下订，号称“MPV 标杆新一代”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-11/10694911.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网9月11日电 据法新社报道，缅甸安全部门消息人士称，缅甸曼德勒机场因无人机袭击导致航班中断，将从当地时间11日开始关闭两天。" data-title="外媒：缅甸机场在无人机袭击后关闭" data-date="09-11 19:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 19:20</span>
          <span class="news-item-title">外媒：缅甸机场在无人机袭击后关闭</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/11/podcasts/the-headlines/jd-vance-iran-war-ai.html" target="_blank" rel="noopener" data-cat="keji" data-summary="此外，还有周五的新闻测验。" data-title="JD Vance对战争的了解，以及关于人工智能的新警告" data-date="09-11 19:14" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-11 19:14</span>
          <span class="news-item-title">JD Vance对战争的了解，以及关于人工智能的新警告</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/435.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 11 日消息，Linux Mint 今天（11 日）提前公布了计划于 2026 年圣诞节推出的下一版本 v23.0 部分新功能，其中最引人注目的是两款全新桌面应用，分别为日历应用 Clockenstein 和 EPUB 电子书阅读器 Xepub。Clockenstein 在桌面上将显示为“日历”，支持同时管理多个日历。用户可以直接创建和修改日程，并自行选择保存到哪个日历。Clockenstein 还配有独立的后台服务，负责持续同步各个日历。远程日历即使暂时断开连接，已有日程也不会消失，只会在连接恢复前变为只读状态。遇到同步失败或连接异常时，Clockenstein 也会立即发出提醒。关闭“日历”窗口不会影响日程提醒。Clockenstein 另有独立通知工具，可直接在桌面弹" data-title="Linux Mint 预告 v23.0“圣诞更新”：新增日历、电子书阅读器应用" data-date="09-11 19:11" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-11 19:11</span>
          <span class="news-item-title">Linux Mint 预告 v23.0“圣诞更新”：新增日历、电子书阅读器应用</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/001/434.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="9 月 8 日，Arm 在上海举办年度旗舰活动 Arm Everywhere China，并在会上发布了第二代移动终端计算子系统 CSS for Mobile 2。这是一个面向智能体 AI 与 AI 原生图形的计算平台，集成了 Arm C2 CPU 集群、Mali G2-Ultra NX GPU 以及 SI L2 系统互连，同时将系统 IP、软件和开发者工具整合为完整平台。如果只看新计算平台的命名，CSS for Mobile 2 看起来就是一次常规的更新迭代。但听完整场发布、又在采访中和 Arm 高管们聊过技术细节后，小编对于这次的新平台又有了新的认知。CSS for Mobile 2 每一项技术细节的升级，Arm 其实都在回答一个更根本的问题：当 AI 从问答助手进化成能理解意图、规划任" data-title="智能体时代的移动计算，Arm 通过一场大会给出自己的答案" data-date="09-11 19:08" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-11 19:08</span>
          <span class="news-item-title">智能体时代的移动计算，Arm 通过一场大会给出自己的答案</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-11/10694882.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网长沙9月11日电(记者 唐小晴)2026年“全国科普月”长沙主场活动11日在西湖科创园启动。活动以“科技改变生活 创新赢得未来——生命健康·科普护航”为主题，旨在助力长沙建设全球研发中心城市、培育新质生产力，挖掘储备创新后备人才。" data-title="2026年“全国科普月”长沙主场启幕 全域科普赋能城市创新" data-date="09-11 19:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 19:08</span>
          <span class="news-item-title">2026年“全国科普月”长沙主场启幕 全域科普赋能城市创新</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c1j4zydzk2zo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联在一次门票宣传调查后禁止了685个球迷账户，并坚称无辜的球迷没有受到惩罚。" data-title="曼联在兜售调查后禁止了 685 个球迷账户" data-date="09-11 19:33" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-11 19:33</span>
          <span class="news-item-title">曼联在兜售调查后禁止了 685 个球迷账户</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cx2zr11l9j6o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼城主教练恩佐·马雷斯卡（ Enzo Maresca ）表示，球队“需要适应”比赛日程安排，因为他的球队在周日的德比比赛中比对手曼联多休息两天。" data-title="团队需要适应夹具调度" data-date="09-11 18:55" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-11 18:55</span>
          <span class="news-item-title">团队需要适应夹具调度</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cgmrz1kdm93o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="BBC Sport FPL 专家 Holly Shand 探讨了 FPL 经理在进入第四周比赛时面临的一些最大困境，包括是队长埃尔林·哈兰德还是切尔西球员。" data-title="切尔西的三重进攻值得吗？ FPL比赛周的四个困境" data-date="09-11 14:28" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-11 14:28</span>
          <span class="news-item-title">切尔西的三重进攻值得吗？ FPL比赛周的四个困境</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cgmrz1kdm93o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英国广播公司体育FPL专家霍莉·尚德（ Holly Shand ）研究了FPL经理在进入第四周比赛时所面临的一些最大困境，包括队长是埃尔林·哈兰德（ Erling Haaland ）还是切尔西球员。" data-title="切尔西三次进攻值得吗？ FPL游戏周四难题" data-date="09-11 14:28" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-11 14:28</span>
          <span class="news-item-title">切尔西三次进攻值得吗？ FPL游戏周四难题</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/11/premier-league-10-things-to-look-out-for-this-weekend" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Nicolas Jackson is ready to impress, Spurs are scrambled and the 199th Manchester derby takes place at Old TraffordPremier League top scorers 2026-27: who is leading race for the golden boot?With 10 top-flight goal contributions between them across three games already this season, the Chelsea trio of Morgan Rogers, João Pedro and Cole Palmer are th" data-title="英超联赛：本周末需要注意的 10 件事" data-date="09-11 07:01" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-11 07:01</span>
          <span class="news-item-title">英超联赛：本周末需要注意的 10 件事</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/11/premier-league-10-things-to-look-out-for-this-weekend" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Nicolas Jackson is ready to impress, Spurs are scrambled and the 199th Manchester derby takes place at Old TraffordPremier League top scorers 2026-27: who is leading race for the golden boot?With 10 top-flight goal contributions between them across three games already this season, the Chelsea trio of Morgan Rogers, João Pedro and Cole Palmer are th" data-title="英超联赛：本周末需要注意的10件事" data-date="09-11 07:01" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-11 07:01</span>
          <span class="news-item-title">英超联赛：本周末需要注意的10件事</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c62mq8j4j5lo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="托特纳姆热刺队和他们的前锋理查利森就他剩余九个月的合同存在争议。" data-title="热刺与理查利森存在合同纠纷" data-date="09-11 02:48" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-11 02:48</span>
          <span class="news-item-title">热刺与理查利森存在合同纠纷</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c62mq8j4j5lo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="托特纳姆热刺和他们的前锋理查利森在合同的剩余9个月内存在争议。" data-title="马刺和Richarlison在合同纠纷中" data-date="09-11 02:48" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-11 02:48</span>
          <span class="news-item-title">马刺和Richarlison在合同纠纷中</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cd94y2vx8gno?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英超联赛今年将在节礼日举办七场比赛，比去年大幅增加。" data-title="七场英超联赛定于节礼日举行" data-date="09-10 22:40" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-10 22:40</span>
          <span class="news-item-title">七场英超联赛定于节礼日举行</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cgrvq2xp8dwo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="据信米克尔·阿尔特塔即将与英超冠军阿森纳敲定一份新合同。" data-title="阿森纳即将敲定阿尔特塔的新合同" data-date="09-10 22:16" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-10 22:16</span>
          <span class="news-item-title">阿森纳即将敲定阿尔特塔的新合同</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cgrvq2xp8dwo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="据信，米克尔·阿尔特塔（ Mikel Arteta ）即将与英超冠军阿森纳（ Arsenal ）敲定新合同。" data-title="阿森纳即将敲定Arteta的新合同" data-date="09-10 22:16" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-10 22:16</span>
          <span class="news-item-title">阿森纳即将敲定Arteta的新合同</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c0re0n84yz7o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="毛里西奥·波切蒂诺是否有理由认为托特纳姆热刺应该重新加冕英超冠军？" data-title="你能为切尔西被剥夺 2016 年资格提供理由吗" data-date="09-10 21:55" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-10 21:55</span>
          <span class="news-item-title">你能为切尔西被剥夺 2016 年资格提供理由吗</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c0re0n84yz7o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="毛里西奥·波切蒂诺是否有理由认为托特纳姆热刺应该重新加冕英超冠军？" data-title="你能为切尔西2016年被剥夺资格提供理由吗" data-date="09-10 21:55" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-10 21:55</span>
          <span class="news-item-title">你能为切尔西2016年被剥夺资格提供理由吗</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/10/premier-league-top-scorers-2026-27-race-for-golden-boot" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="了解哪些英格兰顶级联赛的神射手正在进球榜上一路高歌猛进 继续阅读..." data-title="2026-27赛季英超最佳射手：谁在金靴争夺战中领先？" data-date="09-10 21:43" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-10 21:43</span>
          <span class="news-item-title">2026-27赛季英超最佳射手：谁在金靴争夺战中领先？</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/10/premier-league-top-scorers-2026-27-race-for-golden-boot" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="找出哪位英国顶尖射手正在向进球排行榜射击。继续阅读……" data-title="2026-27赛季英超联赛最佳射手：谁是金靴赛的领跑者？" data-date="09-10 21:43" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-10 21:43</span>
          <span class="news-item-title">2026-27赛季英超联赛最佳射手：谁是金靴赛的领跑者？</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-11/10694941.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网哈尔滨9月11日电 (史轶夫 王迎春)在我们国家长护险制度从局部试点转向全国推行的大背景下，近日，黑龙江省出台了《黑龙江省建立长期护理保险制度实施方案》。9月11日，黑龙江省人民政府新闻办公室召开专题发布会，介绍和解读建立长期护理保险制度的相关政策和配套措施。" data-title="黑龙江全面推开长期护理保险制度 破解失能家庭“照护难”" data-date="09-11 20:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 20:05</span>
          <span class="news-item-title">黑龙江全面推开长期护理保险制度 破解失能家庭“照护难”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-11/10694920.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社北京9月11日电 (记者 刘大炜)古装微短剧《嘉庆君游台湾》11日在北京首映。" data-title="微短剧《嘉庆君游台湾》在北京首映" data-date="09-11 20:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 20:00</span>
          <span class="news-item-title">微短剧《嘉庆君游台湾》在北京首映</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-11/10694922.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社青海玉树9月11日电 题：访青海索南达杰自然保护站：“情”“法”共护“生命树”" data-title="访青海索南达杰自然保护站：“情”“法”共护“生命树”" data-date="09-11 19:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 19:43</span>
          <span class="news-item-title">访青海索南达杰自然保护站：“情”“法”共护“生命树”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-11/10694934.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="原标题：葫芦挂回去了！“葫芦娃爷爷”发声：许多人千里赶来只为看一眼，不能让他们热乎乎的心冷掉" data-title="葫芦挂回去了！“葫芦娃爷爷”发声：不能让游客的心冷掉" data-date="09-11 19:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 19:42</span>
          <span class="news-item-title">葫芦挂回去了！“葫芦娃爷爷”发声：不能让游客的心冷掉</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-11/10694926.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网杭州9月11日电(张煜欢)11日，浙江省“十五五”体育改革与发展规划新闻发布会在浙江杭州举行。浙江省体育局党组书记、局长金志在会上介绍，“十五五”期间，浙江将深入实施全民健身优享工程，持续扩容提质全民健身公共服务供给，构建更高水平、更全覆盖、更具质感的全民健身体系，助力现代化体育强省建设。" data-title="浙江升级全民健身公共服务体系 让民众健康动起来" data-date="09-11 19:38" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 19:38</span>
          <span class="news-item-title">浙江升级全民健身公共服务体系 让民众健康动起来</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-11/10694877.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社河南鹤壁9月11日电 题：一只泥咕咕 吹响千年非遗新声" data-title="（活力中国）一只泥咕咕 吹响千年非遗新声" data-date="09-11 19:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 19:30</span>
          <span class="news-item-title">（活力中国）一只泥咕咕 吹响千年非遗新声</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-11/10694903.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网广州9月11日电 (记者 王坚)广东省防汛防旱防风总指挥部办公室11日印发通知，部署各地各有关部门做好当前南海热带扰动防御工作，全力确保人民群众生命财产安全。" data-title="广东多举措防御南海热带扰动" data-date="09-11 19:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 19:23</span>
          <span class="news-item-title">广东多举措防御南海热带扰动</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-11/10694892.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网首尔9月11日电 (记者 金旭)《我的南京：一条记忆的江，流过我们，奔向未来之海》主题展览当地时间10日在韩国首尔大学开幕。活动通过主题展览、学术探讨、非遗体验和青年对话等形式，共同回望历史、共话和平。" data-title="《我的南京：一条记忆的江，流过我们，奔向未来之海》主题展览在韩国首尔举办" data-date="09-11 19:19" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 19:19</span>
          <span class="news-item-title">《我的南京：一条记忆的江，流过我们，奔向未来之海》主题展览在韩国首尔举办</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ce9e3d5exp8o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="纽卡斯尔联队后卫刘易斯·霍尔与俱乐部签订了一份新合同，合同有效期至2031年。" data-title="霍尔与纽卡斯尔签订新合同至2031年" data-date="09-11 16:00" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-11 16:00</span>
          <span class="news-item-title">霍尔与纽卡斯尔签订新合同至2031年</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cq63868gq5qo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="香港支联会“煽颠”案历经五年，三名核心人物的判刑结果尘埃落定。BBC中文访问李卓人的妻子邓燕娥及邹幸彤战友刘家仪，讲述他们如何面对香港的变迁和怎样陪伴在墙内的人。" data-title="香港支联会“煽动颠覆”案：被告们的伴侣与战友" data-date="09-11 15:48" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-11 15:48</span>
          <span class="news-item-title">香港支联会“煽动颠覆”案：被告们的伴侣与战友</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/ced75zwgd1lo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="美国民众很快将能再次到登机门送别亲友，这是相关改革措施的一部分。" data-title="911事件25年后 美国机场安检酝酿“松绑”：无票可到登机口送行、满瓶水可过安检" data-date="09-11 15:40" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-11 15:40</span>
          <span class="news-item-title">911事件25年后 美国机场安检酝酿“松绑”：无票可到登机口送行、满瓶水可过安检</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/11/nyregion/911-attacks-muslim-sikh-new-yorkers.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="袭击引发了一波仇恨浪潮，但此后几年，美国穆斯林的政治和文化影响力不断增强。" data-title="9/11之后，伊斯兰恐惧症塑造了一代穆斯林纽约人" data-date="09-11 15:00" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-11 15:00</span>
          <span class="news-item-title">9/11之后，伊斯兰恐惧症塑造了一代穆斯林纽约人</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-11/10694601.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="日常打车，计价器本该公开透明。可一旦计价器被非法改装，乘客很容易被多收费。近日，天津首例提供非法控制计算机信息系统工具案一审宣判，案件源于一起乘客投诉，多部门联合揭开了改装计价器背后的猫腻。" data-title="打车20元路程竟收40元？起底计价器虚增里程猫腻" data-date="09-11 14:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 14:41</span>
          <span class="news-item-title">打车20元路程竟收40元？起底计价器虚增里程猫腻</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cvgyj1x17vko/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="三人早于2021年9月被起诉，分别被判囚5至7年。支联会早前已宣告解散，结束32年历史。有香港市民在庭外排队旁听，表示过去几十年曾参加六四烛光晚会，形容案件犹如“对我的控诉”。" data-title="香港支联会“煽动颠覆”案：李卓人、邹幸彤、何俊仁判囚5至7年" data-date="09-11 14:37" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-11 14:37</span>
          <span class="news-item-title">香港支联会“煽动颠覆”案：李卓人、邹幸彤、何俊仁判囚5至7年</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-11/10694576.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网9月11日电 据北京市政府新闻办公室官方微博消息，9月10日，北京市十六届人大常委会第二十六次会议对《北京市博物馆条例(草案)》进行了二次审议。在一审稿提出鼓励博物馆延时、错时开放的基础上，二审稿进一步明确了更为刚性的要求：国家法定节假日和学校寒暑假期间，市属国家一级博物馆应当延时、错时开放。与此同时，“没有围墙的博物馆”这一馆城融合理念被写入草案，博物馆服务市民的便利度和可及性有望进一步提升。" data-title="北京：市属国家一级博物馆节假日寒暑假拟延时错时开放" data-date="09-11 14:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-11 14:24</span>
          <span class="news-item-title">北京：市属国家一级博物馆节假日寒暑假拟延时错时开放</span>
        </a>
  </div>
</div>

<script>
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
    const countEl = document.getElementById('news-search-count');
    if (countEl) countEl.innerText = '';
    return;
  }

  items.forEach(el => {
    const title = (el.getAttribute('data-title') || el.innerText || '').toLowerCase();
    const summary = (el.getAttribute('data-summary') || '').toLowerCase();
    const source = (el.getAttribute('data-source') || '').toLowerCase();
    const cat = (el.getAttribute('data-cat') || '').toLowerCase();
    const date = (el.getAttribute('data-date') || '').toLowerCase();
    const searchTarget = title + ' ' + summary + ' ' + source + ' ' + cat + ' ' + date;
    const isMatch = terms.every(t => searchTarget.includes(t));
    el.style.display = isMatch ? (el.classList.contains('news-item') ? 'flex' : 'block') : 'none';
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


---

<p class="news-updated">🕐 抓取更新于 2026-09-11 20:18（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
