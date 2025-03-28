<template>
  <div class="task-management">
    <!-- 任务筛选 -->
    <div class="task-filter">
      <el-radio-group v-model="filterStatus" @change="filterTasks">
        <el-radio-button label="全部" value="全部" />
        <el-radio-button label="未开始" value="未开始"/>
        <el-radio-button label="进行中" value="进行中"/>
        <el-radio-button label="已完成" value="已完成"/>
      </el-radio-group>
    </div>

    <!-- 任务列表 -->
    <div class="task-list">
      <!-- 任务卡片 -->
      <div
          v-for="task in filteredTasks"
          :key="task.id"
          class="task-card"
          :class="`task-card--${task.status}`"
      >
        <div class="task-header">
          <h3 class="task-name">{{ task.name }}</h3>
          <el-tag :type="getStatusTagType(task.status)" size="small">
            {{ task.status }}
          </el-tag>
        </div>
        <div class="task-actions">
          <el-button v-if="task.status === '未开始'" type="primary" @click="startTask(task.id)">
            开始
          </el-button>
          <el-button v-if="task.status === '进行中'" type="warning" @click="completeTask(task.id)">
            结束
          </el-button>
          <el-button type="info" @click="viewDetails(task.id)">
            详情
          </el-button>
        </div>
      </div>

      <!-- 创建任务卡片 -->
      <div class="task-card create-task-card" @click="createTask">
        <el-icon :size="40" class="add-icon">
          <Plus />
        </el-icon>
        <p>创建任务</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import {ref, computed} from 'vue'
import {Plus} from '@element-plus/icons-vue'

// 任务数据
const tasks = ref([
  {id: 1, name: '测试任务1', spiders: [], status: '未开始'},
  {id: 2, name: '测试任务2', spiders: [], status: '进行中'},
  {id: 3, name: '测试任务3', spiders: [], status: '已完成'},
  {id: 4, name: '测试任务4', spiders: [], status: '未开始'}
])

// 当前筛选状态
const filterStatus = ref('全部')

// 根据筛选状态过滤任务
const filteredTasks = computed(() => {
  if (filterStatus.value === '全部') {
    return tasks.value
  }
  return tasks.value.filter(task => task.status === filterStatus.value)
})

// 开始任务
const startTask = (taskId) => {
  const task = tasks.value.find(task => task.id === taskId)
  if (task) {
    task.status = '进行中'
  }
}

// 完成任务
const completeTask = (taskId) => {
  const task = tasks.value.find(task => task.id === taskId)
  if (task) {
    task.status = '已完成'
  }
}

// 查看任务详情
const viewDetails = (taskId) => {
  console.log('查看任务详情:', taskId)
  // 这里可以跳转到任务详情页
}

// 创建任务
const createTask = () => {
  console.log('创建任务')
  // 这里可以打开创建任务的弹窗或跳转到创建任务页面
}

// 根据任务状态获取标签类型
const getStatusTagType = (status) => {
  switch (status) {
    case '未开始':
      return 'info'
    case '进行中':
      return 'warning'
    case '已完成':
      return 'success'
    default:
      return ''
  }
}
</script>

<style scoped>
.task-management {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.task-filter {
  margin-bottom: 20px;
}

.task-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.task-card {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  padding: 20px;
  width: 300px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.task-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
}

.task-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.task-name {
  font-size: 1.25rem;
  color: #333;
  margin: 0;
}

.task-actions {
  display: flex;
  gap: 10px;
}

.create-task-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  background-color: #f5f7fa;
  border: 2px dashed #409EFF;
}

.create-task-card:hover {
  background-color: #ebf5ff;
}

.add-icon {
  color: #409EFF;
  margin-bottom: 10px;
}

/* 不同状态的卡片样式 */
.task-card--未开始 {
  border-left: 4px solid #409EFF; /* 蓝色边框 */
}

.task-card--进行中 {
  border-left: 4px solid #e6a23c; /* 橙色边框 */
}

.task-card--已完成 {
  border-left: 4px solid #67c23a; /* 绿色边框 */
}
</style>