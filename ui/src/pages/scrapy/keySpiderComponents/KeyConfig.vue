<template>
  <div class="form-container">
    <el-card class="form-card" shadow="hover">
      <template #header>
        <div class="card-header">
          <span>搜索参数</span>
        </div>
      </template>
      <el-form :model="spiderInfo.config" label-width="auto">
        <el-form-item label="关键词">
          <el-input v-model="spiderInfo.config.key"/>
        </el-form-item>
        <el-divider/>
        <!-- 小红书参数配置部分 -->
        <el-form-item label="笔记类型" v-if="spiderInfo.type === 'RedNote'">
          <el-radio-group v-model="spiderInfo.config.NoteType">
            <el-radio-button label="全部" value="all"/>
            <el-radio-button label="图文" value="article"/>
            <el-radio-button label="视频" value="video"/>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="排序依据" v-if="spiderInfo.type === 'RedNote'">
          <el-radio-group v-model="spiderInfo.config.sortedBy">
            <el-radio-button label="综合" value="general"/>
            <el-radio-button label="最新" value="new"/>
            <el-radio-button label="最热" value="hot"/>
          </el-radio-group>
        </el-form-item>
        <!-- 微博参数配置部分 -->
        <el-form-item label="博客类型" v-if="spiderInfo.type === 'Weibo'">
          <el-radio-group v-model="spiderInfo.config.blogType">
            <el-radio-button label="全部" value="all"/>
            <el-radio-button label="热门" value="hot"/>
            <el-radio-button label="原创" value="original"/>
            <el-radio-button label="认证用户" value="vip"/>
            <el-radio-button label="媒体" value="media"/>
            <el-radio-button label="观点" value="view"/>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="时间" v-if="spiderInfo.type === 'Weibo'">
          <el-date-picker
            v-model="spiderInfo.config.time",
            type="datetimerange"
            range-separator="-"
            value-format="YYYY-MM-DD-HH"
            start-placeholder="开始时间"
            end-placeholder="结束时间"
          />
        </el-form-item>
        <!-- 抖音参数配置部分 -->
        <el-form-item label="排序依据" v-if="spiderInfo.type === 'Tiktok'">
          <el-radio-group v-model="spiderInfo.config.sortedBy">
            <el-radio-button label="综合排序" value="general"/>
            <el-radio-button label="最新发布" value="new"/>
            <el-radio-button label="最多点赞" value="hot"/>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="发布时间" v-if="spiderInfo.type === 'Tiktok'">
          <el-radio-group v-model="spiderInfo.config.publishTime">
            <el-radio-button label="不限" value="all"/>
            <el-radio-button label="一天内" value="day"/>
            <el-radio-button label="一周内" value="week"/>
            <el-radio-button label="半年内" value="6months"/>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="视频时长" v-if="spiderInfo.type === 'Tiktok'">
          <el-radio-group v-model="spiderInfo.config.duration">
            <el-radio-button label="不限" value="all"/>
            <el-radio-button label="一分钟以下" value="lessThan1Minute"/>
            <el-radio-button label="1-5分钟" value="1To5Minute"/>
            <el-radio-button label="5分钟以上" value="moreThan5Minute"/>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="内容形式" v-if="spiderInfo.type === 'Tiktok'">
          <el-radio-group v-model="spiderInfo.config.contentType">
            <el-radio-button label="不限" value="all"/>
            <el-radio-button label="图文" value="article"/>
            <el-radio-button label="视频" value="video"/>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="数量限制">
          <el-input v-model="spiderInfo.limit"/>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script setup>
import {reactive} from 'vue';

const spiderInfo = defineModel('spiderInfo')
</script>

<style scoped>
.form-container {
  padding: 20px;
  max-width: 1000px;
  margin: 0 auto;
}

.form-card {
  margin-top: 20px;
}

.card-header {
  text-align: center;
  font-size: 1.2em;
  font-weight: bold;
}

.el-form-item {
  margin-bottom: 18px;
}

.preview-section {
  margin-top: 20px;
  padding: 15px;
  background-color: #f8f9fa;
  border-radius: 4px;
}

pre {
  white-space: pre-wrap;
  word-wrap: break-word;
  background-color: #fff;
  padding: 10px;
  border-radius: 4px;
}
</style>