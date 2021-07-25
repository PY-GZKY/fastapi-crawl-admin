<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-lx-calendar"></i> 节点
        </el-breadcrumb-item>
        <el-breadcrumb-item>节点公钥</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <div>
      <el-card style="border-radius: 0">
        <div>
          <span
            ><i style="font-weight: bold" class="el-icon-key"></i>
            主节点SSH公钥

            <el-input
              type="textarea"
              v-model="rsaPrivateKey"
              rows="6"
            ></el-input>
          </span>
        </div>
      </el-card>
    </div>
    <!-- 这里将公钥推送至各服务器,实现免密登录,多选节点推送　rsa_id.pud 中的公钥
    单个免密可以在主机节点列表中开启,之所以要实现免密登录是因为有一些服务器上的任务高频率的调用,秘钥登录则更合理 -->
  </div>
</template>

<style>
.install {
  margin-top: 20px;
}
.el-table .warning-row {
  background: oldlace;
}

.el-table .success-row {
  background: #f0f9eb;
}

.pagination-footer .description {
  float: left;
  margin-left: 20px;
  margin-top: 12px;
}
.pagination-footer .el-pagination {
  float: right;
  margin-top: 8px;
  margin-bottom: 8px;
}

.cpu {
  white-space: pre-line;
}
</style>

<script>
import {} from "../../api/index";
export default {
  inject: ["reload"],

  data() {
    return {
      hostDetail: "",
      activeNames: ["1"],
      rsaPrivateKey:
        "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCys67ZVQziSBQAK8q1lGU3QBkMVOEUi6XdE9XmWqHJDiS/OYMY6CYpYH4gvBfhTYAscgQQO2uVn4MbbLNV1R5QNpSdY68BDLgJAWUpCLJc2M7Z/Tv/SoYqznX5yOXuA3PU5dovTayKg0KBGxsAMcdCyZdP3k+9KXL1Z6aIBlPvYAPFsf//gOK/9djxs4n19Soz+r7eyMlMQtVL1Gtl8iY2dC6rVibdKmYTPJ5kmYDFKo4LZGD4fpxuRNQeDmn45nrYCM/JaDlHQR5jF39IpAFlxzaOI+Ra+4UTVuJGZwNeHDzDGBwXkmrKsIFfmmFBce2EB7TvOoa/4GCJ1/EajtnP hp@DESKTOP-J85G6E5",
    };
  },

  created() {},

  methods: {},
};
</script>
 
 
 