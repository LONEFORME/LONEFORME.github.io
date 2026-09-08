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
      <span>2026-09-08 14:38 抓取更新</span>
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
        <span class="channel-count">54</span>
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
        <span class="channel-count">9</span>
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
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/09-08/10692565.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网呼和浩特9月8日电 (记者 赵永厚 张玮)第十六届中蒙新闻论坛8日在内蒙古自治区呼和浩特市举办，来自中国、蒙古国的百余名媒体记者就深化中蒙两国新闻媒体交流合作、共同讲好中蒙友好故事等重要议题进行讨论和交流经验。" data-title="第十六届中蒙新闻论坛在内蒙古举办" data-date="09-08 14:26" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 09-08 14:26</span>
      </div>
      <h2 class="hero-featured-title">第十六届中蒙新闻论坛在内蒙古举办</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/0/999/691.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 8 日消息，小米汽车官方本月初宣布，2026 年 8 月，小米汽车交付量持续超过 30,000 台。小米汽车官方并未公布具体的交付数据，不过在乘联分会今日公布的 2026 年 8 月份全国乘用车市场分析中，IT之家查询到了其具体的零售销量为 30,153 辆。IT之家附小米汽车 2026 年各月交付量（官方口径）：1 月交付量超 39000 台2 月交付量超 20000 台3 月交付量超 20000 台4 月交付量超 30000 台5 月交付量超 30000 台6 月交付量超 30000 台7 月交付量超 30,000 台8 月交付量超 30,000 台另外，小米创办人、董事长兼 CEO 雷军昨日宣布，小米汽车累计交付量超过 80 万辆。" data-title="乘联分会报告披露小米汽车 8 月零售销量 30,153 辆" data-date="09-08 14:42" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">乘联分会报告披露小米汽车 8 月零售销量 30,153 辆</p>
    </a>
    <a class="hero-sub-card" href="https://www.chinanews.com.cn/gj/2026/09-08/10692381.shtml" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="中新网巴黎9月8日电 “《原野》回响——中法歌剧艺术分享会”当地时间4日在巴黎中国文化中心举办。中国歌剧舞剧院演出团当天为150余名法国观众带来了一场中法歌剧艺术的对话。" data-title="“《原野》回响" data-date="09-08 11:31" data-source="中国新闻网">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
      </div>
      <p class="hero-sub-title">“《原野》回响</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/0/999/689.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 8 日消息，《旅行青蛙 · 中国之旅》手游今日发布停运公告，由于 IP 授权合作到期，《旅行青蛙 · 中国之旅》将于 2026 年 12 月 8 日正式停止运营。2026 年 9 月 8 日 14 时：关闭全平台下载入口，玩家将无法下载本游戏，同时停止游戏充值、新用户注册；2026 年 12 月 8 日 18 时：正式停止游戏运营，关闭游戏服务器；游戏官网下架。届时玩家将无法通过游戏服务器登录游戏。在游戏服务器关闭后，各服务器内有关游戏的所有帐号数据及角色资料等信息将被全部清空。注意：游戏服务器关闭后，玩家将无法再次登录游戏，可自行提前保存希望保留的角色信息，以供于后续其他问题需要提供。游戏官方会针对游戏内未消耗的虚拟货币（近 3 月充值获得的三叶草）提供以下退款方案：（一" data-title="《旅行青蛙 · 中国之旅》手游宣布 12 月 8 日停止运营，IP 授权合作到期" data-date="09-08 14:41" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">《旅行青蛙 · 中国之旅》手游宣布 12 月 8 日停止运营，IP 授权合作到期</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-08/10692565.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网呼和浩特9月8日电 (记者 赵永厚 张玮)第十六届中蒙新闻论坛8日在内蒙古自治区呼和浩特市举办，来自中国、蒙古国的百余名媒体记者就深化中蒙两国新闻媒体交流合作、共同讲好中蒙友好故事等重要议题进行讨论和交流经验。" data-title="第十六届中蒙新闻论坛在内蒙古举办" data-date="09-08 14:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 14:26</span>
          <span class="news-item-title">第十六届中蒙新闻论坛在内蒙古举办</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-08/10692536.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月8日电 (记者 张素)记者8日从中国最高人民检察院获悉，检察机关在依法严惩传统黑恶犯罪的基础上，重点依法严厉打击利用网络平台和“软暴力”手段有组织地实施裸聊敲诈、非法放贷、非法催收等涉黑涉恶犯罪及相关犯罪。" data-title="中国检方重点打击利用网络平台和“软暴力”手段实施涉黑涉恶犯罪" data-date="09-08 14:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 14:06</span>
          <span class="news-item-title">中国检方重点打击利用网络平台和“软暴力”手段实施涉黑涉恶犯罪</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-08/10692473.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网马尼拉9月8日电 据菲律宾媒体报道，菲律宾前众议长、总统马科斯的表弟马丁·罗穆亚尔德斯7日因涉嫌从政府防洪项目中收受巨额回扣被执行逮捕令，并被控掠夺罪。" data-title="菲律宾前众议长涉74亿比索防洪项目腐败被捕" data-date="09-08 14:02" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 14:02</span>
          <span class="news-item-title">菲律宾前众议长涉74亿比索防洪项目腐败被捕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-08/10692512.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京9月8日电 中共中央政治局委员、中央统战部部长李干杰8日在京会见由党主席朝格特格日勒率领的蒙古民主党代表团。" data-title="李干杰会见蒙古民主党代表团" data-date="09-08 13:14" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 13:14</span>
          <span class="news-item-title">李干杰会见蒙古民主党代表团</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-08/10692503.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社杭州9月8日电 (钱晨菲)第22届亚洲地区海岸警备机构高官会高级别会议8日在浙江杭州开幕。" data-title="第22届亚洲地区海岸警备机构高官会高级别会议在杭州举行" data-date="09-08 13:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 13:04</span>
          <span class="news-item-title">第22届亚洲地区海岸警备机构高官会高级别会议在杭州举行</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-08/10692497.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网9月8日电 据辽宁省纪委监委消息：辽宁省委社会工作部副部长蔡鸿源涉嫌严重违纪违法，目前正接受辽宁省纪委监委纪律审查和监察调查。" data-title="辽宁省委社会工作部副部长蔡鸿源接受审查调查" data-date="09-08 12:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 12:31</span>
          <span class="news-item-title">辽宁省委社会工作部副部长蔡鸿源接受审查调查</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-08/10692331.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京9月8日电 耶路撒冷消息：当地时间9月7日，以色列国防军发表声明称，以军日前在加沙地带发动两次空袭，分别打死巴勒斯坦伊斯兰抵抗运动(哈马斯)和巴勒斯坦伊斯兰圣战组织(杰哈德)各一名武装人员。" data-title="以军：在加沙地带打死两名巴勒斯坦武装人员" data-date="09-08 11:27" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 11:27</span>
          <span class="news-item-title">以军：在加沙地带打死两名巴勒斯坦武装人员</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/07/us/politics/jefferson-county-trump-transgender-lawsuit.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="科罗拉多州杰斐逊县是少数几个起诉特朗普政府要求其撤销跨性别保护或面临资金削减的公立学校系统之一。" data-title="科罗拉多学区如何对抗特朗普的反" data-date="09-08 01:26" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-08 01:26</span>
          <span class="news-item-title">科罗拉多学区如何对抗特朗普的反</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-08/10692298.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="据也门胡塞武装方面消息，当地时间9月7日，沙特方面战机对也门焦夫省哈兹姆地区发动空袭。" data-title="胡塞武装称沙特战机空袭也门焦夫省哈兹姆地区" data-date="09-08 00:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 00:01</span>
          <span class="news-item-title">胡塞武装称沙特战机空袭也门焦夫省哈兹姆地区</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-07/10692295.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社莫斯科9月7日电 (记者 田冰)俄罗斯外交部7日通报说，针对德国方面关闭俄驻波恩总领事馆和位于柏林的“俄罗斯之家”的行为，俄方采取反制措施，宣布关闭德国驻圣彼得堡总领事馆，并关停德国在俄设立的文化机构歌德学院。" data-title="俄宣布关闭德国驻圣彼得堡总领馆及俄境内歌德学院" data-date="09-07 23:53" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-07 23:53</span>
          <span class="news-item-title">俄宣布关闭德国驻圣彼得堡总领馆及俄境内歌德学院</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-07/10692293.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社曼谷9月7日电 (记者 李映民)泰国旅游和体育部7日公布的数据显示，今年前8个月，泰国共接待外国游客2093.51万人次，同比下降3.08%。其中，中国游客达354.33万人次，同比增长16.05%，继续成为泰国最大的外国游客来源市场。" data-title="泰国前8个月入境客流同比下降超3%" data-date="09-07 23:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-07 23:39</span>
          <span class="news-item-title">泰国前8个月入境客流同比下降超3%</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/06/us/politics/michael-cohen-donald-trump-interview.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="总统已经与他的前律师迈克尔·D·科恩(Michael D. Cohen)和解，后者曾反对他。但与特朗普的说法相反，科恩并没有撤销帮助他的前任老板定罪的证词。" data-title="对于特朗普的前调解人来说，从“老鼠”到和解的痛苦之路" data-date="09-07 23:39" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-07 23:39</span>
          <span class="news-item-title">对于特朗普的前调解人来说，从“老鼠”到和解的痛苦之路</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-07/10692288.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社上海9月7日电 （许婧 娄瀚锟 张亨伟）“走进人民城市：中国之治与全球互鉴”驻华使节沪苏行活动启动仪式7日在上海举行。来自白俄罗斯、西班牙、孟加拉国、塞浦路斯、纳米比亚等20个国家的30位驻华使节及外交官，将赴沪苏两地实地参访，共享城市发展先进理念和成功经验。" data-title="驻华使节沪苏行活动在上海启幕" data-date="09-07 23:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-07 23:36</span>
          <span class="news-item-title">驻华使节沪苏行活动在上海启幕</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-07/10692289.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社昆明9月7日电 (记者 阮煜琳 韩帅南)《昆明—蒙特利尔全球生物多样性框架》(下称“昆蒙框架”)实施进展全球审议昆明对话会7日在云南昆明举行。" data-title="“昆蒙框架”实施进展全球审议昆明对话会举行" data-date="09-07 23:19" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-07 23:19</span>
          <span class="news-item-title">“昆蒙框架”实施进展全球审议昆明对话会举行</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/cddvzm721vpo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="shizheng" data-summary="BBC欧洲事务编辑卡缇雅·阿德勒认为，极右翼在萨克森—安哈尔特州获胜，为欧盟及传统政党敲响了警钟。" data-title="从特朗普到中国，德国极右翼政党州选获胜意义在哪？" data-date="09-07 22:36" data-source="BBC">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-07 22:36</span>
          <span class="news-item-title">从特朗普到中国，德国极右翼政党州选获胜意义在哪？</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/0/999/691.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 8 日消息，小米汽车官方本月初宣布，2026 年 8 月，小米汽车交付量持续超过 30,000 台。小米汽车官方并未公布具体的交付数据，不过在乘联分会今日公布的 2026 年 8 月份全国乘用车市场分析中，IT之家查询到了其具体的零售销量为 30,153 辆。IT之家附小米汽车 2026 年各月交付量（官方口径）：1 月交付量超 39000 台2 月交付量超 20000 台3 月交付量超 20000 台4 月交付量超 30000 台5 月交付量超 30000 台6 月交付量超 30000 台7 月交付量超 30,000 台8 月交付量超 30,000 台另外，小米创办人、董事长兼 CEO 雷军昨日宣布，小米汽车累计交付量超过 80 万辆。" data-title="乘联分会报告披露小米汽车 8 月零售销量 30,153 辆" data-date="09-08 14:42" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-08 14:42</span>
          <span class="news-item-title">乘联分会报告披露小米汽车 8 月零售销量 30,153 辆</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/690.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 8 日消息，据上海市市场监督管理局，淘宝闪购关联公司上海拉扎斯信息科技有限公司于 2026 年 8 月 28 日因“未对其平台内的 51 家入网餐饮服务提供者依法履行资质审查义务”，被上海市市场监督管理局责令改正、罚款 655 万元，相应决定文书号为“沪市监总处 [2026]322026000299 号”。公开信息显示，上海拉扎斯信息科技有限公司公司成立于 2010 年 7 月，法定代表人为方永新，注册资本 1000 万人民币，经营范围包括广告制作、广告发布、针纺织品销售等，由杭州阿里巴巴创业投资管理有限公司全资持股。" data-title="未严格审查商家资质，淘宝闪购关联公司“上海拉扎斯信息科技有限公司”被罚 655 万" data-date="09-08 14:42" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-08 14:42</span>
          <span class="news-item-title">未严格审查商家资质，淘宝闪购关联公司“上海拉扎斯信息科技有限公司”被罚 655 万</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/684.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 8 日消息，消息源 The Cipher Project 昨日（9 月 7 日）在 Telegram 频道爆料，分享了三星 Galaxy A08 手机的渲染图，并称外观沿用 Galaxy A07 设计，屏幕周围边框较厚，屏幕采用水滴屏设计。IT之家此前报道，三星 Galaxy A08 4G 型号为 SM-A085F，将会搭载联发科 Helio G99 芯片，ARM Mali G57 GPU，配备 8GB 运行内存。发布日期方面，三星有望 2026 年 10 月发布 4G 网络版三星 Galaxy A08 手机，明年 2 月发布 5G 版，其中两个版本都可能配备 6000mAh 容量电池。延伸阅读作为三星 A0 系列入门机型，前代 Galaxy A07 4G 于 2025 年" data-title="三星 Galaxy A08 渲染图曝光：联发科 Helio G99 芯片、6000mAh 电池" data-date="09-08 14:39" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-08 14:39</span>
          <span class="news-item-title">三星 Galaxy A08 渲染图曝光：联发科 Helio G99 芯片、6000mAh 电池</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/683.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 8 日消息，阿里今日宣布推出数字员工产品 QoderWake 1.0，用户可用一句话描述岗位需求，然后 QoderWake 可生成一份角色文档。确认后即可生成理解工作职责、协作关系、工作权限等信息的数字员工。据介绍，QoderWake 已内置前端、后端、产品经理、内容运营、数据分析师、项目管理员、UI 设计师等 10 个岗位。每个岗位都经过专岗调试，集成了行业头部团队的经验，无需专门训练就能承接真实任务。用户还可以写清核心职责、工作风格、工作流和红线，并提供核心业务资料，即可自定义数字员工。同时，QoderWake 现已无缝接入钉钉、飞书和企业微信三大主流 IM 软件，了解组织内的文档、表格、待办、日历、组织架构和多维表格，钉钉和飞书群里工作的讨论、附件，以及确认过的口径，" data-title="阿里发布数字员工产品 QoderWake 1.0，已有近 10 万个数字员工“上岗”" data-date="09-08 14:38" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-08 14:38</span>
          <span class="news-item-title">阿里发布数字员工产品 QoderWake 1.0，已有近 10 万个数字员工“上岗”</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/681.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 8 日消息，据长期关注国内手机市场份额的数码博主 @RD观测 爆料，截至 2026 年第 30 周（8 月 24 日-8 月 30 日），华为 Mate 80 系列手机的销量约 897.93 万台。这意味着该系列机型距离千万里程碑又更近了一步。值得一提的是，博主给出的数据并非截止至最新的 9 月 8 日。有网友表示到现在系列机型已突破 900 万台的销量，并预测会在十月突破千万台的销量。华为 Mate 80 / Pro / Pro Max / RS 手机已于 2025 年 11 月 25 日发布，搭载麒麟 9020 / 9030 / 9030 Pro 处理器，首发鸿蒙 Harmony OS 6 系统，定价 4699 元起、涨价后 5499 元起（后增加了一款 Pro Max" data-title="千万里程碑越来越近：曝华为 Mate 80 系列手机销量突破 900 万台" data-date="09-08 14:34" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-08 14:34</span>
          <span class="news-item-title">千万里程碑越来越近：曝华为 Mate 80 系列手机销量突破 900 万台</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/679.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 8 日消息，ASML 今日在 SPIE 前夕宣布了与三大先进制程企业的合作，各方将共同推动 High NA EUV 光刻图案化系统从传统 6 英寸掩膜 / 光罩过渡至 12 英寸掩膜，以提升机台生产效率、降低制造成本，化解当前方案存在的“半场”拼接问题。而在合作新闻稿中，三星电子确认计划在 2028 年将 High NA EUV 技术用于先进 DRAM 内存的大规模生产，台积电则计划从 2031 年开始向先进逻辑制程量产中导入 High NA EUV。各方计划在 2031 年前建设 12 英寸掩膜试点线，为其于 2033 年在 High NA EUV 先进制程中投产做好准备。相关阅读：《High-NA EUV 光刻导致单芯片最大面积减半，imec、英特尔各想办法》" data-title="三星电子、台积电确认分别于 2028、2030 年将 High NA EUV 用于量产" data-date="09-08 14:32" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-08 14:32</span>
          <span class="news-item-title">三星电子、台积电确认分别于 2028、2030 年将 High NA EUV 用于量产</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/0/999/677.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 9 月 8 日消息，在今日的百度 AI 开放日“2026 小度新品发布会”上，小度宣布已进入超 5,500 万家庭。小度宣称专注智能屏，是家庭一老一小的首个 AI 屏。百度集团副总裁、小度科技 CEO 李莹表示，超能小度目前已陪伴超 5,500 万家庭，产品日均语言深度交互量实现近 300% 增长。超能小度中一句话即可完成配置的 AI 随心看护功能表现亮眼，摄像机 AI 功能渗透率达 67%，功能使用留存率高达 94%。在今日的发布会上，搭载超能小度智能体能力的小度添添闺蜜机、小度智能屏、小度智能摄像机等多款硬件新品亮相。IT之家从发布会获悉，超能小度推出家庭事务管理智能体，家长手机端可发送消息、语音、图片、文档等，小度可自动理解信息，并分配家庭事务任务，显示在小度智能屏上，还能主" data-title="百度小度已进入超 5500 万家庭，推出家庭事务管理智能体" data-date="09-08 14:26" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-08 14:26</span>
          <span class="news-item-title">百度小度已进入超 5500 万家庭，推出家庭事务管理智能体</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-08/10692546.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网9月8日电 当地时间9月8日起，加拿大对美国的最新关税反击，正式生效。" data-title="加拿大正式报复美国！民众：不去美国旅行、不买美国科技产品……" data-date="09-08 14:01" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 14:01</span>
          <span class="news-item-title">加拿大正式报复美国！民众：不去美国旅行、不买美国科技产品……</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/semiconductors/intel-surpasses-one-million-high-na-euv-wafers-processed-outpaces-the-rest-of-the-industry-combined-company-also-trailblazing-giant-6-12-photomasks-to-speed-production-and-lower-costs1" target="_blank" rel="noopener" data-cat="keji" data-summary="英特尔凭借高 NA 机群和工艺成熟度里程碑引领半导体行业，使用高 NA 工具处理的晶圆数量达到 100 万片，并在 6×12 光掩模方面取得进展。" data-title="英特尔加工的高数值孔径 EUV 晶圆数量超过 100 万片，超过行业其他公司的总和——该公司还开创性地开发了巨型 6×12 光掩模，以加快生产速度并降低成本" data-date="09-08 14:00" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">09-08 14:00</span>
          <span class="news-item-title">英特尔加工的高数值孔径 EUV 晶圆数量超过 100 万片，超过行业其他公司的总和——该公司还开创性地开发了巨型 6×12 光掩模，以加快生产速度并降低成本</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-08/10692508.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="生成式AI普及之后，写作这件事变得有些微妙。过去人们问“写得好不好”，现在多了一个问题“这到底是不是人写的”？AI检测器正是在这样的需求下，进入了人们的视野。它们分析文字中的语言特征，试图判断文本更像是人写的，还是机器生成的。" data-title="AI坐上文本裁判席，真的靠谱吗" data-date="09-08 13:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 13:08</span>
          <span class="news-item-title">AI坐上文本裁判席，真的靠谱吗</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/485794.html" target="_blank" rel="noopener" data-cat="keji" data-summary="百万奖金、大厂直通、VC跟投" data-title="现场围观金融AI决赛，大厂挑人的逻辑我悟了" data-date="09-08 13:05" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-08 13:05</span>
          <span class="news-item-title">现场围观金融AI决赛，大厂挑人的逻辑我悟了</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-08/10692437.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网悉尼9月8日电 车士活街头嘉年华(Chatswood StreetFair)日前在澳大利亚大悉尼地区威洛比市中心举行。" data-title="悉尼举行车士活街头嘉年华" data-date="09-08 11:32" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 11:32</span>
          <span class="news-item-title">悉尼举行车士活街头嘉年华</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/485784.html" target="_blank" rel="noopener" data-cat="keji" data-summary="近日，物理AI企业深度智控（DeepCtrls）完成新一轮B+轮数亿元融资。" data-title="深度智控获宁德时代、沙特阿美战投等重磅加码，加速打造物理AI时代算力与能源底座" data-date="09-08 11:22" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-08 11:22</span>
          <span class="news-item-title">深度智控获宁德时代、沙特阿美战投等重磅加码，加速打造物理AI时代算力与能源底座</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/485630.html" target="_blank" rel="noopener" data-cat="keji" data-summary="从看市场，到见场景；从认识伙伴，到寻找合作。" data-title="深入马来西亚AI现场！WAIC CONNECT MALAYSIA首日亮点全速递" data-date="09-08 10:42" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-08 10:42</span>
          <span class="news-item-title">深入马来西亚AI现场！WAIC CONNECT MALAYSIA首日亮点全速递</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/09/485555.html" target="_blank" rel="noopener" data-cat="keji" data-summary="把多模型执行经验用到了模型训练" data-title="王云鹤创业后交出首个模型" data-date="09-08 10:14" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">09-08 10:14</span>
          <span class="news-item-title">王云鹤创业后交出首个模型</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">9 条</span>
    </div>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-08/10692381.shtml" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="中新网巴黎9月8日电 “《原野》回响——中法歌剧艺术分享会”当地时间4日在巴黎中国文化中心举办。中国歌剧舞剧院演出团当天为150余名法国观众带来了一场中法歌剧艺术的对话。" data-title="“《原野》回响" data-date="09-08 11:31" data-source="中国新闻网">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 11:31</span>
          <span class="news-item-title">“《原野》回响</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-08/10692367.shtml" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="中新网巴黎9月8日电 法国西南部部分地区气温当地时间7日超过40摄氏度，从而突破9月历史同期高温纪录。" data-title="法国西南部气温超过40摄氏度 突破9月历史同期高温纪录" data-date="09-08 11:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 11:30</span>
          <span class="news-item-title">法国西南部气温超过40摄氏度 突破9月历史同期高温纪录</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-08/10692366.shtml" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="中新网巴黎9月8日电 中国驻法国大使邓励当地时间4日应邀出席第八届吉维尼世界论坛闭幕式，就中欧经贸合作阐述中方立场，介绍中国绿色转型成就。" data-title="中国驻法国大使邓励：中欧经贸相互依赖，应加强对话合作" data-date="09-08 11:28" data-source="中国新闻网">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 11:28</span>
          <span class="news-item-title">中国驻法国大使邓励：中欧经贸相互依赖，应加强对话合作</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cj06m1e3e75o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="全球足球主管埃杜在城市球场工作一年多后离开诺丁汉森林。" data-title="埃杜在经历了动荡之后离开了诺丁汉森林" data-date="09-08 00:45" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-08 00:45</span>
          <span class="news-item-title">埃杜在经历了动荡之后离开了诺丁汉森林</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cgrvx1jxrv0o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="切尔西最近对富勒姆的桑德伯格表现出了兴趣，因为他们试图在恩佐·费尔南德斯离开之前加强中场选择。" data-title="切尔西正在考虑引进富勒姆中场贝尔格" data-date="09-08 00:03" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-08 00:03</span>
          <span class="news-item-title">切尔西正在考虑引进富勒姆中场贝尔格</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c5yw73ppwd1o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="接替理查德·休斯的可能候选人——以及利物浦下一任体育总监面临的众多任务。" data-title="谁将成为新任利物浦体育总监——他们面临哪些问题？" data-date="09-07 23:52" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-07 23:52</span>
          <span class="news-item-title">谁将成为新任利物浦体育总监——他们面临哪些问题？</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/07/arsenals-season-could-hardly-have-started-better" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="现在还为时过早，但Mikel Arteta的球队正在发挥他们上赛季有时无法企及的权威和新鲜感在这里注册我们的免费通讯三场联赛，赢了三场比赛。对于阿森纳来说，本赛季只有在曼城（看起来像是他们两个最严肃的挑战者之一）丢掉积分的情况下才能更好地开始。但这不仅仅是结果：阿森纳在eac中表现得更好" data-title="更健康、更快乐、更有成效：阿森纳开局再好不过了乔纳森·威尔逊" data-date="09-07 22:34" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-07 22:34</span>
          <span class="news-item-title">更健康、更快乐、更有成效：阿森纳开局再好不过了乔纳森·威尔逊</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c0lr4401rw0o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="一个新的摄像机角度显示，诺丁汉森林队后卫内科·威廉姆斯在对阵托特纳姆热刺队的比赛中打入被判无效的进球时，球从他的手臂上滑落。" data-title="新视频显示威廉姆斯手球 - 但不会结束 VAR 争议" data-date="09-07 19:13" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-07 19:13</span>
          <span class="news-item-title">新视频显示威廉姆斯手球 - 但不会结束 VAR 争议</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/07/premier-league-10-talking-points-from-the-weekends-action" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="富勒姆需要一场胜利，托特纳姆展示了一些精神，杰克·格雷利什为埃弗顿提供了急需的能量。在25分钟对阵曼联的比赛中，埃弗顿的支持者们对杰克·格雷利什在重新加入租借后回归有了一些咆哮。这位攻击型中场球员仍然广受欢迎，因为他渴望娱乐，在抵达后几秒钟内制造危险情况，让体验达人重新站起来。Everto" data-title="英超联赛：周末比赛的 10 个话题" data-date="09-07 15:00" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">09-07 15:00</span>
          <span class="news-item-title">英超联赛：周末比赛的 10 个话题</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/0/999/689.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 9 月 8 日消息，《旅行青蛙 · 中国之旅》手游今日发布停运公告，由于 IP 授权合作到期，《旅行青蛙 · 中国之旅》将于 2026 年 12 月 8 日正式停止运营。2026 年 9 月 8 日 14 时：关闭全平台下载入口，玩家将无法下载本游戏，同时停止游戏充值、新用户注册；2026 年 12 月 8 日 18 时：正式停止游戏运营，关闭游戏服务器；游戏官网下架。届时玩家将无法通过游戏服务器登录游戏。在游戏服务器关闭后，各服务器内有关游戏的所有帐号数据及角色资料等信息将被全部清空。注意：游戏服务器关闭后，玩家将无法再次登录游戏，可自行提前保存希望保留的角色信息，以供于后续其他问题需要提供。游戏官方会针对游戏内未消耗的虚拟货币（近 3 月充值获得的三叶草）提供以下退款方案：（一" data-title="《旅行青蛙 · 中国之旅》手游宣布 12 月 8 日停止运营，IP 授权合作到期" data-date="09-08 14:41" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">09-08 14:41</span>
          <span class="news-item-title">《旅行青蛙 · 中国之旅》手游宣布 12 月 8 日停止运营，IP 授权合作到期</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-08/10692567.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="直播海报：“梅姨案”进入审判阶段 申军良父子分享案件心路历程" data-title="直播海报：“梅姨案”进入审判阶段 申军良父子分享案件心路历程" data-date="09-08 14:36" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 14:36</span>
          <span class="news-item-title">直播海报：“梅姨案”进入审判阶段 申军良父子分享案件心路历程</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c87v33gxr01o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="专家称，航母给美国盟友的是心理保证。印太区域没有航母，“会加强一种整体感觉：美国正被中东局势分心。”" data-title="美军航母全数撤离印太：台湾该担心“空窗期”吗？" data-date="09-08 14:35" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-08 14:35</span>
          <span class="news-item-title">美军航母全数撤离印太：台湾该担心“空窗期”吗？</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-08/10692566.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="打着“助农”的旗号，却专门骗取种植户的保证金——安徽警方近日侦破一起新型涉农诈骗案，全国各地数百家农户上当受骗，涉案金额超过800万元。" data-title="打着“助农”旗号设局 警方破获新型涉农诈骗案" data-date="09-08 14:33" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 14:33</span>
          <span class="news-item-title">打着“助农”旗号设局 警方破获新型涉农诈骗案</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cly4lngg6npo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="纽卡斯尔联队体育总监罗斯·威尔逊表示，俱乐部正在为前主教练埃迪·豪的离职做长达九个月的准备。" data-title="纽卡斯尔为豪的离开“准备了几个月”" data-date="09-08 14:21" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-08 14:21</span>
          <span class="news-item-title">纽卡斯尔为豪的离开“准备了几个月”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-08/10692528.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网9月8日电 据中央气象台网站消息，海南省白沙县气象台9月8日13时43分发布雷电黄色预警信号：受对流云团影响，我县牙叉镇、七坊镇、打安镇、元门乡、南开乡、青松乡、金波乡8日13时43分到19时可能发生雷电活动，可能会出现雷电灾害事故，建议有关单位和人员做好防范工作。" data-title="海南省白沙县气象台发布雷电黄色预警信号" data-date="09-08 14:04" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 14:04</span>
          <span class="news-item-title">海南省白沙县气象台发布雷电黄色预警信号</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-08/10692540.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="新华社南昌9月8日电 记者从江西遂川高坪镇明坑村泥石流灾害救援现场获悉，截至8日13时，5日凌晨发生的泥石流灾害现场已经发现5具遇难者遗体，仍有7人失联。" data-title="江西遂川高坪镇泥石流已致5人遇难" data-date="09-08 13:50" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 13:50</span>
          <span class="news-item-title">江西遂川高坪镇泥石流已致5人遇难</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-08/10692500.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新社四川若尔盖9月8日电 题：四川若尔盖湿地蜕变：从“长征绝境”到“鹤鸣天堂”" data-title="（长征胜利90周年）四川若尔盖湿地蜕变：从“长征绝境”到“鹤鸣天堂”" data-date="09-08 12:44" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 12:44</span>
          <span class="news-item-title">（长征胜利90周年）四川若尔盖湿地蜕变：从“长征绝境”到“鹤鸣天堂”</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/09-08/10692496.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="9月5日凌晨4时许，江西遂川县高坪镇明坑村石下组发生泥石流灾害。截至8日上午11时，现场又找到1名失联人员，没有生命体征。救援力量正紧急搜救剩下的7名失联人员。" data-title="江西遂川高坪镇泥石流现场又找到1名失联人员 已无生命体征" data-date="09-08 12:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 12:20</span>
          <span class="news-item-title">江西遂川高坪镇泥石流现场又找到1名失联人员 已无生命体征</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-08/10692483.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="随着开渔季的到来" data-title="鲜活的螃蟹能带上高铁吗？官方解答来了！" data-date="09-08 11:42" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 11:42</span>
          <span class="news-item-title">鲜活的螃蟹能带上高铁吗？官方解答来了！</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c5ym2zy4r77o/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="姆拉迪奇因在 20 世纪 90 年代波斯尼亚战争期间犯下种族灭绝罪而被监禁，欧盟警告塞尔维亚不要美化这名被定罪的战争罪犯。" data-title="定罪战犯“波斯尼亚屠夫”姆拉迪奇去世 塞尔维亚数千人送殡" data-date="09-08 11:26" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">09-08 11:26</span>
          <span class="news-item-title">定罪战犯“波斯尼亚屠夫”姆拉迪奇去世 塞尔维亚数千人送殡</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/09-08/10692456.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="8月26日，尼泊尔境内一起冰岩崩塌灾害引发的恐怖泥石流，席卷了两国边境，给两国人民造成重大伤亡。其中，中方一侧吉隆口岸甚至在灾害发生短短7分多钟就被泥石流夷为平地。" data-title="这个污蔑中国的恶毒谣言，被粉碎！" data-date="09-08 11:17" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 11:17</span>
          <span class="news-item-title">这个污蔑中国的恶毒谣言，被粉碎！</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-08/10692446.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="为什么中国能建成超级水网？50年前，8万人，已给过答案。#洞见·求索#寻找引松人#引松工程50周年#好好学习" data-title="一条53.85公里的渠，背后是多大一张网？" data-date="09-08 11:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 11:06</span>
          <span class="news-item-title">一条53.85公里的渠，背后是多大一张网？</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/09-08/10692438.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="近日，国家版权局印发《版权工作“十五五”规划》(以下简称《规划》)，明确了“十五五”时期版权工作的指导思想、主要目标、重点任务和专项工程。" data-title="建设激励创新的版权保护生态 未来五年版权工作这样开展" data-date="09-08 10:56" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">09-08 10:56</span>
          <span class="news-item-title">建设激励创新的版权保护生态 未来五年版权工作这样开展</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/09/07/us/miami-crash-emas-buffer-runways.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="一项涉及可压碎混凝土的技术帮助阻止了超出着陆范围的飞机，从而挽救了近 500 名乘客的生命。" data-title="迈阿密飞机失事引发关于是否需要跑道缓冲区的争论" data-date="09-08 10:48" data-source="纽约时报">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">09-08 10:48</span>
          <span class="news-item-title">迈阿密飞机失事引发关于是否需要跑道缓冲区的争论</span>
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

<p class="news-updated">🕐 抓取更新于 2026-09-08 14:38（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
