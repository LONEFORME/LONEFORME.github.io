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
      <span>2026-10-22 21:05 抓取更新</span>
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
        <span class="channel-count">48</span>
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
        <span class="channel-count">3</span>
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
  <div class="ov-item"><span class="ov-num">48</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">8</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×18 · The Verge×8</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gj/2026/10-22/10719313.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月22日电 利雅得消息：沙特阿拉伯民航总局22日宣布，该国东部达曼市法赫德国王国际机场21日晚遭袭击，已导致2人死亡，8人受伤。" data-title="沙特机场再遭袭击已致2死8伤" data-date="10-22 21:00" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-22 21:00</span>
      </div>
      <h2 class="hero-featured-title">沙特机场再遭袭击已致2死8伤</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/016/685.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 22 日消息，据小鹏汽车官方今日分享，10 月 21 日至 23 日，2026 世界智能网联汽车大会（WICV）在北京亦庄举办。小鹏人形机器人、小鹏 G9L、小鹏 X9、小鹏 G7 等多款产品集中登场，展现在物理 AI 赛道的技术积累。10 月 21 日，何小鹏出席大会 &quot; 巅峰对话 &quot; 环节。就主持人“特斯拉 FSD 与小鹏 NGP 表现接近”的提问，小鹏集团董事长、CEO 何小鹏表示：面对欧洲复杂的路况 —— 狭窄的小路、占比很高的单行道，甚至六车道环线地下没有标线的场景、人车穿行等，要做到符合当地政策法规、安全和文化，是一件很困难的事情。为什么小鹏和特斯拉都能在法国开？实际上，我们是将 L4 的模型能力，去满足靠边停车、在未曾见过的复杂路段符合当地法律法规与文化等。" data-title="何小鹏：L4 技术落地大概在 2028 年下半年，需要全体系软硬件一起开发" data-date="10-22 21:03" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">何小鹏：L4 技术落地大概在 2028 年下半年，需要全体系软硬件一起开发</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/ckg5j1zdn4m3o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="米克尔·阿尔特塔（ Mikel Arteta ）表示，阿森纳的布卡约·萨卡（ Bukayo Saka ）在拜仁慕尼黑的冠军联赛平局中受伤的四头肌“看起来一点也不好”。" data-title="Saka injury &#39;does not look good&#39; - how will Arsenal cope?" data-date="10-22 06:51" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">Saka injury 'does not look good' - how will Arsenal cope?</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/016/686.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 22 日消息，据消息源 LeicaRumors 昨日发文，徕卡计划推出 Hammertone 锤纹版 M-11P 数码旁轴相机和 M-A 胶片旁轴相机。IT之家了解到，徕卡早在今年春季就推出过 M-A 的锤纹限量版，纪念其日本银座旗舰店开业 20 周年，该机全球限量 100 台。不过新版机器据称将不限量，正面取消“20 周年”标识，金属的颜色也会略深一些。据悉，徕卡 M-A 是一台“回归摄影本质”的旁轴相机，整个机身完全没有任何电子元器件，过片、快门等操作完全使用机械驱动。相比 M-P 移除了测光表，因此无需电池即可使用。当然也没有自动曝光、自动对焦等现代功能。机械快门最快可达 1/1000 秒，闪光同步速度 1/50 秒。而徕卡 M-11P 是一台数码旁轴相机，配备 6" data-title="徕卡锤纹新机曝光：M-11P 数码旁轴与 M-A 胶片旁轴齐发" data-date="10-22 21:03" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">徕卡锤纹新机曝光：M-11P 数码旁轴与 M-A 胶片旁轴齐发</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-22/10719313.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月22日电 利雅得消息：沙特阿拉伯民航总局22日宣布，该国东部达曼市法赫德国王国际机场21日晚遭袭击，已导致2人死亡，8人受伤。" data-title="沙特机场再遭袭击已致2死8伤" data-date="10-22 21:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-22 21:00</span>
          <span class="news-item-title">沙特机场再遭袭击已致2死8伤</span>
          <span class="news-value-point">💡 中新社北京10月22日电 利雅得消息：沙特阿拉伯民航总局22日宣布，该国东部达曼市法赫德国王国际机场21日晚遭袭击，已导致2人死亡，8人受伤</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-22/10719349.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月22日电 据美媒当地时间21日消息，多名知情人士称，美国国防部拟打造一个“更强有力的”深度潜伏间谍项目，针对美国的竞争对手开展经济战。" data-title="美媒：美国防部拟打造新的深度潜伏间谍项目" data-date="10-22 20:58" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-22 20:58</span>
          <span class="news-item-title">美媒：美国防部拟打造新的深度潜伏间谍项目</span>
          <span class="news-value-point">💡 中新网10月22日电 据美媒当地时间21日消息，多名知情人士称，美国国防部拟打造一个“更强有力的”深度潜伏间谍项目，针对美国的竞争对手开展经济战</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-22/10719344.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月22日电 据阿根廷媒体报道，当地时间21日，阿根廷总统米莱重申将通过外交途径收回马尔维纳斯群岛(简称马岛，英国称福克兰群岛)主权。" data-title="阿根廷总统重申：将以外交手段收回马岛主权" data-date="10-22 20:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-22 20:54</span>
          <span class="news-item-title">阿根廷总统重申：将以外交手段收回马岛主权</span>
          <span class="news-value-point">💡 中新网10月22日电 据阿根廷媒体报道，当地时间21日，阿根廷总统米莱重申将通过外交途径收回马尔维纳斯群岛(简称马岛，英国称福克兰群岛)主权</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-22/10719339.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月22日电 据江西省纪委监委消息：江西交通职业技术学院原党委副书记、院长黄明忠涉嫌严重违纪违法，主动向组织交代问题，目前正接受江西省纪委监委纪律审查和监察调查。" data-title="江西交通职业技术学院原院长黄明忠接受审查调查" data-date="10-22 20:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-22 20:52</span>
          <span class="news-item-title">江西交通职业技术学院原院长黄明忠接受审查调查</span>
          <span class="news-value-point">💡 中新网10月22日电 据江西省纪委监委消息：江西交通职业技术学院原党委副书记、院长黄明忠涉嫌严重违纪违法，主动向组织交代问题，目前正接受江西省纪…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-22/10719338.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月22日电 据内蒙古自治区纪委监委消息：内蒙古自治区民政厅原党组成员、副厅长刘程民涉嫌严重违纪违法，目前正接受内蒙古自治区纪委监委纪律审查和监察调查。" data-title="内蒙古自治区民政厅原副厅长刘程民接受审查调查" data-date="10-22 20:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-22 20:49</span>
          <span class="news-item-title">内蒙古自治区民政厅原副厅长刘程民接受审查调查</span>
          <span class="news-value-point">💡 中新网10月22日电 据内蒙古自治区纪委监委消息：内蒙古自治区民政厅原党组成员、副厅长刘程民涉嫌严重违纪违法，目前正接受内蒙古自治区纪委监委纪律…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-22/10719336.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月22日电 据海南省纪委监委消息：海南省应急管理厅党委委员、副厅长郭刚涉嫌严重违纪违法，目前正接受海南省纪委监委纪律审查和监察调查。" data-title="海南省应急管理厅党委委员、副厅长郭刚接受审查调查" data-date="10-22 20:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-22 20:49</span>
          <span class="news-item-title">海南省应急管理厅党委委员、副厅长郭刚接受审查调查</span>
          <span class="news-value-point">💡 中新网10月22日电 据海南省纪委监委消息：海南省应急管理厅党委委员、副厅长郭刚涉嫌严重违纪违法，目前正接受海南省纪委监委纪律审查和监察调查</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-22/10719335.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京10月22日电 (记者 陈杭)北京市延庆区拟到2030年，基本建成生态文明幸福的最美冬奥城，为建设国际一流的生态文明示范区奠定坚实基础，确保在与全市同步率先基本实现社会主义现代化上取得决定性进展；到2035年，全面建成生态文明幸福的最美冬奥城，初步建成国际一流的生态文明示范区，与全市同步率先基本实现社会主义现代化。" data-title="北京延庆拟到2035年全面建成生态文明幸福的最美冬奥城" data-date="10-22 20:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-22 20:41</span>
          <span class="news-item-title">北京延庆拟到2035年全面建成生态文明幸福的最美冬奥城</span>
          <span class="news-value-point">💡 中新网北京10月22日电 (记者 陈杭)北京市延庆区拟到2030年，基本建成生态文明幸福的最美冬奥城，为建设国际一流的生态文明示范区奠定坚实基础…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-22/10719291.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月22日电 (记者 谢雁冰 李京泽)“长征的历史从未远去，长征的路在不断延伸。”" data-title="（近观中国）走好新的长征路，习近平强调五个“必须”" data-date="10-22 20:13" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-22 20:13</span>
          <span class="news-item-title">（近观中国）走好新的长征路，习近平强调五个“必须”</span>
          <span class="news-value-point">💡 中新社北京10月22日电 (记者 谢雁冰 李京泽)“长征的历史从未远去，长征的路在不断延伸</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-22/10719311.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="10月22日下午，十四届全国人大常委会第七十四次委员长会议在北京人民大会堂举行。赵乐际委员长主持会议。新华社记者 刘卫兵 摄 新华社北京10月22日电 十四届全国人大常委会第七十四次委员长会议22日下午在北京人民大会堂举行。赵乐际委员长主持会议。会议决定，十四届全国人大常委会第二十五次会议11月2日至6日在北京举行。" data-title="赵乐际主持召开十四届全国人大常委会第七十四次委员长会议 决定十四届全国人大常委会第二十五次会议11月2日至6日在京举行" data-date="10-22 20:12" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-22 20:12</span>
          <span class="news-item-title">赵乐际主持召开十四届全国人大常委会第七十四次委员长会议 决定十四届全国人大常委会第二十五次会议11月2日至6日在京举行</span>
          <span class="news-value-point">💡 10月22日下午，十四届全国人大常委会第七十四次委员长会议在北京人民大会堂举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-22/10719229.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月22日电 加拉加斯消息：当地时间21日，委内瑞拉执政党统一社会主义党发布公报，谴责美国佛罗里达州对古巴革命领袖劳尔·卡斯特罗发出逮捕令。" data-title="委内瑞拉谴责美方对古巴革命领袖劳尔·卡斯特罗发逮捕令" data-date="10-22 19:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-22 19:52</span>
          <span class="news-item-title">委内瑞拉谴责美方对古巴革命领袖劳尔·卡斯特罗发逮捕令</span>
          <span class="news-value-point">💡 中新社北京10月22日电 加拉加斯消息：当地时间21日，委内瑞拉执政党统一社会主义党发布公报，谴责美国佛罗里达州对古巴革命领袖劳尔·卡斯特罗发出…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-22/10719228.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月22日电 综合消息：沙特阿拉伯民航总局当地时间22日发表声明称，位于沙特东部城市达曼的法赫德国王国际机场21日晚遭遇袭击，已造成1人死亡、8人受伤。美国下令驻沙特“非紧急”政府雇员及家属撤离。" data-title="美下令驻沙特“非紧急”政府雇员及家属撤离" data-date="10-22 19:18" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-22 19:18</span>
          <span class="news-item-title">美下令驻沙特“非紧急”政府雇员及家属撤离</span>
          <span class="news-value-point">💡 中新社北京10月22日电 综合消息：沙特阿拉伯民航总局当地时间22日发表声明称，位于沙特东部城市达曼的法赫德国王国际机场21日晚遭遇袭击，已造成…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-22/10719260.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网10月22日电 据美国全国广播公司22日报道，美军正在缩减在约旦、卡塔尔和科威特的驻军规模。但美国中央司令部拒绝对相关报道置评，仅称美军会定期调整兵力部署，以优化部队的战备水平。" data-title="美媒：美军正在缩减约旦、卡塔尔、科威特驻军规模" data-date="10-22 19:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-22 19:16</span>
          <span class="news-item-title">美媒：美军正在缩减约旦、卡塔尔、科威特驻军规模</span>
          <span class="news-value-point">💡 中新网10月22日电 据美国全国广播公司22日报道，美军正在缩减在约旦、卡塔尔和科威特的驻军规模</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/22/world/middleeast/saudi-houthis-yemen-dammam-airport.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="几周来，伊朗支持的胡塞武装一直在攻击沙特的航空和能源部门。" data-title="Strike on Saudi Airport Kills 2 as U.S. Tells Some Diplomats to Leave" data-date="10-22 19:10" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-22 19:10</span>
          <span class="news-item-title">美国告诉一些外交官离开，沙特机场罢工造成2人死亡</span>
          <span class="news-item-title-en">Strike on Saudi Airport Kills 2 as U.S. Tells Some Diplomats to Leave</span>
          <span class="news-value-point">💡 几周来，伊朗支持的胡塞武装一直在攻击沙特的航空和能源部门</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/crly0lw6g726o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="由于移民限制和科技公司削减外籍员工，获得美国永久居留权对许多印度人来说正变得越来越遥不可及。" data-title="特朗普收紧绿卡政策，印度科技从业者的“美国梦”面临考验" data-date="10-22 17:21" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-22 17:21</span>
          <span class="news-item-title">特朗普收紧绿卡政策，印度科技从业者的“美国梦”面临考验</span>
          <span class="news-value-point">💡 由于移民限制和科技公司削减外籍员工，获得美国永久居留权对许多印度人来说正变得越来越遥不可及</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/21/us/politics/michigan-senate-debate-takeaways-el-sayed-rogers.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="阿卜杜勒·赛义德（ Abdul El-Sayed ）指责迈克·罗杰斯（ Mike Rogers ）对特朗普罗杰斯先生指责El-Sayed博士对国家的忠诚度不够。这比他们上次的辩论更亲切。" data-title="MAGA Bingo and Questions of Loyalty: 5 Michigan Senate Debate Takeaways" data-date="10-22 16:03" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-22 16:03</span>
          <span class="news-item-title">MAGA宾果游戏和忠诚度问题： 5密歇根州参议院辩论要点</span>
          <span class="news-item-title-en">MAGA Bingo and Questions of Loyalty: 5 Michigan Senate Debate Takeaways</span>
          <span class="news-value-point">💡 阿卜杜勒·赛义德（ Abdul El-Sayed ）指责迈克·罗杰斯（ Mike Rogers ）对特朗普罗杰斯先生指责El-Sayed博士对国…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/016/685.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 22 日消息，据小鹏汽车官方今日分享，10 月 21 日至 23 日，2026 世界智能网联汽车大会（WICV）在北京亦庄举办。小鹏人形机器人、小鹏 G9L、小鹏 X9、小鹏 G7 等多款产品集中登场，展现在物理 AI 赛道的技术积累。10 月 21 日，何小鹏出席大会 &quot; 巅峰对话 &quot; 环节。就主持人“特斯拉 FSD 与小鹏 NGP 表现接近”的提问，小鹏集团董事长、CEO 何小鹏表示：面对欧洲复杂的路况 —— 狭窄的小路、占比很高的单行道，甚至六车道环线地下没有标线的场景、人车穿行等，要做到符合当地政策法规、安全和文化，是一件很困难的事情。为什么小鹏和特斯拉都能在法国开？实际上，我们是将 L4 的模型能力，去满足靠边停车、在未曾见过的复杂路段符合当地法律法规与文化等。" data-title="何小鹏：L4 技术落地大概在 2028 年下半年，需要全体系软硬件一起开发" data-date="10-22 21:03" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-22 21:03</span>
          <span class="news-item-title">何小鹏：L4 技术落地大概在 2028 年下半年，需要全体系软硬件一起开发</span>
          <span class="news-value-point">💡 IT之家 10 月 22 日消息，据小鹏汽车官方今日分享，10 月 21 日至 23 日，2026 世界智能网联汽车大会（WICV）在北京亦庄举…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1016399/1password-ai-agent-password-sign-in" target="_blank" rel="noopener" data-cat="keji" data-summary="1Password推出了一项新功能，允许AI代理登录您的帐户，而无需实际查看或处理您的密码。正确命名的1Password for Agents不会让机器人免费访问您所有关联的帐户- y" data-title="1Password lets AI agents use your passwords without seeing them" data-date="10-22 21:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-22 21:00</span>
          <span class="news-item-title">1Password允许人工智能代理在不显示密码的情况下使用您的密码</span>
          <span class="news-item-title-en">1Password lets AI agents use your passwords without seeing them</span>
          <span class="news-value-point">💡 1Password推出了一项新功能，允许AI代理登录您的帐户，而无需实际查看或处理您的密码</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1016492/tesla-optimus-robots-production-musk-q3-earnings" target="_blank" rel="noopener" data-cat="keji" data-summary="在周三的特斯拉财报电话会议上，首席执行官埃隆·马斯克(Elon Musk)宣布，该公司已开始在加利福尼亚州弗里蒙特的大批量生产线上早期生产其人形机器人。然后他列出了仍然需要工作的东西：机器人的手，它的安全，" data-title="Just because Tesla’s Optimus is in production doesn’t mean it’s actually ready" data-date="10-22 20:53" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-22 20:53</span>
          <span class="news-item-title">仅仅因为特斯拉的擎天柱正在生产并不意味着它实际上已经准备就绪</span>
          <span class="news-item-title-en">Just because Tesla’s Optimus is in production doesn’t mean it’s actually ready</span>
          <span class="news-value-point">💡 在周三的特斯拉财报电话会议上，首席执行官埃隆·马斯克(Elon Musk)宣布，该公司已开始在加利福尼亚州弗里蒙特的大批量生产线上早期生产其人形…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/016/682.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 22 日消息，OPPO Find 系列产品负责人卓世杰宣布：今天起，OPPO Find X10 系列正式登陆全球超过 60 个国家和地区。据IT之家昨日报道，OPPO 在海外市场推出 Find X10 全球版机型，12GB+256GB 版本售价为 1,099 英镑（IT之家注：现汇率约合 9,834 元人民币） / 1,299 欧元（现汇率约合 9,749 元人民币）。OPPO Find X10 全球版配备 6.59 英寸 LTPO AMOLED 屏幕，分辨率为 2768×1272，边框宽度 0.99 毫米，支持 144Hz 高刷，HDR 峰值亮度可达 3600 尼特。该机搭载联发科天玑 9600M 芯片，采用台积电 3nm 工艺打造。搭配 12GB LPDDR5X 内存" data-title="OPPO Find X10 系列手机正式登陆全球超过 60 个国家和地区" data-date="10-22 20:53" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-22 20:53</span>
          <span class="news-item-title">OPPO Find X10 系列手机正式登陆全球超过 60 个国家和地区</span>
          <span class="news-value-point">💡 IT之家 10 月 22 日消息，OPPO Find 系列产品负责人卓世杰宣布：今天起，OPPO Find X10 系列正式登陆全球超过 60 …</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/cpus/amd-ryzen-5-5500f-review" target="_blank" rel="noopener" data-cat="keji" data-summary="在使用基于塞尚的5500多年后， AMD终于将其$ 100的CPU升级到威猛(Vermeer)家族的5500F ，增加了200 MHz的时钟速度和PCIe 4.0升级。" data-title="AMD Ryzen 5 5500F review: Vermeer rides again for budget gaming PCs" data-date="10-22 20:40" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-22 20:40</span>
          <span class="news-item-title">AMD Ryzen 5 5500F回顾：威猛(Vermeer)再次驾驶经济型游戏PC</span>
          <span class="news-item-title-en">AMD Ryzen 5 5500F review: Vermeer rides again for budget gaming PCs</span>
          <span class="news-value-point">💡 在使用基于塞尚的5500多年后， AMD终于将其$ 100的CPU升级到威猛(Vermeer)家族的5500F ，增加了200 MHz的时钟速度…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/report/1015811/ai-shopping-agents-blocked-amazon-the-realreal-target-meta-muse" target="_blank" rel="noopener" data-cat="keji" data-summary="使用人工智能代理为您购物是一种奇怪的体验。科技公司将它们作为个人助理进行营销-劳动力的民主化通常只适用于富人和有权势的人。在实践中，至少在买东西的时候" data-title="AI agents are ready to shop. Some retailers are wary." data-date="10-22 20:30" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-22 20:30</span>
          <span class="news-item-title">人工智能代理商已准备好购物。一些零售商持谨慎态度。</span>
          <span class="news-item-title-en">AI agents are ready to shop. Some retailers are wary.</span>
          <span class="news-value-point">💡 使用人工智能代理为您购物是一种奇怪的体验</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1016443/anthropic-claude-citrini-vibecoding-scorpion-antivenom" target="_blank" rel="noopener" data-cat="keji" data-summary="一家投资研究公司希望证明人工智能可以彻底改变药物开发。因此，他们与Anthropic合作，看看未发布的Claude版本是否可以制造蝎子抗蛇毒血清。它不能。它想出了一些有前途的起点" data-title="Claude did not invent scorpion antivenom" data-date="10-22 20:21" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-22 20:21</span>
          <span class="news-item-title">克劳德没有发明蝎子抗蛇毒血清</span>
          <span class="news-item-title-en">Claude did not invent scorpion antivenom</span>
          <span class="news-value-point">💡 一家投资研究公司希望证明人工智能可以彻底改变药物开发</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/dram/micron-pulls-the-plug-on-future-4f2-dram-after-two-decades-of-research-in-dramatic-shift-company-says-architecture-offers-no-meaningful-density-advantages-increases-manufacturing-complexity-and-costs-and-has-fundamental-scaling-limitations" target="_blank" rel="noopener" data-cat="keji" data-summary="美光认为，与较小的存储单元相比，更先进的处理技术在DRAM位密度方面将带来更多优势。" data-title="Micron pulls the plug on future 4F² DRAM after two decades of research in dramatic shift" data-date="10-22 20:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-22 20:00</span>
          <span class="news-item-title">经过二十年的戏剧性转变研究，美光拔掉了未来4F ² DRAM的插头</span>
          <span class="news-item-title-en">Micron pulls the plug on future 4F² DRAM after two decades of research in dramatic shift</span>
          <span class="news-value-point">💡 美光认为，与较小的存储单元相比，更先进的处理技术在DRAM位密度方面将带来更多优势</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/retro-gaming/retro-atari-vcs-platform-will-end-with-the-closure-of-its-software-store-in-february-2027-os-update-will-be-released-removing-reliance-on-atari-servers-and-opening-up-homebrew-development" target="_blank" rel="noopener" data-cat="keji" data-summary="随着雅达利决定明年初关闭基于Linux的AMD APU驱动机器的软件商店，现代雅达利VCS正式退役。" data-title="Retro Atari VCS platform will end with the closure of its software store in February 2027" data-date="10-22 19:45" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-22 19:45</span>
          <span class="news-item-title">Retro Atari VCS平台将于2027年2月关闭其软件商店</span>
          <span class="news-item-title-en">Retro Atari VCS platform will end with the closure of its software store in February 2027</span>
          <span class="news-value-point">💡 随着雅达利决定明年初关闭基于Linux的AMD APU驱动机器的软件商店，现代雅达利VCS正式退役</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-22/10719227.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新社吉隆坡10月22日电 (记者 刘育英)马来西亚教育部副部长黄家和近日接受中新社专访时表示，马来西亚正发挥多语言、多元文化教育优势，推动对华教育合作从传统人才交流向职业教育、人工智能和数字教育等领域拓展。" data-title="专访马来西亚教育部副部长：马中教育合作从人才交流迈向新领域" data-date="10-22 19:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-22 19:17</span>
          <span class="news-item-title">专访马来西亚教育部副部长：马中教育合作从人才交流迈向新领域</span>
          <span class="news-value-point">💡 中新社吉隆坡10月22日电 (记者 刘育英)马来西亚教育部副部长黄家和近日接受中新社专访时表示，马来西亚正发挥多语言、多元文化教育优势，推动对华…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/storage/lto-roadmap-extends-to-365-tb-per-cartridge-as-tape-storage-refuses-to-die-25-year-old-format-sees-400x-capacity-increase-without-changing-form-factor" target="_blank" rel="noopener" data-cat="keji" data-summary="尽管存在各种可能性，但人工智能热潮正在增加磁带存储的相关性，因为技术可以在空闲状态下实现零功耗的廉价存储，以及具有气隙的终极安全性。" data-title="LTO roadmap extends to 365 TB per cartridge as tape storage refuses to die" data-date="10-22 19:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-22 19:00</span>
          <span class="news-item-title">随着磁带存储拒绝死亡， LTO路线图扩展到每个磁带盒365 TB</span>
          <span class="news-item-title-en">LTO roadmap extends to 365 TB per cartridge as tape storage refuses to die</span>
          <span class="news-value-point">💡 尽管存在各种可能性，但人工智能热潮正在增加磁带存储的相关性，因为技术可以在空闲状态下实现零功耗的廉价存储，以及具有气隙的终极安全性</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c620re8ye3e4o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="BBC采访了多名前任和现任Google DeepMind员工，了解他们对人工智能在战场上应用的忧虑。" data-title="Google军事人工智能合约引发辞职潮" data-date="10-22 16:44" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-22 16:44</span>
          <span class="news-item-title">Google军事人工智能合约引发辞职潮</span>
          <span class="news-value-point">💡 BBC采访了多名前任和现任Google DeepMind员工，了解他们对人工智能在战场上应用的忧虑</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/504832.html" target="_blank" rel="noopener" data-cat="keji" data-summary="中电信人工智能科技有限公司星辰通用人工智能实验室正式发布并开源意图理解专用模型 Xing4.0-29B-Intent" data-title="既能“做选择题”，也能“做填空题”——星辰意图理解模型Xing4.0-29B-Intent发布" data-date="10-22 15:11" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-22 15:11</span>
          <span class="news-item-title">既能“做选择题”，也能“做填空题”——星辰意图理解模型Xing4.0-29B-Intent发布</span>
          <span class="news-value-point">💡 中电信人工智能科技有限公司星辰通用人工智能实验室正式发布并开源意图理解专用模型 Xing4.0-29B-Intent</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/10/504800.html" target="_blank" rel="noopener" data-cat="keji" data-summary="挤进全球Physical AI核心供应链" data-title="谁在给OpenAI供应具身数据？" data-date="10-22 15:05" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">10-22 15:05</span>
          <span class="news-item-title">谁在给OpenAI供应具身数据？</span>
          <span class="news-value-point">💡 挤进全球Physical AI核心供应链</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/016/403.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 22 日消息，在今日下午的科大讯飞全球 1024 开发者节活动中，讯飞星火 X2.6 端云一体大模型正式发布。讯飞星火 X2.6 宣称首次基于全国产算力实现代码和智能体能力突破。科大讯飞董事长刘庆峰表示，只有星火一家是用全国产算力训练的，其他全是在 N 卡上训练，而且科大讯飞的尺寸是最小的。此外，刘庆峰表示讯飞星火 X2.6 率先突破国产芯片长程任务的训练效率瓶颈，适配国产平台的长程任务动态并行训练技术，解决了因为国产芯片显存带宽限制导致的混合训练效率低下问题。对于国产算力集群在长程任务上的推理效率，科大讯飞也实现了两个重要创新：一个是基于国产异构算力的分布式推理技术，解决国产芯片显存带宽限制导致的训不快问题。另一个是提出基于国产设备的开发技术，很多东西都不用重新再计算，" data-title="讯飞星火 X2.6 端云一体大模型发布，首次基于全国产算力实现代码和智能体能力突破" data-date="10-22 14:40" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-22 14:40</span>
          <span class="news-item-title">讯飞星火 X2.6 端云一体大模型发布，首次基于全国产算力实现代码和智能体能力突破</span>
          <span class="news-value-point">💡 IT之家 10 月 22 日消息，在今日下午的科大讯飞全球 1024 开发者节活动中，讯飞星火 X2.6 端云一体大模型正式发布</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">3 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/ckg5j1zdn4m3o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="米克尔·阿尔特塔（ Mikel Arteta ）表示，阿森纳的布卡约·萨卡（ Bukayo Saka ）在拜仁慕尼黑的冠军联赛平局中受伤的四头肌“看起来一点也不好”。" data-title="Saka injury &#39;does not look good&#39; - how will Arsenal cope?" data-date="10-22 06:51" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-22 06:51</span>
          <span class="news-item-title">SAKA伤势“看起来不太好” -阿森纳将如何应对？</span>
          <span class="news-item-title-en">Saka injury 'does not look good' - how will Arsenal cope?</span>
          <span class="news-value-point">💡 米克尔·阿尔特塔（ Mikel Arteta ）表示，阿森纳的布卡约·萨卡（ Bukayo Saka ）在拜仁慕尼黑的冠军联赛平局中受伤的四头肌…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cq74pjn80x4wo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联队长布鲁诺·费尔南德斯（ Bruno Fernandes ）将主教练迈克尔·卡里克（ Michael Carrick ）归咎于导致科莫在冠军联赛中以4比1尴尬失利的战术。" data-title="Fernandes rounds on Carrick after Man Utd humiliation" data-date="10-22 03:59" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-22 03:59</span>
          <span class="news-item-title">曼联羞辱后，费尔南德斯抨击卡里克</span>
          <span class="news-item-title-en">Fernandes rounds on Carrick after Man Utd humiliation</span>
          <span class="news-value-point">💡 曼联队长布鲁诺·费尔南德斯（ Bruno Fernandes ）将主教练迈克尔·卡里克（ Michael Carrick ）归咎于导致科莫在冠军…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/21/ai-promises-productivity-but-for-managers-its-mostly-a-headache-for-now-says-new-survey/" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="根据一项新的调查，超过50%的经理表示，他们发现在采用人工智能后更难评估员工的工作。" data-title="AI promises productivity, but for managers, it’s mostly a headache for now" data-date="10-21 22:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-21 22:00</span>
          <span class="news-item-title">人工智能有望提高生产力，但对于管理者来说，目前这主要是一个令人头疼的问题</span>
          <span class="news-item-title-en">AI promises productivity, but for managers, it’s mostly a headache for now</span>
          <span class="news-value-point">💡 根据一项新的调查，超过50%的经理表示，他们发现在采用人工智能后更难评估员工的工作</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/016/686.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 22 日消息，据消息源 LeicaRumors 昨日发文，徕卡计划推出 Hammertone 锤纹版 M-11P 数码旁轴相机和 M-A 胶片旁轴相机。IT之家了解到，徕卡早在今年春季就推出过 M-A 的锤纹限量版，纪念其日本银座旗舰店开业 20 周年，该机全球限量 100 台。不过新版机器据称将不限量，正面取消“20 周年”标识，金属的颜色也会略深一些。据悉，徕卡 M-A 是一台“回归摄影本质”的旁轴相机，整个机身完全没有任何电子元器件，过片、快门等操作完全使用机械驱动。相比 M-P 移除了测光表，因此无需电池即可使用。当然也没有自动曝光、自动对焦等现代功能。机械快门最快可达 1/1000 秒，闪光同步速度 1/50 秒。而徕卡 M-11P 是一台数码旁轴相机，配备 6" data-title="徕卡锤纹新机曝光：M-11P 数码旁轴与 M-A 胶片旁轴齐发" data-date="10-22 21:03" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-22 21:03</span>
          <span class="news-item-title">徕卡锤纹新机曝光：M-11P 数码旁轴与 M-A 胶片旁轴齐发</span>
          <span class="news-value-point">💡 IT之家 10 月 22 日消息，据消息源 LeicaRumors 昨日发文，徕卡计划推出 Hammertone 锤纹版 M-11P 数码旁轴相…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1015371/insta360-mic-wireless-microphone-color-e-ink-screen" target="_blank" rel="noopener" data-cat="zonghe" data-summary="继去年5月推出其无线麦克风专业版系统后， Insta360宣布了一种更便宜的替代方案，该系统具有用于定制品牌的内置彩色E墨水屏幕和用于模拟不同拾音模式的三个麦克风阵列，" data-title="Insta360 launches a cheaper version of its wireless mics with color screens" data-date="10-22 21:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-22 21:00</span>
          <span class="news-item-title">Insta360推出更便宜的带彩色屏幕的无线麦克风版本</span>
          <span class="news-item-title-en">Insta360 launches a cheaper version of its wireless mics with color screens</span>
          <span class="news-value-point">💡 继去年5月推出其无线麦克风专业版系统后， Insta360宣布了一种更便宜的替代方案，该系统具有用于定制品牌的内置彩色E墨水屏幕和用于模拟不同拾…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1015659/birdbuddy-smart-bird-feeder-2k-camera-home-nook-ai-identification" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Birdbuddy终于推出了今年早些时候在CES 2026上最初宣布的新型智能喂鸟器，但有新的名称。Birdbuddy 2 Mini现在被称为Birdbuddy Nook ，它的设计是一个更小，更实惠的选择" data-title="Birdbuddy’s Nook is a compact smart bird feeder for small spaces and budgets" data-date="10-22 21:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-22 21:00</span>
          <span class="news-item-title">Birdbuddy's Nook是一款紧凑型智能喂鸟器，适用于小空间和预算</span>
          <span class="news-item-title-en">Birdbuddy’s Nook is a compact smart bird feeder for small spaces and budgets</span>
          <span class="news-value-point">💡 Birdbuddy终于推出了今年早些时候在CES 2026上最初宣布的新型智能喂鸟器，但有新的名称</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1015749/googlebook-hp-acer-lenovo-dell-asus-collective-laptop-review" target="_blank" rel="noopener" data-cat="zonghe" data-summary="E到目前为止，我们测试的每台Googlebook笔记本电脑都有出色的硬件。问题在于软件。虽然Googlebook OS对笔记本电脑和手机如何协同工作有着令人兴奋的想法，但目前它主要是一种令人沮丧的体验，充满了令人讨厌的错误" data-title="Googlebooks just aren’t ready" data-date="10-22 21:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-22 21:00</span>
          <span class="news-item-title">Googlebooks还没有准备好</span>
          <span class="news-item-title-en">Googlebooks just aren’t ready</span>
          <span class="news-value-point">💡 E到目前为止，我们测试的每台Googlebook笔记本电脑都有出色的硬件</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1015791/birdbuddy-home-nook-smart-bird-feeder-hands-on" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Birdbuddy的下一代智能喂鸟器终于来了。在BirdBuddy Nook （ 99美元起）和旗舰Birdbuddy Home （ 219美元）度过了几天之后，有一个明显的赢家： The Nook是完美的全能产品，" data-title="Birdbuddy’s budget feeder foiled my squirrels" data-date="10-22 21:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-22 21:00</span>
          <span class="news-item-title">Birdbuddy的预算喂食器挫败了我的松鼠</span>
          <span class="news-item-title-en">Birdbuddy’s budget feeder foiled my squirrels</span>
          <span class="news-value-point">💡 Birdbuddy的下一代智能喂鸟器终于来了</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/016/684.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 22 日消息，影石今晚发布了全新轻旗舰级无线麦克风 Insta360 Mic，单枚发射器售价 499 元，首发价 439 元。与今年 5 月发布的旗舰 Mic Pro 相比，这款新品的核心变化不在收音硬件，而在存储：Mic Pro 内置存储不可扩展，Mic 则将其替换为可插拔的 microSD 卡槽。据影石介绍，不插卡时，麦克风仍可通过蓝牙或接收器连接设备正常收音，内录功能不开启；插入 microSD 卡后，32-bit 浮点内录才被激活，录音文件直接写入用户自备的存储卡。对于已经为运动相机或无人机购置过多张 microSD 卡的用户，这相当于省去了一笔专用存储的重复投入。除此之外，Mic 在其余核心配置上基本沿用了 Mic Pro 的方案。每枚发射器搭载自定义墨水屏，可" data-title="439 元起影石 Insta360 Mic 发布，用 microSD 卡槽换掉 Mic Pro 的内置存储" data-date="10-22 20:59" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-22 20:59</span>
          <span class="news-item-title">439 元起影石 Insta360 Mic 发布，用 microSD 卡槽换掉 Mic Pro 的内置存储</span>
          <span class="news-value-point">💡 IT之家 10 月 22 日消息，影石今晚发布了全新轻旗舰级无线麦克风 Insta360 Mic，单枚发射器售价 499 元，首发价 439 元</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/016/681.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 22 日消息，据 Android Authority 今日报道，索尼似乎通过 2026 年 6 月的固件更新限制了部分 Xperia 手机在非官方支持市场使用 5G 网络的能力。根据大量 Reddit 用户反馈，受影响设备包括 Xperia 1 V 及更新机型，涉及美国、加拿大、澳大利亚和多个欧洲国家地区。部分用户表示，更新后手机仍可使用 VoLTE，但无法再连接 5G 网络，此前通过切换双卡双待（DSDS）功能并重启手机来恢复 5G 功能的方法也已失效。索尼美国官网的 Xperia 1 V 软件更新记录显示，相关固件版本为 67.2.A.3.178，发布日期是 2026 年 6 月 29 日，更新说明仅提到安全补丁更新至 2026 年 6 月 1 日。Reddit 上的" data-title="非官方支持地区用户反馈 Xperia 系统更新后无法使用 5G 网络，索尼尚未回应" data-date="10-22 20:51" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-22 20:51</span>
          <span class="news-item-title">非官方支持地区用户反馈 Xperia 系统更新后无法使用 5G 网络，索尼尚未回应</span>
          <span class="news-value-point">💡 IT之家 10 月 22 日消息，据 Android Authority 今日报道，索尼似乎通过 2026 年 6 月的固件更新限制了部分 Xp…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/016/677.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 22 日消息，前段时间爆火的第一人称射击游戏《战狗》（Wardogs）开发商 Bulkhead 正在逐步实施跨地区匹配限制，希望借此减少作弊行为。该工作室表示，此举旨在保护尽可能多的玩家，避免作弊较严重地区的玩家对其他地区玩家的游戏体验造成影响。不过，这项措施也引发了部分玩家的不满，部分玩家甚至抗议表示将申请退款。目前，《战狗》采用的地区限制方案以网络延迟为依据，将玩家的最高允许延迟限制在 175 毫秒。超过这一阈值的玩家将受到跨地区游戏限制。Bulkhead 表示，相关功能正在服务器后台逐步实施，但要达到预期效果，还需要进一步调整。Bulkhead 称，团队原本希望通过更宽松的跨地区匹配机制改善玩家的社交体验，但此前的做法未能达到预期，因此决定进一步收紧限制。工作室表示" data-title="《战狗》为打击作弊限制跨区匹配：游戏延迟超 175ms 则受限制，部分玩家威胁退款" data-date="10-22 20:41" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-22 20:41</span>
          <span class="news-item-title">《战狗》为打击作弊限制跨区匹配：游戏延迟超 175ms 则受限制，部分玩家威胁退款</span>
          <span class="news-value-point">💡 IT之家 10 月 22 日消息，前段时间爆火的第一人称射击游戏《战狗》（Wardogs）开发商 Bulkhead 正在逐步实施跨地区匹配限制，…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-22/10719324.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网成都10月22日电(祝欢)22日，“匠心织造·工装风尚”2026成都职工工装风尚T台秀正式开秀。劳模工匠、企业职工、行业代表穿上工装，依次走上红毯，工装不再是车间和柜面后的“制服背景”，而被放上主舞台中央。" data-title="从工作一线走上T台 2026成都职工工装风尚T台秀举行" data-date="10-22 20:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-22 20:33</span>
          <span class="news-item-title">从工作一线走上T台 2026成都职工工装风尚T台秀举行</span>
          <span class="news-value-point">💡 中新网成都10月22日电(祝欢)22日，“匠心织造·工装风尚”2026成都职工工装风尚T台秀正式开秀</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-22/10719307.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网沈阳10月22日电(杨茜茜)为纪念中国工农红军长征胜利90周年，传承弘扬伟大长征精神，走好新时代长征路，22日至25日，“伟大的征程 不朽的精神”辽宁省残疾人书画文创作品展在辽宁美术馆开展，以文艺力量展现残健同心、自强奋进的辽沈风貌。" data-title="走好新时代的长征路 辽宁省残疾人书画文创作品展启幕" data-date="10-22 20:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-22 20:31</span>
          <span class="news-item-title">走好新时代的长征路 辽宁省残疾人书画文创作品展启幕</span>
          <span class="news-value-point">💡 中新网沈阳10月22日电(杨茜茜)为纪念中国工农红军长征胜利90周年，传承弘扬伟大长征精神，走好新时代长征路，22日至25日，“伟大的征程 不朽…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/cyber-security/leaked-private-keys-for-eight-ca-certificates-let-any-attacker-impersonate-any-domain-billions-of-older-devices-and-software-installations-may-be-vulnerable-after-round-of-fixes-patch-yours-immediately" target="_blank" rel="noopener" data-cat="zonghe" data-summary="八个CA证书的私钥泄露让任何攻击者都可以模拟任何域—经过一轮修复后，数十亿台旧设备和软件安装可能容易受到攻击，请立即修补您的问题" data-title="Leaked private keys for eight CA certificates let any attacker impersonate any domain" data-date="10-22 20:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-22 20:30</span>
          <span class="news-item-title">泄露的八个CA证书的私钥让任何攻击者都可以模拟任何域</span>
          <span class="news-item-title-en">Leaked private keys for eight CA certificates let any attacker impersonate any domain</span>
          <span class="news-value-point">💡 八个CA证书的私钥泄露让任何攻击者都可以模拟任何域—经过一轮修复后，数十亿台旧设备和软件安装可能容易受到攻击，请立即修补您的问题</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/10/21/us/politics/judge-dhs-voter-fraud-elections.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这项裁决在很大程度上阻止了国土安全人员在包括加利福尼亚州在内的九个州进行实地采访，这是寻找登记投票的非公民的庞大努力的一部分。" data-title="Judge Restricts D.H.S. Field Operations Aimed at Unearthing Voter Fraud" data-date="10-22 20:06" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">10-22 20:06</span>
          <span class="news-item-title">法官限制针对发掘选民欺诈的DHS现场作业</span>
          <span class="news-item-title-en">Judge Restricts D.H.S. Field Operations Aimed at Unearthing Voter Fraud</span>
          <span class="news-value-point">💡 这项裁决在很大程度上阻止了国土安全人员在包括加利福尼亚州在内的九个州进行实地采访，这是寻找登记投票的非公民的庞大努力的一部分</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-22/10719294.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京10月22日电 (记者 孙自法)中国科技馆10月22日向媒体通报说，在纪念中国工农红军长征胜利90周年之际，该馆推出AI(人工智能)微短剧《1935年的来电，请接听》，剧情基于长征队伍中通信工作者的真实故事改编，讲述90年前烽火岁月中的技术探索与人物精神。" data-title="中国科技馆推出AI微短剧《1935年的来电，请接听》" data-date="10-22 19:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-22 19:48</span>
          <span class="news-item-title">中国科技馆推出AI微短剧《1935年的来电，请接听》</span>
          <span class="news-value-point">💡 中新网北京10月22日电 (记者 孙自法)中国科技馆10月22日向媒体通报说，在纪念中国工农红军长征胜利90周年之际，该馆推出AI(人工智能)微…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-22/10719288.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网哈尔滨10月22日电 (史轶夫 刘烨)10月25日起，全国民航将执行2026—2027年冬春航季航班计划。记者从黑龙江机场集团获悉，新航季，黑龙江机场集团每周计划执行航班4450架次，其中哈尔滨机场每周计划执行航班3510架次，航线网络结构进一步优化，航班密度稳步提升。" data-title="2026—2027冬春航季将至 黑龙江干支联动护航冰雪旅游客流" data-date="10-22 19:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-22 19:41</span>
          <span class="news-item-title">2026—2027冬春航季将至 黑龙江干支联动护航冰雪旅游客流</span>
          <span class="news-value-point">💡 中新网哈尔滨10月22日电 (史轶夫 刘烨)10月25日起，全国民航将执行2026—2027年冬春航季航班计划</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-22/10719286.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网兰州10月22日电 (刘薛梅)在语言不通、民俗各异的环境下，怎样把消防宣传做到牧区群众心里，并收获群众认可与信任？甘肃省武威市天祝藏族自治县消防救援大队“消防娘子军”打造《格桑话消防》汉藏双语科普短视频，探索推行“阵地＋场景＋双语”的宣传模式，得到牧区群众的认可。" data-title="雪域高原“格桑”话消防" data-date="10-22 19:38" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-22 19:38</span>
          <span class="news-item-title">雪域高原“格桑”话消防</span>
          <span class="news-value-point">💡 中新网兰州10月22日电 (刘薛梅)在语言不通、民俗各异的环境下，怎样把消防宣传做到牧区群众心里，并收获群众认可与信任</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-22 21:05（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
