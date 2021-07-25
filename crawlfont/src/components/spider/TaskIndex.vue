<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item
          ><i class="el-icon-lx-calendar"></i> 爬虫</el-breadcrumb-item
        >
        <el-breadcrumb-item>爬虫任务</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <div>
      <el-card style="border-radius: 0">
        <div class="select">
          <div>
            <el-form label-position="right" :model="selectForm" inline>
              <el-form-item label="项目">
                <el-select
                  v-model="selectForm.project"
                  @change="onChangeSubmit"
                  placeholder="全部"
                >
                  <el-option value="" label="全部" />
                  <el-option
                    v-for="project in projectList"
                    :key="project.projectId"
                    :label="project.projectName"
                    :value="project.projectId"
                    :disabled="project.disabled"
                  >
                  </el-option>
                </el-select>
              </el-form-item>

              <el-form-item label="状态">
                <el-select 
                placeholder="全部"
                v-model="selectForm.status"
                @change="onChangeSubmit"
                >
                  <el-option label="全部" />
                  <el-option value="0" label="运行中" />
                  <el-option value="1" label="已完成" />
                </el-select>
              </el-form-item>
            </el-form>
          </div>

          <el-button
            type="success"
            icon="el-icon-plus"
            @click="createTaskVisible = true"
            >创建任务</el-button
          >
        </div>

        <el-table
          :data="
            taskList.slice((currentPage - 1) * pagesize, currentPage * pagesize)
          "
          style="width: 100%,height:auto"
          border
          :row-class-name="tableRowClassName"
        >
          <el-table-column
            prop="taskName"
            label="爬虫名称"
            width="180"
            align="center"
          ></el-table-column>

          <el-table-column
            prop="taskStatus"
            label="运行状态"
            width="140"
            align="center"
          >
            <template slot-scope="scope">
              <div>
                <el-button
                  v-if="scope.row.taskStatus == '1'"
                  style="font-weight: bold"
                  type="primary"
                  plain
                  ><i
                    style="font-weight: bold"
                    size="mini"
                    class="el-icon-check"
                  ></i>
                  已完成</el-button
                >
                <el-button
                  v-else
                  style="font-weight: bold"
                  type="success"
                  plain
                  size="mini"
                  ><i
                    style="font-weight: bold"
                    size="mini"
                    class="el-icon-loading"
                  ></i>
                  运行中</el-button
                >
              </div>
            </template>
          </el-table-column>

          <el-table-column
            prop="lastRunStatus"
            label="上次运行状态"
            width="140"
            align="center"
          >
            <template slot-scope="scope">
              <div>
                <el-button
                  v-if="scope.row.lastRunStatus == '1'"
                  style="font-weight: bold"
                  type="success"
                  plain
                  ><i
                    style="font-weight: bold"
                    size="mini"
                    class="el-icon-check"
                  ></i>
                  成功</el-button
                >
                <el-button
                  v-else-if="scope.row.lastRunStatus == '-1'"
                  style="font-weight: bold"
                  type="danger"
                  plain
                  size="mini"
                  ><i
                    style="font-weight: bold"
                    size="mini"
                    class="el-icon-close"
                  ></i>
                  失败</el-button
                >
                <el-button
                  v-else
                  style="font-weight: bold"
                  type="primary"
                  plain
                  size="mini"
                  ><i
                    style="font-weight: bold"
                    size="mini"
                    class="el-icon-warning-outline"
                  ></i>
                  未知</el-button
                >
              </div>
            </template>
          </el-table-column>

          <el-table-column
            prop="lastRunTime"
            label="上次运行时间"
            width="180"
            align="center"
          ></el-table-column>

          <el-table-column
            prop="createTime"
            label="创建时间"
            width="180"
            align="center"
          ></el-table-column>

          <!-- <el-table-column
            prop="selectHosts"
            label="主机节点"
            align="center"
            width="250"
          >
            <template slot-scope="scope">
              <el-select
                v-model="scope.row.selectHosts"
                multiple
                placeholder="请选择"
              >
                <el-option
                  v-for="item in hostList"
                  :key="item.id"
                  :label="item.ip"
                  :value="item.ip"
                >
                  <span style="float: left">{{ item.ip }}</span>
                  <span style="float: right; color: #8492a6; font-size: 13px">{{
                    item.hostName
                  }}</span>
                </el-option>
              </el-select>
            </template>
          </el-table-column> -->

          <el-table-column
            prop="taskLevel"
            label="操作频率等级"
            align="center"
          ></el-table-column>

          <el-table-column
            prop="submit"
            label="操作"
            width="255"
            align="center"
          >
            <template slot-scope="scope">
              <div>
                <!-- <el-tooltip
                  class="item"
                  effect="dark"
                  content="运行"
                  placement="top-start"
                >
                  <el-button
                    v-if="scope.row.taskId == nowTaskId"
                    type="success"
                    icon="el-icon-loading"
                    disabled
                  ></el-button>
                  <el-button
                    v-else
                    type="success"
                    icon="el-icon-refresh-right"
                    @click="
                      onTaskSubmit(
                        scope.row.taskId,
                        scope.row.taskName,
                        scope.row.taskPath,
                        scope.row.selectHosts
                      )
                    "
                  ></el-button>
                </el-tooltip> -->

                <el-tooltip
                  class="item"
                  effect="dark"
                  content="任务详情"
                  placement="top-start"
                >
                  <el-button
                    type="success"
                    icon=" el-icon-document"
                    @click="taskDetail(scope.row.taskId)"
                  ></el-button>
                </el-tooltip>

                <el-tooltip
                  class="item"
                  effect="dark"
                  content="部署"
                  placement="top-start"
                >
                  <el-button
                    type="warning"
                    icon="el-icon-upload"
                    @click="deployTask(scope.row.taskId)"
                  ></el-button>
                </el-tooltip>

                <el-tooltip
                  class="item"
                  effect="dark"
                  content="查看日志"
                  placement="top-start"
                >
                  <el-button
                    type="primary"
                    icon="el-icon-search"
                    @click="onTaskLog(scope.row.taskId)"
                  ></el-button>
                </el-tooltip>

                <el-tooltip
                  class="item"
                  effect="dark"
                  content="删除"
                  placement="top-start"
                >
                  <el-button
                    type="danger"
                    icon="el-icon-delete"
                    @click="deleteTask(scope.row.taskId)"
                  ></el-button>
                </el-tooltip>
              </div>
            </template>
          </el-table-column>
        </el-table>
      </el-card>

      <div class="pagination-footer">
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="currentPage"
          :page-sizes="[15, 20, 40]"
          :page-size="pagesize"
          layout="total, sizes, prev, pager, next"
          :total="taskList.length"
        >
        </el-pagination>
      </div>

      <!-- 编辑弹出框 -->
      <el-dialog title="添加任务" :visible.sync="createTaskVisible" width="40%">
        <el-form
          :rules="rules"
          :model="ruleForm"
          ref="ruleForm"
          label-width="80px"
        >
          <el-form-item prop="taskName" label="任务名称">
            <el-input
              v-model="ruleForm.taskName"
              placeholder="任务名称"
            ></el-input>
          </el-form-item>
          <el-form-item prop="projectId" label="所属项目">
            <el-select v-model="ruleForm.projectId" placeholder="请选择">
              <el-option
                v-for="project in projectList"
                :key="project.projectId"
                :label="project.projectName"
                :value="project.projectId"
                :disabled="project.disabled"
              >
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item prop="taskLevel" label="频率等级">
            <el-select v-model="ruleForm.taskLevel" placeholder="请选择">
              <el-option label="高频" value="高频"></el-option>
              <el-option label="中频" value="中频"></el-option>
              <el-option label="低频" value="低频"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item prop="taskDesc" label="描述">
            <el-input v-model="ruleForm.taskDesc" placeholder="描述"></el-input>
          </el-form-item>

          <el-form-item prop="taskPath" label="上传代码">
            <el-upload
              drag
              :http-request="uploadZip"
              :limit="limit"
              :before-upload="beforeUpload"
              multiple
            >
              <i class="el-icon-upload"></i>
              <div class="el-upload__text">
                将文件拖到此处，或<em>点击上传</em>
              </div>
              <div class="el-upload__tip" slot="tip">
                只能上传 zip 压缩包，且不超过 10 M
              </div>
            </el-upload>
          </el-form-item>
        </el-form>

        <span slot="footer">
          <el-button @click="createTaskVisible = false">取 消</el-button>
          <el-button type="primary" @click="createTask('ruleForm')"
            >确 定</el-button
          >
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

.upload-demo {
  margin-top: 0px;
  height: 150px;
}
.dialog-conent {
  margin-left: 15px;
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
import {
  projectIndex,
  taskIndex,
  startTask,
  hostList,
  uploadZip,
  createTask,
  deleteTask,
} from "../../api/index";
export default {
  inject: ["reload"],

  data() {
    return {
      projectList: [],
      taskList: [],
      hostList: [],
      nowTaskId: "",
      currentPage: 1, //初始页
      pagesize: 15, //    每页的数据
      loading: false,
      limit: 1,
      sizeLimit: 100,
      ruleForm: {
        taskName: "",
        projectId: "",
        taskLevel: "",
        taskDesc: "",
        taskPath: "",
      },

      selectForm: {
        project: "",
        status: ""
      },
      createTaskVisible: false,
      // form: {},

      rules: {
        taskName: [
          { required: true, message: "请输入任务名称", trigger: "blur" },
          { min: 3, max: 15, message: "长度在 3 到 15 个字符", trigger: "blur" },
        ],
        projectId: [
          { required: true, message: "请选择项目", trigger: "change" },
        ],
        taskLevel: [
          { required: true, message: "请选择等级", trigger: "change" },
        ],
        taskDesc: [
          { required: true, message: "请输入任务描述", trigger: "blur" },
          { min: 4, max: 50, message: "长度在 4 到 50 个字符", trigger: "blur" },
        ],
        // taskPath: [
        //   { required: true, message: '请上传首图' },
        // ],
      },
    };
  },

  created() {
    this.loadProjectIndex();
    this.loadTaskList();
    // this.loadHostList();
  },

  methods: {
    loadHostList() {
      hostList().then((res) => {
        this.hostList = res.data.data;
      });
    },
    tableRowClassName({ row, rowIndex }) {},

    // 初始页currentPage、初始每页数据数pagesize和数据data
    handleSizeChange: function (size) {
      this.pagesize = size;
      // console.log(this.pagesize); //每页下拉显示数据
    },
    handleCurrentChange: function (currentPage) {
      this.currentPage = currentPage;
      // console.log(this.currentPage); //点击第几页
    },

    loadProjectIndex() {
      projectIndex().then((res) => {
        this.projectList = res.data.data;
      });
    },

    loadTaskList() {
      taskIndex().then((res) => {
        this.taskList = res.data.data;
      });
    },

    onChangeSubmit() {
      taskIndex({
        project: this.selectForm.project,
        status:this.selectForm.status
      }).then((res) => {
        this.taskList = res.data.data;
      });
    },



    onTaskSubmit(taskId, taskName, taskPath, selectHosts) {
      const self = this;
      self.nowTaskId = taskId; // 设置当前 taskId
      var data = {
        taskId: taskId,
        taskHosts: selectHosts,
      };
      self.$message.success({
        dangerouslyUseHTMLString: true,
        message: "<strong>成功派发一个爬虫任务</strong>",
      });
      self.$api.startTask(taskPath, data).then((res) => {
        self.nowTaskId = ""; // 回值
        if (res.data.code === 200) {
          // 实时日志数组置为空
          self.$notify({
            title: taskName + "更新成功",
            message: "更新成功 " + new Date().toLocaleTimeString(),
            type: "success",
            duration: 0,
          });
        } else if (res.data.code === 422) {
          self.$notify({
            title: taskName + "正在更新中",
            message:
              taskName +
              "正在更新中,请勿重复调度 " +
              new Date().toLocaleTimeString(),
            type: "warning",
            duration: 0,
          });
        } else {
          self.$notify({
            title: taskName + "更新失败",
            message: res.data.message + " " + new Date().toLocaleTimeString(),
            type: "error",
            duration: 0,
          });
          // self.$message.error(res.data.msg);
        }

        self.reload();
      });
    },

    onTaskLog(taskId) {
      const self = this;
      self.$router.push(`/taskLog/${taskId}`);
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

    uploadZip(param) {
      var self = this;
      const formData = new FormData();
      formData.append("file", param.file);
      uploadZip(formData)
        .then((res) => {
          self.loading = false;
          console.log(res);
          self.ruleForm.taskPath = res.data.data.uuid;
          self.$message.success({
            dangerouslyUseHTMLString: true,
            message: res.data.message,
          });
        })
        .catch(function (error) {
          console.log("error");
        });
    },

    createTask(formName) {
      const self = this;
      self.$refs[formName].validate((valid) => {
        if (valid) {
          var data = self.ruleForm;
          createTask(data).then((res) => {
            if (res.data.code === 200) {
              self.$message.success("创建成功");
              self.reload();
            }
          });
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },

    deleteTask(taskId) {
      const self = this;
      var data = {
        taskId,
      };
      // 二次确认删除
      self
        .$confirm("确定要删除吗？", "提示", {
          type: "warning",
        })
        .then(() => {
          deleteTask(data).then((res) => {
            if (res.data.code === 200) {
              self.$message.success("删除成功");
              self.reload();
            }
          });
        })
        .catch(() => {});
    },

    deployTask(taskId) {
      const self = this;
      self.$router.push(`/deployTask/${taskId}`);
    },

    taskDetail(taskId) {
      const self = this;
      self.$router.push(`/taskDetail/${taskId}`);
    },
  },
};
</script>
 
 
 