<template>
  <div class="register-container">
    <el-card class="register-box">
      <h2 class="register-title">用户注册</h2>
      <el-form
          :model="form"
          :rules="rules"
          ref="registerForm"
          @keyup.enter="handleRegister"
      >
        <el-form-item prop="username">
          <el-input
              v-model="form.username"
              placeholder="请输入用户名"
              :prefix-icon="User"
              size="large"
          />
        </el-form-item>

        <el-form-item prop="email">
          <el-input
              v-model="form.email"
              placeholder="请输入邮箱"
              :prefix-icon="Message"
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

        <el-form-item prop="confirmPassword">
          <el-input
              v-model="form.confirmPassword"
              type="password"
              placeholder="请确认密码"
              show-password
              :prefix-icon="Lock"
              size="large"
          />
        </el-form-item>

        <el-form-item prop="verificationCode">
          <div class="code-input">
            <el-input
                v-model="form.verificationCode"
                placeholder="请输入验证码"
                :prefix-icon="Key"
                size="large"
            />
            <el-button
                type="primary"
                :disabled="isCountingDown"
                @click="sendVerificationCode"
                class="code-btn"
            >
              {{ countdown > 0 ? `${countdown}s后重试` : '获取验证码' }}
            </el-button>
          </div>
        </el-form-item>

        <el-checkbox v-model="agreeTerms" class="terms-check">
          我已阅读并同意<el-link type="primary" :underline="false">《用户协议》</el-link>
        </el-checkbox>

        <el-button
            type="primary"
            size="large"
            @click="handleRegister"
            :loading="loading"
            class="register-btn"
        >
          立即注册
        </el-button>

        <div class="login-link">
          已有账号？<el-link type="primary" :underline="false" @click="goToLogin">立即登录</el-link>
        </div>
      </el-form>
    </el-card>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'
import { ElMessage } from 'element-plus'
import { User, Lock, Message, Key } from '@element-plus/icons-vue'
import router from "@/router/index.js";

// 表单数据
const form = reactive({
  username: '',
  email: '',
  password: '',
  confirmPassword: '',
  verificationCode: ''
})

// 密码确认验证
const validatePassword = (rule, value, callback) => {
  if (value !== form.password) {
    callback(new Error('两次输入密码不一致!'))
  } else {
    callback()
  }
}

// 表单验证规则
const rules = reactive({
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' },
    { min: 3, max: 16, message: '长度在 3 到 16 个字符', trigger: 'blur' }
  ],
  email: [
    { required: true, message: '请输入邮箱地址', trigger: 'blur' },
    { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { min: 6, max: 20, message: '长度在 6 到 20 个字符', trigger: 'blur' }
  ],
  confirmPassword: [
    { required: true, message: '请再次输入密码', trigger: 'blur' },
    { validator: validatePassword, trigger: 'blur' }
  ],
  verificationCode: [
    { required: true, message: '请输入验证码', trigger: 'blur' },
    { len: 6, message: '验证码长度为6位', trigger: 'blur' }
  ]
})

// 其他状态
const agreeTerms = ref(false)
const loading = ref(false)
const registerForm = ref(null)
const countdown = ref(0)
const isCountingDown = computed(() => countdown.value > 0)



// 发送验证码
const sendVerificationCode = () => {
  if (!form.email) {
    ElMessage.warning('请输入邮箱地址')
    return
  }

  // 模拟发送验证码
  countdown.value = 60
  const timer = setInterval(() => {
    countdown.value--
    if (countdown.value <= 0) {
      clearInterval(timer)
    }
  }, 1000)

  ElMessage.success('验证码已发送')
}

// 注册方法
const handleRegister = async () => {
  try {
    if (!agreeTerms.value) {
      ElMessage.warning('请先同意用户协议')
      return
    }

    await registerForm.value.validate()
    loading.value = true

    // 模拟注册请求
    setTimeout(() => {
      ElMessage.success('注册成功')
      loading.value = false
      // 实际项目中这里进行路由跳转
    }, 1000)
  } catch (error) {
    console.log('表单验证失败:', error)
  }
}

// 跳转登录
const goToLogin = () => {
  // 实际项目中这里进行路由跳转
  router.push('/login')
}
</script>

<style scoped>
.register-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.register-box {
  width: 450px;
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
}

.register-title {
  text-align: center;
  color: #303133;
  margin-bottom: 40px;
  font-size: 24px;
  font-weight: 500;
}

.code-input {
  display: flex;
  gap: 12px;
}

.code-btn {
  width: 140px;
}

.terms-check {
  margin: 20px 0;
}

.register-btn {
  width: 100%;
  margin-top: 10px;
  letter-spacing: 2px;
}

.login-link {
  margin-top: 24px;
  text-align: center;
  color: #606266;
}

.el-link {
  font-weight: 500;
}
</style>