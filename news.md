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
      <span>2026-10-15 14:36 抓取更新</span>
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
        <span class="channel-count">49</span>
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
        <span class="channel-count">4</span>
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
  <div class="ov-item"><span class="ov-num">49</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">7</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×20 · 纽约时报×7</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/10-15/10714991.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网西安10月15日电 (记者 张一辰 李一璠)10月15日，第七届海峡两岸(陕西)经贸科技合作大会(以下简称“陕台会”)在陕西西安开幕。" data-title="第七届海峡两岸（陕西）经贸科技合作大会在西安开幕" data-date="10-15 14:31" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-15 14:31</span>
      </div>
      <h2 class="hero-featured-title">第七届海峡两岸（陕西）经贸科技合作大会在西安开幕</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/013/375.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 15 日消息，据路透社今天（15 日）午间报道，全球金融监管标准制定机构金融稳定理事会向银行及其他企业发出呼吁，要求加强对 AI 智能体的人工监督，并将这一要求纳入 AI 风险管理的最终版指引。金融稳定理事会公布指引之际，各国监管机构也在加紧防范 AI 带来的风险，其中就包含了利用 AI 发动网络攻击的威胁。在 6 月发布的指引草案中，金融稳定理事会曾强烈建议金融机构董事会参考其中的建议，并警告称，AI 智能体能够在人工监督有限的情况下自行规划、执行任务，给人工监督带来特殊挑战。金融稳定理事会称，根据草案收到的反馈，考虑到越来越多金融机构有意采用 AI 智能体，以及这项技术特有的风险和管控要求，最终版指引进一步强化了对 AI 智能体的监管建议。一系列事件加深了政策制定者的" data-title="全球金融监管标准制定机构呼吁：银行、企业要加强对 AI 智能体的人工监管" data-date="10-15 14:22" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">全球金融监管标准制定机构呼吁：银行、企业要加强对 AI 智能体的人工监管</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/c9kgj41jgm5go?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="前英格兰主教练加雷斯·索斯盖特（ Gareth Southgate ）表示，他认为自己不会重返英超联赛的俱乐部管理层。" data-title="Southgate does not see return to Premier League management" data-date="10-15 13:39" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">Southgate does not see return to Premier League management</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/013/386.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 15 日消息，华硕 (ASUS) 现已在电商平台上线 PRO WS702 机箱。这一型号面向工作站装机，提供 8 条扩展槽，支持 E-ATX 主板，兼容 400mm 扩展卡，标价 999 元但尚未开售。PRO WS702 主体部分三维 248×530×555 (mm)，电源限长 180mm、处理器散热器限高 190mm，提供 4 个 3.5&quot; / 2.5&quot; 盘位、2 个 2.5&quot; 盘位，背部拥有 35mm 理线空间和多处穿线孔与绑线固定点，集成双卡固定支架。该机箱拥有 7 个风扇位，其中前部支持 3 颗 120mm / 140mm 或 2 颗 160mm / 180mm / 200mm 风扇，上部支持 3 颗 120mm / 140mm 风扇，后部支持 1 颗 120mm" data-title="华硕上线工作站机箱 PRO WS702：支持 E" data-date="10-15 14:35" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">华硕上线工作站机箱 PRO WS702：支持 E</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-15/10714991.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网西安10月15日电 (记者 张一辰 李一璠)10月15日，第七届海峡两岸(陕西)经贸科技合作大会(以下简称“陕台会”)在陕西西安开幕。" data-title="第七届海峡两岸（陕西）经贸科技合作大会在西安开幕" data-date="10-15 14:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-15 14:31</span>
          <span class="news-item-title">第七届海峡两岸（陕西）经贸科技合作大会在西安开幕</span>
          <span class="news-value-point">💡 中新网西安10月15日电 (记者 张一辰 李一璠)10月15日，第七届海峡两岸(陕西)经贸科技合作大会(以下简称“陕台会”)在陕西西安开幕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-15/10714997.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="原标题：20031015！" data-title="23年前，中国人飞向太空！回望载入史册的那一天" data-date="10-15 14:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-15 14:21</span>
          <span class="news-item-title">23年前，中国人飞向太空！回望载入史册的那一天</span>
          <span class="news-value-point">💡 原标题：20031015</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-15/10714984.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月15日电 记者15日从中国水利部获悉，北京时间10月14日晚，在法国马赛召开的国际灌排委员会第77届国际执行理事会会议上，2026年(第十三批)世界灌溉工程遗产名录正式公布，中国申报的河南沁河广利渠(五龙口)、甘肃讨赖河绿洲灌溉系统、江西上饶市广信黄沙渠、福建长泰龙津古陂灌溉工程全部成功入选。至此，中国的世界灌溉工程遗产总数已达46项。" data-title="中国再添4处世界灌溉工程遗产" data-date="10-15 14:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-15 14:10</span>
          <span class="news-item-title">中国再添4处世界灌溉工程遗产</span>
          <span class="news-value-point">💡 中新社北京10月15日电 记者15日从中国水利部获悉，北京时间10月14日晚，在法国马赛召开的国际灌排委员会第77届国际执行理事会会议上，202…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-15/10714967.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月15日电 揣着“威胁”滤镜，美国能把中国AI歪曲成啥样？" data-title="美式双标，“蒸馏”不了真相" data-date="10-15 14:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-15 14:06</span>
          <span class="news-item-title">美式双标，“蒸馏”不了真相</span>
          <span class="news-value-point">💡 中新网10月15日电 揣着“威胁”滤镜，美国能把中国AI歪曲成啥样</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-15/10714974.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="有些信，寄出时只想抵达亲人手中，却在90多年后抵达了更多人的心里。" data-title="红星照耀中国｜写信的人没等到这一天…" data-date="10-15 13:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-15 13:55</span>
          <span class="news-item-title">红星照耀中国｜写信的人没等到这一天…</span>
          <span class="news-value-point">💡 有些信，寄出时只想抵达亲人手中，却在90多年后抵达了更多人的心里</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-15/10714934.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月15日电 中国国务院总理李强10月15日在中朝新鸭绿江大桥开通仪式上发表视频致辞。" data-title="李强在中朝新鸭绿江大桥开通仪式上发表视频致辞" data-date="10-15 13:38" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-15 13:38</span>
          <span class="news-item-title">李强在中朝新鸭绿江大桥开通仪式上发表视频致辞</span>
          <span class="news-value-point">💡 中新社北京10月15日电 中国国务院总理李强10月15日在中朝新鸭绿江大桥开通仪式上发表视频致辞</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-15/10714933.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="前两天，针对赖清德所谓“双十”讲话，大陆央媒中央广播电视总台刊发“总台海峡时评”，直指：赖清德鬼话连篇再次暴露其“台独”恶劣本性。谭主注意到，这句“赖清德鬼话连篇”迅速在两岸舆论场引发关注。" data-title="日月谭天丨一句“赖清德鬼话连篇”何以引发两岸关注" data-date="10-15 13:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-15 13:27</span>
          <span class="news-item-title">日月谭天丨一句“赖清德鬼话连篇”何以引发两岸关注</span>
          <span class="news-value-point">💡 前两天，针对赖清德所谓“双十”讲话，大陆央媒中央广播电视总台刊发“总台海峡时评”，直指：赖清德鬼话连篇再次暴露其“台独”恶劣本性</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-15/10714904.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="10月15日，国务院总理李强在中朝新鸭绿江大桥开通仪式上发表视频致辞。 新华社记者 黄敬文 摄 新华社北京10月15日电(记者孙楠、丁非白)国务院总理李强10月15日在中朝新鸭绿江大桥开通仪式上发表视频致辞。" data-title="李强在中朝新鸭绿江大桥开通仪式上发表视频致辞" data-date="10-15 13:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-15 13:21</span>
          <span class="news-item-title">李强在中朝新鸭绿江大桥开通仪式上发表视频致辞</span>
          <span class="news-value-point">💡 10月15日，国务院总理李强在中朝新鸭绿江大桥开通仪式上发表视频致辞</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-15/10714889.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月15日电 据日本共同社报道，当地时间14日，针对俄罗斯以涉嫌从事间谍活动为由拘留一名日本记者一事，日本外务省召见了俄罗斯驻日本大使尼古拉·诺兹德廖夫。" data-title="就日本记者被拘事件 日本外务省召见俄罗斯大使提出抗议" data-date="10-15 11:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-15 11:16</span>
          <span class="news-item-title">就日本记者被拘事件 日本外务省召见俄罗斯大使提出抗议</span>
          <span class="news-value-point">💡 中新网10月15日电 据日本共同社报道，当地时间14日，针对俄罗斯以涉嫌从事间谍活动为由拘留一名日本记者一事，日本外务省召见了俄罗斯驻日本大使尼…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-15/10714839.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月15日电(记者 刁炜)随着地面战逐渐白热化，位于也门西南部的该国第三大城市塔伊兹，成为胡塞武装、也门政府军激烈争夺的焦点。尤其对后者来讲，塔伊兹之战更是“关乎生死存亡”。" data-title="胡塞武装连日猛攻，也门第三大城市“弥漫绝望情绪”" data-date="10-15 10:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-15 10:11</span>
          <span class="news-item-title">胡塞武装连日猛攻，也门第三大城市“弥漫绝望情绪”</span>
          <span class="news-value-point">💡 中新网10月15日电(记者 刁炜)随着地面战逐渐白热化，位于也门西南部的该国第三大城市塔伊兹，成为胡塞武装、也门政府军激烈争夺的焦点</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-15/10714797.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网巴黎10月15日电 (记者 李洋)在2026年北极圈论坛大会期间，“中国鄂温克驯鹿社区的气候与社会变迁”边会于当地时间10日在冰岛首都雷克雅未克举行。" data-title="“中国鄂温克驯鹿社区的气候与社会变迁”边会在冰岛举行" data-date="10-15 10:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-15 10:11</span>
          <span class="news-item-title">“中国鄂温克驯鹿社区的气候与社会变迁”边会在冰岛举行</span>
          <span class="news-value-point">💡 中新网巴黎10月15日电 (记者 李洋)在2026年北极圈论坛大会期间，“中国鄂温克驯鹿社区的气候与社会变迁”边会于当地时间10日在冰岛首都雷克…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/14/us/politics/vance-talarico-attacks.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在德克萨斯州的一次集会上，副总统暗示民主党参议院候选人是同性恋，这一评论被批评为同性恋恐惧症。" data-title="Vance’s Talarico Attacks Show His Penchant for Personal Broadsides" data-date="10-15 10:08" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-15 10:08</span>
          <span class="news-item-title">Vance的Talarico攻击显示了他对个人宽边的偏爱</span>
          <span class="news-item-title-en">Vance’s Talarico Attacks Show His Penchant for Personal Broadsides</span>
          <span class="news-value-point">💡 在德克萨斯州的一次集会上，副总统暗示民主党参议院候选人是同性恋，这一评论被批评为同性恋恐惧症</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/14/us/politics/trump-administration-kimberly-guilfoyle-women.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="在特朗普总统的第二个任期内，自愿或非自愿离开的人都是女性官员。" data-title="The Trump Administration and the Shrinking Number of Women in Top Roles" data-date="10-15 09:05" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-15 09:05</span>
          <span class="news-item-title">特朗普政府和担任高级职位的女性人数不断减少</span>
          <span class="news-item-title-en">The Trump Administration and the Shrinking Number of Women in Top Roles</span>
          <span class="news-value-point">💡 在特朗普总统的第二个任期内，自愿或非自愿离开的人都是女性官员</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c6lyezge4xywo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="BBC深入分析将界定特朗普总统任期最后两年的选举前景，包括关键民调、选战以及议题。" data-title="美国中期选举2026：赢会赢在哪里，输会输在哪里？" data-date="10-15 08:20" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-15 08:20</span>
          <span class="news-item-title">美国中期选举2026：赢会赢在哪里，输会输在哪里？</span>
          <span class="news-value-point">💡 BBC深入分析将界定特朗普总统任期最后两年的选举前景，包括关键民调、选战以及议题</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/14/world/europe/ukraine-starlink-energy.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="一次大规模的袭击使基辅60万人的电力中断，五角大楼资助的卫星互联网计划似乎在没有任何警告的情况下受到遏制。" data-title="Ukraine’s Vulnerability Grows as Starlink Is Restricted and Russia Escalates" data-date="10-15 01:11" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-15 01:11</span>
          <span class="news-item-title">随着Starlink受限和俄罗斯升级，乌克兰的脆弱性加剧</span>
          <span class="news-item-title-en">Ukraine’s Vulnerability Grows as Starlink Is Restricted and Russia Escalates</span>
          <span class="news-value-point">💡 一次大规模的袭击使基辅60万人的电力中断，五角大楼资助的卫星互联网计划似乎在没有任何警告的情况下受到遏制</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/013/375.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 15 日消息，据路透社今天（15 日）午间报道，全球金融监管标准制定机构金融稳定理事会向银行及其他企业发出呼吁，要求加强对 AI 智能体的人工监督，并将这一要求纳入 AI 风险管理的最终版指引。金融稳定理事会公布指引之际，各国监管机构也在加紧防范 AI 带来的风险，其中就包含了利用 AI 发动网络攻击的威胁。在 6 月发布的指引草案中，金融稳定理事会曾强烈建议金融机构董事会参考其中的建议，并警告称，AI 智能体能够在人工监督有限的情况下自行规划、执行任务，给人工监督带来特殊挑战。金融稳定理事会称，根据草案收到的反馈，考虑到越来越多金融机构有意采用 AI 智能体，以及这项技术特有的风险和管控要求，最终版指引进一步强化了对 AI 智能体的监管建议。一系列事件加深了政策制定者的" data-title="全球金融监管标准制定机构呼吁：银行、企业要加强对 AI 智能体的人工监管" data-date="10-15 14:22" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-15 14:22</span>
          <span class="news-item-title">全球金融监管标准制定机构呼吁：银行、企业要加强对 AI 智能体的人工监管</span>
          <span class="news-value-point">💡 IT之家 10 月 15 日消息，据路透社今天（15 日）午间报道，全球金融监管标准制定机构金融稳定理事会向银行及其他企业发出呼吁，要求加强对 …</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-15/10714968.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="近期，美国家安全局、网络安全与基础设施安全局、联邦调查局联合发布公告，指责中国人工智能企业对美开展“工业规模”蒸馏，获取美前沿模型能力，并向美企提出相关防御措施建议。" data-title="“蒸馏”借口背后，霸权才是真相 | 新漫评" data-date="10-15 14:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-15 14:08</span>
          <span class="news-item-title">“蒸馏”借口背后，霸权才是真相 | 新漫评</span>
          <span class="news-value-point">💡 近期，美国家安全局、网络安全与基础设施安全局、联邦调查局联合发布公告，指责中国人工智能企业对美开展“工业规模”蒸馏，获取美前沿模型能力，并向美企…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/013/360.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 15 日消息，型号为“iPhone19,4”的苹果手机昨日（10 月 14 日）现身 GeekBench 跑分库，目前显示关于 CPU、GPU 和 AI 的多条跑分记录。基于苹果型号列表等信息，该手机关联苹果首款折叠 iPhone Duo。在 GeekBench 跑分平台上，目前 iPhone Duo 在 GeekBench 7 CPU 中共有 6 条记录，在 GeekBench 7 GPU 中共有 3 条记录，在 GeekBench AI 中有 1 条记录。从跑分成绩来看，和 iPhone 18 Pro 系列的差别并不大。在 CPU 跑分方面，这里附上多核跑分最高的一条记录，显示单核成绩为 3,985 分，多核成绩为 11,271 分。Geekbench 信息显示，iP" data-title="苹果首款折叠 iPhone Duo 跑分曝光：iPhone 18 Pro 同款 6 核 4.93GHz CPU" data-date="10-15 14:04" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-15 14:04</span>
          <span class="news-item-title">苹果首款折叠 iPhone Duo 跑分曝光：iPhone 18 Pro 同款 6 核 4.93GHz CPU</span>
          <span class="news-value-point">💡 IT之家 10 月 15 日消息，型号为“iPhone19,4”的苹果手机昨日（10 月 14 日）现身 GeekBench 跑分库，目前显示关…</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/503303.html" target="_blank" rel="noopener" data-cat="keji" data-summary="给企业Agent打了个样" data-title="7天几百元开一家店！用千问办公电商版，立省启动资金5万元" data-date="10-15 09:56" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-15 09:56</span>
          <span class="news-item-title">7天几百元开一家店！用千问办公电商版，立省启动资金5万元</span>
          <span class="news-value-point">💡 给企业Agent打了个样</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/14/ricursive-intelligence-is-betting-on-ai-designed-chips-to-help-solve-the-compute-crisis/" target="_blank" rel="noopener" data-cat="keji" data-summary="创始人详细介绍了他们的创业公司如何开发能够设计芯片、从每次迭代中学习并改进后续设计的人工智能，所有这些都是为了实现芯片设计过程的自动化和加速。" data-title="Ricursive Intelligence is betting on AI-designed chips to help solve the compute crisis" data-date="10-15 09:01" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-15 09:01</span>
          <span class="news-item-title">Ricursive Intelligence押注于人工智能设计的芯片，以帮助解决计算危机</span>
          <span class="news-item-title-en">Ricursive Intelligence is betting on AI-designed chips to help solve the compute crisis</span>
          <span class="news-value-point">💡 创始人详细介绍了他们的创业公司如何开发能够设计芯片、从每次迭代中学习并改进后续设计的人工智能，所有这些都是为了实现芯片设计过程的自动化和加速</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/14/technology/anthropic-ipo-revenue-profit.html" target="_blank" rel="noopener" data-cat="keji" data-summary="该公司周三举行了投资者会议，计划最快在下个月进行大规模的首次公开募股。" data-title="Anthropic Says Revenue Jumped 45% to $16.8 Billion in Third Quarter" data-date="10-15 07:57" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-15 07:57</span>
          <span class="news-item-title">Anthropic表示，第三季度收入增长了45% ，达到168亿美元</span>
          <span class="news-item-title-en">Anthropic Says Revenue Jumped 45% to $16.8 Billion in Third Quarter</span>
          <span class="news-value-point">💡 该公司周三举行了投资者会议，计划最快在下个月进行大规模的首次公开募股</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/news/1011654/mckinsey-ai-client-interview" target="_blank" rel="noopener" data-cat="keji" data-summary="据《华尔街日报》报道，咨询公司麦肯锡公司（ McKinsey &amp; Company ）将要求一些入门级候选人在面试过程中与人工智能模拟客户进行10分钟的对话。人工智能模拟“旨在反射" data-title="McKinsey is making job applicants spar with a fake AI client" data-date="10-15 06:53" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-15 06:53</span>
          <span class="news-item-title">麦肯锡正在让求职者与虚假的人工智能客户争吵</span>
          <span class="news-item-title-en">McKinsey is making job applicants spar with a fake AI client</span>
          <span class="news-value-point">💡 据《华尔街日报》报道，咨询公司麦肯锡公司（ McKinsey & Company ）将要求一些入门级候选人在面试过程中与人工智能模拟客户进行10…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1011500/openai-state-lawsuits-chatgpt-safety" target="_blank" rel="noopener" data-cat="keji" data-summary="据路透社早些时候报道， OpenAI正面临来自美国八个州的新一波诉讼，指控该公司伤害儿童并误导客户ChatGPT的安全。这些诉讼分别由爱荷华州、堪萨斯州、内布拉斯加州、" data-title="Eight states sue OpenAI, saying ChatGPT isn’t safe for kids" data-date="10-15 05:11" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-15 05:11</span>
          <span class="news-item-title">八个州起诉OpenAI ，称ChatGPT对儿童不安全</span>
          <span class="news-item-title-en">Eight states sue OpenAI, saying ChatGPT isn’t safe for kids</span>
          <span class="news-value-point">💡 据路透社早些时候报道， OpenAI正面临来自美国八个州的新一波诉讼，指控该公司伤害儿童并误导客户ChatGPT的安全</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1011311/the-ai-race-is-back-on" target="_blank" rel="noopener" data-cat="keji" data-summary="上周， Anthropic和OpenAI看起来像是在进行人工智能竞赛，以越来越强大的模型领先，使他们的竞争对手陷入困境。谷歌似乎无可救药地远远落后，而Meta ，尽管花费了数十亿美元来复兴我" data-title="The AI race is back on" data-date="10-15 03:06" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-15 03:06</span>
          <span class="news-item-title">人工智能竞赛又开始了</span>
          <span class="news-item-title-en">The AI race is back on</span>
          <span class="news-value-point">💡 上周， Anthropic和OpenAI看起来像是在进行人工智能竞赛，以越来越强大的模型领先，使他们的竞争对手陷入困境</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1011324/apple-tv-4k-missed-features" target="_blank" rel="noopener" data-cat="keji" data-summary="自上次Apple TV 4K发布以来，已经有四年了，在那段时间里，人们对接下来的功能寄予了很多希望和梦想。全新芯片， 4K/120Hz支持，音频直通，远程定位器，更好的家庭控制" data-title="As a TV enthusiast, I was hoping for more from the Apple TV 4K" data-date="10-15 02:38" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-15 02:38</span>
          <span class="news-item-title">作为电视爱好者，我希望从Apple TV 4K获得更多</span>
          <span class="news-item-title-en">As a TV enthusiast, I was hoping for more from the Apple TV 4K</span>
          <span class="news-value-point">💡 自上次Apple TV 4K发布以来，已经有四年了，在那段时间里，人们对接下来的功能寄予了很多希望和梦想</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1011369/youtube-music-ai-label" target="_blank" rel="noopener" data-cat="keji" data-summary="YouTube正在为使用人工智能“更改或完全生成”的曲目添加“人工智能制造”标签，其方法与将人工智能标签应用于视频的现有流程类似。听起来这并不适用于人工智能工具的任何和所有使用" data-title="YouTube sticks new labels on AI" data-date="10-15 02:22" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-15 02:22</span>
          <span class="news-item-title">YouTube在人工智能上贴上新标签</span>
          <span class="news-item-title-en">YouTube sticks new labels on AI</span>
          <span class="news-value-point">💡 YouTube正在为使用人工智能“更改或完全生成”的曲目添加“人工智能制造”标签，其方法与将人工智能标签应用于视频的现有流程类似</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/14/apate-sends-ai-agents-undercover-to-get-scammed-so-they-can-gather-fraud-intelligence/" target="_blank" rel="noopener" data-cat="keji" data-summary="大多数公司使用人工智能代理来更快地运送产品或加快工作流程。Apate.ai派他们卧底去骗人。" data-title="Apate sends AI agents undercover to get scammed so they can gather fraud intelligence" data-date="10-15 02:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-15 02:00</span>
          <span class="news-item-title">Apate派遣人工智能特工进行卧底欺诈，以便收集欺诈情报</span>
          <span class="news-item-title-en">Apate sends AI agents undercover to get scammed so they can gather fraud intelligence</span>
          <span class="news-value-point">💡 大多数公司使用人工智能代理来更快地运送产品或加快工作流程</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/14/technology/ai-agents-communication-tech-dinner-party.html" target="_blank" rel="noopener" data-cat="keji" data-summary="随着人工智能机器人的传播，我们越来越多地看到这些数字实体是如何互动的，以及它们彼此之间在谈论什么。" data-title="22 People Got Together For a Dinner Party. So Did Their A.I. Agents." data-date="10-15 01:35" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-15 01:35</span>
          <span class="news-item-title">22个人聚在一起参加晚宴。他们的人工智能特工也是如此。</span>
          <span class="news-item-title-en">22 People Got Together For a Dinner Party. So Did Their A.I. Agents.</span>
          <span class="news-value-point">💡 随着人工智能机器人的传播，我们越来越多地看到这些数字实体是如何互动的，以及它们彼此之间在谈论什么</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/14/world/europe/ukraine-intelligence-sharing-zelensky-uk.html" target="_blank" rel="noopener" data-cat="keji" data-summary="乌克兰总统弗拉基米尔·泽伦斯基（ Volodymyr Zelensky ）表示，乌克兰“没有从我们的伙伴那里得到关于俄罗斯袭击的早期特朗普总统曾表示，华盛顿仍在“分享情报”。" data-title="Zelensky Visits U.K. as Ukraine Presses Allies on Intelligence Sharing" data-date="10-15 01:13" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-15 01:13</span>
          <span class="news-item-title">泽伦斯基访问英国，乌克兰就情报共享向盟国施压</span>
          <span class="news-item-title-en">Zelensky Visits U.K. as Ukraine Presses Allies on Intelligence Sharing</span>
          <span class="news-value-point">💡 乌克兰总统弗拉基米尔·泽伦斯基（ Volodymyr Zelensky ）表示，乌克兰“没有从我们的伙伴那里得到关于俄罗斯袭击的早期特朗普总统曾…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1011276/openai-employee-unreleased-product-plans" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI声称，一名前员工在加入苹果之前，拿走了100多份与其产品计划相关的文件。在周三提交的一份文件中， OpenAI指控这名未透露姓名的员工将此信息发送到个人账户，然后将其呈现" data-title="OpenAI claims an ex-employee took its product plans and presented them to Apple" data-date="10-15 00:43" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-15 00:43</span>
          <span class="news-item-title">OpenAI声称，一名前员工拿走了其产品计划并将其提交给苹果</span>
          <span class="news-item-title-en">OpenAI claims an ex-employee took its product plans and presented them to Apple</span>
          <span class="news-value-point">💡 OpenAI声称，一名前员工在加入苹果之前，拿走了100多份与其产品计划相关的文件</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">4 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c9kgj41jgm5go?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="前英格兰主教练加雷斯·索斯盖特（ Gareth Southgate ）表示，他认为自己不会重返英超联赛的俱乐部管理层。" data-title="Southgate does not see return to Premier League management" data-date="10-15 13:39" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-15 13:39</span>
          <span class="news-item-title">Southgate没有看到英超联赛管理层的回归</span>
          <span class="news-item-title-en">Southgate does not see return to Premier League management</span>
          <span class="news-value-point">💡 前英格兰主教练加雷斯·索斯盖特（ Gareth Southgate ）表示，他认为自己不会重返英超联赛的俱乐部管理层</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/news/articles/c83vq9vpwwr1o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="自从俱乐部因违反英超联赛规则而被判有罪以来，总理一直承受着越来越大的压力。" data-title="Burnham had two hospitality dinners with Man City chairman, deleted records show" data-date="10-15 09:07" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-15 09:07</span>
          <span class="news-item-title">伯纳姆与曼城主席共进了两顿招待晚餐，删除了记录显示</span>
          <span class="news-item-title-en">Burnham had two hospitality dinners with Man City chairman, deleted records show</span>
          <span class="news-value-point">💡 自从俱乐部因违反英超联赛规则而被判有罪以来，总理一直承受着越来越大的压力</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cvp8g57ne53xo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利桑德罗·马丁内斯（ Lisandro Martinez ）在曼联冠军联赛被马德里竞技（ Atletico Madrid ）击败后发表的爆炸性评论让足球总监杰森·威尔科克斯（ Jason Wilcox ）" data-title="Wilcox the target again in another damaging Man Utd fallout" data-date="10-14 23:30" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-14 23:30</span>
          <span class="news-item-title">威尔科克斯在另一次曼联破坏性影响中再次成为目标</span>
          <span class="news-item-title-en">Wilcox the target again in another damaging Man Utd fallout</span>
          <span class="news-value-point">💡 利桑德罗·马丁内斯（ Lisandro Martinez ）在曼联冠军联赛被马德里竞技（ Atletico Madrid ）击败后发表的爆炸性评…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ckwy4nj4842qo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="延长三周的休息时间可能比英超联赛中任何其他球队都更能让切尔西受益。" data-title="Did Chelsea benefit most from extended international break?" data-date="10-14 18:43" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-14 18:43</span>
          <span class="news-item-title">切尔西是否从延长的国际休息中获益最多？</span>
          <span class="news-item-title-en">Did Chelsea benefit most from extended international break?</span>
          <span class="news-value-point">💡 延长三周的休息时间可能比英超联赛中任何其他球队都更能让切尔西受益</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/013/386.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 15 日消息，华硕 (ASUS) 现已在电商平台上线 PRO WS702 机箱。这一型号面向工作站装机，提供 8 条扩展槽，支持 E-ATX 主板，兼容 400mm 扩展卡，标价 999 元但尚未开售。PRO WS702 主体部分三维 248×530×555 (mm)，电源限长 180mm、处理器散热器限高 190mm，提供 4 个 3.5&quot; / 2.5&quot; 盘位、2 个 2.5&quot; 盘位，背部拥有 35mm 理线空间和多处穿线孔与绑线固定点，集成双卡固定支架。该机箱拥有 7 个风扇位，其中前部支持 3 颗 120mm / 140mm 或 2 颗 160mm / 180mm / 200mm 风扇，上部支持 3 颗 120mm / 140mm 风扇，后部支持 1 颗 120mm" data-title="华硕上线工作站机箱 PRO WS702：支持 E" data-date="10-15 14:35" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-15 14:35</span>
          <span class="news-item-title">华硕上线工作站机箱 PRO WS702：支持 E</span>
          <span class="news-value-point">💡 IT之家 10 月 15 日消息，华硕 (ASUS) 现已在电商平台上线 PRO WS702 机箱</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-15/10714995.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网太原10月15日电 (记者 胡健)“秋意浓西山 红叶映国保——2026年崛围(山围)山·龙山红叶季文化活动”15日在山西太原净因寺广场启动，龙山石窟博物馆设分会场，活动持续至10月31日。" data-title="赏红叶访古建 千年国保在漫山红叶中“活”起来" data-date="10-15 14:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-15 14:23</span>
          <span class="news-item-title">赏红叶访古建 千年国保在漫山红叶中“活”起来</span>
          <span class="news-value-point">💡 中新网太原10月15日电 (记者 胡健)“秋意浓西山 红叶映国保——2026年崛围(山围)山·龙山红叶季文化活动”15日在山西太原净因寺广场启动…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-15/10714990.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网银川10月15日电 (记者 杨迪)贝宁时间10月14日，中国(宁夏)第28批援贝宁医疗队在贝宁洛科萨中心医院，成功开展当地首例低龄儿童先天性外耳道肿物摘除术。医疗队耳鼻喉科医生邓斌精准完成高难度微创手术，填补当地儿童外耳道精细外科手术空白。" data-title="中国援贝宁医疗队完成洛科萨地区首例低龄儿童先天性外耳道肿物摘除术" data-date="10-15 14:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-15 14:21</span>
          <span class="news-item-title">中国援贝宁医疗队完成洛科萨地区首例低龄儿童先天性外耳道肿物摘除术</span>
          <span class="news-value-point">💡 中新网银川10月15日电 (记者 杨迪)贝宁时间10月14日，中国(宁夏)第28批援贝宁医疗队在贝宁洛科萨中心医院，成功开展当地首例低龄儿童先天…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/013/370.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 15 日消息，ATK 现已启动宝可梦 IP 皮卡丘款外设的预售。此次新品包括联名的 RS7 Air 磁轴键盘、烈空 F1 V3 Ultimate+ 鼠标、鼠标垫，单品到手价分别为 399 元、369 元、69 元，套装到手价则是 799 元。皮卡丘联名 RS7 Air 磁轴键盘采用 75% 配列，搭载冰刃磁轴，支持 8kHz 轮询率、32kHz 全键扫描率、256kHz 全键扫描率，传输延迟 0.08ms、全链路响应延迟 0.28ms，支持 0.001mm 的 Rapid Trigger 精度。皮卡丘联名烈空 F1 V3 Ultimate+ 鼠标采用中小手模具，搭载 Nordic nRF54LM20 + 原相 PAW3955 + 欧姆龙光学微动、TTC 金轮编码器的硬件组" data-title="ATK 宝可梦联名皮卡丘款外设预售，键鼠垫三件套到手价 799 元" data-date="10-15 14:19" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-15 14:19</span>
          <span class="news-item-title">ATK 宝可梦联名皮卡丘款外设预售，键鼠垫三件套到手价 799 元</span>
          <span class="news-value-point">💡 IT之家 10 月 15 日消息，ATK 现已启动宝可梦 IP 皮卡丘款外设的预售</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/013/362.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="苹果今日宣布推出 AirPods 5，支持主动降噪，国行定价 999 元起。京东 PLUS 目前可领 100、125 元加补券，10 月 20 日可用，券后仅需 889 元起：点此领券。如果等不及 20 日，或不是 PLUS 会员，京东目前不定时发放 60 元加补券：点此领券。京东 11.11 红包至高 26888 元无门槛可用，每天可抽一次：点此抽取。京东目前支持部分地区政府补贴（收货地址在江苏、吉林、河北、云南、北京、大连），叠加 60 元加补券后，仅需 789.9 元即可入手。如果在 20 日叠加百元 PLUS 券，国补后预计仅需 758 元破冰新低：京东 Apple AirPods 5 支持主动降噪限地区国补直达链接京东 Apple AirPods 5 搭配无线充电盒 增强续航限地区" data-title="苹果 AirPods 5 耳机京东 PLUS 加补 100 元：限地区国补后预计仅需 758 元新低" data-date="10-15 14:16" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-15 14:16</span>
          <span class="news-item-title">苹果 AirPods 5 耳机京东 PLUS 加补 100 元：限地区国补后预计仅需 758 元新低</span>
          <span class="news-value-point">💡 苹果今日宣布推出 AirPods 5，支持主动降噪，国行定价 999 元起</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/ckp8gd38100ro/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="一些人正以小剂量方式使用“胰妥赞”、“周纤达”等GLP-1类药物。使用者表示，这种方法既能帮助减重，又能减少副作用和节省开支。不过，专家指出，目前几乎没研究证据支持这种做法，而且可能存在危险。" data-title="减肥针“微剂量”用药渐成风潮：注射少量真的安全吗？" data-date="10-15 14:09" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-15 14:09</span>
          <span class="news-item-title">减肥针“微剂量”用药渐成风潮：注射少量真的安全吗？</span>
          <span class="news-value-point">💡 一些人正以小剂量方式使用“胰妥赞”、“周纤达”等GLP-1类药物</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-15/10714975.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="几个月前，深圳摩友在昆仑山深处迷路，深夜叩开牧民家门，得到雪中送炭的帮助。脱险后摩友写下感谢信，发出“来深圳看海”的邀约。如今牧民带上妈妈炸的包尔萨克、酸奶疙瘩、毡帽围巾，装满一箱子家乡心意，跨越五千公里奔赴南海之滨。一场昆仑山到深圳湾的双向奔赴，温暖启程。" data-title="从昆仑山到深圳湾的双向奔赴丨带着一箱高原心意 去赴一场看海的约定" data-date="10-15 13:58" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-15 13:58</span>
          <span class="news-item-title">从昆仑山到深圳湾的双向奔赴丨带着一箱高原心意 去赴一场看海的约定</span>
          <span class="news-value-point">💡 几个月前，深圳摩友在昆仑山深处迷路，深夜叩开牧民家门，得到雪中送炭的帮助</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-15/10714953.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网大同10月15日电 (记者 胡健)“根据抽样调查，来大同游客平均停留天数从1.2天逐年提升至如今的3.3天，这标志着大同文旅正从‘过境观光’加速向‘深度体验’转变。”山西省大同市文化和旅游局局长安玉坤如是说。" data-title="大同“十五五”文旅路线图出炉：从“过境观光”转向“深度体验”" data-date="10-15 13:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-15 13:53</span>
          <span class="news-item-title">大同“十五五”文旅路线图出炉：从“过境观光”转向“深度体验”</span>
          <span class="news-value-point">💡 中新网大同10月15日电 (记者 胡健)“根据抽样调查，来大同游客平均停留天数从1.2天逐年提升至如今的3.3天，这标志着大同文旅正从‘过境观光…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-15/10714952.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网长春10月15日电 (记者 郭佳)受一轮寒潮影响，吉林省多地气温骤降，白城市、延边州、长白山保护开发区15日开栓供热，辽源市、四平市也计划提前启动供暖。" data-title="寒潮来袭 吉林多地开栓供热" data-date="10-15 13:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-15 13:52</span>
          <span class="news-item-title">寒潮来袭 吉林多地开栓供热</span>
          <span class="news-value-point">💡 中新网长春10月15日电 (记者 郭佳)受一轮寒潮影响，吉林省多地气温骤降，白城市、延边州、长白山保护开发区15日开栓供热，辽源市、四平市也计划…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-15/10714961.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网绵阳10月15日电(陈选斌)“忆西游主题公园就是一颗榴莲果，喜欢的人爱不释手，不喜欢的人就觉得它是臭的。”四川绵阳忆西游主题公园创建者贺昌林这句形容自己心血之作的话，如今已成为网络热梗，更成了不少游客来打卡时的“接头暗号”。近日，这座由贺昌林耗时16年“手搓”打造的西游主题公园在社交平台走红，造型抽象的雕塑连同背后的建造故事，吸引各地游客实地探访。" data-title="四川一西游主题公园因抽象画风走红 “榴莲果”成游客打卡暗号" data-date="10-15 13:51" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-15 13:51</span>
          <span class="news-item-title">四川一西游主题公园因抽象画风走红 “榴莲果”成游客打卡暗号</span>
          <span class="news-value-point">💡 中新网绵阳10月15日电(陈选斌)“忆西游主题公园就是一颗榴莲果，喜欢的人爱不释手，不喜欢的人就觉得它是臭的</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c674pq1e0dxqo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="尼泊尔能否促成这两个区域大国携手应对喜马拉雅山脉共同面临的气候威胁？" data-title="中国和印度不算老友，尼泊尔想团吉他们应对气候威胁" data-date="10-15 13:50" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-15 13:50</span>
          <span class="news-item-title">中国和印度不算老友，尼泊尔想团吉他们应对气候威胁</span>
          <span class="news-value-point">💡 尼泊尔能否促成这两个区域大国携手应对喜马拉雅山脉共同面临的气候威胁</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-15/10714943.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网临沧10月15日电 (记者 缪超)记者15日从云南省临沧市永德县政府新闻办公室获悉，云南永德大雪山国家级自然保护区管护局联合科研团队近日开展综合科学考察，累计发现1个中国大陆新记录种和4个临沧市新记录种，并探明两种国家二级保护苔藓植物在保护区内多处稳定分布，进一步丰富保护区生物多样性本底资源名录。" data-title="云南临沧发现中国大陆苔藓新记录种" data-date="10-15 13:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-15 13:42</span>
          <span class="news-item-title">云南临沧发现中国大陆苔藓新记录种</span>
          <span class="news-value-point">💡 中新网临沧10月15日电 (记者 缪超)记者15日从云南省临沧市永德县政府新闻办公室获悉，云南永德大雪山国家级自然保护区管护局联合科研团队近日开…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-15/10714915.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社北京10月15日电 综合消息：当地时间14日至15日凌晨，也门胡塞武装与沙特阿拉伯方面继续发生军事对抗。胡塞武装宣称使用地对空导弹击中一架沙特“台风”战斗机，并于此前袭击沙特机场和石油设施。与此同时，也门政府军与胡塞武装在塔伊兹省多地持续交战。" data-title="胡塞武装与沙特相互袭击 也门多地战事持续" data-date="10-15 13:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-15 13:15</span>
          <span class="news-item-title">胡塞武装与沙特相互袭击 也门多地战事持续</span>
          <span class="news-value-point">💡 中新社北京10月15日电 综合消息：当地时间14日至15日凌晨，也门胡塞武装与沙特阿拉伯方面继续发生军事对抗</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/14/us/politics/trump-press-secretary-katie-zacharia-lawyer.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="凯蒂·扎卡里亚（ Katie Zacharia ）告诉《纽约时报》，对她的法律凭据的困惑是一个巨大误解的结果。" data-title="Katie Zacharia Is Trump’s New Press Secretary. But Is She a Lawyer?" data-date="10-15 13:12" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-15 13:12</span>
          <span class="news-item-title">Katie Zacharia是特朗普的新任新闻秘书。但她是律师吗？</span>
          <span class="news-item-title-en">Katie Zacharia Is Trump’s New Press Secretary. But Is She a Lawyer?</span>
          <span class="news-value-point">💡 凯蒂·扎卡里亚（ Katie Zacharia ）告诉《纽约时报》，对她的法律凭据的困惑是一个巨大误解的结果</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/14/figma-announces-new-features-to-define-how-agents-work-on-its-platform/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Figma还在公开测试版中发布其代码层功能。" data-title="Figma announces new features to define how agents work on its platform" data-date="10-15 12:30" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-15 12:30</span>
          <span class="news-item-title">Figma宣布推出新功能，以定义客服代表在其平台上的工作方式</span>
          <span class="news-item-title-en">Figma announces new features to define how agents work on its platform</span>
          <span class="news-value-point">💡 Figma还在公开测试版中发布其代码层功能</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-15 14:36（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
