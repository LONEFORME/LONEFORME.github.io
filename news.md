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
      <span>2026-11-17 17:49 抓取更新</span>
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
        <span class="channel-count">56</span>
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
  <div class="ov-item"><span class="ov-num">56</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">4</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×21 · 天空体育×11</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">按来源聚合 · 最近 24 小时精选</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/11-17/10733564.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="11月17日，国家主席习近平在深圳会见墨西哥总统辛鲍姆。" data-title="新华图讯丨习近平会见墨西哥总统辛鲍姆" data-date="11-17 17:40" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 11-17 17:40</span>
      </div>
      <h2 class="hero-featured-title">新华图讯丨习近平会见墨西哥总统辛鲍姆</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/028/418.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 17 日消息，韩媒 THE ELEC 当地时间今日报道称，三星电子近期已确认了 DRAM 内存技术的未来发展方向，多条技术路线将并行推进。三星电子目前最为先进的 DRAM 工艺为第 6 代 10nm 级的 1c nm (D1c)，采用传统的 6F² 结构和制造工艺。后续的常规迭代 D1d 将用于 LPDDR 等通用内存产品，预计 2027H2 量产。三星此前曾表示 HBM5 内存将升级至新一代 DRAM Die。而根据韩媒报道，这里的“新一代”将是应用混合键合技术的 D0a，而不是普遍认为的 D1d。D0a 在不同的晶圆上制造存储阵列和外围电路，此后以 W2W（晶圆对晶圆）混合键合结合两部分，这意味着可针对性地分别优化阵列和外围器件表现。该报道称 D0a 的阵列基于 D1" data-title="传三星电子确定内存未来发展方向：HBM5 使用 D0a DRAM Die" data-date="11-17 17:03" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">传三星电子确定内存未来发展方向：HBM5 使用 D0a DRAM Die</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/football/live-blog/12040/13025486/arsenal-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Arsenal latest: &#39;Agreement reached over new Raya contract&#39;" data-title="Arsenal latest: &#39;Agreement reached over new Raya contract&#39;" data-date="11-17 17:15" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">阿森纳最新消息：“已就拉亚的新合同达成协议”</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/11-17/10733566.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社太原11月17日电 (记者 胡健)“寻找‘最初的中国’——秦晋豫‘十四五’期间中华文明探源考古成果展”17日在山西博物院开展，共展出文物160余件(组)，系统勾勒中华文明从“满天星斗”到“多元一体”的发展格局。" data-title="秦晋豫探源成果齐聚山西 百余件文物呈现“最初的中国”" data-date="11-17 17:44" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">秦晋豫探源成果齐聚山西 百余件文物呈现“最初的中国”</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-17/10733564.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="11月17日，国家主席习近平在深圳会见墨西哥总统辛鲍姆。" data-title="新华图讯丨习近平会见墨西哥总统辛鲍姆" data-date="11-17 17:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 17:40</span>
          <span class="news-item-title">新华图讯丨习近平会见墨西哥总统辛鲍姆</span>
          <span class="news-value-point">💡 11月17日，国家主席习近平在深圳会见墨西哥总统辛鲍姆</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-17/10733553.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月17日电 近日，第七届海外当代中国研究国际研讨会在北京召开。会议主题为“政党建设与全球治理”，来自98个国家的海外媒体代表与国内专家学者共百余位代表参会。" data-title="第七届海外当代中国研究国际研讨会在北京召开" data-date="11-17 17:25" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 17:25</span>
          <span class="news-item-title">第七届海外当代中国研究国际研讨会在北京召开</span>
          <span class="news-value-point">💡 中新网北京11月17日电 近日，第七届海外当代中国研究国际研讨会在北京召开</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-17/10733556.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社快讯：11月17日，国家主席习近平在深圳会见智利总统卡斯特。" data-title="习近平会见智利总统卡斯特" data-date="11-17 17:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 17:22</span>
          <span class="news-item-title">习近平会见智利总统卡斯特</span>
          <span class="news-value-point">💡 新华社快讯：11月17日，国家主席习近平在深圳会见智利总统卡斯特</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-17/10733545.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月17日电 据湖北省纪委监委消息：经湖北省委批准，湖北省纪委监委对湖北省武汉市人大常委会原党组成员、副主任但长春严重违纪违法问题进行了立案审查调查。" data-title="湖北省武汉市人大常委会原副主任但长春被开除党籍" data-date="11-17 17:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 17:20</span>
          <span class="news-item-title">湖北省武汉市人大常委会原副主任但长春被开除党籍</span>
          <span class="news-value-point">💡 中新网11月17日电 据湖北省纪委监委消息：经湖北省委批准，湖北省纪委监委对湖北省武汉市人大常委会原党组成员、副主任但长春严重违纪违法问题进行了…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-17/10733532.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社快讯：11月17日，国家主席习近平在深圳会见秘鲁总统藤森庆子。" data-title="习近平会见秘鲁总统藤森庆子" data-date="11-17 16:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 16:50</span>
          <span class="news-item-title">习近平会见秘鲁总统藤森庆子</span>
          <span class="news-value-point">💡 新华社快讯：11月17日，国家主席习近平在深圳会见秘鲁总统藤森庆子</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-17/10733488.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月17日电 题：习近平走进孙中山故里 再谈这六个字" data-title="（近观中国）习近平走进孙中山故里 再谈这六个字" data-date="11-17 16:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 16:36</span>
          <span class="news-item-title">（近观中国）习近平走进孙中山故里 再谈这六个字</span>
          <span class="news-value-point">💡 中新社北京11月17日电 题：习近平走进孙中山故里 再谈这六个字</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-17/10733477.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月17日电 乌兰巴托消息：据蒙古国国家通讯社17日报道，蒙古国总统呼日勒苏赫当天上午宣布辞去总统职务。" data-title="蒙古国总统宣布辞职" data-date="11-17 16:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 16:07</span>
          <span class="news-item-title">蒙古国总统宣布辞职</span>
          <span class="news-value-point">💡 中新社北京11月17日电 乌兰巴托消息：据蒙古国国家通讯社17日报道，蒙古国总统呼日勒苏赫当天上午宣布辞去总统职务</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-17/10733500.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社快讯：11月17日，国家主席习近平在深圳会见墨西哥总统辛鲍姆。" data-title="习近平会见墨西哥总统辛鲍姆" data-date="11-17 16:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 16:02</span>
          <span class="news-item-title">习近平会见墨西哥总统辛鲍姆</span>
          <span class="news-value-point">💡 新华社快讯：11月17日，国家主席习近平在深圳会见墨西哥总统辛鲍姆</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-17/10733481.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月17日电 亚太经合组织(APEC)第三十三次领导人非正式会议将于11月18日至19日在深圳举行，受到国际媒体高度关注。在多家外媒看来，科技创新是深圳的关键词之一，在这座充满未来感的城市里，机器人、电动汽车、自动驾驶汽车等创新技术快速发展。" data-title="美媒记者深圳体验自动驾驶汽车 外媒点赞中国科技创新，见证发展活力" data-date="11-17 15:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 15:47</span>
          <span class="news-item-title">美媒记者深圳体验自动驾驶汽车 外媒点赞中国科技创新，见证发展活力</span>
          <span class="news-value-point">💡 中新网11月17日电 亚太经合组织(APEC)第三十三次领导人非正式会议将于11月18日至19日在深圳举行，受到国际媒体高度关注</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-17/10733350.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月17日电(记者 刁炜)据法新社报道，当地时间11月15日，胡塞武装已推进至距也门政府所在地亚丁仅60公里处，也门政府军紧急调兵守卫这座大本营。" data-title="距亚丁仅60公里，胡塞武装逼近也门政府军大本营" data-date="11-17 15:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 15:22</span>
          <span class="news-item-title">距亚丁仅60公里，胡塞武装逼近也门政府军大本营</span>
          <span class="news-value-point">💡 中新网11月17日电(记者 刁炜)据法新社报道，当地时间11月15日，胡塞武装已推进至距也门政府所在地亚丁仅60公里处，也门政府军紧急调兵守卫这…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/crgj360lnqv6o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="离开深圳充满科技感的天际线后，你将会看到习近平治下中国所面临的种种挑战。" data-title="中国以AI奇境接待各国领袖，但他们看不到的另一面是什么？" data-date="11-17 15:05" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-17 15:05</span>
          <span class="news-item-title">中国以AI奇境接待各国领袖，但他们看不到的另一面是什么？</span>
          <span class="news-value-point">💡 离开深圳充满科技感的天际线后，你将会看到习近平治下中国所面临的种种挑战</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-17/10733378.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月17日电 11月18日至19日，亚太经合组织(APEC)第三十三次领导人非正式会议将在中国深圳举行。" data-title="APEC进入“深圳时间”，多图读懂中国贡献：为亚太发展注入正能量" data-date="11-17 14:19" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 14:19</span>
          <span class="news-item-title">APEC进入“深圳时间”，多图读懂中国贡献：为亚太发展注入正能量</span>
          <span class="news-value-point">💡 中新网11月17日电 11月18日至19日，亚太经合组织(APEC)第三十三次领导人非正式会议将在中国深圳举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-17/10733356.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月17日电 据巴勒斯坦官方电视台报道，当地时间16日晚，以色列定居者在约旦河西岸城市杰里科以西一座村庄开枪，造成一名巴勒斯坦妇女死亡、10人受伤。" data-title="巴勒斯坦称以色列定居者在约旦河西岸开枪致1死10伤" data-date="11-17 14:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 14:08</span>
          <span class="news-item-title">巴勒斯坦称以色列定居者在约旦河西岸开枪致1死10伤</span>
          <span class="news-value-point">💡 中新网北京11月17日电 据巴勒斯坦官方电视台报道，当地时间16日晚，以色列定居者在约旦河西岸城市杰里科以西一座村庄开枪，造成一名巴勒斯坦妇女死…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-17/10733344.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月17日电 据美联社报道，当地时间17日，蒙古国总统呼日勒苏赫宣布辞去职务。" data-title="蒙古国总统呼日勒苏赫宣布辞职" data-date="11-17 13:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 13:04</span>
          <span class="news-item-title">蒙古国总统呼日勒苏赫宣布辞职</span>
          <span class="news-value-point">💡 中新网11月17日电 据美联社报道，当地时间17日，蒙古国总统呼日勒苏赫宣布辞去职务</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/17/world/asia/trump-manila-asean-late.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="特朗普总统将在会议即将结束时抵达马尼拉，这表明美国的政策已使该地区在华盛顿与北京之间摇摆不定。" data-title="Trump Will Miss Most of the ASEAN Summit" data-date="11-17 13:00" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-17 13:00</span>
          <span class="news-item-title">特朗普将缺席东盟峰会的大部分议程</span>
          <span class="news-item-title-en">Trump Will Miss Most of the ASEAN Summit</span>
          <span class="news-value-point">💡 特朗普总统将在会议即将结束时抵达马尼拉，这表明美国的政策已使该地区在华盛顿与北京之间摇摆不定</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/028/418.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 17 日消息，韩媒 THE ELEC 当地时间今日报道称，三星电子近期已确认了 DRAM 内存技术的未来发展方向，多条技术路线将并行推进。三星电子目前最为先进的 DRAM 工艺为第 6 代 10nm 级的 1c nm (D1c)，采用传统的 6F² 结构和制造工艺。后续的常规迭代 D1d 将用于 LPDDR 等通用内存产品，预计 2027H2 量产。三星此前曾表示 HBM5 内存将升级至新一代 DRAM Die。而根据韩媒报道，这里的“新一代”将是应用混合键合技术的 D0a，而不是普遍认为的 D1d。D0a 在不同的晶圆上制造存储阵列和外围电路，此后以 W2W（晶圆对晶圆）混合键合结合两部分，这意味着可针对性地分别优化阵列和外围器件表现。该报道称 D0a 的阵列基于 D1" data-title="传三星电子确定内存未来发展方向：HBM5 使用 D0a DRAM Die" data-date="11-17 17:03" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-17 17:03</span>
          <span class="news-item-title">传三星电子确定内存未来发展方向：HBM5 使用 D0a DRAM Die</span>
          <span class="news-value-point">💡 IT之家 11 月 17 日消息，韩媒 THE ELEC 当地时间今日报道称，三星电子近期已确认了 DRAM 内存技术的未来发展方向，多条技术路…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/17/business/economy/global-debt-economy-world-bank.html" target="_blank" rel="noopener" data-cat="keji" data-summary="由于高利率和其他全球性冲击重创发展中国家的经济，其债务负担飙升至9.4万亿美元。" data-title="Debt Problems of the Richest Countries Are Trickling Down to the Poorest" data-date="11-17 16:45" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-17 16:45</span>
          <span class="news-item-title">最富裕国家的债务问题正在蔓延至最贫穷的国家</span>
          <span class="news-item-title-en">Debt Problems of the Richest Countries Are Trickling Down to the Poorest</span>
          <span class="news-value-point">💡 由于高利率和其他全球性冲击重创发展中国家的经济，其债务负担飙升至9.4万亿美元</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/17/business/economy/megaspeed-investigation-trump-doj.html" target="_blank" rel="noopener" data-cat="keji" data-summary="该公告似乎是对近期批评的回应，即商务部在所谓的芯片走私案上行动过于缓慢。" data-title="Facing Criticism, Trump Administration Says It’s Investigating Megaspeed" data-date="11-17 15:02" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-17 15:02</span>
          <span class="news-item-title">面对批评，特朗普政府表示正在调查Megaspeed</span>
          <span class="news-item-title-en">Facing Criticism, Trump Administration Says It’s Investigating Megaspeed</span>
          <span class="news-value-point">💡 该公告似乎是对近期批评的回应，即商务部在所谓的芯片走私案上行动过于缓慢</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/16/us/politics/trump-china-ai-chip-policy.html" target="_blank" rel="noopener" data-cat="keji" data-summary="正值特朗普总统即将与中国国家主席习近平举行关键会晤之际，一场围绕先进人工智能芯片的争论被公之于众，这表明英伟达丑闻已使政府内部的分歧进一步加深。" data-title="Trump Administration Divide on China Policy Breaks Into Public View" data-date="11-17 11:48" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-17 11:48</span>
          <span class="news-item-title">特朗普政府在对华政策上的分歧公开化</span>
          <span class="news-item-title-en">Trump Administration Divide on China Policy Breaks Into Public View</span>
          <span class="news-value-point">💡 正值特朗普总统即将与中国国家主席习近平举行关键会晤之际，一场围绕先进人工智能芯片的争论被公之于众，这表明英伟达丑闻已使政府内部的分歧进一步加深</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/16/technology/nvidia-jensen-madison-huang.html" target="_blank" rel="noopener" data-cat="keji" data-summary="黄仁勋的女儿被任命为父亲的实际幕僚长，这疏远了高管们。如今，她持续发挥的作用对临时首席执行官科莱特·克雷斯（Colette Kress）构成了考验。" data-title="Madison Huang, Jensen Huang’s Daughter, Became a Powerful Force at Nvidia" data-date="11-17 10:15" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-17 10:15</span>
          <span class="news-item-title">黄仁勋的女儿黄悦仁成为英伟达的一股强大力量</span>
          <span class="news-item-title-en">Madison Huang, Jensen Huang’s Daughter, Became a Powerful Force at Nvidia</span>
          <span class="news-value-point">💡 黄仁勋的女儿被任命为父亲的实际幕僚长，这疏远了高管们</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/16/cybersecurity-ai-startup-corma-reaches-1b-valuation-in-about-3-months/" target="_blank" rel="noopener" data-cat="keji" data-summary="自推出产品以来的三个月里，人工智能网络安全初创公司Corba已完成一轮由NEA领投的1.25亿美元A轮融资，估值达10亿美元。" data-title="Cybersecurity AI startup Corma reaches $1B valuation in about 3 months" data-date="11-17 07:32" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-17 07:32</span>
          <span class="news-item-title">网络安全AI初创公司Corma在约3个月内估值达到10亿美元</span>
          <span class="news-item-title-en">Cybersecurity AI startup Corma reaches $1B valuation in about 3 months</span>
          <span class="news-value-point">💡 自推出产品以来的三个月里，人工智能网络安全初创公司Corba已完成一轮由NEA领投的1.25亿美元A轮融资，估值达10亿美元</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1035027/tech-leaders-nvidia-jensen-huang-theories" target="_blank" rel="noopener" data-cat="keji" data-summary="黄仁勋在英伟达工作了33年多后突然辞职，在整个科技行业掀起了轩然大波。现在，知名人士纷纷呼吁让黄仁勋复职，许多人也赞同一种正在流传的说法。" data-title="Tech leaders are convinced that Jensen Huang’s exit was a plot against him" data-date="11-17 07:17" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-17 07:17</span>
          <span class="news-item-title">科技界领袖们深信，黄仁勋的离职是一场针对他的阴谋。</span>
          <span class="news-item-title-en">Tech leaders are convinced that Jensen Huang’s exit was a plot against him</span>
          <span class="news-value-point">💡 黄仁勋在英伟达工作了33年多后突然辞职，在整个科技行业掀起了轩然大波</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/supercomputers/china-retains-fastest-supercomputer-in-the-world-crown-as-ai-data-centers-soak-up-new-hardware-top500-records-fewest-new-systems-in-33-years" target="_blank" rel="noopener" data-cat="keji" data-summary="在计算基础设施投资大规模转向人工智能工厂之际，500强榜单的新上榜企业数量创下历史新低。" data-title="China retains fastest supercomputer in the world crown as AI data centers soak up new hardware" data-date="11-17 06:17" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-17 06:17</span>
          <span class="news-item-title">随着人工智能数据中心吸收新硬件，中国仍保持着世界上最快的超级计算机的桂冠</span>
          <span class="news-item-title-en">China retains fastest supercomputer in the world crown as AI data centers soak up new hardware</span>
          <span class="news-value-point">💡 在计算基础设施投资大规模转向人工智能工厂之际，500强榜单的新上榜企业数量创下历史新低</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/16/all-the-questions-nvidia-should-answer-on-tuesday-but-probably-wont/" target="_blank" rel="noopener" data-cat="keji" data-summary="周二，英伟达将公布第三季度业绩，届时，英伟达临时首席执行官兼长期首席财务官科莱特·克雷斯（Colette Kress）将迎来其职业生涯中最重要的日子之一。鉴于英伟达正处于动荡之中，英伟达应该回答一些问题。" data-title="All the questions Nvidia should answer on Tuesday" data-date="11-17 06:03" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-17 06:03</span>
          <span class="news-item-title">英伟达周二应回答的所有问题</span>
          <span class="news-item-title-en">All the questions Nvidia should answer on Tuesday</span>
          <span class="news-value-point">💡 周二，英伟达将公布第三季度业绩，届时，英伟达临时首席执行官兼长期首席财务官科莱特·克雷斯（Colette Kress）将迎来其职业生涯中最重要的…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/new-us-rules-aim-to-restrict-remote-access-to-ai-servers-and-infrastructure-seeks-to-combat-cloud-rental-workarounds-to-gpu-export-controls" target="_blank" rel="noopener" data-cat="keji" data-summary="美国工业与安全局（BIS）已发布一项新的临时最终规则，以确保无法通过远程访问全球数据中心来规避对物理人工智能硬件出口的限制。" data-title="New US rules aim to restrict Chinese firms’ remote access to AI servers and infrastructure" data-date="11-17 05:50" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-17 05:50</span>
          <span class="news-item-title">美国新规旨在限制中国企业远程访问人工智能服务器和基础设施</span>
          <span class="news-item-title-en">New US rules aim to restrict Chinese firms’ remote access to AI servers and infrastructure</span>
          <span class="news-value-point">💡 美国工业与安全局（BIS）已发布一项新的临时最终规则，以确保无法通过远程访问全球数据中心来规避对物理人工智能硬件出口的限制</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/supercomputers/researchers-recognize-that-ai-will-never-replace-hpc-says-amd-executive-high-precision-workloads-will-exist-for-a-very-long-time-even-as-ai-usage-expands" target="_blank" rel="noopener" data-cat="keji" data-summary="人工智能的出现似乎对高精度 FP64 计算构成了威胁，但 AMD 并不认为在人工智能兴起之后，高性能计算领域会远离这些复杂的计算。" data-title="Researchers ‘recognize that AI will never replace HPC,’ says AMD executive — high-precision workloads will ‘exist for a very long time’ even as AI usage expands" data-date="11-17 05:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-17 05:30</span>
          <span class="news-item-title">AMD高管表示，研究人员“认识到人工智能永远不会取代HPC”——即使人工智能的应用范围不断扩大，高精度工作负载也将“长期存在”</span>
          <span class="news-item-title-en">Researchers ‘recognize that AI will never replace HPC,’ says AMD executive — high-precision workloads will ‘exist for a very long time’ even as AI usage expands</span>
          <span class="news-value-point">💡 人工智能的出现似乎对高精度 FP64 计算构成了威胁，但 AMD 并不认为在人工智能兴起之后，高性能计算领域会远离这些复杂的计算</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/supercomputers/amd-grabs-over-40-percent-of-new-top500-list-for-supercomputers-up-14-percent-since-last-year-new-lux-system-developed-between-amd-and-department-of-energy-debuts-at-no-14-with-epyc-cpus-and-instinct-mi355x-gpus" target="_blank" rel="noopener" data-cat="keji" data-summary="AMD的Lux超级计算机在SC26期间发布的新TOP500榜单中首次亮相，排名第14位。这是AMD与美国能源部达成的一项价值10亿美元的协议中正在开发的两台机器之一。" data-title="AMD grabs over 40% of new TOP500 list for supercomputers, up 14% since last year" data-date="11-17 05:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-17 05:00</span>
          <span class="news-item-title">AMD 在最新的 TOP500 超级计算机榜单中占据超过 40% 的份额，较去年增长了 14%</span>
          <span class="news-item-title-en">AMD grabs over 40% of new TOP500 list for supercomputers, up 14% since last year</span>
          <span class="news-value-point">💡 AMD的Lux超级计算机在SC26期间发布的新TOP500榜单中首次亮相，排名第14位</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1034815/california-openai-hugging-face-lawsuit" target="_blank" rel="noopener" data-cat="keji" data-summary="在OpenAI的AI代理脱离测试环境并黑入包括Hugging Face在内的其他公司后，加利福尼亚州正起诉OpenAI。在周一提起的一起诉讼中，司法部长罗伯·邦塔（Rob Bonta）指控OpenAI明知故犯，违反了消费者安全法。" data-title="California sues OpenAI over rogue AI hacking incidents" data-date="11-17 04:46" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-17 04:46</span>
          <span class="news-item-title">加州就“流氓”人工智能黑客事件起诉OpenAI</span>
          <span class="news-item-title-en">California sues OpenAI over rogue AI hacking incidents</span>
          <span class="news-value-point">💡 在OpenAI的AI代理脱离测试环境并黑入包括Hugging Face在内的其他公司后，加利福尼亚州正起诉OpenAI</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1034787/sam-altman-ram-shortage-semafor" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI首席执行官萨姆·阿尔特曼再次回应了他关于购买PC内存的争议言论。“我想说清楚，我希望人们拥有大量内存，我认为每个人都应该能够为自己的电脑购买大量内存。”阿尔特曼今天表示。" data-title="Sam Altman says he wants everyone ‘to have a lot of RAM’" data-date="11-17 04:41" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-17 04:41</span>
          <span class="news-item-title">萨姆·阿尔特曼表示，他希望每个人“都拥有大量内存”</span>
          <span class="news-item-title-en">Sam Altman says he wants everyone ‘to have a lot of RAM’</span>
          <span class="news-value-point">💡 OpenAI首席执行官萨姆·阿尔特曼再次回应了他关于购买PC内存的争议言论</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1034668/data-centers-electricity-climate-pollution-study-harvard" target="_blank" rel="noopener" data-cat="keji" data-summary="《自然-可持续性》杂志上发表的一篇新论文显示，化石燃料仍然是美国超大规模数据中心最大的电力来源。它们消耗的电能总量可能比许多国家都要多，从而导致" data-title="US data centers now burn more electricity than a midsized country" data-date="11-17 04:27" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-17 04:27</span>
          <span class="news-item-title">美国的数据中心现在消耗的电力比一个中等规模的国家还要多</span>
          <span class="news-item-title-en">US data centers now burn more electricity than a midsized country</span>
          <span class="news-value-point">💡 《自然-可持续性》杂志上发表的一篇新论文显示，化石燃料仍然是美国超大规模数据中心最大的电力来源</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">11 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/12040/13025486/arsenal-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Arsenal latest: &#39;Agreement reached over new Raya contract&#39;" data-title="Arsenal latest: &#39;Agreement reached over new Raya contract&#39;" data-date="11-17 17:15" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-17 17:15</span>
          <span class="news-item-title">阿森纳最新消息：“已就拉亚的新合同达成协议”</span>
          <span class="news-item-title-en">Arsenal latest: 'Agreement reached over new Raya contract'</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025486/arsenal-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Arsenal latest: &#39;Agreement reached over new Raya contract&#39;" data-title="Arsenal latest: &#39;Agreement reached over new Raya contract&#39;" data-date="11-17 17:15" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-17 17:15</span>
          <span class="news-item-title">阿森纳最新消息：“已就拉亚的新合同达成协议”</span>
          <span class="news-item-title-en">Arsenal latest: 'Agreement reached over new Raya contract'</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/12040/12476234/transfer-centre-live-football-transfer-news-updates-and-rumours" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Transfer Centre LIVE! McKennie speaks on USA players reuniting with Poch at Man Utd" data-title="Transfer Centre LIVE! McKennie speaks on USA players reuniting with Poch at Man Utd" data-date="11-17 16:15" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-17 16:15</span>
          <span class="news-item-title">转会中心直播！麦肯尼谈论美国球员在曼联与波切蒂诺重聚</span>
          <span class="news-item-title-en">Transfer Centre LIVE! McKennie speaks on USA players reuniting with Poch at Man Utd</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/12476234/transfer-centre-live-football-transfer-news-updates-and-rumours" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Transfer Centre LIVE! McKennie speaks on USA players reuniting with Poch at Man Utd" data-title="Transfer Centre LIVE! McKennie speaks on USA players reuniting with Poch at Man Utd" data-date="11-17 16:15" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-17 16:15</span>
          <span class="news-item-title">转会中心直播！麦肯尼谈论美国球员在曼联与波切蒂诺重聚</span>
          <span class="news-item-title-en">Transfer Centre LIVE! McKennie speaks on USA players reuniting with Poch at Man Utd</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cvgxvg4v981o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="自他身穿“为什么总是针对我？”的T恤庆祝曼彻斯特德比以来，已经过去了十五年。曼彻斯特德比T恤庆祝活动已经过去了十五年，BBC体育回顾了前曼城前锋马里奥·巴洛特利的职业生涯。" data-title="Why always him? The rise and fall of Balotelli" data-date="11-17 14:15" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-17 14:15</span>
          <span class="news-item-title">为什么总是他？巴洛特利的起起落落</span>
          <span class="news-item-title-en">Why always him? The rise and fall of Balotelli</span>
          <span class="news-value-point">💡 自他身穿“为什么总是针对我</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13612986/declan-rice-contract-arsenal-midfielder-verbally-agrees-new-320000-a-week-deal-with-the-premier-league-champions" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="据天空体育新闻透露，德克兰·赖斯已口头同意阿森纳的新长期合同条款。" data-title="Rice verbally agrees new Arsenal contract" data-date="11-17 05:12" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-17 05:12</span>
          <span class="news-item-title">赖斯口头同意与阿森纳签订新合同</span>
          <span class="news-item-title-en">Rice verbally agrees new Arsenal contract</span>
          <span class="news-value-point">💡 据天空体育新闻透露，德克兰·赖斯已口头同意阿森纳的新长期合同条款</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmge3y2qjlyro?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="托马斯·弗兰克——现已确认成为水晶宫的新任主教练——能否在热刺经历一段艰难时期后，在塞尔赫斯特公园重建自己的声誉？" data-title="How Frank can restore reputation and save Crystal Palace" data-date="11-17 01:46" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-17 01:46</span>
          <span class="news-item-title">弗兰克如何挽回声誉并拯救水晶宫</span>
          <span class="news-item-title-en">How Frank can restore reputation and save Crystal Palace</span>
          <span class="news-value-point">💡 托马斯·弗兰克——现已确认成为水晶宫的新任主教练——能否在热刺经历一段艰难时期后，在塞尔赫斯特公园重建自己的声誉</span>
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
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/12507208/football-latest-news-gossip" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Kaveh Q&amp;A: YOUR questions answered on Man Utd, Man City, England and more" data-title="Kaveh Q&amp;A: YOUR questions answered on Man Utd, Man City, England and more" data-date="11-16 21:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-16 21:00</span>
          <span class="news-item-title">Kaveh问答：回答您关于曼联、曼城、英格兰队等球队的问题</span>
          <span class="news-item-title-en">Kaveh Q&A: YOUR questions answered on Man Utd, Man City, England and more</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-17/10733566.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社太原11月17日电 (记者 胡健)“寻找‘最初的中国’——秦晋豫‘十四五’期间中华文明探源考古成果展”17日在山西博物院开展，共展出文物160余件(组)，系统勾勒中华文明从“满天星斗”到“多元一体”的发展格局。" data-title="秦晋豫探源成果齐聚山西 百余件文物呈现“最初的中国”" data-date="11-17 17:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 17:44</span>
          <span class="news-item-title">秦晋豫探源成果齐聚山西 百余件文物呈现“最初的中国”</span>
          <span class="news-value-point">💡 中新社太原11月17日电 (记者 胡健)“寻找‘最初的中国’——秦晋豫‘十四五’期间中华文明探源考古成果展”17日在山西博物院开展，共展出文物1…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-17/10733567.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网合肥11月17日电 (赵强 金硕)眼下，安徽合肥等地中小学迎来“秋假”，与周末衔接形成五天假期，亲子游、研学游出行需求集中释放。11月14日至18日，合肥铁路公安处管内各客站预计发送旅客135万人次，日均约27万人次。" data-title="合肥铁路警方护航 “秋假”135万人次旅客出行" data-date="11-17 17:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 17:42</span>
          <span class="news-item-title">合肥铁路警方护航 “秋假”135万人次旅客出行</span>
          <span class="news-value-point">💡 中新网合肥11月17日电 (赵强 金硕)眼下，安徽合肥等地中小学迎来“秋假”，与周末衔接形成五天假期，亲子游、研学游出行需求集中释放</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-17/10733565.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="辟 谣 网传“河南许昌鄢陵建机场试飞”不实" data-title="警方披露“和平饭店51万天价小票案”细节（2026·11·17）" data-date="11-17 17:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 17:39</span>
          <span class="news-item-title">警方披露“和平饭店51万天价小票案”细节（2026·11·17）</span>
          <span class="news-value-point">💡 辟 谣 网传“河南许昌鄢陵建机场试飞”不实</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/028/432.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 17 日消息，华为 Mate 90 系列手机今日率先开启鸿蒙 HarmonyOS 7.0.0.115 SP11 版本升级，系统包大小约 10.31GB，带来了 AI 快捷栏等功能。IT之家附华为 Mate 90 系列手机此次更新内容如下：桌面桌面新增 AI 快捷栏，按住 AI 圆环可直接说话，点击可探索更多 AI 服务（设置 &gt; 桌面和个性化 &gt; 桌面设置 &gt; AI 快捷栏）。图库支持批量将 HEIF 格式图片转为 JPG 格式，一次选择多张，转换更高效（图库 &gt; 照片页或某一相册内 &gt; 多选 HEIF 格式图片 &gt; 更多 &gt; 转为 JPG 格式）。相机优化相机在部分场景的拍摄效果，持续提升长焦、人像、夜景与烟花的拍照体验。系统重要补丁亲爱的用户，本次更新修复了部分预览拍" data-title="华为 Mate 90 系列手机获鸿蒙 HarmonyOS 7.0.0.115 升级，AI 快捷栏如约上线" data-date="11-17 17:36" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-17 17:36</span>
          <span class="news-item-title">华为 Mate 90 系列手机获鸿蒙 HarmonyOS 7.0.0.115 升级，AI 快捷栏如约上线</span>
          <span class="news-value-point">💡 IT之家 11 月 17 日消息，华为 Mate 90 系列手机今日率先开启鸿蒙 HarmonyOS 7.0.0.115 SP11 版本升级，系…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/028/429.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 17 日消息，博主 @数码闲聊站 今日发文，谈及了阔折叠手机和大折叠手机的两种形态。他透露，明年安卓阵营也有两种形态并行。根据具体形态来看，大折指的是常规 1:1 比例方正大折叠手机，阔折目前主流定义是√2:1 比例形态的折叠屏手机。前者内部空间充足，电池、散热、影像等更有机会堆料，办公、多窗口生产力有一定优势；后者造型新颖，内屏比例接近平板，观影、游戏等沉浸感更好，内容消费会有一定优势。目前，华为、三星、小米、苹果已率先推出阔折叠形态的手机。今年 10 月数据显示，华为阔折叠手机出货量已突破 321 万台。参考IT之家此前报道，市场调查机构 Omdia 在 10 月 21 日发布研究报告，2026 年全球可折叠智能手机 AMOLED 显示屏出货量有望达到 2900 万片" data-title="阔折叠 VS 大折叠：消息称明年安卓新机阵营也有两种形态并行" data-date="11-17 17:27" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-17 17:27</span>
          <span class="news-item-title">阔折叠 VS 大折叠：消息称明年安卓新机阵营也有两种形态并行</span>
          <span class="news-value-point">💡 IT之家 11 月 17 日消息，博主 @数码闲聊站 今日发文，谈及了阔折叠手机和大折叠手机的两种形态</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-17/10733552.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网海口11月17日电 (记者 王子谦)海南省应急管理厅副厅长，省防灾减灾救灾委员会办公室副主任李京波17日在海口表示，今冬明春海南省森林火险等级整体偏高，相关部门正扎实做好新一轮防火期各项备战工作。" data-title="今冬明春森林火险等级偏高 海南全面防火备战" data-date="11-17 17:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 17:23</span>
          <span class="news-item-title">今冬明春森林火险等级偏高 海南全面防火备战</span>
          <span class="news-value-point">💡 中新网海口11月17日电 (记者 王子谦)海南省应急管理厅副厅长，省防灾减灾救灾委员会办公室副主任李京波17日在海口表示，今冬明春海南省森林火险…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-17/10733551.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网昆明11月17日电 (陆继存)据中国铁路昆明局集团有限公司17日消息，中老铁路老挝段集中整修施工近日启动。" data-title="中老铁路老挝段启动大规模集中整修施工" data-date="11-17 17:18" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 17:18</span>
          <span class="news-item-title">中老铁路老挝段启动大规模集中整修施工</span>
          <span class="news-value-point">💡 中新网昆明11月17日电 (陆继存)据中国铁路昆明局集团有限公司17日消息，中老铁路老挝段集中整修施工近日启动</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/028/428.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 17 日消息，经历多次延期后，宾利首款纯电动汽车终于即将登场，而目前的市场反响相当不错。这款名为 Torcal 的纯电跨界 SUV 甚至还没有正式投产，宾利就已经将 2027 年全部可用产能分配完毕。现在下单的消费者，最早也要等到 2028 年才能提车。宾利首席执行官弗兰克-斯特芬 · 瓦利瑟（Frank-Steffen Walliser）在接受《汽车新闻》（Automotive News）采访时确认，Torcal 将于明年上半年启动生产。不过，宾利尚未透露首批计划生产多少辆汽车。对于目前的市场表现，瓦利瑟显然相当满意。他表示：“毋庸置疑，我们对市场反响以及目前取得的成绩感到非常满意。”Torcal 的早期市场表现尤其重要，因为其代表着宾利品牌全新的入门级车型。相比尺寸更" data-title="还未投产，宾利首款纯电车 Torcal 明年产能已售罄" data-date="11-17 17:17" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-17 17:17</span>
          <span class="news-item-title">还未投产，宾利首款纯电车 Torcal 明年产能已售罄</span>
          <span class="news-value-point">💡 IT之家 11 月 17 日消息，经历多次延期后，宾利首款纯电动汽车终于即将登场，而目前的市场反响相当不错</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-17/10733544.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网宜昌11月17日电 (郭晓莹 岳黎)记者17日从湖北省宜昌市夷陵区第七届人民代表大会第一次会议获悉，未来五年，该区将严守生态保护红线，统筹水库、河湖生态保护，抓实矿山综合治理，加快国家储备林建设，持续筑牢三峡地区生态安全屏障。" data-title="湖北夷陵持续筑牢三峡生态安全屏障" data-date="11-17 17:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 17:11</span>
          <span class="news-item-title">湖北夷陵持续筑牢三峡生态安全屏障</span>
          <span class="news-value-point">💡 中新网宜昌11月17日电 (郭晓莹 岳黎)记者17日从湖北省宜昌市夷陵区第七届人民代表大会第一次会议获悉，未来五年，该区将严守生态保护红线，统筹…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-17/10733541.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京11月17日电 (记者 孙自法)聚焦中国子午工程二期标志性观测设备——圆环阵太阳射电成像望远镜(昵称“千眼天珠”)的专题开放研讨会11月15日至17日在贵州贵阳市举行，专家在会上透露，子午工程二期已实现覆盖广度、技术深度、探测精度的多维度突破。" data-title="专家：子午工程二期实现覆盖广度、技术深度、探测精度多维度突破" data-date="11-17 17:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 17:04</span>
          <span class="news-item-title">专家：子午工程二期实现覆盖广度、技术深度、探测精度多维度突破</span>
          <span class="news-value-point">💡 中新网北京11月17日电 (记者 孙自法)聚焦中国子午工程二期标志性观测设备——圆环阵太阳射电成像望远镜(昵称“千眼天珠”)的专题开放研讨会11…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/028/419.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 17 日消息，京东物流今日发布 2026 财年（2026 年 1 月～2026 年 12 月）第三财季（2026 年 7 月～2026 年 9 月）报告：营业总收入：639.53 亿元，同比增长 16.1%毛利润：59.77 亿元，同比增长 19.4%毛利率：9.3%归母净利润：17.05 亿元，同比下降 16.03%扣非净利润：21.63 亿元，同比增长 4.09%自由现金流：23 亿元AI 解读本期京东物流 2026 财年第三季度营收规模符合市场一致预期，Non-IFRS 经营利润增速受即时配送业务整合投入影响低于机构预期。核心业绩概览营业收入保持增长：第三季度营业收入 639.53 亿元，同比增长 16.1%；毛利润 59.77 亿元，同比增长 19.4%，增幅高于" data-title="京东物流 2026 财年第三财季归母净利润 17.05 亿元，同比下降 16.03%" data-date="11-17 17:04" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-17 17:04</span>
          <span class="news-item-title">京东物流 2026 财年第三财季归母净利润 17.05 亿元，同比下降 16.03%</span>
          <span class="news-value-point">💡 IT之家 11 月 17 日消息，京东物流今日发布 2026 财年（2026 年 1 月～2026 年 12 月）第三财季（2026 年 7 月…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/f1/news/12040/13612958/fernando-alonso-aston-martin-driver-to-race-in-dakar-rally-ahead-of-2027-f1-season-in-return-to-rally-raid-event" target="_blank" rel="noopener" data-cat="zonghe" data-summary="费尔南多·阿隆索将于1月代表阿斯顿·马丁车队参加达喀尔拉力赛。" data-title="Alonso to race in formidable Dakar Rally with Aston Martin" data-date="11-17 17:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-17 17:00</span>
          <span class="news-item-title">阿隆索将驾驶阿斯顿·马丁赛车参加艰苦的达喀尔拉力赛</span>
          <span class="news-item-title-en">Alonso to race in formidable Dakar Rally with Aston Martin</span>
          <span class="news-value-point">💡 费尔南多·阿隆索将于1月代表阿斯顿·马丁车队参加达喀尔拉力赛</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/16/movies/james-bond-robert-pattinson.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这一公告结束了多年来关于丹尼尔·克雷格（Daniel Craig）在出演五部电影后，谁将接替其角色的猜测。" data-title="Robert Pattinson Named as the Next James Bond" data-date="11-17 16:56" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-17 16:56</span>
          <span class="news-item-title">罗伯特·帕丁森被选为下一任詹姆斯·邦德</span>
          <span class="news-item-title-en">Robert Pattinson Named as the Next James Bond</span>
          <span class="news-value-point">💡 这一公告结束了多年来关于丹尼尔·克雷格（Daniel Craig）在出演五部电影后，谁将接替其角色的猜测</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-17/10733530.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网吕梁11月17日电 (范丽芳 刘生锋)17日，记者从山西吕梁临县官方获悉，当地整合县域革命旧址、红色阵地资源，打造两条精品红色主题实践教育线路，构建沉浸式实景课堂，常态化承接红色研学等活动。" data-title="革命老区山西临县赓续红色血脉 打造沉浸式红色研学课堂" data-date="11-17 16:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-17 16:48</span>
          <span class="news-item-title">革命老区山西临县赓续红色血脉 打造沉浸式红色研学课堂</span>
          <span class="news-value-point">💡 中新网吕梁11月17日电 (范丽芳 刘生锋)17日，记者从山西吕梁临县官方获悉，当地整合县域革命旧址、红色阵地资源，打造两条精品红色主题实践教育…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/golf/news/12040/13613113/pga-tour-chad-ramey-saves-tour-card-with-rain-delayed-austin-championship-title-win" target="_blank" rel="noopener" data-cat="zonghe" data-summary="查德·拉米（Chad Ramey）在首五洞中打出三只小鸟球，最终以低于标准杆七杆的65杆成绩收官，在因雨延期的奥斯汀锦标赛中以两杆优势夺冠，结束了这段让他从可能失去PGA巡回赛参赛资格到获得两年豁免权的五天历程。" data-title="&#39;Unbelievable&#39; - Ramey saves PGA Tour card with Austin Championship title win" data-date="11-17 16:19" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-17 16:19</span>
          <span class="news-item-title">“难以置信”——Ramey凭借奥斯汀锦标赛冠军头衔保住了PGA巡回赛参赛资格</span>
          <span class="news-item-title-en">'Unbelievable' - Ramey saves PGA Tour card with Austin Championship title win</span>
          <span class="news-value-point">💡 查德·拉米（Chad Ramey）在首五洞中打出三只小鸟球，最终以低于标准杆七杆的65杆成绩收官，在因雨延期的奥斯汀锦标赛中以两杆优势夺冠，结束…</span>
        </a>
  </div>
</div>
<script defer src="{{ "/assets/js/news-feed.js" | relative_url }}"></script>


<p class="news-updated">🕐 抓取更新于 2026-11-17 17:49（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
