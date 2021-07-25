<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-lx-calendar"></i> 主机
        </el-breadcrumb-item>
        <el-breadcrumb-item>任务部署</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <div>
      <el-link type="warning">
        警告: 该操作将会从主节点中的项目上传至从机的 <b>{{ detail.taskPath }}</b>
        目录
      </el-link>
    </div>
    <div class="container">
      <div class="form-box">
        <el-form ref="form" :model="form" label-width="80px">
          <el-form-item label="任务名称" style="font-weight: bold; font-size: 20px">
            <el-col>{{ detail.taskName }} ({{ detail.taskId }})</el-col>
          </el-form-item>

          <el-form-item label="批量部署">
            <el-checkbox-group v-model="form.hosts">
              <el-checkbox
                v-for="(item, index) in hostList"
                :key="index"
                :label="item.ip"
                @change="handleCheckedHostChange"
              >{{ item.ip }}</el-checkbox>
            </el-checkbox-group>
          </el-form-item>

          <el-form-item>
            <el-button type="primary" @click="onDeploySubmit">确认部署</el-button>
          </el-form-item>
        </el-form>
      </div>

      <div>
        <el-button type="text" disabled>已部署的节点</el-button>
        <el-button
          type="success"
          plain
          v-for="(item, index) in detail.deployedHosts"
          :key="index"
        >{{item}}</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import { hostList, taskDetail, deployTask } from "../../api/index";
export default {
  name: "baseform",
  data() {
    return {
      hostList: [],
      detail: {},
      form: {
        taskId: "",
        hosts: [],
      },
    };
  },

  created() {
    this.form.taskId = this.$route.params.taskId;
    console.log(this.form.taskId);
    this.loadDetail();
    this.loadHostList();
  },
  methods: {
    onDeploySubmit() {
      var data = this.form;
      console.log(data);
      deployTask(data).then((res) => {
        this.$message.success(res.data.message);
      });
    },

    loadDetail() {
      taskDetail({
        taskId: this.$route.params.taskId,
      }).then((res) => {
        this.detail = res.data.data;
      });
    },

    loadHostList() {
      hostList().then((res) => {
        this.hostList = res.data.data;
      });
    },
  },
};
</script>