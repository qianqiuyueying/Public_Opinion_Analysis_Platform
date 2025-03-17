<template>
  <div class="case-studies-page">
    <!-- 客户案例列表 -->
    <div class="case-studies-section">
      <h2 class="section-title">成功案例</h2>
      <div class="case-list">
        <div v-for="(item, index) in caseList" :key="index" class="case-item">
          <el-image :src="item.image" class="case-image" lazy />
          <div class="case-content">
            <h3 class="case-title">{{ item.title }}</h3>
            <p class="case-description">{{ item.description }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- 行动号召 -->
    <div class="call-to-action">
      <h2 class="action-title">开启您的成功之旅</h2>
      <p class="action-subtitle">联系我们，获取专属解决方案！</p>
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
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const showMyself = ref(false)
const router = useRouter()

// 案例列表数据
const caseList = ref([
  {
    id: 'enterprise',
    image: 'https://via.placeholder.com/800x400',
    title: '某知名企业品牌管理',
    description: '通过平台实现全网舆情监控，提升品牌声誉管理效率。'
  },
  {
    id: 'government',
    image: 'https://via.placeholder.com/800x400',
    title: '某政府机构舆情监测',
    description: '实时掌握社会热点，快速响应公众关切。'
  },
  {
    id: 'media',
    image: 'https://via.placeholder.com/800x400',
    title: '某媒体机构热点追踪',
    description: '精准分析热点话题，提升新闻报道时效性。'
  }
])
</script>

<style scoped>
.case-studies-page {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.case-studies-section {
  margin-bottom: 60px;
}

.section-title {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 40px;
  color: #333;
}

.case-list {
  display: flex;
  flex-direction: column;
  gap: 40px;
}

.case-item {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  display: flex;
  align-items: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.case-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
}

.case-image {
  width: 50%;
  height: 300px;
  object-fit: cover;
}

.case-content {
  width: 50%;
  padding: 40px;
  text-align: left;
}

.case-title {
  font-size: 1.75rem;
  margin-bottom: 20px;
  color: #333;
}

.case-description {
  font-size: 1.1rem;
  color: #666;
  line-height: 1.6;
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