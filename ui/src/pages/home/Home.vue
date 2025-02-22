<template>
  <div class="home-page">
    <!-- 导航栏 -->
    <el-header class="header">
      <div class="logo">舆情分析平台</div>
      <div class="nav">
        <el-link type="primary" :underline="false">首页</el-link>
        <el-link type="primary" :underline="false">产品介绍</el-link>
        <el-link type="primary" :underline="false">解决方案</el-link>
        <el-link type="primary" :underline="false">客户案例</el-link>
        <el-link type="primary" :underline="false">关于我们</el-link>
      </div>
      <div class="actions">
        <el-button type="primary" @click="goToLogin">登录</el-button>
        <el-button @click="goToRegister">注册</el-button>
      </div>
    </el-header>

    <!-- 首页 Banner -->
    <div class="banner">
      <div class="banner-content">
        <h1 class="banner-title">舆情分析平台</h1>
        <p class="banner-subtitle">
          全面监测、精准分析、智能预警，助您轻松掌握舆情动态
        </p>
        <el-button type="primary" size="large" @click="goToLogin">
          立即体验
        </el-button>
      </div>
    </div>

    <!-- 平台特色 -->
    <div class="features">
      <h2 class="section-title">平台特色</h2>
      <el-row :gutter="40">
        <el-col :span="8">
          <div class="feature-card">
            <el-icon :size="60" color="#409EFF"><Monitor /></el-icon>
            <h3 class="feature-title">全面监测</h3>
            <p class="feature-description">
              覆盖全网舆情数据，实时监控社交媒体、新闻、论坛等多渠道信息。
            </p>
          </div>
        </el-col>
        <el-col :span="8">
          <div class="feature-card">
            <el-icon :size="60" color="#409EFF"><DataAnalysis /></el-icon>
            <h3 class="feature-title">精准分析</h3>
            <p class="feature-description">
              基于 AI 技术，提供情感分析、热点追踪、趋势预测等深度分析功能。
            </p>
          </div>
        </el-col>
        <el-col :span="8">
          <div class="feature-card">
            <el-icon :size="60" color="#409EFF"><Bell /></el-icon>
            <h3 class="feature-title">智能预警</h3>
            <p class="feature-description">
              自定义预警规则，及时推送舆情风险，助您快速响应。
            </p>
          </div>
        </el-col>
      </el-row>
    </div>

    <!-- 客户案例 -->
    <div class="cases">
      <h2 class="section-title">客户案例</h2>
      <el-carousel height="300px" :interval="5000">
        <el-carousel-item v-for="(item, index) in cases" :key="index">
          <div class="case-item">
            <img :src="item.image" alt="案例图片" class="case-image" />
            <div class="case-content">
              <h3 class="case-title">{{ item.title }}</h3>
              <p class="case-description">{{ item.description }}</p>
            </div>
          </div>
        </el-carousel-item>
      </el-carousel>
    </div>

    <!-- 底部 -->
    <el-footer class="footer">
      <div class="footer-content">
        <p>© 2023 舆情分析平台. All rights reserved.</p>
        <el-link type="primary" :underline="false">隐私政策</el-link>
        <el-link type="primary" :underline="false">服务条款</el-link>
      </div>
    </el-footer>
  </div>
</template>

<script setup>
import { Monitor, DataAnalysis, Bell } from '@element-plus/icons-vue'
import { useRouter } from 'vue-router'
import {ref} from 'vue'

const router = useRouter()

// 客户案例数据
const cases = ref([
  {
    image: 'https://via.placeholder.com/800x400',
    title: '某知名企业舆情管理',
    description: '通过平台实现全网舆情监控，提升品牌声誉管理效率。',
  },
  {
    image: 'https://via.placeholder.com/800x400',
    title: '某政府机构舆情监测',
    description: '实时掌握社会热点，快速响应公众关切。',
  },
  {
    image: 'https://via.placeholder.com/800x400',
    title: '某媒体机构热点追踪',
    description: '精准分析热点话题，提升新闻报道时效性。',
  },
])

// 跳转登录页
const goToLogin = () => {
  router.push('/login')
}

// 跳转注册页
const goToRegister = () => {
  router.push('/register')
}
</script>

<style scoped>
.home-page {
  font-family: Arial, sans-serif;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 40px;
  background-color: #fff;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}

.logo {
  font-size: 24px;
  font-weight: bold;
  color: #409EFF;
}

.nav {
  display: flex;
  gap: 20px;
}

.actions {
  display: flex;
  gap: 10px;
}

.banner {
  height: 500px;
  background: url('https://via.placeholder.com/1920x500') no-repeat center center;
  background-size: cover;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  color: #fff;
}

.banner-content {
  max-width: 800px;
}

/* 方案1：赛博朋克风格 */
.banner-title {
  font-family: 'Arial Black', sans-serif;
  font-size: 4.5rem;
  text-transform: uppercase;
  background: linear-gradient(45deg,
  #00ff9d 25%,
  #00b8ff 50%,
  #ff006e 75%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  text-shadow: 0 0 20px rgba(0,255,157,0.5),
  0 0 40px rgba(0,184,255,0.3),
  0 0 60px rgba(255,0,110,0.2);
  animation: neonGlow 2s ease-in-out infinite alternate;
}

.banner-subtitle {
  font-size: 20px;
  margin-bottom: 40px;
}

.features {
  padding: 60px 40px;
  background-color: #f9f9f9;
  text-align: center;
}

.section-title {
  font-size: 32px;
  margin-bottom: 40px;
}

.feature-card {
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}

.feature-title {
  font-size: 24px;
  margin: 20px 0;
}

.feature-description {
  font-size: 16px;
  color: #666;
}

.cases {
  padding: 60px 40px;
  text-align: center;
}

.case-item {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.case-image {
  width: 50%;
  height: 100%;
  object-fit: cover;
  border-radius: 8px;
}

.case-content {
  width: 40%;
  padding: 20px;
  text-align: left;
}

.case-title {
  font-size: 24px;
  margin-bottom: 10px;
}

.case-description {
  font-size: 16px;
  color: #666;
}

.footer {
  padding: 20px;
  background-color: #f9f9f9;
  text-align: center;
}

.footer-content {
  display: flex;
  justify-content: center;
  gap: 20px;
}
</style>