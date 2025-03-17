<template>
  <div class="announcement-container">
    <!-- 搜索栏 -->
    <div class="search-bar">
      <el-input
          v-model="searchKeyword"
          placeholder="请输入公告标题或内容"
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

    <!-- 公告列表 -->
    <el-table :data="filteredAnnouncements" stripe style="width: 100%">
      <el-table-column prop="title" label="公告标题" width="200" />
      <el-table-column prop="content" label="公告内容" />
      <el-table-column prop="publish_time" label="发布时间" width="180" />
      <el-table-column label="操作" width="120">
        <template #default="scope">
          <el-button type="primary" size="small" @click="handleView(scope.row)">
            <el-icon><View /></el-icon>
            查看
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <!-- 分页 -->
    <div class="pagination">
      <el-pagination
          v-model:current-page="currentPage"
          v-model:page-size="pageSize"
          :total="totalAnnouncements"
          layout="prev, pager, next, jumper"
          @current-change="handlePageChange"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { Search, View } from '@element-plus/icons-vue';

// 模拟公告数据
const announcements = ref([
  {
    id: 1,
    title: '系统维护通知',
    content: '系统将于2025年3月15日凌晨2:00至5:00进行维护，期间无法访问。',
    publish_time: '2025-03-10T09:00:00Z',
  },
  {
    id: 2,
    title: '新功能上线',
    content: '新增用户管理模块，支持批量导入和导出用户数据。',
    publish_time: '2025-03-08T14:30:00Z',
  },
  {
    id: 3,
    title: '安全更新提醒',
    content: '请尽快更新系统至最新版本，修复已知安全漏洞。',
    publish_time: '2025-03-05T11:15:00Z',
  },
  {
    id: 4,
    title: '用户反馈通道开通',
    content: '用户可通过“意见反馈”功能提交问题或建议。',
    publish_time: '2025-03-01T16:45:00Z',
  },
]);

// 搜索关键字
const searchKeyword = ref('');

// 分页相关
const currentPage = ref(1);
const pageSize = ref(10);

// 过滤后的公告列表
const filteredAnnouncements = computed(() => {
  return announcements.value.filter(announcement  => {
    return (
        announcement.title.toLowerCase().includes(searchKeyword.value.toLowerCase())  ||
        announcement.content.toLowerCase().includes(searchKeyword.value.toLowerCase())
    );
  });
});

// 总公告数
const totalAnnouncements = computed(() => filteredAnnouncements.value.length);

// 搜索功能
const handleSearch = () => {
  currentPage.value  = 1; // 搜索后重置到第一页
};

// 分页切换
const handlePageChange = (page) => {
  currentPage.value  = page;
};

// 查看公告详情
const handleView = (announcement) => {
  console.log(' 查看公告:', announcement);
};
</script>

<style scoped>
.announcement-container {
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