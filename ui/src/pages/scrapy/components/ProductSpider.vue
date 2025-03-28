<template>
  <div class="generate-spider-page">
    <el-card class="spider-info-card">

      <!-- 爬虫信息展示 -->
      <div class="spider-info">
        <el-descriptions title="基础信息" :column="2" border>
          <el-descriptions-item label="名称">
            <el-input v-model="spiderInfo.name"/>
          </el-descriptions-item>
          <el-descriptions-item label="描述">
            <el-input v-model="spiderInfo.description"/>
          </el-descriptions-item>
        </el-descriptions>

        <!-- class 展示 -->
        <el-descriptions title="爬虫类型" :column="1" border>
          <el-descriptions-item label="类型" label-width="30%">
            {{ spiderInfo.type }}
          </el-descriptions-item>
        </el-descriptions>

        <!-- request 展示 -->
        <el-descriptions title="请求配置" :column="1" border>
          <el-descriptions-item label="请求方法">
            {{ spiderInfo.request.method }}
          </el-descriptions-item>
          <el-descriptions-item label="请求头" v-if="spiderInfo.request.method === 'GET'">
            <el-table :data="spiderInfo.request.headers" style="width: 100%">
              <el-table-column prop="key" label="键" />
              <el-table-column prop="value" label="值" />
            </el-table>
          </el-descriptions-item>
          <el-descriptions-item label="请求参数" v-if="spiderInfo.request.method === 'GET'">
            <el-table :data="spiderInfo.request.params" style="width: 100%">
              <el-table-column prop="key" label="键" />
              <el-table-column prop="value" label="值" />
            </el-table>
          </el-descriptions-item>
          <el-descriptions-item label="请求体" v-if="spiderInfo.request.method === 'POST'">
            <el-table :data="spiderInfo.request.body" style="width: 100%">
              <el-table-column prop="key" label="键" />
              <el-table-column prop="value" label="值" />
            </el-table>
          </el-descriptions-item>
        </el-descriptions>

        <!-- rules 展示 -->
        <el-descriptions title="规则配置" :column="1" border>
          <el-descriptions-item label="规则列表">
            <el-table :data="spiderInfo.rules" style="width: 100%">
              <el-table-column prop="source" label="源" />
              <el-table-column prop="operate" label="操作" />
            </el-table>
          </el-descriptions-item>
        </el-descriptions>
      </div>

      <!-- 生成爬虫按钮 -->
      <div class="generate-button">
        <el-button type="primary" size="large" @click="generateSpider">
          生成爬虫
        </el-button>
      </div>
    </el-card>
  </div>
</template>

<script setup>
import {createSpiderService} from "@/api/scrapyService.js";

const spiderInfo = defineModel('spiderInfo')
const activeStep = defineModel('activeStep')

// 校验函数
const validateSpiderInfo = () => {
  // 校验 name
  if (!spiderInfo.value.name || spiderInfo.value.name.trim() === '') {
    ElMessage.error('爬虫名称不能为空')
    return false
  }

// 校验 description
  if (!spiderInfo.value.description || spiderInfo.value.description.trim() === '') {
    ElMessage.error('爬虫描述不能为空')
    return false
  }


  // 校验 class
  if (!['APIClass', 'PageClass'].includes(spiderInfo.value.type)) {
    ElMessage.error('爬虫类型必须是 APIClass 或 PageClass')
    return false
  }

  // 校验 address
  if (spiderInfo.value.address.type === 'direct') {
    if (spiderInfo.value.address.links.trim() === '') {
      ElMessage.error('直链地址不能为空')
      return false
    }
  } else if (spiderInfo.value.address.type === 'segment') {
    if (spiderInfo.value.address.rule.length < 2) {
      ElMessage.error('片段组合规则至少需要两条')
      return false
    }
  } else {
    ElMessage.error('地址类型必须是 direct 或 segment')
    return false
  }

  // 校验 rules
  if (spiderInfo.value.rules.length < 1) {
    ElMessage.error('规则列表至少需要一条')
    return false
  }

  // 所有校验通过
  return true
}

// 生成爬虫
const generateSpider = async () => {
  if (validateSpiderInfo()) {
    let {name, description, type, address, request, rules} = spiderInfo;
    const data = await createSpiderService({name, description, type, address, request, rules});
    if (data.data.code === 200) {
      activeStep.value += 1;
    }
  }
}
</script>

<style scoped>
.generate-spider-page {
  padding: 20px;
}

.spider-info-card {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.title {
  text-align: center;
  margin-bottom: 20px;
}

.spider-info {
  display: flex;
  flex-direction: column;
}

.generate-button {
  margin-top: 20px;
  text-align: center;
}
</style>