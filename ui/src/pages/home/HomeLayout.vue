<template>
  <div class="home-page">
    <!-- 导航栏 -->
    <el-header class="header">
      <div class="logo">舆情分析平台</div>
      <div class="nav">
        <el-link type="primary" :underline="false" @click="goToHome">首页</el-link>
        <el-link type="primary" :underline="false" @click="goToProducts">产品介绍</el-link>
        <el-link type="primary" :underline="false" @click="goToSolutions">解决方案</el-link>
        <el-link type="primary" :underline="false" @click="goToCustomers">客户案例</el-link>
        <el-link type="primary" :underline="false" @click="goToAbout">关于我们</el-link>
      </div>
      <div class="actions">
        <el-button type="primary" @click="goToLogin">登录</el-button>
        <el-button @click="goToRegister">注册</el-button>
      </div>
    </el-header>

    <el-main>
      <router-view/>
    </el-main>

    <!-- 底部 -->
    <el-footer class="neko-footer">
      <div class="footer-content">
        <p class="footer-text">
          舆情分析平台 @2025 Created by 秋神
        </p>
        <p class="footer-text">
          仅供用于交流学习，严禁用于商业用途
        </p>
      </div>
    </el-footer>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import {ref} from 'vue'

const router = useRouter()

// 跳转首页
const goToHome = () => {
  router.push('/home')
}

// 跳转产品介绍
const goToProducts = () => {
  router.push('/products')
}

// 跳转解决方案
const goToSolutions = () => {
  router.push('/solutions')
}

// 跳转客户案例
const goToCustomers = () => {
  router.push('/customers')
}

// 跳转关于我们
const goToAbout = () => {
  router.push('/about')
}

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