<template>
  <div id="box">
    <div ref="chart2" style="width: 100%; height: 400px"></div>
  </div>
</template>
<script>
import echarts from "echarts";
import 'echarts-wordcloud';

export default {
  name: "home",
  data() {
    return {
      timer: "7",
      worddata: [
        {
          name: "rest",
          value: 1500,
        },
        {
          name: "hadoop",
          value: 2000,
        },
        {
          name: "hive",
          value: 1000,
        },
        {
          name: "ftp",
          value: 1000,
        },
        {
          name: "csv",
          value: 1200,
        },
        {
          name: "xls",
          value: 1100,
        },
        {
          name: "xlsx",
          value: 1100,
        },
        {
          name: "txt",
          value: 1400,
        },
        {
          name: "mysql",
          value: 1000,
        },
        {
          name: "oracle",
          value: 1100,
        },
        {
          name: "rest",
          value: 2500,
        },
        {
          name: "hadoop",
          value: 2300,
        },
        {
          name: "hive",
          value: 2000,
        },
        {
          name: "ftp",
          value: 1900,
        },
        {
          name: "csv",
          value: 1800,
        },
        {
          name: "xls",
          value: 1700,
        },
        {
          name: "xlsx",
          value: 1600,
        },
        {
          name: "txt",
          value: 1500,
        },
        {
          name: "mysql",
          value: 1200,
        },
        {
          name: "oracle",
          value: 1100,
        },
        {
          name: "rest",
          value: 1500,
        },
        {
          name: "hadoop",
          value: 2000,
        },
        {
          name: "hive",
          value: 1000,
        },
        {
          name: "ftp",
          value: 1000,
        },
        {
          name: "csv",
          value: 1200,
        },
        {
          name: "xls",
          value: 1100,
        },
        {
          name: "xlsx",
          value: 1100,
        },
        {
          name: "txt",
          value: 1400,
        },
        {
          name: "mysql",
          value: 1000,
        },
        {
          name: "oracle",
          value: 1100,
        },
        {
          name: "rest",
          value: 1500,
        },
        {
          name: "hadoop",
          value: 2000,
        },
        {
          name: "hive",
          value: 1000,
        },
        {
          name: "ftp",
          value: 1000,
        },
        {
          name: "csv",
          value: 1200,
        },
        {
          name: "xls",
          value: 1100,
        },
        {
          name: "xlsx",
          value: 1100,
        },
        {
          name: "txt",
          value: 1400,
        },
        {
          name: "mysql",
          value: 1000,
        },
        {
          name: "oracle",
          value: 1100,
        },
        {
          name: "rest",
          value: 2500,
        },
        {
          name: "hadoop",
          value: 2400,
        },
        {
          name: "hive",
          value: 2300,
        },
        {
          name: "ftp",
          value: 2400,
        },
        {
          name: "csv",
          value: 2500,
        },
        {
          name: "xls",
          value: 3500,
        },
        {
          name: "xlsx",
          value: 2100,
        },
        {
          name: "txt",
          value: 2400,
        },
        {
          name: "mysql",
          value: 2000,
        },
        {
          name: "oracle",
          value: 2100,
        },
        {
          name: "rest",
          value: 2500,
        },
        {
          name: "hadoop",
          value: 2400,
        },
        {
          name: "hive",
          value: 2300,
        },
        {
          name: "ftp",
          value: 2400,
        },
        {
          name: "csv",
          value: 2500,
        },
        {
          name: "xls",
          value: 3500,
        },
        {
          name: "xlsx",
          value: 2100,
        },
        {
          name: "txt",
          value: 2400,
        },
        {
          name: "mysql",
          value: 2000,
        },
        {
          name: "oracle",
          value: 2100,
        },
        {
          name: "rest",
          value: 1500,
        },
        {
          name: "hadoop",
          value: 2000,
        },
        {
          name: "hive",
          value: 1000,
        },
        {
          name: "ftp",
          value: 1000,
        },
        {
          name: "csv",
          value: 1200,
        },
        {
          name: "xls",
          value: 1100,
        },
        {
          name: "xlsx",
          value: 1100,
        },
        {
          name: "txt",
          value: 1400,
        },
        {
          name: "mysql",
          value: 1000,
        },
        {
          name: "oracle",
          value: 1100,
        },
        {
          name: "rest",
          value: 1500,
        },
        {
          name: "hadoop",
          value: 2000,
        },
        {
          name: "hive",
          value: 1000,
        },
        {
          name: "ftp",
          value: 1000,
        },
        {
          name: "csv",
          value: 1200,
        },
        {
          name: "xls",
          value: 1100,
        },
        {
          name: "xlsx",
          value: 1100,
        },
        {
          name: "txt",
          value: 1400,
        },
        {
          name: "mysql",
          value: 1000,
        },
        {
          name: "oracle",
          value: 1100,
        },
        {
          name: "rest",
          value: 1500,
        },
        {
          name: "hadoop",
          value: 2000,
        },
        {
          name: "hive",
          value: 1000,
        },
        {
          name: "ftp",
          value: 1000,
        },
        {
          name: "csv",
          value: 1200,
        },
        {
          name: "xls",
          value: 1100,
        },
        {
          name: "xlsx",
          value: 1100,
        },
        {
          name: "txt",
          value: 1400,
        },
        {
          name: "mysql",
          value: 1000,
        },
        {
          name: "oracle",
          value: 1100,
        },
        {
          name: "rest",
          value: 1500,
        },
        {
          name: "hadoop",
          value: 2000,
        },
        {
          name: "hive",
          value: 1000,
        },
        {
          name: "ftp",
          value: 1000,
        },
        {
          name: "csv",
          value: 1200,
        },
        {
          name: "xls",
          value: 1100,
        },
        {
          name: "xlsx",
          value: 1100,
        },
        {
          name: "txt",
          value: 1400,
        },
        {
          name: "mysql",
          value: 1000,
        },
        {
          name: "oracle",
          value: 1100,
        },
      ],
    };
  },
  methods: {
    initCharts() {
      let myChart2 = echarts.init(this.$refs.chart2);
      myChart2.setOption({
        title: {
          //                        text: "热爱祖国",
          x: "center",
        },
        backgroundColor: "#fff",
        // tooltip: {
        //   pointFormat: "{series.name}: <b>{point.percentage:.1f}%</b>"
        // },
        series: [
          {
            type: "wordCloud",
            //用来调整词之间的距离
            gridSize: 10,
            //用来调整字的大小范围
            // Text size range which the value in data will be mapped to.
            // Default to have minimum 12px and maximum 60px size.
            sizeRange: [14, 60],
            // Text rotation range and step in degree. Text will be rotated randomly in range [-90,                                                                             90] by rotationStep 45
            //用来调整词的旋转方向，，[0,0]--代表着没有角度，也就是词为水平方向，需要设置角度参考注释内容
            // rotationRange: [-45, 0, 45, 90],
            // rotationRange: [ 0,90],
            /**
                         * "rgb(" +
                                        Math.round(Math.random() * 255) +
                                        ", " +
                                        Math.round(Math.random() * 255) +
                                        ", " +
                                        Math.round(Math.random() * 255) +
                                        ")"
                         */
            rotationRange: [0, 0],
            //随机生成字体颜色
            textStyle: {
              normal: {
                color: function () {
                  return "#7a828a";
                },
              },
            },
            //位置相关设置
            left: "center",
            top: "center",
            right: null,
            bottom: null,
            width: "200%",
            height: "200%",
            //数据
            data: this.worddata,
          },
        ],
      });
    },
  },
  components: {},
  mounted() {
    this.initCharts();
  },
};
</script>
 
<style >
#box {
  width: 100%;
  background: #f1f2f6;
}
.home {
  margin: 0 auto;
  width: calc(100% - 80px);
}
</style>