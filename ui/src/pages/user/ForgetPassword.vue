<template>
  <div class="forgot-password-container">
    <el-card class="password-card">
      <h2 class="title">找回密码</h2>
      <el-form
          ref="formRef"
          :model="form"
          :rules="rules"
          @keyup.enter="handleSubmit"
      >
        <!-- 邮箱输入 -->
        <el-form-item prop="email">
          <el-input
              v-model="form.email"
              placeholder="请输入注册邮箱"
              :prefix-icon="Message"
              size="large"
          />
        </el-form-item>

        <!-- 验证码 -->
        <el-form-item prop="code">
          <div class="code-input">
            <el-input
                v-model="form.code"
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

        <!-- 新密码 -->
        <el-form-item prop="newPassword">
          <el-input
              v-model="form.newPassword"
              type="password"
              placeholder="请输入新密码"
              show-password
              :prefix-icon="Lock"
              size="large"
          />
        </el-form-item>

        <!-- 确认密码 -->
        <el-form-item prop="confirmPassword">
          <el-input
              v-model="form.confirmPassword"
              type="password"
              placeholder="请确认新密码"
              show-password
              :prefix-icon="Lock"
              size="large"
          />
        </el-form-item>

        <el-button
            type="primary"
            size="large"
            @click="handleSubmit"
            :loading="loading"
            class="submit-btn"
        >
          重置密码
        </el-button>
      </el-form>

      <div class="footer">
        <el-link type="primary" :underline="false" @click="goToLogin">
          ← 返回登录
        </el-link>
      </div>
    </el-card>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'
import { ElMessage } from 'element-plus'
import { Message, Key, Lock } from '@element-plus/icons-vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// 表单数据
const form = reactive({
  email: '',
  code: '',
  newPassword: '',
  confirmPassword: ''
})

// 表单验证规则
const rules = reactive({
  email: [
    { required: true, message: '请输入邮箱地址', trigger: 'blur' },
    { type: 'email', message: '请输入正确的邮箱格式', trigger: ['blur', 'change'] }
  ],
  code: [
    { required: true, message: '请输入验证码', trigger: 'blur' },
    { len: 6, message: '验证码长度为6位', trigger: 'blur' }
  ],
  newPassword: [
    { required: true, message: '请输入新密码', trigger: 'blur' },
    { min: 8, message: '密码长度至少8位', trigger: 'blur' },
    { pattern: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$/,
      message: '需包含大小写字母和数字', trigger: 'blur' }
  ],
  confirmPassword: [
    { required: true, message: '请确认新密码', trigger: 'blur' },
    { validator: validateConfirmPassword, trigger: 'blur' }
  ]
})

// 状态管理
const loading = ref(false)
const countdown = ref(0)
const isCountingDown = computed(() => countdown.value > 0)
const formRef = ref(null)

// 密码确认验证
const validateConfirmPassword = (rule, value, callback) => {
  if (value !== form.newPassword) {
    callback(new Error('两次输入的密码不一致'))
  } else {
    callback()
  }
}

// 发送验证码
const sendVerificationCode = async () => {
  try {
    // 简单验证邮箱格式
    if (!/^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/.test(form.email)) {
      ElMessage.warning('请输入有效的邮箱地址')
      return
    }

    // 模拟API调用
    await new Promise(resolve => setTimeout(resolve, 1000))

    // 开始倒计时
    countdown.value = 60
    const timer = setInterval(() => {
      countdown.value--
      if (countdown.value <= 0) {
        clearInterval(timer)
      }
    }, 1000)

    ElMessage.success('验证码已发送至邮箱')
  } catch (error) {
    ElMessage.error('验证码发送失败，请稍后重试')
  }
}

// 提交表单
const handleSubmit = async () => {
  try {
    await formRef.value.validate()
    loading.value = true

    // 模拟API调用
    await new Promise(resolve => setTimeout(resolve, 1500))

    ElMessage.success('密码重置成功')
    router.push('/login')
  } catch (error) {
    console.error('表单验证失败:', error)
  } finally {
    loading.value = false
  }
}

// 返回登录
const goToLogin = () => {
  router.push('/login')
}
</script>

<style scoped>
.forgot-password-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.password-card {
  width: 450px;
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
}

.title {
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

.submit-btn {
  width: 100%;
  margin-top: 20px;
  letter-spacing: 2px;
}

.footer {
  margin-top: 24px;
  text-align: center;
}

.el-link {
  font-weight: 500;
}
</style>