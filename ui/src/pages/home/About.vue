<template>
  <div class="personal-page">
    <!-- 个人信息 -->
    <div class="info-section">
      <h2 class="section-title">关于我</h2>
      <div class="profile-container">
        <div class="profile">
          <el-image :src="profileImage" class="profile-image" lazy />
          <div class="text-content">
            <p class="description-placeholder"><!-- 留空供您填写个人简介 --></p>
          </div>
        </div>
      </div>
    </div>

    <!-- 项目经验 -->
    <div class="project-section">
      <h2 class="section-title">我的项目</h2>
      <div class="projects-list">
        <div v-for="(project, index) in projects" :key="index" class="project-item">
          <h3 class="project-name">{{ project.name }}</h3>
          <p class="project-description"><!-- 留空供您填写项目描述 --></p>
        </div>
      </div>
    </div>

    <!-- 技能展示 -->
    <div class="skills-section">
      <h2 class="section-title">我的技能</h2>
      <div class="skills-list">
        <div v-for="(skill, index) in skills" :key="index" class="skill-item">
          <span class="skill-name">{{ skill }}</span>
        </div>
      </div>
    </div>

    <!-- 联系方式 -->
    <div class="contact-section">
      <h2 class="section-title">联系我</h2>
      <el-button type="primary" size="large" @click="showMyself=true">
        发送消息
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

// 个人信息
const profileImage = ref('public/myself.jpg')

// 项目经验数据
const projects = ref([
  { name: '大事件管理系统' },
  { name: '低代码爬虫平台' },
  // 可继续添加更多项目
])

// 技能数据
const skills = ref(['全栈，主要语言是java、python、vue', '运维，熟悉linux、docker部署、nginx转发', '爬虫，熟悉自动化批量精准爬取数据'])

</script>

<style scoped>
.personal-page {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto; /* 水平居中 */
}

.section-title {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 20px;
  color: #333;
}

.info-section,
.project-section,
.skills-section,
.contact-section {
  margin-bottom: 40px;
}

.profile-container {
  display: flex;
  justify-content: center;
}

.profile {
  display: flex;
  align-items: center; /* 垂直居中 */
  max-width: 800px;
}

.profile-image {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
}

.text-content {
  display: flex;
  flex-direction: column;
  justify-content: center; /* 垂直居中 */
  flex-grow: 1; /* 让文本内容占据剩余空间 */
}

.description-placeholder,
.project-description {
  font-size: 1.1rem;
  color: #666;
  line-height: 1.6;
  max-width: 600px;
}

.projects-list,
.skills-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
}

.project-item,
.skill-item {
  background-color: #f7f7f7;
  padding: 20px;
  border-radius: 8px;
  width: calc(33.333% - 40px / 3); /* 适应三个一行 */
  box-sizing: border-box;
}

.contact-section {
  text-align: center;
}
</style>