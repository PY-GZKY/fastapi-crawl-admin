<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-lx-calendar"></i> 节点
        </el-breadcrumb-item>
        <el-breadcrumb-item>主机节点</el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div>
      <el-card style="border-radius: 0">
        <div class="select">
          <div>
            <el-form label-position="right" :model="selectForm" inline>
              <el-form-item label="状态">
                <el-select
                  placeholder="全部"
                  v-model="selectForm.status"
                  @change="onChangeProSubmit"
                >
                  <el-option label="全部" />
                  <el-option value="1" label="在线" />
                  <el-option value="-1" label="离线" />
                  <el-option value="0" label="未知" />
                </el-select>
              </el-form-item>
            </el-form>
          </div>

          <el-button
            type="success"
            icon="el-icon-plus"
            @click="addHostVisible = true"
            >添加节点</el-button
          >
        </div>

        <div>
          <el-table :data="hostList" style="width: 100%,height:auto" border>
            <el-table-column
              prop="hostName"
              label="名称"
              width="150"
              align="center"
            ></el-table-column>
            <el-table-column
              prop="ip"
              label="IP"
              width="120"
              align="center"
            ></el-table-column>
            <el-table-column
              prop="port"
              label="端口"
              width="100"
              align="center"
            ></el-table-column>
            <el-table-column
              prop="username"
              label="用户名"
              width="100"
              align="center"
            ></el-table-column>
            <el-table-column
              prop="hostType"
              label="Type"
              width="100"
              align="center"
            >
              <template slot-scope="scope">
                <div>
                  <el-button
                    v-if="scope.row.hostType == 'master'"
                    style="font-weight: bold"
                    type="primary"
                    plain
                    size="mini"
                  >
                    <i style="font-weight: bold" size="mini"></i>
                    {{ scope.row.hostType }}
                  </el-button>
                  <el-button
                    v-else
                    style="font-weight: bold"
                    type="warning"
                    plain
                    size="mini"
                  >
                    <i style="font-weight: bold" size="mini"></i>
                    {{ scope.row.hostType }}
                  </el-button>
                </div>
              </template>
            </el-table-column>

            <el-table-column
              prop="hostStatus"
              label="状态"
              width="90"
              align="center"
            >
              <template slot-scope="scope">
                <div>
                  <el-button
                    v-if="scope.row.hostStatus == 1"
                    style="font-weight: bold"
                    type="success"
                    plain
                    size="mini"
                  >
                    <i style="font-weight: bold" size="mini"></i>
                    在线
                  </el-button>
                  <el-button
                    v-else-if="scope.row.hostStatus == 0"
                    style="font-weight: bold"
                    type="primary"
                    plain
                    size="mini"
                  >
                    <i style="font-weight: bold" size="mini"></i>
                    未知
                  </el-button>
                  <el-button
                    v-else
                    style="font-weight: bold"
                    type="info"
                    plain
                    size="mini"
                  >
                    <i style="font-weight: bold" size="mini"></i>
                    离线
                  </el-button>
                </div>
              </template>
            </el-table-column>

            <el-table-column label="免密登陆" width="90" align="center">
              <template slot-scope="scope">
                <el-switch
                  v-model="scope.row.isVerify"
                  active-color="#13ce66"
                  inactive-color="#ff4949"
                  @change="changeRsaVerify(scope.row.id)"
                ></el-switch>
                <div>
                  <el-button v-if="scope.row.isVerify" plain type="success"
                    >已开启</el-button
                  >
                  <!-- <el-tooltip v-else class="item" effect="dark" content="请前往授权" placement="top-start">
                    <el-button type="info" plain>未授权</el-button>
                  </el-tooltip> -->
                </div>
              </template>
            </el-table-column>

            <el-table-column
              prop="desc"
              label="描述"
              align="center"
            ></el-table-column>

            <el-table-column
              prop="submit"
              label="操作"
              align="center"
              width="290"
            >
              <template slot-scope="scope">
                <div>
                  <el-tooltip
                    class="item"
                    effect="dark"
                    content="详细信息"
                    placement="top-start"
                  >
                    <el-button
                      type="primary"
                      icon="el-icon-search"
                      @click="goHostDetail(scope.row.uuid)"
                    ></el-button>
                  </el-tooltip>

                  <el-tooltip
                    class="item"
                    effect="dark"
                    content="修改连接"
                    placement="top-start"
                  >
                    <el-button
                      type="info"
                      @click="goEdit(scope.row)"
                      icon="el-icon-edit"
                    ></el-button>
                  </el-tooltip>

                  <el-tooltip
                    class="item"
                    effect="dark"
                    content="安装依赖包"
                    placement="top-start"
                  >
                    <el-button type="warning" icon="el-icon-bottom"></el-button>
                  </el-tooltip>

                  <el-tooltip
                    class="item"
                    effect="dark"
                    content="测试连接"
                    placement="top-start"
                  >
                    <el-button
                      type="success"
                      icon="el-icon-s-promotion"
                      @click="testHost(scope.row.id, scope.row.ip)"
                    ></el-button>
                  </el-tooltip>

                  <el-tooltip
                    class="item"
                    effect="dark"
                    content="删除节点"
                    placement="top-start"
                  >
                    <el-button
                      type="danger"
                      icon="el-icon-delete"
                      @click="deleteHost(scope.row.id)"
                    ></el-button>
                  </el-tooltip>
                </div>
              </template>
            </el-table-column>
          </el-table>
        </div>
      </el-card>

      <div class="pagination-footer">
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="currentPage"
          :page-sizes="[15, 20, 40]"
          :page-size="pagesize"
          layout="total, sizes, prev, pager, next"
          :total="2"
        ></el-pagination>
      </div>

      <el-dialog title="添加主机" :visible.sync="addHostVisible" width="30%">
        <el-form ref="form" :model="createForm" label-width="70px">
          <el-form-item label="主机名称">
            <el-input
              v-model="createForm.hostName"
              placeholder="主机名称"
            ></el-input>
          </el-form-item>
          <el-form-item label="类型">
            <el-select v-model="createForm.hostType" placeholder="选择节点类型">
              <el-option
                key="主节点"
                :disabled="true"
                label="主节点(设定该节点为主节点)"
                value="主节点"
              ></el-option>
              <el-option
                key="工作节点"
                label="工作节点"
                value="工作节点"
              ></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="IP">
            <el-input v-model="createForm.ip" placeholder="IP"></el-input>
          </el-form-item>
          <el-form-item label="端口">
            <el-input
              v-model="createForm.port"
              placeholder="默认22端口"
            ></el-input>
          </el-form-item>

          <el-form-item label="认证">
            <el-switch
              v-model="delivery"
              active-color="#13ce66"
              inactive-color="#ff4949"
              disabled
            ></el-switch>
          </el-form-item>

          <el-form-item label="用户名">
            <el-input
              v-model="createForm.username"
              placeholder="用户名"
            ></el-input>
          </el-form-item>

          <el-form-item label="密码">
            <el-input
              v-model="createForm.password"
              show-password
              placeholder="密码"
            ></el-input>
          </el-form-item>
          <el-form-item label="描述">
            <el-input
              v-model="createForm.desc"
              placeholder="填写描述"
            ></el-input>
          </el-form-item>
        </el-form>

        <span slot="footer">
          <el-button type="success" @click="createHost">创建</el-button>
          <el-button @click="addHostVisible = false">取消</el-button>
        </span>
      </el-dialog>

      <el-dialog title="修改信息" :visible.sync="editHostVisible" width="30%">
        <el-form ref="form" :model="editForm" label-width="70px">
          <el-form-item label="主机名称">
            <el-input
              v-model="editForm.hostName"
              placeholder="主机名称"
            ></el-input>
          </el-form-item>
          <el-form-item label="类型">
            <el-select v-model="editForm.hostType" placeholder="从节点">
              <el-option
                key="主节点"
                label="主节点(设定该节点为主节点)"
                :disabled="true"
                value="主节点"
              ></el-option>
              <el-option
                key="工作节点"
                label="工作节点"
                value="工作节点"
              ></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="IP">
            <el-input v-model="editForm.ip" placeholder="IP"></el-input>
          </el-form-item>
          <el-form-item label="端口">
            <el-input
              v-model="editForm.port"
              placeholder="默认22端口"
            ></el-input>
          </el-form-item>

          <el-form-item label="认证">
            <el-switch
              v-model="delivery"
              active-color="#13ce66"
              inactive-color="#ff4949"
              disabled
            >
            </el-switch>
          </el-form-item>

          <el-form-item label="用户名">
            <el-input
              v-model="editForm.username"
              placeholder="用户名"
            ></el-input>
          </el-form-item>

          <el-form-item label="密码">
            <el-input
              v-model="editForm.password"
              show-password
              placeholder="密码"
            ></el-input>
          </el-form-item>
          <el-form-item label="描述">
            <el-input v-model="editForm.desc" placeholder="填写描述"></el-input>
          </el-form-item>
        </el-form>

        <span slot="footer">
          <el-button type="success" @click="editHost(editForm.id)"
            >确认修改</el-button
          >
          <el-button @click="editHostVisible = false">取消</el-button>
        </span>
      </el-dialog>
    </div>
  </div>
</template>

<style>
.select {
  display: flex;
  align-items: center;
  justify-content: space-between;
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
</style>

<script>
import { hostList, createHost, testHost, rsaVerify } from "../../api/index";
export default {
  inject: ["reload"],

  data() {
    return {
      hostList: [],
      currentPage: 1, //初始页
      pagesize: 15, //    每页的数据
      addHostVisible: false,
      editHostVisible: false,
      isNoVerify: false,
      delivery: true,
      selectForm: {
        status: "",
      },
      createForm: {
        hostId: "",
        hostName: "",
        ip: "",
        hostType: "",
        port: "",
        username: "",
        password: "",
        desc: "",
      },
      editForm: {
        hostId: "",
        hostName: "",
        ip: "",
        hostType: "",
        port: "",
        username: "",
        password: "",
        desc: "",
      },
    };
  },

  created() {
    this.loadHostList();
  },

  methods: {
    loadHostList() {
      hostList().then((res) => {
        this.hostList = res.data.data;
      });
    },

    // goHostDetail(uuid) {
    //   const self = this;
    //   self.$router.push(`/hostDetail`);
    // },

    // 初始页currentPage、初始每页数据数pagesize和数据data
    handleSizeChange: function (size) {
      this.pagesize = size;
      // console.log(this.pagesize); //每页下拉显示数据
    },
    handleCurrentChange: function (currentPage) {
      this.currentPage = currentPage;
      // console.log(this.currentPage); //点击第几页
    },

    goEdit(dd) {
      // console.log(dd);
      this.editHostVisible = true;
      this.editForm = dd;
    },

    createHost() {
      const self = this;
      var data = self.createForm;
      console.log(data);
      self.$api.createHost(data).then((res) => {
        if (res.data.code === 200) {
          self.$notify({
            title: "添加成功",
            message: new Date().toLocaleTimeString(),
            type: "success",
            duration: 0,
          });
        }
        self.reload();
      });
    },

    editHost() {
      const self = this;
      var data = self.editForm;
      self.$api.editHost(data).then((res) => {
        if (res.data.code === 200) {
          self.$message.success({
            message: "修改成功",
          });
          self.reload();
        }
      });
    },

    deleteHost(hostId) {
      const self = this;
      var data = {
        hostId,
      };

      // 二次确认删除
      self
        .$confirm("确定要删除吗？", "提示", {
          type: "warning",
        })
        .then(() => {
          self.$api.deleteHost(data).then((res) => {
            if (res.data.code === 200) {
              self.$message.success("删除成功");
              self.reload();
            }
          });
        })
        .catch(() => {});
    },

    testHost(hostId, hostIp) {
      const self = this;
      var data = {
        hostId,
        hostIp,
      };
      testHost(data).then((res) => {
        // console.log(res);
        if (res.data.code == 200) {
          // self.$message.success(res.data.data.ip + "(" + res.data.data.uname + ")" + " 连接成功" );
          this.$notify({
            title: res.data.data.ip + "(连接成功)",
            message:
              res.data.data.uname + "\n" + new Date().toLocaleTimeString(),
            type: "success",
            duration: 0,
          });
          self.reload();
        }
        else if (res.data.code == 400) {
          this.$notify({
            title: data.hostIp + " 连接失败",
            message: res.data.data + "\n" + new Date().toLocaleTimeString(),
            type: "error",
            duration: 0,
          });
          self.reload();
        }
      });
    },

    onChangeProSubmit() {
      hostList({
        status: this.selectForm.status,
      }).then((res) => {
        this.hostList = res.data.data;
      });
    },

    changeRsaVerify(hostId) {
      const self = this;
      var data = {
        hostId,
      };
      self.$api.changeRsaVerify(data).then((res) => {
        if (res.data.code === 200) {
          self.$message.success("设置成功");
          // self.reload();
        }
      });
    },

    goHostDetail(uuid) {
      const self = this;
      self.$router.push(`/hostDetail/${uuid}`);
    },
  },
};
</script>
 
 
 