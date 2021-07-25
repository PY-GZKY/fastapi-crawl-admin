import axios from 'axios';
import router from '../router';

const service = axios.create({
    // process.env.NODE_ENV === 'development', // TODO 来判断是否开发环境
    baseURL: process.env.VUE_APP_BACKEND_URL,
    timeout: 60 * 1000 * 60 * 4
});

// 拦截请求
service.interceptors.request.use(
    config => {
        if (localStorage.getItem('token')) {
            // console.log("token：" + localStorage.getItem('token'));
            config.headers.common['Token'] = localStorage.getItem('token');
        } else {
            config.headers.common['Token'] = "";
        }
        return config
    },
    err => {
        // return Promise.reject(err)
    }
);

// 拦截响应
service.interceptors.response.use(
    response => {
        // console.log("首次拦截");
        switch (response.data.code) {
            case 200:
                return response;
        }
        return response
    },

    err => {
        // console.log(err);
        if (err && err.response) {
            switch (err.response.status) {
                case 400:
                    // console.log(40000000, err.response.data);
                    return err.response;
                case 401:
                    console.log("出现 401");

                    localStorage.clear();
                    sessionStorage.clear();

                    router.replace({
                        path: 'login',
                        query: { redirect: router.currentRoute.fullPath } // 登录成功后跳入浏览的当前页面
                    });
                    break;
                case 403: err.message = '拒绝访问(403)'; return err.response;
                case 404: err.message = '请求出错(404)'; return err.response;
                case 408: err.message = '请求超时(408)'; return err.response;
                case 422: return err.response;
                case 500: err.message = '服务器错误(500)'; return err.response;
                case 501: err.message = '服务未实现(501)'; return err.response;
                case 502: err.message = '网络错误(502)'; return err.response;;
                case 503: err.message = '服务不可用(503)'; return err.response;
                case 504: err.message = '网络超时(504)'; return err.response;
                case 505: err.message = 'HTTP版本不受支持(505)'; return err.response;
                default: err.message = `连接出错(${err.response.status})!`;

            }
        } else {
            err.message = '连接服务器失败!'
            return Promise.reject(err);
        }

    }
)



export default service;
