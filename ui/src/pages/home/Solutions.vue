<template>
  <div class="solutions-page">
    <!-- 解决方案 Banner -->
    <div class="solutions-banner">
      <h1 class="banner-title">舆情分析解决方案</h1>
      <p class="banner-subtitle">
        针对不同行业和场景，提供定制化的舆情监测与分析解决方案
      </p>
    </div>

    <!-- 行业解决方案 -->
    <div class="solutions-section">
      <h2 class="section-title">行业解决方案</h2>
      <div class="industry-list">
        <div class="industry-item">
          <el-icon :size="60" color="#409EFF"><OfficeBuilding /></el-icon>
          <h3 class="industry-title">企业品牌管理</h3>
          <p class="industry-description">
            实时监控品牌声誉，快速响应负面舆情，提升品牌形象。
          </p>
          <el-button type="primary" @click="learnMore('enterprise')">
            了解更多
          </el-button>
        </div>
        <div class="industry-item">
          <el-icon :size="60" color="#409EFF"><User /></el-icon>
          <h3 class="industry-title">政府舆情监测</h3>
          <p class="industry-description">
            掌握社会热点，快速响应公众关切，提升政府公信力。
          </p>
          <el-button type="primary" @click="learnMore('government')">
            了解更多
          </el-button>
        </div>
        <div class="industry-item">
          <el-icon :size="60" color="#409EFF"><TrendCharts /></el-icon>
          <h3 class="industry-title">媒体热点追踪</h3>
          <p class="industry-description">
            精准分析热点话题，提升新闻报道时效性和影响力。
          </p>
          <el-button type="primary" @click="learnMore('media')">
            了解更多
          </el-button>
        </div>
      </div>
    </div>

    <!-- 场景化解决方案 -->
    <div class="solutions-section solutions-scenarios">
      <h2 class="section-title">场景化解决方案</h2>
      <div class="scenario-list">
        <div class="scenario-item">
          <h3 class="scenario-title">危机公关</h3>
          <p class="scenario-description">
            实时监测负面舆情，快速制定应对策略，降低品牌损失。
          </p>
        </div>
        <div class="scenario-item">
          <h3 class="scenario-title">市场调研</h3>
          <p class="scenario-description">
            分析消费者反馈，洞察市场趋势，助力产品优化。
          </p>
        </div>
        <div class="scenario-item">
          <h3 class="scenario-title">政策解读</h3>
          <p class="scenario-description">
            监测政策发布后的社会反响，为政府决策提供数据支持。
          </p>
        </div>
      </div>
    </div>

    <!-- 行动号召 -->
    <div class="call-to-action">
      <h2 class="action-title">定制您的舆情分析解决方案</h2>
      <p class="action-subtitle">
        联系我们，获取专属解决方案！
      </p>
      <el-button type="primary" size="large" @click="showMyself=true">
        联系销售
      </el-button>
    </div>
  </div>
  <el-dialog
    v-model="showMyself"
    title="联系方式"
    width="330"
  >
    <el-image src="public/code.png" lazy fit="cover" style="width: 300px; margin: 0 auto"/>
  </el-dialog>
</template>

<script setup>
import { OfficeBuilding, User, TrendCharts } from '@element-plus/icons-vue'
import { useRouter } from 'vue-router'
import {ref} from 'vue'

const showMyself = ref(false)
const router = useRouter()

// 了解更多
const learnMore = (industry) => {
  router.push(`/solutions/${industry}`)
}
</script>

<style scoped>
.solutions-page {
  padding: 20px;
}

.solutions-banner {
  background: linear-gradient(135deg, #409EFF, #1e3c72);
  color: #fff;
  padding: 80px 20px;
  text-align: center;
  border-radius: 8px;
  margin-bottom: 40px;
}

.banner-title {
  font-size: 3rem;
  margin-bottom: 20px;
}

.banner-subtitle {
  font-size: 1.25rem;
  margin-bottom: 40px;
}

.solutions-section {
  margin-bottom: 60px;
}

.section-title {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 40px;
  color: #333;
}

.industry-list,
.scenario-list {
  display: flex;
  justify-content: space-around;
  gap: 20px;
}

.industry-item,
.scenario-item {
  flex: 1;
  text-align: center;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.industry-title,
.scenario-title {
  font-size: 1.5rem;
  margin: 20px 0 10px;
  color: #333;
}

.industry-description,
.scenario-description {
  font-size: 1rem;
  color: #666;
  margin-bottom: 20px;
}

.solutions-scenarios {
  background-color: #f8f9fa;
  padding: 40px 20px;
  border-radius: 8px;
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