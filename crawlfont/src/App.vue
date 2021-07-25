<template>
  <div id="app">
    <router-view v-if="isRouterAlive"></router-view>
    <!-- <router-view></router-view> -->
  </div>
</template>


<style>
@import "./assets/css/main.css";
@import "./assets/css/color-dark.css";
/*@import "./assets/css/theme-green/color-green.css";*/
@import "./assets/font/font.css";
body {
  font-family: PingFang;
}
</style>


<script>
export default {
  name: "App",
  globalData: {
    logItems: [],
  },
  provide() {
    return {
      reload: this.reload,
    };
  },
  data() {
    return {
      isRouterAlive: true,
    };
  },

  created() {
    console.log(` %c 
          写字楼里写字间，写字间里程序员；
          程序人员写程序，又拿程序换酒钱。
          酒醒只在网上坐，酒醉还来网下眠；
          酒醉酒醒日复日，网上网下年复年。
          但愿老死电脑间，不愿鞠躬老板前；
          奔驰宝马贵者趣，公交自行程序员。
          别人笑我忒疯癫，我笑自己命太贱；
          不见满街漂亮妹，哪个归得程序员？`,'font-size:20px;color:red;');
    // this.initWebSocket();
  },

  // destroyed() {
  //   that.ws.close(); //离开路由之后断开websocket连接
  // },

  methods: {
    reload() {
      let that = this;
      that.isRouterAlive = false;
      that.$nextTick(function () {
        that.isRouterAlive = true;
      });
    },

    // initWebSocket() {
    //   let that = this;
    //   that.ws = new WebSocket(`ws://127.0.0.1:8000/ws`);
    //   that.global.setWs(that.ws);
    //   that.ws.onerror = that.websocketonerror;
    //   that.ws.onclose = that.websocketclose;
    // },

    // websocketonerror() {
    //   let that = this;
    //   that.initWebSocket();
    // },

    // websocketclose(e) {
    //   console.log("断开连接", e);
    // },
  },
};
</script>