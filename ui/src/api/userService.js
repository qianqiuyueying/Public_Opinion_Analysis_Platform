import request from "../utils/request";

// 登录接口
export const login = (data) => {
    return request.post("/user/login", data)
}

// 注册接口
export const register = (data) => {
    return request.post("/user/register", data)
}

// 发送邮箱验证码
export const sendVerificationCode = (data) => {
    return request.post('/user/sendVerificationCode', data)
}

// 获取用户信息
export const getUserInfo = () => {
    return request.get("/user/getUserInfo");
}