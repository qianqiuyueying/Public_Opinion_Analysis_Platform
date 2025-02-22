<template>
  <div class="rule-definition-page">
    <!-- 爬取结果预览区 -->
    <el-card class="preview-card">
      <h3 class="preview-title">爬取结果预览</h3>
      <div class="preview-content">
        <el-input
            v-model="previewContent"
            type="textarea"
            :rows="19"
            placeholder="爬取结果将显示在这里"
            readonly
        />
      </div>
    </el-card>

    <!-- 爬取规则制定区 -->
    <el-card class="rule-card">
      <h3 class="rule-title">爬取规则制定</h3>
      <div class="rule-content">
        <!-- 规则步骤列表 -->
        <div class="rule-steps">
          <div
              v-for="(step, index) in spiderInfo.rules"
              :key="index"
              class="step-item"
          >
            <el-input
                v-model="step.content"
                placeholder="请输入规则内容"
                class="step-input"
            >
              <template #prepend>
                {{ step.type }}
              </template>
            </el-input>
          </div>
        </div>
      </div>
      <div class="actions">
        <el-button type="success" @click="addSelectStep">选取</el-button>
        <el-button type="primary" @click="addActionStep">动作</el-button>
        <el-button type="warning" @click="addListenStep">监听</el-button>
        <el-button type="danger" @click="removeStep">删除</el-button>
        <el-button type="info" @click="handlePreview">预览</el-button>
      </div>
    </el-card>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { ElMessage } from 'element-plus';

const spiderInfo = defineModel('spiderInfo')

// 添加选取步骤
const addSelectStep = () => {
  spiderInfo.value.rules.push({ type: 'select', content: '' });
};

// 添加动作步骤
const addActionStep = () => {
  spiderInfo.value.rules.push({ type: 'action', content: '' });
};

// 添加监听步骤
const addListenStep = () => {
  spiderInfo.value.rules.push({ type: 'listen', content: '' });
};

// 删除步骤
const removeStep = () => {
  if (spiderInfo.value.rules.length > 0) {
    spiderInfo.value.rules.pop();
  } else {
    ElMessage.warning("真的没有步骤了啊！！");
  }
};

// 获取预览结果
const handlePreview = () => {

}

// 爬取结果预览内容
const previewContent = ref('');
</script>

<style scoped>
.rule-definition-page {
  display: flex;
  gap: 20px;
  padding: 20px;
}

.preview-card {
  flex: 2;
}

.rule-card {
  flex: 1;
  max-height: 486px; /* 设置最大高度 */
  overflow-y: auto; /* 自动出现滚动条 */
}

.preview-title,
.rule-title {
  margin-top: 0;
  margin-bottom: 10px;
}

.preview-content {
  height: 100%;
}

.rule-content {
  display: flex;
  flex-direction: column;
  gap: 8px; /* 调整步骤之间的间距 */
}

.rule-steps {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.step-item {
  border: 1px solid #e4e7ed;
  border-radius: 8px;
  padding: 5px; /* 调整内边距 */
  background-color: #f5f7fa;
  display: flex;
  align-items: center;
}

.step-input {
  flex: 1;
}

.actions {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}
</style>