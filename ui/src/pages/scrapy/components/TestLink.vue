<template>
  <div class="test-url-page">
    <el-card class="main-card">
      <!-- 卡片头部 -->
      <div class="card-header">
        <h2 class="title">测试网址配置</h2>
        <el-radio-group v-model="spiderInfo.address.type" class="mode-switch" @change="handleChange">
          <el-radio-button label="direct" value="direct">直链记录</el-radio-button>
          <el-radio-button label="segment" value="segment">智能片段组合</el-radio-button>
        </el-radio-group>
      </div>

      <!-- 直链记录模式 -->
      <div v-if="spiderInfo.address.type === 'direct'" class="direct-mode">
        <el-input
            v-model="spiderInfo.address.links"
            placeholder="请输入单条测试网址，或用英文分号 ';' 分隔的多条网址"
            type="textarea"
            :rows="4"
            class="url-input"
        />
        <div class="instructions">
          <h3>使用说明</h3>
          <p>1. 输入单条测试网址，或使用分号分隔的多条网址。</p>
          <p>2. 系统会自动解析并记录所有网址。</p>
          <p>3. 支持直接粘贴网址，系统会自动校验格式。</p>
          <p>3. 提供网址仅测试使用，不建议输入过多网址，以免影响测试效率</p>
        </div>
      </div>

      <!-- 智能片段组合模式 -->
      <div v-else-if="spiderInfo.address.type === 'segment'" class="segment">
        <div class="base-url-input">
          <el-input
              v-model="spiderInfo.address.rule[0].baseURL"
              placeholder="请输入固定网址开头"
              class="segment-input"
          >
            <template #prepend>https://</template>
          </el-input>
        </div>

        <div class="segment-container">
          <div
              v-for="(segment, index) in spiderInfo.address.rule"
              :key="index"
              class="segment-group"
          >
            <template v-if="segment.type === 'fixed'">
              <el-input
                  v-model="segment.value"
                  placeholder="请输入固定链接部分"
                  class="segment-input fixed-input"
              >
                <template #prepend>/</template>
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
              @click="addFixedSegment"
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

const spiderInfo = defineModel('spiderInfo')

const handleChange = () => {
  if (spiderInfo.value.address.type === 'direct') {
    spiderInfo.value.address.rule = [
      { baseURL: "" }
    ]
  } else if (spiderInfo.value.address.type === 'segment') {
    spiderInfo.value.address.links = ""
  }
}

// 添加固定链接片段
const addFixedSegment = () => {
  if (spiderInfo.value.address.rule.length < 5) {
    spiderInfo.value.address.rule.push({
      type: 'fixed',
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

.instructions {
  padding: 20px;
  background-color: #f5f7fa;
  border-radius: 8px;
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