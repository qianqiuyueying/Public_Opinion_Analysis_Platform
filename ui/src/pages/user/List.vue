<template>
  <div class="user-list-container">
    <!-- 搜索栏 -->
    <div class="search-bar">
      <el-input
          v-model="searchKeyword"
          placeholder="请输入用户名或邮箱"
          clearable
          @clear="handleSearch"
          @keyup.enter="handleSearch"
      >
        <template #append>
          <el-button type="primary" @click="handleSearch">
            <el-icon><Search /></el-icon>
            搜索
          </el-button>
        </template>
      </el-input>
    </div>

    <!-- 用户列表表格 -->
    <el-table :data="filteredUsers" stripe style="width: 100%">
      <el-table-column prop="id" label="用户ID" width="100"/>
      <el-table-column prop="username" label="用户名"/>
      <el-table-column prop="email" label="邮箱"/>
      <el-table-column prop="role" label="角色"/>
      <el-table-column prop="create_at" label="创建时间"/>
      <el-table-column label="操作">
        <template #default="scope">
          <el-button type="primary" size="small" @click="handleEdit(scope.row)">
            <el-icon><Edit /></el-icon>
            编辑
          </el-button>
          <el-button type="danger" size="small" @click="handleDelete(scope.row)">
            <el-icon><Delete /></el-icon>
            删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <!-- 分页 -->
    <div class="pagination">
      <el-pagination
          v-model:current-page="currentPage"
          v-model:page-size="pageSize"
          :total="totalUsers"
          layout="prev, pager, next, jumper"
          @current-change="handlePageChange"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { Search, Edit, Delete } from '@element-plus/icons-vue';

// 模拟用户数据
const users = ref([
  { id: 1, username: 'JohnDoe', email: 'johndoe@example.com',  role: '管理员', create_at: '2023-01-01T12:00:00Z' },
  { id: 2, username: 'JaneSmith', email: 'janesmith@example.com',  role: '普通用户', create_at: '2023-02-15T09:30:00Z' },
  { id: 3, username: 'AliceWang', email: 'alicewang@example.com',  role: '普通用户', create_at: '2023-03-10T14:20:00Z' },
  { id: 4, username: 'BobLee', email: 'boblee@example.com',  role: '管理员', create_at: '2023-04-05T18:45:00Z' },
  { id: 5, username: 'CharlieChen', email: 'charliechen@example.com',  role: '普通用户', create_at: '2023-05-20T11:10:00Z' },
]);

// 搜索关键字
const searchKeyword = ref('');

// 分页相关
const currentPage = ref(1);
const pageSize = ref(10);

// 过滤后的用户列表
const filteredUsers = computed(() => {
  return users.value.filter(user  => {
    return (
        user.username.toLowerCase().includes(searchKeyword.value.toLowerCase())  ||
        user.email.toLowerCase().includes(searchKeyword.value.toLowerCase())
    );
  });
});

// 总用户数
const totalUsers = computed(() => filteredUsers.value.length);

// 搜索功能
const handleSearch = () => {
  currentPage.value  = 1; // 搜索后重置到第一页
};

// 分页切换
const handlePageChange = (page) => {
  currentPage.value  = page;
};

// 编辑操作
const handleEdit = (user) => {
  console.log(' 编辑用户:', user);
};

// 删除操作
const handleDelete = (user) => {
  console.log(' 删除用户:', user);
};
</script>

<style scoped>
.user-list-container {
  max-width: 1200px;
  margin: 20px auto;
  padding: 20px;
}

.search-bar {
  margin-bottom: 20px;
}

.pagination {
  margin-top: 20px;
  text-align: right;
}

.el-table {
  margin-top: 20px;
}

.el-button {
  margin-right: 10px;
}
</style>