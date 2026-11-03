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
      <span>2026-11-03 16:43 抓取更新</span>
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
  <div class="ov-item"><span class="ov-num" style="font-size:13px;line-height:1.5">中国新闻网×21 · 天空体育×11</span><span class="ov-label">TOP 信源</span></div>
  <div class="ov-note">信源交叉印证 · 数据每 3~8 小时自动聚合更新</div>
</div>
<div class="news-hero">
  <div class="news-hero-badge">🔥 今日头条焦点</div>
  <a class="hero-featured-card" href="https://www.chinanews.com.cn/gn/2026/11-03/10725410.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="人大常委会丨报告显示知识产权检察工作专业化水平有效提升" data-title="报告显示知识产权检察工作专业化水平有效提升" data-date="11-03 16:39" data-source="中国新闻网">
    <div class="hero-featured-body">
      <div class="hero-featured-meta">
        <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
        <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
        <span class="hero-featured-date">🕒 11-03 16:39</span>
      </div>
      <h2 class="hero-featured-title">报告显示知识产权检察工作专业化水平有效提升</h2>
    </div>
    <span class="hero-featured-arrow">→</span>
  </a>
  <div class="hero-sub-grid">
    <a class="hero-sub-card" href="https://www.ithome.com/1/021/640.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 3 日消息，Panasonic Industry（松下电器机电）日本当地时间 10 月 30 日宣布向人工智能相关业务投资 920 亿日元（IT之家注：现汇率约合 38.81 亿元人民币）。在 MEGTRON 多层基板材料方面，除分别将于 2026 年 12 月、2027 年 11 月投运的两座工厂外，松下电器机电还将在中国苏州、泰国大城府各建设一座新工厂，投资额分别达到 300 亿和 370 亿日元，预计 2028 年 8 月、2029 年 4 月投运。在 SP-Cap 导电性聚合物片式铝电解电容器方面，松下电器机电计划在日本京都宇治工厂和印度尼西亚峇淡工厂合计投资约 170 亿日元，以满足 GPU 等 AI 服务器元件对该类型电容器日益增长的中长期需求。此外，松下电器" data-title="松下电器机电向 AI 相关领域投资 920 亿日元，提升电路板材料、电解电容器产能" data-date="11-03 16:42" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">松下电器机电向 AI 相关领域投资 920 亿日元，提升电路板材料、电解电容器产能</p>
    </a>
    <a class="hero-sub-card" href="https://www.skysports.com/f1/news/12040/13607194/george-russell-must-find-overdrive-in-2027-or-its-game-over-after-seeing-kimi-antonelli-become-f1-world-champion-says-martin-brundle" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育F1的马丁·布伦德尔（ Martin Brundle ）认为，乔治·拉塞尔（ George Russell ）必须找到一个“超速”来回击今年F1车手锦标赛输给基米·安东内利（ Kimi Antonelli" data-title="Brundle: Russell must find &#39;overdrive&#39; in 2027 or it&#39;s &#39;game over&#39;" data-date="11-03 15:00" data-source="天空体育">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
        <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
      </div>
      <p class="hero-sub-title">Brundle: Russell must find 'overdrive' in 2027 or it's 'game over'</p>
    </a>
    <a class="hero-sub-card" href="https://www.ithome.com/1/021/638.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 3 日消息，索尼 SIE 昨天为 PS5 游戏机推送了系统更新 26.07-14.22.00，大小约 1.26GB，本次更新主要对漏洞进行修复，并未有其他功能调整或性能优化。参考 PlayStation Size，《GTA 6》游戏现已要求 PS5 搭载 14.22.00 系统固件才能运行，未来利用旧版系统运行自制软件的用户可能无法在第一时间玩上《GTA 6》。《GTA 6》目前计划于 11 月 19 日发售，距离正式上市仍有一段时间，因此最终零售版对 PS5 系统版本的具体要求后续仍可能发生变化。" data-title="索尼为 PS5 推送 26.07-14.22.00 系统更新，想玩《GTA 6》就得为游戏机更新最新固件" data-date="11-03 16:37" data-source="IT之家">
      <div class="hero-sub-meta">
        <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
        <span class="source-badge source-cn">🇨🇳 IT之家</span>
      </div>
      <p class="hero-sub-title">索尼为 PS5 推送 26.07-14.22.00 系统更新，想玩《GTA 6》就得为游戏机更新最新固件</p>
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
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-03/10725410.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="人大常委会丨报告显示知识产权检察工作专业化水平有效提升" data-title="报告显示知识产权检察工作专业化水平有效提升" data-date="11-03 16:39" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-03 16:39</span>
          <span class="news-item-title">报告显示知识产权检察工作专业化水平有效提升</span>
          <span class="news-value-point">💡 人大常委会丨报告显示知识产权检察工作专业化水平有效提升</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-03/10725404.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="记者今天了解到，我国牵头修订的放射性废物管理国际标准《考虑作为非放射性废物回收、再利用或处置的固体材料的活度测量》发布，为全球放射性污染物料精准分类管理提供了通用技术准则。该国际标准由我国专家担任项目负责人，美国、法国、日本、英国等国专家参与。" data-title="我国牵头修订的放射性废物管理国际标准发布" data-date="11-03 16:35" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-03 16:35</span>
          <span class="news-item-title">我国牵头修订的放射性废物管理国际标准发布</span>
          <span class="news-value-point">💡 记者今天了解到，我国牵头修订的放射性废物管理国际标准《考虑作为非放射性废物回收、再利用或处置的固体材料的活度测量》发布，为全球放射性污染物料精准…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-03/10725385.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社杭州11月3日电" data-title="李强在2026年世界互联网大会乌镇峰会开幕式上的主旨演讲（全文）" data-date="11-03 16:29" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-03 16:29</span>
          <span class="news-item-title">李强在2026年世界互联网大会乌镇峰会开幕式上的主旨演讲（全文）</span>
          <span class="news-value-point">💡 新华社杭州11月3日电</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-03/10725386.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="乌镇“网事”绘就数字生活新图景" data-title="乌镇“网事”绘就数字生活新图景" data-date="11-03 16:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-03 16:26</span>
          <span class="news-item-title">乌镇“网事”绘就数字生活新图景</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-03/10725382.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社北京11月3日电" data-title="刘延东同志生平" data-date="11-03 16:22" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-03 16:22</span>
          <span class="news-item-title">刘延东同志生平</span>
          <span class="news-value-point">💡 新华社北京11月3日电</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-03/10725380.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月3日电 据最高人民检察院微信公众号消息，检察机关依法分别对韩玉明、白立柱、鲍长山、李国锋、魏学林提起公诉。" data-title="检察机关依法分别对韩玉明、白立柱、鲍长山、李国锋、魏学林提起公诉" data-date="11-03 16:21" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-03 16:21</span>
          <span class="news-item-title">检察机关依法分别对韩玉明、白立柱、鲍长山、李国锋、魏学林提起公诉</span>
          <span class="news-value-point">💡 中新网11月3日电 据最高人民检察院微信公众号消息，检察机关依法分别对韩玉明、白立柱、鲍长山、李国锋、魏学林提起公诉</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-03/10725381.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="焦点访谈｜生物多样性首次全球审查 中国交出亮眼答卷" data-title="生物多样性首次全球审查 中国交出亮眼答卷" data-date="11-03 16:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-03 16:20</span>
          <span class="news-item-title">生物多样性首次全球审查 中国交出亮眼答卷</span>
          <span class="news-value-point">💡 焦点访谈｜生物多样性首次全球审查 中国交出亮眼答卷</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gn/2026/11-03/10725375.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月3日电 据黑龙江省纪委监委消息：日前，经黑龙江省委批准，黑龙江省纪委监委对黑龙江省公安厅原二级警务专员史衍芳严重违纪违法问题进行了立案审查调查。" data-title="黑龙江省公安厅原二级警务专员史衍芳被开除党籍" data-date="11-03 16:20" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-03 16:20</span>
          <span class="news-item-title">黑龙江省公安厅原二级警务专员史衍芳被开除党籍</span>
          <span class="news-value-point">💡 中新网11月3日电 据黑龙江省纪委监委消息：日前，经黑龙江省委批准，黑龙江省纪委监委对黑龙江省公安厅原二级警务专员史衍芳严重违纪违法问题进行了立…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-03/10725367.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月3日电 综合多家伊朗媒体2日报道，德黑兰大区伊斯兰革命卫队司令哈桑扎德说，伊朗首支“为伊朗捐躯”旅已完成组建。" data-title="伊朗：首支“为伊朗捐躯”旅完成组建" data-date="11-03 16:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-03 16:06</span>
          <span class="news-item-title">伊朗：首支“为伊朗捐躯”旅完成组建</span>
          <span class="news-value-point">💡 中新网11月3日电 综合多家伊朗媒体2日报道，德黑兰大区伊斯兰革命卫队司令哈桑扎德说，伊朗首支“为伊朗捐躯”旅已完成组建</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-03/10725361.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="新华社平壤11月3日电(记者王天僚)据朝中社3日报道，朝鲜军事评论员当天发表文章说，日本撕去“和平国家”的外衣，正在快速变成战争国家。其冒险谋求先发制人打击能力的举动，进一步加剧地区紧张局势。" data-title="朝中社：日本正快速变为战争国家" data-date="11-03 15:46" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-03 15:46</span>
          <span class="news-item-title">朝中社：日本正快速变为战争国家</span>
          <span class="news-value-point">💡 新华社平壤11月3日电(记者王天僚)据朝中社3日报道，朝鲜军事评论员当天发表文章说，日本撕去“和平国家”的外衣，正在快速变成战争国家</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-03/10725335.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网11月3日电 综合韩联社报道，韩国总统李在明夫妇、国务委员、总统府青瓦台工作人员等人的个人信息一度在网上遭大规模泄露，引发争议。" data-title="韩总统李在明等168人信息遭大规模泄露 韩政府回应" data-date="11-03 15:26" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-03 15:26</span>
          <span class="news-item-title">韩总统李在明等168人信息遭大规模泄露 韩政府回应</span>
          <span class="news-value-point">💡 中新网11月3日电 综合韩联社报道，韩国总统李在明夫妇、国务委员、总统府青瓦台工作人员等人的个人信息一度在网上遭大规模泄露，引发争议</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-03/10725259.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社华盛顿11月2日电 (记者 陈孟统)在美国2026年中期选举日前一天，美国总统特朗普在华盛顿发表讲话，为其过去一个月密集的助选造势活动“收官”。" data-title="特朗普发表讲话  为中期选举造势“收官”" data-date="11-03 13:07" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-03 13:07</span>
          <span class="news-item-title">特朗普发表讲话  为中期选举造势“收官”</span>
          <span class="news-value-point">💡 中新社华盛顿11月2日电 (记者 陈孟统)在美国2026年中期选举日前一天，美国总统特朗普在华盛顿发表讲话，为其过去一个月密集的助选造势活动“收…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-03/10725236.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新社北京11月3日电 平壤消息：当地时间11月3日，据朝鲜中央通讯社(朝中社)报道，朝鲜劳动党中央委员会部长金与正2日发表谈话称，美国联邦调查局声称所谓朝鲜“支援”的黑客组织参与加密货币交易平台“币安”数十亿美元加密货币盗窃事件，企图诋毁朝鲜为“网络犯罪国家”。" data-title="朝鲜驳斥美国加密货币盗窃指控" data-date="11-03 12:08" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-03 12:08</span>
          <span class="news-item-title">朝鲜驳斥美国加密货币盗窃指控</span>
          <span class="news-value-point">💡 中新社北京11月3日电 平壤消息：当地时间11月3日，据朝鲜中央通讯社(朝中社)报道，朝鲜劳动党中央委员会部长金与正2日发表谈话称，美国联邦调查…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/gj/2026/11-03/10725245.shtml" target="_blank" rel="noopener" data-cat="shizheng" data-summary="中新网伦敦11月3日电 (记者 欧阳开宇)当地时间11月2日晚，由文化和旅游部国际交流与合作局指导，中国驻伦敦旅游办事处、中外文化和旅游交流中心联合主办的中国之夜——”你好！中国”冰雪旅游专题推广活动在伦敦举行。" data-title="中国之夜 ——“你好！中国”冰雪旅游专题推广活动在伦敦举行" data-date="11-03 12:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-03 12:06</span>
          <span class="news-item-title">中国之夜 ——“你好！中国”冰雪旅游专题推广活动在伦敦举行</span>
          <span class="news-value-point">💡 中新网伦敦11月3日电 (记者 欧阳开宇)当地时间11月2日晚，由文化和旅游部国际交流与合作局指导，中国驻伦敦旅游办事处、中外文化和旅游交流中心…</span>
        </a>
        <a class="news-item" href="https://www.nytimes.com/2026/11/02/us/politics/midterms-2020-election-justice-department.html" target="_blank" rel="noopener" data-cat="shizheng" data-summary="美国国务院高级官员拒绝承认唐纳德· J ·特朗普(Donald J. Trump)当年的失败，这推动了加大干预国家选举管理的力度。" data-title="In Run-Up to Midterms, Legacy of 2020 Looms Large Over Justice Dept." data-date="11-03 11:36" data-source="纽约时报">
          <span class="news-cat-tag cat-shizheng">🏛️ 时政要闻</span>
          <span class="source-badge source-nytimes">🇺🇸 纽约时报</span>
          <span class="news-item-date">11-03 11:36</span>
          <span class="news-item-title">在即将到来的中期选举中， 2020年的遗产笼罩在司法部之上</span>
          <span class="news-item-title-en">In Run-Up to Midterms, Legacy of 2020 Looms Large Over Justice Dept.</span>
          <span class="news-value-point">💡 美国国务院高级官员拒绝承认唐纳德· J ·特朗普(Donald J. Trump)当年的失败，这推动了加大干预国家选举管理的力度</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">🤖</span>
      <span class="news-category-title">前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/021/640.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 3 日消息，Panasonic Industry（松下电器机电）日本当地时间 10 月 30 日宣布向人工智能相关业务投资 920 亿日元（IT之家注：现汇率约合 38.81 亿元人民币）。在 MEGTRON 多层基板材料方面，除分别将于 2026 年 12 月、2027 年 11 月投运的两座工厂外，松下电器机电还将在中国苏州、泰国大城府各建设一座新工厂，投资额分别达到 300 亿和 370 亿日元，预计 2028 年 8 月、2029 年 4 月投运。在 SP-Cap 导电性聚合物片式铝电解电容器方面，松下电器机电计划在日本京都宇治工厂和印度尼西亚峇淡工厂合计投资约 170 亿日元，以满足 GPU 等 AI 服务器元件对该类型电容器日益增长的中长期需求。此外，松下电器" data-title="松下电器机电向 AI 相关领域投资 920 亿日元，提升电路板材料、电解电容器产能" data-date="11-03 16:42" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-03 16:42</span>
          <span class="news-item-title">松下电器机电向 AI 相关领域投资 920 亿日元，提升电路板材料、电解电容器产能</span>
          <span class="news-value-point">💡 IT之家 11 月 3 日消息，Panasonic Industry（松下电器机电）日本当地时间 10 月 30 日宣布向人工智能相关业务投资 …</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/021/636.htm" target="_blank" rel="noopener" data-cat="keji" data-summary="IT之家 11 月 3 日消息，据彭博社报道，迈威尔科技（Marvell Technology Inc.）与 Lumentum 控股公司的负责人在敲定这笔近 1,030 亿美元（IT之家注：现汇率约合 6,865.35 亿元人民币）的合并交易前，已经获得英伟达公司 CEO 黄仁勋（Jensen Huang）的支持。据知情人士透露，相关细节尚未对外公开，迈威尔首席执行官马修 · 墨菲（Matthew Murphy）与 Lumentum 首席执行官迈克尔 · 赫尔斯顿（Michael Hurlston）在交易官宣前，曾致电征求黄仁勋的意见。黄仁勋对此表示支持，这件事也体现出，在建设规模持续扩大的数据中心时，高速光互联需求已经成为瓶颈，AI 龙头英伟达正推动核心供应商之间进行行业整合。英伟达是大语" data-title="Marvell 千亿美元吞下 Lumentum，获英伟达黄仁勋点头支持" data-date="11-03 16:34" data-source="IT之家">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-03 16:34</span>
          <span class="news-item-title">Marvell 千亿美元吞下 Lumentum，获英伟达黄仁勋点头支持</span>
          <span class="news-value-point">💡 IT之家 11 月 3 日消息，据彭博社报道，迈威尔科技（Marvell Technology Inc.）与 Lumentum 控股公司的负责人…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-03/10725303.shtml" target="_blank" rel="noopener" data-cat="keji" data-summary="中新网上海11月3日电 (记者 郑莹莹)2026长三角“科普星人充电站”活动3日在上海科技馆启动。本次活动为期3天，旨在探索AI时代科普场馆的创作新方式。上海科技馆自主研发的科普创作平台“科普星人·Agent”在活动上首发。" data-title="2026长三角“科普星人充电站”活动在沪启动 首发科普创作智能体" data-date="11-03 15:05" data-source="中国新闻网">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-03 15:05</span>
          <span class="news-item-title">2026长三角“科普星人充电站”活动在沪启动 首发科普创作智能体</span>
          <span class="news-value-point">💡 中新网上海11月3日电 (记者 郑莹莹)2026长三角“科普星人充电站”活动3日在上海科技馆启动</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/507419.html" target="_blank" rel="noopener" data-cat="keji" data-summary="终于，有了一个可以触摸的起点" data-title="纯语音Personal Agent来了！或许，这就是乔布斯心中的Siri" data-date="11-03 14:55" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-03 14:55</span>
          <span class="news-item-title">纯语音Personal Agent来了！或许，这就是乔布斯心中的Siri</span>
          <span class="news-value-point">💡 终于，有了一个可以触摸的起点</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/507396.html" target="_blank" rel="noopener" data-cat="keji" data-summary="11月3日，小米方面披露，小米集团获得2026世界互联网大会“杰出贡献奖”创新突破类奖项" data-title="小米斩获乌镇峰会双料大奖：小米集团获“杰出贡献奖”，小米具身基座模型获“领先科技奖”" data-date="11-03 13:16" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-03 13:16</span>
          <span class="news-item-title">小米斩获乌镇峰会双料大奖：小米集团获“杰出贡献奖”，小米具身基座模型获“领先科技奖”</span>
          <span class="news-value-point">💡 11月3日，小米方面披露，小米集团获得2026世界互联网大会“杰出贡献奖”创新突破类奖项</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/02/google-takes-dreambeans-to-india-in-bid-to-bring-ai-generated-personal-stories-to-the-masses/" target="_blank" rel="noopener" data-cat="keji" data-summary="谷歌最新的人工智能实验Dreambeans现在支持13种印度语言。" data-title="Google takes Dreambeans to India in bid to bring AI-generated personal stories to the masses" data-date="11-03 11:30" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-03 11:30</span>
          <span class="news-item-title">谷歌将Dreambeans带到印度，将AI生成的个人故事带给大众</span>
          <span class="news-item-title-en">Google takes Dreambeans to India in bid to bring AI-generated personal stories to the masses</span>
          <span class="news-value-point">💡 谷歌最新的人工智能实验Dreambeans现在支持13种印度语言</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/507367.html" target="_blank" rel="noopener" data-cat="keji" data-summary="GPU迭代一百次的事，它一步做完" data-title="模拟计算进入矩阵时代！北大联手硅谷IBM，写下新定义" data-date="11-03 11:16" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-03 11:16</span>
          <span class="news-item-title">模拟计算进入矩阵时代！北大联手硅谷IBM，写下新定义</span>
          <span class="news-value-point">💡 GPU迭代一百次的事，它一步做完</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/507322.html" target="_blank" rel="noopener" data-cat="keji" data-summary="指令执行能力也同步提升" data-title="MIT：GPT-6 Astra能直接修改Qwen权重，数学能力暴涨6倍" data-date="11-03 09:57" data-source="量子位">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-03 09:57</span>
          <span class="news-item-title">MIT：GPT-6 Astra能直接修改Qwen权重，数学能力暴涨6倍</span>
          <span class="news-value-point">💡 指令执行能力也同步提升</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/02/y-combinators-garry-tan-uses-ai-agents-so-much-he-spends-up-to-200k-a-year-on-tokens/" target="_blank" rel="noopener" data-cat="keji" data-summary="Y Combinator的Garry Tan开玩笑地承认他患有“网络精神病” ，有时几乎不睡觉，因为他对与人工智能特工合作感到非常兴奋。在沃尔特·艾萨克森（ Walter Isaacson ）播客的新一集《建造者》（ The Builders ）中，谭恩美给了" data-title="Y Combinator’s Garry Tan uses AI agents so much, he spends up to $200K a year on tokens" data-date="11-03 08:35" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-03 08:35</span>
          <span class="news-item-title">Y Combinator的Garry Tan使用人工智能代理太多，他每年在代币上花费高达20万美元$</span>
          <span class="news-item-title-en">Y Combinator’s Garry Tan uses AI agents so much, he spends up to $200K a year on tokens</span>
          <span class="news-value-point">💡 Y Combinator的Garry Tan开玩笑地承认他患有“网络精神病” ，有时几乎不睡觉，因为他对与人工智能特工合作感到非常兴奋</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/02/trajectory-raises-45m-to-make-ai-model-training-accessible-to-nontechnical-experts/" target="_blank" rel="noopener" data-cat="keji" data-summary="这家成立一年的初创公司现在的估值为3亿美元。" data-title="Trajectory raises $45M to make AI model training accessible to nontechnical experts" data-date="11-03 07:13" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-03 07:13</span>
          <span class="news-item-title">Trajectory筹集了$ 4500万，使非技术专家能够获得人工智能模型培训</span>
          <span class="news-item-title-en">Trajectory raises $45M to make AI model training accessible to nontechnical experts</span>
          <span class="news-value-point">💡 这家成立一年的初创公司现在的估值为3亿美元</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/02/anthropic-warns-that-its-very-close-to-rsi-capability-aka-self-building-ai/" target="_blank" rel="noopener" data-cat="keji" data-summary="RSI是人工智能发展得如此擅长训练自己的时刻，以至于它催生了人工智能能力的急剧加速。对人工智能的毁灭者来说， RSI代表着一场没有回报的灾难。" data-title="Anthropic warns that it’s very close to RSI capability, aka self" data-date="11-03 06:14" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-03 06:14</span>
          <span class="news-item-title">Anthropic警告说，它非常接近RSI能力，也就是自我</span>
          <span class="news-item-title-en">Anthropic warns that it’s very close to RSI capability, aka self</span>
          <span class="news-value-point">💡 RSI是人工智能发展得如此擅长训练自己的时刻，以至于它催生了人工智能能力的急剧加速</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/02/new-york-times-and-other-outlets-sue-web-browser-brave-over-alleged-content-scraping/" target="_blank" rel="noopener" data-cat="keji" data-summary="《纽约时报》起诉以隐私为中心的网络浏览器公司Brave ，指控其抓取该网站受版权保护的内容，并将其非法分发给自己的客户，如Anthropic和Perplexity。" data-title="New York Times and other outlets sue web browser Brave over alleged content scraping" data-date="11-03 03:19" data-source="TechCrunch">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-03 03:19</span>
          <span class="news-item-title">《纽约时报》和其他媒体起诉网络浏览器Brave涉嫌内容抓取</span>
          <span class="news-item-title-en">New York Times and other outlets sue web browser Brave over alleged content scraping</span>
          <span class="news-value-point">💡 《纽约时报》起诉以隐私为中心的网络浏览器公司Brave ，指控其抓取该网站受版权保护的内容，并将其非法分发给自己的客户，如Anthropic和P…</span>
        </a>
        <a class="news-item" href="https://www.tomshardware.com/tech-industry/data-centers/openai-considers-rebranding-data-centers-to-ai-compute-campuses-as-data-center-backlash-intensifies-company-reportedly-sees-2028-presidential-election-becoming-an-ai-issue" target="_blank" rel="noopener" data-cat="keji" data-summary="OpenAI预计人工智能将成为2028年总统大选的一个主要问题，并正在准备在美国中期选举后推动政策和公共关系。该公司还在其数据中心推广“人工智能计算园区”一词，因为它" data-title="OpenAI considers rebranding data centers to &#39;AI compute campuses&quot; as data center backlash intensifies" data-date="11-03 03:15" data-source="Tom's Hardware">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-tomshardware">⚡ Tom's Hardware</span>
          <span class="news-item-date">11-03 03:15</span>
          <span class="news-item-title">OpenAI考虑将数据中心重塑为“AI计算园区” ，因为数据中心的反弹加剧</span>
          <span class="news-item-title-en">OpenAI considers rebranding data centers to 'AI compute campuses" as data center backlash intensifies</span>
          <span class="news-value-point">💡 OpenAI预计人工智能将成为2028年总统大选的一个主要问题，并正在准备在美国中期选举后推动政策和公共关系</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1024632/anthropic-claude-ai-video-game-clones" target="_blank" rel="noopener" data-cat="keji" data-summary="据Tom&#39;s Hardware报道， Anthropic已更新Claude Code的系统提示，以防止人工智能工具被用于重新创建现有视频游戏。复古游戏目前正被人工智能制作的反编译、重新编译和端口所淹没，" data-title="Anthropic clamps down on Claude’s AI video game clones" data-date="11-03 02:56" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-03 02:56</span>
          <span class="news-item-title">Anthropic压制Claude的人工智能视频游戏克隆</span>
          <span class="news-item-title-en">Anthropic clamps down on Claude’s AI video game clones</span>
          <span class="news-value-point">💡 据Tom's Hardware报道， Anthropic已更新Claude Code的系统提示，以防止人工智能工具被用于重新创建现有视频游戏</span>
        </a>
        <a class="news-item" href="https://www.theverge.com/ai-artificial-intelligence/1024604/openai-data-center-grid-protection-program" target="_blank" rel="noopener" data-cat="keji" data-summary="在周一的公告中， OpenAI表示将在佐治亚州埃芬汉县即将到来的数据中心试点其“电网保护器计划” ，该公司承诺在极端天气或紧急情况下释放高达1,000兆瓦的电力，" data-title="OpenAI pitches data center power plants as a way to protect nearby areas" data-date="11-03 02:01" data-source="The Verge">
          <span class="news-cat-tag cat-keji">🤖 AI & 芯片前沿</span>
          <span class="source-badge source-theverge">🌐 The Verge</span>
          <span class="news-item-date">11-03 02:01</span>
          <span class="news-item-title">OpenAI将数据中心发电厂作为保护附近地区的一种方式</span>
          <span class="news-item-title-en">OpenAI pitches data center power plants as a way to protect nearby areas</span>
          <span class="news-value-point">💡 在周一的公告中， OpenAI表示将在佐治亚州埃芬汉县即将到来的数据中心试点其“电网保护器计划” ，该公司承诺在极端天气或紧急情况下释放高达1,…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">⚽</span>
      <span class="news-category-title">英超与足球风云 (赛况战术 · 转会焦点)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.skysports.com/f1/news/12040/13607194/george-russell-must-find-overdrive-in-2027-or-its-game-over-after-seeing-kimi-antonelli-become-f1-world-champion-says-martin-brundle" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育F1的马丁·布伦德尔（ Martin Brundle ）认为，乔治·拉塞尔（ George Russell ）必须找到一个“超速”来回击今年F1车手锦标赛输给基米·安东内利（ Kimi Antonelli" data-title="Brundle: Russell must find &#39;overdrive&#39; in 2027 or it&#39;s &#39;game over&#39;" data-date="11-03 15:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-03 15:00</span>
          <span class="news-item-title">布伦德尔：罗素必须在2027年找到“超速驾驶” ，否则就是“游戏结束”</span>
          <span class="news-item-title-en">Brundle: Russell must find 'overdrive' in 2027 or it's 'game over'</span>
          <span class="news-value-point">💡 天空体育F1的马丁·布伦德尔（ Martin Brundle ）认为，乔治·拉塞尔（ George Russell ）必须找到一个“超速”来回击…</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/c8dx37n11kv2o?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="在本赛季英超联赛的每一轮比赛之后，特洛伊·迪尼（ Troy Deeney ）都给了我们本周最佳球队。你同意他的选择吗？" data-title="Who has made Troy&#39;s Premier League team of the week?" data-date="11-03 07:09" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-03 07:09</span>
          <span class="news-item-title">谁入选了特洛伊本周的英超联赛球队？</span>
          <span class="news-item-title-en">Who has made Troy's Premier League team of the week?</span>
          <span class="news-value-point">💡 在本赛季英超联赛的每一轮比赛之后，特洛伊·迪尼（ Troy Deeney ）都给了我们本周最佳球队</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/news/12040/13607310/bournemouth-forward-junior-kroupi-and-juventus-winger-kenan-yildiz-both-in-arsenal-boss-mikel-artetas-sights-ahead-of-january-window-paper-talk" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="周二报纸的热门报道和转移谣言……" data-title="Papers: Kroupi and Yildiz on Arsenal&#39;s radar ahead of January window" data-date="11-03 06:48" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-03 06:48</span>
          <span class="news-item-title">论文： 1月窗口前阿森纳雷达上的Kroupi和Yildiz</span>
          <span class="news-item-title-en">Papers: Kroupi and Yildiz on Arsenal's radar ahead of January window</span>
          <span class="news-value-point">💡 周二报纸的热门报道和转移谣言……</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/watch/video/13607313/newcastle-0-1-everton-premier-league-highlights" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="纽卡斯尔和埃弗顿之间英超比赛的亮点。" data-title="Barry goal sees Everton ease past dreadful Newcastle" data-date="11-03 06:18" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-03 06:18</span>
          <span class="news-item-title">巴里进球让埃弗顿轻松度过可怕的纽卡斯尔</span>
          <span class="news-item-title-en">Barry goal sees Everton ease past dreadful Newcastle</span>
          <span class="news-value-point">💡 纽卡斯尔和埃弗顿之间英超比赛的亮点</span>
        </a>
        <a class="news-item" href="https://www.bbc.co.uk/sport/football/articles/cmglwjxx45gjo?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="纽卡斯尔联队和埃弗顿的球员在英超比赛后获得评分。" data-title="Who produced the kind of performance Moyes loves?" data-date="11-03 06:08" data-source="BBC">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-03 06:08</span>
          <span class="news-item-title">谁制作了Moyes喜欢的那种表演？</span>
          <span class="news-item-title-en">Who produced the kind of performance Moyes loves?</span>
          <span class="news-value-point">💡 纽卡斯尔联队和埃弗顿的球员在英超比赛后获得评分</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/live/2026/nov/02/newcastle-united-v-everton-premier-league-live" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="蒂尔诺·巴里（ Thierno Barry ）在六场比赛中的第四个进球足以让埃弗顿（ Everton ）战胜可怜的纽卡斯尔（ Newcastle ） ，后者让雅各布·拉姆齐（ Jacob Ramsey ）在贾斯尔（ Jaissle ）告诉Sky Elanga身体状况正在改善，值得今天开始；他希望他和奥苏拉（ Osula ）" data-title="Newcastle United 0-1 Everton: Premier League – as it happened" data-date="11-03 06:07" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-03 06:07</span>
          <span class="news-item-title">纽卡斯尔联队0-1埃弗顿：英超联赛–事实就是这样</span>
          <span class="news-item-title-en">Newcastle United 0-1 Everton: Premier League – as it happened</span>
          <span class="news-value-point">💡 蒂尔诺·巴里（ Thierno Barry ）在六场比赛中的第四个进球足以让埃弗顿（ Everton ）战胜可怜的纽卡斯尔（ Newcastle…</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/sep/10/premier-league-top-scorers-2026-27-race-for-golden-boot" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="找出哪位英国顶尖射手正在向进球排行榜射击。继续阅读……" data-title="Premier League top scorers 2026-27: who is leading race for the golden boot?" data-date="11-03 05:12" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-03 05:12</span>
          <span class="news-item-title">2026-27赛季英超联赛最佳射手：谁是金靴赛的领跑者？</span>
          <span class="news-item-title-en">Premier League top scorers 2026-27: who is leading race for the golden boot?</span>
          <span class="news-value-point">💡 找出哪位英国顶尖射手正在向进球排行榜射击</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/12040/13025491/aston-villa-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Aston Villa latest: McGinn keen to make Nou Camp visit a regular occurrence" data-title="Aston Villa latest: McGinn keen to make Nou Camp visit a regular occurrence" data-date="11-03 04:40" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-03 04:40</span>
          <span class="news-item-title">阿斯顿维拉最新消息：麦金热衷于让诺坎普之旅成为常态</span>
          <span class="news-item-title-en">Aston Villa latest: McGinn keen to make Nou Camp visit a regular occurrence</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/cricket/news/12040/13607259/australias-glenn-maxwell-announces-retirement-from-international-cricket" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="澳大利亚全能选手格伦·麦克斯韦（ Glenn Maxwell ）宣布退出国际板球比赛，但将继续在Big Bash联赛中为墨尔本明星队效力T20。" data-title="Australia&#39;s Maxwell announces retirement from international cricket" data-date="11-03 03:50" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-03 03:50</span>
          <span class="news-item-title">澳大利亚选手麦克斯韦宣布退出国际板球比赛</span>
          <span class="news-item-title-en">Australia's Maxwell announces retirement from international cricket</span>
          <span class="news-value-point">💡 澳大利亚全能选手格伦·麦克斯韦（ Glenn Maxwell ）宣布退出国际板球比赛，但将继续在Big Bash联赛中为墨尔本明星队效力T20</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/02/andy-madley-var-major-anfield-calls-right-arsenal-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Timber对Isak的衬衫拉扯不是审查的处罚， Madueke与Mac Allister的冲突显然不是暴力行为有一起事件让每个人都在周末说话，那就是不判利物浦处罚的决定" data-title="Andy Madley and VAR should take credit – they got major Anfield calls right | Chris Foy" data-date="11-03 03:15" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-03 03:15</span>
          <span class="news-item-title">Andy Madley和VAR应该得到赞扬–他们接到了安菲尔德的重要电话| Chris Foy</span>
          <span class="news-item-title-en">Andy Madley and VAR should take credit – they got major Anfield calls right | Chris Foy</span>
          <span class="news-value-point">💡 Timber对Isak的衬衫拉扯不是审查的处罚， Madueke与Mac Allister的冲突显然不是暴力行为有一起事件让每个人都在周末说话，…</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/football/live-blog/12040/13025499/man-city-transfer-news-rumours-and-gossip-live-updates-and-latest-on-deals-signings-loans-and-contracts" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="Man City latest: Allan eyes City breakthrough after earning first Brazil call" data-title="Man City latest: Allan eyes City breakthrough after earning first Brazil call" data-date="11-03 03:15" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-03 03:15</span>
          <span class="news-item-title">曼城最新消息： Allan在赢得首个巴西通话后关注城市突破</span>
          <span class="news-item-title-en">Man City latest: Allan eyes City breakthrough after earning first Brazil call</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/rugby-union/news/12040/13607223/england-rugby-shaun-edwards-says-steve-borthwick-turned-down-his-offer-to-work-with-side-at-2027-world-cup" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="着名的防守教练肖恩·爱德华兹说，英格兰老板史蒂夫·博思维克拒绝了他在2027年澳大利亚橄榄球世界杯上与球队合作的提议。" data-title="Edwards: Borthwick turned down my offer to work with England" data-date="11-03 02:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-03 02:00</span>
          <span class="news-item-title">Edwards ： Borthwick拒绝了我与英格兰合作的提议</span>
          <span class="news-item-title-en">Edwards: Borthwick turned down my offer to work with England</span>
          <span class="news-value-point">💡 着名的防守教练肖恩·爱德华兹说，英格兰老板史蒂夫·博思维克拒绝了他在2027年澳大利亚橄榄球世界杯上与球队合作的提议</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/netball/news/12040/13607188/england-to-host-south-africa-in-three-test-netball-series-live-on-sky-sports-in-february-as-world-cup-preparation" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="英格兰的Vitality Roses将于2月举办三场无挡板篮球系列赛，所有比赛均在天空体育上直播。" data-title="England to host South Africa live on Sky Sports in Netball World Cup prep" data-date="11-03 02:00" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-03 02:00</span>
          <span class="news-item-title">英格兰将在篮网球世界杯准备中在天空体育现场直播南非</span>
          <span class="news-item-title-en">England to host South Africa live on Sky Sports in Netball World Cup prep</span>
          <span class="news-value-point">💡 英格兰的Vitality Roses将于2月举办三场无挡板篮球系列赛，所有比赛均在天空体育上直播</span>
        </a>
        <a class="news-item" href="https://www.theguardian.com/football/2026/nov/02/arsenal-liverpool-premier-league" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="周日在利物浦的胜利表明，枪手更深入，更有经验，并且与比上赛季更弱的竞争者对抗。在此处注册我们的免费通讯阿森纳在英超联赛排行榜上占据三分。" data-title="Arsenal have everything they need to repeat as Premier League champions | Jonathan Wilson" data-date="11-02 23:47" data-source="卫报">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-theathletic">🇬🇧 卫报</span>
          <span class="news-item-date">11-02 23:47</span>
          <span class="news-item-title">阿森纳拥有成为英超冠军所需的一切|乔纳森·威尔逊</span>
          <span class="news-item-title-en">Arsenal have everything they need to repeat as Premier League champions | Jonathan Wilson</span>
          <span class="news-value-point">💡 周日在利物浦的胜利表明，枪手更深入，更有经验，并且与比上赛季更弱的竞争者对抗</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/darts/news/12040/13607004/beat-luke-littler-fallon-sherrock-should-not-have-been-selected-to-play-in-netflix-show-but-you-cant-blame-queen-of-the-palace" target="_blank" rel="noopener" data-cat="zuqiu" data-summary="天空体育专家马克·韦伯斯特（ Mark Webster ）表示，法伦·谢罗克（ Fallon Sherrock ） “不应该被选中”为Netflix的“击败卢克·利特勒” （ Beat Luke Littler ）效力，她赢得了£ 501,000的奖金。" data-title="Sherrock &#39;should not have been selected to play&#39; for Beat Luke Littler show" data-date="11-02 23:45" data-source="天空体育">
          <span class="news-cat-tag cat-zuqiu">⚽ 足球专栏</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-02 23:45</span>
          <span class="news-item-title">Sherrock “不应该被选中参加” Beat Luke Littler节目</span>
          <span class="news-item-title-en">Sherrock 'should not have been selected to play' for Beat Luke Littler show</span>
          <span class="news-value-point">💡 天空体育专家马克·韦伯斯特（ Mark Webster ）表示，法伦·谢罗克（ Fallon Sherrock ） “不应该被选中”为Netfl…</span>
        </a>
  </div>
  <div class="news-category">
    <div class="news-category-header">
      <span class="category-flag">📰</span>
      <span class="news-category-title">综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)</span>
      <span class="news-category-count">15 条</span>
    </div>
        <a class="news-item" href="https://www.ithome.com/1/021/638.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 3 日消息，索尼 SIE 昨天为 PS5 游戏机推送了系统更新 26.07-14.22.00，大小约 1.26GB，本次更新主要对漏洞进行修复，并未有其他功能调整或性能优化。参考 PlayStation Size，《GTA 6》游戏现已要求 PS5 搭载 14.22.00 系统固件才能运行，未来利用旧版系统运行自制软件的用户可能无法在第一时间玩上《GTA 6》。《GTA 6》目前计划于 11 月 19 日发售，距离正式上市仍有一段时间，因此最终零售版对 PS5 系统版本的具体要求后续仍可能发生变化。" data-title="索尼为 PS5 推送 26.07-14.22.00 系统更新，想玩《GTA 6》就得为游戏机更新最新固件" data-date="11-03 16:37" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-03 16:37</span>
          <span class="news-item-title">索尼为 PS5 推送 26.07-14.22.00 系统更新，想玩《GTA 6》就得为游戏机更新最新固件</span>
          <span class="news-value-point">💡 IT之家 11 月 3 日消息，索尼 SIE 昨天为 PS5 游戏机推送了系统更新 26.07-14.22.00，大小约 1.26GB，本次更新…</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/021/637.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 3 日消息，据《智能涌现》今日爆料，字节跳动旗下视频生成模型 Seedance 的海外收入占比已达到 50%。报道援引接近火山引擎人士消息称，过去半年，Seedance 在海外市场的收入增长近 5 倍。目前，海外已经成为 Seedance 模型的重要战场。知情人士透露，从 Token 消耗和贡献收入来看，腾讯位列 Seedance 中国区客户前三，B站则进入前十 —— 头部互联网企业正在规模化采购 Seedance。综合IT之家此前报道，9 月 27 日，在第十届平遥国际电影展期间，火山引擎正式发布 Seedance 影视合作计划，将面向全球专业影视项目提供 Token 补贴、宣发资源及技术与工具支持，单个项目激励最高可达百万人民币。10 月 23 日，火山引擎正式发布" data-title="曝字节跳动视频生成模型 Seedance 海外收入占比已达 50%，腾讯、B站是国内大客户" data-date="11-03 16:37" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-03 16:37</span>
          <span class="news-item-title">曝字节跳动视频生成模型 Seedance 海外收入占比已达 50%，腾讯、B站是国内大客户</span>
          <span class="news-value-point">💡 IT之家 11 月 3 日消息，据《智能涌现》今日爆料，字节跳动旗下视频生成模型 Seedance 的海外收入占比已达到 50%</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-03/10725388.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="牛河梁遗址第二地点。人民网记者 周颂雪摄 走进位于辽宁省朝阳市的牛河梁遗址博物馆序厅，灯暗了一瞬。" data-title="何以中国｜红山文化，从牛河梁“活”起来" data-date="11-03 16:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-03 16:30</span>
          <span class="news-item-title">何以中国｜红山文化，从牛河梁“活”起来</span>
          <span class="news-value-point">💡 牛河梁遗址第二地点</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/021/634.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 3 日消息，网易 UU 远程 10 月 31 日在 X 平台回应后续是否收费的问题，表示团队目前有在思考契合 UU 远程长久发展需求的商业化方向。用户提到的建议也是团队接下来会仔细斟酌的内容，以求权衡好用户体验和产品发展需要。11 月 2 日，网易 UU 远程表示后续的商业化会慎重考虑如何兼顾大家的使用体验与产品长期发展。此外，大家较为关心的 Linux 版本也即将和大家见面。网易 UU 远程官方还表示，后续会权衡好用户体验与项目长期发展需求的，尽可能保障每一位用户的使用权益。IT之家注：网易 UU 远程是一款由网易开发的专业远程控制软件，主打免费使用、真 4K 画质和低延迟，支持用手机、平板、电脑或电视远程操控另一台电脑。" data-title="网易 UU 远程：后续商业化会慎重考虑如何兼顾，Linux 版本即将和大家见面" data-date="11-03 16:25" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-03 16:25</span>
          <span class="news-item-title">网易 UU 远程：后续商业化会慎重考虑如何兼顾，Linux 版本即将和大家见面</span>
          <span class="news-value-point">💡 IT之家 11 月 3 日消息，网易 UU 远程 10 月 31 日在 X 平台回应后续是否收费的问题，表示团队目前有在思考契合 UU 远程长久…</span>
        </a>
        <a class="news-item" href="https://www.bbc.com/zhongwen/articles/c6eq3ez3qvnxo/trad?at_medium=RSS&at_campaign=rss" target="_blank" rel="noopener" data-cat="zonghe" data-summary="除了张剑虹，据报至少还有3名因《香港国安法》入狱的人士，亦已提早获释。外界关注，壹传媒创办人黎智英能否同获假释机会。" data-title="《苹果日报》前社长张剑虹提早获释，赴深圳交流、向官媒称“好懊悔”" data-date="11-03 16:25" data-source="BBC">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-bbc">🇬🇧 BBC</span>
          <span class="news-item-date">11-03 16:25</span>
          <span class="news-item-title">《苹果日报》前社长张剑虹提早获释，赴深圳交流、向官媒称“好懊悔”</span>
          <span class="news-value-point">💡 除了张剑虹，据报至少还有3名因《香港国安法》入狱的人士，亦已提早获释</span>
        </a>
        <a class="news-item" href="https://www.ithome.com/1/021/633.htm" target="_blank" rel="noopener" data-cat="zonghe" data-summary="IT之家 11 月 3 日消息，据外媒 PhotoRumors 昨天报道，佳能在 2026 财年第三季度财报中警告，旗下产品 2027 年可能涨价。IT之家附财报完整问答内容如下：问：预计供应短缺问题将在 2027 年持续推高成本，佳能计划如何应对？答：对于供应紧张的零部件，我们正采取一切可能措施，确保明年所需的供应量。因此我们预计采购成本将会上升，计划从明年开始通过上调产品价格，抵消这部分成本增长。随着成本上涨，我们已经陆续进行了相应价格调整。未来我们将继续从长期角度出发，决定如何将成本上涨转嫁给客户，同时考虑此举可能对销量产生影响，并在此基础上平衡盈利能力。" data-title="佳能预警：由于零部件供应紧张，旗下产品明年可能会涨价" data-date="11-03 16:23" data-source="IT之家">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 IT之家</span>
          <span class="news-item-date">11-03 16:23</span>
          <span class="news-item-title">佳能预警：由于零部件供应紧张，旗下产品明年可能会涨价</span>
          <span class="news-value-point">💡 IT之家 11 月 3 日消息，据外媒 PhotoRumors 昨天报道，佳能在 2026 财年第三季度财报中警告，旗下产品 2027 年可能涨…</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-03/10725373.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网江西德兴11月3日电(胡坤明)“孩子在学校吃得好不好、安不安全，是我们家长最牵挂的事。”在江西上饶德兴市的金桥学校食堂，前来轮值陪餐的家长丁莲珍，一边对照公示台账核对食材入库信息，一边品尝学生当日午餐。" data-title="餐盘里的“共治”：江西德兴守护学子“舌尖暖意”" data-date="11-03 16:10" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-03 16:10</span>
          <span class="news-item-title">餐盘里的“共治”：江西德兴守护学子“舌尖暖意”</span>
          <span class="news-value-point">💡 中新网江西德兴11月3日电(胡坤明)“孩子在学校吃得好不好、安不安全，是我们家长最牵挂的事</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-03/10725330.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网11月3日电 据“平安九寨”微信公众号消息，九寨沟县公安局发布警情通报，具体内容如下：" data-title="警方通报九寨沟景区游客冲突事件" data-date="11-03 16:06" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-03 16:06</span>
          <span class="news-item-title">警方通报九寨沟景区游客冲突事件</span>
          <span class="news-value-point">💡 中新网11月3日电 据“平安九寨”微信公众号消息，九寨沟县公安局发布警情通报，具体内容如下：</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/cricket/news/12040/13607326/michael-atherton-says-australia-could-implode-before-ashes-and-urges-england-to-keep-pressure-on-in-white-ball-series" target="_blank" rel="noopener" data-cat="zonghe" data-summary="澳大利亚有问题。" data-title="England told to &#39;keep pressure on&#39; with Australia at risk of &#39;imploding&#39;" data-date="11-03 16:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-03 16:00</span>
          <span class="news-item-title">英格兰被告知要“保持压力” ，澳大利亚有“内爆”的风险</span>
          <span class="news-item-title-en">England told to 'keep pressure on' with Australia at risk of 'imploding'</span>
          <span class="news-value-point">💡 澳大利亚有问题</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-03/10725343.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网嘉兴11月3日电 (钱晨菲)清晨的乌镇，河水穿过石桥，乌篷船摇过临水人家。11月3日，2026年世界互联网大会乌镇峰会开幕，来自海内外的嘉宾、客商和游客陆续走进这座江南水乡。千年古镇与全球互联网盛会相遇，古朴街巷里多了国际面孔，临水商铺间也比往日热闹几分。" data-title="平安有“数”：从三个“一”看水乡乌镇" data-date="11-03 15:52" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-03 15:52</span>
          <span class="news-item-title">平安有“数”：从三个“一”看水乡乌镇</span>
          <span class="news-value-point">💡 中新网嘉兴11月3日电 (钱晨菲)清晨的乌镇，河水穿过石桥，乌篷船摇过临水人家</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-03/10725356.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="中新网三亚11月3日电 (张月和)“看着天边橙红色的晚霞，吹着凉爽的海风，耳边还飘来餐厅驻唱歌手的歌声，这样的生活真惬意。”2日傍晚，埃及《中国周报》副社长朱新娥在三亚大东海沿着沙滩栈道漫步，不时驻足拍下她眼中的“三亚元素”。" data-title="从“老牌度假区”到“文旅新地标” ：三亚大东海的蜕变" data-date="11-03 15:45" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-03 15:45</span>
          <span class="news-item-title">从“老牌度假区”到“文旅新地标” ：三亚大东海的蜕变</span>
          <span class="news-value-point">💡 中新网三亚11月3日电 (张月和)“看着天边橙红色的晚霞，吹着凉爽的海风，耳边还飘来餐厅驻唱歌手的歌声，这样的生活真惬意</span>
        </a>
        <a class="news-item" href="https://www.chinanews.com.cn/sh/2026/11-03/10725347.shtml" target="_blank" rel="noopener" data-cat="zonghe" data-summary="青春华章丨让科技接地气 “小院落”展现大作为" data-title="让科技接地气 “小院落”展现大作为" data-date="11-03 15:30" data-source="中国新闻网">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-cn">🇨🇳 中国新闻网</span>
          <span class="news-item-date">11-03 15:30</span>
          <span class="news-item-title">让科技接地气 “小院落”展现大作为</span>
          <span class="news-value-point">💡 青春华章丨让科技接地气 “小院落”展现大作为</span>
        </a>
        <a class="news-item" href="https://techcrunch.com/2026/11/02/apple-watchs-ai-features-for-rewinding-and-recapping-conversations-begin-beta-testing/" target="_blank" rel="noopener" data-cat="zonghe" data-summary="现在处于测试阶段： Apple的新音频智能功能可以帮助您记住某人所说的话或在对话中做笔记。" data-title="Apple Watch’s AI features for rewinding and recapping conversations begin beta testing" data-date="11-03 15:20" data-source="TechCrunch">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🤖 TechCrunch</span>
          <span class="news-item-date">11-03 15:20</span>
          <span class="news-item-title">Apple Watch用于倒带和重新整理对话的人工智能功能开始测试</span>
          <span class="news-item-title-en">Apple Watch’s AI features for rewinding and recapping conversations begin beta testing</span>
          <span class="news-value-point">💡 现在处于测试阶段： Apple的新音频智能功能可以帮助您记住某人所说的话或在对话中做笔记</span>
        </a>
        <a class="news-item" href="https://www.qbitai.com/2026/11/507410.html" target="_blank" rel="noopener" data-cat="zonghe" data-summary="TeleAI智慧看护助手" data-title="苹果被曝的新产品，中国央企8个月前已装进公共卫生间" data-date="11-03 14:29" data-source="量子位">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-techcrunch">🧠 量子位</span>
          <span class="news-item-date">11-03 14:29</span>
          <span class="news-item-title">苹果被曝的新产品，中国央企8个月前已装进公共卫生间</span>
          <span class="news-value-point">💡 TeleAI智慧看护助手</span>
        </a>
        <a class="news-item" href="https://www.skysports.com/f1/news/12040/13607145/lewis-hamilton-demands-serious-talks-at-ferrari-after-charles-leclerc-incident-at-mexico-city-grand-prix" target="_blank" rel="noopener" data-cat="zonghe" data-summary="刘易斯·汉密尔顿（ Lewis Hamilton ）在墨西哥城大奖赛（ Mexico City Grand Prix ）与查尔斯·勒克莱尔（ Charles Leclerc ）开场比赛后呼吁在法拉利进行“认真谈判” ，而车队负责人弗雷德里克·瓦瑟（ Frederic Vasseur ）" data-title="Hamilton calls for &#39;serious talks&#39; at Ferrari after Leclerc incident" data-date="11-03 14:00" data-source="天空体育">
          <span class="news-cat-tag cat-zonghe">📰 综合要闻</span>
          <span class="source-badge source-skysports">🏴󠁧󠁢󠁥󠁮󠁧󠁿 天空体育</span>
          <span class="news-item-date">11-03 14:00</span>
          <span class="news-item-title">勒克莱尔事故发生后，汉密尔顿呼吁在法拉利进行“严肃会谈”</span>
          <span class="news-item-title-en">Hamilton calls for 'serious talks' at Ferrari after Leclerc incident</span>
          <span class="news-value-point">💡 刘易斯·汉密尔顿（ Lewis Hamilton ）在墨西哥城大奖赛（ Mexico City Grand Prix ）与查尔斯·勒克莱尔（ C…</span>
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


<p class="news-updated">🕐 抓取更新于 2026-11-03 16:43（北京时间）· 首页展示最近 24 小时精选动态 · 往期请查阅历史归档</p>
