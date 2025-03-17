<template>
  <div class="sticky-notes">
    <!-- 添加便利贴按钮 -->
    <el-button type="primary" @click="addStickyNote">添加便利贴</el-button>

    <!-- 便利贴列表 -->
    <div class="notes-container">
      <el-card
          v-for="(note, index) in stickyNotes"
          :key="index"
          class="sticky-note"
          shadow="hover"
      >
        <div class="note-header">
          <el-input
              v-model="note.content"
              type="textarea"
              autosize
              placeholder="请输入内容"
              @blur="saveStickyNote(index)"
          ></el-input>
          <i class="el-icon-close delete-icon" @click="deleteStickyNote(index)"></i>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

// 初始化便利贴数组
const stickyNotes = ref([]);

// 添加便利贴
function addStickyNote() {
  stickyNotes.value.push({ content: '' });
}

// 保存便利贴
function saveStickyNote(index) {
  // 这里可以调用API将便利贴内容保存到数据库
  console.log('保存便利贴:', stickyNotes.value[index].content);
}

// 删除便利贴
function deleteStickyNote(index) {
  stickyNotes.value.splice(index, 1);
}
</script>

<style scoped>
.sticky-notes {
  padding: 20px;
}

.notes-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin-top: 20px;
}

.sticky-note {
  width: 250px;
  min-height: 100px;
  background-color: #fffae6;
  border-left: 8px solid #f4d03f;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  position: relative;
}

.note-header {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.el-input__inner {
  border: none;
  resize: none;
  outline: none;
  padding: 10px;
  font-size: 16px;
  line-height: 1.5;
}

.delete-icon {
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
  font-size: 18px;
  color: #ff6b6b;
}

.delete-icon:hover {
  color: #ff4757;
}
</style>