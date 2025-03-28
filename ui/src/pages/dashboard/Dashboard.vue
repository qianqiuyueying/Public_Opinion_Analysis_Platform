<template>
  <div class="dashboard-container">
    <el-row :gutter="20">
      <!-- 左侧爬虫信息列 -->
      <el-col :xs="24" :sm="12" :lg="8">
        <el-card class="info-card">
          <template #header>
            <div class="card-header">
              <span>爬虫管理</span>
              <el-button type="primary" @click="toSpiderManage">前往</el-button>
            </div>
          </template>
          <div v-for="spider in spiders" :key="spider.id" class="item-card">
            <el-card shadow="hover">
              <div class="spider-info">
                <div class="meta">
                  <h4>{{ spider.name }}</h4>
                  <el-button type="text">详情</el-button>
                </div>
                <el-text>{{ spider.description }}</el-text>
              </div>
            </el-card>
          </div>
        </el-card>
      </el-col>

      <!-- 中间任务信息列 -->
      <el-col :xs="24" :sm="12" :lg="8">
        <el-card class="info-card">
          <template #header>
            <div class="card-header">
              <span>任务管理</span>
              <el-button type="info" @click="toTaskManage">前往</el-button>
            </div>
          </template>
          <div v-for="task in tasks" :key="task.id" class="item-card">
            <el-card shadow="hover">
              <div class="task-info">
                <div class="meta">
                  <h4>{{ task.name }}</h4>
                  <el-tag :type="getStatusColor(task.status)" size="small">
                    {{ task.status }}
                  </el-tag>
                </div>
                <el-progress
                    :percentage="task.progress"
                    :status="getProgressStatus(task.status)"
                    :stroke-width="16"
                />
                <div class="stats">
                  <span>启动时间：{{ task.startTime }}</span>
                  <span>持续时间：{{ task.duration }}</span>
                </div>
              </div>
            </el-card>
          </div>
        </el-card>
      </el-col>

      <!-- 右侧数据集分析列 -->
      <el-col :xs="24" :sm="24" :lg="8">
        <el-card class="info-card">
          <template #header>
            <div class="card-header">
              <span>情感分析</span>
              <el-button type="success" @click="toAnalytics">前往</el-button>
            </div>
          </template>
          <div v-for="dataset in datasets" :key="dataset.id" class="item-card">
            <el-card shadow="hover">
              <div class="dataset-info">
                <h4>{{ dataset.taskName }}</h4>
                <div class="chart-container">
                  <div :id="'chart-'+dataset.id" class="sentiment-chart"></div>
                </div>
                <div class="legend">
                  <span class="positive"><i class="dot" /> 正向 {{ dataset.sentiment.positive }}%</span>
                  <span class="neutral"><i class="dot" /> 中立 {{ dataset.sentiment.neutral }}%</span>
                  <span class="negative"><i class="dot" /> 负向 {{ dataset.sentiment.negative }}%</span>
                </div>
              </div>
            </el-card>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import * as echarts from 'echarts'
import router from '@/router/index.js'

// 前往爬虫管理页面
const toSpiderManage = () => {
  router.push('/layout/scrapy/spider')
}

// 前往任务管理页面
const toTaskManage = () => {
  router.push('/layout/scrapy/task')
}

// 前往情感分析页面
const toAnalytics = () => {
  router.push('/layout/analytics/details')
}

// 状态颜色映射
const statusColorMap = {
  '运行中': 'success',
  '已停止': 'info',
  '异常': 'danger',
  '已完成': 'primary',
  '排队中': 'warning'
}

// 响应式数据
const spiders = ref([
  {
    id: 1,
    name: '微博舆情爬虫',
    description: '实时采集微博热点话题',
  },
  {
    id: 2,
    name: '微博舆情爬虫',
    description: '实时采集微博热点话题',

  },
  {
    id: 3,
    name: '微博舆情爬虫',
    description: '实时采集微博热点话题',
  },
  {
    id: 3,
    name: '微博舆情爬虫',
    description: '实时采集微博热点话题',
  }
])

const tasks = ref([
  {
    id: 1,
    name: '七月舆情周报',
    status: '进行中',
    progress: 65,
    startTime: '2023-07-20 09:00',
    duration: '3小时15分'
  },
  {
    id: 2,
    name: '七月舆情周报',
    status: '进行中',
    progress: 65,
    startTime: '2023-07-20 09:00',
    duration: '3小时15分'
  },
  {
    id: 3,
    name: '七月舆情周报',
    status: '进行中',
    progress: 65,
    startTime: '2023-07-20 09:00',
    duration: '3小时15分'
  },
])

const datasets = ref([
  {
    id: 1,
    taskName: '七月第三周数据集',
    sentiment: { positive: 62, neutral: 28, negative: 10 }
  },
  {
    id: 2,
    taskName: '七月第三周数据集',
    sentiment: { positive: 62, neutral: 28, negative: 10 }
  },
])

// 图表实例存储
const charts = ref([])

// 生命周期钩子
onMounted(() => {
  initCharts()
  window.addEventListener('resize', handleResize)
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', handleResize)
  charts.value.forEach(chart => chart.dispose())
})

// 方法
const getStatusColor = (status) => statusColorMap[status] || 'info'

const getProgressStatus = (status) => status === '异常' ? 'exception' : null

const initCharts = () => {
  datasets.value.forEach(dataset => {
    const chartDom = document.getElementById(`chart-${dataset.id}`)
    if (!chartDom) return

    const chart = echarts.init(chartDom)
    chart.setOption({
      color: ['#67C23A', '#909399', '#F56C6C'],
      tooltip: {
        trigger: 'item',
        formatter: '{b}: {c}%'
      },
      series: [{
        type: 'pie',
        radius: ['40%', '70%'],
        avoidLabelOverlap: false,
        itemStyle: {
          borderRadius: 5,
          borderColor: '#fff',
          borderWidth: 2
        },
        label: {
          show: false,
          position: 'center'
        },
        emphasis: {
          label: {
            show: true,
            fontSize: '14',
            fontWeight: 'bold'
          }
        },
        data: [
          { value: dataset.sentiment.positive, name: '正向' },
          { value: dataset.sentiment.neutral, name: '中立' },
          { value: dataset.sentiment.negative, name: '负向' }
        ]
      }]
    })
    charts.value.push(chart)
  })
}

const handleResize = () => {
  charts.value.forEach(chart => chart.resize())
}
</script>

<style scoped>
/* 保持原有样式不变 */
.dashboard-container {
  padding: 10px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.item-card {
  margin-bottom: 15px;
}

.meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.stats {
  display: flex;
  justify-content: space-between;
  font-size: 0.9em;
  color: #666;
  margin-top: 10px;
}

.chart-container {
  height: 180px;
  margin: 15px 0;
}

.legend {
  display: flex;
  justify-content: space-around;
  font-size: 0.9em;
}

.legend span {
  display: flex;
  align-items: center;
}

.dot {
  display: inline-block;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  margin-right: 5px;
}

.positive .dot { background: #67C23A; }
.neutral .dot { background: #909399; }
.negative .dot { background: #F56C6C; }

.sentiment-chart {
  width: 100%;
  height: 100%;
}
</style>