<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item
          ><i class="el-icon-lx-calendar"></i> 图表</el-breadcrumb-item
        >
        <el-breadcrumb-item>图表分析</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <el-row :gutter="24">
      <el-col :span="24" class="mgb20" :offset="0">
        <el-card shadow="hover">
          <div shadow="hover" style="padding-bottom: 8px; color: #000">
            <div class="schart-box">
              <div class="Echarts">
                <div class="content-title">扯淡图</div>
                <div id="chart-line"></div>
              </div>
            </div>
          </div>
        </el-card>
      </el-col>
      <el-col :span="12" class="mgb20" :offset="0">
        <el-card shadow="hover">
          <div shadow="hover">
            <div class="schart-box">
              <div class="content-title">扯淡图</div>
              <div class="Echarts">
                <div id="chart-bar"></div>
              </div>
            </div>
          </div>
        </el-card>
      </el-col>
      <el-col :span="12" class="mgb20" :offset="0">
        <el-card shadow="hover">
          <div shadow="hover">
            <div class="schart-box">
              <div class="content-title">扯淡图</div>
              <div class="Echarts">
                <div id="chart-pie"></div>
              </div>
            </div>
          </div>
        </el-card>
      </el-col>

      <el-col :span="24" class="mgb20" :offset="0">
        <el-card shadow="hover">
          <div shadow="hover" style="padding-bottom: 8px; color: #000">
            <div class="schart-box">
              <div class="Echarts">
                <div id="chart-word"></div>
              </div>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>


<script>
import {
  systemTestCharts,
  uploadWordExcel,
  uploadWordMongo,
} from "../../api/index";
import echarts from "echarts";
import "echarts-wordcloud";
export default {
  data() {
    return {
      systemTestChartsDict: {},
      dialogFormVisible: false,
      dialogDownVisible: false,
      loading: false,
      limit: 1,
      sizeLimit: 100,
      uploadType: "Excel",
      defaultWords: [
        {
          name: "十九大精神",
          value: 15000,
        },
        {
          name: "两学一做",
          value: 10081,
        },
        {
          name: "中华民族",
          value: 9386,
        },
        {
          name: "马克思主义",
          value: 7500,
        },
        {
          name: "民族复兴",
          value: 7500,
        },
        {
          name: "社会主义制度",
          value: 6500,
        },
        {
          name: "国防白皮书",
          value: 6500,
        },
        {
          name: "创新",
          value: 6000,
        },
        {
          name: "民主革命",
          value: 4500,
        },
        {
          name: "文化强国",
          value: 3800,
        },
        {
          name: "国家主权",
          value: 3000,
        },
        {
          name: "武装颠覆",
          value: 2500,
        },
        {
          name: "领土完整",
          value: 2300,
        },
        {
          name: "安全",
          value: 2000,
        },
        {
          name: "从严治党",
          value: 1900,
        },
        {
          name: "现代化经济体系",
          value: 1800,
        },
        {
          name: "国防动员",
          value: 1700,
        },
        {
          name: "信息化战争",
          value: 1600,
        },
        {
          name: "局部战争",
          value: 1500,
        },
        {
          name: "教育",
          value: 1200,
        },
        {
          name: "职业教育",
          value: 1100,
        },
        {
          name: "兵法",
          value: 900,
        },
        {
          name: "一国两制",
          value: 800,
        },
        {
          name: "特色社会主义思想",
          value: 700,
        },
      ],
    };
  },
  name: "Echarts",
  methods: {
    myEcharts() {
      //初始化多个 echarts实例
      var myChart = this.$echarts.init(
        document.getElementById("chart-line"),
        null,
        { renderer: "svg" }
      );
      var myChart1 = this.$echarts.init(
        document.getElementById("chart-bar"),
        null,
        { renderer: "svg" }
      );
      var myChart2 = this.$echarts.init(
        document.getElementById("chart-pie"),
        null,
        { renderer: "svg" }
      );

      var myChart3 = this.$echarts.init(
        document.getElementById("chart-word"),
        null,
        { renderer: "svg" }
      );

      var colors = ["#5793f3", "#d14a61", "#675bba"];

      var option1 = {
        title: {
          text: "某站点用户访问来源",
          subtext: "纯属虚构",
          left: "center",
        },
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {c} ({d}%)",
        },
        legend: {
          orient: "vertical",
          left: "left",
          data: ["直接访问", "邮件营销", "联盟广告", "视频广告", "搜索引擎"],
        },
        series: [
          {
            name: "访问来源",
            type: "pie",
            radius: "55%",
            center: ["50%", "60%"],
            data: this.systemTestChartsDict.systemTestCharts1,
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)",
              },
            },
          },
        ],
      };
      var option2 = {
        xAxis: {
          type: "category",
          boundaryGap: false,
        },
        yAxis: {
          type: "value",
          boundaryGap: [0, "30%"],
        },
        visualMap: {
          type: "piecewise",
          show: false,
          dimension: 0,
          seriesIndex: 0,
          pieces: [
            {
              gt: 1,
              lt: 3,
              color: "rgba(0, 180, 0, 0.5)",
            },
            {
              gt: 5,
              lt: 7,
              color: "rgba(0, 180, 0, 0.5)",
            },
          ],
        },
        series: [
          {
            type: "line",
            smooth: 0.6,
            symbol: "none",
            lineStyle: {
              color: "green",
              width: 5,
            },
            markLine: {
              symbol: ["none", "none"],
              label: { show: false },
              data: [{ xAxis: 1 }, { xAxis: 3 }, { xAxis: 5 }, { xAxis: 7 }],
            },
            areaStyle: {},
            data: this.systemTestChartsDict.systemTestCharts2,
          },
        ],
      };

      var option3 = {
        title: {
          text: "绿吕评论词云图",
          x: "center",
        },
        backgroundColor: "#fff",

        tooltip: {
          pointFormat: "{series.name}: <b>{point.percentage:.1f}%</b>",
        },
        series: [
          {
            type: "wordCloud",
            maskImage: maskImage,
            //用来调整词之间的距离
            gridSize: 10,
            //用来调整字的大小范围
            // Text size range which the value in data will be mapped to.
            // Default to have minimum 12px and maximum 60px size.
            sizeRange: [12, 60],
            // Text rotation range and step in degree. Text will be rotated randomly in range [-90,                                                                             90] by rotationStep 45
            //用来调整词的旋转方向，，[0,0]--代表着没有角度，也就是词为水平方向，需要设置角度参考注释内容
            rotationRange: [-45, 0, 45, 90],
            rotationRange: [0, 90],

            rotationRange: [0, 0],
            //随机生成字体颜色
            textStyle: {
              normal: {
                color: function () {
                  return (
                    "rgb(" +
                    [
                      Math.round(Math.random() * 256),
                      Math.round(Math.random() * 256),
                      Math.round(Math.random() * 256),
                    ].join(",") +
                    ")"
                  );
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
            data: this.defaultWords,
          },
        ],
      };

      var category = this.systemTestChartsDict.systemTestCharts0.category;
      var dottedBase = +new Date();
      var lineData = this.systemTestChartsDict.systemTestCharts0.lineData;
      var barData = this.systemTestChartsDict.systemTestCharts0.barData;

      // for (var i = 0; i < 60; i++) {
      //   var date = new Date((dottedBase += 3600 * 24 * 1000));
      //   category.push(
      //     [date.getFullYear(), date.getMonth() + 1, date.getDate()].join("-")
      //   );
      //   var b = Math.random() * 200;
      //   var d = Math.random() * 200;
      //   barData.push(b);
      //   lineData.push(d + b);
      // }

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
            name: "line55555",
            type: "line",
            smooth: true,
            showAllSymbol: true,
            symbol: "emptyCircle",
            symbolSize: 15,
            data: lineData,
          },
          {
            name: "bar55555",
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
            name: "line5555555",
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
            name: "dotted5555555",
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

      // todo 使用刚指定的配置项和数据显示图表。
      this.$nextTick(function () {});
      myChart.setOption(option);
      myChart1.setOption(option1);
      myChart2.setOption(option2);

      var maskImage = new Image();
      // todo 背景图
      maskImage.src =
        "https://img-blog.csdnimg.cn/2020021201012593.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjI5NDUxNw==,size_16,color_FFFFFF,t_70";
      maskImage.onload = function () {
        myChart3.setOption(option3);
      };
    },

    // todo 上传前钩子函数
    beforeUpload(file) {
      const limit = file.size / 1024 / 1024 < this.sizeLimit;
      if (!limit) {
        this.$message.error(`上传的文件小不能超过 ${this.sizeLimit} MB!`);
      }
      if (limit) {
        this.loading = true;
      }
      return limit;
    },

    upload(param) {
      var self = this;
      const formData = new FormData();
      formData.append("file", param.file);
      self.$api
        .uploadWordExcel(formData)
        .then((res) => {
          this.loading = false;
          console.log(res);
          this.defaultWords = res.data.data;
          self.$message.success({
            dangerouslyUseHTMLString: true,
            message: res.data.message,
          });
        })
        .catch(function (error) {
          console.log("error");
        });
    },

    mongoToWord() {
      var self = this;
      self.$api
        .uploadWordMongo()
        .then((res) => {
          this.defaultWords = res.data.data;
        })
        .catch(function (error) {
          console.log("error");
        });
    },

    loadSystemCharts() {
      systemTestCharts().then((res) => {
        this.systemTestChartsDict = res.data.data;
        this.myEcharts();
      });
    },
  },

  mounted() {
    this.mongoToWord();
    this.loadSystemCharts();
  },
};
</script>





<style scoped>
#chart-bar,
#chart-pie {
  width: 800px;
  height: 300px;
  margin: 0;
  padding: 0;
  list-style: none;
}

#chart-line {
  width: 1600px;
  height: 500px;
  margin: 0;
  padding: 0;
  list-style: none;
}

#chart-word {
  width: 1600px;
  height: 500px;
  margin: 0;
  padding: 0;
  list-style: none;
}

.schart {
  width: 800px;
  height: 400px;
  background-color: white;
  margin: 0;
  padding: 0;
  list-style: none;
}

.schart-box {
  display: inline-block;
  background-color: white;
}

.content-title {
  clear: both;
  font-weight: 400;
  line-height: 30px;
  margin: 8px 8px;
  font-size: 20px;
  color: #1f2f3d;
}
</style>