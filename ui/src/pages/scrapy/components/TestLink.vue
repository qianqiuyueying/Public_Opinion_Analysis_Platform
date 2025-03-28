<template>
  <div class="test-url-page">
    <el-card class="main-card">
      <!-- 卡片头部 -->
      <div class="card-header">
        <h2 class="title">
          测试网址配置
        </h2>
        <el-radio-group v-model="spiderInfo.address.type" class="mode-switch" @change="handleChange">
          <el-tooltip placement="top">
            <template #content>
              <div>
                请输入所有目标网址，多个网址之间使用英文分号（;）分隔。<br>
                例如：https://example.com;https://example.org
              </div>
            </template>
            <el-radio-button label="direct" value="direct">直链记录</el-radio-button>
          </el-tooltip>

          <el-tooltip placement="top">
            <template #content>
              <div>
                通过编辑规则，自动生成多条目标网址。<br>
                适用于需要批量生成网址的场景。
              </div>
            </template>
            <el-radio-button label="segment" value="segment">智能片段组合</el-radio-button>
          </el-tooltip>
        </el-radio-group>
      </div>

      <!-- 直链记录模式 -->
      <div v-if="spiderInfo.address.type === 'direct'" class="direct-mode">
        <el-input
            v-model="spiderInfo.address.links"
            placeholder="请输入单条测试网址，或用英文分号加回车 ';' 分隔的多条网址"
            type="textarea"
            :rows="14"
            class="url-input"
        />
      </div>

      <!-- 智能片段组合模式 -->
      <div v-else-if="spiderInfo.address.type === 'segment'" class="segment">
        <div class="base-url-input">
          <el-input
              v-model="spiderInfo.address.rule[0].value"
              placeholder="请输入固定网址开头"
              class="segment-input"
          >
          </el-input>
        </div>

        <div class="segment-container">
          <div
              v-for="(segment, index) in spiderInfo.address.rule"
              :key="index"
              class="segment-group"
          >
            <template v-if="segment.type === 'URLSegment'">
              <el-input
                  v-model="segment.value"
                  placeholder="请输入固定链接部分"
                  class="segment-input fixed-input"
              >
              </el-input>
            </template>
            <template v-else-if="segment.type === 'loop'">
              <el-input-number
                  v-model="segment.min"
                  placeholder="最小值"
                  class="segment-input loop-input"
                  controls-position="right"
              >
                <template #prefix>最小值</template>
              </el-input-number>
              <el-input-number
                  v-model="segment.max"
                  placeholder="最大值"
                  class="segment-input loop-input"
                  controls-position="right"
              >
                <template #prefix>最大值</template>
              </el-input-number>
              <el-input-number
                  v-model="segment.step"
                  placeholder="步长"
                  class="segment-input loop-input"
                  controls-position="right"
              >
                <template #prefix>步长</template>
              </el-input-number>
            </template>
          </div>
        </div>

        <!-- 固定在底部的按钮 -->
        <div class="fixed-button-container">
          <el-button
              type="primary"
              @click="addURLSegment"
              :disabled="spiderInfo.address.rule.length >= 5"
          >
            添加固定链接
          </el-button>
          <el-button
              type="success"
              @click="addLoopSegment"
              :disabled="spiderInfo.address.rule.length >= 5"
          >
            添加数字循环
          </el-button>
          <el-button
              type="danger"
              @click="removeLastSegment"
              :disabled="spiderInfo.address.rule.length === 1"
          >
            删除最后一个片段
          </el-button>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script setup>
import {ref} from 'vue'
import Tips from "@/components/Tips.vue";

const spiderInfo = defineModel('spiderInfo')

const tipContent = ref("测试提示")

const handleChange = () => {
  if (spiderInfo.value.address.type === 'direct') {
    spiderInfo.value.address.rule = [
      {
        type: "baseURL",
        value: ""
      }
    ]
  } else if (spiderInfo.value.address.type === 'segment') {
    spiderInfo.value.address.links = ""
  }
}

// 添加固定链接片段
const addURLSegment = () => {
  if (spiderInfo.value.address.rule.length < 5) {
    spiderInfo.value.address.rule.push({
      type: 'URLSegment',
      value: '',
    })
  }
}

// 添加数字循环片段
const addLoopSegment = () => {
  if (spiderInfo.value.address.rule.length < 5) {
    spiderInfo.value.address.rule.push({
      type: 'loop',
      min: 1,
      max: 10,
      step: 1
    })
  }
}

// 删除最后一个片段
const removeLastSegment = () => {
  if (spiderInfo.value.address.rule.length > 1) {
    spiderInfo.value.address.rule.pop()
  }
}
</script>

<style scoped>
.test-url-page {
  padding: 20px;
}

.main-card {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  position: relative; /* 为固定按钮容器提供定位上下文 */
  min-height: 420px; /* 确保卡片有足够的高度 */
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.title {
  margin: 0;
}

.mode-switch {
  margin-left: 20px;
}

.direct-mode {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.url-input {
  margin-bottom: 20px;
}


.instructions h3 {
  margin-top: 0;
}

.segment {
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding-bottom: 80px; /* 为固定按钮容器留出空间 */
}

.base-url-input {
  margin-bottom: 20px;
}

.segment-container {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.segment-group {
  display: flex;
  gap: 10px;
}

.segment-input {
  flex: 1;
}

.fixed-input {
  background-color: #f0f9eb; /* 浅绿色背景 */
  border-color: #c2e7b0; /* 浅绿色边框 */
}

.loop-input {
  background-color: #f9f0f0; /* 浅红色背景 */
  border-color: #f5caca; /* 浅红色边框 */
}

.fixed-button-container {
  position: absolute; /* 固定在卡片底部 */
  bottom: 20px;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  gap: 10px;
  padding: 0 20px; /* 左右留出间距 */
}
</style>