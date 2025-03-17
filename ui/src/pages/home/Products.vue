<template>
  <div class="product-intro-page">

    <!-- 产品概述 -->
    <div class="product-overview">
      <h2 class="section-title">产品概述</h2>
      <p class="overview-description">
        舆情分析平台是一款基于 AI 技术的智能化舆情监测与分析工具，帮助企业和机构实时掌握全网舆情动态，提供精准的情感分析、热点追踪和趋势预测，助力快速响应和科学决策。
      </p>
    </div>

    <!-- 核心功能 -->
    <div class="product-section">
      <h2 class="section-title">核心功能</h2>
      <div class="feature-list">
        <div class="feature-item">
          <el-icon :size="60" color="#409EFF"><Monitor /></el-icon>
          <h3 class="feature-title">全面监测</h3>
          <p class="feature-description">
            覆盖全网舆情数据，实时监控社交媒体、新闻、论坛等多渠道信息。
          </p>
        </div>
        <div class="feature-item">
          <el-icon :size="60" color="#409EFF"><DataAnalysis /></el-icon>
          <h3 class="feature-title">精准分析</h3>
          <p class="feature-description">
            基于 AI 技术，提供情感分析、热点追踪、趋势预测等深度分析功能。
          </p>
        </div>
        <div class="feature-item">
          <el-icon :size="60" color="#409EFF"><Bell /></el-icon>
          <h3 class="feature-title">智能预警</h3>
          <p class="feature-description">
            自定义预警规则，及时推送舆情风险，助您快速响应。
          </p>
        </div>
      </div>
    </div>

    <!-- 产品优势 -->
    <div class="product-section product-advantages">
      <h2 class="section-title">产品优势</h2>
      <div class="advantage-list">
        <div class="advantage-item">
          <h3 class="advantage-title">高效便捷</h3>
          <p class="advantage-description">
            一键配置，快速启动舆情监测任务，节省时间和人力成本。
          </p>
        </div>
        <div class="advantage-item">
          <h3 class="advantage-title">智能分析</h3>
          <p class="advantage-description">
            基于 AI 的智能分析引擎，自动生成舆情报告，提升决策效率。
          </p>
        </div>
        <div class="advantage-item">
          <h3 class="advantage-title">灵活定制</h3>
          <p class="advantage-description">
            支持自定义监测规则和预警条件，满足不同场景需求。
          </p>
        </div>
      </div>
    </div>

    <!-- 客户评价 -->
    <div class="product-section">
      <h2 class="section-title">客户评价</h2>
      <div class="testimonial-list">
        <div class="testimonial-item">
          <el-avatar :size="60" src="https://via.placeholder.com/60" />
          <div class="testimonial-content">
            <p class="testimonial-text">
              “舆情分析平台帮助我们实时掌握市场动态，极大提升了品牌管理效率。”
            </p>
            <p class="testimonial-author">—— 某知名企业市场总监</p>
          </div>
        </div>
        <div class="testimonial-item">
          <el-avatar :size="60" src="https://via.placeholder.com/60" />
          <div class="testimonial-content">
            <p class="testimonial-text">
              “平台的智能预警功能非常实用，帮助我们快速响应舆情风险。”
            </p>
            <p class="testimonial-author">—— 某政府机构负责人</p>
          </div>
        </div>
      </div>
    </div>

    <!-- 行动号召 -->
    <div class="call-to-action">
      <h2 class="action-title">立即体验舆情分析平台</h2>
      <p class="action-subtitle">
        开启您的数据之旅，轻松掌握舆情动态！
      </p>
      <el-button type="primary" size="large" @click="getStarted">
        免费试用
      </el-button>
    </div>
  </div>
</template>

<script setup>
import { Monitor, DataAnalysis, Bell } from '@element-plus/icons-vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// 跳转到体验页面
const getStarted = () => {
  router.push('/login')
}
</script>

<style scoped>
.product-intro-page {
  padding: 20px;
}


.product-overview {
  text-align: center;
  margin-bottom: 60px;
}

.overview-description {
  font-size: 1.1rem;
  color: #666;
  max-width: 800px;
  margin: 0 auto;
}

.product-section {
  margin-bottom: 60px;
}

.section-title {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 40px;
  color: #333;
}

.feature-list,
.advantage-list {
  display: flex;
  justify-content: space-around;
  gap: 20px;
}

.feature-item,
.advantage-item {
  flex: 1;
  text-align: center;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.feature-title,
.advantage-title {
  font-size: 1.5rem;
  margin: 20px 0 10px;
  color: #333;
}

.feature-description,
.advantage-description {
  font-size: 1rem;
  color: #666;
}

.product-advantages {
  background-color: #f8f9fa;
  padding: 40px 20px;
  border-radius: 8px;
}

.testimonial-list {
  display: flex;
  justify-content: center;
  gap: 40px;
}

.testimonial-item {
  display: flex;
  align-items: center;
  gap: 20px;
  max-width: 400px;
}

.testimonial-text {
  font-size: 1rem;
  color: #666;
  margin-bottom: 10px;
}

.testimonial-author {
  font-size: 0.9rem;
  color: #999;
  text-align: right;
}

.call-to-action {
  background: linear-gradient(135deg, #409EFF, #1e3c72);
  color: #fff;
  padding: 80px 20px;
  text-align: center;
  border-radius: 8px;
  margin-bottom: 40px;
}

.action-title {
  font-size: 2rem;
  margin-bottom: 20px;
}

.action-subtitle {
  font-size: 1.25rem;
  margin-bottom: 40px;
}
</style>