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
      <span>2026-09-06 19:43 抓取更新</span>
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
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/09-06/10691544.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社广州9月6日电#8195;中央宣传部、中央军委国防动员部联合主办的2026年“全民国防教育月”活动启动仪式9月6日在广东岭南国防教育基地举行。" data-title="2026年“全民国防教育月”活动启动" data-date="09-06 19:35" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 09-06 19:35</span>
      </div>
      <h2 class="hero-featured-title">2026年“全民国防教育月”活动启动</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/gn/2026/09-06/10691550.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="央广网合肥9月6日消息(记者徐秋韵)国家重大科技基础设施也被称为大科学装置，是为进行大规模科学研究而建造的大型设施，通常被认为是国家创新高地的重要要素。目前，安徽已建、在建和预研大科学装置数量位居全国前列。" data-title="向新之翼|追“光”逐“日”，探秘合肥未来大科学城" data-date="09-06 19:39" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">向新之翼|追“光”逐“日”，探秘合肥未来大科学城</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/live/2026/sep/06/everton-v-manchester-united-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Minute-by-minute updates from the action at Hill Dickinson StadiumTransfer failures leave Everton scrambling | Mail TimAfternoon everyone and welcome to the David Moyes derby. Or is it the Wayne Rooney, Michael Keane, James Garner, Morgan Schneiderlin and not quite Joshua Zirkzee derby?The Premier League prediction posse, both human and automated," data-title="埃弗顿v曼联：英超联赛" data-date="09-06 19:36" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">埃弗顿v曼联：英超联赛</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/0/999/020.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 6 日消息，2026 世界超级摩托车锦标赛（WSBK）法国站 WorldSSP 组别次回合正赛今日在法国讷韦尔-马尼库尔赛道举行，比赛进行到还剩 8 圈时一度红旗中断，重新发车后排在第二的张雪机车 53 号车手瓦伦丁 · 德比斯最终完成 5 圈比赛拿下第三名，继第一回合季军登台后本赛季第 8 次登上领奖台。另一位张雪机车车手卡里卡苏洛，以第 8 名的成绩同样带回积分。至此，“张雪机车”完成法国站全部比赛。下一站比赛将于 9 月 25 日至 27 日在意大利克雷莫纳赛道举行。" data-title="2026 WSBK 法国站第二回合，张雪机车德比斯再获季军" data-date="09-06 19:33" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">2026 WSBK 法国站第二回合，张雪机车德比斯再获季军</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-06/10691544.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社广州9月6日电#8195;中央宣传部、中央军委国防动员部联合主办的2026年“全民国防教育月”活动启动仪式9月6日在广东岭南国防教育基地举行。" data-title="2026年“全民国防教育月”活动启动" data-date="09-06 19:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 19:35</span>
          <span class="news-item-title">2026年“全民国防教育月”活动启动</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-06/10691540.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网雅加达9月6日电 中国驻棉兰总领馆6日发文，提醒领区中国公民注意防范喀拉喀托之子火山灾害。" data-title="中领馆提醒领区中国公民注意防范印尼喀拉喀托之子火山灾害" data-date="09-06 19:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 19:34</span>
          <span class="news-item-title">中领馆提醒领区中国公民注意防范印尼喀拉喀托之子火山灾害</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-06/10691534.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月6日电 据黎巴嫩国家通讯社报道，黎卫生部当地时间6日发表声明说，以色列当天对黎巴嫩南部奈拜提耶地区多个城镇发动空袭，造成4人死亡、20人受伤。" data-title="以色列袭击黎巴嫩南部致4死20伤" data-date="09-06 19:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 19:17</span>
          <span class="news-item-title">以色列袭击黎巴嫩南部致4死20伤</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-06/10691522.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社雅加达9月6日电 (记者 李志全)印度尼西亚交通部长杜迪·普尔瓦甘迪6日表示，受喀拉喀托之子火山持续喷发及火山灰扩散影响，包括首都雅加达苏加诺—哈达国际机场在内的6座机场临时关闭。" data-title="印尼六座机场因火山喷发临时关闭 数百航班受影响" data-date="09-06 19:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 19:16</span>
          <span class="news-item-title">印尼六座机场因火山喷发临时关闭 数百航班受影响</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-06/10691516.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网约翰内斯堡9月6日电 中国驻南非使馆6日发布公告称，近期，南非约翰内斯堡的塞尔比、杰米斯顿地区连续发生涉我侨胞被绑架案件。绑匪以经营店铺、酒铺的侨胞为主要目标，以索要赎金为作案目的，选择受害人送货途中或门店附近作案。我侨胞人身财产安全受到严重威胁。驻南非使馆提醒广大侨胞，务必密切关注当地安全和治安形势，进一步提高安全防护意识，主动防范被绑架风险。" data-title="南非约堡多地发生侨胞被绑架案 使馆提醒旅南侨胞主动防范" data-date="09-06 19:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 19:16</span>
          <span class="news-item-title">南非约堡多地发生侨胞被绑架案 使馆提醒旅南侨胞主动防范</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-06/10691536.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月6日电 据阿联酋外交部官网消息，当地时间9月6日，阿联酋、沙特阿拉伯、卡塔尔、约旦、印度尼西亚、巴基斯坦、土耳其和埃及八国外长发表联合声明，强烈谴责以色列国家安全部长本-格维尔和以色列国防部长卡茨有关将巴勒斯坦民众迁出加沙地带的言论，以及其提出的旨在强行将巴勒斯坦人赶离其土地的相关计划和机制。" data-title="八国外长发表联合声明 谴责以色列方面涉加沙言论" data-date="09-06 19:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 19:14</span>
          <span class="news-item-title">八国外长发表联合声明 谴责以色列方面涉加沙言论</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/06/world/europe/ukraine-zelensky-witkoff-kushner-russia-putin.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="史蒂夫·维特科夫（ Steve Witkoff ）和贾里德·库什纳（ Jared Kushner ）周六在莫斯科会见了俄罗斯总统弗拉基米尔· V ·普京（ Vladimir" data-title="特朗普特使首次访问基辅" data-date="09-06 19:06" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-06 19:06</span>
          <span class="news-item-title">特朗普特使首次访问基辅</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-06/10691533.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月6日电 据重庆市纪委监委消息：重庆贸促会原党组成员、副会长章晓风涉嫌严重违纪违法，目前正接受重庆市纪委监委纪律审查和监察调查。" data-title="重庆贸促会原党组成员、副会长章晓风接受审查调查" data-date="09-06 19:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 19:05</span>
          <span class="news-item-title">重庆贸促会原党组成员、副会长章晓风接受审查调查</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-06/10691532.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月6日电 据江西省纪委监委消息：江西省公安厅原党委委员万秀奇涉嫌严重违纪违法，主动向组织交代问题，目前正接受江西省纪委监委纪律审查和监察调查。" data-title="江西省公安厅原党委委员万秀奇接受审查调查" data-date="09-06 19:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 19:05</span>
          <span class="news-item-title">江西省公安厅原党委委员万秀奇接受审查调查</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/06/us/politics/trump-miderm-elections-republicans.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="总统的战略、信息和支出使共和党陷入困境，因为立法者试图超越他下滑的支持率。" data-title="随着中期选举的临近，共和党人发现特朗普无法逃脱" data-date="09-06 17:04" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-06 17:04</span>
          <span class="news-item-title">随着中期选举的临近，共和党人发现特朗普无法逃脱</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/06/us/elections/trump-mail-in-voting-confusion.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="从俄勒冈州到佛罗里达州，官员们立即向选民保证他们的选票是安全的，并鼓励他们使用投递箱或亲自投票。" data-title="特朗普对邮寄选票的战争让选民感到困惑。这可能就是重点。" data-date="09-06 17:01" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-06 17:01</span>
          <span class="news-item-title">特朗普对邮寄选票的战争让选民感到困惑。这可能就是重点。</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-06/10691397.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社莫斯科9月6日电 俄罗斯总统助理乌沙科夫6日凌晨召开新闻发布会，通报俄总统普京5日晚在克里姆林宫与美国总统特朗普的特使威特科夫和女婿库什纳的会谈情况。" data-title="俄总统助理：普京重申愿通过政治外交手段解决俄乌冲突" data-date="09-06 15:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 15:49</span>
          <span class="news-item-title">俄总统助理：普京重申愿通过政治外交手段解决俄乌冲突</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-06/10691396.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社西安9月6日电 题：陕西文学“牵手”乌尔都语 “巴铁”青年跨界传递文化共鸣" data-title="陕西文学“牵手”乌尔都语　“巴铁”青年跨界传递文化共鸣" data-date="09-06 15:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 15:48</span>
          <span class="news-item-title">陕西文学“牵手”乌尔都语　“巴铁”青年跨界传递文化共鸣</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cm2q6pyyzn0o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="随着阿根廷总统米莱承诺为福克兰群岛带来“变革之风”，特朗普会改变他对英国统治的立场吗？" data-title="特朗普取态何以左右福克兰群岛争议" data-date="09-06 15:42" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-06 15:42</span>
          <span class="news-item-title">特朗普取态何以左右福克兰群岛争议</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-06/10691367.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="近期，多地公安、国安部门发布安全提示，手机蓝牙长期保持开启状态暗藏风险。听听公安部门怎么说。" data-title="手机蓝牙别常开 这些窃密手段一定要警惕" data-date="09-06 14:34" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 14:34</span>
          <span class="news-item-title">手机蓝牙别常开 这些窃密手段一定要警惕</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-06/10691550.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="央广网合肥9月6日消息(记者徐秋韵)国家重大科技基础设施也被称为大科学装置，是为进行大规模科学研究而建造的大型设施，通常被认为是国家创新高地的重要要素。目前，安徽已建、在建和预研大科学装置数量位居全国前列。" data-title="向新之翼|追“光”逐“日”，探秘合肥未来大科学城" data-date="09-06 19:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 19:39</span>
          <span class="news-item-title">向新之翼|追“光”逐“日”，探秘合肥未来大科学城</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/018.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 6 日消息，尽管个人电脑市场出现季节性放缓，且内存短缺导致组件成本上升，但第二季度独立显卡出货量仍实现增长。考虑到第二季度通常比第一季度表现更弱，这一增长尤其值得关注。与此同时，内存短缺已经推高了 PC 厂商和消费者的成本，尤其是搭载高端显卡的 PC 产品受到的影响更为明显。根据 Jon Peddie Research（JPR）的数据，第二季度独立 GPU 出货量较第一季度增长 12.2%，同比增长 14.1%。同期，整个客户端 CPU 市场同比下降 1.1%，台式机 PC 需求也有所走弱。JPR 表示，2026 年第二季度，包含集成显卡和独立显卡在内的消费级 PC GPU 总出货量达到 7550 万颗，环比增长 10.4%，同比增长 1.1%。IT之家注意到，笔记本电脑是" data-title="JPR：2026 二季度 PC 市场需求疲软，独立 GPU 出货量逆势增长 12.2%" data-date="09-06 19:28" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-06 19:28</span>
          <span class="news-item-title">JPR：2026 二季度 PC 市场需求疲软，独立 GPU 出货量逆势增长 12.2%</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/017.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 6 日消息，今日，比亚迪、理想汽车、深蓝汽车、长安汽车、凯迪拉克、北汽集团等车企纷纷在微博发文，预祝小米澎程上市成功。对此，小米创办人，董事长兼 CEO 雷军发文致谢：“感谢所有的朋友们，谢谢大家！”从雷军公布的截图看，共 54 个微博账号为小米澎程送出祝福。除了大家熟悉的汽车品牌外，欣旺达、中创新航、东安动力、禾赛科技、宇树科技、快手、百度、飞书等品牌也进行了发文。小米秋季旗舰新品发布会已定档 9 月 7 日晚 7 点，届时将发布澎程 N70 Pro / N70 Max / N90 Max、小米 18 Fold 全新折叠屏旗舰手机、小米平板 9 Pro Max 等。小米澎程 N90 Max 预售价为 29.99 万元，该车提供远山青、蝴蝶谷蓝、火山灰等配色，尺寸为 528" data-title="比亚迪、理想、北汽集团等多家车企预祝小米澎程上市成功，雷军发文致谢" data-date="09-06 19:28" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-06 19:28</span>
          <span class="news-item-title">比亚迪、理想、北汽集团等多家车企预祝小米澎程上市成功，雷军发文致谢</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-06/10691512.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网福建顺昌9月6日电 (张丽君 朱城铖)台湾台中科技大学应用中文系教授林翠凤6日在福建南平市顺昌县受访时说，“一定要不忘本，一定要溯源，一定要让它核心的传统绵延长久，扎根在顺昌本土的大圣文化，才有面向世界长长久久的底气。”" data-title="第四届闽台大圣文化交流研讨会在福建南平顺昌县举行" data-date="09-06 19:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 19:28</span>
          <span class="news-item-title">第四届闽台大圣文化交流研讨会在福建南平顺昌县举行</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/016.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="小米新一代米家破壁机 3 现已开启预售，主打可拆洗刀座设计与多重降噪结构，京东售价 389 元，叠加国补后到手价 330.65 元起。晒单返 20 元京豆，折合仅需 310.65 元：京东米家破壁机 3 1.5L 国补后 330.65 元直达链接确认收货后，完成晒图 1 张 +10 字以上评价，即可获得价值 20 元京豆一份，奖品共 300 份。这款破壁机采用重力自锁式刀座结构，无需辅助工具即可便捷拆卸，水流可直接冲洗刀座，不易藏污纳垢，具备 IPX9 防水等级。产品升级多重降噪结构，采用 13 重降噪设计，运行声音低至 45 dB(A)，制浆噪音 51 dB(A)，相比前代产品整机噪音降低 8%。该机支持微米级强劲破壁，内置 35000 转 / 分钟电机，配备双层 8 叶精钢刀，搭配 4" data-title="首发 389 → 311 元：小米 1.5L 米家破壁机 3 预售，可拆刀座 + 陶瓷油不粘涂层" data-date="09-06 19:23" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-06 19:23</span>
          <span class="news-item-title">首发 389 → 311 元：小米 1.5L 米家破壁机 3 预售，可拆刀座 + 陶瓷油不粘涂层</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/015.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 6 日消息，在普遍认为企业还不知道该如何真正利用 AI 的当下，微软却已经制定了一套计划：借助 AI，让更多原生 WinUI 应用进入 Microsoft Store。IT之家注意到，微软近日发布了一份新的快速入门指南，帮助开发者利用 AI、VS Code 和自家的 winapp CLI，从一个空文件夹开始，一步步创建并发布 WinUI 3 应用。微软表示，整个流程大约只需要 30 分钟，而且无需安装 Visual Studio，使用的工具也都是免费的，包括 GitHub Copilot 的免费版本。这份简单的 30 分钟指南，本质上是在吸引初学者为 Windows 11 开发应用，而且不必再经历传统开发中那些“繁重”的编码工作。现在，任何人都可以借助 AI 创建一个新的" data-title="微软借力 AI 重塑 Win11 应用生态：30 分钟即可生成 WinUI 原生应用" data-date="09-06 19:17" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-06 19:17</span>
          <span class="news-item-title">微软借力 AI 重塑 Win11 应用生态：30 分钟即可生成 WinUI 原生应用</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/014.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 6 日消息，据 Windows Latest 报道，微软希望 Windows 重新赢得用户喜爱，并正在采取一系列措施改善这款操作系统。该系统将迎来可移动的任务栏，甚至还有不再依赖 Bing 的 Windows 搜索。不过，这是否意味着微软会从 Windows 11 中彻底淡化 AI，把精力重新放在稳定性和质量上？当然不是。未来只是不会再把重点放在 Copilot 按钮上。微软 CEO 萨蒂亚 · 纳德拉的第三季度讲话非常罕见地多次提到了 Windows。他首先透露，Windows 每月活跃设备数量已经达到 16 亿台；随后又确认微软正在采取更广泛的战略，把重点重新放回基础体验，同时还用一个新的概念“unmetered intelligence”（无计量智能）来暗示操作系统的" data-title="微软重塑 Win11 AI 战略：“无计量智能”将让更多 AI 在 PC 本地运行" data-date="09-06 18:51" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-06 18:51</span>
          <span class="news-item-title">微软重塑 Win11 AI 战略：“无计量智能”将让更多 AI 在 PC 本地运行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-06/10691502.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网南京9月6日电 (记者 徐珊珊)宁马线“科学家号”科普专列于9月6日正式命名开通。宁马线是国内首条跨省共建、共管、共运营的市域(郊)铁路，该专列由江苏省科协、安徽省科协指导，南京市科协与马鞍山市科协共同主办。" data-title="宁马线开出“科学家号” 跨省地铁变身“移动科普馆”" data-date="09-06 18:43" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 18:43</span>
          <span class="news-item-title">宁马线开出“科学家号” 跨省地铁变身“移动科普馆”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-06/10691501.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网南京9月6日电 (记者 徐珊珊)2026年“全国科普月”南京市暨雨花台区主场活动于9月6日在南京科技馆举行。今年活动主题为“科技改变生活 创新赢得未来”，活动期间全市将开展各类科普活动千余场。" data-title="全国科普月南京主场启幕 千余场活动点亮“科学盛宴”" data-date="09-06 18:41" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 18:41</span>
          <span class="news-item-title">全国科普月南京主场启幕 千余场活动点亮“科学盛宴”</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/012.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 6 日消息，大众安徽今日宣布，与众 08 猎影版已陆续登陆全国门店。与众 08 猎影版将于 9 月 12 日正式上市交付，该车已在 2026 成都车展开启预售，预售价 23 万元。IT之家获悉，与众 08 猎影版车身尺寸为长 5000mm、宽 1954mm、高 1688mm，轴距 3030mm，定位中大型五座纯电 SUV。新车基于与众 08 Ultra 版打造，全系标配价值超过 4 万元的猎影内外套装、威巴克双腔空气悬架与采埃孚 DCC 底盘、车载冰箱及后排折叠桌板等四大装备包。与众 08 猎影版搭载最新一代 VLA 2.0 端到端大模型，标配双图灵芯片，总算力达 1500 TOPS，配合 26 颗高精度感知硬件。动力与底盘方面，与众 08 猎影版基于 800V 高压平台打" data-title="大众与众 08 猎影版车型已陆续登陆全国门店：预售价 23 万元，9 月 12 日上市" data-date="09-06 18:34" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-06 18:34</span>
          <span class="news-item-title">大众与众 08 猎影版车型已陆续登陆全国门店：预售价 23 万元，9 月 12 日上市</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/video-games/former-old-school-runescape-dev-gets-jail-time-for-stealing-usd400-000-from-players-virtual-gold-stolen-and-sold-on-the-black-market-before-jagex-caught-the-culprit-using-hidden-firewall-tweaks" target="_blank" rel="noopener" data-cat="keji" data-summary="一名前 Jagex 员工从 OSRS 玩家那里窃取了价值超过 40 万美元的游戏内物品和虚拟货币，并将其在黑市上出售。他最终被捕并被判处三年监禁，一名调查员表示，“仅仅因为它是虚拟的，并不意味着他不应该面对法律的全部效力。”" data-title="前 Old School RuneScape 开发者因从玩家那里窃取 40 万美元而入狱——虚拟黄金被盗并在黑市上出售，之后 Jagex 使用隐藏的防火墙调整抓住了罪魁祸首" data-date="09-06 18:30" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-06 18:30</span>
          <span class="news-item-title">前 Old School RuneScape 开发者因从玩家那里窃取 40 万美元而入狱——虚拟黄金被盗并在黑市上出售，之后 Jagex 使用隐藏的防火墙调整抓住了罪魁祸首</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/011.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 6 日消息，据新浪汽车今日报道，2026 世界动力电池大会上，欧阳明高院士发布电池领域重大标志性技术成果：超快充动力电池技术：实现十分钟左右安全快充。高比能混合固液电池技术：实现 350Wh/kg 高比能高安全电池规模化生产。换电乘用车长寿命电池技术：解决换电电池长寿命服役的衰减问题。大容量高安全储能电池技术：储能电池从 300Ah 跨越到 600Ah，已规模化生产。第四代高压实磷酸铁锂材料技术：磷酸铁锂比能量超过 200Wh/kg。乘用车电池全气候热管理技术：破解低温充电慢、高温充电过热难题。新一代方形电池高速卷绕技术：生产效率从每分钟 4.4 个电芯提升到 7.5 个。构建国家电池强制安全标准的电池安全技术体系，支撑今年 7 月 1 日实施的国标。2026 世界动力电池" data-title="2026 世界动力电池大会重大标志性技术成果公布：超快充动力电池技术、高比能混合固液电池技术等" data-date="09-06 18:02" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-06 18:02</span>
          <span class="news-item-title">2026 世界动力电池大会重大标志性技术成果公布：超快充动力电池技术、高比能混合固液电池技术等</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/998/924.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 6 日消息，据科技媒体 Tweak Town 昨天报道，PS5 游戏机模拟器 KyTyPS5 近期取得进展，已经能够运行《GTA5》游戏北扬克顿序章任务。IT之家从原报道获悉，该模拟器可在 AMD 锐龙 9 9950X3D 处理器和 Radeon RX 7900 XT 显卡的 PC 上，以 40-60FPS 帧率运行《GTA5》的北扬克顿鲁登朵夫剧情。不过游戏画面表现仍然很不稳定，光照以及其他元素都会出现闪烁和消失现象。今年 7 月，KyTyPS5 模拟器还只能启动《GTA5》的主菜单和设置界面，完全无法进入故事模式。如今不到两个月后，模拟器已经能够实际运行游戏，进度喜人。不过，这款模拟器距离完美运行 PS5 版《侠盗猎车手 V》还有相当长的距离，当前阶段开发人员还有很多工" data-title="PS5 游戏机模拟器 KyTyPS5 新进展：可运行《GTA5》北扬克顿序章任务" data-date="09-06 14:27" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-06 14:27</span>
          <span class="news-item-title">PS5 游戏机模拟器 KyTyPS5 新进展：可运行《GTA5》北扬克顿序章任务</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-06/10691365.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网9月6日电 据公安部微信公众号消息，为进一步提升防范电信网络诈骗工作的信息化、智能化水平，帮助群众有效识诈防诈，近日，公安部刑侦局指导，上海市公安局自主研发的“国家反诈AI”APP正式上线。" data-title="随时能问、随手可查 反诈智能助手“国家反诈AI”APP上线" data-date="09-06 14:25" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 14:25</span>
          <span class="news-item-title">随时能问、随手可查 反诈智能助手“国家反诈AI”APP上线</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/998/922.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 6 日消息，公安部今日宣布，为进一步提升防范电信网络诈骗工作的信息化、智能化水平，帮助群众有效识诈防诈，近日，公安部刑侦局指导，上海市公安局自主研发的“国家反诈 AI”App 正式上线。据介绍，“国家反诈 AI”App 融合了大语言、多模态模型和智能体技术，用户通过手机输入可疑场景，该 App 即可完成风险研判、识别诈骗套路、推送典型案例，从“文字 + 语音 + 视频”等多个维度拆解诈骗手法，提供识别防范对策。IT之家从公安部了解到，“国家反诈 AI”App 有三大功能：一是 AI 大模型智能问答。用户提问后，系统将从诈骗风险分析、诈骗类型识别、防范建议等多个维度回答，并同步关联视频案例，实时为用户提供反诈知识学习和涉诈场景判断服务。二是反诈资讯。内嵌国家反诈中心和上海“8" data-title="“随时能问、随手可查”的反诈智能助手“国家反诈 AI”App 上线，微信、支付宝小程序也同步开放" data-date="09-06 13:44" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-06 13:44</span>
          <span class="news-item-title">“随时能问、随手可查”的反诈智能助手“国家反诈 AI”App 上线，微信、支付宝小程序也同步开放</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/sep/06/everton-v-manchester-united-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Minute-by-minute updates from the action at Hill Dickinson StadiumTransfer failures leave Everton scrambling | Mail TimAfternoon everyone and welcome to the David Moyes derby. Or is it the Wayne Rooney, Michael Keane, James Garner, Morgan Schneiderlin and not quite Joshua Zirkzee derby?The Premier League prediction posse, both human and automated," data-title="埃弗顿v曼联：英超联赛" data-date="09-06 19:36" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-06 19:36</span>
          <span class="news-item-title">埃弗顿v曼联：英超联赛</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-06/10691242.shtml" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="中新网巴黎9月6日电 中国经典歌剧《原野》当地时间5日晚亮相法国巴黎。该剧由中国对外文化集团有限公司“中华风韵”品牌呈现、中国歌剧舞剧院出品。" data-title="中国经典歌剧《原野》亮相法国巴黎" data-date="09-06 10:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 10:20</span>
          <span class="news-item-title">中国经典歌剧《原野》亮相法国巴黎</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cg49v57rxvgo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="经理迈克尔·卡里克（ Michael Carrick ）和首席执行官奥马尔·贝拉达（ Omar Berrada ）一致认为，尽管俱乐部的夏季支出相对较低，但曼联可以取得成功。" data-title="曼联计划如何与更富有的竞争对手竞争" data-date="09-06 05:57" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-06 05:57</span>
          <span class="news-item-title">曼联计划如何与更富有的竞争对手竞争</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cg49v57rxvgo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="经理迈克尔·卡里克（ Michael Carrick ）和首席执行官奥马尔·贝拉达（ Omar Berrada ）一致认为，尽管俱乐部的夏季支出相对较低，但曼联可以取得成功。" data-title="曼联计划如何与BIG竞争" data-date="09-06 05:57" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-06 05:57</span>
          <span class="news-item-title">曼联计划如何与BIG竞争</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cy8zd574yzyo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="解决生存话题可能还为时过早，但新晋升的赫尔城为自己提供了在英超联赛中建立的完美平台。" data-title="三场比赛的7分-赫尔是否正在避免降级？" data-date="09-06 04:56" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-06 04:56</span>
          <span class="news-item-title">三场比赛的7分-赫尔是否正在避免降级？</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cz7z09v9pp1o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="高级足球记者萨米·莫克贝尔（ Sami Mokbel ）进入了阿森纳的竞标，以利用他们的英超联赛冠军，并在今年夏天加强他们的阵容。" data-title="阿森纳在入围名单上有20多名球员，以利用冠军头衔" data-date="09-06 03:08" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-06 03:08</span>
          <span class="news-item-title">阿森纳在入围名单上有20多名球员，以利用冠军头衔</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/sep/05/hull-city-v-aston-villa-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="赫尔继续他们本赛季的不败开局，连续第三次对阵钝的阿斯顿维拉4分钟：赫尔安顿下来。房源正在蹦蹦跳跳。2分钟：杰克逊头宽！当Maatsen从左边穿过别墅时，杰克逊在赫尔中后卫之间上升，并将其带回最近的岗位。继续阅读..." data-title="赫尔城0-0阿斯顿维拉：英超联赛–事实如此" data-date="09-06 02:33" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-06 02:33</span>
          <span class="news-item-title">赫尔城0-0阿斯顿维拉：英超联赛–事实如此</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/05/hull-city-aston-villa-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="赫尔从来都不乏味，正如这些地方的俗话所说，仅仅三场比赛之后，英超联赛就被证明对赫尔城的支持者来说是一段相当长的路。在开幕当天让曼联感到尴尬并在上周末在考文垂获胜之后，这张当之无愧的积分和第三张干净的纸仅仅加强了谢尔盖·贾基罗维奇的信念，即他的手下可以击败失利。继续阅读..." data-title="高飞的船体保持不败，让阿斯顿维拉陷入僵局" data-date="09-06 02:28" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-06 02:28</span>
          <span class="news-item-title">高飞的船体保持不败，让阿斯顿维拉陷入僵局</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cx2zqp52pr2o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在克雷文小屋（ Craven Cottage ）水晶宫（ Crystal Palace ）以3比2击败英超联赛后，富勒姆（ Fulham ）被一些支持者嘘声" data-title="富勒姆连续第三次失利后嘘了一声" data-date="09-06 02:28" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-06 02:28</span>
          <span class="news-item-title">富勒姆连续第三次失利后嘘了一声</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cp3kql8g1vyo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="曼城给了1.85亿英镑的截止日期天才，他们的英超联赛在战胜考文垂的比赛中首次亮相-经理恩佐·马雷斯卡将享受他所看到的一切。" data-title="费尔南德斯和恩迪亚耶在曼城首次亮相时表现出希望的迹象" data-date="09-06 02:04" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-06 02:04</span>
          <span class="news-item-title">费尔南德斯和恩迪亚耶在曼城首次亮相时表现出希望的迹象</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/05/nottingham-forest-tottenham-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Oliver Glasner argued there was insufficient evidence to disallow Neco Williams’s goal against Tottenham, accusing the video assistant referee Peter Bankes of guessing that the Nottingham Forest defender handled and said ruling it out weakens the officials’ authority. Midway through the second half, Williams stooped to head in on the goalline as Sa" data-title="Glasner声称在Forest被拒绝赢得马刺之后， VAR正在“猜测”" data-date="09-06 01:59" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-06 01:59</span>
          <span class="news-item-title">Glasner声称在Forest被拒绝赢得马刺之后， VAR正在“猜测”</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c2e03wdw47jo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="托特纳姆热刺在首场三场英超比赛中未能得分，经理罗伯托·德·泽比表示，将他昂贵的球队打造成一支球队需要时间。" data-title="“不是足球经理” - De Zerbi说失误的马刺需要时间" data-date="09-06 01:56" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-06 01:56</span>
          <span class="news-item-title">“不是足球经理” - De Zerbi说失误的马刺需要时间</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/sep/05/premier-league-manchester-city-coventry-nottingham-forest-v-tottenham-efl-clockwatch-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Erling Haaland scored his 300th club goal while Crystal Palace’s left wing-backs grabbed the glory at Craven CottageIliman Ndiaye starts for City after joining from Everton in the week. Phil Foden drops out and will be joined on the bench by City’s other big signing, Enzo Fernandez.Coventry bring in Ethan Pinnock and Frank Onyeka for Caleb Yirenki" data-title="曼彻斯特城1-0考文垂，富勒姆2-3水晶宫等：足球钟表–恰巧" data-date="09-06 00:30" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-06 00:30</span>
          <span class="news-item-title">曼彻斯特城1-0考文垂，富勒姆2-3水晶宫等：足球钟表–恰巧</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/05/manchester-city-coventry-city-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Enzo Fernández started for Manchester City after Nico O’Reilly’s back injury during the warm-up and sparkled, showing why the club paid a British-record-equalling £125m for the midfielder. The winner came courtesy of Erling Haaland’s 300th goal in club football and Fernández had a key part, feeding Antoine Semenyo, whose cross from the right was cr" data-title="哈兰德超越曼城，超越考文垂，费尔南德斯在首次亮相时闪闪发光" data-date="09-06 00:02" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-06 00:02</span>
          <span class="news-item-title">哈兰德超越曼城，超越考文垂，费尔南德斯在首次亮相时闪闪发光</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/report/989270/fantasy-footballers-podcast-andy-holloway-interview" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Andy Holloway与他的朋友Jason Moore和Mike Wright共同主持了Fantasy Footballers播客。该节目是首屈一指的奇幻体育播客之一，每月吸引超过200万听众和众多奖项，包括来自iHeartRadio的最佳体育播客和连续四年在播客奖中的人民选择。Holloway的目标是[…]" data-title="Fantasy Footballers 的安迪·霍洛威 (Andy Holloway) 是一位专注的零" data-date="09-05 23:00" data-source="The Verge">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-05 23:00</span>
          <span class="news-item-title">Fantasy Footballers 的安迪·霍洛威 (Andy Holloway) 是一位专注的零</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/0/999/020.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 6 日消息，2026 世界超级摩托车锦标赛（WSBK）法国站 WorldSSP 组别次回合正赛今日在法国讷韦尔-马尼库尔赛道举行，比赛进行到还剩 8 圈时一度红旗中断，重新发车后排在第二的张雪机车 53 号车手瓦伦丁 · 德比斯最终完成 5 圈比赛拿下第三名，继第一回合季军登台后本赛季第 8 次登上领奖台。另一位张雪机车车手卡里卡苏洛，以第 8 名的成绩同样带回积分。至此，“张雪机车”完成法国站全部比赛。下一站比赛将于 9 月 25 日至 27 日在意大利克雷莫纳赛道举行。" data-title="2026 WSBK 法国站第二回合，张雪机车德比斯再获季军" data-date="09-06 19:33" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-06 19:33</span>
          <span class="news-item-title">2026 WSBK 法国站第二回合，张雪机车德比斯再获季军</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-06/10691541.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北海9月6日电(李梦)9月初，正值晚稻拔节孕穗的关键期，广西北海市海城区赤西村连片的稻田里，稻株长势喜人，稻叶翠绿舒展。这一时段，不仅是决定穗粒数量、筑牢产量基础的核心节点，也是病虫害防控的紧要关口。" data-title="孕穗关键期  “空中卫士”为广西北海守护稻田希望" data-date="09-06 19:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 19:33</span>
          <span class="news-item-title">孕穗关键期  “空中卫士”为广西北海守护稻田希望</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-06/10691521.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网广州9月6日电 题：薪火相传百年狮艺 广州乌溪少年舞动南粤" data-title="薪火相传百年狮艺 广州乌溪少年舞动南粤" data-date="09-06 19:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 19:28</span>
          <span class="news-item-title">薪火相传百年狮艺 广州乌溪少年舞动南粤</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-06/10691514.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京9月6日电 (刘艺静 张素)记者从中国关心下一代健康体育基金会获悉，关爱青年工程公益捐赠仪式5日在承德举行，此次捐赠活动聚焦智慧教学、沉浸式育人、校园食安监管三个领域，将为当地百余所学校配齐数字化教育设备与智慧管理系统。" data-title="关爱青年工程公益捐赠 聚焦智慧教学、沉浸式育人、校园食安监管" data-date="09-06 19:18" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 19:18</span>
          <span class="news-item-title">关爱青年工程公益捐赠 聚焦智慧教学、沉浸式育人、校园食安监管</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-06/10691535.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="9月6日，西藏自治区吉隆县“8·26”泥石流灾害应急救援指挥部举行中外媒体见面会。" data-title="预警窗口仅几分钟 吉隆泥石流灾害链源头在境外是监测最大短板" data-date="09-06 19:09" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 19:09</span>
          <span class="news-item-title">预警窗口仅几分钟 吉隆泥石流灾害链源头在境外是监测最大短板</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-06/10691531.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社成都9月6日电 (记者 阮煜琳)最新研究报告显示，自2013年以来，中国先后实施三个清洁空气行动计划，推动空气质量实现历史性改善，带来显著的公众健康收益。" data-title="中国清洁空气行动健康收益显著 持续深度治理PM2.5" data-date="09-06 18:54" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 18:54</span>
          <span class="news-item-title">中国清洁空气行动健康收益显著 持续深度治理PM2.5</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-06/10691528.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="独家！一名中国游客的尼泊尔泥石流脱困之路：通往外界的道路被摧毁，在中国使馆协调下登上尼军直升机" data-title="独家！一名中国游客的尼泊尔泥石流脱困之路" data-date="09-06 18:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 18:45</span>
          <span class="news-item-title">独家！一名中国游客的尼泊尔泥石流脱困之路</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-06/10691508.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网江西遂川9月6日电 (刘力鑫 朱莹 吴敏)受台风“沙德尔”带来的持续强降雨影响，江西省吉安市遂川县高坪镇明坑村石下组5日凌晨突发泥石流地质灾害。6日上午，记者随救援人员徒步近半小时，抵达此次泥石流灾害的核心受灾区。" data-title="直击江西遂川泥石流核心受灾区：路面淤泥没过小腿 救援难度大" data-date="09-06 18:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 18:39</span>
          <span class="news-item-title">直击江西遂川泥石流核心受灾区：路面淤泥没过小腿 救援难度大</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-06/10691520.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="记者今天从西藏自治区吉隆县“8·26”泥石流灾害应急救援指挥部举行的中外媒体见面会上了解到，灾害发生后，我国组织相关领域专家团队和技术力量，对东林藏布流域面积大于0.1平方公里的11处冰湖持续展开卫星遥感监测，目前冰湖面积未见异常。" data-title="卫星遥感监测显示：东林藏布流域冰湖面积目前未见异常" data-date="09-06 18:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 18:31</span>
          <span class="news-item-title">卫星遥感监测显示：东林藏布流域冰湖面积目前未见异常</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-06/10691519.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="记者今天从西藏自治区吉隆县“8·26”泥石流灾害应急救援指挥部举行的中外媒体见面会上了解到，针对吉隆口岸选址问题，日喀则市委副书记、代理市长罗布次仁表示，吉隆口岸自古便是茶马古道、唐蕃古道的核心节点，承载中尼双方千年贸易与人文交流，吉隆沟有地形、交通、边境通行的便利条件，历史上形成了重要陆路通道。据唐代、清代等相关史料记载，吉隆河谷地区是中国西藏与尼泊尔边民民间往来，双方人员可以通过喜马拉雅山脉来往通行。对口岸功能恢复等事宜进行深入研究论证。" data-title="西藏日喀则：将深入研究口岸功能恢复等事宜" data-date="09-06 18:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 18:29</span>
          <span class="news-item-title">西藏日喀则：将深入研究口岸功能恢复等事宜</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/storage/this-246tb-ssd-media-server-is-built-for-millionaire-cinephiles-kaleidescapes-newest-home-theater-vault-supports-25-simultaneous-4k-streams-stores-up-to-2-300-4k-cinematic-movies" target="_blank" rel="noopener" data-cat="zonghe" data-summary="豪华家庭影院设备制造商 Kaleidescape 推出了其最新的媒体服务器“Compact Terra Prime 246TB SSD”。" data-title="这款 246TB SSD 媒体服务器专为百万富翁影迷打造 — Kaleidescape 最新的家庭影院库支持 25 个同步 4K 流，可存储多达 2,300 部 4K 电影电影" data-date="09-06 18:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-06 18:00</span>
          <span class="news-item-title">这款 246TB SSD 媒体服务器专为百万富翁影迷打造 — Kaleidescape 最新的家庭影院库支持 25 个同步 4K 流，可存储多达 2,300 部 4K 电影电影</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/06/world/europe/ukraine-military-audits-spending-weapons.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="这些文件相当于对武器承包过程的尸体解剖。" data-title="秘密审计告诉我们乌克兰军方如何花钱" data-date="09-06 17:02" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-06 17:02</span>
          <span class="news-item-title">秘密审计告诉我们乌克兰军方如何花钱</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/06/us/memphis-cantina-gambling-raid-immigration.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="在今年田纳西州最大的移民行动之一的孟菲斯酒吧，有120多人被捕。" data-title="孟菲斯赌博突袭如何成为一场全面的移民行动" data-date="09-06 17:02" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-06 17:02</span>
          <span class="news-item-title">孟菲斯赌博突袭如何成为一场全面的移民行动</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/06/us/politics/hegseth-army-general-donahue.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="克里斯托弗· T ·多纳休（ Christopher T. Donahue ）将军对未来战争的愿景为他赢得了世界各地的强大支持者。他们能挽救他的事业吗？" data-title="从黑格塞特的军队清洗中拯救多纳休将军的战斗" data-date="09-06 17:00" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-06 17:00</span>
          <span class="news-item-title">从黑格塞特的军队清洗中拯救多纳休将军的战斗</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/06/world/europe/ukraine-war-weapons-fraud-corruption.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="秘密军事审计揭示了一个充斥着管理不善的军事采购系统。仅在2024年，乌克兰就因欺诈和浪费损失了12 $。" data-title="在乌克兰，欺诈和浪费得到更多武器合同的奖励" data-date="09-06 17:00" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-06 17:00</span>
          <span class="news-item-title">在乌克兰，欺诈和浪费得到更多武器合同的奖励</span>
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

<p class="news-updated">🕐 抓取更新于 2026-09-06 19:43（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
