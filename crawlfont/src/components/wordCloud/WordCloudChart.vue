<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item
          ><i class="el-icon-lx-calendar"></i> 词云</el-breadcrumb-item
        >
        <el-breadcrumb-item>词云分析</el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div class="handle-select">
      查看实时词云图
      <el-button type="primary" size="small" @click="dialogFormVisible = true"
        >上传表格</el-button
      >
    </div>

    <el-row :gutter="24">
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

    <el-dialog title="上传文件" :visible.sync="dialogFormVisible" width="35%">
      <div
        class="upload-demo"
        v-if="loading"
        v-loading="loading"
        element-loading-text="数据上传中"
        element-loading-spinner="el-icon-loading"
        element-loading-background="white"
      ></div>

      <el-upload
        v-else
        class="upload-demo"
        drag
        action=""
        :http-request="upload"
        :limit="limit"
        :before-upload="beforeUpload"
        multiple
      >
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
        <div class="el-upload__tip" slot="tip">
          只能上传 {{ uploadType }} 文件，且不超过 {{ sizeLimit }} M
        </div>
      </el-upload>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="dialogFormVisible = false"
          >确 定</el-button
        >
      </div>
    </el-dialog>
  </div>
</template>

<style scoped>
.mgb20{
  height: 100%;
}
.upload-demo {
  margin-top: 0px;
  height: 150px;
}
.crumbs {
  margin-top: 0px;
}
.dialog-conent {
  margin-left: 15px;
}
.handle-box {
  margin-bottom: 15px;
}

.handle-select {
  width: 140px;
  margin-bottom: 10px;
}

.handle-input {
  width: 300px;
  display: inline-block;
}
.table {
  width: 100%;
  font-size: 12px;
}
.red {
  color: #ff0000;
}
.mr10 {
  margin-right: 10px;
}
.table-td-thumb {
  display: block;
  margin: auto;
  width: 40px;
  height: 40px;
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


<script>
import echarts from "echarts";
import "echarts-wordcloud";
import { uploadWordExcel } from "../../api/index";
export default {
  name: "app",
  data() {
    return {
      dialogFormVisible: false,
      dialogDownVisible: false,
      loading: false,
      limit: 1,
      sizeLimit: 100,
      uploadType: "Excel",
      myColors: ["#1f77b4", "#629fc9", "#94bedb", "#c9e0ef"],
      defaultWords: [],
    };
  },
  methods: {
    myEcharts() {
      //初始化多个 echarts实例
      var myChart3 = this.$echarts.init(
        document.getElementById("chart-word"),
        null,
        { renderer: "svg" }
      );

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

      // todo 使用刚指定的配置项和数据显示图表。
      this.$nextTick(function () {});
      myChart3.setOption(option3);
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
          this.myEcharts();
        })
        .catch(function (error) {
          console.log("error");
        });
    },
  },

  mounted() {
    this.myEcharts();
  },
};
</script>


