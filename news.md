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
      <span>2026-10-10 21:55 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num">7</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×22 · IT之家×10</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gj/2026/10-10/10710826.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月10日电 据美国全国广播公司(NBC)当地时间10月报道，美国宾夕法尼亚州伊利市9日晚些时候发生大规模枪击事件，已造成9人死亡，其中包括数名儿童。" data-title="突发：美国宾州发生大规模枪击事件 已致9人死亡" data-date="10-10 21:53" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-10 21:53</span>
      </div>
      <h2 class="hero-featured-title">突发：美国宾州发生大规模枪击事件 已致9人死亡</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/10-10/10710824.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="“十五五”开局，国家重点布局、系统推进“六张网”建设。水网、新型电网、算力网、新一代通信网、城市地下管网、物流网，一张张网从图纸到现实，交织纵横又各司其职，为高质量发展积势蓄能，也托举起万家灯火的日常。" data-title="一线调研丨从“头痛医头”到全域统筹 六网交织托举起万家灯火" data-date="10-10 21:49" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">一线调研丨从“头痛医头”到全域统筹 六网交织托举起万家灯火</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/live/2026/oct/10/arsenal-v-leeds-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="卫冕冠军被迫从后面深入挖掘，并击败那些可以高举头部回家的游客阅读来自阿联酋体育场的保罗·麦金尼斯的比赛报告一封电子邮件： “星期六快乐，巴里，”马云写道" data-title="Arsenal 2-1 Leeds: Premier League – live" data-date="10-10 21:53" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Arsenal 2-1 Leeds: Premier League – live</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/011/515.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 10 日消息，漫步者现已在京东上架 HECATE G2000 Bar 电竞音箱，将于 10 月 16 日发售，定价为 387 元，首发价 349 元。京东漫步者 HECATE G2000 Bar 音箱首发价 349 元直达链接该音箱提供黑白双色可选，使用机甲风格电竞造型，顶部配备一根可插拔式防啸叫麦克风。前面板提供五款主题贴纸供玩家自由更换。产品内置十二种 RGB 效果，支持彩虹、流光等灯效模式。该音箱采用两只 56mm 全频单元与两只 60mm 被动辐射器，可实现 THX 7.1.4 空间音效，音箱额定功率为 3W+3W，峰值达 12W。耳机配备的麦克风搭载 AEC 2.0 回音消除技术，可减少外音干扰。IT之家附产品参数：" data-title="漫步者 HECATE G2000 Bar 电竞音箱上架：四单元声学配置、配可插拔麦克风，首发价 349 元" data-date="10-10 21:54" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">漫步者 HECATE G2000 Bar 电竞音箱上架：四单元声学配置、配可插拔麦克风，首发价 349 元</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-10/10710826.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月10日电 据美国全国广播公司(NBC)当地时间10月报道，美国宾夕法尼亚州伊利市9日晚些时候发生大规模枪击事件，已造成9人死亡，其中包括数名儿童。" data-title="突发：美国宾州发生大规模枪击事件 已致9人死亡" data-date="10-10 21:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-10 21:53</span>
          <span class="news-item-title">突发：美国宾州发生大规模枪击事件 已致9人死亡</span>
          <span class="news-value-point">💡 中新网10月10日电 据美国全国广播公司(NBC)当地时间10月报道，美国宾夕法尼亚州伊利市9日晚些时候发生大规模枪击事件，已造成9人死亡，其中…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/crkg7xppy4zwo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="周先旺于2020年新冠疫情爆发时，曾暗示北京须对披露疫情不及时负责；法院称其受贿行为涵盖武汉市长任内。" data-title="新冠疫情时期武汉市长周先旺受贿罪判囚14年" data-date="10-10 21:49" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-10 21:49</span>
          <span class="news-item-title">新冠疫情时期武汉市长周先旺受贿罪判囚14年</span>
          <span class="news-value-point">💡 周先旺于2020年新冠疫情爆发时，曾暗示北京须对披露疫情不及时负责</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-10/10710818.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网杭州10月10日电(董易鑫)“我的祖母汤修慧女士曾说，我的祖父用‘一只秃笔’在那个时代与黑暗势力斗争。这句话虽是自谦，甚至带几分自嘲，但他的斗争是真实而激烈的。”10月10日，邵飘萍嫡孙邵澄在杭州受访时说。" data-title="纪念“一代报人”邵飘萍：“一只秃笔”的斗争" data-date="10-10 21:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-10 21:48</span>
          <span class="news-item-title">纪念“一代报人”邵飘萍：“一只秃笔”的斗争</span>
          <span class="news-value-point">💡 中新网杭州10月10日电(董易鑫)“我的祖母汤修慧女士曾说，我的祖父用‘一只秃笔’在那个时代与黑暗势力斗争</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-10/10710788.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社乌鲁木齐10月10日电 (胡嘉琛)第三次新疆综合科学考察(简称“科考”)成果发布会10日在乌鲁木齐市举行。" data-title="第三次新疆综合科学考察成果发布" data-date="10-10 21:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-10 21:42</span>
          <span class="news-item-title">第三次新疆综合科学考察成果发布</span>
          <span class="news-value-point">💡 中新社乌鲁木齐10月10日电 (胡嘉琛)第三次新疆综合科学考察(简称“科考”)成果发布会10日在乌鲁木齐市举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-10/10710817.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月10日电 据半岛电视台、土耳其阿纳多卢通讯社(AA)当地时间10日最新援引也门胡塞武装控制的马西拉电视台消息，沙特阿拉伯战机对也门首都萨那国际机场发动四次空袭。" data-title="快讯：胡塞武装称沙特战机四次空袭萨那国际机场" data-date="10-10 21:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-10 21:40</span>
          <span class="news-item-title">快讯：胡塞武装称沙特战机四次空袭萨那国际机场</span>
          <span class="news-value-point">💡 中新网10月10日电 据半岛电视台、土耳其阿纳多卢通讯社(AA)当地时间10日最新援引也门胡塞武装控制的马西拉电视台消息，沙特阿拉伯战机对也门首…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-10/10710792.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社河南洛阳10月10日电 (记者 韩章云)位于河南洛阳的世界文化遗产龙门石窟，是东西方文明交融的见证。“2026世界市长对话·洛阳”首场情景对话10日在此举行，多位外国市长与中方学者围绕“文脉赓续——文化遗产保护传承利用”这一主题，共同探讨古城如何守护历史、激活遗产、古为今用。" data-title="多国市长河南洛阳共话文化遗产古为今用之道" data-date="10-10 21:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-10 21:37</span>
          <span class="news-item-title">多国市长河南洛阳共话文化遗产古为今用之道</span>
          <span class="news-value-point">💡 中新社河南洛阳10月10日电 (记者 韩章云)位于河南洛阳的世界文化遗产龙门石窟，是东西方文明交融的见证</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-10/10710800.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网兰州10月10日电 (记者 张素)涉荷兰“莱克思蒂”玫瑰案将侵权实施转化为授权合作，涉新西兰“赛雷特”苹果案细化植物新品种侵权赔偿认定标准，涉国际铁路运输合同纠纷得以快捷高效化解……" data-title="甘肃法院：立足向西开放前沿区位优势强化涉外司法服务保障" data-date="10-10 21:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-10 21:34</span>
          <span class="news-item-title">甘肃法院：立足向西开放前沿区位优势强化涉外司法服务保障</span>
          <span class="news-value-point">💡 中新网兰州10月10日电 (记者 张素)涉荷兰“莱克思蒂”玫瑰案将侵权实施转化为授权合作，涉新西兰“赛雷特”苹果案细化植物新品种侵权赔偿认定标准…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-10/10710787.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月10日电 据中国海警局10日消息，当日，中国海警厦门舰编队在中国钓鱼岛及其附属岛屿领海内维权巡航。这是中国海警依法开展的维权巡航活动。(完)" data-title="中国海警舰艇编队在中国钓鱼岛及其附属岛屿领海内维权巡航" data-date="10-10 21:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-10 21:22</span>
          <span class="news-item-title">中国海警舰艇编队在中国钓鱼岛及其附属岛屿领海内维权巡航</span>
          <span class="news-value-point">💡 中新社北京10月10日电 据中国海警局10日消息，当日，中国海警厦门舰编队在中国钓鱼岛及其附属岛屿领海内维权巡航</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-10/10710803.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社快讯：据目击者称，沙特阿拉伯首都利雅得哈立德国王国际机场T3航站楼传出爆炸声。" data-title="新华社快讯：沙特首都国际机场传出爆炸声" data-date="10-10 21:18" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-10 21:18</span>
          <span class="news-item-title">新华社快讯：沙特首都国际机场传出爆炸声</span>
          <span class="news-value-point">💡 新华社快讯：据目击者称，沙特阿拉伯首都利雅得哈立德国王国际机场T3航站楼传出爆炸声</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-10/10710775.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="良渚古城遗址公园。余杭区委宣传部供图 中新网杭州10月10日电(记者 王逸飞)第四届“良渚论坛”将于10月18日—20日在杭州市余杭区举行。今年是良渚遗址发现90周年，作为良渚遗址所在地，余杭将向全球嘉宾展现怎样的遗址保护、传承、利用面貌，备受关注。" data-title="“良渚论坛”东道主：写出文明守护新叙事" data-date="10-10 21:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-10 21:15</span>
          <span class="news-item-title">“良渚论坛”东道主：写出文明守护新叙事</span>
          <span class="news-value-point">💡 良渚古城遗址公园</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-10/10710796.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社曼谷10月10日电 (王茜 李映民)泰国防灾减灾厅10日通报，目前泰国21个府及曼谷仍受洪灾影响，涉及315.86万人。泰国总理阿努廷当天要求有关部门继续做好救灾和灾后恢复工作，同时加强防范新一轮降雨可能引发的灾害。" data-title="泰国21个府及曼谷仍受洪灾影响  总理部署防范新一轮降雨" data-date="10-10 21:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-10 21:14</span>
          <span class="news-item-title">泰国21个府及曼谷仍受洪灾影响  总理部署防范新一轮降雨</span>
          <span class="news-value-point">💡 中新社曼谷10月10日电 (王茜 李映民)泰国防灾减灾厅10日通报，目前泰国21个府及曼谷仍受洪灾影响，涉及315.86万人</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-10/10710791.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月10日电 基辅消息：当地时间10月10日凌晨，俄军对乌克兰扎波罗热地区进行空袭，导致12人死亡、14人受伤。死者中有3名儿童。" data-title="俄军袭击乌克兰扎波罗热地区 致12死14伤" data-date="10-10 21:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-10 21:13</span>
          <span class="news-item-title">俄军袭击乌克兰扎波罗热地区 致12死14伤</span>
          <span class="news-value-point">💡 中新社北京10月10日电 基辅消息：当地时间10月10日凌晨，俄军对乌克兰扎波罗热地区进行空袭，导致12人死亡、14人受伤</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-10/10710798.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月10日电 据俄罗斯新闻社等俄罗斯媒体当地时间10日报道，俄总统普京已向美国总统特朗普转达了伊朗方面关于解决冲突的构想。" data-title="俄媒：普京向特朗普转达伊朗方面关于解决冲突的构想" data-date="10-10 21:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-10 21:08</span>
          <span class="news-item-title">俄媒：普京向特朗普转达伊朗方面关于解决冲突的构想</span>
          <span class="news-value-point">💡 中新网10月10日电 据俄罗斯新闻社等俄罗斯媒体当地时间10日报道，俄总统普京已向美国总统特朗普转达了伊朗方面关于解决冲突的构想</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-10/10710772.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网合肥10月10日电 (记者 赵强)据安徽纪检监察网10日消息，日前，经中共安徽省委批准，安徽省纪委监委对池州市东至县委原书记洪克峰严重违纪违法问题进行了立案审查调查。" data-title="安徽省东至县委原书记洪克峰被“双开”" data-date="10-10 21:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-10 21:00</span>
          <span class="news-item-title">安徽省东至县委原书记洪克峰被“双开”</span>
          <span class="news-value-point">💡 中新网合肥10月10日电 (记者 赵强)据安徽纪检监察网10日消息，日前，经中共安徽省委批准，安徽省纪委监委对池州市东至县委原书记洪克峰严重违纪…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-10/10710753.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月10日电 (记者 谢雁冰)国务院新闻办公室10日举行“新征程上的奋斗者”中外记者见面会，请检察系统代表围绕“强化检察监督 履行好国家法律监督机关职责”与中外记者见面交流。多位来自检察系统的代表在见面会上讲述如何在每一起案件的办理中，努力让群众感受到检察为民的温度。" data-title="检察官共话检察为民：把案件办到老百姓心坎上" data-date="10-10 20:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-10 20:53</span>
          <span class="news-item-title">检察官共话检察为民：把案件办到老百姓心坎上</span>
          <span class="news-value-point">💡 中新网北京10月10日电 (记者 谢雁冰)国务院新闻办公室10日举行“新征程上的奋斗者”中外记者见面会，请检察系统代表围绕“强化检察监督 履行好…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-10/10710824.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="“十五五”开局，国家重点布局、系统推进“六张网”建设。水网、新型电网、算力网、新一代通信网、城市地下管网、物流网，一张张网从图纸到现实，交织纵横又各司其职，为高质量发展积势蓄能，也托举起万家灯火的日常。" data-title="一线调研丨从“头痛医头”到全域统筹 六网交织托举起万家灯火" data-date="10-10 21:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-10 21:49</span>
          <span class="news-item-title">一线调研丨从“头痛医头”到全域统筹 六网交织托举起万家灯火</span>
          <span class="news-value-point">💡 “十五五”开局，国家重点布局、系统推进“六张网”建设</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/513.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 10 日消息，综合台媒 BenchLife.info 报道、消息人士 @hongxing2020 分享的内容，NVIDIA（英伟达）在停产 GeForce RTX 5090 / 5090 D v2 的同时，也将调整 GeForce RTX 5080 显卡。NVIDIA 计划停产配备 16GB 显存的现有 GeForce RTX 5080，转而推出 24GB 显存版本。新型号预计将在 2027 年第 1 季度面世，AIC 合作伙伴预计将在近期收到相应的开发资料。不出意外的话，GeForce RTX 5080 24GB 将配备 8 颗 24Gb (3GB) GDDR7 DRAM Die，尚不清楚其是否会像此前泄露的 SUPER 变体那样提升显存等效速率和整卡功耗。参考http" data-title="消息称英伟达计划以 24GB 显存 GeForce RTX 5080 显卡取代现有 16GB 版本" data-date="10-10 21:41" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-10 21:41</span>
          <span class="news-item-title">消息称英伟达计划以 24GB 显存 GeForce RTX 5080 显卡取代现有 16GB 版本</span>
          <span class="news-value-point">💡 IT之家 10 月 10 日消息，综合台媒 BenchLife.info 报道、消息人士 @hongxing2020 分享的内容，NVIDIA（…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/top-ai-labs-reportedly-planning-for-catastrophic-ai-event-fallout-anthropic-openai-and-others-reportedly-building-contingency-plans-and-running-scenarios-of-a-runaway-ai-wreaking-havoc" target="_blank" rel="noopener" data-cat="keji" data-summary="这些应急计划的一个重点是如何在灾难性事件使这些实验室成为焦点之后管理国会。" data-title="Top AI labs reportedly planning for catastrophic AI event fallout" data-date="10-10 21:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-10 21:20</span>
          <span class="news-item-title">据报道，顶级人工智能实验室正在计划灾难性的人工智能事件后果</span>
          <span class="news-item-title-en">Top AI labs reportedly planning for catastrophic AI event fallout</span>
          <span class="news-value-point">💡 这些应急计划的一个重点是如何在灾难性事件使这些实验室成为焦点之后管理国会</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1009051/privacy-ai-agent-promises-openai-meta-muse-dots" target="_blank" rel="noopener" data-cat="keji" data-summary="在今年的OpenAI DevDay上，首席执行官萨姆·奥尔特曼（ Sam Altman ）推出了该公司的新人工智能代理Dots ，并告诉观众，该公司希望“为前沿人工智能的隐私设定一个新标准。“ OpenAI会花一天时间在Meta&#39;s Muse拍摄面纱照片，" data-title="AI agent makers are promising privacy" data-date="10-10 21:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-10 21:00</span>
          <span class="news-item-title">人工智能代理制造商承诺保护隐私</span>
          <span class="news-item-title-en">AI agent makers are promising privacy</span>
          <span class="news-value-point">💡 在今年的OpenAI DevDay上，首席执行官萨姆·奥尔特曼（ Sam Altman ）推出了该公司的新人工智能代理Dots ，并告诉观众，该…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/pc-gaming/free-steam-demo-runs-up-usd1-000-daily-ai-bill-and-forces-devs-to-take-out-bank-loan-studio-eyes-local-hardware-models-to-escape-cloud-limits-as-cheaper-automatic-fallback-ai-models-create-problems-game-uses-ai-to-process-your-voice-and-build-responses" target="_blank" rel="noopener" data-cat="keji" data-summary="Easy Fox对用户数量感到惊讶，没想到演示的受欢迎程度会导致其人工智能费用如此之高。" data-title="Free Steam demo runs up $1,000 daily AI bill and forces devs to take out bank loan" data-date="10-10 20:52" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-10 20:52</span>
          <span class="news-item-title">免费的Steam演示每日增加1000 $的人工智能账单，并迫使开发人员申请银行贷款</span>
          <span class="news-item-title-en">Free Steam demo runs up $1,000 daily AI bill and forces devs to take out bank loan</span>
          <span class="news-value-point">💡 Easy Fox对用户数量感到惊讶，没想到演示的受欢迎程度会导致其人工智能费用如此之高</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-halts-geforce-rtx-5090-production-in-favor-of-ai-data-center-and-professional-gpus-impending-supply-drought-expected-to-drive-up-prices-rtx-5080-24gb-rumored-as-new-gaming-flagship" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道，英伟达停止生产GeForce RTX 5090系列产品，为数据中心和专业显卡留下GB202。传闻GeForce RTX 5080 24 GB将在一段时间内成为绿色阵营事实上的旗舰产品。" data-title="Nvidia reportedly halts GeForce RTX 5090 production in favor of AI data center and professional GPUs" data-date="10-10 20:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-10 20:20</span>
          <span class="news-item-title">据报道，英伟达暂停GeForce RTX 5090的生产，转而支持人工智能数据中心和专业GPU</span>
          <span class="news-item-title-en">Nvidia reportedly halts GeForce RTX 5090 production in favor of AI data center and professional GPUs</span>
          <span class="news-value-point">💡 据报道，英伟达停止生产GeForce RTX 5090系列产品，为数据中心和专业显卡留下GB202</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-10/10710637.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网悉尼10月10日电 (记者 薄雯雯)2026澳大利亚人工智能生态链峰会日前在悉尼科技大学举行，吸引近400名高校科研人员、企业代表及投资界人士参加。" data-title="2026澳大利亚人工智能生态链峰会在悉尼举行" data-date="10-10 19:59" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-10 19:59</span>
          <span class="news-item-title">2026澳大利亚人工智能生态链峰会在悉尼举行</span>
          <span class="news-value-point">💡 中新网悉尼10月10日电 (记者 薄雯雯)2026澳大利亚人工智能生态链峰会日前在悉尼科技大学举行，吸引近400名高校科研人员、企业代表及投资界…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/playstation/anyps5-reaches-critical-gpu-milestone-with-100-percent-shader-instruction-coverage-ps5-games-running-natively-on-pc-still-far-off" target="_blank" rel="noopener" data-cat="keji" data-summary="开源AnyPS5项目已达到100% GPU着色器指令覆盖率。" data-title="AnyPS5 project reaches critical GPU milestone in race to enable running PS5 games natively on PC" data-date="10-10 19:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-10 19:30</span>
          <span class="news-item-title">AnyPS5项目在竞赛中达到了关键的GPU里程碑，可以在PC上原生运行PS5游戏</span>
          <span class="news-item-title-en">AnyPS5 project reaches critical GPU milestone in race to enable running PS5 games natively on PC</span>
          <span class="news-value-point">💡 开源AnyPS5项目已达到100% GPU着色器指令覆盖率</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/400.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 10 日消息，据央视新闻报道，教育部今天（10 日）在京召开人工智能赋能教师发展现场会。国家智慧教育平台教师发展中心全新升级上线，同时，教师人工智能素养全覆盖培训启动。新上线的教师发展中心开设 AI 素养专区，集成人工智能学习资源、智能工具和研修社群，为教师自主学习和全覆盖培训提供支撑。作为全覆盖培训第一课，教育部邀请一线教师、校长和教育局长开展现场沉浸式、场景式示范培训，展示在课前、课中、课后等全链条中，如何用 AI 赋能高效备课、课堂教学、学业评价、教研反思和学校治理，帮助教师掌握从“学 AI”到“用 AI”再到“创 AI”的方法路径，以人工智能赋能教育教学和教师发展，更好助力因材施教。据IT之家此前报道，今年 4 月，教育部等五部门提出，推动师范生培养改革，将人工智" data-title="教育部：教师 AI 素养全覆盖培训启动" data-date="10-10 15:49" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-10 15:49</span>
          <span class="news-item-title">教育部：教师 AI 素养全覆盖培训启动</span>
          <span class="news-value-point">💡 IT之家 10 月 10 日消息，据央视新闻报道，教育部今天（10 日）在京召开人工智能赋能教师发展现场会</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/397.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 10 日消息，消息人士 MEGAsizeGPU (@Zed__Wang) 今日爆料称，NVIDIA（英伟达）将不再向 GeForce RTX 50 系列游戏显卡分配 GB202，该 GPU 的供应将由 RTX PRO Blackwell 专业显卡独占。这意味着 GeForce RTX 5090 / 5090 D v2 两款旗舰产品都将停产，玩家可入手的最高性能游戏显卡将降级至 GeForce RTX 5080。IT之家注意到，NVIDIA 现有 3 档基于 GB202 的 RTX PRO 产品，分别为 6000 / 5500 / 5000 Blackwell，其中新近发布的 RTX PRO 5500 Blackwell 与 GeForce RTX 5090 / 5090" data-title="传英伟达将不再向 GeForce 游戏显卡分配 GB202 GPU" data-date="10-10 15:43" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-10 15:43</span>
          <span class="news-item-title">传英伟达将不再向 GeForce 游戏显卡分配 GB202 GPU</span>
          <span class="news-value-point">💡 IT之家 10 月 10 日消息，消息人士 MEGAsizeGPU (@Zed__Wang) 今日爆料称，NVIDIA（英伟达）将不再向 GeF…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/396.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 10 日消息，据博主 @数码闲聊站 今日爆料，某厂阔家族将率先推出搭载 2nm 芯片的阔折叠，结合该博主此前的爆料习惯，预计该机为 OPPO 旗下。据其爆料，该机采用 7.6 英寸无痕铰链方案，工程机是三星屏，搭载 200Mp 大底主摄 +50Mp 超广角 +50Mp 潜望长焦 +3Mp 多光谱镜头，哈苏全焦段影像，主打轻薄无痕全能。IT之家注意到，早在今年 1 月，该博主便爆料某厂的阔折叠新机确定在评估中，大概率是下代。当时，这款新机预计归属 OPPO 品牌。今年 6 月，再次爆料某机测试 2nm 骁龙 8 Elite Gen6 系列，工程机采用 7.6± 英寸主屏，5.5± 英寸副屏。目前，OPPO 官方暂未这款新机的更多消息，感兴趣的朋友可以关注IT之家后续报道。" data-title="消息称某厂 2nm 阔折叠工程机采用三星屏、哈苏全焦段影像，预计 OPPO 旗下" data-date="10-10 15:40" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-10 15:40</span>
          <span class="news-item-title">消息称某厂 2nm 阔折叠工程机采用三星屏、哈苏全焦段影像，预计 OPPO 旗下</span>
          <span class="news-value-point">💡 IT之家 10 月 10 日消息，据博主 @数码闲聊站 今日爆料，某厂阔家族将率先推出搭载 2nm 芯片的阔折叠，结合该博主此前的爆料习惯，预计…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/394.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 10 日消息，据深圳市市场监管局，近期一家小型服务商因“套取 AI 收录标准、批量编造虚假排名”，被市场监管局处以 5 万元罚款。GEO（AI 模型输出结果优化）自 DeepSeek 爆红后兴起，与传统 SEO（搜索引擎优化）争夺网页排名不同，GEO 瞄准的是大模型的回复内容。服务商通过研究 AI 的回答偏好，生产、投放更容易被 AI 引用的内容，帮助商家在 AI 问答中获得曝光，也就是“AI 广告”。本次深圳市市场监管局发现，该公司会通过一套“GEO 分析系统”主动探测大模型回复偏好，向 AI 平台套取收录标准。为了提高广告内容被 AI 引用的概率，该公司还编造虚假行业评分，将相关信息发布到多个社交平台。深圳市市场监管局因此认为，该行为违反《网络反不正当竞争暂行规定》第" data-title="给 AI 植入广告涉“虚假宣传”，深圳一家 GEO 服务商被市场监管局处以 5 万元罚款" data-date="10-10 15:35" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-10 15:35</span>
          <span class="news-item-title">给 AI 植入广告涉“虚假宣传”，深圳一家 GEO 服务商被市场监管局处以 5 万元罚款</span>
          <span class="news-value-point">💡 IT之家 10 月 10 日消息，据深圳市市场监管局，近期一家小型服务商因“套取 AI 收录标准、批量编造虚假排名”，被市场监管局处以 5 万元…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/392.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 10 日消息，人工智能企业 Sierra 当地时间宣布，其与 Meta 以及行业合作伙伴 Shopify、Stripe、沃尔玛、Genesys、Instinct、Rocket 共同推出个人智能体协议 (Personal Agent Protocol, PAP)。PAP 旨在规范个人智能体与企业服务的交互方式，为智能体创造更为高效安全的互动环境。在这一过程中，消费者能确保其利益得到维护，品牌方获得可见性与控制权。该协议基于 OAuth 等成熟标准；运行原则是消费者决定向其个人智能体授予何种访问权限，企业则设定这些智能体可执行操作的参数。" data-title="Meta 与多家伙伴合作推出 PAP 协议：规范个人智能体与企业服务交互方式" data-date="10-10 15:30" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-10 15:30</span>
          <span class="news-item-title">Meta 与多家伙伴合作推出 PAP 协议：规范个人智能体与企业服务交互方式</span>
          <span class="news-value-point">💡 IT之家 10 月 10 日消息，人工智能企业 Sierra 当地时间宣布，其与 Meta 以及行业合作伙伴 Shopify、Stripe、沃尔…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1007674/smart-bird-feeders-attact-pests-too" target="_blank" rel="noopener" data-cat="keji" data-summary="一开始就充满希望。在我安装了350美元269美元的Kiwibit Bird Feeder 2 Pro后几周，几十只五颜六色的小鸟被吸引到我的花园。“看起来像大山雀！”阅读发送到我手机的第一个人工智能驱动的警报。“看起来像欧拉" data-title="My brief romance with an AI bird feeder" data-date="10-10 15:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-10 15:00</span>
          <span class="news-item-title">我与人工智能喂鸟器的短暂浪漫</span>
          <span class="news-item-title-en">My brief romance with an AI bird feeder</span>
          <span class="news-value-point">💡 一开始就充满希望</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/09/nyregion/mamdani-trump-ice-shooting-nyc.html" target="_blank" rel="noopener" data-cat="keji" data-summary="一名联邦特工在纽约市向一名移民开枪，煽动抗议活动后，市长佐赫兰·马姆达尼（ Zohran Mamdani ）的一些盟友质疑他对总统和他自己的警察局的态度。" data-title="Mamdani’s Ability to Persuade Trump Hits Limit in Wake of ICE Shooting" data-date="10-10 09:01" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-10 09:01</span>
          <span class="news-item-title">Mamdani说服特朗普唤醒ICE射击的能力达到极限</span>
          <span class="news-item-title-en">Mamdani’s Ability to Persuade Trump Hits Limit in Wake of ICE Shooting</span>
          <span class="news-value-point">💡 一名联邦特工在纽约市向一名移民开枪，煽动抗议活动后，市长佐赫兰·马姆达尼（ Zohran Mamdani ）的一些盟友质疑他对总统和他自己的警察…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/10/arsenal-v-leeds-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="卫冕冠军被迫从后面深入挖掘，并击败那些可以高举头部回家的游客阅读来自阿联酋体育场的保罗·麦金尼斯的比赛报告一封电子邮件： “星期六快乐，巴里，”马云写道" data-title="Arsenal 2-1 Leeds: Premier League – live" data-date="10-10 21:53" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-10 21:53</span>
          <span class="news-item-title">阿森纳2-1利兹：英超联赛–直播</span>
          <span class="news-item-title-en">Arsenal 2-1 Leeds: Premier League – live</span>
          <span class="news-value-point">💡 卫冕冠军被迫从后面深入挖掘，并击败那些可以高举头部回家的游客阅读来自阿联酋体育场的保罗·麦金尼斯的比赛报告一封电子邮件： “星期六快乐，巴里，”…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/10/chelsea-v-bournemouth-sunderland-v-brighton-and-more-football-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="周六下午开球⚽得分的⚽更新|桌子|十大注意事项|邮件莎拉狮子队昨晚在世界杯资格赛附加赛的第一回合以3比1击败希腊，我们自己的Suzy Wrack分析了性能" data-title="Chelsea v Bournemouth, Sunderland v Brighton, and more: football" data-date="10-10 21:49" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-10 21:49</span>
          <span class="news-item-title">切尔西诉伯恩茅斯、桑德兰诉布莱顿等：足球</span>
          <span class="news-item-title-en">Chelsea v Bournemouth, Sunderland v Brighton, and more: football</span>
          <span class="news-value-point">💡 周六下午开球⚽得分的⚽更新|桌子|十大注意事项|邮件莎拉狮子队昨晚在世界杯资格赛附加赛的第一回合以3比1击败希腊，我们自己的Suzy Wrack…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/10/arsenal-leeds-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳从一个进球中恢复过来，击败了强大的对手，并在漫长的国际休息后重置了他们的状态。枪手在对阵利兹的比赛中表现不佳，防守看起来比上赛季更加脆弱，但" data-title="Bruno Guimarães completes Arsenal comeback to end Leeds’ unbeaten run" data-date="10-10 21:41" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-10 21:41</span>
          <span class="news-item-title">布鲁诺·吉马良斯（ Bruno Guimarães ）完成阿森纳复出，结束了利兹的不败战绩</span>
          <span class="news-item-title-en">Bruno Guimarães completes Arsenal comeback to end Leeds’ unbeaten run</span>
          <span class="news-value-point">💡 阿森纳从一个进球中恢复过来，击败了强大的对手，并在漫长的国际休息后重置了他们的状态</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmx2dpwv02e1o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳和利兹球员在英超比赛后的评分。" data-title="Who changed the game? - player ratings for Arsenal v Leeds" data-date="10-10 21:30" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-10 21:30</span>
          <span class="news-item-title">谁改变了比赛？ -阿森纳对利兹的球员评分</span>
          <span class="news-item-title-en">Who changed the game? - player ratings for Arsenal v Leeds</span>
          <span class="news-value-point">💡 阿森纳和利兹球员在英超比赛后的评分</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/10/premier-league-how-to-watch-manchester-united-tottenham-hotspur" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联和托特纳姆热刺今天的票价如何？以下是需要了解的内容，包括开球时间、电视频道和直播选项随着曼联和托特纳姆热刺抵达老特拉福德" data-title="Premier League today: How to watch Manchester United v Spurs, TV channels &amp; live stream" data-date="10-10 19:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-10 19:30</span>
          <span class="news-item-title">今日英超联赛：如何观看曼联对马刺、电视频道和直播</span>
          <span class="news-item-title-en">Premier League today: How to watch Manchester United v Spurs, TV channels & live stream</span>
          <span class="news-value-point">💡 曼联和托特纳姆热刺今天的票价如何</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cwe9lngxzjpno?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="科尔·帕尔默（ Cole Palmer ）签订了一份新的切尔西合同，合同条款有所改善，直至2034年，这是英超联赛中最长的有效交易之一。" data-title="Palmer signs new Chelsea contract until 2034" data-date="10-10 17:51" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-10 17:51</span>
          <span class="news-item-title">帕尔默与切尔西签订新合同至2034年</span>
          <span class="news-item-title-en">Palmer signs new Chelsea contract until 2034</span>
          <span class="news-value-point">💡 科尔·帕尔默（ Cole Palmer ）签订了一份新的切尔西合同，合同条款有所改善，直至2034年，这是英超联赛中最长的有效交易之一</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/10/premier-league-how-to-watch-arsenal-v-leeds-united" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳和利兹联队今天的表现如何？以下是需要了解的内容，包括开球时间、电视频道和直播选项三分是阿森纳和利兹联队在英超联赛三周后回归时的唯一区别" data-title="Premier League today: How to watch Arsenal v Leeds United, TV channels &amp; live stream" data-date="10-10 14:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-10 14:30</span>
          <span class="news-item-title">今日英超联赛：如何观看阿森纳对利兹联，电视频道和直播</span>
          <span class="news-item-title-en">Premier League today: How to watch Arsenal v Leeds United, TV channels & live stream</span>
          <span class="news-value-point">💡 阿森纳和利兹联队今天的表现如何</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmzxjdvv784xo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼城主教练恩佐·马雷斯卡（ Enzo Maresca ）表示，俱乐部的冠军头衔在英超联赛对他们提出的115项指控中被判有罪后， “绝对没有”受到污染。" data-title="Man City titles &#39;absolutely not&#39; tainted" data-date="10-10 13:56" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-10 13:56</span>
          <span class="news-item-title">曼城冠军头衔“绝对没有”被污染</span>
          <span class="news-item-title-en">Man City titles 'absolutely not' tainted</span>
          <span class="news-value-point">💡 曼城主教练恩佐·马雷斯卡（ Enzo Maresca ）表示，俱乐部的冠军头衔在英超联赛对他们提出的115项指控中被判有罪后， “绝对没有”受到…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6d93ql8jvdko?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="米克尔·阿尔特塔（ Mikel Arteta ）表示，在他担任俱乐部助理经理期间，他的良心对曼城的违规行为很清楚。" data-title="Arteta&#39;s conscience clear over Man City charges" data-date="10-10 05:30" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-10 05:30</span>
          <span class="news-item-title">阿尔特塔对曼城指控的良心清醒</span>
          <span class="news-item-title-en">Arteta's conscience clear over Man City charges</span>
          <span class="news-value-point">💡 米克尔·阿尔特塔（ Mikel Arteta ）表示，在他担任俱乐部助理经理期间，他的良心对曼城的违规行为很清楚</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/09/the-premier-league-is-back-welcome-to-the-new-era-of-post-verdict-unreality" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="随着顶级飞行员的回归，凭借其连续冠军的知识，他们是10年虚假霸权的创始人，第一个问题很简单：感觉如何？互联网：道歉。原来你是对的。这实际上是一个" data-title="The Premier League is back: welcome to the new era of post-verdict unreality | Barney Ronay" data-date="10-10 03:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-10 03:00</span>
          <span class="news-item-title">英超联赛回来了：欢迎来到判决后不真实的新时代| Barney Ronay</span>
          <span class="news-item-title-en">The Premier League is back: welcome to the new era of post-verdict unreality | Barney Ronay</span>
          <span class="news-value-point">💡 随着顶级飞行员的回归，凭借其连续冠军的知识，他们是10年虚假霸权的创始人，第一个问题很简单：感觉如何</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/09/premier-league-so-far-data-pointers-draw-xg" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="平均进球数正在崩溃，因为球员在禁区内进球较少，并且在英超联赛中对阵xGGoals的前锋表现不佳。2026-27赛季平均每场2.70个非点球进球高于上赛季，" data-title="The Premier League so far: draws, underperforming xG and other data pointers" data-date="10-10 02:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-10 02:00</span>
          <span class="news-item-title">到目前为止的英超联赛：平局，表现不佳的xG和其他数据指针</span>
          <span class="news-item-title-en">The Premier League so far: draws, underperforming xG and other data pointers</span>
          <span class="news-value-point">💡 平均进球数正在崩溃，因为球员在禁区内进球较少，并且在英超联赛中对阵xGGoals的前锋表现不佳</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/oct/09/premier-league-team-news-predicted-lineups-for-the-weekend-action" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在经历了艰难的国际休息之后，曼城面对利物浦，而托特纳姆热刺队则在挣扎中前往老特拉福德周六中午12:30 TNT Sports 1场馆阿联酋体育场继续阅读..." data-title="Premier League team news: predicted lineups for the weekend action" data-date="10-10 00:22" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-10 00:22</span>
          <span class="news-item-title">英超球队新闻：周末动作的预测阵容</span>
          <span class="news-item-title-en">Premier League team news: predicted lineups for the weekend action</span>
          <span class="news-value-point">💡 在经历了艰难的国际休息之后，曼城面对利物浦，而托特纳姆热刺队则在挣扎中前往老特拉福德周六中午12:30 TNT Sports 1场馆阿联酋体育场…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/oct/09/premier-league-resumes-manchester-city-in-spotlight-football-news-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="自英超联赛裁定曼城违反100多项财务规则以来，恩佐·马雷斯卡首次面对媒体。《足球周刊》：您可以观看/收听播音员小组讨论周日利物浦和曼彻斯特之间的冲突。" data-title="Maresca says Manchester City titles not tainted; Liverpool’s Isak and Gakpo injured" data-date="10-09 23:55" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">10-09 23:55</span>
          <span class="news-item-title">马雷斯卡说曼城冠军没有受到影响；利物浦的伊萨克和Gakpo受伤</span>
          <span class="news-item-title-en">Maresca says Manchester City titles not tainted; Liverpool’s Isak and Gakpo injured</span>
          <span class="news-value-point">💡 自英超联赛裁定曼城违反100多项财务规则以来，恩佐·马雷斯卡首次面对媒体</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c3y0e8n9q4e0o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="埃弗顿再次出售。首席足球作家菲尔·麦克纳尔蒂（ Phil McNulty ）着眼于老板弗里德金集团（ The Friedkin Group ）寻找出路" data-title="Everton up for sale again - so what next as owners TFG look for a way out?" data-date="10-09 23:38" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-09 23:38</span>
          <span class="news-item-title">埃弗顿再次出售-那么作为所有者TFG寻找出路的下一步是什么？</span>
          <span class="news-item-title-en">Everton up for sale again - so what next as owners TFG look for a way out?</span>
          <span class="news-value-point">💡 埃弗顿再次出售</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ck5ynv45lymdo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联老板迈克尔·卡里克说，他个人受到曼城案的影响，该案发现俱乐部违反了英超联赛的财务规则，并对此事仍有疑问。" data-title="I&#39;ve got my own questions on Man City case" data-date="10-09 22:30" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-09 22:30</span>
          <span class="news-item-title">我对曼城的案子有自己的疑问</span>
          <span class="news-item-title-en">I've got my own questions on Man City case</span>
          <span class="news-value-point">💡 曼联老板迈克尔·卡里克说，他个人受到曼城案的影响，该案发现俱乐部违反了英超联赛的财务规则，并对此事仍有疑问</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/011/515.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 10 日消息，漫步者现已在京东上架 HECATE G2000 Bar 电竞音箱，将于 10 月 16 日发售，定价为 387 元，首发价 349 元。京东漫步者 HECATE G2000 Bar 音箱首发价 349 元直达链接该音箱提供黑白双色可选，使用机甲风格电竞造型，顶部配备一根可插拔式防啸叫麦克风。前面板提供五款主题贴纸供玩家自由更换。产品内置十二种 RGB 效果，支持彩虹、流光等灯效模式。该音箱采用两只 56mm 全频单元与两只 60mm 被动辐射器，可实现 THX 7.1.4 空间音效，音箱额定功率为 3W+3W，峰值达 12W。耳机配备的麦克风搭载 AEC 2.0 回音消除技术，可减少外音干扰。IT之家附产品参数：" data-title="漫步者 HECATE G2000 Bar 电竞音箱上架：四单元声学配置、配可插拔麦克风，首发价 349 元" data-date="10-10 21:54" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-10 21:54</span>
          <span class="news-item-title">漫步者 HECATE G2000 Bar 电竞音箱上架：四单元声学配置、配可插拔麦克风，首发价 349 元</span>
          <span class="news-value-point">💡 IT之家 10 月 10 日消息，漫步者现已在京东上架 HECATE G2000 Bar 电竞音箱，将于 10 月 16 日发售，定价为 387…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-10/10710823.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="景区游人如织，街巷餐饮飘香，文体场馆人气汇聚，家电数码热销出圈……这个国庆假期，消费市场亮点纷呈。增值税发票数据显示，国庆假期，全国服务消费旺盛，相关行业日均销售收入同比增长19.5%，家用电器、数码电子、厨卫等销售增幅较高。" data-title="尺素金声｜发票数据增长19.5%，国庆假期服务消费旺盛" data-date="10-10 21:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-10 21:45</span>
          <span class="news-item-title">尺素金声｜发票数据增长19.5%，国庆假期服务消费旺盛</span>
          <span class="news-value-point">💡 景区游人如织，街巷餐饮飘香，文体场馆人气汇聚，家电数码热销出圈……这个国庆假期，消费市场亮点纷呈</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/software/windows/we-tested-gaming-performance-in-17-year-old-windows-7-against-windows-11-on-a-modern-gaming-pc-older-operating-system-delivers-advantages-in-some-scenarios" target="_blank" rel="noopener" data-cat="zonghe" data-summary="我们设法在现代PC上安装了Windows 7 ，并在八款DirectX 11游戏和两款DirectX 9游戏中对其进行了测试，以了解其游戏性能与今天的Windows 11相比如何。" data-title="We tested gaming performance in 17-year-old Windows 7 on a modern gaming PC against Windows 11" data-date="10-10 21:40" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-10 21:40</span>
          <span class="news-item-title">我们在一台现代游戏PC上针对Windows 11测试了17年前的Windows 7的游戏性能</span>
          <span class="news-item-title-en">We tested gaming performance in 17-year-old Windows 7 on a modern gaming PC against Windows 11</span>
          <span class="news-value-point">💡 我们设法在现代PC上安装了Windows 7 ，并在八款DirectX 11游戏和两款DirectX 9游戏中对其进行了测试，以了解其游戏性能与…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/512.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 10 日消息，锐捷网络为旗下“锐捷星耀家”App 推送公告，称因星耀系列产品退市，“锐捷星耀家”App 将于 2026 年 12 月 31 日 24:00 停止运行，2027 年 1 月 1 日起服务迁移至“锐捷睿易”App。官方表示，新版 App 部分功能可能有所调整，但基础服务功能不受影响。用户可以直接使用星耀家 App 账号密码直接在睿易 App 登录，原有项目信息及基础配置将予以保留。公开信息显示，锐捷目前主要销售睿易系列智能路由器产品，其锐捷睿易 App 主要提供设备管理、无线信道功率修改、Mesh 一键组网、家长控制等管理功能。" data-title="“锐捷星耀家”路由器管理应用将于 12 月 31 日停止运行，用户需迁移至“锐捷睿易”App" data-date="10-10 21:32" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-10 21:32</span>
          <span class="news-item-title">“锐捷星耀家”路由器管理应用将于 12 月 31 日停止运行，用户需迁移至“锐捷睿易”App</span>
          <span class="news-value-point">💡 IT之家 10 月 10 日消息，锐捷网络为旗下“锐捷星耀家”App 推送公告，称因星耀系列产品退市，“锐捷星耀家”App 将于 2026 年 …</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/511.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 10 日消息，小米米家智能温湿度计 3 Pro 今日开售，支持二氧化碳及温湿度检测、3.6 英寸多功能显示，129 元。IT之家从商品页面获悉，新品支持监测室内三项核心指标：温度、湿度及二氧化碳浓度，帮助用户及时了解空气状态，适时通风或联动设备调节环境。产品搭载 Sensirion 新一代低功耗热导原理二氧化碳传感器，持续监测室内空气二氧化碳浓度。不用看数字、不用查标准，三色指示，帮用户判断何时需要通风。新品选用 3.6 英寸大尺寸 LCD 显示屏，外边框更窄，屏占比更高，显示面积更大，数据显示更清晰，远距离读取数据也轻松。日期、星期、时间、温度、湿度、二氧化碳浓度一屏显示，一屏掌握室内环境与日常信息。新品支持小米澎湃智联，搭配具备蓝牙 Mesh 网关功能的设备共同使用，" data-title="小米米家智能温湿度计 3 Pro 开售：二氧化碳检测、三色提醒，129 元" data-date="10-10 21:27" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-10 21:27</span>
          <span class="news-item-title">小米米家智能温湿度计 3 Pro 开售：二氧化碳检测、三色提醒，129 元</span>
          <span class="news-value-point">💡 IT之家 10 月 10 日消息，小米米家智能温湿度计 3 Pro 今日开售，支持二氧化碳及温湿度检测、3.6 英寸多功能显示，129 元</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-10/10710811.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中央安全生产考核巡查二、三季度明察暗访工作正式启动以来，比以往力度更大、要求更严，还首次开展了监管执法问题专项检查。危险货物道路运输是风险很高的行业，因此国家制定了严苛的规范标准，旨在从源头上防范重特大生产安全事故的发生，但考核巡查组在一些地方却发现，存在危货车超载、设备检验报告造假、电子运单管理系统存在漏洞等问题，需要引起高度重视。" data-title="焦点访谈丨91份检验报告全造假！危货车超载运输谁在“放水”？" data-date="10-10 21:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-10 21:26</span>
          <span class="news-item-title">焦点访谈丨91份检验报告全造假！危货车超载运输谁在“放水”？</span>
          <span class="news-value-point">💡 中央安全生产考核巡查二、三季度明察暗访工作正式启动以来，比以往力度更大、要求更严，还首次开展了监管执法问题专项检查</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-10/10710809.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="近日，“超强厄尔尼诺已形成”的话题冲上了热搜。记者从中国气象局国家气候中心了解到，一次“东部型超强厄尔尼诺事件”已于今年9月正式形成。此次事件发展速度快、强度强，预计将成为有系统性监测以来最强厄尔尼诺事件。面对这些说法，不少人也产生了疑问：赤道太平洋的海水升温，为什么会牵动远方的天气？厄尔尼诺来了，今年冬天会更暖吗？明年夏天会更热吗？暴雨、台风、干旱是不是也都归因于它？" data-title="一问到底丨最强厄尔尼诺来了，如何影响全球气候？" data-date="10-10 21:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-10 21:23</span>
          <span class="news-item-title">一问到底丨最强厄尔尼诺来了，如何影响全球气候？</span>
          <span class="news-value-point">💡 近日，“超强厄尔尼诺已形成”的话题冲上了热搜</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-10/10710764.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网银川10月10日电 (记者 李佩珊)金秋时节，硕果盈枝。10月10日，2026年银川市中国农民丰收节在“中国减贫地标”永宁县闽宁镇启幕。当地农民代表、基层工作者及市民游客齐聚贺兰山脚下，以文艺展演、农产品展销、趣味互动等多样形式共庆丰收，集中展现乡村振兴稳步推进的鲜活成效。" data-title="2026银川农民丰收节在闽宁镇启幕" data-date="10-10 21:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-10 21:07</span>
          <span class="news-item-title">2026银川农民丰收节在闽宁镇启幕</span>
          <span class="news-value-point">💡 中新网银川10月10日电 (记者 李佩珊)金秋时节，硕果盈枝</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-10/10710784.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="辟 谣 “河南新乡可直接申领摩托车D证”不实" data-title="“河南新乡可直接申领摩托车D证”不实（2026·10·10）" data-date="10-10 21:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-10 21:03</span>
          <span class="news-item-title">“河南新乡可直接申领摩托车D证”不实（2026·10·10）</span>
          <span class="news-value-point">💡 辟 谣 “河南新乡可直接申领摩托车D证”不实</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/011/508.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 10 日消息，小米金沙江充电宝超薄磁吸 10000 45W 今日上架小米有品，售价 399 元（点击前往）。IT之家从商品页面获悉，新品搭载小米金沙江硅碳负极电池，能量密度高达 840Wh/L，拥有 16% 旗舰级含硅量，通过新国标认证。依托于旗舰同源小米金沙江电池先进技术，精密堆叠工艺再升级，将两块 5000mAh 电池内置于纤薄机身，重量约 195g 。集成专属智能快充芯片，广泛兼容 BC、QC、PD 等多种主流充电协议。连接充电设备时可自动识别所需充电电流，智能匹配充电功率，快充更稳更安全。新品支持 20W Max 磁吸无线快充、45W Max 有线快充、有线无线双设备同时充、30W Max 快速自充回血。新品内置 NTC 智能控温芯片，实时精准监测电芯温度，搭配大" data-title="399 元，小米金沙江充电宝超薄磁吸 10000 45W 上架" data-date="10-10 21:01" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-10 21:01</span>
          <span class="news-item-title">399 元，小米金沙江充电宝超薄磁吸 10000 45W 上架</span>
          <span class="news-value-point">💡 IT之家 10 月 10 日消息，小米金沙江充电宝超薄磁吸 10000 45W 今日上架小米有品，售价 399 元（点击前往）</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1008957/lg-mrgb95b-rgb-led-tv-review" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在电视方面， LG的名字长期以来一直是OLED的代名词，一直领先于三星和索尼作为顶级OLED制造商。但2026年的重点是RGB LED电视。几乎所有大公司都发布了采用新技术的车型-包括" data-title="LG’s RGB LED TV is good for certain situations, but an OLED is better" data-date="10-10 21:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-10 21:00</span>
          <span class="news-item-title">LG的RGB LED电视适用于某些情况，但OLED更好</span>
          <span class="news-item-title-en">LG’s RGB LED TV is good for certain situations, but an OLED is better</span>
          <span class="news-value-point">💡 在电视方面， LG的名字长期以来一直是OLED的代名词，一直领先于三星和索尼作为顶级OLED制造商</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-10/10710773.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网昆明10月10日电 (韩帅南 陆星羽)“我父亲沈从龙生前并未向我讲述过‘滇批’的故事，这次回到昆明，我才真正读懂这些泛黄档案里藏着的家国情怀与人间暖意。”10日，“滇批”书写者后人、美籍华人沈昆回到云南昆明寻根溯源时如是说。" data-title="“滇批”书写者后人昆明寻根 溯源工业抗战史中的家国情怀" data-date="10-10 20:58" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-10 20:58</span>
          <span class="news-item-title">“滇批”书写者后人昆明寻根 溯源工业抗战史中的家国情怀</span>
          <span class="news-value-point">💡 中新网昆明10月10日电 (韩帅南 陆星羽)“我父亲沈从龙生前并未向我讲述过‘滇批’的故事，这次回到昆明，我才真正读懂这些泛黄档案里藏着的家国情…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/09/nyregion/oscar-belgal-ice-shooting-nyc.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="28岁的奥斯卡·贝尔加尔（ Oscar Belgal ）经常在大理石山大道（ Marble Hill Avenue ）修车和播放音乐，那里很少有居民知道他的犯罪记录" data-title="What We Know About the Man Shot by ICE" data-date="10-10 20:43" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-10 20:43</span>
          <span class="news-item-title">我们对ICE射击男子的了解</span>
          <span class="news-item-title-en">What We Know About the Man Shot by ICE</span>
          <span class="news-value-point">💡 28岁的奥斯卡·贝尔加尔（ Oscar Belgal ）经常在大理石山大道（ Marble Hill Avenue ）修车和播放音乐，那里很少有…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/10/us/politics/trump-inflation-midterms-republicans.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="通货膨胀在许多层面上伤害了美国人：农民、卡车司机和消费者。它还将选举地图扩展到几个月前安全的共和党国家。" data-title="Economic Pain and an Unpopular Trump Put G.O.P. on its Heels With Three Weeks to Go" data-date="10-10 20:10" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-10 20:10</span>
          <span class="news-item-title">经济痛苦和不受欢迎的特朗普让G.O.P.紧追不舍，还有三周时间</span>
          <span class="news-item-title-en">Economic Pain and an Unpopular Trump Put G.O.P. on its Heels With Three Weeks to Go</span>
          <span class="news-value-point">💡 通货膨胀在许多层面上伤害了美国人：农民、卡车司机和消费者</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/pc-gaming/dlss-5-on-pac-man-is-a-creepypasta-one-rendering-mode-even-removes-the-eyes-of-a-ghost" target="_blank" rel="noopener" data-cat="zonghe" data-summary="致力于DLSS 5实验的俄罗斯YouTube频道尝试吃豆人，它真的被诅咒了。" data-title="Russian modder slaps DLSS 5 onto Pac-Man with 4x Multipass" data-date="10-10 20:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-10 20:00</span>
          <span class="news-item-title">俄罗斯改装工使用4x Multipass将DLSS 5拍到吃豆人身上</span>
          <span class="news-item-title-en">Russian modder slaps DLSS 5 onto Pac-Man with 4x Multipass</span>
          <span class="news-value-point">💡 致力于DLSS 5实验的俄罗斯YouTube频道尝试吃豆人，它真的被诅咒了</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-10 21:55（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
