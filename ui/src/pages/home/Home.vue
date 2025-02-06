<template>
  <div class="home-container">
    <!-- 数据概览 -->
    <el-row :gutter="20" class="overview-row">
      <el-col :span="6">
        <el-card class="overview-card">
          <div class="card-content">
            <span class="card-label">总舆情数</span>
            <span class="card-value">12,345</span>
            <el-icon :size="40" class="card-icon"><TrendCharts /></el-icon>
          </div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card class="overview-card">
          <div class="card-content">
            <span class="card-label">正面舆情</span>
            <span class="card-value">8,765</span>
            <el-icon :size="40" class="card-icon"><SuccessFilled /></el-icon>
          </div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card class="overview-card">
          <div class="card-content">
            <span class="card-label">负面舆情</span>
            <span class="card-value">1,234</span>
            <el-icon :size="40" class="card-icon"><WarningFilled /></el-icon>
          </div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card class="overview-card">
          <div class="card-content">
            <span class="card-label">今日新增</span>
            <span class="card-value">567</span>
            <el-icon :size="40" class="card-icon"><DataLine /></el-icon>
          </div>
        </el-card>
      </el-col>
    </el-row>

    <!-- 舆情趋势图 -->
    <el-card class="chart-card">
      <template #header>
        <span class="card-title">舆情趋势图</span>
      </template>
      <div ref="chartRef" class="chart-container"></div>
    </el-card>

    <!-- 热门话题和最新动态 -->
    <el-row :gutter="20" class="bottom-row">
      <el-col :span="12">
        <el-card class="list-card">
          <template #header>
            <span class="card-title">热门话题</span>
          </template>
          <el-table :data="hotTopics" style="width: 100%">
            <el-table-column prop="rank" label="排名" width="80" />
            <el-table-column prop="topic" label="话题" />
            <el-table-column prop="count" label="讨论量" width="120" />
          </el-table>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card class="list-card">
          <template #header>
            <span class="card-title">最新动态</span>
          </template>
          <el-timeline>
            <el-timeline-item
                v-for="(event, index) in latestEvents"
                :key="index"
                :timestamp="event.time"
            >
              {{ event.content }}
            </el-timeline-item>
          </el-timeline>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import * as echarts from 'echarts'
import {
  TrendCharts,
  SuccessFilled,
  WarningFilled,
  DataLine,
} from '@element-plus/icons-vue'

// 舆情趋势图
const chartRef = ref(null)
let chartInstance = null

// 初始化图表
const initChart = () => {
  chartInstance = echarts.init(chartRef.value)
  const option = {
    tooltip: {
      trigger: 'axis',
    },
    xAxis: {
      type: 'category',
      data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日'],
    },
    yAxis: {
      type: 'value',
    },
    series: [
      {
        name: '舆情数量',
        type: 'line',
        data: [120, 200, 150, 80, 70, 110, 130],
        smooth: true,
      },
    ],
  }
  chartInstance.setOption(option)
}

// 热门话题数据
const hotTopics = ref([
  { rank: 1, topic: '某品牌新品发布', count: 1234 },
  { rank: 2, topic: '某事件引发热议', count: 987 },
  { rank: 3, topic: '某明星动态', count: 765 },
  { rank: 4, topic: '某政策解读', count: 543 },
  { rank: 5, topic: '某行业趋势', count: 321 },
])

// 最新动态数据
const latestEvents = ref([
  { time: '2023-10-01 12:00', content: '新增舆情 123 条' },
  { time: '2023-10-01 10:00', content: '用户 A 发布了新话题' },
  { time: '2023-10-01 09:30', content: '系统完成数据更新' },
  { time: '2023-10-01 08:00', content: '新增负面舆情 10 条' },
])

// 组件挂载后初始化图表
onMounted(() => {
  initChart()
})
</script>

<style scoped>
.home-container {
  padding: 20px;
}

.overview-row {
  margin-bottom: 20px;
}

.overview-card {
  height: 120px;
}

.card-content {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  position: relative;
}

.card-label {
  font-size: 14px;
  color: #666;
}

.card-value {
  font-size: 24px;
  font-weight: bold;
  margin: 10px 0;
}

.card-icon {
  position: absolute;
  right: 20px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--el-color-primary);
}

.chart-card {
  margin-bottom: 20px;
}

.chart-container {
  height: 300px;
}

.bottom-row {
  margin-top: 20px;
}

.list-card {
  height: 400px;
}

.card-title {
  font-size: 18px;
  font-weight: bold;
}
</style>