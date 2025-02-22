<template>
  <div class="celebration-page">
    <!-- 背景动画 -->
    <div class="background-animation">
      <div class="star"></div>
      <div class="star"></div>
      <div class="star"></div>
      <div class="star"></div>
      <div class="star"></div>
    </div>

    <!-- 主要内容 -->
    <div class="celebration-content">
      <h1 class="celebration-title">🎉 恭喜！ 🎉</h1>
      <p class="celebration-message">
        您的爬虫已成功生成！<br />
        准备好开始您的数据之旅了吗？
      </p>

      <!-- 后续操作介绍 -->
      <div class="next-steps">
        <h3>接下来您可以：</h3>
        <ul>
          <li>前往任务管理，开始爬虫任务</li>
          <li>前往爬虫管理，查看所有爬虫。</li>
        </ul>
      </div>

      <!-- 操作按钮 -->
      <div class="celebration-actions">
        <el-button type="primary" size="large" @click="goToTask">
          任务管理
        </el-button>
        <el-button type="success" size="large" @click="goToSpider">
          爬虫管理
        </el-button>
      </div>
    </div>
  </div>
</template>

<script setup>
import router from "@/router/index.js";





const goToTask = () => {
  router.push('/layout/scrapy/task')
}

const goToSpider = () => {
  router.push('/layout/scrapy/spider')
}
</script>

<style scoped>
.celebration-page {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 50vh;
  background-color: #f8f9fa; /* 浅灰色背景 */
  overflow: hidden;
  position: relative;
}

.background-animation {
  position: absolute;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.star {
  position: absolute;
  width: 2px;
  height: 2px;
  background-color: #409eff; /* 蓝色星星 */
  border-radius: 50%;
  animation: star-fall 5s infinite;
}

.star:nth-child(1) {
  left: 10%;
  animation-delay: 0s;
}

.star:nth-child(2) {
  left: 20%;
  animation-delay: 1s;
}

.star:nth-child(3) {
  left: 30%;
  animation-delay: 2s;
}

.star:nth-child(4) {
  left: 40%;
  animation-delay: 3s;
}

.star:nth-child(5) {
  left: 50%;
  animation-delay: 4s;
}

@keyframes star-fall {
  0% {
    transform: translateY(-100vh);
  }
  100% {
    transform: translateY(100vh);
  }
}

.celebration-content {
  text-align: center;
  color: #333; /* 深灰色文字 */
  z-index: 1;
}

.celebration-title {
  font-size: 4rem;
  margin-bottom: 20px;
  animation: bounce 2s infinite;
  color: #409eff; /* 蓝色标题 */
}

.celebration-message {
  font-size: 1.5rem;
  margin-bottom: 40px;
  color: #666; /* 灰色文字 */
}

.next-steps {
  background: rgba(255, 255, 255, 0.9); /* 半透明白色背景 */
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 40px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* 轻微阴影 */
}

.next-steps h3 {
  margin-top: 0;
  font-size: 1.25rem;
  color: #409eff; /* 蓝色标题 */
}

.next-steps ul {
  list-style: none;
  padding: 0;
}

.next-steps li {
  margin: 10px 0;
  font-size: 1rem;
  color: #666; /* 灰色文字 */
}

.celebration-actions {
  display: flex;
  justify-content: center;
  gap: 20px;
}

@keyframes bounce {
  0%,
  20%,
  50%,
  80%,
  100% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(-30px);
  }
  60% {
    transform: translateY(-15px);
  }
}
</style>