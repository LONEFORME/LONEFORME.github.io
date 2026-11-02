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
      <span>2026-11-02 16:30 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num">10</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×19 · IT之家×10</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/11-02/10724803.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="今年是党领导人民治理黄河80年。沿黄各省区正共同抓好大保护，协同推进大治理，黄河流域治理水土流失面积29万平方公里，流域生态面貌持续向好。" data-title="候鸟翩飞、生态蝶变 黄河流域治理保护成绩单亮眼" data-date="11-02 16:24" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 11-02 16:24</span>
      </div>
      <h2 class="hero-featured-title">候鸟翩飞、生态蝶变 黄河流域治理保护成绩单亮眼</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/021/101.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 2 日消息，据《科创板日报》报道，三星电子已决定全面退出 8 英寸晶圆代工业务，公司近期已通知客户，计划在 2030 年底前关闭所有相关生产线。IT之家注意到，此前，三星电子一直仅表示将逐步缩减 8 英寸生产线，此次则是首次明确提出业务退出的具体时间表，之后公司计划将人力和设备投资集中于基于 12 英寸晶圆先进制程。长期委托三星电子进行芯片生产的韩国本土无晶圆厂（Fabless）企业，如今正面临紧急寻找替代生产厂商的压力。延伸阅读8 英寸晶圆指直径为 200 毫米的硅芯片，其制程主要集中在 90 纳米及以上节点，属于成熟制程范畴。这类产线主要生产电源管理芯片（PMIC）、显示驱动 IC（DDIC）、CMOS 图像传感器、微控制器（MCU）、功率器件、射频芯片、指纹识别芯片" data-title="三星计划 2030 年底前关闭 8 英寸晶圆代工所有产线" data-date="11-02 16:30" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">三星计划 2030 年底前关闭 8 英寸晶圆代工所有产线</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/2026/nov/02/premier-league-10-talking-points-from-the-weekends-action" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Marco Rose的战术提升了伯恩茅斯， Roméo Lavia在切尔西取得了进步， Roberto De Zerbi为年轻人提供了马刺的机会。良好的防守是冠军的标志。在安菲尔德，阿森纳在过去的13次访问中没有获胜， Mikel Arteta" data-title="Premier League: 10 talking points from the weekend’s action" data-date="11-02 16:00" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">Premier League: 10 talking points from the weekend’s action</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/021/102.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 2 日消息，首届 CMG 世界机器人登泰山大赛于今日（11 月 2 日）在山东泰安正式开赛，近 90 支赛队同台竞技，在红门至中天门（3100 级台阶、600 米高差）千年盘道开启实景山地竞技比拼。据央视新闻报道，经过激烈角逐，多项冠军揭晓：人形机器人竞速赛的正赛赛段（红门广场 — 斗母宫），智身凌岳队以最终成绩 27 分 26 秒夺冠。人形机器人竞速赛挑战赛段（斗母宫 — 壶天阁），获得“勇闯巅峰奖”的是智身凌岳队，用时 55 分 34 秒。北京灵翌科技队获得足式机器人竞速赛冠军，总时间 43 分 41 秒。灵锶智能灵狮队最终积分 400 分、用时 1 小时 51 分 29 秒，夺得足式机器人负重赛的冠军。据IT之家此前报道，大赛包含人形机器人竞速、足式机器人竞速、足式" data-title="首届 CMG 世界机器人登泰山大赛赛果出炉，最快 27 分 26 秒夺冠" data-date="11-02 16:30" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">首届 CMG 世界机器人登泰山大赛赛果出炉，最快 27 分 26 秒夺冠</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-02/10724803.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="今年是党领导人民治理黄河80年。沿黄各省区正共同抓好大保护，协同推进大治理，黄河流域治理水土流失面积29万平方公里，流域生态面貌持续向好。" data-title="候鸟翩飞、生态蝶变 黄河流域治理保护成绩单亮眼" data-date="11-02 16:24" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 16:24</span>
          <span class="news-item-title">候鸟翩飞、生态蝶变 黄河流域治理保护成绩单亮眼</span>
          <span class="news-value-point">💡 今年是党领导人民治理黄河80年</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-02/10724791.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月2日电 (记者 黄钰钦 谢雁冰)中国外交部发言人毛宁11月2日主持例行记者会。" data-title="联大一委通过中国提交的有关决议 外交部介绍情况" data-date="11-02 15:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 15:47</span>
          <span class="news-item-title">联大一委通过中国提交的有关决议 外交部介绍情况</span>
          <span class="news-value-point">💡 中新网北京11月2日电 (记者 黄钰钦 谢雁冰)中国外交部发言人毛宁11月2日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-02/10724788.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京11月2日电 题：新征程上强党强国的光辉文献——《中共中央关于持之以恒推进全面从严治党若干重大问题的决定》诞生记" data-title="新征程上强党强国的光辉文献——《中共中央关于持之以恒推进全面从严治党若干重大问题的决定》诞生记" data-date="11-02 15:46" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 15:46</span>
          <span class="news-item-title">新征程上强党强国的光辉文献——《中共中央关于持之以恒推进全面从严治党若干重大问题的决定》诞生记</span>
          <span class="news-value-point">💡 新华社北京11月2日电 题：新征程上强党强国的光辉文献——《中共中央关于持之以恒推进全面从严治党若干重大问题的决定》诞生记</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-02/10724789.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月2日电 (记者 黄钰钦)中国外交部发言人11月2日宣布：中共中央政治局委员、外交部长王毅将于11月3日至4日在北京主持澜沧江—湄公河合作第十一次外长会。" data-title="王毅将主持澜湄合作第十一次外长会" data-date="11-02 15:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 15:42</span>
          <span class="news-item-title">王毅将主持澜湄合作第十一次外长会</span>
          <span class="news-value-point">💡 中新网北京11月2日电 (记者 黄钰钦)中国外交部发言人11月2日宣布：中共中央政治局委员、外交部长王毅将于11月3日至4日在北京主持澜沧江—湄…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-02/10724776.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月2日电 索非亚消息：根据保加利亚中央选举委员会当地时间2日公布的数据，现任总统约托娃在总统选举第二轮投票中获得最多票数。根据相关规定，她将当选为新一任总统。" data-title="保加利亚现总统约托娃赢得总统选举" data-date="11-02 15:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 15:32</span>
          <span class="news-item-title">保加利亚现总统约托娃赢得总统选举</span>
          <span class="news-value-point">💡 中新社北京11月2日电 索非亚消息：根据保加利亚中央选举委员会当地时间2日公布的数据，现任总统约托娃在总统选举第二轮投票中获得最多票数</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-02/10724785.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月2日电 (记者 黄钰钦)中国外交部发言人毛宁11月2日主持例行记者会。" data-title="中方：希望有关方正视半岛问题根源，坚持政治解决大方向" data-date="11-02 15:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 15:31</span>
          <span class="news-item-title">中方：希望有关方正视半岛问题根源，坚持政治解决大方向</span>
          <span class="news-value-point">💡 中新网北京11月2日电 (记者 黄钰钦)中国外交部发言人毛宁11月2日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-02/10724774.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间11月1日晚，哥伦比亚中西部托利马省普拉纳达斯市发生一起爆炸袭击事件。初步调查结果显示，袭击造成至少4人死亡，其中包括一名婴儿。" data-title="哥伦比亚中西部发生爆炸袭击事件 致4人死亡" data-date="11-02 15:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 15:22</span>
          <span class="news-item-title">哥伦比亚中西部发生爆炸袭击事件 致4人死亡</span>
          <span class="news-value-point">💡 当地时间11月1日晚，哥伦比亚中西部托利马省普拉纳达斯市发生一起爆炸袭击事件</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-02/10724756.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="日前在天津举办的中国新型政党制度理论研讨会上，多位学者表示，与当前欧美政党政治乱象频发形成鲜明对比，中国新型政党制度以一种崭新的制度模式、政党关系和执政方式，为世界政党政治提供了中国方案。" data-title="为世界政党政治贡献中国方案" data-date="11-02 15:19" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 15:19</span>
          <span class="news-item-title">为世界政党政治贡献中国方案</span>
          <span class="news-value-point">💡 日前在天津举办的中国新型政党制度理论研讨会上，多位学者表示，与当前欧美政党政治乱象频发形成鲜明对比，中国新型政党制度以一种崭新的制度模式、政党关…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-02/10724755.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="北京市政协近日召开“进一步完善普惠托育服务体系建设，持续提升托育服务保障水平”专题协商会，与会委员、专家学者围绕普惠托育如何“托得到、托得好”积极建言献策。" data-title="北京市政协献策 助力普惠托育“托得到、托得好”" data-date="11-02 15:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 15:16</span>
          <span class="news-item-title">北京市政协献策 助力普惠托育“托得到、托得好”</span>
          <span class="news-value-point">💡 北京市政协近日召开“进一步完善普惠托育服务体系建设，持续提升托育服务保障水平”专题协商会，与会委员、专家学者围绕普惠托育如何“托得到、托得好”积…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-02/10724773.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="外交部发言人宣布：" data-title="王毅将主持澜湄合作第十一次外长会" data-date="11-02 15:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 15:15</span>
          <span class="news-item-title">王毅将主持澜湄合作第十一次外长会</span>
          <span class="news-value-point">💡 外交部发言人宣布：</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-02/10724758.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月2日电 据美联社当地时间11月1日报道，当日是美国中期选举(定于3日举行)前的最后一个周日，美国总统特朗普前往堪萨斯州萨利纳和艾奥瓦州迪比克参加助选集会。" data-title="“共和党将迎压倒性胜利” 美中期选举进入最后冲刺，特朗普赴两州拉票" data-date="11-02 15:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 15:08</span>
          <span class="news-item-title">“共和党将迎压倒性胜利” 美中期选举进入最后冲刺，特朗普赴两州拉票</span>
          <span class="news-value-point">💡 中新网11月2日电 据美联社当地时间11月1日报道，当日是美国中期选举(定于3日举行)前的最后一个周日，美国总统特朗普前往堪萨斯州萨利纳和艾奥瓦…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-02/10724747.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月2日电 据西班牙广播电视台报道，西班牙卡斯蒂利亚-拉曼查自治区高等法院2日发布通报称，西班牙托莱多省乌尔达列车相撞事故69名遇难者中，已有66人身份得到确认，另有3人身份尚待确认。" data-title="西班牙列车相撞事故66名遇难者身份已确认" data-date="11-02 14:19" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 14:19</span>
          <span class="news-item-title">西班牙列车相撞事故66名遇难者身份已确认</span>
          <span class="news-value-point">💡 中新网11月2日电 据西班牙广播电视台报道，西班牙卡斯蒂利亚-拉曼查自治区高等法院2日发布通报称，西班牙托莱多省乌尔达列车相撞事故69名遇难者中…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/01/upshot/poll-times-siena-senate-midterms.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="根据新的Times/Siena调查，民主党在将决定参议院控制权的所有关键州中处于领先地位。" data-title="The Final Polls Show a Blue Surge. Can We Trust Them?" data-date="11-02 14:07" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-02 14:07</span>
          <span class="news-item-title">最终民意调查显示蓝色溢价。我们能相信他们吗？</span>
          <span class="news-item-title-en">The Final Polls Show a Blue Surge. Can We Trust Them?</span>
          <span class="news-value-point">💡 根据新的Times/Siena调查，民主党在将决定参议院控制权的所有关键州中处于领先地位</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-02/10724738.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中国新闻周刊记者；郑立颖" data-title="印度“蟑螂运动”的第二季" data-date="11-02 13:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 13:57</span>
          <span class="news-item-title">印度“蟑螂运动”的第二季</span>
          <span class="news-value-point">💡 中国新闻周刊记者</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/02/us/elections/newsom-harris-becerra-rally.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="两位可能的总统候选人出现在洛杉矶，支持加州州长民主党候选人泽维尔·贝塞拉（ Xavier Becerra ）。" data-title="Newsom and Harris Appear Together, With Little Hint of What’s to Come" data-date="11-02 13:17" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-02 13:17</span>
          <span class="news-item-title">纽瑟姆和哈里斯一起出现，对即将发生的事情略有暗示</span>
          <span class="news-item-title-en">Newsom and Harris Appear Together, With Little Hint of What’s to Come</span>
          <span class="news-value-point">💡 两位可能的总统候选人出现在洛杉矶，支持加州州长民主党候选人泽维尔·贝塞拉（ Xavier Becerra ）</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/021/101.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 2 日消息，据《科创板日报》报道，三星电子已决定全面退出 8 英寸晶圆代工业务，公司近期已通知客户，计划在 2030 年底前关闭所有相关生产线。IT之家注意到，此前，三星电子一直仅表示将逐步缩减 8 英寸生产线，此次则是首次明确提出业务退出的具体时间表，之后公司计划将人力和设备投资集中于基于 12 英寸晶圆先进制程。长期委托三星电子进行芯片生产的韩国本土无晶圆厂（Fabless）企业，如今正面临紧急寻找替代生产厂商的压力。延伸阅读8 英寸晶圆指直径为 200 毫米的硅芯片，其制程主要集中在 90 纳米及以上节点，属于成熟制程范畴。这类产线主要生产电源管理芯片（PMIC）、显示驱动 IC（DDIC）、CMOS 图像传感器、微控制器（MCU）、功率器件、射频芯片、指纹识别芯片" data-title="三星计划 2030 年底前关闭 8 英寸晶圆代工所有产线" data-date="11-02 16:30" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-02 16:30</span>
          <span class="news-item-title">三星计划 2030 年底前关闭 8 英寸晶圆代工所有产线</span>
          <span class="news-value-point">💡 IT之家 11 月 2 日消息，据《科创板日报》报道，三星电子已决定全面退出 8 英寸晶圆代工业务，公司近期已通知客户，计划在 2030 年底前…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/021/096.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 2 日消息，TrendForce（集邦）10 月 29 日发布预测，认为在人工智能计算负载转向推理和智能体的影响下，CPU 需求走强，带动高容量 MLCC（IT之家注：多层陶瓷电容器）需求激增。在上游 NVIDIA、AMD 新一代高规格 AI 算力平台放量的推动下，这类 MLCC 的缺货预计将持续到 2027 年上半年。此外，AI 基建带动光通信板块，光收发模块 MLCC 也出现供应缺口。与此同时，智能手机、笔记本电脑需求因涨价萎缩，导致 ODM 下调订单规模，消费级中低容量 MLCC 现货价格也在 10 月上旬走低 5%。▲ 村田陶瓷电容器产品机构认为，供方仍掌握高端 MLCC 定价主导权。日本制造商很可能会与三星电机一样在本月启动的 2027Q1 合约谈判中涨价。相关" data-title="TrendForce 预测：AI CPU 需求强劲，高容量 MLCC 缺货将延续至 2027H1" data-date="11-02 16:24" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-02 16:24</span>
          <span class="news-item-title">TrendForce 预测：AI CPU 需求强劲，高容量 MLCC 缺货将延续至 2027H1</span>
          <span class="news-value-point">💡 IT之家 11 月 2 日消息，TrendForce（集邦）10 月 29 日发布预测，认为在人工智能计算负载转向推理和智能体的影响下，CPU …</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/021/095.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 2 日消息，Y Combinator 与 Olam Labs 的人工智能研究人员近期在游戏场景中测试了智能体集群。研究选用《我的世界》及其各类玩法作为试验沙盒，让上百个智能体在其中协作或者相互对抗。研究思路是，借助游戏内的协作与冲突，帮助人们理解现实世界里那些引发广泛关注的智能体事件。IT之家注意到，这项研究有助于厘清近期各类智能体集群事件里的利弊得失，方便技术开发者对相关能力进行优化。博文提到了两个反差鲜明的案例：一个是上千个智能体组成集群，“近期攻克了数百道公开数学难题”；另一个则是 OpenAI 与 Hugging Face 之间那起“风险极高”的事件。本次研究建立在以往的成果与框架之上，主要依托 Mindcraft 等代码仓库以及 Mineflayer 脚本工具。" data-title="研究者在《我的世界》测试 AI 智能体集群：协作容易官僚化，对战 GPT 胜率更高" data-date="11-02 16:24" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-02 16:24</span>
          <span class="news-item-title">研究者在《我的世界》测试 AI 智能体集群：协作容易官僚化，对战 GPT 胜率更高</span>
          <span class="news-value-point">💡 IT之家 11 月 2 日消息，Y Combinator 与 Olam Labs 的人工智能研究人员近期在游戏场景中测试了智能体集群</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/507150.html" target="_blank" rel="noopener" data-cat="keji" data-summary="模型管线双驱动" data-title="央视严选“中国AI创业十骏”：唯一AI制药公司是清华系" data-date="11-02 14:28" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-02 14:28</span>
          <span class="news-item-title">央视严选“中国AI创业十骏”：唯一AI制药公司是清华系</span>
          <span class="news-value-point">💡 模型管线双驱动</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/507107.html" target="_blank" rel="noopener" data-cat="keji" data-summary="能指挥Agent干活，还能控制智能家居" data-title="小米开源了个150元的AI小玩意，火到配件都涨价了" data-date="11-02 14:08" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-02 14:08</span>
          <span class="news-item-title">小米开源了个150元的AI小玩意，火到配件都涨价了</span>
          <span class="news-value-point">💡 能指挥Agent干活，还能控制智能家居</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/507082.html" target="_blank" rel="noopener" data-cat="keji" data-summary="HuggingFace疑似泄露权重已被下5000次" data-title="GPT-6.2 Astra开启灰测！Claude Mythos 5.5同日曝光" data-date="11-02 12:28" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-02 12:28</span>
          <span class="news-item-title">GPT-6.2 Astra开启灰测！Claude Mythos 5.5同日曝光</span>
          <span class="news-value-point">💡 HuggingFace疑似泄露权重已被下5000次</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c5djvk2dm33xo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="keji" data-summary="这些数据中心正滚存着数百亿英镑的债务。" data-title="人工智能泡沫将爆破？这群“新云端”公司正加剧市场担忧" data-date="11-02 08:17" data-source="BBC">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-02 08:17</span>
          <span class="news-item-title">人工智能泡沫将爆破？这群“新云端”公司正加剧市场担忧</span>
          <span class="news-value-point">💡 这些数据中心正滚存着数百亿英镑的债务</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/01/openai-might-rebrand-its-data-centers-as-ai-compute-campuses/" target="_blank" rel="noopener" data-cat="keji" data-summary="数据中心非常不受欢迎。但是，如果我们称之为其他东西呢？" data-title="OpenAI might rebrand its data centers as ‘AI compute campuses’" data-date="11-02 05:55" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-02 05:55</span>
          <span class="news-item-title">OpenAI可能会将其数据中心重新命名为“AI计算园区”</span>
          <span class="news-item-title-en">OpenAI might rebrand its data centers as ‘AI compute campuses’</span>
          <span class="news-value-point">💡 数据中心非常不受欢迎</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/cyber-security/new-ai-driven-windows-malware-feeds-stolen-data-to-claude-to-rank-victims-assets-by-value-then-deletes-itself-payload-builds-custom-target-assessment-can-switch-models-if-one-refuses-or-skip-the-ai-step-entirely" target="_blank" rel="noopener" data-cat="keji" data-summary="Cisco Talos表示， VOLTA信息窃取者将被盗受害者数据发送给Claude Opus 4.6 ，以根据货币化价值对资产进行排名。" data-title="New AI-driven Windows malware feeds stolen data to Claude to rank victims’ assets by value, then deletes itself" data-date="11-02 05:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-02 05:00</span>
          <span class="news-item-title">新的人工智能驱动的Windows恶意软件将被盗数据馈送给Claude ，按价值对受害者的资产进行排名，然后自行删除</span>
          <span class="news-item-title-en">New AI-driven Windows malware feeds stolen data to Claude to rank victims’ assets by value, then deletes itself</span>
          <span class="news-value-point">💡 Cisco Talos表示， VOLTA信息窃取者将被盗受害者数据发送给Claude Opus 4.6 ，以根据货币化价值对资产进行排名</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/brazilian-lawyers-busted-for-attempting-to-manipulate-courts-ai-with-prompt-injection-hidden-in-filing-courts-ai-flags-hidden-text-that-demanded-superficial-legal-scrutiny-lawyers-fined-usd16-000" target="_blank" rel="noopener" data-cat="keji" data-summary="在一起劳工案件中，原告的律师试图使用即时注入来影响法院的人工智能，但被抓获。无论如何，他们都赢了，因为被告没有回应，这使得此举完全没有必要。" data-title="Brazilian lawyers busted for attempting to manipulate court&#39;s AI with prompt injection hidden in filing" data-date="11-01 23:05" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-01 23:05</span>
          <span class="news-item-title">巴西律师因试图操纵法院的人工智能而被捕，提示注入隐藏在文件中</span>
          <span class="news-item-title-en">Brazilian lawyers busted for attempting to manipulate court's AI with prompt injection hidden in filing</span>
          <span class="news-value-point">💡 在一起劳工案件中，原告的律师试图使用即时注入来影响法院的人工智能，但被抓获</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/sam-altman-travels-to-south-korea-to-meet-samsung-leadership-to-secure-more-ram-for-data-centers-amid-crushing-shortages-openai-ceo-meets-samsung-leadership-to-discuss-future-ai-data-centers" target="_blank" rel="noopener" data-cat="keji" data-summary="10月31日， OpenAI首席执行官Sam Altman在韩国会见了大约50名三星高管，讨论了人工智能的未来、商业机会以及该技术对企业运营的影响。会议召开之际，对内存芯片的需求也随之增长" data-title="Sam Altman meets with Samsung leadership to secure more RAM for data centers amid crushing shortages" data-date="11-01 22:21" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-01 22:21</span>
          <span class="news-item-title">Sam Altman与三星领导层会面，在严重短缺的情况下为数据中心提供更多RAM</span>
          <span class="news-item-title-en">Sam Altman meets with Samsung leadership to secure more RAM for data centers amid crushing shortages</span>
          <span class="news-value-point">💡 10月31日， OpenAI首席执行官Sam Altman在韩国会见了大约50名三星高管，讨论了人工智能的未来、商业机会以及该技术对企业运营的影…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/020/837.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 1 日消息，OpenAI、谷歌、微软以及 Anthropic 近日宣布将采用一项新标准，内容发布方可以借助该标准选择拒绝 AI 抓取自家网站内容。借助这项管控机制，内容发布方可以一次性向多家 AI 企业统一申明自身针对 AI 模型训练的内容使用偏好，而不必为每家企业单独设置规则。该标准由 Anthropic 技术负责人 Kevin Kelley 向互联网工程任务组（IETF）提出，并将集成在网站的 robots.txt 文件中。长期以来，robots.txt 文件用于告知网络爬虫哪些网站内容允许抓取、哪些禁止抓取，适用场景包含搜索索引、网页归档以及 AI 模型训练。目前，网站必须向每一家 AI 企业分别单独声明自己的 AI 训练相关内容使用偏好。在此背景下，各类 AI 爬" data-title="OpenAI、谷歌、微软和 Anthropic 联手推行 AI 数据抓取退出标准" data-date="11-01 22:19" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-01 22:19</span>
          <span class="news-item-title">OpenAI、谷歌、微软和 Anthropic 联手推行 AI 数据抓取退出标准</span>
          <span class="news-value-point">💡 IT之家 11 月 1 日消息，OpenAI、谷歌、微软以及 Anthropic 近日宣布将采用一项新标准，内容发布方可以借助该标准选择拒绝 A…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/020/836.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 1 日消息，海贝宣布推出一款 HiBy R6III SE 便携 Hi-Fi 播放器，定价为 1798 元。该机整体尺寸为 129.4 x 73.1 x 15.6 mm，重量为 250 g。提供黑色和海军蓝两种颜色选择，正面配备了一块 5 英寸 1280x720 分辨率 IPS 面板，背部搭配了钻石切割纹理的玻璃背板。该机采用 4 颗 CS43198 DAC 芯片，支持 8 路独立输出。耳放部分支持 A 类和 AB 类模式切换，其中 A 类耳放由 OPA1652 运放、晶体管及 ELNA 音频电容组成。硬件搭载 45.158MHz 和 49.152MHz 两颗专用音频晶振。该机搭载骁龙 665 处理器，配备 3GB RAM 与 32GB 存储空间，机身底部配备 3.5mm" data-title="海贝推出 HiBy R6III SE 便携 Hi-Fi 播放器：4 颗 CS43198 DAC 芯片，1798 元" data-date="11-01 22:01" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-01 22:01</span>
          <span class="news-item-title">海贝推出 HiBy R6III SE 便携 Hi-Fi 播放器：4 颗 CS43198 DAC 芯片，1798 元</span>
          <span class="news-value-point">💡 IT之家 11 月 1 日消息，海贝宣布推出一款 HiBy R6III SE 便携 Hi-Fi 播放器，定价为 1798 元</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1024108/homepod-mini-2-hands-on-siri-smart-home-mac-speaker" target="_blank" rel="noopener" data-cat="keji" data-summary="当我上个月在苹果的欢迎回家活动上第一次听说新的$ 149 HomePod Mini 2时，我感到很失望。苹果推出入门级智能音箱已经六年了，它在第二代中得到的只是一个芯片凸起，一些颜色" data-title="HomePod Mini 2 first look: Three things I love and one disappointment" data-date="11-01 22:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-01 22:00</span>
          <span class="news-item-title">HomePod Mini 2首次亮相：三件我喜欢的事情和一件令人失望的事情</span>
          <span class="news-item-title-en">HomePod Mini 2 first look: Three things I love and one disappointment</span>
          <span class="news-value-point">💡 当我上个月在苹果的欢迎回家活动上第一次听说新的$ 149 HomePod Mini 2时，我感到很失望</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/open-source-usb-tool-unlocks-nvidias-half-speed-gpu-ai-limiter-on-windows-lifts-gpus-fp16-math-performance-up-to-65-percent-uefi-unlocker-covers-rtx-20-30-and-40-series-desktops-and-laptops" target="_blank" rel="noopener" data-cat="keji" data-summary="开源UEFI工具nv-uefi-unlocker提升了Nvidia在Windows下RTX 20、30和40系列GPU上的张量速率上限。" data-title="Open-source USB tool unlocks Nvidia&#39;s half-speed GPU AI limiter on Windows" data-date="11-01 22:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-01 22:00</span>
          <span class="news-item-title">开源USB工具在Windows上解锁Nvidia的半速GPU AI限制器</span>
          <span class="news-item-title-en">Open-source USB tool unlocks Nvidia's half-speed GPU AI limiter on Windows</span>
          <span class="news-value-point">💡 开源UEFI工具nv-uefi-unlocker提升了Nvidia在Windows下RTX 20、30和40系列GPU上的张量速率上限</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/02/premier-league-10-talking-points-from-the-weekends-action" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Marco Rose的战术提升了伯恩茅斯， Roméo Lavia在切尔西取得了进步， Roberto De Zerbi为年轻人提供了马刺的机会。良好的防守是冠军的标志。在安菲尔德，阿森纳在过去的13次访问中没有获胜， Mikel Arteta" data-title="Premier League: 10 talking points from the weekend’s action" data-date="11-02 16:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-02 16:00</span>
          <span class="news-item-title">英超联赛：周末行动的10个谈话要点</span>
          <span class="news-item-title-en">Premier League: 10 talking points from the weekend’s action</span>
          <span class="news-value-point">💡 Marco Rose的战术提升了伯恩茅斯， Roméo Lavia在切尔西取得了进步， Roberto De Zerbi为年轻人提供了马刺的机会</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13606815/arsenals-defensive-masterclass-praised-in-liverpool-win-as-jamie-carragher-salutes-world-class-declan-rice" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="自2012年以来-当时现任老板米克尔·阿尔特塔在球场上指挥阿森纳的中场-枪手在利物浦的比赛中获胜。那个诅咒终于被打破了。" data-title="Defensive &#39;masterclass&#39; and elite Rice - how Arsenal ended Anfield torment" data-date="11-02 07:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-02 07:00</span>
          <span class="news-item-title">防守“大师班”和精英大米-阿森纳如何结束安菲尔德的折磨</span>
          <span class="news-item-title-en">Defensive 'masterclass' and elite Rice - how Arsenal ended Anfield torment</span>
          <span class="news-value-point">💡 自2012年以来-当时现任老板米克尔·阿尔特塔在球场上指挥阿森纳的中场-枪手在利物浦的比赛中获胜</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/01/andoni-iraola-responds-liverpool-penalty-denial-arsenal-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="经理对裁判驳回的两项罚款索赔表示遗憾伊拉奥拉抱怨“如果你不下去，你就不叫它‘安东尼·伊拉奥拉说，在亚历山大·伊萨克（ Alexander Isak ）在阿森期间被拒绝罚款后，他将指示利物浦球员将来进入禁区" data-title="‘We have to tell them to go down’: Iraola responds to Isak penalty denial for Liverpool" data-date="11-02 05:25" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-02 05:25</span>
          <span class="news-item-title">“我们必须告诉他们失败” ：伊拉奥拉回应伊萨克对利物浦的罚款否认</span>
          <span class="news-item-title-en">‘We have to tell them to go down’: Iraola responds to Isak penalty denial for Liverpool</span>
          <span class="news-value-point">💡 经理对裁判驳回的两项罚款索赔表示遗憾伊拉奥拉抱怨“如果你不下去，你就不叫它‘安东尼·伊拉奥拉说，在亚历山大·伊萨克（ Alexander Isa…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cvp8grpjk4leo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="安东尼·伊拉奥拉（ Andoni Iraola ）表示，在利物浦在周日被阿森纳击败后被罚下场后，他将告诉他的球员们将来会倒下。" data-title="I&#39;ll tell my players to dive in future" data-date="11-02 05:00" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-02 05:00</span>
          <span class="news-item-title">我会告诉我的玩家将来潜水</span>
          <span class="news-item-title-en">I'll tell my players to dive in future</span>
          <span class="news-value-point">💡 安东尼·伊拉奥拉（ Andoni Iraola ）表示，在利物浦在周日被阿森纳击败后被罚下场后，他将告诉他的球员们将来会倒下</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c39wz2epven4o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳从二级联赛弗利特伍德的失利低点反弹回来，确保了他们在安菲尔德14年来的首次胜利-并在英超联赛的顶端开启了三分领先优势。" data-title="From Fleetwood embarrassment to &#39;magical&#39; Anfield win 14 years in making" data-date="11-02 04:16" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-02 04:16</span>
          <span class="news-item-title">从Fleetwood的尴尬到“神奇”的安菲尔德赢得了14年的制作经验</span>
          <span class="news-item-title-en">From Fleetwood embarrassment to 'magical' Anfield win 14 years in making</span>
          <span class="news-value-point">💡 阿森纳从二级联赛弗利特伍德的失利低点反弹回来，确保了他们在安菲尔德14年来的首次胜利-并在英超联赛的顶端开启了三分领先优势</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13606793/liverpool-0-1-arsenal-alexander-isak-jurrien-timber-shirt-pull-and-noni-madueke-alexis-mac-allister-headbutt-show-good-and-bad-sides-of-var" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在阿森纳1-0战胜利物浦的比赛中，有两个重要的爆发点，展示了VAR的好处和坏处。" data-title="Isak&#39;s non-penalty and Madueke-Mac Allister &#39;headbutt&#39; - were big calls right?" data-date="11-02 04:05" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-02 04:05</span>
          <span class="news-item-title">Isak的非惩罚和Madueke-Mac Allister的“头撞” -是大电话对吧？</span>
          <span class="news-item-title-en">Isak's non-penalty and Madueke-Mac Allister 'headbutt' - were big calls right?</span>
          <span class="news-value-point">💡 在阿森纳1-0战胜利物浦的比赛中，有两个重要的爆发点，展示了VAR的好处和坏处</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/videos/cmly09yv9xl6o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="阿森纳自2012年以来首次在安菲尔德获胜，在一场端到端的比赛之后，在安菲尔德获得了三分领先优势，这让利物浦对一无所获感到沮丧。" data-title="Arsenal move clear at the top with a rare win at Liverpool" data-date="11-02 04:00" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-02 04:00</span>
          <span class="news-item-title">阿森纳凭借在利物浦的罕见胜利在顶部清除</span>
          <span class="news-item-title-en">Arsenal move clear at the top with a rare win at Liverpool</span>
          <span class="news-value-point">💡 阿森纳自2012年以来首次在安菲尔德获胜，在一场端到端的比赛之后，在安菲尔德获得了三分领先优势，这让利物浦对一无所获感到沮丧</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025486/arsenal-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Arsenal latest: Ending long waits motivates me, says Arteta" data-title="Arsenal latest: Ending long waits motivates me, says Arteta" data-date="11-02 03:39" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-02 03:39</span>
          <span class="news-item-title">阿森纳最新消息： Arteta说，结束漫长的等待激励着我</span>
          <span class="news-item-title-en">Arsenal latest: Ending long waits motivates me, says Arteta</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025501/liverpool-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Liverpool latest: Iraola &#39;will tell players to dive&#39; after Isak controversy" data-title="Liverpool latest: Iraola &#39;will tell players to dive&#39; after Isak controversy" data-date="11-02 03:18" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-02 03:18</span>
          <span class="news-item-title">利物浦最新消息：伊拉奥拉将在伊萨克争议后“告诉球员潜水”</span>
          <span class="news-item-title-en">Liverpool latest: Iraola 'will tell players to dive' after Isak controversy</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/nov/01/liverpool-v-arsenal-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Kai Havertz的目标足以让阿森纳自2012年9月以来首次在安菲尔德取得胜利，并让他们在积分榜上获得三分。那么比赛在哪里？当阿森纳拿到球时，利物浦将寻求让球员绕过球，" data-title="Liverpool 0-1 Arsenal: Premier League – as it happened" data-date="11-02 02:55" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-02 02:55</span>
          <span class="news-item-title">利物浦0-1阿森纳：英超联赛–事实如此</span>
          <span class="news-item-title-en">Liverpool 0-1 Arsenal: Premier League – as it happened</span>
          <span class="news-value-point">💡 Kai Havertz的目标足以让阿森纳自2012年9月以来首次在安菲尔德取得胜利，并让他们在积分榜上获得三分</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/01/liverpool-arsenal-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="这是一场比赛，阿森纳展示了他们无情的一面，以及他们在上赛季积累的所有冠军知识。他们发表声明后返回伦敦。不管曼城发生了什么" data-title="Arsenal hold on for first league win at Liverpool since 2012 after Kai Havertz pounces early" data-date="11-02 02:44" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-02 02:44</span>
          <span class="news-item-title">阿森纳自2012年以来首次在利物浦赢得联赛冠军，此前凯·哈弗兹（ Kai Havertz ）提前扑向利物浦</span>
          <span class="news-item-title-en">Arsenal hold on for first league win at Liverpool since 2012 after Kai Havertz pounces early</span>
          <span class="news-value-point">💡 这是一场比赛，阿森纳展示了他们无情的一面，以及他们在上赛季积累的所有冠军知识</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cqj9kgyww478o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦和阿森纳的球员在安菲尔德的英超比赛中是如何评分的，因为过去两个赛季的冠军是面对面的。" data-title="Rice rewarded, Wirtz must do more - Liverpool and Arsenal player ratings" data-date="11-02 02:38" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-02 02:38</span>
          <span class="news-item-title">大米奖励， Wirtz必须做得更多-利物浦和阿森纳球员评级</span>
          <span class="news-item-title-en">Rice rewarded, Wirtz must do more - Liverpool and Arsenal player ratings</span>
          <span class="news-value-point">💡 利物浦和阿森纳的球员在安菲尔德的英超比赛中是如何评分的，因为过去两个赛季的冠军是面对面的</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/liverpool-vs-arsenal/report/559530" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在凯·哈维兹（ Kai Havertz ）的罢工以1比0大获全胜后，阿森纳14年来首次在安菲尔德获胜，但利物浦被剥夺了看似明显的惩罚。" data-title="Arsenal win at Anfield for first time in 14 years to move top" data-date="11-02 02:30" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-02 02:30</span>
          <span class="news-item-title">阿森纳14年来首次在安菲尔德夺冠</span>
          <span class="news-item-title-en">Arsenal win at Anfield for first time in 14 years to move top</span>
          <span class="news-value-point">💡 在凯·哈维兹（ Kai Havertz ）的罢工以1比0大获全胜后，阿森纳14年来首次在安菲尔德获胜，但利物浦被剥夺了看似明显的惩罚</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/01/michael-carrick-manchester-united-favourite-premier-league-sack-race" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="不同寻常的是，顶级联赛中的所有俱乐部都有同一位经理，他们本赛季的开局经理是同一个人–但第一次解雇可能并不遥远本赛季还没有英超经理丢掉工作。在过去的10次活动中，只有三次是11月份的" data-title="Should Premier League strugglers stick or twist as pressure on managers mounts?  | Andrew Beasley" data-date="11-02 02:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-02 02:00</span>
          <span class="news-item-title">随着经理的压力越来越大，英超联赛的挣扎者应该坚持还是扭曲？ |安德鲁·比斯利</span>
          <span class="news-item-title-en">Should Premier League strugglers stick or twist as pressure on managers mounts?  | Andrew Beasley</span>
          <span class="news-value-point">💡 不同寻常的是，顶级联赛中的所有俱乐部都有同一位经理，他们本赛季的开局经理是同一个人–但第一次解雇可能并不遥远本赛季还没有英超经理丢掉工作</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13606752/asia-pacific-amateur-championship-day-four-highlights" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="亚太业余锦标赛第四天的亮点， FIFA Laopakdee赢得了大师赛和公开锦标赛的邀请。" data-title="Laopakdee earns major invites after winning Asia-Pacific Amateur Championship" data-date="11-02 01:21" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-02 01:21</span>
          <span class="news-item-title">Laopakdee在赢得亚太业余锦标赛后赢得了重要的邀请</span>
          <span class="news-item-title-en">Laopakdee earns major invites after winning Asia-Pacific Amateur Championship</span>
          <span class="news-value-point">💡 亚太业余锦标赛第四天的亮点， FIFA Laopakdee赢得了大师赛和公开锦标赛的邀请</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/021/102.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 2 日消息，首届 CMG 世界机器人登泰山大赛于今日（11 月 2 日）在山东泰安正式开赛，近 90 支赛队同台竞技，在红门至中天门（3100 级台阶、600 米高差）千年盘道开启实景山地竞技比拼。据央视新闻报道，经过激烈角逐，多项冠军揭晓：人形机器人竞速赛的正赛赛段（红门广场 — 斗母宫），智身凌岳队以最终成绩 27 分 26 秒夺冠。人形机器人竞速赛挑战赛段（斗母宫 — 壶天阁），获得“勇闯巅峰奖”的是智身凌岳队，用时 55 分 34 秒。北京灵翌科技队获得足式机器人竞速赛冠军，总时间 43 分 41 秒。灵锶智能灵狮队最终积分 400 分、用时 1 小时 51 分 29 秒，夺得足式机器人负重赛的冠军。据IT之家此前报道，大赛包含人形机器人竞速、足式机器人竞速、足式" data-title="首届 CMG 世界机器人登泰山大赛赛果出炉，最快 27 分 26 秒夺冠" data-date="11-02 16:30" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-02 16:30</span>
          <span class="news-item-title">首届 CMG 世界机器人登泰山大赛赛果出炉，最快 27 分 26 秒夺冠</span>
          <span class="news-value-point">💡 IT之家 11 月 2 日消息，首届 CMG 世界机器人登泰山大赛于今日（11 月 2 日）在山东泰安正式开赛，近 90 支赛队同台竞技，在红门…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/021/099.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 2 日消息，今年 4 月，华为发布了 Pura X Max 系列和 Pura 90 系列手机，并带来了“智阅键”翻页功能。据介绍，智阅键翻页是在阅读书籍时可以通过智控键（指纹解锁键）进行交互翻页的一种翻页方式。功能开关在华为阅读 3.1.52.300 及以上版本上默认打开。IT之家注意到，目前华为官网已公开该功能的适配机型：HUAWEI Pura X Max 系列HUAWEI Pura 90 系列HUAWEI Mate XT 2 | ULTIMATE DESIGN 系列HUAWEI Pura X View 系列HUAWEI Mate 90 系列智阅键翻页使用逻辑如下：（1）单页往上翻页：上滑智阅键往上翻一页。（2）单页往下翻页：下滑、下滑长触或点触智阅键，翻至下一页。（3" data-title="华为“智阅键”翻页功能最新适配机型公布，含 Pura X View、Mate 90 系列等" data-date="11-02 16:29" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-02 16:29</span>
          <span class="news-item-title">华为“智阅键”翻页功能最新适配机型公布，含 Pura X View、Mate 90 系列等</span>
          <span class="news-value-point">💡 IT之家 11 月 2 日消息，今年 4 月，华为发布了 Pura X Max 系列和 Pura 90 系列手机，并带来了“智阅键”翻页功能</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/021/098.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 2 日消息，JBL 旗下 Authentics 30 音箱现已在京东上架，该产品主打外观设计，定价为 2999 元。京东 JBL Authentics 30 音箱 2999 元直达链接该音箱提供了大地橙与金属黑两种配色，尺寸为 331 x 279 x 180 mm，重量为 4.83 kg。其采用仿皮革材质箱体，正面配备 Quadrex 网罩，机身顶部配备铸铝提手，支持室内及户外灵活切换使用。该音箱内部配备了 1 x 5.25&quot; (138 mm) 的低音单元以及 2 x 1&quot; (25 mm) 的高音单元，搭载蓝牙 6.0 技术，用户可以搭配 JBL One App 定制专属声音参数。音箱本身内置电池，支持脱离固定电源线进行移动使用。在电池充满的情况下，设备可提供长达 8 小" data-title="JBL 推出 Authentics 30 音箱：Quadrex 艺术网罩设计，2999 元" data-date="11-02 16:29" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-02 16:29</span>
          <span class="news-item-title">JBL 推出 Authentics 30 音箱：Quadrex 艺术网罩设计，2999 元</span>
          <span class="news-value-point">💡 IT之家 11 月 2 日消息，JBL 旗下 Authentics 30 音箱现已在京东上架，该产品主打外观设计，定价为 2999 元</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/021/097.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 2 日消息，据科技媒体 MacRumors 昨天报道，欧美国家切换成冬令时后，部分用户发现，他们手上的 Apple Watch 时间显示出了问题：抬起手腕时手表显示的时间正常，但放下进入 AOD 后时间慢了 1 小时。苹果公司对此回应称，这个问题确实存在，但不影响闹钟等功能。用户如果发现 Apple Watch 时间显示不正确，可以切换到其他表盘，然后再切回来修复；或者更简单的办法就是重启手表。IT之家注：夏令时 / 冬令时是一种人为调整时钟的制度，通常是在夏季将时间拨快一小时，让人们在傍晚获得更多日照时间，从而减少照明用电，并更充分地利用自然光。夏令时结束、冬令时开始时，人们需要把时钟拨回一小时，让原本快一小时的时间恢复正常。在美国，2026 年夏令时开始于 3 月 8" data-title="苹果 Apple Watch 被曝冬令时显示异常：抬腕唤醒时间正常、放下慢一小时，重启即可修复" data-date="11-02 16:28" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-02 16:28</span>
          <span class="news-item-title">苹果 Apple Watch 被曝冬令时显示异常：抬腕唤醒时间正常、放下慢一小时，重启即可修复</span>
          <span class="news-value-point">💡 IT之家 11 月 2 日消息，据科技媒体 MacRumors 昨天报道，欧美国家切换成冬令时后，部分用户发现，他们手上的 Apple Watc…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/021/090.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 2 日消息，索尼 PlayStation Stars 奖励计划今日起正式永久关停，5 月 22 日起已停止新注册。索尼官方表示，在探索未来会员忠诚度计划新发展方向的同时，索尼也将通过已规划的各类社区活动持续回馈所有玩家。索尼表示，即使在这些变化发生之后，PlayStation Stars 会员仍然可以访问他们的数字收藏品。感谢所有玩家自 2022 年 PlayStation Stars 推出以来一直以来的支持。IT之家注意到，索尼 PlayStation Stars 服务于 2022 年 9 月上线，每一笔在 PlayStation Store 符合条件的消费，都能获得积分。所得到的积分可以换算成为 PSN 钱包金额，作为储蓄或下回在 PS Store 购买时花费、兑换成" data-title="索尼 PlayStation Stars 奖励计划今日起永久关停" data-date="11-02 16:21" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-02 16:21</span>
          <span class="news-item-title">索尼 PlayStation Stars 奖励计划今日起永久关停</span>
          <span class="news-value-point">💡 IT之家 11 月 2 日消息，索尼 PlayStation Stars 奖励计划今日起正式永久关停，5 月 22 日起已停止新注册</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-02/10724801.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在上海工作的刘先生在刷短视频时，认识了一位叫婷婷的美丽女子。双方网恋一段时间后，开始谈婚论嫁。然而刘先生想不到的是，他频频转账的这位“未婚妻”竟然是AI生成的。" data-title="7天“剧本”套路聊天 揭秘“AI生成女友”网恋诈骗流水线" data-date="11-02 16:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 16:20</span>
          <span class="news-item-title">7天“剧本”套路聊天 揭秘“AI生成女友”网恋诈骗流水线</span>
          <span class="news-value-point">💡 在上海工作的刘先生在刷短视频时，认识了一位叫婷婷的美丽女子</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-02/10724797.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网西宁11月2日电 救回来的雪豹没有放归，就是为了留着当“网红”？一段时间以来，围绕青海省野生动物救护繁育中心，网上出现了“圈养雪豹、兔狲只为博取流量”“不积极治疗、故意不放归”等说法。还有人将藏獒驱离雪豹的旧视频与雪豹幼崽获救的画面拼接，编造出“先放狗围攻，再送去救护”的情节。一场救护，就这样被说成了一场人为安排的“流量生意”。" data-title="救护雪豹咋就成了“流量生意”？丨真相" data-date="11-02 16:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 16:15</span>
          <span class="news-item-title">救护雪豹咋就成了“流量生意”？丨真相</span>
          <span class="news-value-point">💡 中新网西宁11月2日电 救回来的雪豹没有放归，就是为了留着当“网红”</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025492/man-utd-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Man Utd latest: Relegation certainly possible, says former boss Ten Hag" data-title="Man Utd latest: Relegation certainly possible, says former boss Ten Hag" data-date="11-02 15:55" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-02 15:55</span>
          <span class="news-item-title">曼联最新消息：前老板Ten Hag表示，降级当然是可能的</span>
          <span class="news-item-title-en">Man Utd latest: Relegation certainly possible, says former boss Ten Hag</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-02/10724793.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="剧本杀新玩法“恋陪本”为何引发争议衍生乱象？" data-title="虚拟恋爱背后的生意与迷局" data-date="11-02 15:51" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 15:51</span>
          <span class="news-item-title">虚拟恋爱背后的生意与迷局</span>
          <span class="news-value-point">💡 剧本杀新玩法“恋陪本”为何引发争议衍生乱象</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/01/us/politics/times-siena-poll-senate.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="《纽约时报》/锡耶纳的新民意调查发现，密歇根州、德克萨斯州、堪萨斯州、缅因州和俄亥俄州的民主党人占优势，在阿拉斯加州占据优势，与爱荷华州的共和党人实际上并驾齐驱。" data-title="Democrats Show Strength in Final Days of Race for the Senate, New Polls Find" data-date="11-02 15:49" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-02 15:49</span>
          <span class="news-item-title">民主党人在参议院竞选的最后几天显示出实力，新民意调查发现</span>
          <span class="news-item-title-en">Democrats Show Strength in Final Days of Race for the Senate, New Polls Find</span>
          <span class="news-value-point">💡 《纽约时报》/锡耶纳的新民意调查发现，密歇根州、德克萨斯州、堪萨斯州、缅因州和俄亥俄州的民主党人占优势，在阿拉斯加州占据优势，与爱荷华州的共和党…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-02/10724784.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网青海格尔木11月2日电 题：柴达木盆地涩北“采气人”：日巡检超两万步 守护气田“周全”" data-title="柴达木盆地涩北“采气人”：日巡检超两万步 守护气田“周全”" data-date="11-02 15:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 15:34</span>
          <span class="news-item-title">柴达木盆地涩北“采气人”：日巡检超两万步 守护气田“周全”</span>
          <span class="news-value-point">💡 中新网青海格尔木11月2日电 题：柴达木盆地涩北“采气人”：日巡检超两万步 守护气田“周全”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-02/10724777.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社长沙11月2日电 题：湖南乡村“变形记”：闲置资源激活文旅新消费" data-title="（走进中国乡村）湖南乡村“变形记”：闲置资源激活文旅新消费" data-date="11-02 15:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 15:30</span>
          <span class="news-item-title">（走进中国乡村）湖南乡村“变形记”：闲置资源激活文旅新消费</span>
          <span class="news-value-point">💡 中新社长沙11月2日电 题：湖南乡村“变形记”：闲置资源激活文旅新消费</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-02/10724759.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网邵阳11月2日电(李立颖 张晗)秋高气爽，大东山脚下，夜色四合。湖南隆回县六都寨镇张家铺村，刻着“中国村晚”字样的巨石旁，一支由当地农民组建的铜管乐团——“和乐团”正在舞台上演奏。明快的旋律，让隆回偏远的乡野热闹起来。" data-title="湖南隆回“村晚”点亮乡野  380个村搭起百姓舞台" data-date="11-02 15:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-02 15:21</span>
          <span class="news-item-title">湖南隆回“村晚”点亮乡野  380个村搭起百姓舞台</span>
          <span class="news-value-point">💡 中新网邵阳11月2日电(李立颖 张晗)秋高气爽，大东山脚下，夜色四合</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cm70pv70jwrjo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="BBC Sport调查了埃弗顿的年轻人对本赛季成功机会日益增长的影响。" data-title="No Grealish, no cry - the rise of Everton&#39;s youngsters" data-date="11-02 15:19" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-02 15:19</span>
          <span class="news-item-title">没有Grealish ，没有哭泣-埃弗顿的年轻人的崛起</span>
          <span class="news-item-title-en">No Grealish, no cry - the rise of Everton's youngsters</span>
          <span class="news-value-point">💡 BBC Sport调查了埃弗顿的年轻人对本赛季成功机会日益增长的影响</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/cricket/news/12040/13606943/marnus-labuschagne-australia-batter-set-to-be-dropped-after-not-taking-his-opportunity-in-south-africa-test-series" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Marnus Labuschagne在南非2-1系列赛失利后面临澳大利亚测试队的斧头，主教练Andrew McDonald说“他没有抓住这次巡回赛的机会”。" data-title="Labuschagne facing Australia axe after poor South Africa series?" data-date="11-02 15:09" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-02 15:09</span>
          <span class="news-item-title">在糟糕的南非系列之后， Labuschagne面对澳大利亚斧头？</span>
          <span class="news-item-title-en">Labuschagne facing Australia axe after poor South Africa series?</span>
          <span class="news-value-point">💡 Marnus Labuschagne在南非2-1系列赛失利后面临澳大利亚测试队的斧头，主教练Andrew McDonald说“他没有抓住这次巡回…</span>
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


<p class="news-updated">🕐 抓取更新于 2026-11-02 16:30（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
