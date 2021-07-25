import Vue from 'vue';
import App from './App.vue';
import router from './router';
import ElementUI from 'element-ui';
import VueI18n from 'vue-i18n';
import {messages} from './components/common/i18n';
import 'element-ui/lib/theme-chalk/index.css'; // 默认主题
// import './assets/css/theme-green/index.css'; // 浅绿色主题
// import 'font-awesome/fonts/fontawesome-webfont.woff'
import './assets/css/icon.css';
import './components/common/directives';
import 'babel-polyfill';
import cookie from 'vue-cookie'
import axios from 'axios'
import Api from './api';
import global from './utils/global.js'



Vue.prototype.global = global

// 简直垃圾
// import dataV from '@jiaminghi/data-view'
// Vue.use(wordcloud)

import eCharts from 'echarts'
Vue.prototype.$echarts = eCharts


axios.defaults.withCredentials = true; // 让ajax携带cookie
Vue.prototype.$axios = axios;

Vue.prototype.$api = Api;
Vue.prototype.$cookie = cookie;


Vue.config.productionTip = false;
Vue.use(VueI18n);
Vue.use(ElementUI, {
    size: 'small'
});
const i18n = new VueI18n({
    locale: 'zh',
    messages
});

// 使用钩子函数对路由进行权限跳转

router.beforeEach((to, from, next) => {
    document.title = `${to.meta.title} | Crawl`;
    const role = localStorage.getItem('username');
    // console.log(role);
    if (!role && to.path !== '/login') {
        next('/login');
    } else if (to.meta.permission) {
        // 如果是管理员权限则可进入，这里只是简单的模拟管理员权限而已
        role === 'admin' ? next() : next('/403');
    } else {
        // 简单的判断IE10及以下不进入富文本编辑器，该组件不兼容
        if (navigator.userAgent.indexOf('MSIE') > -1 && to.path === '/editor') {
            Vue.prototype.$alert('vue-quill-editor组件不兼容IE10及以下浏览器，请使用更高版本的浏览器查看', '浏览器不兼容通知', {
                confirmButtonText: '确定'
            });
        } else {
            next();
        }
    }
});

new Vue({
    router,
    i18n,
    render: h => h(App)
}).$mount('#app');
