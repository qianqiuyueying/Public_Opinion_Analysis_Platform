import axios from 'axios'
import setting from "../setting.js";
import {useUserStore} from "@/stores/userStore.js";

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


export default request;