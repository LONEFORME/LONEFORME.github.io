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
      <span>2026-09-05 14:24 抓取更新</span>
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
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/09-05/10690893.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="9月5日，中国建筑集团有限公司党组召开会议，通报中央纪委国家监委对中建集团党组成员、副总经理陈勇涉嫌严重违纪违法进行纪律审查和监察调查的决定。中建集团党组书记、董事长郑学选主持会议并讲话，党组成员逐一表态发言，一致表示坚决拥护党中央决定，坚决拥护中央纪委国家监委决定。" data-title="中建集团党组：坚决拥护党中央决定" data-date="09-05 13:28" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 09-05 13:28</span>
      </div>
      <h2 class="hero-featured-title">中建集团党组：坚决拥护党中央决定</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/0/998/739.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 5 日消息，在接受《华盛顿邮报》采访时，顽皮狗工作室负责人尼尔 · 德鲁克曼（Neil Druckmann）透露，团队正为《最后生还者》（The Last of Us）筹备多个项目。德鲁克曼并未透露更多细节，只是确认工作室正在开发“几个项目”，也没有明确说明这些项目是否均为游戏。IT之家援引博文介绍，顽皮狗工作室的开发重心目前放在《星际：异端先知》（Intergalactic: The Heretic Prophet）方面，如果该工作室在推进《最后生还者》相关游戏项目，其发行日期可能会晚于《星际：异端先知》。《最后生还者》系列目前最后一款正式发售的游戏是 《The Last of Us Part II Remastered》，于 2025 年 1 月登陆 PS5，随后也推出" data-title="《最后生还者》游戏新动向：顽皮狗确认多个项目筹备中" data-date="09-05 13:58" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">《最后生还者》游戏新动向：顽皮狗确认多个项目筹备中</p>
    </a>
    <a class="hero-sub-card" href="https://www.bbc.co.uk/sport/football/articles/c209xvxe558o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="首席足球作家菲尔·麦克纳尔蒂问道，在英超联赛战胜伊普斯维奇的比赛中梅开二度后，真正的亚历山大·伊萨克终于抵达利物浦了吗？" data-title="伊萨克终于到来，加克波证明了对利物浦的价值" data-date="09-05 06:37" data-source="BBC">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-bbc">🇬🇧 BBC</span>
      </div>
      <p class="hero-sub-title">伊萨克终于到来，加克波证明了对利物浦的价值</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/gn/2026/09-05/10690906.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="9月5日，江西省遂川县高坪镇明坑村石下组发生泥石流和山体滑坡，应急管理部立即调度部署抢险救援工作，要求全力搜救被困人员，核实核清伤亡失联人数，就近调派通信保障、工程抢险等队伍装备，尽快组织救援人员挺进灾区，加强水文、地质灾害监测预警，科学施救，严防次生灾害发生。" data-title="应急管理部调度江西遂川泥石流灾害救援 派出工作组赶赴现场" data-date="09-05 14:14" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">应急管理部调度江西遂川泥石流灾害救援 派出工作组赶赴现场</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-05/10690893.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="9月5日，中国建筑集团有限公司党组召开会议，通报中央纪委国家监委对中建集团党组成员、副总经理陈勇涉嫌严重违纪违法进行纪律审查和监察调查的决定。中建集团党组书记、董事长郑学选主持会议并讲话，党组成员逐一表态发言，一致表示坚决拥护党中央决定，坚决拥护中央纪委国家监委决定。" data-title="中建集团党组：坚决拥护党中央决定" data-date="09-05 13:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-05 13:28</span>
          <span class="news-item-title">中建集团党组：坚决拥护党中央决定</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-05/10690828.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月5日电 拉巴斯消息：当地时间4日下午，玻利维亚西部拉巴斯省维亚查镇一处军营发生爆炸，已造成至少58人受伤。" data-title="玻利维亚一军营爆炸造成至少58人受伤" data-date="09-05 12:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-05 12:06</span>
          <span class="news-item-title">玻利维亚一军营爆炸造成至少58人受伤</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-05/10690827.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月5日电 综合消息：以色列军方4日表示，在黎巴嫩真主党对以士兵发动无人机袭击后，以色列对黎巴嫩南部进行了打击。" data-title="以色列空袭黎巴嫩南部致5死23伤" data-date="09-05 12:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-05 12:05</span>
          <span class="news-item-title">以色列空袭黎巴嫩南部致5死23伤</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-05/10690824.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网北京9月5日电 (记者 孙自法)国际学术期刊《自然》最新发表一篇遗传学论文称，研究人员通过对超过100万名参与者的数据进行荟萃分析，识别出1000多个与人类五大人格相关的基因遗传变异。" data-title="五大人格与基因有何关联？国际最新研究识别1000多个相关遗传变异" data-date="09-05 12:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-05 12:05</span>
          <span class="news-item-title">五大人格与基因有何关联？国际最新研究识别1000多个相关遗传变异</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-05/10690836.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社加德满都9月4日电#8195;专访｜“中国政府给予我们的支持是全方位的！”——访尼泊尔外交部长希西尔" data-title="专访｜“中国政府给予我们的支持是全方位的！”" data-date="09-05 11:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-05 11:04</span>
          <span class="news-item-title">专访｜“中国政府给予我们的支持是全方位的！”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-05/10690830.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="比什凯克峰会有望为上合组织承前启后、继往开来注入新的动力，推动上合组织各领域合作不断迈上新台阶" data-title="推动上合组织合作取得更多务实成果（国际论坛）" data-date="09-05 10:57" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-05 10:57</span>
          <span class="news-item-title">推动上合组织合作取得更多务实成果（国际论坛）</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-05/10690809.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月5日电 据路透社报道，玻利维亚地方政府称，当地时间4日，该国西部比亚查市一处军营发生爆炸，已造成数十人死伤。" data-title="玻利维亚一军营发生爆炸 已造成数十人死伤" data-date="09-05 10:25" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-05 10:25</span>
          <span class="news-item-title">玻利维亚一军营发生爆炸 已造成数十人死伤</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/04/us/politics/pentagon-staff-polygraph-tests.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="大约 50 人接受了测试，这是在有关伊朗战争和美军弹药库存减少的新闻报道之后进行的一次前所未有的调查。" data-title="在重大泄密搜寻中，五角大楼对联合参谋人员进行测谎测试" data-date="09-05 10:08" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-05 10:08</span>
          <span class="news-item-title">在重大泄密搜寻中，五角大楼对联合参谋人员进行测谎测试</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/04/us/politics/judge-blocks-trump-mail-ballots.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="该裁决是在最高法院决定是否干预之前做出的，但似乎肯定会引发另一轮上诉。" data-title="法官再次阻止特朗普政府限制邮件的计划" data-date="09-05 07:27" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-05 07:27</span>
          <span class="news-item-title">法官再次阻止特朗普政府限制邮件的计划</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/04/us/politics/trump-pardons-drug-offenders-union-boss.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="周四，总统对 30 人发出赦免或减刑，继续以非正统且不可预测的方式使用特赦权。" data-title="特朗普最新的特赦补助金有利于毒品犯罪者、工会老板" data-date="09-05 06:57" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-05 06:57</span>
          <span class="news-item-title">特朗普最新的特赦补助金有利于毒品犯罪者、工会老板</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/04/us/politics/trump-administration-fund-compensation-jan-6.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="设立一个基金的计划可以将纳税人的钱输送给总统的盟友，这一计划引起了反复的审查，包括来自参议院共和党人的罕见谴责。" data-title="法官命令特朗普官员透露 18 亿美元基金设立者的姓名" data-date="09-05 04:52" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-05 04:52</span>
          <span class="news-item-title">法官命令特朗普官员透露 18 亿美元基金设立者的姓名</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/04/us/politics/trump-qatar-jet-flight-ireland.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="总统打算乘坐这架飞机前往爱尔兰，这是自有人对其防御能力提出质疑以来，他首次在海外使用这架飞机。" data-title="尽管存在安全问题，特朗普仍计划使用卡塔尔喷气机进行另一次海外飞行" data-date="09-05 04:47" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-05 04:47</span>
          <span class="news-item-title">尽管存在安全问题，特朗普仍计划使用卡塔尔喷气机进行另一次海外飞行</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/04/us/politics/putin-zelensky-kushner-witkoff-talks.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="贾里德·库什纳（ Jared Kushner ）和史蒂夫·维特科夫（ Steve Witkoff ）会见两国总统的行程正值乌克兰冲突的不稳定时刻。" data-title="库什纳和威特科夫将前往俄罗斯和乌克兰重启和谈" data-date="09-04 23:21" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-04 23:21</span>
          <span class="news-item-title">库什纳和威特科夫将前往俄罗斯和乌克兰重启和谈</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-04/10690712.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网海口9月4日电 (尹建军 陈甲勇)记者4日从海南省自然资源和规划厅获悉，《海南省城镇开发边界管理实施细则(试行)》近日在全国率先出台，通过细化管控标准、优化调整规则、创新激励机制，进一步健全城镇开发边界精细化管理体系，有效破解规划落地难题、提升国土空间治理水平。" data-title="海南精细化规范城镇开发边界管理 提升国土空间治理水平" data-date="09-04 22:25" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-04 22:25</span>
          <span class="news-item-title">海南精细化规范城镇开发边界管理 提升国土空间治理水平</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-04/10690695.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网天津9月4日电 (记者 江莹)天津市卫生健康委4日召开新闻发布会，发布《天津市居民健康状况报告(2025年度)》(以下简称《报告》)，全面披露当地居民整体健康水平、重点疾病发病与死亡原因分析、健康风险防控等最新核心数据，系统呈现天津居民健康现状。" data-title="天津发布2025年度居民健康报告 居民期望寿命达82.80岁" data-date="09-04 22:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-04 22:20</span>
          <span class="news-item-title">天津发布2025年度居民健康报告 居民期望寿命达82.80岁</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/0/998/739.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 5 日消息，在接受《华盛顿邮报》采访时，顽皮狗工作室负责人尼尔 · 德鲁克曼（Neil Druckmann）透露，团队正为《最后生还者》（The Last of Us）筹备多个项目。德鲁克曼并未透露更多细节，只是确认工作室正在开发“几个项目”，也没有明确说明这些项目是否均为游戏。IT之家援引博文介绍，顽皮狗工作室的开发重心目前放在《星际：异端先知》（Intergalactic: The Heretic Prophet）方面，如果该工作室在推进《最后生还者》相关游戏项目，其发行日期可能会晚于《星际：异端先知》。《最后生还者》系列目前最后一款正式发售的游戏是 《The Last of Us Part II Remastered》，于 2025 年 1 月登陆 PS5，随后也推出" data-title="《最后生还者》游戏新动向：顽皮狗确认多个项目筹备中" data-date="09-05 13:58" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-05 13:58</span>
          <span class="news-item-title">《最后生还者》游戏新动向：顽皮狗确认多个项目筹备中</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-05/10690883.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网广州9月5日电 (记者 王坚)“AI生活家·寻找1001种AI生活新方式”城市共创项目9月4日在XAIR Expo2026具身智能产业博览会(以下简称“博览会”)上启动。该项目将以“AI七进”形式推动人工智能技术赋能千行百业、服务万家灯火。" data-title="广州多举措打通AI技术落地民生的“最后100米”" data-date="09-05 13:46" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-05 13:46</span>
          <span class="news-item-title">广州多举措打通AI技术落地民生的“最后100米”</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/998/738.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 5 日消息，科技媒体 NotebookCheck 昨日（9 月 4 日）发布博文，报道称瑞典零售商 Retrospelbutiken 已上架 Switch 2 版《塞尔达传说：时之笛》重制版页面，显示该游戏于 2026 年 11 月 12 日发行，标价 849 瑞典克朗（当前汇率约合 595 元人民币）。IT之家此前报道，任天堂将于 2026 年 9 月 8 日、9 日连续举办两场 Direct 直面会：9 月 8 日（IT之家注：北京时间 22:00）将举行《塞尔达传说》40 周年直面会，带来有关《塞尔达传说》的最新游戏资讯，节目时长约为 30 分钟。北京时间 9 月 9 日 22:00 还将举行另一场任天堂直面会，本场直面会将以今年冬季发售的游戏为核心，带来任天堂 Sw" data-title="Switch 2 版《塞尔达传说：时之笛》重制版游戏预估 11 月 12 日发行，将推典藏版" data-date="09-05 13:45" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-05 13:45</span>
          <span class="news-item-title">Switch 2 版《塞尔达传说：时之笛》重制版游戏预估 11 月 12 日发行，将推典藏版</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/998/735.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 5 日消息，科技媒体 sammyfans 昨日（9 月 4 日）发布博文，报道称三星 Exynos 2,700 工程样片 GeekBench 跑分曝光，6.7.1 版本单核成绩为 4,328 分，多核成绩为 14,700 分。IT之家注：上述跑分来自内部 Geekbench 6 跑分列表，在公开数据库中仅有 1 条 4 月上传的记录，6.6.0 版本单核成绩为 2,603 分，多核成绩为 10,350，由于版本差异，两条记录无法直接对比。今年 4 月曝光的跑分数据，显示 CPU 时钟频率存在差异根据最新跑分页面信息，基本符合此前曝光的 Exynos 2,700 Die Shot 图片信息，CPU 部分采用 1+4+1+4 集群设计，共有 10 个核心，分为 2 组：第 1" data-title="三星 Galaxy S27 手机首发：Exynos 2700 芯片跑分曝光，10 核 CPU 设计" data-date="09-05 13:27" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-05 13:27</span>
          <span class="news-item-title">三星 Galaxy S27 手机首发：Exynos 2700 芯片跑分曝光，10 核 CPU 设计</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/998/734.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 5 日消息，特斯拉中国现已在其 Tesla App 商城及微信小程序上架新款浅色汽车头枕 / 腰靠，其中头枕定价为 219 元，腰靠定价为 269 元。Tesla 头枕设计灵感源自特斯拉车辆内饰座椅，造型简约，与内饰完美融合，表面印有 Tesla 字标。采用与内饰材质一致的人造超纤皮材料，质感细腻，耐磨防滑，阻燃性能优良。头枕内部填充采用杜邦生物棉，舒适环保更安全。腰靠结合座椅弧度设计，贴合人体腰椎曲线，为您提供舒适支撑，缓解驾驶疲劳。Tesla 腰靠设计灵感源自特斯拉车辆内饰座椅，造型简约，与内饰完美融合，表面印有 Tesla 字标。采用与内饰材质一致的人造超纤皮材料，质感细腻，耐磨防滑，阻燃性能优良。头枕内部填充采用杜邦生物棉，舒适环保更安全。腰靠结合座椅弧度设计，贴合" data-title="特斯拉中国上线浅色 Tesla 头枕 / 腰靠，219 元起" data-date="09-05 13:11" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-05 13:11</span>
          <span class="news-item-title">特斯拉中国上线浅色 Tesla 头枕 / 腰靠，219 元起</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/998/733.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 5 日消息，中吉乌铁路吉尔吉斯斯坦境内段建设取得重要进展，该段科什特伯北 2 号隧道已顺利贯通，这也是该项目在吉境内段贯通的首座隧道。此次贯通的科什特伯北 2 号隧道全长 209.6 米，为单洞单线隧道，最大埋深 41 米。该隧道于 2026 年 5 月 10 日开工建设，建设团队仅用时 87 天即完成贯通。与此同时，纳伦 1 号隧道等控制性工程也取得阶段性成果。中吉乌铁路吉境内段全线土建工程自 2025 年 6 月开工以来，已开工隧道 27 座，其中贯通 1 座；已开工桥梁 43 座、路基 88 段；20 座车站基础建设也已全面展开。此外，全线大型临时道路、临时电力保障项目已全部竣工投用。中吉乌铁路是三国元首亲自推动的共建“一带一路”标志性工程。项目起自中国新疆喀什，经吐" data-title="中吉乌铁路吉境内段首座隧道贯通，全线最高大桥同步推进施工" data-date="09-05 12:55" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-05 12:55</span>
          <span class="news-item-title">中吉乌铁路吉境内段首座隧道贯通，全线最高大桥同步推进施工</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/998/731.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 5 日消息，据特斯拉 Tesla 官方公众号，特斯拉宣布上线“全损车用户特享关怀福利”，不限原车品牌，不限车型，9 月 30 日（含）前下订 Model S/3/X/Y 可享 800 元现金减免，直接抵扣订单尾款。特斯拉表示，全损出险时间介于 2026 年 9 月 1 日至活动结束，全损旧车与新购特斯拉的车主须为同一人（车主以行驶证中车辆所有人为准）。全损旧车赔付方为特斯拉合作保险公司（中国人民财产保险、中国平安财产保险、中国太平洋财产保险、中国人寿财产保险、太平财产保险、阳光财产保险），参与活动需提供保险公司出具的全损协议。" data-title="特斯拉上线“全损车用户特享关怀福利”，购车限时享 800 元尾款减免" data-date="09-05 12:54" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-05 12:54</span>
          <span class="news-item-title">特斯拉上线“全损车用户特享关怀福利”，购车限时享 800 元尾款减免</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/484649.html" target="_blank" rel="noopener" data-cat="keji" data-summary="AI直接吐出正确答案，但最关键的可能不是答案" data-title="陶哲轩吐槽GPT" data-date="09-05 12:24" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-05 12:24</span>
          <span class="news-item-title">陶哲轩吐槽GPT</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/484611.html" target="_blank" rel="noopener" data-cat="keji" data-summary="如此“反骨”的方法，具体又是怎么实现的？" data-title="这个世界模型训练完就“退场”，机器人反而更能干了" data-date="09-05 12:18" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-05 12:18</span>
          <span class="news-item-title">这个世界模型训练完就“退场”，机器人反而更能干了</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/484551.html" target="_blank" rel="noopener" data-cat="keji" data-summary="最后靠Harness救回来" data-title="姚班校友主导，Claude攻克费马大定理首个完整形式化证明" data-date="09-05 09:17" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-05 09:17</span>
          <span class="news-item-title">姚班校友主导，Claude攻克费马大定理首个完整形式化证明</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/04/xdof-just-three-months-out-of-stealth-is-in-talks-for-a-series-b-at-a-1-2b-valuation/" target="_blank" rel="noopener" data-cat="keji" data-summary="本轮融资是在这家机器人数据初创公司退出秘密几个月后进行的。" data-title="XDOF刚刚退出三个月，正在就B轮融资进行谈判，估值为12亿美元$" data-date="09-05 07:36" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-05 07:36</span>
          <span class="news-item-title">XDOF刚刚退出三个月，正在就B轮融资进行谈判，估值为12亿美元$</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/04/openais-rogue-agents-keep-escaping-with-no-formal-process-to-investigate-them/" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI 最新的代理群事件增加了独立调查的紧迫性，因为研究人员和立法者质疑人工智能实验室是否应该控制自己的安全审查范围。" data-title="OpenAI 的流氓特工不断逃跑，却没有正式的程序来调查他们" data-date="09-05 07:15" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-05 07:15</span>
          <span class="news-item-title">OpenAI 的流氓特工不断逃跑，却没有正式的程序来调查他们</span>
        </a>
        <a class="news-item" href="https://arstechnica.com/security/2026/09/openai-agents-discussed-ways-to-escape-their-sandbox-on-public-wiki/" target="_blank" rel="noopener" data-cat="keji" data-summary="总共有 3,700 名内部特工发布了 18,000 条讨论考试作弊的消息。" data-title="OpenAI 代理在公共 wiki 上讨论了逃离沙箱的方法" data-date="09-05 06:17" data-source="Ars Technica">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-arstechnica">🔬 Ars Technica</span>
          <span class="news-item-date">09-05 06:17</span>
          <span class="news-item-title">OpenAI 代理在公共 wiki 上讨论了逃离沙箱的方法</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/990658/audacity-4-update-audio-editing" target="_blank" rel="noopener" data-cat="keji" data-summary="《Audacity 4》已经开发了一段时间，去年，当一个不幸的重新设计的徽标开始流传时，它也引发了一些小争议。新图标的最终版本并不像去年十月流传的早期版本那么糟糕。但更重要的是，所有承诺的改进 [...]" data-title="Audacity 4 是“世界上最受欢迎”的音频编辑器的彻底改造" data-date="09-05 05:23" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-05 05:23</span>
          <span class="news-item-title">Audacity 4 是“世界上最受欢迎”的音频编辑器的彻底改造</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/09/04/ai-compute-provider-nscale-is-looking-for-3-5b-in-pre-ipo-financing/" target="_blank" rel="noopener" data-cat="keji" data-summary="Nscale 最近与 Anthropic 达成了 450 亿美元的交易，目前正在洽谈筹集更多资金，以应对即将到来的 IPO。" data-title="AI 计算提供商 Nscale 正在寻找 $3.5B" data-date="09-05 05:12" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">09-05 05:12</span>
          <span class="news-item-title">AI 计算提供商 Nscale 正在寻找 $3.5B</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c209xvxe558o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="首席足球作家菲尔·麦克纳尔蒂问道，在英超联赛战胜伊普斯维奇的比赛中梅开二度后，真正的亚历山大·伊萨克终于抵达利物浦了吗？" data-title="伊萨克终于到来，加克波证明了对利物浦的价值" data-date="09-05 06:37" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-05 06:37</span>
          <span class="news-item-title">伊萨克终于到来，加克波证明了对利物浦的价值</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/sep/04/ipswich-town-v-liverpool-premier-league-live-updates" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Alexander Isak’s early quick-fire double gave Andoni Iraola his first win as Liverpool managerThe teams are out! Ipswich in blue, Liverpool in red. A wonderful start-of-the-weekend, possibly-a-few-pints-to-the-good atmosphere under the lights at Portman Road! Not long now. In the meantime, here’s Dave Estherby with some pre-match words of encourage" data-title="伊普斯维奇镇 0-2 利物浦：英超联赛——事实如此" data-date="09-05 05:35" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-05 05:35</span>
          <span class="news-item-title">伊普斯维奇镇 0-2 利物浦：英超联赛——事实如此</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/04/premier-league-news-manchester-united-everton-aston-villa-manchester-city-tottenham" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="托特纳姆热刺队主教练罗伯托·德泽尔比坚称他的巴西前锋“决定了一切，而不是我”继续阅读..." data-title="英超新闻：理查利森拒绝新合同，阿隆索支持詹姆斯中场" data-date="09-05 05:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-05 05:30</span>
          <span class="news-item-title">英超新闻：理查利森拒绝新合同，阿隆索支持詹姆斯中场</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/04/ipswich-liverpool-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="A first win for Andoni Iraola’s Liverpool, the introduction of the latest star signing in Bradley Barcola making for a successful Friday night. Better yet, continuing signs that Alexander Isak, last year’s model, is coming back to life, his two, well-taken early goals securing the three points. That Cody Gakpo, Isak’s supplier, might have been at M" data-title="伊萨克快速梅开二度击溃伊普斯维奇，为安多尼·伊劳拉带来利物浦首场胜利" data-date="09-05 05:07" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-05 05:07</span>
          <span class="news-item-title">伊萨克快速梅开二度击溃伊普斯维奇，为安多尼·伊劳拉带来利物浦首场胜利</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c5y5g5vq00lo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="利物浦和伊普斯维奇的球员在英超比赛后的评价。" data-title="伊萨克最终大放异彩，但谢尔彭遭遇困境——伊普斯维奇对阵利物浦球员评分" data-date="09-05 04:54" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-05 04:54</span>
          <span class="news-item-title">伊萨克最终大放异彩，但谢尔彭遭遇困境——伊普斯维奇对阵利物浦球员评分</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/czjzn84wn9wo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="有没有证据表明前英超裁判迈克·迪恩曾在比赛中玩小游戏？ BBC 体育频道查看了证据。" data-title="迪恩说他总是遵守法律——但他参加了哪些比赛？" data-date="09-05 02:33" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-05 02:33</span>
          <span class="news-item-title">迪恩说他总是遵守法律——但他参加了哪些比赛？</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/04/premier-league-team-news-predicted-lineups-for-the-weekend-action" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="周日周六中午 12 点 30 分，在 TNT 体育 1 场地圣詹姆斯公园球场对切尔西的冠军资格进行测试之前，考文垂将面临一场艰巨的曼城之旅 继续阅读..." data-title="英超球队新闻：周末比赛的预测阵容" data-date="09-05 01:38" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-05 01:38</span>
          <span class="news-item-title">英超球队新闻：周末比赛的预测阵容</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/04/a-window-tax-to-curb-the-premier-leagues-big-spenders" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="转会窗口|周日滑雪|债券市场|突破名义决定论泡沫|严肃的结论巴尼·罗尼（ Barney Ronay ）在他的文章中就最近的英超转会窗口（英超联赛的钱在9月2日混乱的过剩景象中失去了一切意义）提出了很多很好的观点。我有一个建议要补充：意外之财税。对消费者征收，它可以为游戏的基层筹集资金，并可能作为" data-title="征收窗户税以遏制英超联赛的大手笔|简短的信件" data-date="09-05 00:53" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-05 00:53</span>
          <span class="news-item-title">征收窗户税以遏制英超联赛的大手笔|简短的信件</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c79038z3q4yo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="托特纳姆热刺队主教练罗伯托·德泽尔比表示，将理查利森排除在俱乐部英超阵容之外并不是他的决定。" data-title="理查利森的遗漏不是我的决定" data-date="09-04 23:32" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-04 23:32</span>
          <span class="news-item-title">理查利森的遗漏不是我的决定</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/04/premier-league-news-manchester-united-everton-aston-villa-manchester-city-tottenham" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="马雷斯卡欢呼“胜利者”费尔南德斯，但不会让他成为队长，德泽尔比为理查利森的待遇辩护继续阅读..." data-title="英超新闻：卡里克警告没有快速解决办法，埃默里对哈伍德“严厉”" data-date="09-04 22:58" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-04 22:58</span>
          <span class="news-item-title">英超新闻：卡里克警告没有快速解决办法，埃默里对哈伍德“严厉”</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/998/617.htm" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="IT之家 9 月 4 日消息，据共同社报道，日本电机巨头尼得科 Nidec 今日公布了关于产品质量问题的调查委员会报告。调查委员会认定存在 844 起擅自变更制造工序等不当行为，并指出达成业绩目标及削减成本等压力是原因之一。IT之家获悉，尼得科不当行为可追溯至 2012 年，其中超九成属于未经客户同意变更部件及工序等情况。此外还存在篡改、捏造测试及检查结果的问题。从事情的严重程度来看，60 起被认定为重大不当行为，包括尼得科集团高层及据点负责人参与，以及涉嫌违反法令的情况。除品质问题外，关于生产地存在 6 起不当行为。关于原因，报告指出企业规模通过并购等方式日益扩大，而与之相应的经营体制完善工作滞后，另一方面短期内达成业绩目标及降低成本的要求强烈。品质保证所需人才也未得到充分地确保。社长岸田" data-title="日本电机巨头尼得科确认存在 844 起擅自变更制造工序等不当行为，社长岸田光哉致歉" data-date="09-04 22:47" data-source="IT之家">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-04 22:47</span>
          <span class="news-item-title">日本电机巨头尼得科确认存在 844 起擅自变更制造工序等不当行为，社长岸田光哉致歉</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cvgypzg4y75o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="考文垂城确认签下图卢兹边锋雅恩·博霍（Yann Gboho），他是巴黎圣日耳曼和法国前锋德西雷·杜埃的表弟。" data-title="考文垂签下边锋格博霍——巴黎圣日耳曼球员杜埃的表弟" data-date="09-04 22:32" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-04 22:32</span>
          <span class="news-item-title">考文垂签下边锋格博霍——巴黎圣日耳曼球员杜埃的表弟</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c3v49617lzko?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="埃弗顿主帅大卫·莫耶斯承认，他想在转会截止日做更多的生意，但他承认自己“必须忍受失望”。" data-title="截止日期后，莫耶斯生活在失望之中" data-date="09-04 22:03" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-04 22:03</span>
          <span class="news-item-title">截止日期后，莫耶斯生活在失望之中</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c5y4ge76jx8o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼城主教练恩佐·马雷斯卡表示，一些曼城球员想知道恩佐·费尔南德斯是否会在转会窗口的最后几天加盟。" data-title="多名球员希望获得费尔南德斯的最新消息" data-date="09-04 21:35" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-04 21:35</span>
          <span class="news-item-title">多名球员希望获得费尔南德斯的最新消息</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cgk5g2z3kyxo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="布莱顿主帅法比安·胡尔泽勒表示，在海鸥队拒绝了利物浦对这位边锋的报价后，扬库巴·明特未来仍然可以“实现他的梦想”。" data-title="利物浦目标明特仍然可以获得梦想的转会" data-date="09-04 18:44" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-04 18:44</span>
          <span class="news-item-title">利物浦目标明特仍然可以获得梦想的转会</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-05/10690906.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="9月5日，江西省遂川县高坪镇明坑村石下组发生泥石流和山体滑坡，应急管理部立即调度部署抢险救援工作，要求全力搜救被困人员，核实核清伤亡失联人数，就近调派通信保障、工程抢险等队伍装备，尽快组织救援人员挺进灾区，加强水文、地质灾害监测预警，科学施救，严防次生灾害发生。" data-title="应急管理部调度江西遂川泥石流灾害救援 派出工作组赶赴现场" data-date="09-05 14:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-05 14:14</span>
          <span class="news-item-title">应急管理部调度江西遂川泥石流灾害救援 派出工作组赶赴现场</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-05/10690905.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="记者5日从中国海洋大学获悉，中国工程院院士、中国现代海洋药物学科的开拓者与奠基人、该校原校长管华诗，因病医治无效，于2026年9月4日11时18分在青岛逝世，享年87岁。" data-title="痛别！管华诗逝世" data-date="09-05 14:11" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-05 14:11</span>
          <span class="news-item-title">痛别！管华诗逝世</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-05/10690902.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="【2026打卡中国】赣州章贡：千年宋城，何以“活”在今天？" data-title="赣州章贡：千年宋城，何以“活”在今天？" data-date="09-05 14:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-05 14:02</span>
          <span class="news-item-title">赣州章贡：千年宋城，何以“活”在今天？</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-05/10690878.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社福建连城9月5日电 题：松毛岭祭无名英烈 一碗热粥四代传承" data-title="（长征胜利90周年）松毛岭祭无名英烈 一碗热粥四代传承" data-date="09-05 13:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-05 13:45</span>
          <span class="news-item-title">（长征胜利90周年）松毛岭祭无名英烈 一碗热粥四代传承</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-05/10690876.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社江西庐山9月5日电 题：鄱阳湖退捕渔村多元业态引客来" data-title="（走进中国乡村）鄱阳湖退捕渔村多元业态引客来" data-date="09-05 13:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-05 13:43</span>
          <span class="news-item-title">（走进中国乡村）鄱阳湖退捕渔村多元业态引客来</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-05/10690897.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="全国入秋进程图出炉！北方多地入秋偏晚 冷空气将推动秋天版图扩张" data-title="全国入秋进程图出炉！北方多地入秋偏晚" data-date="09-05 13:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-05 13:41</span>
          <span class="news-item-title">全国入秋进程图出炉！北方多地入秋偏晚</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-05/10690874.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社北京9月5日电 (记者 李京泽)记者5日从中国民政部获悉，据不完全统计，目前，西藏吉隆泥石流灾害慈善捐赠已超过6.6亿元人民币；其中，超147万人次通过互联网公开募捐服务平台，向有关公开募捐慈善项目捐赠5016万元。" data-title="中国民政部：西藏吉隆泥石流灾害慈善捐赠超6.6亿元人民币" data-date="09-05 13:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-05 13:41</span>
          <span class="news-item-title">中国民政部：西藏吉隆泥石流灾害慈善捐赠超6.6亿元人民币</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/998/737.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 5 日消息，雷神现已在京东上架“Z527F165L”27 英寸显示器，该机支持 5K 165Hz/2K 330Hz 双模，定价为 3599 元，国补后低至 2999 元。京东雷神“Z527F165L”显示器 3599 元直达链接该机配备的 27 英寸 Fast IPS 面板支持以 5120x2880 分辨率 165Hz / 或 2560x1440 分辨率 330Hz 显示（并非带鱼屏显示器的“5K”实为“1440P”套路），最快响应时间 1ms GTG，可视角度 178°/178°，最高亮度 400 尼特，原生静态对比度 1500:1，显示器支持 10-Bit 色彩，覆盖 95% DCI-P3 与 99% sRGB 色域。该机支架支持升降 / 倾斜 / 旋转，显示器本体支持" data-title="雷神推出“Z527F165L”27 英寸显示器：5K 165Hz / 2K 330Hz 双模，3599 元（国补后 2999 元）" data-date="09-05 13:30" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-05 13:30</span>
          <span class="news-item-title">雷神推出“Z527F165L”27 英寸显示器：5K 165Hz / 2K 330Hz 双模，3599 元（国补后 2999 元）</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-05/10690890.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="按照《国家自然灾害救助应急预案》，针对近期台风及极端强降雨对福建莆田、宁德等地造成的严重影响，9月5日，国家防减救灾委、应急管理部将针对福建的国家自然灾害救助应急响应级别提升至三级，增派救灾工作组紧急赶赴灾区实地查看灾情，指导和协助地方做好受灾群众基本生活保障及灾后应急恢复等灾害救助工作。" data-title="两部门针对福建提升国家自然灾害救助应急响应级别至三级" data-date="09-05 13:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-05 13:22</span>
          <span class="news-item-title">两部门针对福建提升国家自然灾害救助应急响应级别至三级</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-05/10690886.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="何谓科学家？一颗报国心，一身真本事。他们勇攀高峰，接续奋斗，干惊天动地事，做隐姓埋名人。为何选择这份事业？从“两弹一星”元勋到量子科技的领军人，一代代科大人接力续写着科教报国的青春华章。报国无声，迎接着永恒的东风！" data-title="青春华章｜报国无声，迎接着永恒的东风！" data-date="09-05 13:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-05 13:02</span>
          <span class="news-item-title">青春华章｜报国无声，迎接着永恒的东风！</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-05/10690882.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="近日，在西藏吉隆口岸受灾核心区，现场工作人员在国旗下轻轻放上几束鲜花，悼念此次泥石流灾害的遇难者。连日来，西藏统筹各方救援力量，同步开展人员搜救、道路抢通、善后处置和风险防范各项工作，目前抢险救援和应急处置工作正在受灾核心区开展。" data-title="西藏吉隆口岸：国旗屹立 信念长存" data-date="09-05 12:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-05 12:53</span>
          <span class="news-item-title">西藏吉隆口岸：国旗屹立 信念长存</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-05/10690881.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="【环球网记者 石丁 朱马烈 许庆瑶报道】百年前，先辈们以青春之我，创建青春之国家、青春之民族。这份跨越时空的青春接力，至今仍在神州大地上激荡回响。回望来路，钱学森、邓稼先、于敏等老一辈科学家，在筚路蓝缕中挺起民族脊梁。“外国人能搞的，难道中国人不能搞？”“国家需要我，我一定全力以赴！”这不仅是历史的铿锵回音，更是中国科技青年代代相传的报国初心与铮铮铁骨。" data-title="青春华章｜这就是中国的模样！从觉醒年代到星辰大海，看中国青年的“硬核”接力" data-date="09-05 12:51" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-05 12:51</span>
          <span class="news-item-title">青春华章｜这就是中国的模样！从觉醒年代到星辰大海，看中国青年的“硬核”接力</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/998/730.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 5 日消息，《东方 Project》制作者“上海爱丽丝幻乐团（ZUN）”现已发布弹幕射击游戏《东方红魔乡：新典 ～ the Embodiment of Scarlet Devil.》发售预告片，本作将于北京时间 9 月 9 日发售，登陆 PS5、Switch 2、PC 平台，支持中文。IT之家获悉，《东方红魔乡：新典》是 2002 年推出的《东方红魔乡 ～ 绯红恶魔的体现》（the Embodiment of Scarlet Devil.）时隔 24 年首次推出的重制版本，玩家将操控博丽灵梦与雾雨魔理沙，在漫天飞舞的弹幕之间穿梭，调查笼罩幻想乡的神秘红雾异变。▲ 注：北京时间 9 月 9 日发售重制版除了将游戏画面升级至高清规格外，官方还对全部游戏 BGM 进行重新编曲，Z" data-title="经典弹幕游戏重制《东方红魔乡：新典》北京时间 9 月 9 日发售：BGM 重新编曲、画面升至高清规格" data-date="09-05 12:48" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-05 12:48</span>
          <span class="news-item-title">经典弹幕游戏重制《东方红魔乡：新典》北京时间 9 月 9 日发售：BGM 重新编曲、画面升至高清规格</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-05/10690837.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="尼泊尔共产党(毛主义中心)前总书记德沃·古隆9月3日在《中国日报》撰文称，尼泊尔此次遭遇泥石流灾害的根源在于气候变化导致的冰川失稳。国际社会应加强跨境监测预警，并由发达国家承担气候责任、加大对发展中国家的资金和技术支持。" data-title="尼共前总书记：西方媒体谣言让冰川灾害“雪上加霜”" data-date="09-05 11:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-05 11:10</span>
          <span class="news-item-title">尼共前总书记：西方媒体谣言让冰川灾害“雪上加霜”</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/04/us/lindsay-clancy-trial-unanimous-verdicts.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="洪氏陪审团并不常见，但林赛·克兰西谋杀案的审判令人痛苦且极其复杂。" data-title="在像林赛·克兰西这样的复杂案件中，很难达成一致裁决" data-date="09-05 07:47" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-05 07:47</span>
          <span class="news-item-title">在像林赛·克兰西这样的复杂案件中，很难达成一致裁决</span>
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

<p class="news-updated">🕐 抓取更新于 2026-09-05 14:24（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
