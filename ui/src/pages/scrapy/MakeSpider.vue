<template>
  <el-container style="padding:40px 0 0 0; height:100%; margin:auto;">
    <el-header style="height: auto">
      <el-steps :active="activeStep" align-center>
        <el-step title='爬虫类型' description="选择合适的爬虫类型"/>
        <el-step title="测试网址" description="设置用于测试爬虫的单条或多条网址"/>
        <el-step title="请求配置" description="为爬虫配置合适的请求及参数"/>
        <el-step title="定义规则" description="为爬虫自定义合适的数据筛选规则以及简单结果预览"/>
        <el-step title="结果预览" description="预览全部网址的爬取结果"/>
        <el-step title="生成爬虫" description="为该爬虫设置自定义信息并保存至数据库"/>
      </el-steps>
    </el-header>
    <el-main>
      <SpiderClass v-if="activeStep === 0" v-model:spiderInfo="spiderInfo"/>
      <TestLink v-else-if="activeStep === 1" v-model:spiderInfo="spiderInfo"/>
      <RequestConfig v-else-if="activeStep === 2" v-model:spiderInfo="spiderInfo"/>
      <MakeRules v-else-if="activeStep === 3" v-model:spiderInfo="spiderInfo"/>
      <ResultView v-else-if="activeStep === 4" v-model:spiderInfo="spiderInfo"/>
      <ProductSpider v-else-if="activeStep === 5" v-model:active-step="activeStep" v-model:spiderInfo="spiderInfo"/>
      <Celebration v-else-if="activeStep === 6"/>
    </el-main>
    <el-footer style="text-align:right">
      <el-button-group>
        <el-button :icon="ArrowLeft" @click="handlePreviousStep" size="large">上一步</el-button>
        <el-button type="primary" :icon="ArrowRight" @click="handleNextStep" size="large">下一步</el-button>
      </el-button-group>
    </el-footer>
  </el-container>
</template>

<script setup>
import {ref, reactive, onMounted} from 'vue';
import SpiderClass from "@/pages/scrapy/components/SpiderClass.vue";
import TestLink from "@/pages/scrapy/components/TestLink.vue";
import RequestConfig from "@/pages/scrapy/components/RequestConfig.vue";
import MakeRules from "@/pages/scrapy/components/MakeRules.vue";
import ResultView from "@/pages/scrapy/components/ResultView.vue";
import ProductSpider from "@/pages/scrapy/components/ProductSpider.vue";
import {ArrowLeft, ArrowRight} from "@element-plus/icons-vue";
import Celebration from "@/pages/scrapy/components/Celebration.vue";
import {createSpiderService} from '@/api/scrapyService.js'

onMounted(async () => {

})


const activeStep = ref(0); // 当前激活的步骤
const spiderInfo = reactive({
  name: "",  // 昵称
  description: "",  // 描述
  type: "APIClass",  // 爬虫类型
  address: {
    type: "direct",  // 默认直链类型
    links: "",  // 直链们
    rule: [
      { type: "baseURL", value: "" },
    ]
  },
  request: {
    method: "GET",
    headers: [],
    params: [],
    body: [],
  },
  rules: [],
})


// 校验函数
const validateSpiderInfo = () => {
  // 校验 name
  if (!spiderInfo.name || spiderInfo.name.trim() === '') {
    ElMessage.error('爬虫名称不能为空')
    return false
  }

// 校验 description
  if (!spiderInfo.description || spiderInfo.description.trim() === '') {
    ElMessage.error('爬虫描述不能为空')
    return false
  }


  // 校验 type
  if (!['APIClass', 'PageClass'].includes(spiderInfo.type)) {
    ElMessage.error('爬虫类型必须是 APIClass 或 PageClass')
    return false
  }

  // 校验 address
  if (spiderInfo.address.type === 'direct') {
    if (spiderInfo.address.links.trim() === '') {
      ElMessage.value.error('直链地址不能为空')
      return false
    }
  } else if (spiderInfo.address.type === 'segment') {
    if (spiderInfo.address.rule.length < 2) {
      ElMessage.error('片段组合规则至少需要两条')
      return false
    }
  } else {
    ElMessage.error('地址类型必须是 direct 或 segment')
    return false
  }

  // 校验 rules
  if (spiderInfo.rules.length < 1) {
    ElMessage.error('规则列表至少需要一条')
    return false
  }

  // 所有校验通过
  return true
}

const handlePreviousStep = () => {
  if (activeStep.value > 0) {
    activeStep.value -= 1;
  } else {
    ElMessage.warning('前面没有东西了哦~请开始制作爬虫吧！')
  }
}

const handleNextStep = async () => {
  if (activeStep.value < 5) {
    activeStep.value += 1;
  } else if (activeStep.value === 5) {
    // 校验
    if (validateSpiderInfo()) {
      let {name, description, type, address, request, rules} = spiderInfo;
      const data = await createSpiderService({name, description, type, address, request, rules});
      if (data.data.code === 200) {
        activeStep.value += 1;
      }
    }
  } else {
    ElMessage.success('爬虫已经制作完成了哦~请前往任务管理开始采集任务吧！')
  }
}
</script>

<style scoped>

</style>