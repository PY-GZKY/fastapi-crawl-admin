
<template>
  <div class="log-item" style="style" :class="`log-item-${source.index}`">
    <!-- <div class="line-no">{{ source.index }}</div> -->
    <div :class="['line-content', color]">
      <div>{{ source.updateTime }}</div>
      <div id="gang">|</div>
      <div>{{ source.taskLogLevel }}</div>
      <div id="gang">|</div>
        <div>{{ source.host }} </div>
      <div id="gang">|</div>
      <div>{{ source.taskLogMsg }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LogItem",
  props: {
    index: {
      // index of current item
      type: Number,
    },
    source: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  data() {
    return {};
  },
  computed: {
    isLogEnd() {
      return this.source.data === "###LOG_END###";
    },
    color() {
      switch (this.source.taskLogLevel) {
        case "WARN":
          return "yellow";
          break;
        case "DEBUG":
          return "skyblue";
          break;
        case "INFO":
          return "white";
          break;
        case "ERROR":
          return "red";
          break;
      }
    },
  },
};
</script>

<style scoped>
#gang {
  margin-right: 10px;
  text-align: center;
}
.log-item {
  display: block;
}
.log-item:hover {
  background: rgba(55, 57, 59, 0.5);
}
.log-item:first-child .line-no {
  padding-top: 10px;
  text-align: right;
}
.red {
  color: #ffb3b3;
}
.skyblue {
  color: #06b8b8;
}
.white {
  color: white;
}
.yellow {
  color: rgb(194, 194, 79);
}
.pink {
  color: pink;
}
.log-item .line-no {
  display: inline-block;
  width: 120px;
  color: #a9b7c6;
  background: #313335;
  padding-right: 10px;
  text-align: right;
}
.log-item .line-content {
  padding-left: 10px;
  font-size: 12px;
  white-space: pre-line;
  display: flex;
  width: 400%;
}




.log-item .line-content div {
  text-align: center;
  min-width: 20px;
  /* margin-right: 15px; */
}
.loading-text {
  margin-right: 5px;
  animation: blink 2s ease-in infinite;
}
@keyframes blink {
  0% {
    opacity: 1;
  }
  50% {
    opacity: 0.3;
  }
  100% {
    opacity: 1;
  }
}
</style>