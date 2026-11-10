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
      <span>2026-11-10 16:53 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num">9</span><span class="ov-label">独立信源</span></div>
  <div class="ov-item"><span class="ov-num">5</span><span class="ov-label">覆盖频道</span></div>
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×22 · 天空体育×12</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gj/2026/11-10/10729497.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月10日电 据俄罗斯媒体报道，新一轮俄美乌三方会谈10日在阿联酋首都阿布扎比开始举行。" data-title="新一轮俄美乌三方会谈在阿联酋开始举行" data-date="11-10 16:22" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 11-10 16:22</span>
      </div>
      <h2 class="hero-featured-title">新一轮俄美乌三方会谈在阿联酋开始举行</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/024/888.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 10 日消息，科技媒体 Ars Technica 昨日（11 月 9 日）发布博文，指出 AI 编程智能体 Claude Code 正在把部分开发者的敏感凭据意外暴露到公开的 GitHub 仓库中。安全公司 Apiiro 的研究人员发现，超过 10 万份 Claude Code 本地设置文件被上传至公共仓库，其中约 1,100 份文件含有数据库密码、API Token、私钥或 root 登录信息等机密数据。结合 Git 历史记录、共享设置文件及智能体聊天记录，共识别出 1,994 个代码库中的 2,539 个真实凭据。受影响对象包括 63 个组织，涵盖学生团队、初创企业、软件代理商及成熟供应商，泄露内容涉及 Azure 数据库密码、Square 生产令牌、SSH root" data-title="官方正在修复：Claude Code 被爆把密码写进项目文件，GitHub 上发现 2539 个真实凭据" data-date="11-10 16:45" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">官方正在修复：Claude Code 被爆把密码写进项目文件，GitHub 上发现 2539 个真实凭据</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/football/news/12040/13608837/james-penrice-scotland-and-rangers-defender-on-his-slow-rise-from-part-time-football-to-international-call-up" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="“我一直认为，如果我继续比赛并继续表演，它就会到来。谢天谢地，它做到了。”" data-title="Penrice on &#39;slow rise&#39; from part-time football to Scotland call-up" data-date="11-10 16:00" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">Penrice on 'slow rise' from part-time football to Scotland call-up</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/024/886.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 10 日消息，理想汽车法务部刚刚发文，就关于网络社群以“理想 i6 团购返佣”为名招募人员下单的情况作出声明，称该活动与理想汽车无关，并提醒广大用户警惕“下单返佣”等承诺。IT之家附理想汽车法务部声明原文如下：该活动与理想汽车无关，理想汽车未组织或授权任何组织、个人开展该活动。理想汽车已就相关情况向警方报案，并将积极配合调查。请广大用户警惕“下单返佣”等承诺，不要向不明身份人员提供订单信息、验证码等资料。如掌握相关线索，可发送至 legal@lixiang.com；如遭遇财产损失，请保存相关记录并及时报警。相关阅读：《理想汽车法务部：不法分子假借“理想汽车”名义发送诈骗短信，所称“召回事项”纯属虚构》延伸阅读理想 i6 是理想汽车旗下一款中大型五座纯电 SUV，基于原生纯" data-title="理想汽车法务部声明“理想 i6 团购返佣”活动与公司无关，已就相关情况向警方报案" data-date="11-10 16:43" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">理想汽车法务部声明“理想 i6 团购返佣”活动与公司无关，已就相关情况向警方报案</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-10/10729497.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月10日电 据俄罗斯媒体报道，新一轮俄美乌三方会谈10日在阿联酋首都阿布扎比开始举行。" data-title="新一轮俄美乌三方会谈在阿联酋开始举行" data-date="11-10 16:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 16:22</span>
          <span class="news-item-title">新一轮俄美乌三方会谈在阿联酋开始举行</span>
          <span class="news-value-point">💡 中新网11月10日电 据俄罗斯媒体报道，新一轮俄美乌三方会谈10日在阿联酋首都阿布扎比开始举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-10/10729499.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="日本执政党自民党及其执政伙伴日本维新会10日举行工作层磋商，讨论修订“安保三文件”等事宜。" data-title="日本自民党与维新会讨论修订“安保三文件”" data-date="11-10 16:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 16:22</span>
          <span class="news-item-title">日本自民党与维新会讨论修订“安保三文件”</span>
          <span class="news-value-point">💡 日本执政党自民党及其执政伙伴日本维新会10日举行工作层磋商，讨论修订“安保三文件”等事宜</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-10/10729490.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社快讯：据俄罗斯媒体报道，新一轮俄美乌三方会谈10日在阿联酋首都阿布扎比开始举行。" data-title="新一轮俄美乌三方会谈在阿布扎比开始举行" data-date="11-10 16:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 16:17</span>
          <span class="news-item-title">新一轮俄美乌三方会谈在阿布扎比开始举行</span>
          <span class="news-value-point">💡 新华社快讯：据俄罗斯媒体报道，新一轮俄美乌三方会谈10日在阿联酋首都阿布扎比开始举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-10/10729480.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月10日电 据中央纪委国家监委网站消息，近日，山东省纪委监委公开通报3起招标投标领域腐败问题典型案件，分别是：" data-title="山东通报3起招标投标领域腐败问题案件" data-date="11-10 16:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 16:11</span>
          <span class="news-item-title">山东通报3起招标投标领域腐败问题案件</span>
          <span class="news-value-point">💡 中新网11月10日电 据中央纪委国家监委网站消息，近日，山东省纪委监委公开通报3起招标投标领域腐败问题典型案件，分别是：</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-10/10729476.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京11月10日电#8195;中共中央党史和文献研究院编辑的习近平同志《论减贫脱贫》，近日由中央文献出版社出版，在全国发行。" data-title="习近平同志《论减贫脱贫》出版发行" data-date="11-10 16:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 16:09</span>
          <span class="news-item-title">习近平同志《论减贫脱贫》出版发行</span>
          <span class="news-value-point">💡 新华社北京11月10日电#8195;中共中央党史和文献研究院编辑的习近平同志《论减贫脱贫》，近日由中央文献出版社出版，在全国发行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-10/10729474.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月10日电 据英国《独立报》报道，美国总统特朗普当地时间9日在社交媒体上发文，质疑中期选举结果的公正性。对此，美国参议院民主党领袖查克·舒默回应称，特朗普质疑选举结果是“迟早会发生的事”。" data-title="特朗普质疑中期选举结果 民主党人回应：迟早的事" data-date="11-10 16:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 16:02</span>
          <span class="news-item-title">特朗普质疑中期选举结果 民主党人回应：迟早的事</span>
          <span class="news-value-point">💡 中新网11月10日电 据英国《独立报》报道，美国总统特朗普当地时间9日在社交媒体上发文，质疑中期选举结果的公正性</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-10/10729455.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社台北11月10日电 台湾当局内部事务主管部门10日公布统计显示，截至2026年10月底，台湾总人口为2320.4万人，连续34个月负增长。同期全台登记户数约993.9万户，创新高，平均每户人口为2.33人。" data-title="最新统计：台湾人口持续缩水 平均每户2.33人" data-date="11-10 16:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 16:00</span>
          <span class="news-item-title">最新统计：台湾人口持续缩水 平均每户2.33人</span>
          <span class="news-value-point">💡 中新社台北11月10日电 台湾当局内部事务主管部门10日公布统计显示，截至2026年10月底，台湾总人口为2320.4万人，连续34个月负增长</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-10/10729417.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社华盛顿11月10日电 (记者 陈孟统)美国总统特朗普9日在白宫表示，“从军事角度讲，伊朗战事实际上已经结束。我们只是维持现状。”" data-title="特朗普：伊朗战事从军事角度“实际上已结束”" data-date="11-10 15:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 15:49</span>
          <span class="news-item-title">特朗普：伊朗战事从军事角度“实际上已结束”</span>
          <span class="news-value-point">💡 中新社华盛顿11月10日电 (记者 陈孟统)美国总统特朗普9日在白宫表示，“从军事角度讲，伊朗战事实际上已经结束</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-10/10729457.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京11月10日电 (记者 谢雁冰)中国外交部发言人郭嘉昆10日主持例行记者会。" data-title="黄乐是否为中国公民？外交部回应" data-date="11-10 15:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 15:36</span>
          <span class="news-item-title">黄乐是否为中国公民？外交部回应</span>
          <span class="news-value-point">💡 中新网北京11月10日电 (记者 谢雁冰)中国外交部发言人郭嘉昆10日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-10/10729415.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间11月10日，日本东京地方法院就原自卫队官员村田晃大非法持刀侵闯中国驻日本大使馆一案开庭审理。检方要求判处被告人村田晃大1年6个月“拘禁刑”。" data-title="日本检方要求判处持刀强闯我驻日使馆人员村田晃大1年6个月刑期" data-date="11-10 15:00" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 15:00</span>
          <span class="news-item-title">日本检方要求判处持刀强闯我驻日使馆人员村田晃大1年6个月刑期</span>
          <span class="news-value-point">💡 当地时间11月10日，日本东京地方法院就原自卫队官员村田晃大非法持刀侵闯中国驻日本大使馆一案开庭审理</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/09/us/politics/hegseth-impeachment-massie.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="肯塔基州共和党众议员托马斯·马西（ Thomas Massie ）启动了必须在周三进行的投票。如果众议院批准这些指控，将促使参议院进行审判。" data-title="Thomas Massie Moves to Force Vote on Impeaching Pete Hegseth" data-date="11-10 06:35" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-10 06:35</span>
          <span class="news-item-title">托马斯·马西（ Thomas Massie ）动议对弹劾皮特·赫格塞斯（ Pete Hegseth</span>
          <span class="news-item-title-en">Thomas Massie Moves to Force Vote on Impeaching Pete Hegseth</span>
          <span class="news-value-point">💡 肯塔基州共和党众议员托马斯·马西（ Thomas Massie ）启动了必须在周三进行的投票</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-10/10729169.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="土耳其总统埃尔多安9日晚表示，当天伊兹密尔省阿利亚阿区一家钢铁厂发生的爆炸事故已造成16人死亡，13人受伤，其中2人伤势严重。" data-title="土耳其西部一钢铁厂发生爆炸 死亡人数升至16人" data-date="11-10 05:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 05:57</span>
          <span class="news-item-title">土耳其西部一钢铁厂发生爆炸 死亡人数升至16人</span>
          <span class="news-value-point">💡 土耳其总统埃尔多安9日晚表示，当天伊兹密尔省阿利亚阿区一家钢铁厂发生的爆炸事故已造成16人死亡，13人受伤，其中2人伤势严重</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-10/10729168.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间11月9日，坦桑尼亚警方表示，当天在该国伊林加省，一辆客车与一辆卡车相撞，造成至少21人死亡、5人受伤。" data-title="坦桑尼亚一客车与卡车相撞致21人死亡" data-date="11-10 05:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 05:56</span>
          <span class="news-item-title">坦桑尼亚一客车与卡车相撞致21人死亡</span>
          <span class="news-value-point">💡 当地时间11月9日，坦桑尼亚警方表示，当天在该国伊林加省，一辆客车与一辆卡车相撞，造成至少21人死亡、5人受伤</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-10/10729166.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="当地时间11月9日，美国肯塔基州共和党籍联邦众议员托马斯·梅西向众议院提交决议，试图推动全院就弹劾国防部长皮特·赫格塞思进行表决。此举意在向共和党同僚施压，要求他们就是否罢免特朗普政府中最引人注目的人物之一作出抉择。此前，共和党在选举中遭遇全面失利。" data-title="美众议员向众议院提交决议 要求弹劾国防部长赫格塞思" data-date="11-10 05:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 05:54</span>
          <span class="news-item-title">美众议员向众议院提交决议 要求弹劾国防部长赫格塞思</span>
          <span class="news-value-point">💡 当地时间11月9日，美国肯塔基州共和党籍联邦众议员托马斯·梅西向众议院提交决议，试图推动全院就弹劾国防部长皮特·赫格塞思进行表决</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-10/10729165.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="美国总统特朗普11月9日在其社交媒体上发帖，质疑美国中期选举，但没有提供证据支持。" data-title="特朗普质疑美国中期选举结果 称提前投票数据异常" data-date="11-10 05:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 05:53</span>
          <span class="news-item-title">特朗普质疑美国中期选举结果 称提前投票数据异常</span>
          <span class="news-value-point">💡 美国总统特朗普11月9日在其社交媒体上发帖，质疑美国中期选举，但没有提供证据支持</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/024/888.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 10 日消息，科技媒体 Ars Technica 昨日（11 月 9 日）发布博文，指出 AI 编程智能体 Claude Code 正在把部分开发者的敏感凭据意外暴露到公开的 GitHub 仓库中。安全公司 Apiiro 的研究人员发现，超过 10 万份 Claude Code 本地设置文件被上传至公共仓库，其中约 1,100 份文件含有数据库密码、API Token、私钥或 root 登录信息等机密数据。结合 Git 历史记录、共享设置文件及智能体聊天记录，共识别出 1,994 个代码库中的 2,539 个真实凭据。受影响对象包括 63 个组织，涵盖学生团队、初创企业、软件代理商及成熟供应商，泄露内容涉及 Azure 数据库密码、Square 生产令牌、SSH root" data-title="官方正在修复：Claude Code 被爆把密码写进项目文件，GitHub 上发现 2539 个真实凭据" data-date="11-10 16:45" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-10 16:45</span>
          <span class="news-item-title">官方正在修复：Claude Code 被爆把密码写进项目文件，GitHub 上发现 2539 个真实凭据</span>
          <span class="news-value-point">💡 IT之家 11 月 10 日消息，科技媒体 Ars Technica 昨日（11 月 9 日）发布博文，指出 AI 编程智能体 Claude C…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/024/887.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 10 日消息，据彭博社报道，随着人工智能投资热潮推动数据中心建设迅速扩张，泰国出台了针对数据中心噪音、热量和用水的新规定，为这一快速发展的行业设定了明确的环境限制。泰国经济规划机构秘书长丹努查 · 皮查亚南（Danucha Pichayanan）周二表示，内阁已批准相关规定。根据新规，数据中心的不间断电源系统运行时，噪音必须控制在约 70 分贝（A 计权分贝，dBA）以内。这一指标经过加权处理，能够更贴近人耳对声音大小的实际感受。此外，数据中心场地边界处的温度升幅将被限制在 1 至 2 摄氏度以内。冷却用水必须循环利用，排放的废水也必须接受检测。他还表示，位于工业园区内的数据中心设施将面临额外的要求。这套规定是泰国应对人工智能投资热潮的一部分。随着计算基础设施投资激增，泰" data-title="泰国给数据中心戴上“紧箍咒”：噪音限 70 分贝，温升不超 2 摄氏度" data-date="11-10 16:44" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-10 16:44</span>
          <span class="news-item-title">泰国给数据中心戴上“紧箍咒”：噪音限 70 分贝，温升不超 2 摄氏度</span>
          <span class="news-value-point">💡 IT之家 11 月 10 日消息，据彭博社报道，随着人工智能投资热潮推动数据中心建设迅速扩张，泰国出台了针对数据中心噪音、热量和用水的新规定，为…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/024/884.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 10 日消息，中微半导体设备（上海）股份有限公司（简称“中微公司”）近日发布其全新产品 ——Primo Matrix 双反应台等离子体晶圆切割设备，今日宣布首台设备已顺利付运国内重要集成电路封装客户。随着先进封装技术成为延续摩尔定律的重要路径，晶圆切割作为封装工艺中的关键环节，直接影响芯片良率与生产效率。针对先进封装对高精度、低损伤、窄切割道的迫切需求，中微公司在等离子晶圆切割设备领域取得重要突破，此次发布的新品 Primo Matrix 系列宣称是该公司在先进封装领域等离子体切割赛道的核心自主成果，并为该路线国产化落地增添头部方案选择。▲ 中微公司 Primo Matrix中微公司 Primo Matrix 采用在量产已得到充分验证的 Primo TSV 的等离子体深硅" data-title="国产再突破：中微公司首台等离子体晶圆切割设备成功交付国内重要集成电路封装客户" data-date="11-10 16:35" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-10 16:35</span>
          <span class="news-item-title">国产再突破：中微公司首台等离子体晶圆切割设备成功交付国内重要集成电路封装客户</span>
          <span class="news-value-point">💡 IT之家 11 月 10 日消息，中微半导体设备（上海）股份有限公司（简称“中微公司”）近日发布其全新产品 ——Primo Matrix 双反应…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-10/10729482.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网杭州11月10日电(郭其钰)员工离职前将客户名单等经营信息从公司系统导出，被老东家以侵犯商业秘密诉至法院。在科创企业集聚的浙江杭州高新区(滨江)，针对此类常见纠纷，法院构建覆盖数据技术、具身智能、数字经济等领域的咨询专家库，助科创企业守住“核心资产”。" data-title="员工离职带走公司商业信息 法院助科创企业守住“家底”" data-date="11-10 16:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 16:32</span>
          <span class="news-item-title">员工离职带走公司商业信息 法院助科创企业守住“家底”</span>
          <span class="news-value-point">💡 中新网杭州11月10日电(郭其钰)员工离职前将客户名单等经营信息从公司系统导出，被老东家以侵犯商业秘密诉至法院</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/09/us/politics/trump-jensen-huang-spy.html" target="_blank" rel="noopener" data-cat="keji" data-summary="特朗普总统周一告诉记者，他相信黄延森的说法，并表示他不记得收到过关于黄的联络警告他的简报。" data-title="Nvidia CEO Jensen Huang Told Trump He Did Not Know Chinese Woman Was Suspected Spy" data-date="11-10 10:13" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-10 10:13</span>
          <span class="news-item-title">英伟达首席执行官黄延森告诉特朗普他不知道中国女子涉嫌间谍</span>
          <span class="news-item-title-en">Nvidia CEO Jensen Huang Told Trump He Did Not Know Chinese Woman Was Suspected Spy</span>
          <span class="news-value-point">💡 特朗普总统周一告诉记者，他相信黄延森的说法，并表示他不记得收到过关于黄的联络警告他的简报</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/09/anthropic-reportedly-plans-to-move-forward-with-ipo-plans/" target="_blank" rel="noopener" data-cat="keji" data-summary="据《华尔街日报》报道，这家AI公司预计将在本周设定估值范围。" data-title="Anthropic reportedly plans to move forward with IPO plans" data-date="11-10 09:27" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-10 09:27</span>
          <span class="news-item-title">据报道， Anthropic计划推进IPO计划</span>
          <span class="news-item-title-en">Anthropic reportedly plans to move forward with IPO plans</span>
          <span class="news-value-point">💡 据《华尔街日报》报道，这家AI公司预计将在本周设定估值范围</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/big-tech/law-firm-files-class-action-lawsuit-against-nvidia-after-ceo-jensen-huang-confirms-affair-with-alleged-chinese-spy-more-to-come-as-multiple-other-law-firms-investigate-securities-fraud-following-stock-drop" target="_blank" rel="noopener" data-cat="keji" data-summary="针对英伟达证券欺诈的集体诉讼和法律调查开始浮出水面" data-title="Law firm files class-action lawsuit against Nvidia after CEO Jensen Huang confirms affair with alleged Chinese spy" data-date="11-10 08:03" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-10 08:03</span>
          <span class="news-item-title">在首席执行官Jensen Huang证实与涉嫌中国间谍有染后，律师事务所对英伟达提起集体诉讼</span>
          <span class="news-item-title-en">Law firm files class-action lawsuit against Nvidia after CEO Jensen Huang confirms affair with alleged Chinese spy</span>
          <span class="news-value-point">💡 针对英伟达证券欺诈的集体诉讼和法律调查开始浮出水面</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1030328/what-could-china-get-from-jensen-huang" target="_blank" rel="noopener" data-cat="keji" data-summary="在当今的人工智能格局中，很难夸大英伟达的力量。该公司的芯片是美国先进人工智能技术的基础，多年来需求一直超过供应。Nvidia也一直是影响" data-title="What could China get from Jensen Huang?" data-date="11-10 07:51" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-10 07:51</span>
          <span class="news-item-title">中国可以从Jensen Huang那里得到什么？</span>
          <span class="news-item-title-en">What could China get from Jensen Huang?</span>
          <span class="news-value-point">💡 在当今的人工智能格局中，很难夸大英伟达的力量</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/09/us/politics/democrats-trump-ai-nvidia.html" target="_blank" rel="noopener" data-cat="keji" data-summary="在英伟达(Nvidia)调查其首席执行官与一名中国间谍嫌疑人的婚外情时，国会领导人在一封信中提出了担忧。" data-title="Democrats Demand Answers on Trump’s A.I. Policy Amid Spy Plot" data-date="11-10 07:48" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-10 07:48</span>
          <span class="news-item-title">民主党人要求在间谍阴谋中回答特朗普的人工智能政策</span>
          <span class="news-item-title-en">Democrats Demand Answers on Trump’s A.I. Policy Amid Spy Plot</span>
          <span class="news-value-point">💡 在英伟达(Nvidia)调查其首席执行官与一名中国间谍嫌疑人的婚外情时，国会领导人在一封信中提出了担忧</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/1030446/trump-jensen-huang-press-conference" target="_blank" rel="noopener" data-cat="keji" data-summary="特朗普总统今天早些时候举行了白宫新闻发布会，并回答了有关他对Nvidia首席执行官Jensen Huang与一名涉嫌中国间谍事件的了解的几个问题。黄本周末说他对妻子“不忠”" data-title="Here’s what Trump said he knew about Jensen Huang" data-date="11-10 07:47" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-10 07:47</span>
          <span class="news-item-title">以下是特朗普所说的他对黄延森的了解</span>
          <span class="news-item-title-en">Here’s what Trump said he knew about Jensen Huang</span>
          <span class="news-value-point">💡 特朗普总统今天早些时候举行了白宫新闻发布会，并回答了有关他对Nvidia首席执行官Jensen Huang与一名涉嫌中国间谍事件的了解的几个问题</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/09/business/economy/nvidia-megaspeed-investigation-huang.html" target="_blank" rel="noopener" data-cat="keji" data-summary="在Nvidia的一名高管与商务部官员取得联系后，对购买高级Nvidia人工智能芯片的新加坡公司Megaspeed的调查被移交给了司法部。" data-title="U.S. Commerce Dept. Inquiry Into Megaspeed Was Halted After Nvidia Intervention" data-date="11-10 07:27" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-10 07:27</span>
          <span class="news-item-title">美国商务部对Megaspeed的调查在英伟达干预后停止</span>
          <span class="news-item-title-en">U.S. Commerce Dept. Inquiry Into Megaspeed Was Halted After Nvidia Intervention</span>
          <span class="news-value-point">💡 在Nvidia的一名高管与商务部官员取得联系后，对购买高级Nvidia人工智能芯片的新加坡公司Megaspeed的调查被移交给了司法部</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1030422/nvidia-jensen-huang-ai-china-alice-huang" target="_blank" rel="noopener" data-cat="keji" data-summary="Nvidia的皮夹克首席执行官Jensen Huang承认与Megaspeed高管Alice Huang有染，这引发了他的公司的调查，并在全球范围内进行了激烈的讨论。最近的报道指出，自去年以来，美国情报代表" data-title="Everything we know so far about the Nvidia spy scandal targeting CEO Jensen Huang" data-date="11-10 07:07" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-10 07:07</span>
          <span class="news-item-title">到目前为止，我们所知道的关于Nvidia针对首席执行官Jensen Huang的间谍丑闻的一切</span>
          <span class="news-item-title-en">Everything we know so far about the Nvidia spy scandal targeting CEO Jensen Huang</span>
          <span class="news-value-point">💡 Nvidia的皮夹克首席执行官Jensen Huang承认与Megaspeed高管Alice Huang有染，这引发了他的公司的调查，并在全球范…</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/09/a-short-seller-flagged-nvidia-ceos-ties-to-a-suspected-chinese-spy-six-months-before-the-scandal/" target="_blank" rel="noopener" data-cat="keji" data-summary="在英伟达间谍丑闻爆发六个月前， Culper Research已经在质疑Jensen Huang与一位中国高管的异常亲密的关系。" data-title="A short seller flagged Nvidia CEO’s ties to a suspected Chinese spy six months before the scandal" data-date="11-10 06:46" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-10 06:46</span>
          <span class="news-item-title">一名卖空者在丑闻发生前六个月标记了英伟达首席执行官与一名疑似中国间谍的关系</span>
          <span class="news-item-title-en">A short seller flagged Nvidia CEO’s ties to a suspected Chinese spy six months before the scandal</span>
          <span class="news-value-point">💡 在英伟达间谍丑闻爆发六个月前， Culper Research已经在质疑Jensen Huang与一位中国高管的异常亲密的关系</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/09/the-race-is-on-to-sue-nvidia/" target="_blank" rel="noopener" data-cat="keji" data-summary="英伟达董事会对Jensen Huang与一名中国间谍嫌疑人的关系展开调查后，英伟达股价下跌超过4% ，一名证券法专家表示，该公司早些时候坚持认为这一切都是“正常的” ，这可能会变成一个" data-title="The race is on to sue Nvidia" data-date="11-10 06:23" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-10 06:23</span>
          <span class="news-item-title">起诉英伟达的竞赛即将开始</span>
          <span class="news-item-title-en">The race is on to sue Nvidia</span>
          <span class="news-value-point">💡 英伟达董事会对Jensen Huang与一名中国间谍嫌疑人的关系展开调查后，英伟达股价下跌超过4% ，一名证券法专家表示，该公司早些时候坚持认为…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/09/business/nvidia-stock-price-jensen-huang-ceo.html" target="_blank" rel="noopener" data-cat="keji" data-summary="在首席执行官黄延森(Jensen Huang)承认与一名涉嫌为中国从事间谍活动的女商人发生关系后，这家芯片制造商的股价大幅下跌。" data-title="Nvidia’s Stock Price Drops After Investigation Into CEO Jensen Huang" data-date="11-10 05:23" data-source="纽约时报">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-10 05:23</span>
          <span class="news-item-title">英伟达对首席执行官黄延森进行调查后股价下跌</span>
          <span class="news-item-title-en">Nvidia’s Stock Price Drops After Investigation Into CEO Jensen Huang</span>
          <span class="news-value-point">💡 在首席执行官黄延森(Jensen Huang)承认与一名涉嫌为中国从事间谍活动的女商人发生关系后，这家芯片制造商的股价大幅下跌</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13608837/james-penrice-scotland-and-rangers-defender-on-his-slow-rise-from-part-time-football-to-international-call-up" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="“我一直认为，如果我继续比赛并继续表演，它就会到来。谢天谢地，它做到了。”" data-title="Penrice on &#39;slow rise&#39; from part-time football to Scotland call-up" data-date="11-10 16:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 16:00</span>
          <span class="news-item-title">Penrice谈从兼职足球到苏格兰征召的“缓慢崛起”</span>
          <span class="news-item-title-en">Penrice on 'slow rise' from part-time football to Scotland call-up</span>
          <span class="news-value-point">💡 “我一直认为，如果我继续比赛并继续表演，它就会到来</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/cricket/news/12040/13610462/sandpapergate-mitchell-starc-denies-knowledge-after-usman-khawaja-claims-as-cricket-australia-says-investigation-will-not-be-re-opened" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在前队友Usman Khawaja爆炸性地声称整个更衣室都知道2018年南非的球篡改计划之后，澳大利亚快速投球手Mitchell Starc否认了“Sandpapergate”的任何先前知识。" data-title="Starc denies Khawaja claims as Cricket Australia says investigation won&#39;t reopen" data-date="11-10 15:45" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 15:45</span>
          <span class="news-item-title">Starc否认Khawaja的说法，因为Cricket Australia表示调查不会重新开始</span>
          <span class="news-item-title-en">Starc denies Khawaja claims as Cricket Australia says investigation won't reopen</span>
          <span class="news-value-point">💡 在前队友Usman Khawaja爆炸性地声称整个更衣室都知道2018年南非的球篡改计划之后，澳大利亚快速投球手Mitchell Starc否认…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmy0r041ed0po?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）的曼联统治似乎在俱乐部40年来最糟糕的国内竞选开始后接近尾声。" data-title="Man Utd expected to sack head coach Carrick" data-date="11-10 07:13" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-10 07:13</span>
          <span class="news-item-title">曼联预计将解雇主教练卡里克</span>
          <span class="news-item-title-en">Man Utd expected to sack head coach Carrick</span>
          <span class="news-value-point">💡 迈克尔·卡里克（ Michael Carrick ）的曼联统治似乎在俱乐部40年来最糟糕的国内竞选开始后接近尾声</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13610412/michael-carrick-future-man-utd-head-coach-position-increasingly-in-doubt-but-no-final-decision-made" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="迈克尔·卡里克（ Michael Carrick ）作为曼联主教练的地位越来越令人怀疑，但天空体育新闻（ Sky Sports News ）迄今为止已被告知，尚未就他在老特拉福德的未来做出最终决定。" data-title="Carrick&#39;s position increasingly in doubt" data-date="11-10 07:04" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 07:04</span>
          <span class="news-item-title">卡里克的立场越来越令人怀疑</span>
          <span class="news-item-title-en">Carrick's position increasingly in doubt</span>
          <span class="news-value-point">💡 迈克尔·卡里克（ Michael Carrick ）作为曼联主教练的地位越来越令人怀疑，但天空体育新闻（ Sky Sports News ）迄今…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cw4g1g7z2mdgo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼联董事会尚未对迈克尔·卡里克的未来做出最终决定，尽管这是俱乐部40年来最糟糕的一场比赛。" data-title="Man Utd yet to make decision on Carrick&#39;s future" data-date="11-10 01:49" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-10 01:49</span>
          <span class="news-item-title">曼联尚未就卡里克的未来做出决定</span>
          <span class="news-item-title-en">Man Utd yet to make decision on Carrick's future</span>
          <span class="news-value-point">💡 曼联董事会尚未对迈克尔·卡里克的未来做出最终决定，尽管这是俱乐部40年来最糟糕的一场比赛</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13610315/michael-carrick-future-man-utd-will-not-rush-decision-over-head-coachs-tenure-despite-dropping-into-relegation-zone" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在4-4战平阿斯顿维拉之后，曼联的老板们不会急于就迈克尔卡里克的未来做出决定，这让他们处于降级区。" data-title="Man Utd will not rush decision on Carrick future" data-date="11-10 00:52" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 00:52</span>
          <span class="news-item-title">曼联不会急于决定卡里克的未来</span>
          <span class="news-item-title-en">Man Utd will not rush decision on Carrick future</span>
          <span class="news-value-point">💡 在4-4战平阿斯顿维拉之后，曼联的老板们不会急于就迈克尔卡里克的未来做出决定，这让他们处于降级区</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13610315/michael-carrick-future-man-utd-will-not-rush-decision-over-head-coachs-tenure-despite-dropping-into-relegation-zone" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在4-4战平阿斯顿维拉之后，曼联的老板们不会急于就迈克尔卡里克的未来做出决定，这让他们处于降级区。" data-title="Man Utd will not rush decision on Carrick future" data-date="11-10 00:52" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 00:52</span>
          <span class="news-item-title">曼联不会急于决定卡里克的未来</span>
          <span class="news-item-title-en">Man Utd will not rush decision on Carrick future</span>
          <span class="news-value-point">💡 在4-4战平阿斯顿维拉之后，曼联的老板们不会急于就迈克尔卡里克的未来做出决定，这让他们处于降级区</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/09/manchester-city-enzo-maresca-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在连续三场失利后，曼城的经理表示，他将利用国际休息时间重新评估。他们的问题可能不仅仅是战术在这里注册我们的免费通讯恩佐·马雷斯卡（ Enzo Maresca ）似乎对他周六击败诺特感到困惑" data-title="Manchester City’s weaknesses under Enzo Maresca are being exposed" data-date="11-10 00:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-10 00:30</span>
          <span class="news-item-title">曼城在恩佐·马雷斯卡（ Enzo Maresca ）领导下的弱点正在暴露</span>
          <span class="news-item-title-en">Manchester City’s weaknesses under Enzo Maresca are being exposed</span>
          <span class="news-value-point">💡 在连续三场失利后，曼城的经理表示，他将利用国际休息时间重新评估</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13610134/manchester-united-the-key-questions-with-michael-carricks-future-still-up-in-the-air-at-old-trafford" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在周日以4比4战平阿斯顿维拉之后，迈克尔·卡里克在曼联的未来仍然是一个谜。" data-title="The key questions for Man Utd and Carrick after history" data-date="11-09 23:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-09 23:00</span>
          <span class="news-item-title">曼联和卡里克历史上的关键问题</span>
          <span class="news-item-title-en">The key questions for Man Utd and Carrick after history</span>
          <span class="news-value-point">💡 在周日以4比4战平阿斯顿维拉之后，迈克尔·卡里克在曼联的未来仍然是一个谜</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13610134/manchester-united-the-key-questions-with-michael-carricks-future-still-up-in-the-air-at-old-trafford" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在周日以4比4战平阿斯顿维拉之后，迈克尔·卡里克在曼联的未来仍然是一个谜。" data-title="What now for Man Utd and Carrick?" data-date="11-09 23:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-09 23:00</span>
          <span class="news-item-title">曼联和卡里克现在该怎么办？</span>
          <span class="news-item-title-en">What now for Man Utd and Carrick?</span>
          <span class="news-value-point">💡 在周日以4比4战平阿斯顿维拉之后，迈克尔·卡里克在曼联的未来仍然是一个谜</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c6n9r93dnr9do?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="本周末，英超联赛中几乎每场比赛都有一个有争议的VAR决定。但是，有多少可能会作为错误记录下来？" data-title="Incident-by-incident: Was it a bad weekend for VAR?" data-date="11-09 22:34" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-09 22:34</span>
          <span class="news-item-title">逐个事件：对于VAR来说，这是一个糟糕的周末吗？</span>
          <span class="news-item-title-en">Incident-by-incident: Was it a bad weekend for VAR?</span>
          <span class="news-value-point">💡 本周末，英超联赛中几乎每场比赛都有一个有争议的VAR决定</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/dram/memory-shortage-spurs-smartphone-makers-to-melt-used-memory-off-old-devices-then-re-solder-it-onto-new-products-recycled-memory-to-keep-budget-phones-affordable-reballing-adoption-to-double-by-2027" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="重新包装的内存目前只占智能手机组件的一小部分，但由于制造商正在寻找日益昂贵的DRAM的替代品，到2027年采用率可能会增加近一倍。" data-title="Memory shortage spurs smartphone makers to melt used memory off old devices, then re-solder it onto new products" data-date="11-09 21:40" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-09 21:40</span>
          <span class="news-item-title">内存短缺促使智能手机制造商融化旧设备的废旧内存，然后将其重新焊接到新产品上</span>
          <span class="news-item-title-en">Memory shortage spurs smartphone makers to melt used memory off old devices, then re-solder it onto new products</span>
          <span class="news-value-point">💡 重新包装的内存目前只占智能手机组件的一小部分，但由于制造商正在寻找日益昂贵的DRAM的替代品，到2027年采用率可能会增加近一倍</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025501/liverpool-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Liverpool latest: Van Dijk pulls out of Netherlands squad" data-title="Liverpool latest: Van Dijk pulls out of Netherlands squad" data-date="11-09 21:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-09 21:00</span>
          <span class="news-item-title">利物浦最新消息：范迪克退出荷兰队</span>
          <span class="news-item-title-en">Liverpool latest: Van Dijk pulls out of Netherlands squad</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c98rzr51rlvpo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="切尔西警告工作人员要小心通过幻想英超联赛透露球队新闻，因为Joao Pedro的伤势似乎在球队选择中被无意中透露。" data-title="Chelsea staff warned over Fantasy Premier League use" data-date="11-09 20:41" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-09 20:41</span>
          <span class="news-item-title">切尔西工作人员警告使用Fantasy Premier League</span>
          <span class="news-item-title-en">Chelsea staff warned over Fantasy Premier League use</span>
          <span class="news-value-point">💡 切尔西警告工作人员要小心通过幻想英超联赛透露球队新闻，因为Joao Pedro的伤势似乎在球队选择中被无意中透露</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/11661/13610181/alisson-liverpool-goalkeeper-wants-to-stay-at-anfield-beyond-contract-expiry-at-the-end-of-this-season" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦守门员阿利森表示，他希望在合同到期后的赛季结束后继续留在安菲尔德。" data-title="&#39;My will is to stay&#39; - Alisson wants new Liverpool contract" data-date="11-09 20:38" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-09 20:38</span>
          <span class="news-item-title">“我的意愿是留下来” - Alisson想要新的利物浦合同</span>
          <span class="news-item-title-en">'My will is to stay' - Alisson wants new Liverpool contract</span>
          <span class="news-value-point">💡 利物浦守门员阿利森表示，他希望在合同到期后的赛季结束后继续留在安菲尔德</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/024/886.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 10 日消息，理想汽车法务部刚刚发文，就关于网络社群以“理想 i6 团购返佣”为名招募人员下单的情况作出声明，称该活动与理想汽车无关，并提醒广大用户警惕“下单返佣”等承诺。IT之家附理想汽车法务部声明原文如下：该活动与理想汽车无关，理想汽车未组织或授权任何组织、个人开展该活动。理想汽车已就相关情况向警方报案，并将积极配合调查。请广大用户警惕“下单返佣”等承诺，不要向不明身份人员提供订单信息、验证码等资料。如掌握相关线索，可发送至 legal@lixiang.com；如遭遇财产损失，请保存相关记录并及时报警。相关阅读：《理想汽车法务部：不法分子假借“理想汽车”名义发送诈骗短信，所称“召回事项”纯属虚构》延伸阅读理想 i6 是理想汽车旗下一款中大型五座纯电 SUV，基于原生纯" data-title="理想汽车法务部声明“理想 i6 团购返佣”活动与公司无关，已就相关情况向警方报案" data-date="11-10 16:43" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-10 16:43</span>
          <span class="news-item-title">理想汽车法务部声明“理想 i6 团购返佣”活动与公司无关，已就相关情况向警方报案</span>
          <span class="news-value-point">💡 IT之家 11 月 10 日消息，理想汽车法务部刚刚发文，就关于网络社群以“理想 i6 团购返佣”为名招募人员下单的情况作出声明，称该活动与理想…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-10/10729487.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网西宁11月10日电 (记者 孙睿)11月10日，青海省政府新闻办公室召开“筑牢基层健康服务网底开启‘十五五’惠民新征程”新闻发布会。青海省卫生健康委党组成员、副主任端智介绍，截至2025年底，青海共有基层医疗卫生机构6544个，基层诊疗量占比提升至44.8%。看病不出远门，正成为青海农牧民的生活常态。" data-title="青海基层医疗提质扩容 基层诊疗量占比升至44.8%" data-date="11-10 16:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 16:34</span>
          <span class="news-item-title">青海基层医疗提质扩容 基层诊疗量占比升至44.8%</span>
          <span class="news-value-point">💡 中新网西宁11月10日电 (记者 孙睿)11月10日，青海省政府新闻办公室召开“筑牢基层健康服务网底开启‘十五五’惠民新征程”新闻发布会</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/024/883.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 10 日消息，博主 @刹那数码 发文，透露为迎合全新交互，过几年 iPhone 直板机会调整屏幕比例，时间点“大概就是正面只剩一个挖孔，甚至彻底实现屏下摄像头的那一年”。该博主后续补充“也有业内人士讲后年 2028 就无挖孔”。该博主表示，后续苹果不会继续把屏幕做宽，而是会把机身做短一点，相当于直接砍掉现在顶部状态栏占据的那部分高度。屏幕从现在的 19.5:9，变成接近 18:9，让握持和单手操作更舒服一些。尽管屏幕变短，但显示的信息不会减少。顶部的操作区会和状态栏整合到同一行，不再单独占用一层空间。IT之家注意到，苹果 iPhone 现行的 19.5:9 屏幕比例最早由 2017 年发布的 iPhone X 引入，该机首次采用 OLED 全面屏并带来刘海设计；在此之前，" data-title="消息称苹果 iPhone 直板机未来将调整屏幕比例：从 19.5:9 改为接近 18:9" data-date="11-10 16:34" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-10 16:34</span>
          <span class="news-item-title">消息称苹果 iPhone 直板机未来将调整屏幕比例：从 19.5:9 改为接近 18:9</span>
          <span class="news-value-point">💡 IT之家 11 月 10 日消息，博主 @刹那数码 发文，透露为迎合全新交互，过几年 iPhone 直板机会调整屏幕比例，时间点“大概就是正面只…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/024/881.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 10 日消息，星闪联盟官网显示，一款型号为“SL10”的音箱产品已通过测试列名，归属深圳市因科美通信有限公司旗下（即 EACOME 品牌）。测试集显示，EACOME SL10 音箱通过了 SLE 射频一致性测试、基础服务层协议一致性测试、高清音频协议一致性测试。这意味着，这款音箱将支持 NearLink E2.0（即星闪音频）。根据官方描述，星闪音频物理层传输速率可达 16Mbps，带宽能力超传统技术，充足的通道容量就能够承载 48kHz/24bit Hi-Fi 音频无损传输。IT之家注：目前支持星闪音频的耳机包括 FreeClip 2 典藏版、FreeClip 2、FreeBuds Pro 5 等。延伸阅读星闪（NearLink）是由国际星闪联盟主导的新一代无线短距通信" data-title="首款星闪音箱将至！归属 EACOME 品牌旗下、支持 NearLink E2.0，型号“SL10”" data-date="11-10 16:31" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-10 16:31</span>
          <span class="news-item-title">首款星闪音箱将至！归属 EACOME 品牌旗下、支持 NearLink E2.0，型号“SL10”</span>
          <span class="news-value-point">💡 IT之家 11 月 10 日消息，星闪联盟官网显示，一款型号为“SL10”的音箱产品已通过测试列名，归属深圳市因科美通信有限公司旗下（即 EAC…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/11661/13025492/man-utd-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Man Utd latest: Carrick arrives at training ground" data-title="Man Utd latest: Carrick arrives at training ground" data-date="11-10 16:25" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 16:25</span>
          <span class="news-item-title">曼联最新消息：卡里克抵达训练场</span>
          <span class="news-item-title-en">Man Utd latest: Carrick arrives at training ground</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cjr4y41lv6zko/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="辉达黄仁勋承认对妻子不忠，绯闻锁定被指中共间谍的黄乐。这位女子曾任新加坡科技公司高管，大量采购辉达芯片，美情报称她受国安部招募。但特朗普（川普）为黄仁勋辩护，中方则否认指控。" data-title="黄仁勋婚外情：被指为“中共间谍”的黄乐是谁？" data-date="11-10 16:24" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-10 16:24</span>
          <span class="news-item-title">黄仁勋婚外情：被指为“中共间谍”的黄乐是谁？</span>
          <span class="news-value-point">💡 辉达黄仁勋承认对妻子不忠，绯闻锁定被指中共间谍的黄乐</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-10/10729489.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="4561名“小叶子”，9大类158个岗位，还有65名来自港澳台的志愿者——本届进博会，他们如约而至，与“四叶草”一起长大。三位志愿者的故事，三种截然不同的成长轨迹。" data-title="“四叶草”上的年轮：小叶子和进博会共同成长" data-date="11-10 16:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 16:15</span>
          <span class="news-item-title">“四叶草”上的年轮：小叶子和进博会共同成长</span>
          <span class="news-value-point">💡 4561名“小叶子”，9大类158个岗位，还有65名来自港澳台的志愿者——本届进博会，他们如约而至，与“四叶草”一起长大</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/boxing/news/12040/13610207/denzel-bentley-id-happily-go-to-ireland-beat-aaron-mckenna-in-his-home-town-and-bring-the-belt-back-to-england" target="_blank" rel="noopener" data-cat="zonghe" data-summary="丹泽尔·本特利（ Denzel Bentley ）在周六击败小谢恩·莫斯利（ Shane Mosley Jr. ）后，希望再次赢得世界冠" data-title="Bentley: I&#39;d happily go to Ireland and beat McKenna in his home town!" data-date="11-10 16:15" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 16:15</span>
          <span class="news-item-title">Bentley ：我很乐意去爱尔兰，在他的家乡击败McKenna ！</span>
          <span class="news-item-title-en">Bentley: I'd happily go to Ireland and beat McKenna in his home town!</span>
          <span class="news-value-point">💡 丹泽尔·本特利（ Denzel Bentley ）在周六击败小谢恩·莫斯利（ Shane Mosley Jr. ）后，希望再次赢得世界冠</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-10/10729484.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="第九届进博会热力十足、人气满满" data-title="老外“逛”进博：一边Chinamaxxing，一边China Haul" data-date="11-10 16:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 16:09</span>
          <span class="news-item-title">老外“逛”进博：一边Chinamaxxing，一边China Haul</span>
          <span class="news-value-point">💡 第九届进博会热力十足、人气满满</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-10/10729479.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="央广网烟台11月10日消息(记者刘佳音)黄渤海交汇处，碧海环抱着连绵岛礁。当海风掠过山东烟台长岛的渔村街巷，新型渔家乐小院里，一场关于算“碳账”的绿色实践，正在海岸线上铺展出一条海岛转型新路。" data-title="行进的海岸线｜黄渤海交汇处澎湃全球海岛绿色新动能" data-date="11-10 16:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 16:04</span>
          <span class="news-item-title">行进的海岸线｜黄渤海交汇处澎湃全球海岛绿色新动能</span>
          <span class="news-value-point">💡 央广网烟台11月10日消息(记者刘佳音)黄渤海交汇处，碧海环抱着连绵岛礁</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-10/10729462.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京11月10日电 (记者 程小路)在孙中山先生诞辰160周年之际，“薪火传志续华章——孙中山、宋庆龄与中国共产党”展览9日在国家名誉主席宋庆龄同志故居开幕。中国宋庆龄基金会党组书记、副主席沈蓓莉，孙中山先生玄侄孙、中国宋庆龄基金会理事、香港宋庆龄基金副会长孙伟勇等出席开幕式。" data-title="“薪火传志续华章——孙中山、宋庆龄与中国共产党”展览在京开幕" data-date="11-10 16:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 16:02</span>
          <span class="news-item-title">“薪火传志续华章——孙中山、宋庆龄与中国共产党”展览在京开幕</span>
          <span class="news-value-point">💡 中新网北京11月10日电 (记者 程小路)在孙中山先生诞辰160周年之际，“薪火传志续华章——孙中山、宋庆龄与中国共产党”展览9日在国家名誉主席…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-10/10729443.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京11月10日电 (记者 谢雁冰)中国外交部发言人郭嘉昆10日主持例行记者会。" data-title="旅美大熊猫“平平”“福双”正式与公众见面 外交部回应" data-date="11-10 15:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 15:27</span>
          <span class="news-item-title">旅美大熊猫“平平”“福双”正式与公众见面 外交部回应</span>
          <span class="news-value-point">💡 中新网北京11月10日电 (记者 谢雁冰)中国外交部发言人郭嘉昆10日主持例行记者会</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-10/10729418.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网11月10日电 综合外媒报道，法国柔道传奇人物、五届奥运柔道冠军特迪·里内9日在社交媒体宣布，他将参加下一届法国总统选举。此前，他曾对法国“极右翼势力抬头”表达担忧。" data-title="奥运冠军宣布竞选法国总统 马克龙表态：欢迎" data-date="11-10 15:19" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-10 15:19</span>
          <span class="news-item-title">奥运冠军宣布竞选法国总统 马克龙表态：欢迎</span>
          <span class="news-value-point">💡 中新网11月10日电 综合外媒报道，法国柔道传奇人物、五届奥运柔道冠军特迪·里内9日在社交媒体宣布，他将参加下一届法国总统选举</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/09/otter-ai-can-now-follow-conversations-across-30-languages/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="Otter AI刚刚增加了对27种语言的支持，并揭示了一个即将推出的功能，如果说话者在语言之间切换，可以随之而来。" data-title="Otter AI can now follow conversations across 30+ languages" data-date="11-10 15:00" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-10 15:00</span>
          <span class="news-item-title">Otter AI现在可以跟踪30多种语言的对话</span>
          <span class="news-item-title-en">Otter AI can now follow conversations across 30+ languages</span>
          <span class="news-value-point">💡 Otter AI刚刚增加了对27种语言的支持，并揭示了一个即将推出的功能，如果说话者在语言之间切换，可以随之而来</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/darts/news/12040/13610214/grand-slam-of-darts-2026-schedule-new-format-players-prize-money-past-winners-as-luke-littler-looks-to-retain-title" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在2026年飞镖大满贯之前，看看你需要知道的一切，包括新的形式、时间表、过去的获奖者，以及增加的奖金..." data-title="Grand Slam of Darts 2026: Schedule, new format, players, prize money, past winners" data-date="11-10 15:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-10 15:00</span>
          <span class="news-item-title">2026年飞镖大满贯：时间表、新格式、玩家、奖金、过往获奖者</span>
          <span class="news-item-title-en">Grand Slam of Darts 2026: Schedule, new format, players, prize money, past winners</span>
          <span class="news-value-point">💡 在2026年飞镖大满贯之前，看看你需要知道的一切，包括新的形式、时间表、过去的获奖者，以及增加的奖金...</span>
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


<p class="news-updated">🕐 抓取更新于 2026-11-10 16:53（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
