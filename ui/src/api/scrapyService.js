import request from '../utils/request.js'
import {registerService} from "@/api/userService.js";

// 测试单条网址爬虫接口

// 测试爬虫接口

// 获取爬虫列表接口

// 测试接口
export const testService = async () => {
    return request.post("/scrapy/test")
}
