import request_ from '../utils/request.js'

// 测试爬虫接口
export const testSpiderService = async ({type, address, request, rules}) => {
    return request_.post('/scrapy/test-spider', {type, address, request, rules})
}

// 预览爬虫预览结果接口
export const getPreviewDataService = async ({ type, address, request, rules }) => {
    return request_.post("/scrapy/get-preview-data", {type, address, request, rules})
}

// 预览关键词爬虫结果接口
export const getKeySpiderPreviewDataService = async ({type, config, limit}) => {
    return request_.post('/scrapy/get-key-spider-preview-data', {type, config, limit})
}

// 获取爬虫信息接口
export const getSpiderService = async () => {

}

// 修改爬虫信息接口
export const updateSpiderService = async () => {

}

// 获取爬虫列表接口
export const getSpiderList = () => {

}

// 创建爬虫
export const createSpiderService = async ({name, description, type, address, request, rules}) => {
    return request.post("/scrapy/create-spider", {name, description, type, address, request, rules})
}
