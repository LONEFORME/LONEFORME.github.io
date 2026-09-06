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
      <span>2026-09-06 23:35 抓取更新</span>
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
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/09-06/10691607.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网合肥9月6日电 (记者 任帅 张强 储玮玮)9月6日晚，2026“把青春华章写在祖国大地上”大思政课网络主题宣传和互动引导活动在中国科学技术大学举行。针对现场有学生提问称“从小草房到世界五百强，这一路上哪个品牌是您最强劲的对手？”奇瑞汽车股份有限公司董事长尹同跃以一席幽默回答，赢得满堂彩。" data-title="青春华章丨奇瑞董事长幽默回应谁是最强劲对手" data-date="09-06 23:31" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 09-06 23:31</span>
      </div>
      <h2 class="hero-featured-title">青春华章丨奇瑞董事长幽默回应谁是最强劲对手</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/0/999/045.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 6 日消息，苹果公司于 9 月 1 日换帅迈入“特努斯时代”，约翰 · 特努斯（John Ternus）接替蒂姆 · 库克（Tim Cook）出任苹果公司 CEO，而库克同日转任董事会执行主席。苹果公司将于当地时间 9 月 9 日（北京时间 9 月 10 日凌晨 1 点）举行秋季新品发布会，主题为“亮新篇，来耀眼”（Surprise and shine），这将是约翰 · 特努斯接任苹果 CEO 后的首场发布会。IT之家注意到，彭博社的马克 · 古尔曼（Mark Gurman）今晚发文透露，库克将会出现在苹果秋季发布会现场，但他本人不会在活动视频中出镜。苹果一直在精心布局这场交接，意在让约翰 · 特努斯成为折叠屏 iPhone 及后续所有新品的核心代言人。如果此时让库克在发布" data-title="古尔曼：库克不会在苹果秋季发布会视频中出现，现在是特努斯时代" data-date="09-06 23:21" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">古尔曼：库克不会在苹果秋季发布会视频中出现，现在是特努斯时代</p>
    </a>
    <a class="hero-sub-card" href="https://www.theguardian.com/football/live/2026/sep/06/arsenal-v-chelsea-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="酋长球场比赛的每分钟更新 阿森纳在窗口关闭后保持连续性现在第三个进球......希尔迪金森体育场有第二个进球。点击点击点击点击！继续阅读..." data-title="阿森纳 VS 切尔西：英超联赛" data-date="09-06 23:35" data-source="卫报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-theathletic">🇬🇧 卫报</span>
      </div>
      <p class="hero-sub-title">阿森纳 VS 切尔西：英超联赛</p>
    </a>
    <a class="hero-sub-card" href="https://www.nytimes.com/2026/09/06/us/politics/hegseth-army-general-donahue.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="克里斯托弗·T·多纳休将军对未来战争的愿景为他赢得了世界各地的强大支持者。他们能挽救他的职业生涯吗？" data-title="将多纳休将军从赫格塞斯的军队清洗中拯救出来的战斗" data-date="09-06 23:19" data-source="纽约时报">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
      </div>
      <p class="hero-sub-title">将多纳休将军从赫格塞斯的军队清洗中拯救出来的战斗</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-06/10691607.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网合肥9月6日电 (记者 任帅 张强 储玮玮)9月6日晚，2026“把青春华章写在祖国大地上”大思政课网络主题宣传和互动引导活动在中国科学技术大学举行。针对现场有学生提问称“从小草房到世界五百强，这一路上哪个品牌是您最强劲的对手？”奇瑞汽车股份有限公司董事长尹同跃以一席幽默回答，赢得满堂彩。" data-title="青春华章丨奇瑞董事长幽默回应谁是最强劲对手" data-date="09-06 23:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 23:31</span>
          <span class="news-item-title">青春华章丨奇瑞董事长幽默回应谁是最强劲对手</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-06/10691602.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网合肥9月6日电 (记者 任帅 张强 储玮玮)9月6日晚，2026“把青春华章写在祖国大地上”大思政课网络主题宣传和互动引导活动在中国科学技术大学举行。" data-title="青春华章丨“国家需要什么，我们就做什么”！中国科研人的这番话，热血又有力量" data-date="09-06 22:51" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 22:51</span>
          <span class="news-item-title">青春华章丨“国家需要什么，我们就做什么”！中国科研人的这番话，热血又有力量</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/06/us/politics/trump-mail-in-voting-supreme-court.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="该文件将总统推动对邮寄投票施加限制的合法性直接摆在法官面前，即使各州开始寄出选票。" data-title="特朗普政府再次要求最高法院允许邮寄投票限制" data-date="09-06 22:31" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-06 22:31</span>
          <span class="news-item-title">特朗普政府再次要求最高法院允许邮寄投票限制</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-06/10691594.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网合肥9月6日电 (记者 任帅 张强 储玮玮)9月6日晚，2026“把青春华章写在祖国大地上”大思政课网络主题宣传和互动引导活动在中国科学技术大学(简称“中国科大”)举行。中国科学院院士、中国科学技术大学校长常进在会上，用三件信物勉励莘莘学子：一枚重达515克、纯金打造的“两弹一星”功勋奖章；一块粗糙的红砖；一组珍贵照片。常进动情地说，愿学生们像“两弹一星”元勋那样胸怀家国，像烧砖前辈那样自自立自强，和当代中国科大人一起勇攀高峰。(记者 任帅 张强 储玮玮)" data-title="青春华章丨院士展示三件信物勉励莘莘学子" data-date="09-06 21:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 21:32</span>
          <span class="news-item-title">青春华章丨院士展示三件信物勉励莘莘学子</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-06/10691554.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="总台记者当地时间9月6日获悉，刚果(金)政府通报，首都金沙萨5日一婚礼现场发生的火灾事故造成的死亡人数更正为12人，此前地方官员公布的数据为22人。" data-title="刚果（金）婚礼火灾事故遇难人数更正为12人" data-date="09-06 19:47" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 19:47</span>
          <span class="news-item-title">刚果（金）婚礼火灾事故遇难人数更正为12人</span>
        </a>
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
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/0/999/045.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 6 日消息，苹果公司于 9 月 1 日换帅迈入“特努斯时代”，约翰 · 特努斯（John Ternus）接替蒂姆 · 库克（Tim Cook）出任苹果公司 CEO，而库克同日转任董事会执行主席。苹果公司将于当地时间 9 月 9 日（北京时间 9 月 10 日凌晨 1 点）举行秋季新品发布会，主题为“亮新篇，来耀眼”（Surprise and shine），这将是约翰 · 特努斯接任苹果 CEO 后的首场发布会。IT之家注意到，彭博社的马克 · 古尔曼（Mark Gurman）今晚发文透露，库克将会出现在苹果秋季发布会现场，但他本人不会在活动视频中出镜。苹果一直在精心布局这场交接，意在让约翰 · 特努斯成为折叠屏 iPhone 及后续所有新品的核心代言人。如果此时让库克在发布" data-title="古尔曼：库克不会在苹果秋季发布会视频中出现，现在是特努斯时代" data-date="09-06 23:21" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-06 23:21</span>
          <span class="news-item-title">古尔曼：库克不会在苹果秋季发布会视频中出现，现在是特努斯时代</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-06/10691605.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网合肥9月6日电 (记者 任帅 张强 储玮玮)9月6日晚，2026“把青春华章写在祖国大地上”大思政课网络主题宣传和互动引导活动在中国科学技术大学举行。中国为什么要倾尽心力深耕量子信息科技？中国科学院院士、中国科学技术大学常务副校长潘建伟在会上表示，因为这一领域是新一轮科技革命和产业变革的关键基石，是关乎国家未来科技主动权的战略必争领域。量子通信守护国家信息安全，量子计算重塑未来算力格局，这不是遥远的科学概念，是国家长远发展的底气。经过三十年不懈努力，中国在量子领域终于实现了从跟跑、并跑到部分领跑的跨越。" data-title="青春华章丨中国为何要倾尽心力深耕量子信息科技？潘建伟解答" data-date="09-06 23:16" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 23:16</span>
          <span class="news-item-title">青春华章丨中国为何要倾尽心力深耕量子信息科技？潘建伟解答</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/044.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 6 日消息，据彭博社记者马克 · 古尔曼最新一期《Power On》时事通讯透露，苹果据称正在考虑对 App Store 进行一些调整，目标是进一步提高这一平台带来的收入。目前还不清楚苹果究竟计划对 App Store 做出哪些改变。古尔曼表示，苹果希望“想办法提高利润率，并从这一平台榨取更多持续性收入”，而这项工作主要由苹果新任 CEO 约翰 · 特努斯和现任服务业务高级副总裁埃迪 · 库伊推动。据称，这项计划也是苹果长期高管菲尔 · 席勒上周离职的原因之一。席勒在 2020 年卸任苹果全球营销高级副总裁一职后，转任苹果 Fellow（苹果院士），其职责之一就是负责 App Store。不过，席勒似乎并不赞成这一想法。古尔曼写道，席勒认为，这类举措只会进一步激怒开发者和政" data-title="古尔曼：苹果考虑调整 App Store 以提高收入和利润率" data-date="09-06 23:03" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-06 23:03</span>
          <span class="news-item-title">古尔曼：苹果考虑调整 App Store 以提高收入和利润率</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/gpus/single-slot-low-profile-75w-rtx-3060-with-no-power-connectors-disappoints-in-tests-gpu-runs-entirely-off-the-pcie-slot-but-offers-severely-crippled-performance-and-frightening-thermals" target="_blank" rel="noopener" data-cat="keji" data-summary="如果您想将 12GB RTX 3060 的性能降低一半，同时降低散热性能，那么这可能是您的完美产品。" data-title="没有电源连接器的单插槽薄型 75W RTX 3060 在测试中令人失望 - GPU 完全依靠 PCIe 插槽运行，但性能严重受损且散热令人恐惧" data-date="09-06 22:58" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-06 22:58</span>
          <span class="news-item-title">没有电源连接器的单插槽薄型 75W RTX 3060 在测试中令人失望 - GPU 完全依靠 PCIe 插槽运行，但性能严重受损且散热令人恐惧</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/043.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 6 日消息，据韩联社昨日报道，三星电子同行工会宣布，将在三星电子会长李在镕的住宅前举行集会，抗议内部薪酬差距。该工会主要由负责智能手机、家电等终端产品的 DX 部门员工组成。业内人士于 9 月 5 日透露，同行工会计划从 18 日开始，在首尔龙山区李在镕住宅附近持续举行集会及单人示威。同行工会相关负责人接受采访时表示：“我们不设截止期限，计划长期抗争。在未能获批集会申报的日子里，将通过单人示威的形式继续进行。”IT之家注意到，同行工会指出，在今年 5 月三星电子劳资双方达成的薪资协议中，DX 部门被边缘化，其薪酬水平与负责半导体业务的 DS 部门存在过大差距。基于此，同行工会提出了以下诉求：向 DX 部门员工每人发放 1,000 股公司股票；提取全公司一定比例的经营利润，设" data-title="三星电子 DX 部门工会不满与其他部门薪酬差距，将在会长李在镕住宅前集会抗议" data-date="09-06 22:43" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-06 22:43</span>
          <span class="news-item-title">三星电子 DX 部门工会不满与其他部门薪酬差距，将在会长李在镕住宅前集会抗议</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-admits-to-wiki-incident-after-its-agents-were-discovered-using-a-programming-hub-to-communicate-says-more-transparency-is-needed-regarding-misalignments" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI承认，其实验性人工智能代理使用开放的德国编程维基进行通信。" data-title="OpenAI 在其代理被发现使用编程中心进行通信后承认发生了“维基事件”——表示需要提高关于错位的透明度" data-date="09-06 22:31" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-06 22:31</span>
          <span class="news-item-title">OpenAI 在其代理被发现使用编程中心进行通信后承认发生了“维基事件”——表示需要提高关于错位的透明度</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/041.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 6 日消息，小米集团合伙人、总裁卢伟冰今晚发文称：“彩排结束，内容很丰富，还有惊喜。”此外，他还在评论区透露本次发布会不会登场，雷军将讲全场。IT之家注意到，小米秋季旗舰新品发布会将于 9 月 7 日晚 7 点举行，小米澎程 N70 Pro、N70 Max、N90 Max 正式上市。同场发布的，还有两款旗舰新品：小米 18 Fold 全新折叠屏旗舰手机、小米平板 9 Pro Max，首发玄戒 O3 AI 旗舰处理器。雷军此前透露，这次的发布会是小米科技创新的一次集中展示，时间估计有点长，会努力控制在 2 小时 45 分钟以内。主要产品中，今年 7 月 30 日，小米举行了澎程技术发布会，澎程 N90 Max 预售价为 29.99 万元；澎程 N70 Max 预售价为 25." data-title="小米卢伟冰预告明晚发布会有惊喜，雷军讲全场" data-date="09-06 22:30" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-06 22:30</span>
          <span class="news-item-title">小米卢伟冰预告明晚发布会有惊喜，雷军讲全场</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/040.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 6 日消息，9 月 1 日，商务部、工业和信息化部、市场监管总局三部门发布《汽车行业境外竞争行为与合规建设指引》。《汽车行业境外竞争行为与合规建设指引》为从事国际化生产经营活动的中国汽车行业企业在境外发生的市场竞争等生产经营行为提供参照，重点围绕汽车行业企业海外营销等竞争行为，以及境外安全生产、质量管理、劳动保障、数据安全等合规建设，提出一般性指引，供企业参考。IT之家注意到，长安汽车于 9 月 4 日宣布，合规不是成本，而是可持续发展的竞争力。未来，长安汽车将以更高标准推进海外合规建设，为中国汽车品牌在全球市场稳行致远筑能力基石。截至IT之家发文，比亚迪、奇瑞、赛力斯、吉利控股、长城汽车、广汽集团等车企均已发文回应《汽车行业境外竞争行为与合规建设指引》。" data-title="长安汽车响应《汽车行业境外竞争行为与合规建设指引》：将以更高标准推进海外合规建设" data-date="09-06 22:20" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-06 22:20</span>
          <span class="news-item-title">长安汽车响应《汽车行业境外竞争行为与合规建设指引》：将以更高标准推进海外合规建设</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/039.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 6 日消息，联想来酷 Air 16 酷睿版笔记本今日开启预约，9 月 10 日 20:00 正式开售，国补到手价 3314.15 元起。据介绍，该产品约 1.28kg 轻盈全金属机身，超薄约 13.3mm，采用 16 英寸黄金尺寸，提供凝霜银、暮霞紫、涧云蓝配色，支持 3 挡背光调节、1.2mm 键程。该产品搭载第三代英特尔酷睿处理器，Intel 18A 领先制程，功耗降低 64%，网页浏览性能提升 45%。该产品拥有约 17.8 小时超长办公续航，支持 65W PD 便携适配器。产品配备 16:10 高清屏幕，支持 300nits 亮度 (典型值)、100% sRGB (典型值)、DC 调光无频闪。IT之家整理价格信息如下：凝霜银Core3 304+12GB+512GB" data-title="联想来酷 Air 16 酷睿版笔记本开启预约，国补到手价 3314.15 元起" data-date="09-06 22:11" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-06 22:11</span>
          <span class="news-item-title">联想来酷 Air 16 酷睿版笔记本开启预约，国补到手价 3314.15 元起</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-06/10691597.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网合肥9月6日电(记者 任帅 张强 储玮玮) 9月6日晚，2026“把青春华章写在祖国大地上”大思政课网络主题宣传和互动引导活动在中国科学技术大学举行。“时代楷模”、国防科技大学计算机学院研究员王戟感慨道：“如今，我坐着轮椅，继续追逐前沿科技，继续为科技强军努力工作。只要大脑还能思考，我就是科研战场上的战士，只要双手还能敲键盘，我就可以继续冲锋！”王戟感慨道，何其有幸，他能把个人奋斗和国家命运紧紧相连。祖国不会辜负每一个实干者，“同学们，请你们珍惜现在这个伟大的时代。未来你们无论去往何方，请记住四个字‘同频共振’。把自己安放于国家需要之处，路自然越走越宽。”" data-title="青春华章丨“时代楷模”王戟：只要大脑还能思考，我就是科研战场上的战士" data-date="09-06 22:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 22:01</span>
          <span class="news-item-title">青春华章丨“时代楷模”王戟：只要大脑还能思考，我就是科研战场上的战士</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/power-supplies/fsp-mega-gm-1200w-power-supply-review" target="_blank" rel="noopener" data-cat="keji" data-summary="FSP Mega GM 1200W 电源具有白金级效率、全日本电容器组以及 1200W 设备中罕见的紧凑占地面积。" data-title="FSP Mega GM 1200W电源评测：悄然超越自家金标的全汉自研平台" data-date="09-06 21:57" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-06 21:57</span>
          <span class="news-item-title">FSP Mega GM 1200W电源评测：悄然超越自家金标的全汉自研平台</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/bitcoin-mining-data-center-condemned-after-leaking-3-million-gallons-of-water-and-forcing-school-closures-facility-operated-for-years-under-a-city-stop-work-order" target="_blank" rel="noopener" data-cat="keji" data-summary="俄克拉荷马州埃尔里诺市的一个比特币挖矿数据中心因泄漏 300 万加仑的水而受到谴责。" data-title="比特币挖矿数据中心因泄漏 300 万加仑水并迫使学校关闭而受到谴责——该设施在城市停工令下运营多年" data-date="09-06 21:44" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-06 21:44</span>
          <span class="news-item-title">比特币挖矿数据中心因泄漏 300 万加仑水并迫使学校关闭而受到谴责——该设施在城市停工令下运营多年</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/ssds/samsung-990-2tb-pcie-4-0-ssd-falls-to-usd339-99-on-amazon-usd190-discount-makes-high-capacity-storage-more-affordable" target="_blank" rel="noopener" data-cat="keji" data-summary="三星 2TB 990 为游戏提供充足的快速存储空间，目前比常规价格 529.99 美元便宜 190 美元。" data-title="三星 990 2TB PCIe 4.0 SSD 在亚马逊上跌至 339.99 美元——190 美元折扣让大容量存储更实惠" data-date="09-06 21:08" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-06 21:08</span>
          <span class="news-item-title">三星 990 2TB PCIe 4.0 SSD 在亚马逊上跌至 339.99 美元——190 美元折扣让大容量存储更实惠</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/tech/990436/fairphone-6-plus-review" target="_blank" rel="noopener" data-cat="keji" data-summary="Fairphone 6 Plus感觉像是一款非常普通的中端Android手机，我非常激动。这项任务一直令人钦佩。Fairphone寻求道德来源的材料，并为其设备提供高度的可维修性。但手机本身需要做出很多牺牲，比如容忍处理器性能不足[…]" data-title="Fairphone 6 Plus是我们迫切需要的中端手机" data-date="09-06 21:00" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-06 21:00</span>
          <span class="news-item-title">Fairphone 6 Plus是我们迫切需要的中端手机</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/pc-components/liquid-cooling/msi-meg-coreliquid-e15-360-aio-review-bold-and-stunning-with-market-leading-performance" target="_blank" rel="noopener" data-cat="keji" data-summary="微星的 MEG CoreLiquid E15 360 AIO 是一款豪华散热产品，拥有令人惊叹的 6.7 英寸屏幕和业界领先的散热性能。" data-title="微星MEG CoreLiquid E15 360一体机评测：大胆惊艳，有市场" data-date="09-06 20:48" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-06 20:48</span>
          <span class="news-item-title">微星MEG CoreLiquid E15 360一体机评测：大胆惊艳，有市场</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/sep/06/arsenal-v-chelsea-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="酋长球场比赛的每分钟更新 阿森纳在窗口关闭后保持连续性现在第三个进球......希尔迪金森体育场有第二个进球。点击点击点击点击！继续阅读..." data-title="阿森纳 VS 切尔西：英超联赛" data-date="09-06 23:35" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-06 23:35</span>
          <span class="news-item-title">阿森纳 VS 切尔西：英超联赛</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/sep/06/everton-v-manchester-united-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="伊恩·科佩斯塔克（ Ian Copestake ）说： “从伯肯黑德（ Birkenhead ）到比赛的火车上，埃弗顿球迷对埃弗顿（ Everton ）的转会失败一分钟一分钟地进行了更新，这让埃弗顿（ Everton ）陷入了困境。新业主（未提及闪亮的新体育场）的承诺尚未兑现。叛变就在拐角处（可能在沙丘）。”来自John Ste的意想不到的提议" data-title="埃弗顿 2-2 曼联：英超联赛——事情发生了" data-date="09-06 23:29" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-06 23:29</span>
          <span class="news-item-title">埃弗顿 2-2 曼联：英超联赛——事情发生了</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/06/everton-manchester-united-premier-league-match-report" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="温和地说，埃弗顿在周一以签下安斯利·梅特兰-内尔斯（ Ainsley Maitland-Niles ）结束时，对新右后卫的详尽寻找得到了压倒性的回应。但是，对于这位£ 430万新兵的埃弗顿首次亮相，人们的反应非常积极，因为他惊人的25码罢工几乎在对阵曼联的比赛中最后一脚抢救了一分。迈克尔·卡里克在比赛结束后完全难以置信地擦了擦脸。" data-title="梅特兰-奈尔斯的绝妙进球帮助埃弗顿对阵曼联" data-date="09-06 23:22" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-06 23:22</span>
          <span class="news-item-title">梅特兰-奈尔斯的绝妙进球帮助埃弗顿对阵曼联</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c78070053wvo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="埃弗顿和曼联球员在希尔狄金森体育场的评分。" data-title="哪个子项目影响最大？埃弗顿 v 曼联 球员评分" data-date="09-06 23:11" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-06 23:11</span>
          <span class="news-item-title">哪个子项目影响最大？埃弗顿 v 曼联 球员评分</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/042.htm" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="IT之家 9 月 6 日消息，据卫报报道，午休期间，吉尔 · 森内特看到了一些让她完全提不起食欲的东西，于是忍不住分享给自己在 X 平台上的 2.6 万名粉丝：一家牙买加烧烤快闪餐厅使用人工智能生成的菜单图片，里面的肉看起来像是一条条皮带，上面还爬满了细小的甲虫。这些图片随后被 500 多人转发，许多人同样表达了厌恶之情。现年 37 岁、居住在丹佛的护士森内特表示，吃饭“是人类最基本的体验之一”。她说：“我认为，餐厅开始采用这种恐怖、诡异又让人毫无食欲的食物图片，是一种不好的文化现象。”不过，森内特最终还是点了鸡肉和芝士通心粉。这家餐厅是她午餐时为数不多的选择之一，而且她以前也在那里吃过饭。如今，越来越多消费者开始在餐厅菜单和营销材料中看到 AI 生成的食物图片。很多食客认为，这些图片既不诱" data-title="诡异又倒胃口：AI 食物图片攻占餐厅菜单，让消费者食欲全无" data-date="09-06 22:37" data-source="IT之家">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-06 22:37</span>
          <span class="news-item-title">诡异又倒胃口：AI 食物图片攻占餐厅菜单，让消费者食欲全无</span>
        </a>
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
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cg49v57rxvgo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="主教练迈克尔·卡里克和首席执行官奥马尔·贝拉达一致认为，尽管俱乐部夏季支出相对较低，但曼联仍能取得成功。" data-title="曼联计划如何与大牌球队竞争" data-date="09-06 05:57" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-06 05:57</span>
          <span class="news-item-title">曼联计划如何与大牌球队竞争</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cy8zd574yzyo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="解决生存话题可能还为时过早，但新晋升的赫尔城为自己提供了在英超联赛中建立的完美平台。" data-title="三场比赛的7分-赫尔是否正在避免降级？" data-date="09-06 04:56" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-06 04:56</span>
          <span class="news-item-title">三场比赛的7分-赫尔是否正在避免降级？</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cy8zd574yzyo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="现在解决生存问题可能还为时过早，但升班马赫尔城已经为自己在英超联赛中提供了完美的平台。" data-title="三场比赛积七分——赫尔城有望保级吗？" data-date="09-06 04:56" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-06 04:56</span>
          <span class="news-item-title">三场比赛积七分——赫尔城有望保级吗？</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cz7z09v9pp1o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="高级足球记者萨米·莫克贝尔（ Sami Mokbel ）进入了阿森纳的竞标，以利用他们的英超联赛冠军，并在今年夏天加强他们的阵容。" data-title="阿森纳在入围名单上有20多名球员，以利用冠军头衔" data-date="09-06 03:08" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-06 03:08</span>
          <span class="news-item-title">阿森纳在入围名单上有20多名球员，以利用冠军头衔</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cz7z09v9pp1o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="资深足球记者萨米·莫克贝尔深入了解了阿森纳今年夏天利用英超冠军头衔并加强阵容的努力。" data-title="阿森纳有超过 20 名球员入围争夺冠军的候选名单" data-date="09-06 03:08" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-06 03:08</span>
          <span class="news-item-title">阿森纳有超过 20 名球员入围争夺冠军的候选名单</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c3v4537e60yo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="诺丁汉森林队主教练奥利弗·格拉斯纳和内科·威廉姆斯认为，VAR 不应该排除后卫对阵托特纳姆热刺队的进球。" data-title="格拉斯纳和威廉姆斯对森林队手球的 VAR 判罚提出异议" data-date="09-06 02:36" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-06 02:36</span>
          <span class="news-item-title">格拉斯纳和威廉姆斯对森林队手球的 VAR 判罚提出异议</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.nytimes.com/2026/09/06/us/politics/hegseth-army-general-donahue.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="克里斯托弗·T·多纳休将军对未来战争的愿景为他赢得了世界各地的强大支持者。他们能挽救他的职业生涯吗？" data-title="将多纳休将军从赫格塞斯的军队清洗中拯救出来的战斗" data-date="09-06 23:19" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-06 23:19</span>
          <span class="news-item-title">将多纳休将军从赫格塞斯的军队清洗中拯救出来的战斗</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-06/10691604.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网合肥9月6日电 (记者 任帅 张强 储玮玮)9月6日晚，2026“把青春华章写在祖国大地上”大思政课网络主题宣传和互动引导活动在中国科学技术大学举行。演员马少骅赞叹：安徽了不起，中国文房四宝安徽占三宝。其中，宣纸的历史有1200多年，也就是在唐朝的时候就有了。他说，宣纸制作有108道工序，“创造宣纸的人，就是当时中国的具有创造性的科学家。”" data-title="青春华章丨马少骅称创造宣纸的人就是当时中国的科学家" data-date="09-06 23:15" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 23:15</span>
          <span class="news-item-title">青春华章丨马少骅称创造宣纸的人就是当时中国的科学家</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-06/10691600.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网合肥9月6日电 (记者任帅 张强 储玮玮)9月6日晚，2026“把青春华章写在祖国大地上”大思政课网络主题宣传和互动引导活动在中国科学技术大学举行。国家级非物质文化遗产项目黄梅戏代表性传承人、中国科学技术大学首位“驻校艺术家”韩再芬邀请学子学唱黄梅戏，并现场表演了一段，引发全场掌声。" data-title="青春华章丨黄梅戏艺术家韩再芬邀学子学唱黄梅戏" data-date="09-06 22:40" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 22:40</span>
          <span class="news-item-title">青春华章丨黄梅戏艺术家韩再芬邀学子学唱黄梅戏</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-06/10691598.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网合肥9月6日电 (记者 任帅 张强 储玮玮)9月6日晚，2026“把青春华章写在祖国大地上”大思政课网络主题宣传和互动引导活动在中国科学技术大学举行。 演员、歌手孙浩现场演唱《中华民谣》，“朝花夕拾杯中酒”曲调一出，引发全场大合唱。" data-title="青春华章丨孙浩再唱《中华民谣》引全场大合唱" data-date="09-06 22:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 22:26</span>
          <span class="news-item-title">青春华章丨孙浩再唱《中华民谣》引全场大合唱</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/037.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 6 日消息，据央视财经报道，随着 AI 短剧、数字广告产业快速扩张，数字人脸素材采购需求持续高涨。一门特殊的生意 ——“人脸授权”也因此火了起来。不用出镜拍戏、无需线下试镜，依靠自己的面部形象就能赚取收益。IT之家从报道获悉，平台工作人员表示，根据授权人不同，AI 数字形象分为普通人和专业演员两大类：普通人的数字肖像按照每部短视频约 100 元付费使用；专业演员则按使用范围和剧集长度定价，价格从 500 元到数千元。采购方可以按年龄、性别、风格挑选并购买使用权。成交后，平台和授权人按比例分成。行业研究机构 Data Eye 的估算数据显示，今年前 5 个月，AI 短剧市场规模已突破 220 亿元，全年有望冲击 400 亿元大关；一季度全行业上线的微短剧中，AI 微短剧占比超" data-title="AI 短剧爆发带火“人脸授权”，普通人数字肖像价格约每部 100 元" data-date="09-06 22:06" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-06 22:06</span>
          <span class="news-item-title">AI 短剧爆发带火“人脸授权”，普通人数字肖像价格约每部 100 元</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cj4j2kp0818o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="印度洋葱价格急剧飙升，这种家家户户必备食材正被运往主要城市。这个国家生产和消费大量洋葱，而其价格波动历来具有政治影响。" data-title="印度洋葱“政治敏感”得要坐上铁路快车" data-date="09-06 21:17" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-06 21:17</span>
          <span class="news-item-title">印度洋葱“政治敏感”得要坐上铁路快车</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-06/10691589.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网北京9月6日电 在哈尔滨医科大学迎来建校100周年之际，中国科学技术出版社近日对16年前出版的《发现伍连德——诺贝尔奖候选人华人第一人》一书首版进行了二次印刷。" data-title="哈尔滨医科大学迎百年校庆 《发现伍连德》一书重印" data-date="09-06 21:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 21:08</span>
          <span class="news-item-title">哈尔滨医科大学迎百年校庆 《发现伍连德》一书重印</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/games/990691/competitive-pokemon-champions-mobile-tournament-accessibility" target="_blank" rel="noopener" data-cat="zonghe" data-summary="要开始 Pokémon 竞技对战，您只需要手机即可。但要参加最高级别的比赛，例如神奇宝贝世界锦标赛，您将需要 Switch。而且似乎没有充分的理由。战斗模拟器 Pokémon Champion 最初在 Switch 和 Switch 2 上推出 [...]" data-title="口袋妖怪竞技现已登陆手机，但你仍需要 Switch 才能成为冠军" data-date="09-06 21:00" data-source="The Verge">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">09-06 21:00</span>
          <span class="news-item-title">口袋妖怪竞技现已登陆手机，但你仍需要 Switch 才能成为冠军</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-06/10691581.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社西藏吉隆9月6日电 (记者 赵朗)记者6日从西藏自治区吉隆县“8·26”泥石流灾害应急救援指挥部举行的中外媒体见面会上获悉，西藏将对吉隆口岸周边灾害风险深入评估，对口岸相关功能恢复等事宜进行深入研究论证。" data-title="西藏吉隆泥石流灾后：将深入研究口岸相关功能恢复等事宜" data-date="09-06 20:49" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 20:49</span>
          <span class="news-item-title">西藏吉隆泥石流灾后：将深入研究口岸相关功能恢复等事宜</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-06/10691579.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网瑞丽9月6日电 (杨雪梅)6日，2026年瑞丽市首届“瑞丽江杯”系列体育赛事在位于云南省德宏傣族景颇族自治州的瑞丽国际文体中心开幕。来自中缅两国的近1500名运动员齐聚边城瑞丽，以体育赛事为媒，共叙“胞波”情谊。" data-title="近1500名中缅运动员齐聚云南瑞丽 以赛畅叙“胞波”情" data-date="09-06 20:48" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 20:48</span>
          <span class="news-item-title">近1500名中缅运动员齐聚云南瑞丽 以赛畅叙“胞波”情</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-06/10691562.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网杭州9月6日电 (钱晨菲)6日，浙江省防指发布消息称，根据《浙江省防汛防台抗旱应急预案》，经会商研判，决定于当日15时结束海上防台风应急响应。" data-title="台风“科罗旺”逐渐远离东海 浙江结束海上防台风应急响应" data-date="09-06 20:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 20:01</span>
          <span class="news-item-title">台风“科罗旺”逐渐远离东海 浙江结束海上防台风应急响应</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-06/10691553.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="新华社南昌9月6日电(记者闵尊涛)6日下午，记者从江西省吉安市遂川县相关部门获悉，左安镇扬芬村地质灾害已找到1名失联人员，已无生命体征。截至目前，遂川县因地质灾害造成的遇难者人数增至4人。此前，遂川县高坪镇明坑村的泥石流和山体滑坡灾害已造成3人遇难，另有9人失联。目前，多方力量仍在现场展开救援。" data-title="江西遂川地质灾害遇难人数增至4人" data-date="09-06 19:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 19:45</span>
          <span class="news-item-title">江西遂川地质灾害遇难人数增至4人</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-06/10691545.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社西藏吉隆9月6日电 (赵朗 李林 贡嘎来松)记者6日从西藏自治区吉隆县“8·26”泥石流灾害应急救援指挥部举行的中外媒体见面会上获悉，灾害发生后，截至9月5日18时，累计接待家属791人，安置家属640人。当地已妥善做好1720名尼泊尔籍边民的生活保障。" data-title="西藏吉隆泥石流灾害后 已妥善做好1720名尼籍边民生活保障" data-date="09-06 19:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 19:44</span>
          <span class="news-item-title">西藏吉隆泥石流灾害后 已妥善做好1720名尼籍边民生活保障</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-06/10691546.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社厦门9月6日电 (吴冠标)今年是厦门大学建校105周年暨机械工程学科创立100周年，厦门大学智能制造学院6日在厦门成立。" data-title="厦门大学智能制造学院成立" data-date="09-06 19:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-06 19:42</span>
          <span class="news-item-title">厦门大学智能制造学院成立</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/020.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 6 日消息，2026 世界超级摩托车锦标赛（WSBK）法国站 WorldSSP 组别次回合正赛今日在法国讷韦尔-马尼库尔赛道举行，比赛进行到还剩 8 圈时一度红旗中断，重新发车后排在第二的张雪机车 53 号车手瓦伦丁 · 德比斯最终完成 5 圈比赛拿下第三名，继第一回合季军登台后本赛季第 8 次登上领奖台。另一位张雪机车车手卡里卡苏洛，以第 8 名的成绩同样带回积分。至此，“张雪机车”完成法国站全部比赛。下一站比赛将于 9 月 25 日至 27 日在意大利克雷莫纳赛道举行。" data-title="2026 WSBK 法国站第二回合，张雪机车德比斯再获季军" data-date="09-06 19:33" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-06 19:33</span>
          <span class="news-item-title">2026 WSBK 法国站第二回合，张雪机车德比斯再获季军</span>
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

<p class="news-updated">🕐 抓取更新于 2026-09-06 23:35（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
