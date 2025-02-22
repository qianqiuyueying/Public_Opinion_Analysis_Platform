<template>
  <div class="request-config-container">
    <el-card class="request-config-card">
      <!-- 请求类型 -->
      <div class="request-type">
        <span class="type-label">请求类型：</span>
        <el-radio-group v-model="spiderInfo.request.method" @change="handleChange">
          <el-radio label="GET" value="GET">GET</el-radio>
          <el-radio label="POST" value="POST">POST</el-radio>
        </el-radio-group>
      </div>

      <!-- 配置区域 -->
      <div class="config-area">
        <!-- 请求头配置 -->
        <div class="config-section">
          <div class="section-title">请求头</div>
          <div class="input-group">
            <el-empty v-if="spiderInfo.request.headers.length === 0"/>
            <div v-for="(header, index) in spiderInfo.request.headers" :key="index" class="input-row">
              <el-input
                  v-model="header.key"
                  placeholder="请输入键"
                  style="flex: 1; margin-right: 10px;"
              ></el-input>
              <el-input
                  v-model="header.value"
                  placeholder="请输入值"
                  style="flex: 1;"
              ></el-input>
            </div>
          </div>
          <div>
            <el-button
                type="primary"
                @click="addHeader"
                :disabled="spiderInfo.request.headers.length >= 8"
            >
              添加
            </el-button>
            <el-button
                type="danger"
                @click="removeLastHeader"
                :disabled="spiderInfo.request.headers.length === 0"
            >
              删除
            </el-button>
          </div>
        </div>

        <!-- GET 请求参数 -->
        <div v-if="spiderInfo.request.method === 'GET'" class="config-section">
          <h2 class="section-title">请求参数</h2>
          <div class="input-group">
            <el-empty v-if="spiderInfo.request.params.length === 0"/>
            <div
                v-for="(param, index) in spiderInfo.request.params"
                :key="index"
                class="input-row"
            >
              <el-input
                  v-model="param.key"
                  placeholder="请输入键"
                  style="flex: 1; margin-right: 10px;"
              />
              <el-input
                  v-model="param.value"
                  placeholder="请输入值"
                  style="flex: 1;"
              />
            </div>
          </div>
          <div class="button-group">
            <el-button
                type="primary"
                @click="addParam"
                :disabled="spiderInfo.request.params.length >= 8"
            >
              添加
            </el-button>
            <el-button
            type="danger"
            @click="removeLastParam"
            :disabled="spiderInfo.request.params.length === 0">
              删除
            </el-button>
          </div>
        </div>

        <!-- POST 请求体 -->
        <div v-else-if="spiderInfo.request.method === 'POST'" class="config-section">
          <h2 class="section-title">请求体</h2>
          <div class="input-group">
            <el-empty v-if="spiderInfo.request.body.length === 0"/>
            <div
                v-for="(body, index) in spiderInfo.request.body"
                :key="index"
                class="input-row"
            >
              <el-input
                  v-model="body.key"
                  placeholder="请输入键"
                  style="flex: 1; margin-right: 10px;"
              />
              <el-input
                  v-model="body.value"
                  placeholder="请输入值"
                  style="flex: 1;"
              />
            </div>
          </div>
          <div class="button-group">
            <el-button
                type="primary"
                @click="addBody"
                :disabled="spiderInfo.request.body.length >= 8"
            >
              添加
            </el-button>
            <el-button
                type="danger"
                @click="removeLastBody"
                :disabled="spiderInfo.request.body.length === 0"
            >
              删除
            </el-button>
          </div>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const spiderInfo = defineModel('spiderInfo')

const handleChange = () => {
  if (spiderInfo.value.request.method === 'GET') {
    spiderInfo.value.request.body = []
  } else if (spiderInfo.value.request.method === 'POST') {
    spiderInfo.value.request.params = []
  }
}

// 请求配置数据
const requestConfig = ref({
  method: 'GET', // 请求类型
  headers: [{ key: '', value: '' }], // 请求头
  params: [{ key: '', value: '' }], // GET 请求参数
  body: [{ key: '', value: '' }], // POST 请求体（键值对形式）
});

// 添加请求头
const addHeader = () => {
  if (spiderInfo.value.request.headers.length < 8) {
    spiderInfo.value.request.headers.push({key: "", value: ""})
  }

};

// 删除最后一个请求头
const removeLastHeader = () => {
  if (spiderInfo.value.request.headers.length > 0) {
    spiderInfo.value.request.headers.pop()
  }
};

// 添加 GET 参数
const addParam = () => {
  if (spiderInfo.value.request.params.length < 8) {
    spiderInfo.value.request.params.push({key: "", value: ""})
  }
};

// 删除最后一个 GET 参数
const removeLastParam = () => {
  if (spiderInfo.value.request.params.length > 0) {
    spiderInfo.value.request.params.pop()
  }
};

// 添加 POST 请求体键值对
const addBody = () => {
  if (spiderInfo.value.request.body.length < 8) {
    spiderInfo.value.request.body.push({key: "", value: ""})
  }
};

// 删除最后一个 POST 请求体键值对
const removeLastBody = () => {
  if (spiderInfo.value.request.body.length > 0) {
    spiderInfo.value.request.body.pop()
  }
  if (requestConfig.value.body.length > 0) {
    requestConfig.value.body.pop();
  }
};
</script>

<style scoped>
.request-config-container {
  padding: 0;
}

.request-config-card {
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.request-type {
  margin-bottom: 20px;
}

.type-label {
  font-size: 14px;
  font-weight: bold;
  margin-right: 10px;
}

.config-area {
  display: flex;
  gap: 20px;
}

.config-section {
  flex: 1;
  display: flex;
  flex-direction: column;
  height: 430px; /* 固定高度，确保布局稳定 */
  border: 1px solid #e4e7ed; /* 添加边框，颜色为浅灰色 */
  border-radius: 8px; /* 可选：添加圆角边框 */
  padding: 20px; /* 可选：添加内边距，让内容不紧贴边框 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 可选：添加阴影，让边框更立体 */
}

.section-title {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 10px;
}

.input-group {
  flex: 1;
  overflow-y: auto; /* 超出高度时滚动 */
  margin-bottom: 10px;
}

.input-row {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.button-group {
  margin-top: auto; /* 按钮固定在底部 */
}
</style>