import request from "../utils/request";

// 登录接口
export const loginService = async ({username, password}) => {
    return request.post("/user/login", {username, password})
}

// 注册接口
export const registerService = async ({username, password, email, code}) => {
    console.log(code)
    return request.post("/user/register", {username, password, email, code})
}

// 发送邮箱验证码
export const sendVerificationCodeService = async ({username, email}) => {
    return request.post('/user/send-verify-code', {username, email})
}

// 获取用户信息
export const getUserInfoService = async (data) => {
    return request.get("/user/info", {params: data});
}