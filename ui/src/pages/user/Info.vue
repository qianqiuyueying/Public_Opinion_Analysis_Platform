<template>
  <el-card class="user-info-card">
    <template #header>
      <div class="card-header">
        <span>用户信息</span>
      </div>
    </template>
    <el-row :gutter="20">
      <!-- 左侧：用户头像 -->
      <el-col :span="6">
        <div class="avatar-container">
          <el-avatar :size="120" :src="user.avatar"  />
        </div>
      </el-col>
      <!-- 右侧：用户详细信息 -->
      <el-col :span="18">
        <el-descriptions :column="1" border>
          <el-descriptions-item label="用户ID">
            <span class="info-text">{{ user.id  }}</span>
          </el-descriptions-item>
          <el-descriptions-item label="用户名">
            <span class="info-text">{{ user.username  }}</span>
          </el-descriptions-item>
          <el-descriptions-item label="邮箱">
            <span class="info-text">{{ user.email  }}</span>
          </el-descriptions-item>
          <el-descriptions-item label="创建时间">
            <span class="info-text">{{ formatDate(user.create_at)  }}</span>
          </el-descriptions-item>
          <el-descriptions-item label="最近更新时间">
            <span class="info-text">{{ formatDate(user.update_at)  }}</span>
          </el-descriptions-item>
          <el-descriptions-item label="上次登录时间">
            <span class="info-text">{{ formatDate(user.last_login)  }}</span>
          </el-descriptions-item>
          <el-descriptions-item label="角色">
            <span class="info-text">{{ user.role  }}</span>
          </el-descriptions-item>
        </el-descriptions>
      </el-col>
    </el-row>
  </el-card>
</template>

<script setup>
import { ref } from 'vue';

// 模拟用户数据
const user = ref({
  id: 1,
  username: 'JohnDoe',
  avatar: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png',
  email: 'johndoe@example.com',
  password: '********', // 密码通常不直接展示
  create_at: '2023-01-01T12:00:00Z',
  update_at: '2025-03-10T15:30:00Z',
  last_login: '2025-03-12T10:00:00Z',
  role: '管理员'
});

// 格式化日期时间
const formatDate = (dateString) => {
  const date = new Date(dateString);
  return date.toLocaleString();
};
</script>

<style scoped>
.user-info-card {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
}

.card-header {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 20px;
}

.avatar-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.info-text {
  font-size: 14px;
  color: #606266;
}

.el-descriptions {
  margin-top: 10px;
}

.el-descriptions-item {
  padding: 10px;
}
</style>