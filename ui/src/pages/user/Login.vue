<template>
  <div class="login-container">
    <el-card class="login-box">
      <h2 class="login-title">欢迎登录</h2>
      <el-form
          :model="form"
          :rules="rules"
          ref="loginForm"
          @keyup.enter="handleLogin"
      >
        <el-form-item prop="username">
          <el-input
              v-model="form.username"
              placeholder="请输入用户名"
              :prefix-icon="User"
              size="large"
          />
        </el-form-item>

        <el-form-item prop="password">
          <el-input
              v-model="form.password"
              type="password"
              placeholder="请输入密码"
              show-password
              :prefix-icon="Lock"
              size="large"
          />
        </el-form-item>

        <div class="login-options">
          <el-checkbox v-model="rememberMe">记住我</el-checkbox>
          <el-link type="primary" :underline="false" href="/forget-password">忘记密码?</el-link>
        </div>

        <el-button
            type="primary"
            size="large"
            @click="handleLogin"
            :loading="loading"
            class="login-btn"
        >
          立即登录
        </el-button>

        <div class="register-link">
          没有账号？<el-link type="primary" :underline="false" href="/register">立即注册</el-link>
        </div>
      </el-form>
    </el-card>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import 'element-plus/dist/index.css'
import { ElMessage } from 'element-plus'
import { User, Lock } from '@element-plus/icons-vue'
import {loginService} from '@/api/userService.js'
import router from "@/router/index.js";
import {getUserInfoService} from "@/api/userService.js";
import {useUserStore} from "@/stores/userStore.js";


// 表单数据
const form = reactive({
  username: '',
  password: ''
})

// 表单验证规则
const rules = reactive({
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { min: 6, message: '密码长度至少6位', trigger: 'blur' }
  ]
})

// 其他状态
const rememberMe = ref(false)
const loading = ref(false)
const loginForm = ref(null)

// 登录方法
const handleLogin = async () => {
  try {
    await loginForm.value.validate()
    loading.value = true
    let {username, password} = form
    const data = await loginService({username, password})
    if (data.data.code === 200) {
      const infoRes = await getUserInfoService({username})
      if (infoRes.data.code === 200) {
        const store = useUserStore()
        store.setInfo(infoRes.data.data)
        console.log(infoRes.data.data)
      }
      await router.push('/layout/dashboard')
    }
  } catch (error) {
    ElMessage.error(error.response.data.detail)
  }
  finally {
    loading.value = false
  }
}
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.login-box {
  width: 400px;
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
}

.login-title {
  text-align: center;
  color: #303133;
  margin-bottom: 40px;
  font-size: 24px;
  font-weight: 500;
}

.login-options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.login-btn {
  width: 100%;
  margin-top: 10px;
  letter-spacing: 2px;
}

.register-link {
  margin-top: 24px;
  text-align: center;
  color: #606266;
}

.el-link {
  font-weight: 500;
}
</style>