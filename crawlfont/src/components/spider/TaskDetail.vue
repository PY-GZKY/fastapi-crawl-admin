
<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-lx-global"></i>
          {{ detail.taskName }}
        </el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div class="container">
      <div class="update-time">
        <span>
          <i class="el-icon-time"></i> 最近一次更新时间
        </span>
        <br />
        <time class="time">{{detail.lastRunTime}}</time>
      </div>

      <div class="form-box">
        <el-form ref="form" :model="form" label-width="80px">
          <el-form-item label="爬虫名称" style="font-weight: bold; font-size: 20px">
            <el-col>{{ detail.taskName }} ({{ detail.taskId }})</el-col>
          </el-form-item>

          <!-- <el-form-item
            label="日期时间"
            style="font-weight: bold; font-size: 20px"
          >
            <el-col :span="11">
              <el-date-picker
                type="date"
                placeholder="选择日期"
                v-model="form.date"
                value-format="yyyy-MM-dd"
                style="width: 100%"
              ></el-date-picker>
            </el-col>
            <el-col class="line" :span="2">-</el-col>
            <el-col :span="11">
              <el-time-picker
                placeholder="选择时间"
                v-model="form.date_time"
                style="width: 100%"
              ></el-time-picker>
            </el-col>
          </el-form-item>-->

          <!-- <el-form-item
            label="定时任务"
            style="font-weight: bold; font-size: 20px"
          >
            <el-switch v-model="form.delivery"></el-switch>
          </el-form-item>-->

          <el-form-item label="执行命令" style="font-weight: bold; font-size: 20px">
            <el-input v-model="form.cmd" clearable placeholder="请输入 cmd"></el-input>
          </el-form-item>

          <el-form-item label="选择节点">
            <el-checkbox-group v-model="form.hosts" v-if="detail.deployedHosts.length>0">
              <el-checkbox
                v-for="(item, index) in detail.deployedHosts"
                :key="index"
                :label="item"
                @change="handleCheckedHostChange"
              >{{ item }}</el-checkbox>
            </el-checkbox-group>
            <el-link v-else type="warning" :underline="false">还没部署节点? </el-link>
          </el-form-item>
          <!-- <el-form-item
            label="Cookie"
            style="font-weight: bold; font-size: 20px"
          >
            <el-input type="textarea" rows="5" v-model="form.cookie"></el-input>
          </el-form-item>-->

          <!-- <el-form-item
            label="并发度"
            style="font-weight: bold; font-size: 20px"
          >
            <el-slider v-model="form.bing"></el-slider>
          </el-form-item>-->
          <el-form-item>
            <el-button type="primary" @click="onSubmit">运行</el-button>
            <el-button>取消</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>


<style>
.update-time {
  font-size: 14px;
  position: absolute;
  left: 85%;
  top: 100px;
}
.desc {
  color: rgb(97, 94, 94);
  font-size: 12px;
}
</style>

<script>
import { taskDetail, startTask, hostList } from "../../api/index";

export default {
  name: "baseform",
  data() {
    return {
      form: {
        taskId: "",
        hosts: [],
        cmd: "",
        // date: "",
        // date_time: "",
        // delivery: true,
        // cookie: "",
        // bing: 60,
      },
      cmd: "输入cmd命令",
      detail: {},
      hostList: [],
    };
  },
  created() {
    this.form.taskId = this.$route.params.taskId;
    this.loadDetail();
    this.loadHostList();
  },
  methods: {
    loadDetail() {
      taskDetail({
        taskId: this.$route.params.taskId,
      }).then((res) => {
        this.detail = res.data.data;
      });
    },
    onSubmit() {
      var data = this.form;
      console.log(data);
      this.$message.success("抓取中");
      startTask(data).then((res) => {
        if (res.data.code === 200) {
          this.$notify({
            title: "成功",
            message:
              res.data.data.taskName +
              " 更新成功 " +
              new Date().toLocaleTimeString(),
            type: "success",
            duration: 0,
          });
        } else {
          this.$message.error(res.data);
        }
      });
    },

    loadHostList() {
      hostList().then((res) => {
        this.hostList = res.data.data;
      });
    },

    handleCheckedHostChange() {
      console.log(this.form.host);
    },
  },
};
</script>

