import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUserStore = defineStore('user', () => {
    const id = ref() // id
    const username = ref()  // 用户名
    const email = ref()  // email
    const createTime = ref()  // 注册时间
    const lastLogin = ref()  // 上次登录时间
    const role = ref()  // 对应权限
    const token = ref()
    return {id, username, email, createTime, lastLogin, role, token}
})

export default { userStore }