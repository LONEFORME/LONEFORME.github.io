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
      <span>2026-11-21 16:54 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×22 · BBC×8</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">按来源聚合 · 最近 24 小时精选</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/11-21/10735773.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社快讯：神舟二十四号任务完成最后一次全区合练，发射场做好发射前各项准备。" data-title="神舟二十四号任务完成最后一次全区合练，发射场做好发射前各项准备" data-date="11-21 16:35" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 11-21 16:35</span>
      </div>
      <h2 class="hero-featured-title">神舟二十四号任务完成最后一次全区合练，发射场做好发射前各项准备</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/gn/2026/11-21/10735757.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新社重庆11月21日电 (记者 钟旖)国家人工智能应用中试基地(人力资源领域人力资源服务方向)21日在重庆揭牌，标志着行业人工智能应用从“技术突破”向“规模应用”迈出关键一步。" data-title="人力资源服务方向国家人工智能应用中试基地在重庆揭牌" data-date="11-21 16:37" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">人力资源服务方向国家人工智能应用中试基地在重庆揭牌</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/cv7028xeler2o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="当本·怀特在对阵世界冠军西班牙队时攻入英格兰的第三粒进球后庆祝离场时，这不仅仅是一粒进球，最终还成为了这场特殊胜利的制胜球。" data-title="Jeers, injuries and doubters - White&#39;s journey back to the top" data-date="11-21 14:17" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">嘲讽、伤病和质疑——怀特的巅峰回归之路</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/11-21/10735771.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网柳州11月21日电 11月20日，广西柳州市林业和园林局发布通报称，2026年10月，接到关于该市融水、三江两县出现涉非法猎捕贩卖野生鸟类的举报线索后，柳州市林业和园林局会同公安机关，对涉事区域实行全域拉网清查，对相关违法犯罪行为实施严厉打击。" data-title="广西柳州通报打击非法猎捕贩卖野生鸟类 抓捕涉案人员35人" data-date="11-21 16:47" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">广西柳州通报打击非法猎捕贩卖野生鸟类 抓捕涉案人员35人</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-21/10735773.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社快讯：神舟二十四号任务完成最后一次全区合练，发射场做好发射前各项准备。" data-title="神舟二十四号任务完成最后一次全区合练，发射场做好发射前各项准备" data-date="11-21 16:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-21 16:35</span>
          <span class="news-item-title">神舟二十四号任务完成最后一次全区合练，发射场做好发射前各项准备</span>
          <span class="news-value-point">💡 新华社快讯：神舟二十四号任务完成最后一次全区合练，发射场做好发射前各项准备</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-21/10735768.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网拉萨11月21日电 (李林)20日，阿里地区档案馆介绍，该馆已完成全部全宗、全部门类馆藏档案数字化加工工作，实现馆藏档案数字化全覆盖。" data-title="西藏阿里地区档案馆实现馆藏档案100%数字化" data-date="11-21 16:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-21 16:32</span>
          <span class="news-item-title">西藏阿里地区档案馆实现馆藏档案100%数字化</span>
          <span class="news-value-point">💡 中新网拉萨11月21日电 (李林)20日，阿里地区档案馆介绍，该馆已完成全部全宗、全部门类馆藏档案数字化加工工作，实现馆藏档案数字化全覆盖</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-21/10735764.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="亚太经合组织第三十三次领导人非正式会议日前在深圳落下帷幕，会议达成富有雄心、务实全面的《2026年亚太经合组织领导人深圳展望》(以下简称《深圳展望》)，持续引发外媒关注。" data-title="全球媒体聚焦丨为在变局中谋增长的亚太注入合作新动能" data-date="11-21 16:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-21 16:26</span>
          <span class="news-item-title">全球媒体聚焦丨为在变局中谋增长的亚太注入合作新动能</span>
          <span class="news-value-point">💡 亚太经合组织第三十三次领导人非正式会议日前在深圳落下帷幕，会议达成富有雄心、务实全面的《2026年亚太经合组织领导人深圳展望》(以下简称《深圳展…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-21/10735751.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网宜昌11月21日电 题：湖北兴山：有水喝、喝好水，就是村民最踏实的幸福感" data-title="湖北兴山：有水喝、喝好水，就是村民最踏实的幸福感" data-date="11-21 15:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-21 15:54</span>
          <span class="news-item-title">湖北兴山：有水喝、喝好水，就是村民最踏实的幸福感</span>
          <span class="news-value-point">💡 中新网宜昌11月21日电 题：湖北兴山：有水喝、喝好水，就是村民最踏实的幸福感</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-21/10735743.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网海口11月21日电(黄嘉雯) 烽火岁月铸就琼崖革命丰碑，开放潮头续写海南自贸港新篇。由中央网信办网络传播局指导，海南省委宣传部、海南省委网信办、海南省委省直机关工委、海南省委党史研究室(海南省地方志办公室)、共青团海南省委等单位联合主办的“红星照耀中国·从琼崖烽火到开放自贸港”网络主题宣传活动启动仪式，于11月20日在海南广播电视总台举行。" data-title="“红星照耀中国·从琼崖烽火到开放自贸港”网络主题宣传活动在海口启动" data-date="11-21 15:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-21 15:48</span>
          <span class="news-item-title">“红星照耀中国·从琼崖烽火到开放自贸港”网络主题宣传活动在海口启动</span>
          <span class="news-value-point">💡 中新网海口11月21日电(黄嘉雯) 烽火岁月铸就琼崖革命丰碑，开放潮头续写海南自贸港新篇</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-21/10735733.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月21日电(燕新台)美国总统特朗普在中美元首19日深圳会晤时明确表示，美国不支持“台独”。此番涉台表述引发岛内舆论高度关注。" data-title="岛内舆论高度关注特朗普不支持“台独”表态" data-date="11-21 15:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-21 15:36</span>
          <span class="news-item-title">岛内舆论高度关注特朗普不支持“台独”表态</span>
          <span class="news-value-point">💡 中新网11月21日电(燕新台)美国总统特朗普在中美元首19日深圳会晤时明确表示，美国不支持“台独”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-21/10735663.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月21日电 据沙特《利雅得报》当地时间21日凌晨报道，沙特阿拉伯主导的多国联军称摧毁了也门胡塞武装向沙特首都利雅得发射的三枚弹道导弹。" data-title="沙特称拦截3枚胡塞武装导弹 也门媒体称沙特袭击致41死" data-date="11-21 11:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-21 11:33</span>
          <span class="news-item-title">沙特称拦截3枚胡塞武装导弹 也门媒体称沙特袭击致41死</span>
          <span class="news-value-point">💡 中新社北京11月21日电 据沙特《利雅得报》当地时间21日凌晨报道，沙特阿拉伯主导的多国联军称摧毁了也门胡塞武装向沙特首都利雅得发射的三枚弹道导…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-21/10735662.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社秘鲁钱凯11月20日电 题：探访秘鲁钱凯港：跨越太平洋的发展新机遇" data-title="探访秘鲁钱凯港：跨越太平洋的发展新机遇" data-date="11-21 11:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-21 11:32</span>
          <span class="news-item-title">探访秘鲁钱凯港：跨越太平洋的发展新机遇</span>
          <span class="news-value-point">💡 中新社秘鲁钱凯11月20日电 题：探访秘鲁钱凯港：跨越太平洋的发展新机遇</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-21/10735674.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月21日电 综合外媒报道，当地时间20日，丹麦外交大臣拉斯穆森宣布，丹麦决定驱逐俄罗斯驻丹麦国防武官，要求其在7日内离境。俄外交部表示，将对丹麦驱逐其武官一事“作出适当回应”。" data-title="丹麦驱逐俄罗斯武官，俄表示将“适当回应”" data-date="11-21 11:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-21 11:27</span>
          <span class="news-item-title">丹麦驱逐俄罗斯武官，俄表示将“适当回应”</span>
          <span class="news-value-point">💡 中新网11月21日电 综合外媒报道，当地时间20日，丹麦外交大臣拉斯穆森宣布，丹麦决定驱逐俄罗斯驻丹麦国防武官，要求其在7日内离境</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-21/10735660.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月21日电 据美联社报道，美国总统特朗普当地时间20日表示，伊朗希望达成一项结束伊美敌对行动的协议，但伊朗方面想要的并非他所能接受的协议。" data-title="特朗普称无法接受伊朗想达成的协议 重申伊朗“永远不会拥有核武器”" data-date="11-21 10:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-21 10:31</span>
          <span class="news-item-title">特朗普称无法接受伊朗想达成的协议 重申伊朗“永远不会拥有核武器”</span>
          <span class="news-value-point">💡 中新网11月21日电 据美联社报道，美国总统特朗普当地时间20日表示，伊朗希望达成一项结束伊美敌对行动的协议，但伊朗方面想要的并非他所能接受的协…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-21/10735659.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社东京11月20日电(记者梁晨 李子越)据日本共同社20日报道，日本政府为年底修订“安保三文件”拟定的草案内容曝光。草案提出“启动研究”引进核动力潜艇问题，并允许在紧急情况下将核武器运进日本。" data-title="日媒：日本研究引进核潜艇及为“无核三原则”设例外" data-date="11-21 10:25" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-21 10:25</span>
          <span class="news-item-title">日媒：日本研究引进核潜艇及为“无核三原则”设例外</span>
          <span class="news-value-point">💡 新华社东京11月20日电(记者梁晨 李子越)据日本共同社20日报道，日本政府为年底修订“安保三文件”拟定的草案内容曝光</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-21/10735636.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网雅加达11月21日电 (记者 李志全)心联通·文互鉴——“讲中国故事”暨印尼摄影家赴福建采风成果展20日在雅加达举行。" data-title="“讲中国故事”暨印尼摄影家赴福建采风成果展在雅加达举行" data-date="11-21 10:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-21 10:05</span>
          <span class="news-item-title">“讲中国故事”暨印尼摄影家赴福建采风成果展在雅加达举行</span>
          <span class="news-value-point">💡 中新网雅加达11月21日电 (记者 李志全)心联通·文互鉴——“讲中国故事”暨印尼摄影家赴福建采风成果展20日在雅加达举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-21/10735614.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社伦敦11月20日电 (记者 欧阳开宇)英国内政部20日宣布，英国政府持续推进移民庇护制度改革，再度关停多处用于安置寻求庇护者的临时酒店，进一步缓解地方社区公共服务压力，压降庇护安置财政成本。" data-title="英国推进移民制度改革 持续关停庇护安置酒店" data-date="11-21 10:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-21 10:05</span>
          <span class="news-item-title">英国推进移民制度改革 持续关停庇护安置酒店</span>
          <span class="news-value-point">💡 中新社伦敦11月20日电 (记者 欧阳开宇)英国内政部20日宣布，英国政府持续推进移民庇护制度改革，再度关停多处用于安置寻求庇护者的临时酒店，进…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-21/10735613.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社华盛顿11月20日电 (记者 陈孟统)美国总统特朗普20日在白宫表示，美国、中国和俄罗斯三国领导人日前在中国深圳举行首次三方会晤，这是“一场具有重大历史意义的国际峰会”。" data-title="特朗普：中俄美元首会晤具有重大历史意义" data-date="11-21 10:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-21 10:04</span>
          <span class="news-item-title">特朗普：中俄美元首会晤具有重大历史意义</span>
          <span class="news-value-point">💡 中新社华盛顿11月20日电 (记者 陈孟统)美国总统特朗普20日在白宫表示，美国、中国和俄罗斯三国领导人日前在中国深圳举行首次三方会晤，这是“一…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/entertainment/1038410/andrey-zvyagintsev-minotaur-interview-director" target="_blank" rel="noopener" data-cat="shizheng" data-summary="故事发生在2022年。弗拉基米尔·普京宣布征兵。在安德烈·萨金采夫的《牛头怪》中，故事发生在虚构的克拉索博尔斯克镇，一对名为格列布和加利娜的夫妻默默无闻地过着不幸福的生活，或者说试图过着这样的生活，尽管地缘政治局势动荡不安。" data-title="Andrey Zvyagintsev believes filmmakers know what the audience wants" data-date="11-21 00:00" data-source="The Verge">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-21 00:00</span>
          <span class="news-item-title">安德烈·萨金塞夫认为，电影人知道观众想要什么</span>
          <span class="news-item-title-en">Andrey Zvyagintsev believes filmmakers know what the audience wants</span>
          <span class="news-value-point">💡 故事发生在2022年</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-21/10735757.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新社重庆11月21日电 (记者 钟旖)国家人工智能应用中试基地(人力资源领域人力资源服务方向)21日在重庆揭牌，标志着行业人工智能应用从“技术突破”向“规模应用”迈出关键一步。" data-title="人力资源服务方向国家人工智能应用中试基地在重庆揭牌" data-date="11-21 16:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-21 16:37</span>
          <span class="news-item-title">人力资源服务方向国家人工智能应用中试基地在重庆揭牌</span>
          <span class="news-value-point">💡 中新社重庆11月21日电 (记者 钟旖)国家人工智能应用中试基地(人力资源领域人力资源服务方向)21日在重庆揭牌，标志着行业人工智能应用从“技术…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/410.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 21 日消息，蔚来今日宣布，在即将于 11 月 25 日举办的 NIO IN 2026 蔚来创新科技日上，将正式发布 NWM 3.0 世界模型。官方表示，NWM 3.0 将会在模型架构、闭环训练、跨域融合等方面，带来蔚来智能辅助驾驶团队对物理世界人工智能的最新思考与探索成果，敬请期待。据IT之家此前报道，2024 年 7 月，蔚来发布行业首个智能辅助驾驶世界模型 ——“蔚来世界模型 NWM”（NIO World Model）。据介绍，蔚来世界模型是一个多元自回归生成模型，可全量理解数据、长时序推演和决策，具备像人一样“空间认知-想象重建”和“时间认知-想象推演”的能力，并且可以输出规划轨迹。相比常规的端到端架构，蔚来世界模型在空间理解上，通过生成式模型重构传感器输入，更加" data-title="蔚来官宣 NWM 3.0 世界模型，11 月 25 日在 NIO IN 2026 蔚来创新科技日发布" data-date="11-21 16:33" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-21 16:33</span>
          <span class="news-item-title">蔚来官宣 NWM 3.0 世界模型，11 月 25 日在 NIO IN 2026 蔚来创新科技日发布</span>
          <span class="news-value-point">💡 IT之家 11 月 21 日消息，蔚来今日宣布，在即将于 11 月 25 日举办的 NIO IN 2026 蔚来创新科技日上，将正式发布 NWM…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/409.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 21 日消息，博主 @数码闲聊站 今天（21 日）下午爆料称，当下手机市场“阔形态”升级势不可挡：除了华为，其他家也考虑在正代旗舰线加入阔形态，与常规直板机双线并行。@数码闲聊站 在回复网友评论时还透露，安卓阵营中，阔直板与常规直板双线并行，且常规直板机定位高于阔直板；“真小屏手机”今后将会越来越少。综合IT之家此前报道，本月早些时候的消息称，华为 Pura X View 阔直板手机上市 66 天，激活销量已突破 100 万台。此外，预计属于 OPPO 的阔折也已经蓄势待发，搭载 2nm 骁龙 AI 旗舰芯，采用宽屏无感折痕设计，后置 2 亿云台影像；阔直板手机加速推进中，搭载天玑 9 旗舰芯，配备 16:9 窄边框定制屏，后置 2 亿大底影像。同样在本月上旬，安卓阵营首" data-title="不只是华为，消息称其他厂商也考虑为旗舰产品线引入阔直板形态" data-date="11-21 16:27" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-21 16:27</span>
          <span class="news-item-title">不只是华为，消息称其他厂商也考虑为旗舰产品线引入阔直板形态</span>
          <span class="news-value-point">💡 IT之家 11 月 21 日消息，博主 @数码闲聊站 今天（21 日）下午爆料称，当下手机市场“阔形态”升级势不可挡：除了华为，其他家也考虑在正…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/20/business/nvidia-sec-accounting.html" target="_blank" rel="noopener" data-cat="keji" data-summary="在有关该公司在亚洲存在可疑芯片销售行为的爆料中，围绕该公司会计事务的问题浮出水面。" data-title="Nvidia Said to Face S.E.C. Probe Into Its Accounting Practices" data-date="11-21 09:06" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-21 09:06</span>
          <span class="news-item-title">据称Nvidia正面临美国证券交易委员会对其会计做法的调查</span>
          <span class="news-item-title-en">Nvidia Said to Face S.E.C. Probe Into Its Accounting Practices</span>
          <span class="news-value-point">💡 在有关该公司在亚洲存在可疑芯片销售行为的爆料中，围绕该公司会计事务的问题浮出水面</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/20/science/anthropic-ai-math-riemann-hypothesis.html" target="_blank" rel="noopener" data-cat="keji" data-summary="如果得到证实，黎曼猜想的证明将巩固该领域的这一认识，即没有哪个未解问题能幸免于人工智能。" data-title="Anthropic Mathematician Claims to Solve Riemann Hypothesis With Help From Claude" data-date="11-21 08:33" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-21 08:33</span>
          <span class="news-item-title">Anthropic 数学家声称在 Claude 的帮助下解决了黎曼猜想</span>
          <span class="news-item-title-en">Anthropic Mathematician Claims to Solve Riemann Hypothesis With Help From Claude</span>
          <span class="news-value-point">💡 如果得到证实，黎曼猜想的证明将巩固该领域的这一认识，即没有哪个未解问题能幸免于人工智能</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/20/daniel-ek-backs-ai-researchers-fusion-power-startup-heres-what-theyre-building/" target="_blank" rel="noopener" data-cat="keji" data-summary="Spotify创始人丹尼尔·埃克（Daniel Ek）正在支持Europa Fusion，这是一家由人工智能研究员创立的聚变能初创公司。以下是这家初创公司正在打造的产品。" data-title="Daniel Ek backs AI researcher’s fusion power startup. Here’s what they’re building." data-date="11-21 03:53" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-21 03:53</span>
          <span class="news-item-title">丹尼尔·埃克支持人工智能研究人员的聚变能初创公司。以下是他们正在打造的项目。</span>
          <span class="news-item-title-en">Daniel Ek backs AI researcher’s fusion power startup. Here’s what they’re building.</span>
          <span class="news-value-point">💡 Spotify创始人丹尼尔·埃克（Daniel Ek）正在支持Europa Fusion，这是一家由人工智能研究员创立的聚变能初创公司</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/20/ai-claimed-a-solution-to-the-167-year-old-riemann-hypothesis-and-a-human-did-too/" target="_blank" rel="noopener" data-cat="keji" data-summary="最新的AI驱动的结果让数学家们大为震惊——而且还有一种与之竞争的人类解决方案。" data-title="AI claimed a solution to the 167-year-old Riemann hypothesis — and a human did, too" data-date="11-21 03:32" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-21 03:32</span>
          <span class="news-item-title">人工智能声称解决了有167年历史的黎曼猜想——人类也解决了</span>
          <span class="news-item-title-en">AI claimed a solution to the 167-year-old Riemann hypothesis — and a human did, too</span>
          <span class="news-value-point">💡 最新的AI驱动的结果让数学家们大为震惊——而且还有一种与之竞争的人类解决方案</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/policy/1038892/trump-foreign-data-centers-tax" target="_blank" rel="noopener" data-cat="keji" data-summary="唐纳德·特朗普总统承诺对在美国境外建设数据中心的公司征收“巨额税”，尽管美国各州和各城市正在对新建数据中心的新申请施加限制。“我们不会允许我们的……" data-title="Trump threatens ‘tremendous tax’ for moving AI data centers outside the US" data-date="11-21 02:50" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-21 02:50</span>
          <span class="news-item-title">特朗普威胁要对将人工智能数据中心迁至美国境外征收“巨额税款”</span>
          <span class="news-item-title-en">Trump threatens ‘tremendous tax’ for moving AI data centers outside the US</span>
          <span class="news-value-point">💡 唐纳德·特朗普总统承诺对在美国境外建设数据中心的公司征收“巨额税”，尽管美国各州和各城市正在对新建数据中心的新申请施加限制</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/20/us/politics/nvidia-alice-huang-chips-china.html" target="_blank" rel="noopener" data-cat="keji" data-summary="与Nvidia丑闻核心人物黄仁勋有关联的公司，是需要先进算力的中国科技公司和国防承包商网络的一部分。" data-title="Alice Huang, Accused of Spying on Nvidia’s CEO, Is Linked to Firms With Ties to China’s Military" data-date="11-21 02:05" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-21 02:05</span>
          <span class="news-item-title">被指控监视英伟达首席执行官的Alice Huang与多家与中国军方有联系的公司有关联</span>
          <span class="news-item-title-en">Alice Huang, Accused of Spying on Nvidia’s CEO, Is Linked to Firms With Ties to China’s Military</span>
          <span class="news-value-point">💡 与Nvidia丑闻核心人物黄仁勋有关联的公司，是需要先进算力的中国科技公司和国防承包商网络的一部分</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1010051/anthropic-riemann-hypothesis-millennium-prize-problem" target="_blank" rel="noopener" data-cat="keji" data-summary="Anthropic 的数学家 Levent Alpöge 声称，在 Claude 的帮助下，他证明了黎曼猜想——数学界最臭名昭著的难题之一，破解了这个困扰世界顶级数学家数十年的谜题。" data-title="Anthropic mathematician claims to have solved prestigious Millennium Prize problem with Claude" data-date="11-21 00:34" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-21 00:34</span>
          <span class="news-item-title">Anthropic 的数学家声称已使用 Claude 解决了著名的千年大奖难题</span>
          <span class="news-item-title-en">Anthropic mathematician claims to have solved prestigious Millennium Prize problem with Claude</span>
          <span class="news-value-point">💡 Anthropic 的数学家 Levent Alpöge 声称，在 Claude 的帮助下，他证明了黎曼猜想——数学界最臭名昭著的难题之一，破解…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-mathematician-claims-to-have-solved-167-year-old-math-problem-with-claude-riemann-hypothesis-proof-allegedly-discovered-but-remains-unconfirmed" target="_blank" rel="noopener" data-cat="keji" data-summary="一位人类数学家声称使用 Claude 解决了黎曼猜想。" data-title="Anthropic mathematician claims to have solved 167-year-old math problem with Claude" data-date="11-21 00:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-21 00:30</span>
          <span class="news-item-title">Anthropic 数学家声称已借助 Claude 解决了有 167 年历史的数学难题</span>
          <span class="news-item-title-en">Anthropic mathematician claims to have solved 167-year-old math problem with Claude</span>
          <span class="news-value-point">💡 一位人类数学家声称使用 Claude 解决了黎曼猜想</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/278.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 20 日消息，据《科学美国人》报道，当地时间 20 日，Anthropic 数学家莱文特 · 阿尔波格宣称，自己与 AI 模型 Claude 合作，攻克了数学界最著名的难题之一 —— 黎曼猜想。阿尔波格在个人网站发表声明称：“我相信，我与 Claude 合作找到了黎曼猜想的证明。”IT之家注：黎曼猜想由德国数学家伯恩哈德 · 黎曼于 1859 年提出，认为看似随机分布在数轴上的质数，实际上遵循着复杂而有意义的规律。此后，黎曼猜想成为整个数论研究领域的重要指引，也是数学界最著名的未解难题。由于长期缺乏明确的证明思路，研究进展极其有限，就连顶尖数学家也很少花费大量时间直接尝试证明。直到今年 10 月，OpenAI 集中公布的一批数学研究成果中，有一项证明在揭示质数分布规律方面" data-title="AI 攻克黎曼猜想？Anthropic 数学家宣称已与 Claude 合作完成证明" data-date="11-20 23:37" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-20 23:37</span>
          <span class="news-item-title">AI 攻克黎曼猜想？Anthropic 数学家宣称已与 Claude 合作完成证明</span>
          <span class="news-value-point">💡 IT之家 11 月 20 日消息，据《科学美国人》报道，当地时间 20 日，Anthropic 数学家莱文特 · 阿尔波格宣称，自己与 AI 模…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/podcast/the-fallout-from-nvidias-jensen-huang-scandal-continues/" target="_blank" rel="noopener" data-cat="keji" data-summary="在应对罢免首席执行官黄仁勋所带来的影响之际，英伟达本周发布了最新财报，显示出稳健的增长态势，并承诺美好势头将持续下去。与此同时，这家芯片制造商表示将停止" data-title="The fallout from Nvidia’s Jensen Huang scandal continues" data-date="11-20 22:55" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-20 22:55</span>
          <span class="news-item-title">英伟达黄仁勋丑闻的影响仍在持续</span>
          <span class="news-item-title-en">The fallout from Nvidia’s Jensen Huang scandal continues</span>
          <span class="news-value-point">💡 在应对罢免首席执行官黄仁勋所带来的影响之际，英伟达本周发布了最新财报，显示出稳健的增长态势，并承诺美好势头将持续下去</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/20/technology/jensen-huang-nvidia-culture.html" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达联合创始人对员工的贬损行为可以追溯到几十年前。这种行为曾导致与一位高管达成保密和解协议，该高管称黄先生“恐吓”员工。" data-title="How Jensen Huang Made Humiliation Routine at Nvidia" data-date="11-20 22:43" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-20 22:43</span>
          <span class="news-item-title">黄仁勋是如何在英伟达将羞辱常态化的</span>
          <span class="news-item-title-en">How Jensen Huang Made Humiliation Routine at Nvidia</span>
          <span class="news-value-point">💡 英伟达联合创始人对员工的贬损行为可以追溯到几十年前</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/19/your-money/anthropic-ipo-investing.html" target="_blank" rel="noopener" data-cat="keji" data-summary="将您的财富中很大一部分投入到一只股票上绝不是一个好主意，但如果您有投资的冲动，请先问自己几个问题。" data-title="Should You Invest in Anthropic? Here’s What to Consider." data-date="11-20 22:39" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-20 22:39</span>
          <span class="news-item-title">您应该投资Anthropic吗？以下是需要考虑的事项。</span>
          <span class="news-item-title-en">Should You Invest in Anthropic? Here’s What to Consider.</span>
          <span class="news-value-point">💡 将您的财富中很大一部分投入到一只股票上绝不是一个好主意，但如果您有投资的冲动，请先问自己几个问题</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cv7028xeler2o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="当本·怀特在对阵世界冠军西班牙队时攻入英格兰的第三粒进球后庆祝离场时，这不仅仅是一粒进球，最终还成为了这场特殊胜利的制胜球。" data-title="Jeers, injuries and doubters - White&#39;s journey back to the top" data-date="11-21 14:17" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-21 14:17</span>
          <span class="news-item-title">嘲讽、伤病和质疑——怀特的巅峰回归之路</span>
          <span class="news-item-title-en">Jeers, injuries and doubters - White's journey back to the top</span>
          <span class="news-value-point">💡 当本·怀特在对阵世界冠军西班牙队时攻入英格兰的第三粒进球后庆祝离场时，这不仅仅是一粒进球，最终还成为了这场特殊胜利的制胜球</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cwd01n9z23x5o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在确认毛里西奥·波切蒂诺将成为新任主教练的三天后，曼联借款 1000 万英镑，其中 750 万英镑将用于向美国足球协会支付赔偿金。" data-title="Cost of Man Utd hiring and firing managers nears £100m" data-date="11-21 07:18" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-21 07:18</span>
          <span class="news-item-title">曼联聘请和解雇教练的费用接近1亿英镑</span>
          <span class="news-item-title-en">Cost of Man Utd hiring and firing managers nears £100m</span>
          <span class="news-value-point">💡 在确认毛里西奥·波切蒂诺将成为新任主教练的三天后，曼联借款 1000 万英镑，其中 750 万英镑将用于向美国足球协会支付赔偿金</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmg46k97k92do?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="美国橄榄球巨星汤姆·布雷迪正计划通过所有权集团Clearlake Capital投资切尔西。" data-title="NFL great Brady could buy Chelsea stake" data-date="11-21 06:36" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-21 06:36</span>
          <span class="news-item-title">NFL巨星布雷迪可能收购切尔西股份</span>
          <span class="news-item-title-en">NFL great Brady could buy Chelsea stake</span>
          <span class="news-value-point">💡 美国橄榄球巨星汤姆·布雷迪正计划通过所有权集团Clearlake Capital投资切尔西</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/20/premier-league-news-everton-jack-grealish-manchester-city-liverpool-chelsea" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="埃弗顿的组织核心在下课后回归，而利物浦的主教练则专注于安菲尔德的对决。继续阅读……" data-title="Premier League news: Moyes demands more from Grealish, Iraola wary of United threat" data-date="11-21 06:31" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-21 06:31</span>
          <span class="news-item-title">英超联赛新闻：莫耶斯要求格拉利什有更好的表现，伊拉奥拉对曼联的威胁保持警惕</span>
          <span class="news-item-title-en">Premier League news: Moyes demands more from Grealish, Iraola wary of United threat</span>
          <span class="news-value-point">💡 埃弗顿的组织核心在下课后回归，而利物浦的主教练则专注于安菲尔德的对决</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c678299n1018o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在考文垂队被埃弗顿队判罚点球无效后，考文垂队主教练弗兰克·兰帕德希望裁判们花时间确保他们做出正确的判罚。" data-title="Lampard calls for fairness after Coventry penalty row" data-date="11-21 06:04" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-21 06:04</span>
          <span class="news-item-title">兰帕德在考文垂点球争议后呼吁公平</span>
          <span class="news-item-title-en">Lampard calls for fairness after Coventry penalty row</span>
          <span class="news-value-point">💡 在考文垂队被埃弗顿队判罚点球无效后，考文垂队主教练弗兰克·兰帕德希望裁判们花时间确保他们做出正确的判罚</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cjn502n9vqp4o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="米哈伊洛·穆德里克指责乌克兰传奇人物安德烈·舍甫琴科就其药检呈阳性的相关情况撒谎，而他与该国足球协会的争端仍在继续。" data-title="Shevchenko lying about drugs test claims" data-date="11-21 05:54" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-21 05:54</span>
          <span class="news-item-title">舍甫琴科就药物检测结果撒谎</span>
          <span class="news-item-title-en">Shevchenko lying about drugs test claims</span>
          <span class="news-value-point">💡 米哈伊洛·穆德里克指责乌克兰传奇人物安德烈·舍甫琴科就其药检呈阳性的相关情况撒谎，而他与该国足球协会的争端仍在继续</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13614508/liverpool-virgil-van-dijk-uncertain-on-anfield-future-beyond-the-summer-but-believes-he-can-play-for-many-more-years" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦队长维吉尔·范戴克（Virgil van Dijk）认为他还能再踢“很多年”的球，但他表示，自己还不知道下赛季是否会在安菲尔德球场效力。" data-title="Van Dijk uncertain on Liverpool future" data-date="11-21 04:15" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-21 04:15</span>
          <span class="news-item-title">范迪克对自己在利物浦的未来不确定</span>
          <span class="news-item-title-en">Van Dijk uncertain on Liverpool future</span>
          <span class="news-value-point">💡 利物浦队长维吉尔·范戴克（Virgil van Dijk）认为他还能再踢“很多年”的球，但他表示，自己还不知道下赛季是否会在安菲尔德球场效力</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13614363/mauricio-pochettino-manchester-united-head-coach-discusses-drone-footage-his-approach-to-data-and-bruno-fernandes-ahead-of-first-game" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在执教曼联的首场比赛对阵利物浦之前，毛里西奥·波切蒂诺对无人机拍摄的曼联训练视频可能带来的好处提出了质疑。" data-title="Drones, data and Bruno - Pochettino on his early Man Utd challenges" data-date="11-21 04:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-21 04:00</span>
          <span class="news-item-title">无人机、数据和布鲁诺——波切蒂诺谈论他在曼联面临的早期挑战</span>
          <span class="news-item-title-en">Drones, data and Bruno - Pochettino on his early Man Utd challenges</span>
          <span class="news-value-point">💡 在执教曼联的首场比赛对阵利物浦之前，毛里西奥·波切蒂诺对无人机拍摄的曼联训练视频可能带来的好处提出了质疑</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13614363/mauricio-pochettino-manchester-united-head-coach-discusses-drone-footage-his-approach-to-data-and-bruno-fernandes-ahead-of-first-game" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在执教曼联的首场比赛对阵利物浦之前，毛里西奥·波切蒂诺对无人机拍摄的曼联训练视频可能带来的好处提出了质疑。" data-title="Drones, data and Bruno - Pochettino on his early Man Utd challenges" data-date="11-21 04:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-21 04:00</span>
          <span class="news-item-title">无人机、数据和布鲁诺——波切蒂诺谈论他在曼联面临的早期挑战</span>
          <span class="news-item-title-en">Drones, data and Bruno - Pochettino on his early Man Utd challenges</span>
          <span class="news-value-point">💡 在执教曼联的首场比赛对阵利物浦之前，毛里西奥·波切蒂诺对无人机拍摄的曼联训练视频可能带来的好处提出了质疑</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/nov/20/weekend-football-countdown-live-news-updates" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="周末前的最新足球新闻，毛里西奥·波切蒂诺正准备率领曼联前往安菲尔德⚽ 赛程 | 排行榜 | 十大看点一名利物浦球迷被指控对安托万·塞梅尼奥进行种族歧视，但被判无罪" data-title="Pochettino demands say on big United decisions; Arteta takes fantasy football action" data-date="11-21 03:03" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-21 03:03</span>
          <span class="news-item-title">波切蒂诺要求在曼联重大决策中有发言权；阿尔特塔采取梦幻足球行动</span>
          <span class="news-item-title-en">Pochettino demands say on big United decisions; Arteta takes fantasy football action</span>
          <span class="news-value-point">💡 周末前的最新足球新闻，毛里西奥·波切蒂诺正准备率领曼联前往安菲尔德⚽ 赛程 | 排行榜 | 十大看点一名利物浦球迷被指控对安托万·塞梅尼奥进行种…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cvj6l7pd1yd0o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="水晶宫前锋伊斯梅拉·萨尔表示，他已经不再在意利物浦对签下他的兴趣，并渴望在托马斯·弗兰克的带领下“重新开始”。" data-title="Sarr focused on Palace return after Liverpool interest" data-date="11-21 02:41" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-21 02:41</span>
          <span class="news-item-title">在利物浦表现出兴趣后，萨尔将重心放在重返水晶宫上</span>
          <span class="news-item-title-en">Sarr focused on Palace return after Liverpool interest</span>
          <span class="news-value-point">💡 水晶宫前锋伊斯梅拉·萨尔表示，他已经不再在意利物浦对签下他的兴趣，并渴望在托马斯·弗兰克的带领下“重新开始”</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/20/premier-league-team-news-predicted-lineups-for-the-weekend-action" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="纽卡斯尔将于周六主场迎战阿森纳，而毛里西奥·波切蒂诺的曼联将于周日客场挑战利物浦。周六下午12:30 TNT Sports 1 频道，比赛地点：伊蒂哈德体育场。继续阅读……" data-title="Premier League team news: predicted lineups for the weekend action" data-date="11-21 02:03" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-21 02:03</span>
          <span class="news-item-title">英超球队新闻：周末动作的预测阵容</span>
          <span class="news-item-title-en">Premier League team news: predicted lineups for the weekend action</span>
          <span class="news-value-point">💡 纽卡斯尔将于周六主场迎战阿森纳，而毛里西奥·波切蒂诺的曼联将于周日客场挑战利物浦</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cwyvde0n8zqyo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英格兰足球总会（FA）对切尔西处以15万英镑的罚款，原因是该队在1月份足总杯第三轮对阵查尔顿的胜利比赛中出现了反天主教和反爱尔兰的喊叫声。" data-title="Chelsea fined £150,000 for discriminatory chanting" data-date="11-21 01:52" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-21 01:52</span>
          <span class="news-item-title">切尔西因歧视性喊叫被罚款15万英镑</span>
          <span class="news-item-title-en">Chelsea fined £150,000 for discriminatory chanting</span>
          <span class="news-value-point">💡 英格兰足球总会（FA）对切尔西处以15万英镑的罚款，原因是该队在1月份足总杯第三轮对阵查尔顿的胜利比赛中出现了反天主教和反爱尔兰的喊叫声</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/video/2026/nov/20/brightons-fabian-hurzeler-on-what-the-club-looks-for-when-signing-players-video" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="继续阅读。" data-title="Brighton&#39;s Fabian Hürzeler on what the club looks for when signing players" data-date="11-21 01:52" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-21 01:52</span>
          <span class="news-item-title">布莱顿的法比安·许策勒谈俱乐部在签约球员时看重哪些方面</span>
          <span class="news-item-title-en">Brighton's Fabian Hürzeler on what the club looks for when signing players</span>
          <span class="news-value-point">💡 继续阅读</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cwz0k32j9kr9o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联首席执行官奥马尔·贝拉达（Omar Berrada）表示，最近对俱乐部高层的批评中，有些“越过了界限”。" data-title="Man Utd fan criticism has gone too far at times" data-date="11-21 00:55" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-21 00:55</span>
          <span class="news-item-title">曼联球迷的批评有时太过分了</span>
          <span class="news-item-title-en">Man Utd fan criticism has gone too far at times</span>
          <span class="news-value-point">💡 曼联首席执行官奥马尔·贝拉达（Omar Berrada）表示，最近对俱乐部高层的批评中，有些“越过了界限”</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-21/10735771.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网柳州11月21日电 11月20日，广西柳州市林业和园林局发布通报称，2026年10月，接到关于该市融水、三江两县出现涉非法猎捕贩卖野生鸟类的举报线索后，柳州市林业和园林局会同公安机关，对涉事区域实行全域拉网清查，对相关违法犯罪行为实施严厉打击。" data-title="广西柳州通报打击非法猎捕贩卖野生鸟类 抓捕涉案人员35人" data-date="11-21 16:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-21 16:47</span>
          <span class="news-item-title">广西柳州通报打击非法猎捕贩卖野生鸟类 抓捕涉案人员35人</span>
          <span class="news-value-point">💡 中新网柳州11月21日电 11月20日，广西柳州市林业和园林局发布通报称，2026年10月，接到关于该市融水、三江两县出现涉非法猎捕贩卖野生鸟类…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-21/10735758.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网南京11月21日电 (记者 徐珊珊)记者20日从紫金山实验室召开的新闻通气会上获悉，第六届新一代通信网内生安全学术大会暨第九届“强网”拟态防御国际精英挑战赛将于12月3日至6日在南京举办。同期，还将举办IEEE CRESS2026国际会议。" data-title="聚焦AI攻防变局 第六届新一代通信网内生安全大会12月南京举行" data-date="11-21 16:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-21 16:45</span>
          <span class="news-item-title">聚焦AI攻防变局 第六届新一代通信网内生安全大会12月南京举行</span>
          <span class="news-value-point">💡 中新网南京11月21日电 (记者 徐珊珊)记者20日从紫金山实验室召开的新闻通气会上获悉，第六届新一代通信网内生安全学术大会暨第九届“强网”拟态…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/415.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 21 日消息，技嘉旗下钛金雕 GP-AP1600TM 钛金电源现已在京东发售，定价为 4599 元，提供 10 年质保。京东技嘉（GIGABYTE）钛金雕 GP-AP1600TM 电源 4599 元直达链接该电源尺寸为 150x160x86mm，电源侧面配有 4.3 英寸 LCD 屏幕，采用数字化控制方案及氮化镓技术，配备全日系电容，支持 ATX 3.1 设计规范，提供 2 个 12V-2×6 接口，采用独立压纹线套。该电源配备 14cm 双滚珠风扇，支持智能启停功能，并可通过 GCC 实现反转清灰功能，支持 OCP、OTP、OVP、OPP、UVP、SCP、NLO 以及 SIP。IT之家附产品参数：" data-title="技嘉钛金雕 GP-AP1600TM 钛金电源发售：4.3 英寸 LCD 屏幕、14cm 双滚珠风扇，4599 元" data-date="11-21 16:42" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-21 16:42</span>
          <span class="news-item-title">技嘉钛金雕 GP-AP1600TM 钛金电源发售：4.3 英寸 LCD 屏幕、14cm 双滚珠风扇，4599 元</span>
          <span class="news-value-point">💡 IT之家 11 月 21 日消息，技嘉旗下钛金雕 GP-AP1600TM 钛金电源现已在京东发售，定价为 4599 元，提供 10 年质保</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/413.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 21 日消息，据 ScitechDaily 报道，悉尼大学与昆士兰大学的研究人员近日开发出一种可生物降解的新型纳米材料，有望帮助先天性唇腭裂儿童再生缺失的颌骨。公开信息显示，唇腭裂是较为常见的先天性疾病，约每 700 名新生儿中就有 1 名受到影响。该疾病通常是由于胎儿发育期间，上唇或口腔顶部的组织未能完全融合所致。由此产生的颌骨缺损是治疗过程中最棘手的问题之一，可能影响患者的进食、呼吸、语言表达以及社交能力。悉尼大学医学院与健康学院悉尼地平线研究员 Chun Xu 副教授表示，此次开发的新方案旨在通过一种可生物降解的钙铝硅酸盐纳米材料，刺激人体自身形成新的活骨组织。具体来看，这种材料能够激活一种名为潜伏型转化生长因子 β1（TGF-β1）的天然生长因子。该蛋白质通常以非" data-title="研究人员开发可生物降解纳米材料，有望让唇腭裂儿童再生颌骨" data-date="11-21 16:40" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-21 16:40</span>
          <span class="news-item-title">研究人员开发可生物降解纳米材料，有望让唇腭裂儿童再生颌骨</span>
          <span class="news-value-point">💡 IT之家 11 月 21 日消息，据 ScitechDaily 报道，悉尼大学与昆士兰大学的研究人员近日开发出一种可生物降解的新型纳米材料，有望…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-21/10735765.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社新疆富蕴11月21日电 (记者 苟继鹏)“作为本雪季中国首家开滑的室外高山滑雪场，自今年10月20日新雪季开板以来，我们已累计接待游客超7.5万人次，开局即火热。”新疆富蕴县的可可托海国际滑雪度假区营销企划部员工赵婷玉21日说。" data-title="（走进中国乡村）新雪季新疆“冰雪小镇”迎客忙" data-date="11-21 16:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-21 16:37</span>
          <span class="news-item-title">（走进中国乡村）新雪季新疆“冰雪小镇”迎客忙</span>
          <span class="news-value-point">💡 中新社新疆富蕴11月21日电 (记者 苟继鹏)“作为本雪季中国首家开滑的室外高山滑雪场，自今年10月20日新雪季开板以来，我们已累计接待游客超7…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-21/10735766.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社西藏那曲11月21日电 初冬的藏北高原，寒风凛冽，羌塘国家级自然保护区内，管护员正如常开展巡护工作。那曲市林业和草原局21日介绍，依托日益完善的管护网络与科技手段，当地正为藏羚羊等野生动物营造“不被打扰”的栖息环境。" data-title="藏羚羊正值交配期 西藏那曲营造“不被打扰”的栖息环境" data-date="11-21 16:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-21 16:32</span>
          <span class="news-item-title">藏羚羊正值交配期 西藏那曲营造“不被打扰”的栖息环境</span>
          <span class="news-value-point">💡 中新社西藏那曲11月21日电 初冬的藏北高原，寒风凛冽，羌塘国家级自然保护区内，管护员正如常开展巡护工作</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/408.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 21 日消息，乔思伯旗下 BO400 VP 铝制海景房机箱现已在京东发售，该产品采用真空镀工艺，支持 360 水冷，拥有 10 风扇位，定价为 1999 元。京东乔思伯（JONSBO）BO400 VP ATX 铝制海景房机箱 1999 元直达链接该机箱使用 ATX 分仓结构，具体尺寸为 474mm x 311mm x 489mm，净重 12.9kg，其内部骨架由十二根型材铝柱与八个压铸转角件通过榫卯结构连接而成，中空型材框架厚度为 2mm，前面板使用厚度为 6mm 的 CNC 铝面板，表面经过阳极拉丝处理与水电镀镍铬打底，面板指示灯可接入 ARGB 系统进行控制。该机箱支持三面侧透自由切换，出厂默认的金属顶盖可直接替换为附赠的玻璃顶盖，以满足不同视觉需求。机箱内部支持显卡" data-title="乔思伯 BO400 VP 铝制海景房机箱发售：可实现三面侧透自由切换，支持 360 水冷，1999 元" data-date="11-21 16:27" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-21 16:27</span>
          <span class="news-item-title">乔思伯 BO400 VP 铝制海景房机箱发售：可实现三面侧透自由切换，支持 360 水冷，1999 元</span>
          <span class="news-value-point">💡 IT之家 11 月 21 日消息，乔思伯旗下 BO400 VP 铝制海景房机箱现已在京东发售，该产品采用真空镀工艺，支持 360 水冷，拥有 1…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/030/407.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 21 日消息，魅族 MIFI N1 随身 Wi-Fi 现已在京东上架发售，首发价 39 元起。京东魅族随身 Wi-Fi 券后 39 元领 5 元券据介绍，这款随身 Wi-Fi 搭载移芯 EC800LE，集成基带、射频、电源管理，支持智能切网；尺寸为 96.6×58×14.8mm，重约 102g；支持 Wi-Fi 6 协议，下行峰值 150Mbps；电池容量 3000mAh，通过 3C 认证，最多支持 16 台设备同时接入。IT之家附这款产品主要参数：" data-title="魅族 MIFI N1 随身 Wi-Fi 发售：搭移芯 EC800LE 芯片，3000mAh 电池，39 元起" data-date="11-21 16:26" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-21 16:26</span>
          <span class="news-item-title">魅族 MIFI N1 随身 Wi-Fi 发售：搭移芯 EC800LE 芯片，3000mAh 电池，39 元起</span>
          <span class="news-value-point">💡 IT之家 11 月 21 日消息，魅族 MIFI N1 随身 Wi-Fi 现已在京东上架发售，首发价 39 元起</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-21/10735742.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网合肥11月21日电(记者 赵强)安徽省东至县青山乡一名4岁男童走失已超过45小时，当地多方力量仍在全力搜寻。截至11月21日12时，尚未发现走失儿童下落。" data-title="安徽东至一4岁男童走失 多方持续全力搜寻" data-date="11-21 16:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-21 16:05</span>
          <span class="news-item-title">安徽东至一4岁男童走失 多方持续全力搜寻</span>
          <span class="news-value-point">💡 中新网合肥11月21日电(记者 赵强)安徽省东至县青山乡一名4岁男童走失已超过45小时，当地多方力量仍在全力搜寻</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/monitors/gaming-monitors/samsungs-gorgeous-49-inch-odyssey-oled-g9-hits-a-new-all-time-low-price-of-usd854-amazon-black-friday-deal-slashes-33-percent-off-gaming-monitor-upgrade" target="_blank" rel="noopener" data-cat="zonghe" data-summary="现在，这款49英寸超宽QD-OLED游戏显示器在亚马逊的黑色星期五促销中创下历史新低，您有机会将它收入囊中。" data-title="Samsung’s gorgeous 49-inch Odyssey OLED G9 hits a new all-time low price of $854 — Amazon Black Friday deal slashes 33% off gaming monitor upgrade" data-date="11-21 16:02" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-21 16:02</span>
          <span class="news-item-title">三星靓丽的 49 英寸 Odyssey OLED G9 创下 854 美元的历史新低价——亚马逊黑色星期五优惠，这款游戏显示器升级版降价 33%</span>
          <span class="news-item-title-en">Samsung’s gorgeous 49-inch Odyssey OLED G9 hits a new all-time low price of $854 — Amazon Black Friday deal slashes 33% off gaming monitor upgrade</span>
          <span class="news-value-point">💡 现在，这款49英寸超宽QD-OLED游戏显示器在亚马逊的黑色星期五促销中创下历史新低，您有机会将它收入囊中</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-21/10735739.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网杭州11月21日电(林波 曹丹 孙琳茹)在杭州市美术高级中学的画室里，高一学生徐进正对着石膏像起稿。入学前她几乎没有拿过画笔，中考结束后一度以为自己的升学选择十分有限。如今她注册的是普通高中学籍，课表上既有语数英、政史地等普高文化基础课程，又有素描、图创、摄影等职业体验课程。" data-title="给成长多一种可能 浙江综合高中改革试点“三校”观察" data-date="11-21 15:58" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-21 15:58</span>
          <span class="news-item-title">给成长多一种可能 浙江综合高中改革试点“三校”观察</span>
          <span class="news-value-point">💡 中新网杭州11月21日电(林波 曹丹 孙琳茹)在杭州市美术高级中学的画室里，高一学生徐进正对着石膏像起稿</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/cricket/live-blog/12040/13614441/australia-vs-england-first-t20i-live-score-over-by-over-updates-and-analysis-from-series-opener-in-melbourne" target="_blank" rel="noopener" data-cat="zonghe" data-summary="England&#39;s Brook slams 20-ball fifty as Australia drop FIVE catches LIVE!" data-title="England&#39;s Brook slams 20-ball fifty as Australia drop FIVE catches LIVE!" data-date="11-21 15:30" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-21 15:30</span>
          <span class="news-item-title">英格兰的布鲁克20球轰出50分，澳大利亚错失五个接球机会！</span>
          <span class="news-item-title-en">England's Brook slams 20-ball fifty as Australia drop FIVE catches LIVE!</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-21/10735736.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="央视网消息：眼下，全国多地遭遇大风降温天气，各地采暖、生产用能需求加大。我国西煤东运主要通道大秦铁路全力保障冬季电煤运输顺畅，日运量保持在120万吨以上。" data-title="做好冬季电煤保供运输“加减法” 守护万家冬日暖意" data-date="11-21 15:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-21 15:16</span>
          <span class="news-item-title">做好冬季电煤保供运输“加减法” 守护万家冬日暖意</span>
          <span class="news-value-point">💡 央视网消息：眼下，全国多地遭遇大风降温天气，各地采暖、生产用能需求加大</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/f1/news/12040/13614576/george-russell-hits-out-at-max-verstappen-after-las-vegas-gp-clash-and-says-somebodys-got-to-stand-up-to-that-guy" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在拉斯维加斯大奖赛的最后一次练习赛中，乔治·拉塞尔（George Russell）和马克斯·维斯塔潘（Max Verstappen）发生碰撞，随后拉塞尔对维斯塔潘进行了严厉批评。两人现在将并排在前排发车。" data-title="&#39;Somebody’s got to stand up to that guy&#39; - Russell slams Verstappen after clash" data-date="11-21 15:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-21 15:00</span>
          <span class="news-item-title">“总得有人站出来对抗那家伙”——拉塞尔在碰撞后抨击维斯塔潘</span>
          <span class="news-item-title-en">'Somebody’s got to stand up to that guy' - Russell slams Verstappen after clash</span>
          <span class="news-value-point">💡 在拉斯维加斯大奖赛的最后一次练习赛中，乔治·拉塞尔（George Russell）和马克斯·维斯塔潘（Max Verstappen）发生碰撞，随…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/racing/news/12040/13614349/today-on-sky-sports-racing-ascot-lingfield-park-and-newcastle-feature-live-on-saturday" target="_blank" rel="noopener" data-cat="zonghe" data-summary="周六我们将迎来繁忙的赛马日，阿斯科特、林菲尔德公园和纽卡斯尔的赛事将在Sky Sports Racing上直播……" data-title="Doyen Quest and Blow Your Wad re-oppose in Ascot&#39;s 1965 Chase" data-date="11-21 15:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-21 15:00</span>
          <span class="news-item-title">Doyen Quest和Blow Your Wad将在阿斯科特赛马场的1965年障碍赛中再次对决</span>
          <span class="news-item-title-en">Doyen Quest and Blow Your Wad re-oppose in Ascot's 1965 Chase</span>
          <span class="news-value-point">💡 周六我们将迎来繁忙的赛马日，阿斯科特、林菲尔德公园和纽卡斯尔的赛事将在Sky Sports Racing上直播……</span>
        </a>
  </div>
</div>
<script defer src="{{ "/assets/js/news-feed.js" | relative_url }}"></script>


<p class="news-updated">🕐 抓取更新于 2026-11-21 16:54（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
