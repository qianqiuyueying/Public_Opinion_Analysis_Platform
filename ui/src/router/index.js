import {createRouter, createWebHistory} from "vue-router";
import Login from "../pages/user/Login.vue";
import Register from "../pages/user/Register.vue";

import Home from "../pages/home/Home.vue";
import ForgetPassword from "../pages/user/ForgetPassword.vue";
import Layout from "@/components/Layout.vue";
import Dashboard from "@/pages/dashboard/Dashboard.vue";
import Overview from "@/pages/analytics/Overview.vue";
import Task from '@/pages/scrapy/Task.vue'
import Spider from "@/pages/scrapy/Spider.vue";
import Data from "@/pages/scrapy/Data.vue";
import Detail from "@/pages/analytics/Detail.vue";
import Trend from "@/pages/analytics/Trend.vue";
import Info from '@/pages/user/Info.vue'
import List from '@/pages/user/List.vue'
import Board from "@/pages/board/Board.vue";
import Message from '@/pages/message/Message.vue'
import MakeSpider from "@/pages/scrapy/MakeSpider.vue";

const routes = [
    {path: "/", component: Home},
    {path: "/login", component: Login},
    {path: "/register", component: Register},
    {path: '/forget-password', component: ForgetPassword},
    {
        path: '/layout',
        component: Layout,
        children: [
            {path: "/layout/dashboard", component: Dashboard},
            {
                path: "/layout/scrapy",
                children: [
                    {path: "/layout/scrapy/make-spider", component: MakeSpider},
                    {path: "/layout/scrapy/spider", component: Spider},
                    {path: '/layout/scrapy/task', component: Task},
                    {path: "/layout/scrapy/data", component: Data},
                ]
            },
            {
                path: "/layout/analytics",
                children: [
                    {path: "/layout/analytics/overview", component: Overview},
                    {path: "/layout/analytics/details", component: Detail},
                    {path: '/layout/analytics/trend', component: Trend}
                ]
            },
            {
                path: "/layout/user",
                children: [
                    {path: "/layout/user/info", component: Info},
                    {path: '/layout/user/list', component: List},
                ]
            },
            {
                path: "/layout/message",
                component: Message
            },
            {
                path: '/layout/board',
                component: Board
            }
        ]
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router;