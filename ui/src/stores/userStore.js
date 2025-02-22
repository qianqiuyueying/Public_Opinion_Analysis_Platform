import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUserStore = defineStore('user', () => {
    const id = ref() // id
    const avatar = ref() // 头像
    const username = ref()  // 用户名
    const email = ref()  // email
    const createTime = ref()  // 注册时间
    const lastLogin = ref()  // 上次登录时间
    const role = ref()  // 对应权限
    const token = ref()
    const setToken = (newToken) => {
        token.value = newToken
    }
    const setInfo = (info) => {
        id.value = info.id
        avatar.value = info.avatar
        username.value = info.username
        email.value = info.email
        createTime.value = info.createTime
        lastLogin.value = info.lastLogin
        role.value = info.role
        token.value = info.token
    }
    const reset = () => {
        id.value = ''
        avatar.value = ''
        username.value = ''
        email.value = ''
        createTime.value = ''
        lastLogin.value = ''
        role.value = ''
        token.value = ''
    }

    return {id, username, avatar, email, createTime, lastLogin, role, token, setInfo, setToken, reset}
})

