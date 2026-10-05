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
      <span>2026-10-05 14:14 抓取更新</span>
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
        <span class="channel-count">41</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('shizheng', this)">
        <span>🏛️ 时政与国际</span>
        <span class="channel-count">15</span>
      </button>
      <button class="channel-btn" onclick="filterNewsChannel('keji', this)">
        <span>🤖 AI模型 & 芯片算力</span>
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
  <div class="ov-item"><span class="ov-num">41</span><span class="ov-label">今日动态</span></div>
  <div class="ov-item"><span class="ov-num">6</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×20 · IT之家×8</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gj/2026/10-04/10707996.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社加德满都10月4日电 (记者 崔楠)由中国地质大学(北京)牵头、尼泊尔科学院协同组建的中尼地质灾害应急跨境科学考察队中方成员10月4日抵达尼泊尔首都加德满都，将与尼方科研人员共同在尼开展为期约20天的跨境冰冻圈与岩石圈巨灾应急联合科考。" data-title="中尼科学家开展跨境巨灾应急联合科考" data-date="10-04 23:40" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 10-04 23:40</span>
      </div>
      <h2 class="hero-featured-title">中尼科学家开展跨境巨灾应急联合科考</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.theverge.com/ai-artificial-intelligence/1004549/well-if-ai-said-it-it-must-be-true" target="_blank" rel="noopener" data-cat="keji" data-summary="新泽西州副州长戴尔·考德威尔（ Dale Caldwell ）在调查发现他对一名工作人员进行了性骚扰并一再违反道德规则后，于9月25日被迫辞职。现任前任副州长一直在媒体上巡回报道" data-title="NJ’s lieutenant governor told PBS, AI says he didn’t commit sexual harassment" data-date="10-05 00:16" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">NJ’s lieutenant governor told PBS, AI says he didn’t commit sexual harassment</p>
    </a>
    <a class="hero-sub-card" href="https://www.theverge.com/gadgets/1004360/this-toolless-modular-lever-action-wallet-is-the-coolest-ive-stuck-to-my-phone" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这款无工具模块化杠杆式钱包是我手机上最酷的。还记得我测试过超薄和方便的OhSnap按扣支架，非常喜欢它，我自己买的吗？现在， OhSnap有一个磁力杠杆动作卡片钱包，" data-title="This toolless modular lever-action wallet is the coolest I’ve stuck to my phone" data-date="10-04 23:00" data-source="The Verge">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-theverge">🌐 The Verge</span>
      </div>
      <p class="hero-sub-title">This toolless modular lever-action wallet is the coolest I’ve stuck to my phone</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/gj/2026/10-04/10707993.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="围绕驻日美军涉嫌杀人案，日本政府4日向美国提出抗议。事发地冲绳民众发出愤怒声音，认为美军基地的存在与日本政府的不作为导致类似犯罪事件不断发生。" data-title="冲绳民众就驻日美军涉嫌杀人案发出愤怒声音" data-date="10-04 22:57" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">冲绳民众就驻日美军涉嫌杀人案发出愤怒声音</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/009/736.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 4 日消息，据 tomshardware 今日报道，一家机器人格斗公司在旧金山举办了一场人机格斗赛后，收到了加州政府发来的停止侵权禁令。加州州立体育委员会（CSAC）要求该公司停止举办、宣传或赞助这类未经审批的格斗赛事，并称在未取得许可的情况下组织此类活动属于轻罪。IT之家从报道获悉，这份停止令针对的是该公司在 2026 年 9 月 18 日赞助的一场人形机器人笼斗赛。油管博主弗兰基・拉彭纳（Frankie LaPenna）进入格斗笼，先后与三台不同的机器人对战。目前尚不清楚这场活动究竟属于体育竞赛还是营销噱头，但很明显，它是用来为 REK 机器人格斗平台博取更多关注度的。报道提到，历史上曾发生机器人致人死亡事件，1979 年的今天，美国工厂工人罗伯特・威廉姆斯成为首位死" data-title="机器人格斗公司 REK 举办真人与机器人笼斗赛被叫停：未取得许可组织活动" data-date="10-04 23:22" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">机器人格斗公司 REK 举办真人与机器人笼斗赛被叫停：未取得许可组织活动</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/009/733.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 4 日消息，据交通运输部动态研判，10 月 5 日，全国高速公路预计有 30 个服务区充电特别繁忙，主要集中在河北、湖南、山西等省份，大家可通过“e 路畅通”微信小程序查询服务区充电桩运行状态。IT之家整理如下：序号省份所在城市服务区名称编号方向1河北唐山市唐海服务区G0111天津-沈阳2河北唐山市唐海服务区G0111沈阳-天津3河北唐山市唐山服务区S0105唐山-天津4河北唐山市乐亭服务区G0111秦皇岛-天津5河北唐山市乐亭服务区G0111天津-秦皇岛6河北秦皇岛市昌黎服务区G0111天津-秦皇岛7河北秦皇岛市抚宁服务区G0111沈阳-天津8河北秦皇岛市抚宁服务区G0111天津-沈阳9河北秦皇岛市昌黎服务区G0111秦皇岛-天津10河北沧州市东光服务区G3台北-北京1" data-title="10 月 5 日高速服务区充电特别繁忙清单公布，主要集中河北、湖南、山西等省份" data-date="10-04 22:48" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">10 月 5 日高速服务区充电特别繁忙清单公布，主要集中河北、湖南、山西等省份</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707996.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社加德满都10月4日电 (记者 崔楠)由中国地质大学(北京)牵头、尼泊尔科学院协同组建的中尼地质灾害应急跨境科学考察队中方成员10月4日抵达尼泊尔首都加德满都，将与尼方科研人员共同在尼开展为期约20天的跨境冰冻圈与岩石圈巨灾应急联合科考。" data-title="中尼科学家开展跨境巨灾应急联合科考" data-date="10-04 23:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 23:40</span>
          <span class="news-item-title">中尼科学家开展跨境巨灾应急联合科考</span>
          <span class="news-value-point">💡 中新社加德满都10月4日电 (记者 崔楠)由中国地质大学(北京)牵头、尼泊尔科学院协同组建的中尼地质灾害应急跨境科学考察队中方成员10月4日抵达…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707993.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="围绕驻日美军涉嫌杀人案，日本政府4日向美国提出抗议。事发地冲绳民众发出愤怒声音，认为美军基地的存在与日本政府的不作为导致类似犯罪事件不断发生。" data-title="冲绳民众就驻日美军涉嫌杀人案发出愤怒声音" data-date="10-04 22:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 22:57</span>
          <span class="news-item-title">冲绳民众就驻日美军涉嫌杀人案发出愤怒声音</span>
          <span class="news-value-point">💡 围绕驻日美军涉嫌杀人案，日本政府4日向美国提出抗议</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707982.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京10月4日电 德黑兰消息：伊朗伊斯兰议会议长、外交部长、军方高级指挥官等4日分别发表讲话，强调美方言论和“认知战”不会影响伊方立场，伊朗同时准备好“谈判和战斗”，在条件得到满足前，不会重新开放霍尔木兹海峡。" data-title="伊朗强调同时准备“谈判和战斗”" data-date="10-04 22:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 22:55</span>
          <span class="news-item-title">伊朗强调同时准备“谈判和战斗”</span>
          <span class="news-value-point">💡 中新社北京10月4日电 德黑兰消息：伊朗伊斯兰议会议长、外交部长、军方高级指挥官等4日分别发表讲话，强调美方言论和“认知战”不会影响伊方立场，伊…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707991.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间10月4日，美国总统特朗普在社交媒体平台“真实社交”发文宣布，提名约翰·科尔(John Coale)担任美国总统人质事务特使。" data-title="特朗普提名约翰·科尔为美总统人质事务特使" data-date="10-04 22:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 22:54</span>
          <span class="news-item-title">特朗普提名约翰·科尔为美总统人质事务特使</span>
          <span class="news-value-point">💡 当地时间10月4日，美国总统特朗普在社交媒体平台“真实社交”发文宣布，提名约翰·科尔(John Coale)担任美国总统人质事务特使</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707989.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="据伊朗方面4日消息，伊朗军方发言人阿克拉米尼亚说，伊朗军方已决定着手提升其导弹射程。" data-title="伊朗军方称将提升导弹射程" data-date="10-04 22:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 22:49</span>
          <span class="news-item-title">伊朗军方称将提升导弹射程</span>
          <span class="news-value-point">💡 据伊朗方面4日消息，伊朗军方发言人阿克拉米尼亚说，伊朗军方已决定着手提升其导弹射程</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707988.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间10月4日，联合国世界粮食计划署发布声明称，两辆隶属于该机构的卡车3日在苏丹南部南科尔多凡州遭到袭击，造成1名卡车司机遇难。" data-title="联合国人道主义车队在苏丹南部遇袭 1名司机遇难" data-date="10-04 22:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 22:39</span>
          <span class="news-item-title">联合国人道主义车队在苏丹南部遇袭 1名司机遇难</span>
          <span class="news-value-point">💡 当地时间10月4日，联合国世界粮食计划署发布声明称，两辆隶属于该机构的卡车3日在苏丹南部南科尔多凡州遭到袭击，造成1名卡车司机遇难</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707977.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社阿斯塔纳10月4日电 记者手记丨在中亚国家感受“中文热”" data-title="记者手记丨在中亚国家感受“中文热”" data-date="10-04 21:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 21:24</span>
          <span class="news-item-title">记者手记丨在中亚国家感受“中文热”</span>
          <span class="news-value-point">💡 新华社阿斯塔纳10月4日电 记者手记丨在中亚国家感受“中文热”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707976.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中国在科技领域取得的进展正受到越来越多外媒的关注。印度《德干先驱报》网站10月4日刊文称，凭借制造能力和国家支持，中国正在打造科技强国，科技的主导地位日益上升。" data-title="全球媒体聚焦 | 印度媒体：中国正在打造科技强国" data-date="10-04 21:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 21:21</span>
          <span class="news-item-title">全球媒体聚焦 | 印度媒体：中国正在打造科技强国</span>
          <span class="news-value-point">💡 中国在科技领域取得的进展正受到越来越多外媒的关注</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707970.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="原标题：永不磨灭的印记 | 一张借谷证：见证红色政权的铮铮诺言" data-title="一张借谷证：见证红色政权的铮铮诺言" data-date="10-04 21:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 21:05</span>
          <span class="news-item-title">一张借谷证：见证红色政权的铮铮诺言</span>
          <span class="news-value-point">💡 原标题：永不磨灭的印记 | 一张借谷证：见证红色政权的铮铮诺言</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707941.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社伦敦10月4日电 (记者 欧阳开宇)英国政府4日发布消息称，英国皇家刑事法院待审积压案件创下历史新高，总量约8.1万宗，其中近三分之一案件等待审理时长超过一年。" data-title="英皇家刑事法院积压案件约8.1万宗" data-date="10-04 20:55" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 20:55</span>
          <span class="news-item-title">英皇家刑事法院积压案件约8.1万宗</span>
          <span class="news-value-point">💡 中新社伦敦10月4日电 (记者 欧阳开宇)英国政府4日发布消息称，英国皇家刑事法院待审积压案件创下历史新高，总量约8.1万宗，其中近三分之一案件…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707956.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="视频：听英雄后代讲长征故事丨开国上将朱良才之子讲述长征路上的鱼水深情来源：新华网" data-title="听英雄后代讲长征故事丨开国上将朱良才之子讲述长征路上的鱼水深情" data-date="10-04 20:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 20:48</span>
          <span class="news-item-title">听英雄后代讲长征故事丨开国上将朱良才之子讲述长征路上的鱼水深情</span>
          <span class="news-value-point">💡 视频：听英雄后代讲长征故事丨开国上将朱良才之子讲述长征路上的鱼水深情来源：新华网</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707899.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="爱国主义是中华民族精神的核心，是中国人民和中华民族同心同德、自强不息的精神纽带。党的十八大以来，习近平总书记在不同场合发表一系列重要讲话，生动阐述爱国主义的丰富内涵。一起学习感悟。" data-title="学习新语·家国同心｜怀爱国之心 立报国之志" data-date="10-04 20:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 20:28</span>
          <span class="news-item-title">学习新语·家国同心｜怀爱国之心 立报国之志</span>
          <span class="news-value-point">💡 爱国主义是中华民族精神的核心，是中国人民和中华民族同心同德、自强不息的精神纽带</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cr89zllz31wdo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="加拿大总理马克‧卡尼表示，军方正在制定应对方案，以防美国入侵加拿大这种不太可能发生的情况。" data-title="加拿大为何要为（概率极小的）美国入侵做准备" data-date="10-04 19:51" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">10-04 19:51</span>
          <span class="news-item-title">加拿大为何要为（概率极小的）美国入侵做准备</span>
          <span class="news-value-point">💡 加拿大总理马克‧卡尼表示，军方正在制定应对方案，以防美国入侵加拿大这种不太可能发生的情况</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707894.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="今天(10月4日)，我国喜马拉雅“8·26”极端地质灾害应急跨境科学考察队从成都启程赴尼泊尔，开展冰冻圈与岩石圈巨灾应急联合科考。本次科考共有十余家高校与科研院所50余名科研人员参加。" data-title="我国科学家赴尼泊尔开展联合科考 研判喜马拉雅冰冻灾害" data-date="10-04 18:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 18:52</span>
          <span class="news-item-title">我国科学家赴尼泊尔开展联合科考 研判喜马拉雅冰冻灾害</span>
          <span class="news-value-point">💡 今天(10月4日)，我国喜马拉雅“8·26”极端地质灾害应急跨境科学考察队从成都启程赴尼泊尔，开展冰冻圈与岩石圈巨灾应急联合科考</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/10-04/10707880.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="视频：跟着课本走长征丨90多年前，他们爬过这座老山界来源：新华社" data-title="跟着课本走长征丨90多年前，他们爬过这座老山界" data-date="10-04 18:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 18:04</span>
          <span class="news-item-title">跟着课本走长征丨90多年前，他们爬过这座老山界</span>
          <span class="news-value-point">💡 视频：跟着课本走长征丨90多年前，他们爬过这座老山界来源：新华社</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">11 条</span>
    </div>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1004549/well-if-ai-said-it-it-must-be-true" target="_blank" rel="noopener" data-cat="keji" data-summary="新泽西州副州长戴尔·考德威尔（ Dale Caldwell ）在调查发现他对一名工作人员进行了性骚扰并一再违反道德规则后，于9月25日被迫辞职。现任前任副州长一直在媒体上巡回报道" data-title="NJ’s lieutenant governor told PBS, AI says he didn’t commit sexual harassment" data-date="10-05 00:16" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-05 00:16</span>
          <span class="news-item-title">新泽西州副州长告诉PBS ， AI说他没有犯下性骚扰</span>
          <span class="news-item-title-en">NJ’s lieutenant governor told PBS, AI says he didn’t commit sexual harassment</span>
          <span class="news-value-point">💡 新泽西州副州长戴尔·考德威尔（ Dale Caldwell ）在调查发现他对一名工作人员进行了性骚扰并一再违反道德规则后，于9月25日被迫辞职</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/736.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 4 日消息，据 tomshardware 今日报道，一家机器人格斗公司在旧金山举办了一场人机格斗赛后，收到了加州政府发来的停止侵权禁令。加州州立体育委员会（CSAC）要求该公司停止举办、宣传或赞助这类未经审批的格斗赛事，并称在未取得许可的情况下组织此类活动属于轻罪。IT之家从报道获悉，这份停止令针对的是该公司在 2026 年 9 月 18 日赞助的一场人形机器人笼斗赛。油管博主弗兰基・拉彭纳（Frankie LaPenna）进入格斗笼，先后与三台不同的机器人对战。目前尚不清楚这场活动究竟属于体育竞赛还是营销噱头，但很明显，它是用来为 REK 机器人格斗平台博取更多关注度的。报道提到，历史上曾发生机器人致人死亡事件，1979 年的今天，美国工厂工人罗伯特・威廉姆斯成为首位死" data-title="机器人格斗公司 REK 举办真人与机器人笼斗赛被叫停：未取得许可组织活动" data-date="10-04 23:22" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-04 23:22</span>
          <span class="news-item-title">机器人格斗公司 REK 举办真人与机器人笼斗赛被叫停：未取得许可组织活动</span>
          <span class="news-value-point">💡 IT之家 10 月 4 日消息，据 tomshardware 今日报道，一家机器人格斗公司在旧金山举办了一场人机格斗赛后，收到了加州政府发来的停…</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1004543/openai-gpt-cheat-starcraft" target="_blank" rel="noopener" data-cat="keji" data-summary="StarSkirmish让人工智能制作的《星际争霸》游戏机器人相互对抗，也与人造机器人对抗。OpenAI的GPT-6 Astra和Claude Opus 5.5基本上并列为表现最好的人工智能机器人，但他们无法超越最高速的星尘" data-title="An AI couldn’t beat humans at StarCraft, so it decided to cheat" data-date="10-04 23:21" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-04 23:21</span>
          <span class="news-item-title">在《星际争霸》中，人工智能无法击败人类，所以它决定作弊</span>
          <span class="news-item-title-en">An AI couldn’t beat humans at StarCraft, so it decided to cheat</span>
          <span class="news-value-point">💡 StarSkirmish让人工智能制作的《星际争霸》游戏机器人相互对抗，也与人造机器人对抗</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/10/04/trump-unveils-his-new-super-intelligence-force/" target="_blank" rel="noopener" data-cat="keji" data-summary="这个新的工作组是特朗普对人工智能安全辩论的最新回应。" data-title="Trump unveils his new Super Intelligence Force" data-date="10-04 23:15" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">10-04 23:15</span>
          <span class="news-item-title">特朗普推出他的新超级情报部队</span>
          <span class="news-item-title-en">Trump unveils his new Super Intelligence Force</span>
          <span class="news-value-point">💡 这个新的工作组是特朗普对人工智能安全辩论的最新回应</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/734.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 10 月 4 日消息，据外媒 The Verge 报道，微软正在推行一项名为“仿生”（Biomimicry）的计划，该公司正重新规划旗下 20 多个数据中心周边土地，陆续恢复原先湿地生态、种植本土植物，希望让数据中心更好地融入当地环境。微软透露，后续微软在美国境内所有新建项目都将采用这一方式，在项目建设过程中，微软会收集当地社区意见，并通过生态研究了解项目所在地的环境状况。微软团队还将使用一款名为“Ecosystem Intelligence”的工具，对项目地点的水质、生物多样性、噪音控制等多个指标进行评估。不过，随着 AI 数据中心持续扩张，微软仍面临来自当地社区和环保组织的压力。当前微软真正的考验在于公司应当如何计算、跟踪并让当地社区相信这些生态修复措施所带来的实际收益。只有建" data-title="消息称微软为 20 多个数据中心建设项目引入“仿生”计划：修复湿地生态、种植本土植物以降低环境影响" data-date="10-04 22:59" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-04 22:59</span>
          <span class="news-item-title">消息称微软为 20 多个数据中心建设项目引入“仿生”计划：修复湿地生态、种植本土植物以降低环境影响</span>
          <span class="news-value-point">💡 IT之家 10 月 4 日消息，据外媒 The Verge 报道，微软正在推行一项名为“仿生”（Biomimicry）的计划，该公司正重新规划旗…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/modder-fixes-melting-rtx-5090-power-connectors-with-custom-distributor-dual-8-pin-mod-peaks-at-just-40c-during-a-48-hour-550w-stress-test" target="_blank" rel="noopener" data-cat="keji" data-summary="Reddit用户u/DallasGrave分享了他的RTX 5090的修复程序，这是最好的显卡之一，其12VHPWR连接器过热，以及拧在GPU背面的模块图像。" data-title="Modder &#39;fixes&#39; melting RTX 5090 power connectors with custom distributor" data-date="10-04 22:50" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-04 22:50</span>
          <span class="news-item-title">Modder “修复”熔化RTX 5090电源连接器与定制分销商</span>
          <span class="news-item-title-en">Modder 'fixes' melting RTX 5090 power connectors with custom distributor</span>
          <span class="news-value-point">💡 Reddit用户u/DallasGrave分享了他的RTX 5090的修复程序，这是最好的显卡之一，其12VHPWR连接器过热，以及拧在GPU背…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/robotics/robotics-startup-has-real-human-vs-robot-cage-match-california-responds-with-cease-and-desist-order-regulator-threatens-misdemeanor-charges-after-youtuber-fights-three-robotic-humanoids" target="_blank" rel="noopener" data-cat="keji" data-summary="当加利福尼亚州体育委员会看到一名人类在战斗环内与一名人形机器人对峙时，它进行了干预。" data-title="Robotics startup has real human vs. robot cage match, California responds with cease" data-date="10-04 22:36" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-04 22:36</span>
          <span class="news-item-title">机器人初创公司拥有真正的人类与机器人笼匹配，加利福尼亚州以停止回应</span>
          <span class="news-item-title-en">Robotics startup has real human vs. robot cage match, California responds with cease</span>
          <span class="news-value-point">💡 当加利福尼亚州体育委员会看到一名人类在战斗环内与一名人形机器人对峙时，它进行了干预</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/10-04/10707987.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="当地时间10月4日，美国总统特朗普宣布成立“超级智能特别工作组”(Super Intelligence Force，SIF)，负责协调美国联邦政府在超级智能领域的相关工作。" data-title="特朗普宣布成立“超级智能特别工作组”" data-date="10-04 22:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 22:35</span>
          <span class="news-item-title">特朗普宣布成立“超级智能特别工作组”</span>
          <span class="news-value-point">💡 当地时间10月4日，美国总统特朗普宣布成立“超级智能特别工作组”(Super Intelligence Force，SIF)，负责协调美国联邦政…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpu-drivers/modder-brings-nvidia-pascal-gpu-support-to-windows-xp-32-bit-modded-drivers-unlock-better-displayport-and-hdmi-support-for-modern-monitors" target="_blank" rel="noopener" data-cat="keji" data-summary="Retro techie改装Nvidia Windows XP 32位驱动程序，支持Pascal卡，并改进了对当代显示器的DisplayPort和HDMI支持" data-title="Modder brings Nvidia Pascal GPU support to Windows XP 32" data-date="10-04 22:25" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-04 22:25</span>
          <span class="news-item-title">Modder为Windows XP 32带来Nvidia Pascal GPU支持</span>
          <span class="news-item-title-en">Modder brings Nvidia Pascal GPU support to Windows XP 32</span>
          <span class="news-value-point">💡 Retro techie改装Nvidia Windows XP 32位驱动程序，支持Pascal卡，并改进了对当代显示器的DisplayPort…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/robotics/ai-robot-company-decommissioned-its-robots-terminator-style-in-a-75-ton-vat-of-molten-steel-arnold-schwarzenegger-suggested-melting-them-one-robot-held-up-a-thumbs-up-sign-as-it-sank-into-molten-metal" target="_blank" rel="noopener" data-cat="keji" data-summary="人工智能机器人公司Figure找到了一种创新的方法，可以将其旧的F.02机队退役，而无需分配资源进行困难而耗时的拆卸。" data-title="AI robot company decommissioned its robots ‘Terminator-style’ in a 75-ton vat of molten steel" data-date="10-04 21:20" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-04 21:20</span>
          <span class="news-item-title">人工智能机器人公司在75吨钢水桶中退役其机器人“终结者式”</span>
          <span class="news-item-title-en">AI robot company decommissioned its robots ‘Terminator-style’ in a 75-ton vat of molten steel</span>
          <span class="news-value-point">💡 人工智能机器人公司Figure找到了一种创新的方法，可以将其旧的F.02机队退役，而无需分配资源进行困难而耗时的拆卸</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/chatgpt-6-astra-cracks-217-year-old-napoleonic-code-in-just-six-hours-single-prompt-ai-run-solves-24-rows-of-custom-symbols-from-a-single-image-reveals-lost-troop-orders" target="_blank" rel="noopener" data-cat="keji" data-summary="一位人工智能工程师使用GPT-6 Astra揭示了自拿破仑战争以来从未被读取的密码的内容。这项任务是用一张图片和提示发起的，从开始到结束只花了六个小时。" data-title="ChatGPT-6 Astra cracks 217-year-old Napoleonic code in just six hours" data-date="10-04 21:08" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-04 21:08</span>
          <span class="news-item-title">ChatGPT-6 Astra在短短六小时内破解了217年前的拿破仑密码</span>
          <span class="news-item-title-en">ChatGPT-6 Astra cracks 217-year-old Napoleonic code in just six hours</span>
          <span class="news-value-point">💡 一位人工智能工程师使用GPT-6 Astra揭示了自拿破仑战争以来从未被读取的密码的内容</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theverge.com/gadgets/1004360/this-toolless-modular-lever-action-wallet-is-the-coolest-ive-stuck-to-my-phone" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这款无工具模块化杠杆式钱包是我手机上最酷的。还记得我测试过超薄和方便的OhSnap按扣支架，非常喜欢它，我自己买的吗？现在， OhSnap有一个磁力杠杆动作卡片钱包，" data-title="This toolless modular lever-action wallet is the coolest I’ve stuck to my phone" data-date="10-04 23:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-04 23:00</span>
          <span class="news-item-title">这款免工具模块化杠杆式钱包是我手机上最酷的</span>
          <span class="news-item-title-en">This toolless modular lever-action wallet is the coolest I’ve stuck to my phone</span>
          <span class="news-value-point">💡 这款无工具模块化杠杆式钱包是我手机上最酷的</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/733.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 4 日消息，据交通运输部动态研判，10 月 5 日，全国高速公路预计有 30 个服务区充电特别繁忙，主要集中在河北、湖南、山西等省份，大家可通过“e 路畅通”微信小程序查询服务区充电桩运行状态。IT之家整理如下：序号省份所在城市服务区名称编号方向1河北唐山市唐海服务区G0111天津-沈阳2河北唐山市唐海服务区G0111沈阳-天津3河北唐山市唐山服务区S0105唐山-天津4河北唐山市乐亭服务区G0111秦皇岛-天津5河北唐山市乐亭服务区G0111天津-秦皇岛6河北秦皇岛市昌黎服务区G0111天津-秦皇岛7河北秦皇岛市抚宁服务区G0111沈阳-天津8河北秦皇岛市抚宁服务区G0111天津-沈阳9河北秦皇岛市昌黎服务区G0111秦皇岛-天津10河北沧州市东光服务区G3台北-北京1" data-title="10 月 5 日高速服务区充电特别繁忙清单公布，主要集中河北、湖南、山西等省份" data-date="10-04 22:48" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-04 22:48</span>
          <span class="news-item-title">10 月 5 日高速服务区充电特别繁忙清单公布，主要集中河北、湖南、山西等省份</span>
          <span class="news-value-point">💡 IT之家 10 月 4 日消息，据交通运输部动态研判，10 月 5 日，全国高速公路预计有 30 个服务区充电特别繁忙，主要集中在河北、湖南、山…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707986.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="正值国庆假期，各地迎来消费高峰。在线上线下购物时，您是否遇到过，货不对板、实物和宣传存在明显差距、虚假宣传等问题呢？假日外出聚餐，您是否遇到过包间设置最低消费？在结账时，凭空多出来没有提前告知的服务费，要不要接受呢？节假日如果商家只允许购买套餐、不能单点菜品，又该怎么办？遭遇霸王条款，我们该如何维权呢？" data-title="假期提示：遭遇霸王条款和消费陷阱 如何维权？" data-date="10-04 22:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 22:33</span>
          <span class="news-item-title">假期提示：遭遇霸王条款和消费陷阱 如何维权？</span>
          <span class="news-value-point">💡 正值国庆假期，各地迎来消费高峰</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/732.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 4 日消息，《生化危机：爆发夜》游改真人电影将于明日在中国内地上映，该电影将以 CINITY、IMAX、中国巨幕、4DX、SCREENX 多制式上映，让影迷感受扑面而来的惊悚感。值得一提的是，这也是《生化危机》系列时隔九年，重返内地大银幕。IT之家附该电影官方简介如下：嘘，别出声。黑暗中的生化怪物正在凝视，楼顶上的嗜血异种们虎视眈眈。城市变为血色废墟，危险即将全面爆发！检查好手中的武器，抱紧需要运送的快递。前方高能，浣熊市的求生副本即将开启，请做好逃离准备。据介绍，本片根据热门恐怖游戏《生化危机》改编，这也是该 IP 的最新一部院线电影，由《凶器》《野蛮人》导演扎克・克雷格倾力打造，奥斯汀 · 艾布拉姆斯、保罗 · 沃尔特 · 豪泽、扎克 · 切利、卡莉 · 瑞斯参与主演" data-title="时隔九年重返内地大银幕，《生化危机：爆发夜》游改真人电影明日上映" data-date="10-04 22:26" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-04 22:26</span>
          <span class="news-item-title">时隔九年重返内地大银幕，《生化危机：爆发夜》游改真人电影明日上映</span>
          <span class="news-value-point">💡 IT之家 10 月 4 日消息，《生化危机：爆发夜》游改真人电影将于明日在中国内地上映，该电影将以 CINITY、IMAX、中国巨幕、4DX、S…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707985.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="每逢长假，身边的人大抵分成两种状态：" data-title="好了好了这下坏了！别人都活力四射，只有我在倒立玩手机，这假白放了......" data-date="10-04 22:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 22:17</span>
          <span class="news-item-title">好了好了这下坏了！别人都活力四射，只有我在倒立玩手机，这假白放了......</span>
          <span class="news-value-point">💡 每逢长假，身边的人大抵分成两种状态：</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/pc-gaming/database-expert-runs-doom-in-sql-with-just-5-900-lines-of-code-1-300-line-graphical-renderer-spans-89-different-tables-full-featured-sqldoom-is-the-sequel-to-embryonic-doomql" target="_blank" rel="noopener" data-cat="zonghe" data-summary="数据库专家再次在SQL中运行Doom —功能齐全的SQLDoom是胚胎DoomQL的续集" data-title="Database expert runs Doom in SQL with just 5,900 lines of code" data-date="10-04 22:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-04 22:00</span>
          <span class="news-item-title">数据库专家在SQL中运行Doom ，仅需5,900行代码</span>
          <span class="news-item-title-en">Database expert runs Doom in SQL with just 5,900 lines of code</span>
          <span class="news-value-point">💡 数据库专家再次在SQL中运行Doom —功能齐全的SQLDoom是胚胎DoomQL的续集</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/731.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 4 日消息，海南商发 10 月 1 日官宣，海南商业航天发射场二期项目以崭新姿态震撼亮相，该项目已基本建成并正式进入全系统合练阶段。IT之家注意到，海南商业航天发射场是中国首个专业化商业航天发射基地，位于海南省文昌市东郊镇，由海南国际商业航天发射有限公司建设运营。该项目于 2022 年 7 月 6 日正式开工。2024 年 6 月建成国内首个液体通用型发射工位并具备执行发射能力。同年 11 月 30 日首次发射长征十二号火箭圆满成功。2025 年 3 月 12 日实现双工位发射能力。海南商业航天发射场二期项目是位于海南省文昌市东郊镇的商业航天发射场扩建工程，毗邻一期工程。该项目于 2025 年 1 月 25 日正式开工，计划工期约 730 天，主要建设三号、四号发射工位，" data-title="海南商发二期项目已基本建成，再添三号、四号两个发射工位" data-date="10-04 21:42" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-04 21:42</span>
          <span class="news-item-title">海南商发二期项目已基本建成，再添三号、四号两个发射工位</span>
          <span class="news-value-point">💡 IT之家 10 月 4 日消息，海南商发 10 月 1 日官宣，海南商业航天发射场二期项目以崭新姿态震撼亮相，该项目已基本建成并正式进入全系统合…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/drones/us-army-unit-deploys-drone-assembled-completely-in-house-uses-3d-printed-dragoon-bombs-with-ball-bearing-shrapnel-device-has-a-range-of-up-to-12-miles-and-can-be-configured-for-anti-personnel-and-anti-light-armor-missions" target="_blank" rel="noopener" data-cat="zonghe" data-summary="美国陆军士兵正在接受组装无人机和3D打印炸弹外壳的训练，以供野外使用。" data-title="US Army unit deploys drone assembled completely in-house, uses 3D-printed &#39;Dragoon Bombs&#39; with ball bearing shrapnel" data-date="10-04 21:40" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">10-04 21:40</span>
          <span class="news-item-title">美国陆军部队部署完全由内部组装的无人机，使用带有球轴承弹片的3D打印“龙骑兵炸弹”</span>
          <span class="news-item-title-en">US Army unit deploys drone assembled completely in-house, uses 3D-printed 'Dragoon Bombs' with ball bearing shrapnel</span>
          <span class="news-value-point">💡 美国陆军士兵正在接受组装无人机和3D打印炸弹外壳的训练，以供野外使用</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/730.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 4 日消息，据央视新闻报道，近期市面上出现一种“ETC 异常”短信骗局，相应短信谎称汽车 ETC“被停用”“更新升级”“认证失效”，要求车主点击所谓链接处理。央视新闻表示，相应短信系陷阱。这种不明链接往往是骗子专门设置的钓鱼网站，为的就是骗取银行卡号、密码、身份证号等个人信息。如果车主对车辆 ETC 存在疑问，可打开“交管 12123”App，或者拨打 ETC 官方客服电话查询，全国统一的 ETC 服务热线号码为 95022。在扣费方式上，常见的 ETC 记账卡会与银行借记卡或对公账户绑定，通行时直接从银行卡或账户扣除通行费，因此车主也可通过银行官方手机银行 App 等正规渠道核对 ETC 通行记录与账单。延伸阅读ETC 全称“电子不停车收费系统”，是一种通过安装在车辆上" data-title="央视曝光车辆“ETC 异常”短信骗局：系不法分子钓鱼陷阱" data-date="10-04 21:34" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-04 21:34</span>
          <span class="news-item-title">央视曝光车辆“ETC 异常”短信骗局：系不法分子钓鱼陷阱</span>
          <span class="news-value-point">💡 IT之家 10 月 4 日消息，据央视新闻报道，近期市面上出现一种“ETC 异常”短信骗局，相应短信谎称汽车 ETC“被停用”“更新升级”“认证…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/729.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 4 日消息，荣耀平板 X10 Mini 现已在京东平台上架并预约，将于 10 月 23 日 10:00 发售。IT之家从官方海报获悉，这款新品配备 9.7 英寸 2K 护眼屏，内置 8000mAh 大电池，获得 SGS 抗摔抗压五星金标认证。作为参考，今年 3 月发布的荣耀平板 X10 搭载高通骁龙 680 处理器，首发价 1299 元起。该产品配备 11 英寸 LCD 护眼屏，内置 10100mAh 电池，前后均配备 500 万像素摄像头，标配 15W 充电器。" data-title="荣耀平板 X10 Mini 上架：9.7 英寸护眼屏，10 月 23 日发售" data-date="10-04 21:31" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-04 21:31</span>
          <span class="news-item-title">荣耀平板 X10 Mini 上架：9.7 英寸护眼屏，10 月 23 日发售</span>
          <span class="news-value-point">💡 IT之家 10 月 4 日消息，荣耀平板 X10 Mini 现已在京东平台上架并预约，将于 10 月 23 日 10:00 发售</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/009/728.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 10 月 4 日消息，近期网络上流传一段所谓“乐山大佛开展养护作业”短视频，其中显示文保工人正在给大佛“掏耳朵”，佛耳里掏出鸽子和腐叶，鼻孔里清理出大量腐叶等物质，旁边还有一只猴子在佛身上上蹿下跳，猴子还抢工人的安全帽戴在自己头上。对此，乐山大佛文物保护（景区）管委会回应媒体“四川观察”，称相应视频不实，系他人 AI 生成，不是乐山大佛景区里的真实场景。希望广大网友不信谣、不传谣。乐山大佛文物保护（景区）管委会数字化信息中心副主任陈芮透露，“2026 年以来乐山大佛总计开展 5 次保养维护，其中第 5 次是 9 月 20 日至 25 日，主要内容包含岩体表面微损伤修复、微生物清理、表层植被清除等，与视频内容无关。同时，大佛耳鼻内并无杂物需要清理，乐山大佛所在的凌云山片区目前没有猴子" data-title="乐山大佛景区回应网传“掏耳朵”养护作业视频：系 AI 合成，佛耳内并无所谓“杂物”" data-date="10-04 21:20" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">10-04 21:20</span>
          <span class="news-item-title">乐山大佛景区回应网传“掏耳朵”养护作业视频：系 AI 合成，佛耳内并无所谓“杂物”</span>
          <span class="news-value-point">💡 IT之家 10 月 4 日消息，近期网络上流传一段所谓“乐山大佛开展养护作业”短视频，其中显示文保工人正在给大佛“掏耳朵”，佛耳里掏出鸽子和腐叶…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707973.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="新华社重庆10月3日电 题：重庆：焕新历史街巷唤醒城市记忆" data-title="重庆：焕新历史街巷唤醒城市记忆" data-date="10-04 21:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 21:10</span>
          <span class="news-item-title">重庆：焕新历史街巷唤醒城市记忆</span>
          <span class="news-value-point">💡 新华社重庆10月3日电 题：重庆：焕新历史街巷唤醒城市记忆</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707971.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网三亚10月4日电 (张月和)“我很喜欢舞狮和画中国画。”三亚之行给新西兰奥克兰派恩赫斯特学校学生多里安(Dorian)留下了深刻印象，“画中国画十分有趣且别具特色，在新西兰我们体验不到这类活动；舞狮也特别酷，对我们而言这算是一种全新的体验”。" data-title="新西兰青少年的三亚之行：文化体验中感知中国" data-date="10-04 21:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 21:09</span>
          <span class="news-item-title">新西兰青少年的三亚之行：文化体验中感知中国</span>
          <span class="news-value-point">💡 中新网三亚10月4日电 (张月和)“我很喜欢舞狮和画中国画</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/10-04/10707967.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="原标题：我的铁路风景｜候车室里搭“文化集市”，将赣西三地风光送到旅客身边！" data-title="候车室里搭“文化集市”，将赣西三地风光送到旅客身边！" data-date="10-04 21:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">10-04 21:02</span>
          <span class="news-item-title">候车室里搭“文化集市”，将赣西三地风光送到旅客身边！</span>
          <span class="news-value-point">💡 原标题：我的铁路风景｜候车室里搭“文化集市”，将赣西三地风光送到旅客身边</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/gadgets/1004242/airpods-pro-3-amazon-october-prime-day-deal-sale" target="_blank" rel="noopener" data-cat="zonghe" data-summary="我们已经有一段时间没有在Apple AirPods Pro 3上看到很好的折扣了，但就像最新的iPad Mini和M5 MacBook Airs一样， 10月Prime Day现在正在发生一个很棒的折扣。您可以抢购一对降噪耳机，其中包括" data-title="The AirPods Pro 3 are a fantastic deal at $179" data-date="10-04 21:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">10-04 21:00</span>
          <span class="news-item-title">AirPods Pro 3非常划算，售价179 $</span>
          <span class="news-item-title-en">The AirPods Pro 3 are a fantastic deal at $179</span>
          <span class="news-value-point">💡 我们已经有一段时间没有在Apple AirPods Pro 3上看到很好的折扣了，但就像最新的iPad Mini和M5 MacBook Airs…</span>
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


<p class="news-updated">🕐 抓取更新于 2026-10-05 14:14（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
