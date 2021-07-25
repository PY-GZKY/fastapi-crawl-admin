<template>
  <div class="Echarts">
    <div id="main" style="width: 800px; height: 400px"></div>
  </div>
</template>

<script>
export default {
  name: "Echarts",
  methods: {
    myEcharts() {
      // 基于准备好的dom，初始化echarts实例
      var myChart = this.$echarts.init(document.getElementById("main"));

      // var option1 = {
      //   title: {
      //     text: "某站点用户访问来源",
      //     subtext: "纯属虚构",
      //     left: "center",
      //   },
      //   tooltip: {
      //     trigger: "item",
      //     formatter: "{a} <br/>{b} : {c} ({d}%)",
      //   },
      //   legend: {
      //     orient: "vertical",
      //     left: "left",
      //     data: ["直接访问", "邮件营销", "联盟广告", "视频广告", "搜索引擎"],
      //   },
      //   series: [
      //     {
      //       name: "访问来源",
      //       type: "pie",
      //       radius: "55%",
      //       center: ["50%", "60%"],
      //       data: [
      //         { value: 335, name: "直接访问" },
      //         { value: 310, name: "邮件营销" },
      //         { value: 234, name: "联盟广告" },
      //         { value: 135, name: "视频广告" },
      //         { value: 1548, name: "搜索引擎" },
      //       ],
      //       emphasis: {
      //         itemStyle: {
      //           shadowBlur: 10,
      //           shadowOffsetX: 0,
      //           shadowColor: "rgba(0, 0, 0, 0.5)",
      //         },
      //       },
      //     },
      //   ],
      // };
      // var option2 = {
      //   title: {
      //     text: "某站点用户访问来源",
      //     subtext: "纯属虚构",
      //     left: "center",
      //   },
      //   tooltip: {
      //     trigger: "item",
      //     formatter: "{a} <br/>{b} : {c} ({d}%)",
      //   },
      //   legend: {
      //     orient: "vertical",
      //     left: "left",
      //     data: ["直接访问", "邮件营销", "联盟广告", "视频广告", "搜索引擎"],
      //   },
      //   series: [
      //     {
      //       name: "访问来源",
      //       type: "pie",
      //       // radius: "55%",
      //       radius: [20, 110],
      //       center: ["25%", "50%"],
      //       data: [
      //         { value: 335, name: "直接访问" },
      //         { value: 310, name: "邮件营销" },
      //         { value: 234, name: "联盟广告" },
      //         { value: 135, name: "视频广告" },
      //         { value: 1548, name: "搜索引擎" },
      //       ],
      //       emphasis: {
      //         itemStyle: {
      //           shadowBlur: 10,
      //           shadowOffsetX: 0,
      //           shadowColor: "rgba(0, 0, 0, 0.5)",
      //         },
      //       },
      //     },
      //     {
      //       name: "rrrr",
      //       type: "pie",
      //       // radius: "55%",
      //       radius: [30, 110],
      //       center: ["75%", "50%"],
      //       data: [
      //         { value: 335, name: "直接访问" },
      //         { value: 310, name: "邮件营销" },
      //         { value: 234, name: "联盟广告" },
      //         { value: 135, name: "视频广告" },
      //         { value: 1548, name: "搜索引擎" },
      //       ],
      //       emphasis: {
      //         itemStyle: {
      //           shadowBlur: 10,
      //           shadowOffsetX: 0,
      //           shadowColor: "rgba(0, 0, 0, 0.5)",
      //         },
      //       },
      //     },

      //     {
      //       name: "rrrr",
      //       type: "pie",
      //       // radius: "55%",
      //       radius: [30, 110],
      //       center: ["25%", "12%"],
      //       data: [
      //         { value: 335, name: "直接访问" },
      //         { value: 310, name: "邮件营销" },
      //         { value: 234, name: "联盟广告" },
      //         { value: 135, name: "视频广告" },
      //         { value: 1548, name: "搜索引擎" },
      //       ],
      //       emphasis: {
      //         itemStyle: {
      //           shadowBlur: 10,
      //           shadowOffsetX: 0,
      //           shadowColor: "rgba(0, 0, 0, 0.5)",
      //         },
      //       },
      //     },
      //   ],
      // };

      var category = [];
      var dottedBase = +new Date();
      var lineData = [];
      var barData = [];

      for (var i = 0; i < 20; i++) {
        var date = new Date((dottedBase += 3600 * 24 * 1000));
        category.push(
          [date.getFullYear(), date.getMonth() + 1, date.getDate()].join("-")
        );
        var b = Math.random() * 200;
        var d = Math.random() * 200;
        barData.push(b);
        lineData.push(d + b);
      }

      console.log(category);
      console.log(dottedBase);
      console.log(lineData);
      console.log(barData);

      // option
      var option = {
        backgroundColor: "#0f375f",
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "shadow",
          },
        },
        legend: {
          data: ["line", "bar"],
          textStyle: {
            color: "#ccc",
          },
        },
        xAxis: {
          data: category,
          axisLine: {
            lineStyle: {
              color: "#ccc",
            },
          },
        },
        yAxis: {
          splitLine: { show: false },
          axisLine: {
            lineStyle: {
              color: "#ccc",
            },
          },
        },
        series: [
          {
            name: "line",
            type: "line",
            smooth: true,
            showAllSymbol: true,
            symbol: "emptyCircle",
            symbolSize: 15,
            data: lineData,
          },
          {
            name: "bar",
            type: "bar",
            barWidth: 10,
            itemStyle: {
              barBorderRadius: 5,
              color: new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                { offset: 0, color: "#14c8d4" },
                { offset: 1, color: "#43eec6" },
              ]),
            },
            data: barData,
          },
          {
            name: "line",
            type: "bar",
            barGap: "-100%",
            barWidth: 10,
            itemStyle: {
              color: new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                { offset: 0, color: "rgba(20,200,212,0.5)" },
                { offset: 0.2, color: "rgba(20,200,212,0.2)" },
                { offset: 1, color: "rgba(20,200,212,0)" },
              ]),
            },
            z: -12,
            data: lineData,
          },
          {
            name: "dotted",
            type: "pictorialBar",
            symbol: "rect",
            itemStyle: {
              color: "#0f375f",
            },
            symbolRepeat: true,
            symbolSize: [12, 4],
            symbolMargin: 1,
            z: -10,
            data: lineData,
          },
        ],
      };



      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option);
      // myChart.setOption(option2);
    },
  },
  mounted() {
    this.myEcharts();
  },
};
</script>

<style>
</style>
