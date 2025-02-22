<template>
  <div class="result-preview-page">
    <el-card class="preview-card">
      <h3 class="preview-title">结果预览</h3>
      <div class="preview-content">
        <el-input
            v-model="currentPageContent"
            type="textarea"
            :rows="17"
            placeholder="预览内容将显示在这里"
            readonly
        />
      </div>
      <div class="pagination">
        <el-pagination
            :current-page="currentPage"
            :page-size="1"
            :total="totalPages"
            layout="prev, pager, next"
            @current-change="handlePageChange"
        />
      </div>
    </el-card>
  </div>
</template>

<script setup>
import { ref } from 'vue';


// 模拟的分页数据
const allPageContents = ref([
  "这是第一页的内容，展示一些爬取的结果。",
  "这是第二页的内容，展示更多的爬取结果。",
  "这是第三页的内容，继续展示爬取的结果。",
  // 可以根据实际需求添加更多页面内容
]);

const currentPage = ref(1); // 当前页码
const totalPages = ref(allPageContents.value.length); // 总页数

// 当前页面的内容
const currentPageContent = ref(allPageContents.value[0]);

// 处理页码变化
const handlePageChange = (newPage) => {
  currentPage.value = newPage;
  currentPageContent.value = allPageContents.value[newPage - 1];
};
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