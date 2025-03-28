<template>
  <div class="spider-selector">
    <h1 class="title">选择爬取关键词的平台</h1>
    <div class="card-container">
      <!-- 小红书 -->
      <div
          class="spider-card"
          :class="{ active: spiderInfo.type === 'RedNote' }"
          @click="handleToRedNote"
      >
        <div class="card-icon">
          <el-icon :size="60">
            <Connection/>
          </el-icon>
        </div>
        <h2 class="card-title">小红书</h2>
        <p class="card-description">
          小红书以年轻用户为主，内容涵盖生活方式、美妆、时尚等领域，是分析消费趋势和品牌口碑的重要平台。
        </p>
      </div>

      <!-- 微博 -->
      <div
          class="spider-card"
          :class="{ active: spiderInfo.type === 'Weibo' }"
          @click="handleToWeibo"
      >
        <div class="card-icon">
          <el-icon :size="60">
            <ChromeFilled/>
          </el-icon>
        </div>
        <h2 class="card-title">微博</h2>
        <p class="card-description">
          微博作为开放的社交媒体平台，实时性强，热点话题传播迅速，是舆情监测和事件追踪的核心渠道。
        </p>
      </div>

      <!-- 抖音 -->
      <div
          class="spider-card"
          :class="{ active: spiderInfo.type === 'Tiktok' }"
          @click="handleToTiktok"
      >
        <div class="card-icon">
          <el-icon :size="60">
            <Document/>
          </el-icon>
        </div>
        <h2 class="card-title">抖音</h2>
        <p class="card-description">
          抖音以短视频形式为主，用户活跃度高，内容传播速度快，适合捕捉年轻群体的情绪和流行趋势。
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import {reactive, ref} from "vue";
import {Connection, ChromeFilled, Document} from "@element-plus/icons-vue";

// 使用 defineModel 声明双向绑定的模型
const spiderInfo = defineModel('spiderInfo')

// 切换到 RedNote 类型爬虫
const handleToRedNote = () => {
  spiderInfo.value.type = 'RedNote';
  spiderInfo.value.config = {
    key: "",  // 关键词
    NoteType: "all",  // 笔记类型（不限：自动识别图文或视频 图文：爬取文章和评论 视频：爬取标题和评论）
    sortedBy: "general"  // 排序依据（综合 general 最新 new 最热 hot）
  }
};

// 切换到 weibo 爬虫
const handleToWeibo = () => {
  spiderInfo.value.type = 'Weibo';
  spiderInfo.value.config = {
    key: "",  // 关键词
    blogType: "all",  // 类型（全部 all 热门 hot 原创 original 认证用户 vip 媒体 media 观点 view）
    time: ""  // 时间限制
  }
};

// 切换到抖音爬虫
const handleToTiktok = () => {
  spiderInfo.value.type = 'Tiktok';
  spiderInfo.value.config = {
    sortedBy: "general",  // 排序依据
    publishTime: "all",  // 发布时间（不限 一天内 一周内 半年内）
    duration: "all",  // 视频时长单位暂定为秒（不限 一分钟以下 1-5分钟 5分钟以上）
    contentType: 'all'  // 内容形式（图文、视频）
  }
};
</script>

<style scoped>
.spider-selector {
  padding: 40px;
  max-width: 1200px;
  margin: 0 auto;
}

.title {
  text-align: center;
  font-size: 32px;
  color: #2c3e50;
  margin-bottom: 40px;
}

.card-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* 改为 3 列 */
  gap: 40px;
}

.spider-card {
  padding: 40px;
  border: 2px solid #e4e7ed;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
  text-align: center;
  background: #fff;
}

.spider-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

.spider-card.active {
  border-color: #409eff;
  background: #f5f7fa;
}

.card-icon {
  margin-bottom: 20px;
  color: #409eff;
}

.card-title {
  font-size: 24px;
  color: #2c3e50;
  margin-bottom: 16px;
}

.card-description {
  font-size: 16px;
  color: #666;
  line-height: 1.6;
}
</style>