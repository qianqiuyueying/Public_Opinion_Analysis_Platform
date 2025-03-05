<template>
  <div class="result-preview-page">
    <el-card class="preview-card">
      <el-divider content-position="left"><el-text>当前预览链接 <el-text type="info">{{currentAddress[currentPage - 1]}}</el-text>
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
      <div class="pagination">
        <el-pagination
            :current-page="currentPage"
            :total="totalPages"
            :page-size="1"
            layout="prev, pager, next"
            @current-change="handlePageChange"
        />
      </div>
    </el-card>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import {getPreviewDataService} from "@/api/scrapyService.js";

const spiderInfo = defineModel('spiderInfo')
const isLoading = ref(true);

// 响应式根据address指定的规则以列表形式返回所有address
const currentAddress = computed(() => {
  let addresses = [""]
  if (spiderInfo.value.address.type === 'direct') {
    let tem = spiderInfo.value.address.links
    tem = tem.split("\n").join()
    addresses = tem.split(';')
  } else if (spiderInfo.value.address.type === 'segment') {
    let currentURL = [spiderInfo.value.address.rule[0].value]
    for (let i = 1; i < spiderInfo.value.address.rule.length; i++) {
      if (spiderInfo.value.address.rule[i].type === 'URLSegment') {
        for (let j = 0; j < currentURL.length; j++) {
          currentURL[j] = currentURL[j] + spiderInfo.value.address.rule[i].value
        }
      } else if (spiderInfo.value.address.rule[i].type === 'loop') {
        let tem = []
        for (let j = 0; j < currentURL.length; j++) {
          for (let k = spiderInfo.value.address.rule[i].min; k <= spiderInfo.value.address.rule[i].max; k += spiderInfo.value.address.rule[i].step) {
            tem.push(currentURL[j] + k)
          }
        }
        currentURL = tem
      }
      addresses = currentURL
    }
  }
  return addresses
})

onMounted(() => {
  getPreviewData()
})

const currentPage = ref(1); // 当前页码
const totalPages = ref(currentAddress.value.length); // 总页数

// 当前页面的内容
let currentPageContent = currentAddress.value[0];

// 处理页码变化
const handlePageChange = async (newPage) => {
  currentPage.value = newPage;
  // currentPageContent = currentAddress.value[newPage - 1];
  await getPreviewData()
};

// 获取预览内容的公共方法
const getPreviewData = async () => {
  let { type, request, rules } = spiderInfo.value;
  let address = currentAddress.value[currentPage.value - 1];
  const data = getPreviewDataService({type, address, request, rules});
  console.log(data);
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