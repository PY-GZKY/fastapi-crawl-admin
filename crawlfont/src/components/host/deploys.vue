
<template>
  <div>
    <div class="container">
      <div class="form-box">
        <el-form ref="form" :model="form" label-width="80px">
          <el-form-item label="" style="font-weight: bold; font-size: 20px">
            <el-col
              >暂时只支持命令行部署,你知道真正自动化一键部署并有效监控这个过程是艰难的</el-col
            >
            <el-col
              >等我把这个功能测全了,尝试做成可视化远程安装服务,目前大部分都基于 PIP 包构建,不够深度</el-col
            >
          </el-form-item>

          <el-form-item
            label="执行命令"
            style="font-weight: bold; font-size: 20px"
          >
            <el-input
              v-model="form.cmd"
              clearable
              placeholder="请输入 cmd"
            ></el-input>
          </el-form-item>

          <el-form-item label="选择节点">
            <el-checkbox-group v-model="form.hosts" v-if="hostList.length>0">
              <el-checkbox
                v-for="(item, index) in hostList"
                :label="item.ip"
                :key="item.ip"
                @change="handleCheckedHostChange"
                >{{ item.ip }}</el-checkbox
              >
            </el-checkbox-group>

            <el-link v-else type="warning" :underline="false">好像找不到节点? </el-link>
          </el-form-item>
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
import { startTask, deployServer,hostList } from "../../api/index";
export default {
  data() {
    return {
      form: {
        cmd: "yum -y install wget",
        hosts: [],
      },
      hostList: [],
    };
  },
  created() {
    this.loadHostList();
  },

  methods: {
    onSubmit() {
      var data = this.form;
      console.log(data);
      // 考虑加个遮罩层,避免重复安装服务
      this.$message.success("安装中");
      deployServer(data).then((res) => {
        if (res.data.code === 200) {
          this.$notify({
            title: "成功",
            message:"服务部署成功 " +
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
        console.log(this.hostList);
      });
    },

    handleCheckedHostChange() {
      console.log(this.form.host);
    },
  },
};
</script>

