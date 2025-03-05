<template>
  <div class="rule-definition-page">
    <!-- 左栏：添加选取规则 -->
    <el-card class="left-panel">
      <h3>添加选取规则</h3>
      <div
          class="rule-section"
          v-for="(item, index) in selectorList"
          :key="index"
      >
        <template v-if="item.type === 'Root'">
          <el-input
              v-model="item.rules"
              readonly>
            <template #prepend>
              <el-select
                  v-model="item.type"
                  style="width: 125px"
                  disabled>
                <el-option
                    v-for="i in selectorType"
                    :key="i.value"
                    :label="i.label"
                    :value="i.value"/>
              </el-select>
            </template>
          </el-input>
        </template>
        <template v-else-if="item.type === 'elementSelector' || item.type === 'jsonSelector'">
          <el-input-tag
              v-model="item.rules">
            <template #prefix>
              <el-select
                  v-model="item.type"
                  style="width: 125px">
                <el-option
                    v-for="i in selectorType"
                    :key="i.value"
                    :label="i.label"
                    :value="i.value"/>
              </el-select>
            </template>
          </el-input-tag>
        </template>
        <template v-else-if="item.type === 'APISelector'">
          <el-input
              v-model="item.rules">
            <template #prepend>
              <el-select
                  v-model="item.type"
                  style="width: 125px">
                <el-option
                    v-for="i in selectorType"
                    :key="i.value"
                    :label="i.label"
                    :value="i.value"/>
              </el-select>
            </template>
          </el-input>
        </template>
      </div>

      <!-- 添加/删除按钮 -->
      <div class="action-buttons">
        <el-button type="primary" @click="handleAddSelector">添加规则</el-button>
        <el-button type="danger" @click="handleRemoveSelector">删除规则</el-button>
      </div>
    </el-card>

    <!-- 右栏：规则制定 -->
    <el-card class="right-panel">
      <h3>规则制定</h3>

      <!-- 规则步骤列表 -->
      <div class="rule-steps">
        <!-- 使用 v-for 遍历生成多行 -->
        <div v-for="(step, index) in spiderInfo.rules" :key="index" class="step-row">
          <span class="show-text">源：</span>
          <el-select
              v-model="step.source"
              style="margin-right: 15px">
            <el-option
                v-for="(item, i) in selectorList"
                :key="i"
                :label="String(item.rules)"
                :value="item.rules.length !== 0 ? item.rules : '未填写'"/>
          </el-select>
          <span class="show-text">操作：</span>
          <el-select v-model="step.operate">
            <el-option
                v-for="(item, i) in partialOperationList"
                :key="i"
                :label="item.label"
                :value="item.value"/>

            <el-option v-for="(item, i) in selectorList"
                       :key="i"
                       :label="item.rules.length !== 0 ? String(item.rules) : '未填写'"
                       :value="item.rules"/>
          </el-select>
        </div>
      </div>
      <!-- 添加/删除按钮 -->
      <div class="action-buttons">
        <el-button type="primary" @click="handleAddRules">添加规则</el-button>
        <el-button type="danger" @click="handleRemoveRules">删除规则</el-button>
      </div>
    </el-card>
  </div>
</template>

<script setup>
import {ref} from 'vue'

const spiderInfo = defineModel('spiderInfo')

// 选择器类型
const selectorType = ref([
  {"value": "elementSelector", "label": "元素选择器"},
  {"value": "jsonSelector", "label": "JSON选择器"},
  {"value": "APISelector", "label": "监听API"}
])
// 已创建的选择器
const selectorList = ref([
  {
    "type": "Root",
    "rules": "root"
  }
])
// 部分操作的列表
const partialOperationList = ref([
  {'label': "点击", 'value': "click"},
  {'label': "滚动", 'value': "scroll"},
  {'label': "监听", "value": "listen"}
])


// 添加规则的方法
const handleAddRules = () => {
  spiderInfo.value.rules.push({'source': "root", 'operate': ""})
};

// 删除规则方法
const handleRemoveRules = () => {
  spiderInfo.value.rules.pop()
}



// 添加选择器规则
const handleAddSelector = () => {
  selectorList.value.push({type: "elementSelector", rules: []})
}

// 删除选择器规则
const handleRemoveSelector = () => {
  if (selectorList.value.length > 1) {
    selectorList.value.pop()
  }
}

</script>

<style scoped>
:deep(.el-input-tag__prefix) {
  padding: 0;
}

.rule-definition-page {
  display: flex;
  gap: 20px;
  padding: 20px;
  height: 50vh;
}

.left-panel {
  overflow: auto;
  flex: 2;
  position: relative;
}

.right-panel {
  flex: 3;
  padding: 20px;
}

.rule-steps {
  margin-top: 20px;
}

.step-row {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
}

.show-text {
  margin-right: 10px;
  white-space: nowrap; /* 防止文字换行 */
}

.el-input {
  margin-right: 10px;
  flex: 1; /* 让输入框占据剩余空间 */
}

.rule-section {
  margin-bottom: 20px;
}

.action-buttons {
  display: flex;
  gap: 10px;
  margin-top: 20px;
}

.rule-steps {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

</style>