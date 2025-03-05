import axios from 'axios'
import setting from "../setting.js";
import {useUserStore} from "@/stores/userStore.js";
import router from '@/router/index.js'

const request = axios.create({
    baseURL: `${setting.Host}`
})

request.interceptors.request.use(config => {
    const store = useUserStore();
    const token = store.token;

    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
}, error => {
    return Promise.reject(error);
})

request.interceptors.response.use(response => {
    if (response.data.code === 401) {
        const store = useUserStore();
        store.reset()
        router.push("/login");
    }
    return response;
})


export default request;