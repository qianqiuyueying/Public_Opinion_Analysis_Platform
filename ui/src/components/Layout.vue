<template>
  <div class="admin-container">
    <!-- 顶部导航栏 -->
    <el-header class="header">
      <div class="header-left">
        <span class="system-title">舆情分析平台管理后台</span>
      </div>
      <div class="header-right">
        <el-badge :value="newMessageCount" class="notification-badge">
          <el-icon @click="handleToMessage" :size="20">
            <Bell/>
          </el-icon>
        </el-badge>
        <el-dropdown>
          <div class="user-info">
            <el-avatar :size="30" :src="store.avatar"/>
            <span class="user-name">{{store.username}}</span>
            <el-icon class="arrow-down">
              <ArrowDown/>
            </el-icon>
          </div>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item @click="handleToInfo">个人中心</el-dropdown-item>
              <el-dropdown-item @click="handleLogout">退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </div>
    </el-header>

    <!-- 整体布局 -->
    <div class="main-wrapper">
      <!-- 左侧菜单栏 -->
      <el-aside class="sidebar" :width="isCollapse ? '64px' : '240px'">
        <div class="collapse-btn" @click="toggleCollapse">
          <el-icon :size="20">
            <Expand v-if="isCollapse"/>
            <Fold v-else/>
          </el-icon>
        </div>

        <el-menu
            :default-active="activeMenu"
            class="nav-menu"
            :collapse="isCollapse"
            router
            unique-opened
        >
          <el-menu-item index="/layout/dashboard">
            <el-icon>
              <Location/>
            </el-icon>
            <span>仪表盘</span>
          </el-menu-item>

          <!-- 爬虫管理模块 -->
          <el-sub-menu index="2">
            <template #title>
              <el-icon>
                <DataBoard/>
              </el-icon>
              <span>爬虫管理</span>
            </template>
            <el-menu-item index="/layout/scrapy/spider">爬虫管理</el-menu-item>
            <el-menu-item index="/layout/scrapy/task">任务管理</el-menu-item>
            <el-menu-item index="/layout/scrapy/data">数据管理</el-menu-item>
          </el-sub-menu>

          <!-- 数据分析模块 -->
          <el-sub-menu index="1">
            <template #title>
              <el-icon>
                <DataAnalysis/>
              </el-icon>
              <span>数据分析</span>
            </template>
            <el-menu-item index="/layout/analytics/overview">数据总览</el-menu-item>
            <el-menu-item index="/layout/analytics/details">情感分析</el-menu-item>
            <el-menu-item index="/layout/analytics/trend">趋势分析</el-menu-item>
          </el-sub-menu>

          <!-- 用户管理模块 -->
          <el-sub-menu index="/user">

            <template #title>
              <el-icon>
                <User/>
              </el-icon>
              <span>用户管理</span>
            </template>

            <el-menu-item index="/layout/user/info">
              个人信息
            </el-menu-item>
            <el-menu-item index="/layout/user/list">
              用户列表
            </el-menu-item>
          </el-sub-menu>

          <!-- 消息 -->
          <el-menu-item index="/layout/message">
            <el-icon>
              <Message/>
            </el-icon>
            <span>消息</span>
          </el-menu-item>

          <!--  公告板  -->
          <el-menu-item index="/layout/board">
            <el-icon>
              <DataBoard/>
            </el-icon>
            <span>公告板</span>
          </el-menu-item>

        </el-menu>
      </el-aside>

      <!-- 主内容区域 -->
      <main class="content-wrapper">
        <router-view/>
      </main>
    </div>
  </div>
</template>

<script setup>
import {ref, onMounted} from 'vue'
import {useRouter} from 'vue-router'
import {
  DataAnalysis,
  DataBoard,
  User,
  Bell,
  Expand,
  Fold,
  ArrowDown,
  Location, Message
} from '@element-plus/icons-vue'
import {useUserStore} from "@/stores/userStore.js";
import {getUserInfoService} from "@/api/userService.js";

onMounted(async () => {

})


const newMessageCount = ref(0)
const router = useRouter()
const activeMenu = ref('/layout/dashboard')
const isCollapse = ref(false)
const store = useUserStore()

const toggleCollapse = () => {
  isCollapse.value = !isCollapse.value
}

const handleToMessage = () => {
  router.push('/layout/message')
  activeMenu.value = '/layout/message'
}

const handleToInfo = () => {
  router.push('/layout/user/info')
  activeMenu.value = '/layout/user/info'
}


const handleLogout = () => {
  router.push('/login')
  // 实际项目需添加退出登录逻辑
}
</script>

<style scoped>
.admin-container {
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #fff;
  border-bottom: 1px solid #e6e6e6;
  padding: 0 24px;
}

.system-title {
  font-size: 20px;
  font-weight: 600;
  color: #409EFF;
}

.header-right {
  display: flex;
  align-items: center;
  gap: 24px;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  padding: 8px 12px;
  border-radius: 4px;
  transition: background 0.3s;
}

.user-info:hover {
  background: #f5f7fa;
}

.user-name {
  font-weight: 500;
}

.arrow-down {
  margin-left: 4px;
}

.notification-badge {
  cursor: pointer;
}

.main-wrapper {
  flex: 1;
  display: flex;
  overflow: hidden;
}

.sidebar {
  background: #fff;
  border-right: 1px solid #e6e6e6;
  transition: width 0.3s;
  position: relative;
}

.collapse-btn {
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  border-bottom: 1px solid #e6e6e6;
}

.nav-menu {
  border-right: none;
}

.nav-menu:not(.el-menu--collapse) {
  width: 240px;
}

.content-wrapper {
  flex: 1;
  padding: 24px;
  background: #f5f7fa;
  overflow-y: auto;
}
</style>