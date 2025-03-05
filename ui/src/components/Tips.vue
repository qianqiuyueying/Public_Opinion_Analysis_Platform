<template>
  <el-tooltip :content="content" :placement="placement">
    <el-icon size="16"><QuestionFilled/></el-icon>
  </el-tooltip>
</template>

<script setup>
import {QuestionFilled} from "@element-plus/icons-vue";

const content = defineModel("content", {
  type: String,
})
const placement = defineModel("placement", {
  type: String,
  default: 'top'
})

</script>


<style scoped>

</style>