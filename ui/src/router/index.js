import {createRouter, createWebHistory} from "vue-router";
import Login from "../pages/user/Login.vue";
import Register from "../pages/user/Register.vue";

import Home from "../pages/home/Home.vue";
import ForgetPassword from "../pages/user/ForgetPassword.vue";

const routes = [
    {path: "/", component: Home},
    {path: "/login", component: Login},
    {path: "/register", component: Register},
    {path: '/forget-password', component: ForgetPassword},
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router;