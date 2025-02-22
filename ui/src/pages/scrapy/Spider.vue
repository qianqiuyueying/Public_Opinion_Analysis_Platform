<template>
  <div class="spider-management-page">
    <el-card class="management-card">

      <el-table :data="spiderList" style="width: 100%">
        <el-table-column label="id" prop="id" width="100"/>
        <el-table-column label="名称" prop="name" width="150" />
        <el-table-column label="描述" prop="description" />
        <el-table-column align="right">
          <template #header>
            <el-input v-model="search" placeholder="搜索名称" />
          </template>
          <template #default="scope">
            <el-button size="small" @click="handleEdit(scope.$index, scope.row)">
              详情
            </el-button>
            <el-button
                size="small"
                type="danger"
                @click="handleDelete(scope.$index, scope.row)"
            >
              删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>

      <!-- 分页器 -->
      <div class="pagination-section">
        <el-pagination
            v-model:current-page="currentPage"
            v-model:page-size="pageSize"
            :page-sizes="[10, 20, 30, 50]"
            :size="size"
            layout="total, sizes, prev, pager, next, jumper"
            :total="total"
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
        />
      </div>
    </el-card>
  </div>
</template>

<script setup>
import {ref, onMounted} from 'vue'

const currentPage = ref(1)
const pageSize = ref(20)
const size = ref(20)
const total = ref(100)

const spiderList = ref()

onMounted(() => {

})

const handleSizeChange = () => {
  console.log(pageSize.value)
}

const handleCurrentChange = (currentPage) => {
  console.log(currentPage)
}
</script>

<style scoped>
.spider-management-page {
  padding: 20px;
  display: flex;
  justify-content: center;
  height: 90%;
}

.management-card {
  width: 100%;
  max-width: 1200px;
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
  text-align: center;
}


.pagination-section {
  padding: 10px;
  background-color: #f5f7fa;
  border-top: 1px solid #e4e7ed;
  position: sticky;
  bottom: 0;
  z-index: 10;
}
</style>