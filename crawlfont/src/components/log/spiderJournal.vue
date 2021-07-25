<template>
  <div class="log-view-container">
    <div class="filter-wrapper">
      <div class="left">
        <el-alert
          title="最后一次操作日志"
          type="warning"
          :closable="false"
        ></el-alert>
      </div>
      <div class="right">
        <el-pagination
          size="small"
          :total="100"
          :current-page="23"
          :page-sizes="[100, 500, 1000, 5000]"
          :page-size="100"
          :page-count="3"
          layout="sizes, prev, pager, next"
        />
      </div>
    </div>

    <div class="log-view-wrapper">
      <virtual-list
        style="overflow-y: auto"
        class="log-view"
        :data-key="'id'"
        :data-sources="items"
        :data-component="itemComponent"
      />
    </div>
  </div>
</template>

<script>
import virtualList from "vue-virtual-scroll-list";
import Item from "./LogItem";

export default {
  components: { "virtual-list": virtualList },
  props: {
    msg: String,
  },
  data() {
    return {
      itemComponent: Item,
      items: [],
      num: 0,
      taskId: "",
    };
  },
  watch: {
    $route() {
      this.closeWS();
      this.taskId = this.$route.params.taskId;
      
      this.initWebSocket();
      this.handdleMsg();
    },
  },

  created() {
    // console.log(this.$route.params);
    this.taskId = this.$route.params.taskId;
    this.initWebSocket();
    this.handdleMsg();
  },

  methods: {
    closeWS() {
      let that = this;
      that.ws.close(); //离开路由之后断开websocket连接
      that.items = [];
    },
    initWebSocket() {
      let that = this;
      console.log(`ws://127.0.0.1:8000/ws/${that.taskId}`);
      that.ws = new WebSocket(`ws://127.0.0.1:8000/ws/${that.taskId}`);
      that.global.setWs(that.ws);
      that.ws.onerror = that.websocketonerror;
      that.ws.onclose = that.websocketclose;
    },

    // 接收消息
    handdleMsg() {
      let that = this;

      that.global.ws.onmessage = function (res) {
        console.log("收到服务器内容", res.data);
        const redata = res.data;
        // 直接赋值而非push
        that.items = JSON.parse(redata);
      };
    },

    websocketonerror() {
      let that = this;
      that.initWebSocket(that.taskId);
    },

    websocketclose(e) {
      console.log("webSocket TM直接断开", e);
    },
  },
};
</script>



<style scoped>
.log-desc {
  font-size: 12px;
  color: rgb(102, 90, 90);
  margin-right: 10px;
}

.filter-wrapper {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}
.content {
  display: block;
}
.log-view-wrapper {
  float: left;
  flex-basis: calc(100% - 240px);
  width: calc(100%);
  transition: width 0.3s;
}

.log-view {
  margin-top: 0 !important;
  overflow-y: scroll !important;
  height: 800px;
  list-style: none;
  color: #a9b7c6;
  background: #2b2b2b;
  border: none;
}
.errors-wrapper.collapsed {
  width: 0;
}
.errors-wrapper .error-list {
  list-style: none;
  padding: 0;
  margin: 0;
}
.errors-wrapper .error-list .error-item {
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
  /*height: 18px;*/
  border-bottom: 1px solid white;
  padding: 5px 0;
  background: #f56c6c;
  color: white;
  cursor: pointer;
}
.errors-wrapper .error-list .error-item.active {
  background: #e6a23c;
  font-weight: bolder;
  text-decoration: underline;
}
.errors-wrapper .error-list .error-item:hover {
  font-weight: bolder;
  text-decoration: underline;
}
.errors-wrapper .error-list .error-item .line-no {
  display: inline-block;
  text-align: right;
  width: 70px;
}
.errors-wrapper .error-list .error-item .line-content {
  display: inline;
  width: calc(100% - 70px);
  padding-left: 10px;
}
.right {
  display: flex;
  align-items: center;
}
.right .el-pagination {
  margin-right: 10px;
}
</style>