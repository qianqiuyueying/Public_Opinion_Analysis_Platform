<template>
  <div class="result-preview-page">
    <el-card class="preview-card">
      <el-divider content-position="left"><el-text>当前爬取平台 <el-text type="info">{{spiderInfo.type}}</el-text>
      </el-text></el-divider>
      <div class="preview-content">
        <el-input
            v-loading="isLoading"
            v-model="currentPageContent"
            type="textarea"
            :rows="17"
            readonly
        />
      </div>
    </el-card>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import {getKeySpiderPreviewDataService} from "@/api/scrapyService.js";

const spiderInfo = defineModel('spiderInfo')
const isLoading = ref(true);


onMounted(() => {
  getPreviewData()
})


// 当前页面的内容
let currentPageContent = ref();


// 获取预览内容的公共方法
const getPreviewData = async () => {
  let {type, config, limit} = spiderInfo.value;
  const data = await getKeySpiderPreviewDataService({type, config, limit});
  if (data && data.data.code === 200){
    isLoading.value = false;
    currentPageContent.value = JSON.stringify(data.data.data)
  } else {
    ElMessage.error(data.data.message)
  }
  console.log(data.data.data)
}
</script>

<style scoped>
.result-preview-page {
  padding: 5px;
  display: flex;
  justify-content: center;
}

.preview-card {
  width: 100%;
  max-width: 1200px; /* 最大宽度 */
  display: flex;
  flex-direction: column;
}

.preview-title {
  margin-bottom: 20px;
}

.preview-content {
  flex: 1;
  overflow-y: auto; /* 自动出现滚动条 */
}

.pagination {
  margin-top: 20px;
  display: flex;
  justify-content: center;
}
</style>