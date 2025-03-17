<template>
  <div class="data-overview">
    <el-row :gutter="20" style="margin-bottom: 20px;">
      <!-- 每个卡片代表一个数据集 -->
      <el-col :span="8" v-for="(dataset, index) in datasets" :key="index">
        <el-card shadow="hover" class="dataset-card" @click="showDetailedReport(dataset)">
          <div slot="header" class="clearfix">
            <span>{{ dataset.name }}</span>
          </div>
          <div :id="'chart-' + index" style="height: 150px;"></div>
        </el-card>
      </el-col>
    </el-row>

    <!-- 详细报告对话框 -->
    <el-dialog :title="selectedDataset.name" :visible.sync="dialogVisible" width="60%">
      <h4>情感分析详情</h4>
      <p>积极: {{ selectedDataset.sentiment.positive }}%</p>
      <p>消极: {{ selectedDataset.sentiment.negative }}%</p>
      <p>未分析: {{ selectedDataset.sentiment.unanalyzed }}%</p>
      <div ref="detailedChartContainer" id="detailed-chart" style="height: 400px;"></div>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import * as echarts from 'echarts';

// 模拟数据集
const datasets = [
  {
    name: '数据集 A',
    sentiment: {
      positive: 60,
      negative: 30,
      unanalyzed: 10
    }
  },
  {
    name: '数据集 B',
    sentiment: {
      positive: 70,
      negative: 20,
      unanalyzed: 10
    }
  },
  {
    name: '数据集 C',
    sentiment: {
      positive: 50,
      negative: 40,
      unanalyzed: 10
    }
  }
];

const dialogVisible = ref(false);
const selectedDataset = ref({});

// 初始化图表
onMounted(() => {
  datasets.forEach((dataset, index) => {
    const chartId = 'chart-' + index;
    initChart(chartId, dataset.sentiment);
  });
});

// 初始化 ECharts 图表
function initChart(id, sentiment) {
  const chartDom = document.getElementById(id);
  const chart = echarts.init(chartDom);
  const option = {
    title: {
      text: '情感分析结果',
      left: 'center'
    },
    tooltip: {
      trigger: 'item'
    },
    legend: {
      show: false
    },
    series: [
      {
        name: '情感分布',
        type: 'pie',
        radius: ['50%', '70%'],
        avoidLabelOverlap: false,
        label: {
          show: false,
          position: 'center'
        },
        emphasis: {
          label: {
            show: true,
            fontSize: '20',
            fontWeight: 'bold'
          }
        },
        labelLine: {
          show: false
        },
        data: [
          { value: sentiment.positive, name: '积极' },
          { value: sentiment.negative, name: '消极' },
          { value: sentiment.unanalyzed, name: '未分析' }
        ]
      }
    ]
  };
  chart.setOption(option);
}

// 显示详细报告
function showDetailedReport(dataset) {
  selectedDataset.value = dataset;
  dialogVisible.value = true;

  // 初始化详细图表
  nextTick(() => {
    const detailedChartDom = document.getElementById('detailed-chart');
    const detailedChart = echarts.init(detailedChartDom);
    const detailedOption = {
      title: {
        text: '详细情感分析结果',
        left: 'center'
      },
      tooltip: {
        trigger: 'item'
      },
      legend: {
        orient: 'vertical',
        left: 'left'
      },
      series: [
        {
          name: '情感分布',
          type: 'pie',
          radius: '50%',
          data: [
            { value: dataset.sentiment.positive, name: '积极' },
            { value: dataset.sentiment.negative, name: '消极' },
            { value: dataset.sentiment.unanalyzed, name: '未分析' }
          ],
          emphasis: {
            itemStyle: {
              shadowBlur: 10,
              shadowOffsetX: 0,
              shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
          }
        }
      ]
    };
    detailedChart.setOption(detailedOption);
  });
}
</script>

<style scoped>
.data-overview {
  padding: 20px;
}

.dataset-card {
  margin-bottom: 20px;
  cursor: pointer;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both;
}

.el-card__body {
  padding: 10px;
}

#detailed-chart {
  margin-top: 20px;
}
</style>