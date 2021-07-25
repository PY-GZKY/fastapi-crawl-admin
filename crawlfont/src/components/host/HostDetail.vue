<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-lx-calendar"></i> 节点
        </el-breadcrumb-item>
        <el-breadcrumb-item>节点详情</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <div>
      <el-card style="border-radius: 0">
        <div>
          <span class="cpu">
            <el-link type="warning"
              >{{ hostDetail.hostInfo.hostName }} ({{
                hostDetail.hostInfo.desc
              }})</el-link
            >
            <el-divider></el-divider>
            <span>{{ hostDetail.hostInfo.info }}</span>
          </span>

          <el-divider></el-divider>

          <span class="cpu">
            <el-link type="warning">{{ hostDetail.hostInfo.pyInfo }}</el-link>
          </span>
          <el-divider></el-divider>

          <span class="cpu">
            <el-input
              type="textarea"
              rows="24"
              placeholder="请输入内容"
              v-model="hostDetail.hostInfo.pipInfo"
            >
            </el-input>
          </span>
          <el-divider></el-divider>
        </div>
      </el-card>
    </div>
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
import { hostDetail, getRsaPrivateKey } from "../../api/index";
export default {
  inject: ["reload"],

  data() {
    return {
      hostDetail: "",
      currentPage: 1, //初始页
      pagesize: 15, //    每页的数据
      activeNames: ["1"],
      rsaPrivateKey:
        "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCys67ZVQziSBQAK8q1lGU3QBkMVOEUi6XdE9XmWqHJDiS/OYMY6CYpYH4gvBfhTYAscgQQO2uVn4MbbLNV1R5QNpSdY68BDLgJAWUpCLJc2M7Z/Tv/SoYqznX5yOXuA3PU5dovTayKg0KBGxsAMcdCyZdP3k+9KXL1Z6aIBlPvYAPFsf//gOK/9djxs4n19Soz+r7eyMlMQtVL1Gtl8iY2dC6rVibdKmYTPJ5kmYDFKo4LZGD4fpxuRNQeDmn45nrYCM/JaDlHQR5jF39IpAFlxzaOI+Ra+4UTVuJGZwNeHDzDGBwXkmrKsIFfmmFBce2EB7TvOoa/4GCJ1/EajtnP hp@DESKTOP-J85G6E5",
    };
  },

  created() {
    this.loadHostDetail();
  },

  methods: {
    loadHostDetail() {
      hostDetail({
        uuid: this.$route.params.uuid,
      }).then((res) => {
        this.hostDetail = res.data;
        console.log(this.hostDetail);
      });
    },

    getRsaPrivateKey() {
      var data = {
        hostId: 3,
      };
      getRsaPrivateKey(data).then((res) => {
        if (res.data.code === 200) {
          this.$message.success(res.data.message);
        } else {
          this.$message.warning(res.data.message);
        }
      });
    },

    // 初始页currentPage、初始每页数据数pagesize和数据data
    handleSizeChange: function (size) {
      this.pagesize = size;
      // console.log(this.pagesize); //每页下拉显示数据
    },
    handleCurrentChange: function (currentPage) {
      this.currentPage = currentPage;
      // console.log(this.currentPage); //点击第几页
    },
  },
};
</script>
 
 
 