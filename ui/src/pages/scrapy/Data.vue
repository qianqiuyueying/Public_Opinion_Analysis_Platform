<template>
  <div class="spider-management-page">
    <el-card class="management-card"
             :body-style="{
        height:'100%',
        width:'100%',
        boxSizing:'border-box',
        display: 'flex',        // 新增flex布局
        flexDirection: 'column' // 纵向排列
      }">
      <!-- 表格部分 -->
      <el-table
          :data="spiderList"
          style="width: 100%"
          class="auto-height-table"
      >
        <el-table-column type="index" :index="getIndex"/>
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
        <template #empty>
          <el-empty/>
        </template>
      </el-table>

      <!-- 分页器 -->
      <div class="pagination-section">
        <el-pagination
            v-model:current-page="currentPage"
            v-model:page-size="pageSize"
            :page-sizes="[10, 20, 30, 50]"
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
import { ref, onMounted } from 'vue'

const currentPage = ref(1)
const pageSize = ref(20)
const size = ref('20')
const total = ref(100)

const spiderList = ref()

const getIndex = (index) => {
  return index
}

onMounted(() => {
  // 初始化数据
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
  height: 82vh; /* 改为视窗单位更可靠 */
}

.management-card {
  height: 100%;
  /* 移除padding改用body-style控制 */
}

.auto-height-table {
  flex: 1;
  min-height: 100px; /* 防止内容过少时高度塌陷 */
  overflow: auto;
}

.pagination-section {
  flex-shrink: 0; /* 防止被压缩 */
  padding: 16px;
  background: #fff;
  border-top: 1px solid #ebeef5;
  margin-top: auto; /* 确保始终位于底部 */
}
</style>