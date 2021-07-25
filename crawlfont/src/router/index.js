import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            redirect: '/dashboard'
        },
        {
            path: '/',
            component: () => import(/* webpackChunkName: "home" */ '../components/common/Home.vue'),
            meta: { title: '自述文件' },
            children: [
                {
                    path: 'dashboard',
                    component: () => import(/* webpackChunkName: "dashboard" */ '../components/home/Dashboard.vue'),
                    meta: { title: '系统首页' }
                },
                {
                    path: 'projectIndex',
                    component: () => import(/* webpackChunkName: "dashboard" */ '../components/spider/ProIndex.vue'),
                    meta: { title: '爬虫项目' },

                },
                {
                    path: 'project/:projectId',
                    component: () => import(/* webpackChunkName: "dashboard" */ '../components/spider/TaskList.vue'),
                    meta: { title: '项目列表' },

                },
                {
                    path: 'taskIndex',
                    name: '爬虫任务',
                    component: () => import('../components/spider/TaskIndex.vue'),
                    meta: {
                        title: '爬虫任务',
                    },
                },

                {
                    path: 'monitor',
                    name: '定时任务',
                    component: () => import('../components/monitor/Monitor.vue'),
                    meta: {
                        title: '定时任务',
                    },
                },

                {
                    path: 'corn',
                    name: '定时任务',
                    component: () => import('../components/spider/corn.vue'),
                    meta: {
                        title: '定时任务',
                    },
                },

                {
                    path: 'taskLog/:taskId',
                    component: () => import(/* webpackChunkName: "dashboard" */ '../components/log/spiderJournal.vue'),
                    meta: { title: '任务详情' }
                },
                {
            
                    path: 'taskDetail/:taskId',
                    component: () => import(/* webpackChunkName: "dashboard" */ '../components/spider/TaskDetail.vue'),
                    meta: { title: '爬虫详情' }
                },
                {
                    path: '/spiderdata',
                    component: () => import(/* webpackChunkName: "dashboard" */ '../components/spider/SpiderData.vue'),
                    meta: { title: '爬虫数据' }
                },
                {
                    path: '/erpdata',
                    component: () => import(/* webpackChunkName: "dashboard" */ '../components/until/Erp.vue'),
                    meta: { title: '库存数据' }
                },
                {
                    path: '/icon',
                    component: () => import(/* webpackChunkName: "icon" */ '../components/until/Icon.vue'),
                    meta: { title: '自定义图标' }
                },
                {
                    path: '/wordcloud',
                    component: () => import(/* webpackChunkName: "table" */ '../components/wordCloud/WordCloudChart.vue'),
                    meta: { title: '词云图' }
                },
                {
                    path: '/table',
                    component: () => import(/* webpackChunkName: "table" */ '../components/forms/BaseTable.vue'),
                    meta: { title: '基础表格' }
                },
                {
                    path: '/hosts',
                    component: () => import(/* webpackChunkName: "table" */ '../components/host/HostList.vue'),
                    meta: { title: '节点' }
                },
                {
                    path: '/host/deploys',
                    component: () => import(/* webpackChunkName: "table" */ '../components/host/deploys.vue'),
                    meta: { title: '安装服务' }
                },
                {
            
                    path: 'hostDetail/:uuid',
                    component: () => import(/* webpackChunkName: "dashboard" */ '../components/host/HostDetail.vue'),
                    meta: { title: '节点详情' }
                },

                {
            
                    path: '/host/masterRsa',
                    component: () => import(/* webpackChunkName: "dashboard" */ '../components/host/MasterRsa.vue'),
                    meta: { title: 'master公钥' }
                },

                {
                    path: '/deployTask/:taskId',
                    component: () => import(/* webpackChunkName: "table" */ '../components/spider/TaskDeploy.vue'),
                    meta: { title: '部署任务' }
                },

                {
                    path: '/hostDetail',
                    component: () => import(/* webpackChunkName: "table" */ '../components/host/HostDetail.vue'),
                    meta: { title: '节点详情' }
                },
                {
                    path: '/box',
                    component: () => import(/* webpackChunkName: "table" */ '../components/until/Box.vue'),
                    meta: { title: '消息盒子' }
                },
                
                {
                    path: '/tabs',
                    component: () => import(/* webpackChunkName: "tabs" */ '../components/until/Tabs.vue'),
                    meta: { title: 'tab选项卡' }
                },
                {
                    path: '/form',
                    component: () => import(/* webpackChunkName: "form" */ '../components/forms/BaseForm.vue'),
                    meta: { title: '基本表单' }
                },
                {
                    // 富文本编辑器组件
                    path: '/editor',
                    component: () => import(/* webpackChunkName: "editor" */ '../components/until/VueEditor.vue'),
                    meta: { title: '富文本编辑器' }
                },
                {
                    // markdown组件
                    path: '/markdown',
                    component: () => import(/* webpackChunkName: "markdown" */ '../components/until/Markdown.vue'),
                    meta: { title: 'markdown编辑器' }
                },
                {
                    // 图片上传组件
                    path: '/upload',
                    component: () => import(/* webpackChunkName: "upload" */ '../components/until/Upload.vue'),
                    meta: { title: '文件上传' }
                },
                {
                    path: '/charts',
                    component: () => import(/* webpackChunkName: "chart" */ '../components/eCharts/BaseCharts.vue'),
                    meta: { title: 'schart图表' }
                },
                {
                    path: '/workLog',
                    component: () => import('../components/workLog/LogIndex.vue'),
                    meta: {title: '任务日志'}
                },

                {
                    path: '/setting',
                    component: () => import('../components/setting/Setting.vue'),
                    meta: {title: '设置'}
                },

                {
                    // 拖拽列表组件
                    path: '/drag',
                    component: () => import(/* webpackChunkName: "drag" */ '../components/until/DragList.vue'),
                    meta: { title: '拖拽列表' }
                },
                {
                    // 拖拽Dialog组件
                    path: '/dialog',
                    component: () => import(/* webpackChunkName: "dragdialog" */ '../components/until/DragDialog.vue'),
                    meta: { title: '拖拽弹框' }
                },
                {
                    // 国际化组件
                    path: '/i18n',
                    component: () => import(/* webpackChunkName: "i18n" */ '../components/until/I18n.vue'),
                    meta: { title: '国际化' }
                },
                {
                    // 权限页面
                    path: '/permission',
                    component: () => import(/* webpackChunkName: "permission" */ '../components/until/Permission.vue'),
                    meta: { title: '权限测试', permission: true }
                },
                {
                    path: '/404',
                    component: () => import(/* webpackChunkName: "404" */ '../components/error/404.vue'),
                    meta: { title: '404' }
                },
                {
                    path: '/403',
                    component: () => import(/* webpackChunkName: "403" */ '../components/error/403.vue'),
                    meta: { title: '403' }
                },
                {
                    path: '/donate',
                    component: () => import(/* webpackChunkName: "donate" */ '../components/author/Donate.vue'),
                    meta: { title: '支持作者' }
                }
            ]
        },
        {
            path: '/login',
            component: () => import(/* webpackChunkName: "login" */ '../components/login/Login.vue'),
            meta: { title: '登录' }
        },
        {
            path: '*',
            redirect: '/404'
        }
    ]
});
