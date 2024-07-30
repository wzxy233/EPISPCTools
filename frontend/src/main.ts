import { createApp } from "vue";
//element-plus
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import App from "./App.vue";
import router from "./router";
import axios from "axios";
import store from "./store";

//创建实例
const app = createApp(App);

//全局应用配置
//axios发送http请求的目标地址的基础路径
axios.defaults.baseURL = "http://localhost:8000"
app.config.globalProperties.$axios = axios;
 
app.use(ElementPlus).use(store).use(router).mount("#app");