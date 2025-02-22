<script setup>
import { Connection, ChromeFilled } from "@element-plus/icons-vue";

// 使用 defineModel 声明双向绑定的模型
const spiderInfo = defineModel('spiderInfo');
</script>

<template>
  <div class="spider-selector">
    <h1 class="title">选择爬虫类型</h1>
    <div class="card-container">
      <div
          class="spider-card"
          :class="{ active: spiderInfo.type === 'APIClass' }"
          @click="spiderInfo.type = 'APIClass'; spiderInfo.description = 'API类型爬虫的描述'"
      >
        <div class="card-icon">
          <el-icon :size="60">
            <Connection />
          </el-icon>
        </div>
        <h2 class="card-title">API类型爬虫</h2>
        <p class="card-description">
          爬取目标是网站的API接口，获取接口响应后通过分析JSON结构进行有效数据的采集
        </p>
      </div>

      <div
          class="spider-card"
          :class="{ active: spiderInfo.type === 'PageClass' }"
          @click="spiderInfo.type = 'PageClass'; spiderInfo.description = '网页类型爬虫的描述'"
      >
        <div class="card-icon">
          <el-icon :size="60">
            <ChromeFilled />
          </el-icon>
        </div>
        <h2 class="card-title">网页类型爬虫</h2>
        <p class="card-description">
          爬取目标是普通网页，获取网页的DOM后通过分析页面结构进行有效元素的采集
        </p>
      </div>
    </div>
  </div>
</template>

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
  grid-template-columns: repeat(2, 1fr);
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