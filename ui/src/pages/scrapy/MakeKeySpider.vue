<template>
  <el-container style="padding:40px 0 0 0; height:100%; margin:auto;">
    <el-header style="height: auto">
      <el-steps :active="activeStep" align-center>
        <el-step title='平台选择' description="选择搜索关键词的平台"/>
        <el-step title="配置参数" description="依据平台搜索规则爬取合适的信息"/>
        <el-step title="结果预览" description="预览信息获取结果"/>
        <el-step title="生成爬虫" description="将该爬虫保存至数据库"/>
      </el-steps>
    </el-header>
    <el-main>
      <KeySpiderClass v-if="activeStep === 0" v-model:spiderInfo="spiderInfo"/>
      <KeyConfig v-if="activeStep === 1" v-model:spiderInfo="spiderInfo"/>
      <KeyResultView v-if="activeStep === 2" v-model:spiderInfo="spiderInfo"/>
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
import {ArrowLeft, ArrowRight} from "@element-plus/icons-vue";
import KeySpiderClass from "@/pages/scrapy/keySpiderComponents/KeySpiderClass.vue";
import KeyConfig from "@/pages/scrapy/keySpiderComponents/KeyConfig.vue";
import KeyResultView from "@/pages/scrapy/keySpiderComponents/KeyResultView.vue";

onMounted(async () => {

})


const activeStep = ref(0); // 当前激活的步骤
const spiderInfo = reactive({
  type: 'RedNote',
  config: {
    NoteType: 'all',
    sortedBy: "general"
  },
  limit: ""
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
  if (activeStep.value < 6) {
    activeStep.value += 1;
  }
}
</script>

<style scoped>

</style>