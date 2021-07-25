<template>
  <div class="sidebar">
    <el-menu
      class="sidebar-el-menu"
      :default-active="onRoutes"
      :collapse="collapse"
      background-color="#324157"
      text-color="#bfcbd9"
      active-text-color="#20a0ff"
      unique-opened
      router
      @select="lalala"
    >
      <template v-for="item in items">
        <template v-if="item.subs">
          <el-submenu :index="item.index" :key="item.index">
            <template slot="title">
              <i :class="item.icon"></i>
              <span slot="title">{{ item.title }}</span>
            </template>
            <template v-for="subItem in item.subs">
              <el-submenu
                v-if="subItem.subs"
                :index="subItem.index"
                :key="subItem.index"
              >
                <template slot="title">{{ subItem.title }}</template>
                <el-menu-item
                  v-for="(threeItem, i) in subItem.subs"
                  :key="i"
                  :index="threeItem.index"
                  >{{ threeItem.title }}</el-menu-item
                >
              </el-submenu>

              <el-menu-item
                v-else
                :index="subItem.index"
                :key="subItem.index"
                >{{ subItem.title }}</el-menu-item
              >
            </template>
          </el-submenu>
        </template>
        <template v-else>
          <el-menu-item :index="'/' + item.index" :key="item.index">
            <i :class="item.icon"></i>
            <span slot="title">{{ item.title }}</span>
          </el-menu-item>
        </template>
      </template>
    </el-menu>
  </div>
</template>

<script>
import bus from "../common/bus";
export default {
  data() {
    return {
      collapse: false,
      items: [
        {
          icon: "el-icon-lx-home",
          index: "dashboard",
          title: "主页",
        },
        {
          icon: "el-icon-s-promotion",
          index: "projectIndex",
          title: "爬虫项目",
        },
        {
          icon: "el-icon-check",
          index: "taskIndex",
          title: "爬虫任务",
        },

        // {
        //   icon: "el-icon-time",
        //   index: "timeup",
        //   title: "定时任务",
        // },
        {
          icon: "el-icon-monitor",
          // index: "host",
          title: "节点",
          subs: [
            {
              index: "/hosts",
              title: "主机列表",
            },

            {
              index: "/host/deploys",
              title: "安装服务",
            },

             {
              index: "/host/masterRsa",
              title: "SSH公钥",
            },
          ],
        },

        {
            icon: 'el-icon-lx-home',
            index: 'monitor',
            title: '监控服务'
        },
         {
            icon: 'el-icon-time',
            index: 'corn',
            title: '定时任务'
        },
        // {
        //   icon: "el-icon-lx-cascades",
        //   index: "table",
        //   title: "基础表格",
        // },

        // {
        //   icon: "el-icon-lx-copy",
        //   index: "tabs",
        //   title: "tab选项卡",
        // },

        // {
        //   icon: "el-icon-lx-calendar",
        //   index: "3",
        //   title: "表单相关",
        //   subs: [
        //     {
        //       index: "form",
        //       title: "基本表单",
        //     },
        //     {
        //       index: "3-2",
        //       title: "三级菜单",
        //       subs: [
        //         {
        //           index: "editor",
        //           title: "富文本编辑器",
        //         },
        //         {
        //           index: "markdown",
        //           title: "markdown编辑器",
        //         },
        //       ],
        //     },
        //     {
        //       index: "upload",
        //       title: "文件上传",
        //     },
        //   ],
        // },


        // {
        //     icon: 'el-icon-lx-emoji',
        //     index: 'icon',
        //     title: '自定义图标'
        // },

        // {
        //   icon: "el-icon-lx-emoji",
        //   index: "wordcloud",
        //   title: "词云图",
        // },

        {
          icon: "el-icon-s-data",
          index: "charts",
          title: "任务统计",
        },

        {
          icon: "el-icon-tickets",
          index: "workLog",
          title: "任务日志",
        },

        {
          icon: "el-icon-setting",
          index: "setting",
          title: "设置",
        },
    
        // {
        //     icon: 'el-icon-rank',
        //     index: '6',
        //     title: '拖拽组件',
        //     subs: [
        //         {
        //             index: 'drag',
        //             title: '拖拽列表'
        //         },
        //         {
        //             index: 'dialog',
        //             title: '拖拽弹框'
        //         }
        //     ]
        // },
        // {
        //   icon: "el-icon-lx-global",
        //   index: "i18n",
        //   title: "国际化功能",

        // },
        // {
        //   icon: "el-icon-lx-warn",
        //   index: "7",
        //   title: "错误处理",
        //   subs: [
        //     {
        //       index: "permission",
        //       title: "权限测试",
        //     },
        //     {
        //       index: "404",
        //       title: "404页面",
        //     },
        //   ],
        // },

        {
            icon: 'el-icon-lx-redpacket_fill',
            index: '/donate',
            title: '支持作者'
        }
      ],
    };
  },
  computed: {
    onRoutes() {
      // return this.$route.path.replace('/', '');
    },
  },
  created() {
    // 通过 Event Bus 进行组件间通信，来折叠侧边栏
    bus.$on("collapse", (msg) => {
      this.collapse = msg;
      bus.$emit("collapse-content", msg);
    });
  },
  methods: {
    lalala(index, indexPath) {
      console.log(index, indexPath);
    },
  },
};
</script>

<style scoped>
.sidebar {
  display: block;
  position: absolute;
  left: 0;
  top: 65px;
  bottom: 0;
  overflow-y: scroll;
}
.sidebar::-webkit-scrollbar {
  width: 0;
}
.sidebar-el-menu:not(.el-menu--collapse) {
  width: 200px;
}
.sidebar > ul {
  height: 100%;
}
</style>
