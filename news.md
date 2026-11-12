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
      <span>2026-11-12 16:54 抓取更新</span>
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
        <span class="channel-count">61</span>
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
        <span class="channel-count">1</span>
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
  <div class="ov-item"><span class="ov-num">61</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">10</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×23 · 天空体育×12</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/11-12/10730921.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="【学习贯彻党的二十届五中全会精神】" data-title="深刻理解和把握持之以恒推进全面从严治党的重大原则" data-date="11-12 16:47" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 11-12 16:47</span>
      </div>
      <h2 class="hero-featured-title">深刻理解和把握持之以恒推进全面从严治党的重大原则</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/026/145.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 12 日消息，Sharp（夏普）当地时间今日宣布，以 222 亿日元（IT之家注：现汇率约合 9.31 亿元人民币）的价格向日东电工 (Nitto) 出售其位于日本三重县津市的久居彩色滤光片工厂，进一步推进其轻资产化策略。IT之家了解到，久居工厂是夏普龟山第二 LCD 显示面板工厂的配套项目，而龟山第二工厂已于上月停产，久居工厂也随之停产。夏普计划在年内敲定龟山第二工厂的处理方案。另一方面，日东电工正加速培育自身半导体业务，计划在久居工厂推进基于自有成膜技术的薄型基板的商业化。" data-title="夏普以 222 亿日元向日东电工出售久居彩色滤光片工厂，进一步瘦身" data-date="11-12 16:26" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">夏普以 222 亿日元向日东电工出售久居彩色滤光片工厂，进一步瘦身</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/gj/2026/11-12/10730891.shtml" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="中新网11月12日电 据路透社报道，美国足协11日告知球员，出于安全方面的担忧，该协会已决定让本国U17男足退出在卡塔尔举行的U17男足世界杯。" data-title="因安全担忧 美国男足宣布退赛" data-date="11-12 16:23" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">因安全担忧 美国男足宣布退赛</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/sh/2026/11-12/10730851.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社安徽黄山11月12日电 (江婉琪)2026RCEP世界遗产地文旅交流推广大会12日在安徽黄山举行。来自印度尼西亚等国家的遗产主管部门代表，以及15个国家的相关遗产地和文旅机构代表参会。" data-title="中外嘉宾齐聚黄山 共推RCEP世界遗产地文旅深度融合" data-date="11-12 16:44" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">中外嘉宾齐聚黄山 共推RCEP世界遗产地文旅深度融合</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-12/10730921.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="【学习贯彻党的二十届五中全会精神】" data-title="深刻理解和把握持之以恒推进全面从严治党的重大原则" data-date="11-12 16:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-12 16:47</span>
          <span class="news-item-title">深刻理解和把握持之以恒推进全面从严治党的重大原则</span>
          <span class="news-value-point">💡 【学习贯彻党的二十届五中全会精神】</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-12/10730919.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="央广网白银11月10日消息(记者魏晋雪 寇刚 见习记者安娜)11月10日，“红星照耀中国·三军会师启新程”网络主题宣传媒体采访团走进甘肃省会宁县红军会宁会师旧址，整座旧址庄严肃穆，浓郁厚重的红色底蕴扑面而来。" data-title="红星照耀中国丨会师塔下，山河有回响" data-date="11-12 16:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-12 16:42</span>
          <span class="news-item-title">红星照耀中国丨会师塔下，山河有回响</span>
          <span class="news-value-point">💡 央广网白银11月10日消息(记者魏晋雪 寇刚 见习记者安娜)11月10日，“红星照耀中国·三军会师启新程”网络主题宣传媒体采访团走进甘肃省会宁县…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-12/10730917.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="五中全会精神在基层丨特写：“小饭碗”装着“大民生”" data-title="特写：“小饭碗”装着“大民生”" data-date="11-12 16:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-12 16:39</span>
          <span class="news-item-title">特写：“小饭碗”装着“大民生”</span>
          <span class="news-value-point">💡 五中全会精神在基层丨特写：“小饭碗”装着“大民生”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-12/10730911.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="2026年美国中期选举在11月3日投票。广告监测机构AdImpact统计，截至11月2日，本周期政治广告支出达到118.7亿美元，超过2024年总统选举周期的112亿美元，广告开支由此创下新纪录。统计范围包括联邦和州级选举广告，竞选人员薪酬、基层组织建设和民调等费用不在其中。" data-title="美国有史以来最贵的中期选举" data-date="11-12 16:38" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-12 16:38</span>
          <span class="news-item-title">美国有史以来最贵的中期选举</span>
          <span class="news-value-point">💡 2026年美国中期选举在11月3日投票</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-12/10730914.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="95岁的美国老人柏大卫，在青海湟源度过了童年和少年时光。18岁离开，阔别38年后重返湟源，此后又一次次跨越重洋，为当地筹赠医疗设备、支持教育。他始终认定：“一个人一生只能有一个故乡，我的故乡就是湟源。”" data-title="记者手记：关于柏大卫故事的十个细节" data-date="11-12 16:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-12 16:35</span>
          <span class="news-item-title">记者手记：关于柏大卫故事的十个细节</span>
          <span class="news-value-point">💡 95岁的美国老人柏大卫，在青海湟源度过了童年和少年时光</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-12/10730913.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中国新闻周刊记者：郑立颖" data-title="桑德罗·马科斯的腐败风波" data-date="11-12 16:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-12 16:35</span>
          <span class="news-item-title">桑德罗·马科斯的腐败风波</span>
          <span class="news-value-point">💡 中国新闻周刊记者：郑立颖</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-12/10730844.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社广州11月12日电 (记者 程景伟)《纪念孙中山先生诞辰160周年》纪念邮票首发仪式12日在广州中山纪念堂园区举行。" data-title="《纪念孙中山先生诞辰160周年》纪念邮票首发" data-date="11-12 16:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-12 16:26</span>
          <span class="news-item-title">《纪念孙中山先生诞辰160周年》纪念邮票首发</span>
          <span class="news-value-point">💡 中新社广州11月12日电 (记者 程景伟)《纪念孙中山先生诞辰160周年》纪念邮票首发仪式12日在广州中山纪念堂园区举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-12/10730867.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月12日电 据人社部网站消息，国务院任免国家工作人员。" data-title="国务院任免国家工作人员" data-date="11-12 16:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-12 16:17</span>
          <span class="news-item-title">国务院任免国家工作人员</span>
          <span class="news-value-point">💡 中新网11月12日电 据人社部网站消息，国务院任免国家工作人员</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-12/10730854.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="视频：IUCN副总干事点赞中国：江苏除草2万公顷，给濒危候鸟留滩涂｜新闻会客厅来源：中国新闻网" data-title="19处世界遗产、34处IUCN绿色名录保护地，拿下两个全球第一，中国为什么能？ | 新闻会客厅" data-date="11-12 16:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-12 16:15</span>
          <span class="news-item-title">19处世界遗产、34处IUCN绿色名录保护地，拿下两个全球第一，中国为什么能？ | 新闻会客厅</span>
          <span class="news-value-point">💡 视频：IUCN副总干事点赞中国：江苏除草2万公顷，给濒危候鸟留滩涂｜新闻会客厅来源：中国新闻网</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-12/10730852.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社莫斯科11月12日电 俄罗斯侦查委员会圣彼得堡市侦查总局12日表示，针对圣彼得堡普希金区汽车爆炸致一名军人死亡事件，侦查机关已进行刑事立案，并展开调查。" data-title="俄方对圣彼得堡汽车爆炸致军人死亡案展开刑事调查" data-date="11-12 16:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-12 16:12</span>
          <span class="news-item-title">俄方对圣彼得堡汽车爆炸致军人死亡案展开刑事调查</span>
          <span class="news-value-point">💡 中新社莫斯科11月12日电 俄罗斯侦查委员会圣彼得堡市侦查总局12日表示，针对圣彼得堡普希金区汽车爆炸致一名军人死亡事件，侦查机关已进行刑事立案…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-12/10730841.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月12日电 (记者 张素)12日，中国外交部发言人宣布：经中韩双方商定，韩国外长赵显将于11月13日至14日访华。" data-title="韩国外长赵显将访华 中国外交部介绍有关安排" data-date="11-12 16:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-12 16:02</span>
          <span class="news-item-title">韩国外长赵显将访华 中国外交部介绍有关安排</span>
          <span class="news-value-point">💡 中新网北京11月12日电 (记者 张素)12日，中国外交部发言人宣布：经中韩双方商定，韩国外长赵显将于11月13日至14日访华</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-12/10730848.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京11月12日电#8195;记者12日从中央政法委获悉，为依法从严查处危害食品安全违法犯罪，公安部、最高人民检察院、最高人民法院近日对18起涉食品安全重大犯罪案件集中挂牌督办，其中包括“甲醛白菜”案、“假洋保健品”案、“硫磺竹笋”案等案件。" data-title="18起涉食品安全重大犯罪案件被挂牌督办" data-date="11-12 16:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-12 16:01</span>
          <span class="news-item-title">18起涉食品安全重大犯罪案件被挂牌督办</span>
          <span class="news-value-point">💡 新华社北京11月12日电#8195;记者12日从中央政法委获悉，为依法从严查处危害食品安全违法犯罪，公安部、最高人民检察院、最高人民法院近日对1…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-12/10730812.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社雅加达11月12日电(记者 李志全)印度尼西亚副总统吉布兰12日向该国人民协商会议正式递交辞职信。印尼人民协商会议主席穆扎尼表示，该机构领导层将召开会议，讨论辞职信的后续处理事宜。" data-title="印尼副总统吉布兰正式递交辞职信" data-date="11-12 15:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-12 15:34</span>
          <span class="news-item-title">印尼副总统吉布兰正式递交辞职信</span>
          <span class="news-value-point">💡 中新社雅加达11月12日电(记者 李志全)印度尼西亚副总统吉布兰12日向该国人民协商会议正式递交辞职信</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/11/us/elections/mississippi-senate-colom-hyde-smith.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="检察官科洛姆先生将成为自南北战争后的重建时期以来密西西比州首位当选的黑人参议员。" data-title="Scott Colom, a Democrat, Wins Mississippi Senate Election" data-date="11-12 15:12" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-12 15:12</span>
          <span class="news-item-title">民主党人斯科特·科洛姆赢得密西西比州参议院选举</span>
          <span class="news-item-title-en">Scott Colom, a Democrat, Wins Mississippi Senate Election</span>
          <span class="news-value-point">💡 检察官科洛姆先生将成为自南北战争后的重建时期以来密西西比州首位当选的黑人参议员</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-12/10730803.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月12日电 日本高市政府推进“再军事化”的动作不断。近日，日本执政党自民党及其执政伙伴日本维新会讨论修订“安保三文件”的相关动向，引发日本舆论广泛担忧和批评。日本各界纷纷发声，要求日本政府坚持“无核三原则”。" data-title="日本被曝拟松动“无核三原则” 日本民众抗议：决不允许" data-date="11-12 15:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-12 15:09</span>
          <span class="news-item-title">日本被曝拟松动“无核三原则” 日本民众抗议：决不允许</span>
          <span class="news-value-point">💡 中新网11月12日电 日本高市政府推进“再军事化”的动作不断</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/026/145.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 12 日消息，Sharp（夏普）当地时间今日宣布，以 222 亿日元（IT之家注：现汇率约合 9.31 亿元人民币）的价格向日东电工 (Nitto) 出售其位于日本三重县津市的久居彩色滤光片工厂，进一步推进其轻资产化策略。IT之家了解到，久居工厂是夏普龟山第二 LCD 显示面板工厂的配套项目，而龟山第二工厂已于上月停产，久居工厂也随之停产。夏普计划在年内敲定龟山第二工厂的处理方案。另一方面，日东电工正加速培育自身半导体业务，计划在久居工厂推进基于自有成膜技术的薄型基板的商业化。" data-title="夏普以 222 亿日元向日东电工出售久居彩色滤光片工厂，进一步瘦身" data-date="11-12 16:26" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-12 16:26</span>
          <span class="news-item-title">夏普以 222 亿日元向日东电工出售久居彩色滤光片工厂，进一步瘦身</span>
          <span class="news-value-point">💡 IT之家 11 月 12 日消息，Sharp（夏普）当地时间今日宣布，以 222 亿日元（IT之家注：现汇率约合 9.31 亿元人民币）的价格向…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/026/125.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 12 日消息，据共同社昨天报道，日本政府正考虑要求 AI 企业履行安全保障义务，并新增处罚措施应对前沿 AI 的失控风险。IT之家从原报道获悉，日本政府计划今年年底前公布制度改革整体方案，相关内容已在某个讨论 AI 法律制度的非公开工作组会议中得到确认。此举旨在应对 AI 网络攻击、失控等重大威胁，确保政府能对拒绝协商的恶意企业采取应对措施。目前 AI 企业的业务分工日益细化，包含基础研究、基础模型研发及用户服务等多个环节。未来日本政府将进一步讨论监管对象范围。如果将美国 AI 大模型公司也纳入监管，如何切实保护日本用户权益，也将成为亟待解决的问题。对于发生问题后仍拒绝配合协商的企业，日本政府计划在必要时发布强制执行命令，并考虑对违抗命令的企业实施处罚，这些措施预计将主要" data-title="日本政府考虑对前沿 AI 失控行为设立处罚措施，拟修订法律应对拒不配合的恶意企业" data-date="11-12 16:09" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-12 16:09</span>
          <span class="news-item-title">日本政府考虑对前沿 AI 失控行为设立处罚措施，拟修订法律应对拒不配合的恶意企业</span>
          <span class="news-value-point">💡 IT之家 11 月 12 日消息，据共同社昨天报道，日本政府正考虑要求 AI 企业履行安全保障义务，并新增处罚措施应对前沿 AI 的失控风险</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/11/technology/nvidia-jensen-huang.html" target="_blank" rel="noopener" data-cat="keji" data-summary="黄先生因与一名据称是中国间谍的女性有染，以及与他的人工智能芯片公司的一名高管有不正当关系而受到审查。" data-title="Nvidia’s Board Is Weighing Jensen Huang’s Future" data-date="11-12 13:53" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-12 13:53</span>
          <span class="news-item-title">英伟达董事会正在权衡黄仁勋的未来</span>
          <span class="news-item-title-en">Nvidia’s Board Is Weighing Jensen Huang’s Future</span>
          <span class="news-value-point">💡 黄先生因与一名据称是中国间谍的女性有染，以及与他的人工智能芯片公司的一名高管有不正当关系而受到审查</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c63egjy85wq8o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="随着第二宗婚外情的报导曝光，Nvidia股价大幅下跌。据报董事会正与一家外部公司合作，寻找黄仁勋的潜在继任者。" data-title="黄仁勋疑涉另一宗婚外情，Nvidia董事会传拟撤换执行长" data-date="11-12 13:20" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-12 13:20</span>
          <span class="news-item-title">黄仁勋疑涉另一宗婚外情，Nvidia董事会传拟撤换执行长</span>
          <span class="news-value-point">💡 随着第二宗婚外情的报导曝光，Nvidia股价大幅下跌</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/article/nvidia-investigation-jensen-huang.html" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达董事会正在权衡该公司首席执行官黄仁勋的未来，他承认与一名据美国情报部门称曾为中国从事间谍活动的女性有染。" data-title="What to Know About Nvidia’s Investigation of CEO Jensen Huang" data-date="11-12 11:55" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-12 11:55</span>
          <span class="news-item-title">关于英伟达对首席执行官黄仁勋的调查，您需要了解什么？</span>
          <span class="news-item-title-en">What to Know About Nvidia’s Investigation of CEO Jensen Huang</span>
          <span class="news-value-point">💡 英伟达董事会正在权衡该公司首席执行官黄仁勋的未来，他承认与一名据美国情报部门称曾为中国从事间谍活动的女性有染</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/11/who-could-replace-jensen-huang-a-highly-unscientific-list-of-possible-successors/" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达没有继任计划，而且首席执行官正深陷困境，因此我们拟定了一份候选人名单。" data-title="Who could replace Jensen Huang? A highly unscientific list of possible successors" data-date="11-12 11:13" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-12 11:13</span>
          <span class="news-item-title">谁能接替黄仁勋？一份极不科学的可能继任者名单</span>
          <span class="news-item-title-en">Who could replace Jensen Huang? A highly unscientific list of possible successors</span>
          <span class="news-value-point">💡 英伟达没有继任计划，而且首席执行官正深陷困境，因此我们拟定了一份候选人名单</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/11/business/nvidia-stock-jensen-huang-ceo.html" target="_blank" rel="noopener" data-cat="keji" data-summary="有关董事会讨论Jensen Huang去留的消息导致英伟达的股价在盘后交易中下跌了8%以上。" data-title="Nvidia’s Stock Price Plummets as Board Is Said to Consider Jensen Huang’s Future as CEO" data-date="11-12 10:40" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-12 10:40</span>
          <span class="news-item-title">据称董事会正在考虑黄仁勋的首席执行官未来，Nvidia股价暴跌</span>
          <span class="news-item-title-en">Nvidia’s Stock Price Plummets as Board Is Said to Consider Jensen Huang’s Future as CEO</span>
          <span class="news-value-point">💡 有关董事会讨论Jensen Huang去留的消息导致英伟达的股价在盘后交易中下跌了8%以上</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/11/technology/jensen-huang-nvidia-affair.html" target="_blank" rel="noopener" data-cat="keji" data-summary="Nvidia的首席执行官黄先生正因与一位中国女商人的婚外情而受到审查，美国情报部门认定该女子是一名中国间谍。" data-title="Jensen Huang Said to Have Had Relationship With Nvidia Executive Who Reports to Him" data-date="11-12 09:57" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-12 09:57</span>
          <span class="news-item-title">据称黄仁勋与向他汇报工作的英伟达高管存在不正当关系</span>
          <span class="news-item-title-en">Jensen Huang Said to Have Had Relationship With Nvidia Executive Who Reports to Him</span>
          <span class="news-value-point">💡 Nvidia的首席执行官黄先生正因与一位中国女商人的婚外情而受到审查，美国情报部门认定该女子是一名中国间谍</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/509281.html" target="_blank" rel="noopener" data-cat="keji" data-summary="跨境称重量方等场景完成PMF验证并出现客户复购，新一代构型机器人计划12月底发布" data-title="“双十一”机器人在物流仓“埋头苦干”：昆腾动力开启具身智能规模化获客与交付阶段" data-date="11-12 09:45" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-12 09:45</span>
          <span class="news-item-title">“双十一”机器人在物流仓“埋头苦干”：昆腾动力开启具身智能规模化获客与交付阶段</span>
          <span class="news-value-point">💡 跨境称重量方等场景完成PMF验证并出现客户复购，新一代构型机器人计划12月底发布</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/11/nvidia-ceo-jensen-huangs-affair-with-alleged-chinese-spy-a-timeline/" target="_blank" rel="noopener" data-cat="keji" data-summary="随着美国和中国竞相开发最先进的人工智能基础设施，这一事件可能会对国家安全产生影响。" data-title="The unfolding Jensen Huang scandal: a timeline" data-date="11-12 07:50" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-12 07:50</span>
          <span class="news-item-title">正在发酵的黄仁勋丑闻：时间线</span>
          <span class="news-item-title-en">The unfolding Jensen Huang scandal: a timeline</span>
          <span class="news-value-point">💡 随着美国和中国竞相开发最先进的人工智能基础设施，这一事件可能会对国家安全产生影响</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/nvidias-board-reportedly-preparing-to-oust-ceo-jensen-huang-as-second-extra-marital-affair-emerges-stock-has-plunged-20-percent-since-scandals-began-huang-has-been-first-and-only-ceo-for-33-years" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道，英伟达董事会正着手罢免黄仁勋，原因是该公司因近期丑闻和缺乏继任计划而导致股价暴跌。" data-title="Nvidia’s Board reportedly preparing to oust CEO Jensen Huang as second extra-marital affair emerges" data-date="11-12 07:45" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-12 07:45</span>
          <span class="news-item-title">据报道，Nvidia董事会正准备罢免首席执行官黄仁勋，原因是其第二起婚外情曝光。</span>
          <span class="news-item-title-en">Nvidia’s Board reportedly preparing to oust CEO Jensen Huang as second extra-marital affair emerges</span>
          <span class="news-value-point">💡 据报道，英伟达董事会正着手罢免黄仁勋，原因是该公司因近期丑闻和缺乏继任计划而导致股价暴跌</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/11/nvidias-stock-drops-as-board-reportedly-preps-to-oust-ceo-jensen-huang/" target="_blank" rel="noopener" data-cat="keji" data-summary="最早在周三晚上，英伟达董事会就可能决定罢免其已任职33年的创始人兼首席执行官。" data-title="Nvidia’s stock drops as board reportedly preps to oust CEO Jensen Huang" data-date="11-12 07:28" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-12 07:28</span>
          <span class="news-item-title">据报道，英伟达董事会正准备罢免首席执行官黄仁勋，该公司股价应声下跌</span>
          <span class="news-item-title-en">Nvidia’s stock drops as board reportedly preps to oust CEO Jensen Huang</span>
          <span class="news-value-point">💡 最早在周三晚上，英伟达董事会就可能决定罢免其已任职33年的创始人兼首席执行官</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/11/jensen-huang-accused-of-having-another-affair-with-a-nvidia-exec/" target="_blank" rel="noopener" data-cat="keji" data-summary="Jensen Huang 承认与一名被指控为中国情报人员的女性有染，因此饱受抨击，如今又被指控与一名 Nvidia 的下属有另一段婚外情。" data-title="Jensen Huang accused of having another affair" data-date="11-12 07:17" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-12 07:17</span>
          <span class="news-item-title">Jensen Huang被指控有另一段婚外情</span>
          <span class="news-item-title-en">Jensen Huang accused of having another affair</span>
          <span class="news-value-point">💡 Jensen Huang 承认与一名被指控为中国情报人员的女性有染，因此饱受抨击，如今又被指控与一名 Nvidia 的下属有另一段婚外情</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1031652/jensen-huang-rumor" target="_blank" rel="noopener" data-cat="keji" data-summary="据《华尔街日报》报道，在《纽约时报》报道了有关黄仁勋涉嫌第二次婚外情的文章仅几天后，Nvidia的董事会正准备解雇首席执行官黄仁勋。此前，他曾承认与一名据称是中国间谍的女性有婚外情。" data-title="Nvidia is reportedly preparing to fire Jensen Huang" data-date="11-12 06:44" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-12 06:44</span>
          <span class="news-item-title">据报道，英伟达正准备解雇黄仁勋</span>
          <span class="news-item-title-en">Nvidia is reportedly preparing to fire Jensen Huang</span>
          <span class="news-value-point">💡 据《华尔街日报》报道，在《纽约时报》报道了有关黄仁勋涉嫌第二次婚外情的文章仅几天后，Nvidia的董事会正准备解雇首席执行官黄仁勋</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/jensen-huang-now-accused-of-affair-with-nvidia-executive-who-reported-to-him-alleged-cover-up-attempt-new-indiscretion-comes-in-wake-of-admitted-affair-with-alleged-chinese-spy" target="_blank" rel="noopener" data-cat="keji" data-summary="据报道，英伟达首席执行官黄仁勋与一名直接下属有婚外情，此前他还与一名疑似中国间谍的女性有婚外情。" data-title="Jensen Huang now accused of affair with Nvidia executive who reported to him, alleged cover" data-date="11-12 06:31" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-12 06:31</span>
          <span class="news-item-title">Jensen Huang现被指控与向他汇报工作的Nvidia高管有染，并涉嫌掩盖此事</span>
          <span class="news-item-title-en">Jensen Huang now accused of affair with Nvidia executive who reported to him, alleged cover</span>
          <span class="news-value-point">💡 据报道，英伟达首席执行官黄仁勋与一名直接下属有婚外情，此前他还与一名疑似中国间谍的女性有婚外情</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-12/10730891.shtml" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="中新网11月12日电 据路透社报道，美国足协11日告知球员，出于安全方面的担忧，该协会已决定让本国U17男足退出在卡塔尔举行的U17男足世界杯。" data-title="因安全担忧 美国男足宣布退赛" data-date="11-12 16:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-12 16:23</span>
          <span class="news-item-title">因安全担忧 美国男足宣布退赛</span>
          <span class="news-value-point">💡 中新网11月12日电 据路透社报道，美国足协11日告知球员，出于安全方面的担忧，该协会已决定让本国U17男足退出在卡塔尔举行的U17男足世界杯</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/rugby-league/news/12040/13610091/australia-vs-new-zealand-age-old-rivalry-bookends-rugby-league-world-cup-but-will-it-end-18-years-of-supremacy" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="一场由来已久的宿敌对决将为2026年橄榄球世界杯画上句号，这是橄榄球运动在全球范围内蓬勃发展的最新标志，但归根结底，挑战者仍只是挑战者，夺冠热门仍只是夺冠热门。" data-title="Age-old rivalry bookends RLWC but will it end 18 years of supremacy?" data-date="11-12 15:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-12 15:00</span>
          <span class="news-item-title">古老的宿敌之争为橄榄球世界杯画上句号，但它能否终结18年的霸主地位？</span>
          <span class="news-item-title-en">Age-old rivalry bookends RLWC but will it end 18 years of supremacy?</span>
          <span class="news-value-point">💡 一场由来已久的宿敌对决将为2026年橄榄球世界杯画上句号，这是橄榄球运动在全球范围内蓬勃发展的最新标志，但归根结底，挑战者仍只是挑战者，夺冠热门…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/racing/news/12040/13610641/today-on-sky-sports-racing-hereford-hosts-six-race-card" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="周二的赫里福德六场赛事，敬请收看天空体育赛马频道（Sky Sports Racing）的直播。" data-title="Hereford hosts six" data-date="11-12 14:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-12 14:00</span>
          <span class="news-item-title">赫里福德有六家</span>
          <span class="news-item-title-en">Hereford hosts six</span>
          <span class="news-value-point">💡 周二的赫里福德六场赛事，敬请收看天空体育赛马频道（Sky Sports Racing）的直播</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13611250/smith-is-one-of-the-best-in-the-world-who-can-we-expect-to-see-at-pl-of-darts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Matt Porter向飞镖迷们介绍了新赛季飞镖超级联赛的参赛选手阵容。" data-title="PDC chief reveals who we might see at Premier League Darts in 2027" data-date="11-12 06:47" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-12 06:47</span>
          <span class="news-item-title">PDC主席透露2027年英超飞镖赛可能有哪些选手参赛</span>
          <span class="news-item-title-en">PDC chief reveals who we might see at Premier League Darts in 2027</span>
          <span class="news-value-point">💡 Matt Porter向飞镖迷们介绍了新赛季飞镖超级联赛的参赛选手阵容</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/11/mauricio-pochettino-manchester-united-old-trafford-manager" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="这位主教练在豪门俱乐部的经历让他备受打击，但老特拉福德的几名球员可能适合他的踢球风格。欢迎毛里西奥来到这片绞肉场。或者更确切地说，欢迎回来。我们一直在等你。曼联的新闻中没有什么令人意外之处。" data-title="Meeting of two lost souls: can Pochettino make it work at Manchester United? | Barney Ronay" data-date="11-12 05:10" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-12 05:10</span>
          <span class="news-item-title">两个迷失灵魂的相遇：波切蒂诺能在曼联成功吗？| 巴尼·罗内</span>
          <span class="news-item-title-en">Meeting of two lost souls: can Pochettino make it work at Manchester United? | Barney Ronay</span>
          <span class="news-value-point">💡 这位主教练在豪门俱乐部的经历让他备受打击，但老特拉福德的几名球员可能适合他的踢球风格</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/12476234/transfer-centre-live-football-transfer-news-updates-and-rumours" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Transfer Centre LIVE! &#39;USA to target Guardiola as Pochettino replacement&#39;" data-title="Transfer Centre LIVE! &#39;USA to target Guardiola as Pochettino replacement&#39;" data-date="11-12 03:33" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-12 03:33</span>
          <span class="news-item-title">转会中心直播！“美国队将瞄准瓜迪奥拉作为波切蒂诺的替代者”</span>
          <span class="news-item-title-en">Transfer Centre LIVE! 'USA to target Guardiola as Pochettino replacement'</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13610949/mauricio-pochettino-man-utd-strike-agreement-with-michael-carricks-potential-successor" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联已与毛里西奥·波切蒂诺（Mauricio Pochettino）就其担任主教练一事达成原则性口头协议。" data-title="Man Utd strike Pochettino agreement with Carrick set to depart" data-date="11-12 01:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-12 01:00</span>
          <span class="news-item-title">曼联与波切蒂诺达成协议，卡里克即将离任</span>
          <span class="news-item-title-en">Man Utd strike Pochettino agreement with Carrick set to depart</span>
          <span class="news-value-point">💡 曼联已与毛里西奥·波切蒂诺（Mauricio Pochettino）就其担任主教练一事达成原则性口头协议</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13610949/mauricio-pochettino-man-utd-strike-agreement-with-michael-carricks-potential-successor" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联已与毛里西奥·波切蒂诺（Mauricio Pochettino）就其担任主教练一事达成原则性口头协议。" data-title="Man Utd strike Pochettino agreement with Carrick set to depart" data-date="11-12 01:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-12 01:00</span>
          <span class="news-item-title">曼联与波切蒂诺达成协议，卡里克即将离任</span>
          <span class="news-item-title-en">Man Utd strike Pochettino agreement with Carrick set to depart</span>
          <span class="news-value-point">💡 曼联已与毛里西奥·波切蒂诺（Mauricio Pochettino）就其担任主教练一事达成原则性口头协议</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/rugby-union/news/12040/13611181/ellie-kildunne-its-harsh-to-say-england-dropped-me-after-canada-defeat-my-role-just-changed" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英格兰红玫瑰队世界杯冠军埃莉·基尔敦（Ellie Kildunne）表示，说她在球队最近的北美巡回赛中被弃用是“苛刻”的，她声称自己只是被赋予了“不同的角色”。" data-title="Kildunne: It&#39;s &#39;harsh&#39; to say England dropped me - &#39;My role just changed&#39;" data-date="11-12 00:48" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-12 00:48</span>
          <span class="news-item-title">基尔杜恩：说英格兰队放弃了我“太苛刻”了——“我的角色只是发生了变化”</span>
          <span class="news-item-title-en">Kildunne: It's 'harsh' to say England dropped me - 'My role just changed'</span>
          <span class="news-value-point">💡 英格兰红玫瑰队世界杯冠军埃莉·基尔敦（Ellie Kildunne）表示，说她在球队最近的北美巡回赛中被弃用是“苛刻”的，她声称自己只是被赋予了…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqvg25pj36mvo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="毛里西奥·波切蒂诺已准备好接受曼联的邀约，成为球队的下一任主教练。" data-title="Pochettino ready to accept Man Utd offer to replace Carrick" data-date="11-12 00:03" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-12 00:03</span>
          <span class="news-item-title">波切蒂诺准备接受曼联的邀约，接替卡里克</span>
          <span class="news-item-title-en">Pochettino ready to accept Man Utd offer to replace Carrick</span>
          <span class="news-value-point">💡 毛里西奥·波切蒂诺已准备好接受曼联的邀约，成为球队的下一任主教练</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13611018/manchester-utd-latest-five-things-mauricio-pochettino-will-need-to-sort-at-old-trafford" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育的尼克·赖特（Nick Wright）分析了毛里西奥·波切蒂诺（Mauricio Pochettino）如果并一旦接替迈克尔·卡里克（Michael Carrick）担任曼联主教练，将需要解决的五个问题。" data-title="Five things Pochettino will need to sort out at Man Utd" data-date="11-11 21:30" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-11 21:30</span>
          <span class="news-item-title">波切蒂诺在曼联需要解决的五件事</span>
          <span class="news-item-title-en">Five things Pochettino will need to sort out at Man Utd</span>
          <span class="news-value-point">💡 天空体育的尼克·赖特（Nick Wright）分析了毛里西奥·波切蒂诺（Mauricio Pochettino）如果并一旦接替迈克尔·卡里克（M…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cwzd9pvjy426o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="首席足球撰稿人菲尔·麦克纳尔蒂（Phil McNulty）表示，毛里西奥·波切蒂诺（Mauricio Pochettino）似乎即将把与曼联长达十年的“暧昧”关系发展为正式的“恋爱”关系。" data-title="Pochettino a decade in Man Utd&#39;s making - but Carrick deserves better" data-date="11-11 20:58" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-11 20:58</span>
          <span class="news-item-title">波切蒂诺在曼联的十年——但卡里克理应得到更好的待遇</span>
          <span class="news-item-title-en">Pochettino a decade in Man Utd's making - but Carrick deserves better</span>
          <span class="news-value-point">💡 首席足球撰稿人菲尔·麦克纳尔蒂（Phil McNulty）表示，毛里西奥·波切蒂诺（Mauricio Pochettino）似乎即将把与曼联长达…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13611004/mauricio-pochettino-manchester-uniteds-approach-for-former-tottenham-and-chelsea-boss-questioned" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育新闻的卡韦·索尔赫科尔对曼联追求毛里西奥·波切蒂诺的做法提出质疑，认为还有更好的选择。" data-title="Is Pochettino a short-term fix? Man Utd pursuit of Carrick replacement questioned" data-date="11-11 20:44" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-11 20:44</span>
          <span class="news-item-title">波切蒂诺是短期解决方案吗？曼联寻求卡里克替代者受到质疑</span>
          <span class="news-item-title-en">Is Pochettino a short-term fix? Man Utd pursuit of Carrick replacement questioned</span>
          <span class="news-value-point">💡 天空体育新闻的卡韦·索尔赫科尔对曼联追求毛里西奥·波切蒂诺的做法提出质疑，认为还有更好的选择</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/cricket/news/12040/13610871/sandpapergate-nasser-hussain-calls-australia-ball-tampering-scandal-a-complete-mess-after-usman-khawaja-claims" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育的纳瑟·侯赛因（Nasser Hussain）将澳大利亚的“砂纸门”事件及其随后引发的轩然大波称为“一团糟”。" data-title="Hussain calls &#39;Sandpapergate&#39; affair a &#39;complete mess&#39;" data-date="11-11 20:15" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-11 20:15</span>
          <span class="news-item-title">侯赛因称“砂纸门”事件是一团糟</span>
          <span class="news-item-title-en">Hussain calls 'Sandpapergate' affair a 'complete mess'</span>
          <span class="news-value-point">💡 天空体育的纳瑟·侯赛因（Nasser Hussain）将澳大利亚的“砂纸门”事件及其随后引发的轩然大波称为“一团糟”</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cw30e0yz0p04o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="正在进行的国际比赛日让主教练恩佐·马雷斯卡有了亟需的时间来解决曼城队日益增多的问题。" data-title="Assessing the reasons for Man City&#39;s decline in form under Maresca" data-date="11-11 19:47" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-11 19:47</span>
          <span class="news-item-title">评估马雷斯卡执教下曼城状态下滑的原因</span>
          <span class="news-item-title-en">Assessing the reasons for Man City's decline in form under Maresca</span>
          <span class="news-value-point">💡 正在进行的国际比赛日让主教练恩佐·马雷斯卡有了亟需的时间来解决曼城队日益增多的问题</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-12/10730851.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社安徽黄山11月12日电 (江婉琪)2026RCEP世界遗产地文旅交流推广大会12日在安徽黄山举行。来自印度尼西亚等国家的遗产主管部门代表，以及15个国家的相关遗产地和文旅机构代表参会。" data-title="中外嘉宾齐聚黄山 共推RCEP世界遗产地文旅深度融合" data-date="11-12 16:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-12 16:44</span>
          <span class="news-item-title">中外嘉宾齐聚黄山 共推RCEP世界遗产地文旅深度融合</span>
          <span class="news-value-point">💡 中新社安徽黄山11月12日电 (江婉琪)2026RCEP世界遗产地文旅交流推广大会12日在安徽黄山举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-12/10730915.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="近年来，很多地方将一个个曾经拥挤狭窄的露天菜市场，在保留市井烟火、留住老摊主与本土风味的基础上，焕新升级，打造成为集民生保障、文旅休闲于一体的城市新空间。下面我们先去安徽合肥的四湾菜市看看。" data-title="多地老菜市变身新地标 焕新不减烟火气" data-date="11-12 16:37" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-12 16:37</span>
          <span class="news-item-title">多地老菜市变身新地标 焕新不减烟火气</span>
          <span class="news-value-point">💡 近年来，很多地方将一个个曾经拥挤狭窄的露天菜市场，在保留市井烟火、留住老摊主与本土风味的基础上，焕新升级，打造成为集民生保障、文旅休闲于一体的城…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cwr7grvx00yxo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="从失禁到长期疼痛，数以百万计的女性在分娩数十年后仍然饱受后遗症困扰。" data-title="“你甚至不会告诉密友”：分娩后遗症，为何多年后仍挥之不去？" data-date="11-12 16:33" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-12 16:33</span>
          <span class="news-item-title">“你甚至不会告诉密友”：分娩后遗症，为何多年后仍挥之不去？</span>
          <span class="news-value-point">💡 从失禁到长期疼痛，数以百万计的女性在分娩数十年后仍然饱受后遗症困扰</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-12/10730865.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网乌鲁木齐11月12日电 (杨阳 江珊)“一批批援疆专家接力，通过传经验、带队伍，让基层医院的医疗服务能力得到很大提升。相信今后，越来越多病症可在县域内诊治，更多的边疆百姓在家门口就能看好病。”谈及专科联盟的发展，新疆生产建设兵团第一师医院党委副书记、院长马涛近日受访时说。" data-title="浙江省医疗援疆专科联盟7年接力提升边疆基层医疗服务能力" data-date="11-12 16:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-12 16:28</span>
          <span class="news-item-title">浙江省医疗援疆专科联盟7年接力提升边疆基层医疗服务能力</span>
          <span class="news-value-point">💡 中新网乌鲁木齐11月12日电 (杨阳 江珊)“一批批援疆专家接力，通过传经验、带队伍，让基层医院的医疗服务能力得到很大提升</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-12/10730871.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网广州11月12日电 (记者 程景伟)12日，孙中山先生诞辰160周年纪念日当天，《纪念孙中山先生诞辰160周年》纪念邮票首发仪式在广州中山纪念堂园区举行。" data-title="《纪念孙中山先生诞辰160周年》纪念邮票在广州首发" data-date="11-12 16:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-12 16:26</span>
          <span class="news-item-title">《纪念孙中山先生诞辰160周年》纪念邮票在广州首发</span>
          <span class="news-value-point">💡 中新网广州11月12日电 (记者 程景伟)12日，孙中山先生诞辰160周年纪念日当天，《纪念孙中山先生诞辰160周年》纪念邮票首发仪式在广州中山…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-12/10730855.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="为进一步强化医疗机构医疗质量安全监管，有效防范化解执业风险，全面提升辖区医疗机构依法依规执业能力，日前，盐城市亭湖区卫健委、亭湖区疾控中心(卫生监督所)联合盐城市医疗保障基金管理中心亭湖分中心，组织开展专项依法执业专题培训。培训聚焦中医诊所、医疗美容机构重点主体，辖区百余家相关医疗机构参训。" data-title="江苏盐城市亭湖区组织开展医疗机构依法执业专题培训" data-date="11-12 16:23" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-12 16:23</span>
          <span class="news-item-title">江苏盐城市亭湖区组织开展医疗机构依法执业专题培训</span>
          <span class="news-value-point">💡 为进一步强化医疗机构医疗质量安全监管，有效防范化解执业风险，全面提升辖区医疗机构依法依规执业能力，日前，盐城市亭湖区卫健委、亭湖区疾控中心(卫生…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-12/10730887.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="“买两个包子2块钱，路边停车要10块”，这句在上海纠结多年的问题，11月18日起将翻篇。" data-title="“停车费比饭钱还贵”，这事儿终于有说法了" data-date="11-12 16:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-12 16:22</span>
          <span class="news-item-title">“停车费比饭钱还贵”，这事儿终于有说法了</span>
          <span class="news-value-point">💡 “买两个包子2块钱，路边停车要10块”，这句在上海纠结多年的问题，11月18日起将翻篇</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/026/131.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 12 日消息，京东现已公布 2026 年度双十一成交数据，截至 11 月 11 日 23:59，2026 年京东 11.11 共售出超 5000 万件 AI 产品，产生超 3 亿服务订单，第一次参加京东 11.11 的新用户平均下单 6 件商品。京东表示，截至 11 月 11 日 23:59，JoyInside 累计完成超 7000 万次交互，已经成为百万家庭的 AI 伙伴。JoyAI App 日均活跃用户峰值达常态期 5 倍以上。京东 11.11 期间，AI 医生“大为”问诊订单量同比增长超 5 倍。11.11 全周期，AIPC、AI 工作站、AI 相机、AI 眼镜、AI 录音设备等 AI 趋势品成交额同比增长超 100%，“Token”搜索量环比提升超 13 倍，京东" data-title="京东 2026 双十一战报出炉：产生超 3 亿服务订单、超 2000 个家电家居品牌成交额同比增长 100%" data-date="11-12 16:19" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-12 16:19</span>
          <span class="news-item-title">京东 2026 双十一战报出炉：产生超 3 亿服务订单、超 2000 个家电家居品牌成交额同比增长 100%</span>
          <span class="news-value-point">💡 IT之家 11 月 12 日消息，京东现已公布 2026 年度双十一成交数据，截至 11 月 11 日 23:59，2026 年京东 11.11…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/026/128.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 12 日消息，据央视新闻今日从中国海油获悉，我国在渤海中部海域超 5000 米地层钻探获得一口火山岩高产油气井，测试日产天然气约 80 万立方米，标志着我国在海上超深层天然气勘探领域取得重大突破。IT之家从报道获悉，这口井位于渤海中部海域，井深 5770 米。该井在勘探过程中，在火山岩地层累计钻遇天然气层超 120 米，展现出海上超深层火山岩领域广阔的勘探前景。中国海油天津公司渤海石油研究院地质总师郭涛介绍，该井储层温度达 150 摄氏度，地层压力超过 80 兆帕，面对高温高压的恶劣地层条件，开展多专业协同攻关，最大化提升复杂地质条件下作业质量，最终完成钻探作业并获得高产天然气流。海洋油气勘探领域通常把埋深超过 3500 米的地层称为深层，超过 4500 米的称为超深层。" data-title="井深 5770 米：我国海上超深层天然气勘探取得突破，测试日产天然气约 80 万立方米" data-date="11-12 16:13" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-12 16:13</span>
          <span class="news-item-title">井深 5770 米：我国海上超深层天然气勘探取得突破，测试日产天然气约 80 万立方米</span>
          <span class="news-value-point">💡 IT之家 11 月 12 日消息，据央视新闻今日从中国海油获悉，我国在渤海中部海域超 5000 米地层钻探获得一口火山岩高产油气井，测试日产天然…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/026/126.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 12 日消息，七彩虹 (Coloful) 现已在电商平台售卖 BATTLE-AX B850M-GAMING WIFI6E V14 主板。这一战斧系列新品价格为 799 元。BATTLE-AX B850M-GAMING WIFI6E V14 采用 230×220 (mm) 的“缩水”Micro-ATX 板型，配备 1 组 8Pin EPS CPU 供电接口。其拥有 7+2+1 相供电，选用 60A DrMOS；提供 2 条支持 7200+ MT/s 超频的 DDR5 UDIMM 内存插槽；PCIe 方面包括 1 个 Gen5 ×16 插槽、1 个 Gen4 ×1 插槽，两个 M.2 分别是 Gen5 ×4 和 Gen4 ×4；配备 2.5GbE LAN、Wi-Fi 6E &amp;" data-title="七彩虹推出 BATTLE-AX B850M-GAMING WIFI6E V14 主板，799 元" data-date="11-12 16:09" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-12 16:09</span>
          <span class="news-item-title">七彩虹推出 BATTLE-AX B850M-GAMING WIFI6E V14 主板，799 元</span>
          <span class="news-value-point">💡 IT之家 11 月 12 日消息，七彩虹 (Coloful) 现已在电商平台售卖 BATTLE-AX B850M-GAMING WIFI6E V…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/026/124.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 12 日消息，克罗地亚汽车制造商 Rimac 即将结束旗下 Nevera 纯电动超级跑车的生产。目前，公司正在制造最后 10 辆 Nevera R，预计这些车辆将在今年年底前全部交付客户。此后，该车将正式停产。Rimac 创始人兼 CEO 马特 · 里马克（Mate Rimac）在一段 Instagram 视频中透露，自 2022 年开始交付以来，Rimac Automobili 总共生产了 71 辆 Nevera 系列超跑。其中，标准版 Nevera 有 51 辆，性能更强的 Nevera R 有 20 辆。2018 年，公司首次展示后来发展为 Nevera 的概念车型时，原本计划生产 150 辆。尽管最终产量远低于最初目标，马特 · 里马克对此仍然相当满意。他在视频最" data-title="Rimac 宣布 Nevera 电动超跑即将停产，累计仅生产 71 辆" data-date="11-12 16:07" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-12 16:07</span>
          <span class="news-item-title">Rimac 宣布 Nevera 电动超跑即将停产，累计仅生产 71 辆</span>
          <span class="news-value-point">💡 IT之家 11 月 12 日消息，克罗地亚汽车制造商 Rimac 即将结束旗下 Nevera 纯电动超级跑车的生产</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-12/10730838.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网重庆11月12日电 (记者 贾楠)重庆市綦江区消防救援局12日发布警情通报称，2026年11月12日10时22分，綦江区消防救援局接到报警，綦江区古南街道北渡场嘉升包装制品有限公司发生火灾。接警后，綦江区消防救援局立即调派辖区消防救援力量赶赴现场处置。火势已经得到控制，目前正在清理余火，现场无人员伤亡。(完)" data-title="重庆綦江一包装制品公司发生火灾 现场无人员伤亡" data-date="11-12 16:03" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-12 16:03</span>
          <span class="news-item-title">重庆綦江一包装制品公司发生火灾 现场无人员伤亡</span>
          <span class="news-value-point">💡 中新网重庆11月12日电 (记者 贾楠)重庆市綦江区消防救援局12日发布警情通报称，2026年11月12日10时22分，綦江区消防救援局接到报警…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/golf/live-blog/12040/13611295/dp-world-tour-championship-first-round-live-latest-scores-highlights-as-rory-mcilroy-chases-race-to-dubai-title" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Hatton makes fast start as McIlroy chases Race to Dubai win LIVE!" data-title="Hatton makes fast start as McIlroy chases Race to Dubai win LIVE!" data-date="11-12 16:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-12 16:00</span>
          <span class="news-item-title">哈顿迅速发力，麦克罗伊紧追不舍，争夺迪拜争霸赛冠军，敬请观看直播！</span>
          <span class="news-item-title-en">Hatton makes fast start as McIlroy chases Race to Dubai win LIVE!</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025492/man-utd-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Man Utd latest: Carrick arrives at training ground after Poch agreement reached" data-title="Man Utd latest: Carrick arrives at training ground after Poch agreement reached" data-date="11-12 16:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-12 16:00</span>
          <span class="news-item-title">曼联最新消息：在与波切蒂诺达成协议后，卡里克抵达训练基地</span>
          <span class="news-item-title-en">Man Utd latest: Carrick arrives at training ground after Poch agreement reached</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-12/10730811.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社东京11月12日电(记者 朱晨曦)日本农林水产省12日说，京都府一个家禽农场出现高致病性禽流感。这是日本确认的本季第一起禽流感疫情。" data-title="日本报告本季首起禽流感疫情" data-date="11-12 15:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-12 15:32</span>
          <span class="news-item-title">日本报告本季首起禽流感疫情</span>
          <span class="news-value-point">💡 中新社东京11月12日电(记者 朱晨曦)日本农林水产省12日说，京都府一个家禽农场出现高致病性禽流感</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🌍</span>
      <span class="news-category-title">西方媒体视角 (外媒看中国 · 奇葩言论集锦)</span>
      <span class="news-category-count">1 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cje391ee1xvlo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="meimei" data-summary="据报导，卷入婚外情、被指涉入中国间谍活动的女子黄乐（Alice Huang Le）已经返回中国。近年来，她曾十次入境美国、八次入境台湾。" data-title="黄仁勋婚外情：黄乐据称身在北京，台湾废止其入境许可证" data-date="11-12 16:00" data-source="BBC">
          <span class="news-cat-tag cat-meimei">🌍 外媒视角</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-12 16:00</span>
          <span class="news-item-title">黄仁勋婚外情：黄乐据称身在北京，台湾废止其入境许可证</span>
          <span class="news-value-point">💡 据报导，卷入婚外情、被指涉入中国间谍活动的女子黄乐（Alice Huang Le）已经返回中国</span>
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


<p class="news-updated">🕐 抓取更新于 2026-11-12 16:54（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
