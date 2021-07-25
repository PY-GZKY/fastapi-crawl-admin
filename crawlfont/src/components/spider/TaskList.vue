<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-lx-calendar"></i> 爬虫项目
        </el-breadcrumb-item>
        <el-breadcrumb-item>爬虫列表</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <div>
      <el-table
        :data="
          tableData.slice((currentPage - 1) * pagesize, currentPage * pagesize)
        "
        style="width: 100%,height:auto"
        border
        :row-class-name="tableRowClassName"
      >
        <el-table-column prop="taskName" label="爬虫名称" width="180" align="center"></el-table-column>

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

        <el-table-column prop="lastRunStatus" label="上次运行状态" width="140" align="center">
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
          <el-button style="font-weight: bold" type="success" plain icon="el-icon-check"></el-button>
        </el-table-column>

        <el-table-column prop="lastRunTime" label="上次运行时间" width="180" align="center"></el-table-column>

        <el-table-column prop="createTime" label="创建时间" width="180" align="center"></el-table-column>

        <el-table-column prop="taskLevel" label="操作频率等级" width="120" align="center"></el-table-column>

        <el-table-column prop="taskDesc" label="描述" align="center"></el-table-column>

        <el-table-column prop="submit" label="操作" width="255">
          <template slot-scope="scope">
            <div>
              <el-tooltip class="item" effect="dark" content="任务详情" placement="top-start">
                <el-button
                  type="success"
                  icon=" el-icon-document"
                  @click="taskDetail(scope.row.taskId)"
                ></el-button>
              </el-tooltip>

              <!-- <el-tooltip
                class="item"
                effect="dark"
                content="运行爬虫"
                placement="top-start"
              >
                <el-button
                  v-if="scope.row.taskId == nowTaskId"
                  type="success"
                  size="small"
                  icon="el-icon-loading"
                  disabled
                ></el-button>
                <el-button
                  v-else
                  type="success"
                  size="small"
                  icon="el-icon-refresh"
                  @click="
                    onTaskSubmit(
                      scope.row.taskId,
                      scope.row.taskName,
                      scope.row.taskPath,
                      scope.row.selectHosts // todo 节点列表
                    )
                  "
                ></el-button>
              </el-tooltip>-->

              <el-tooltip class="item" effect="dark" content="查看日志" placement="top-start">
                <el-button
                  type="primary"
                  size="small"
                  icon="el-icon-search"
                  @click="onTaskLog(scope.row.taskId)"
                ></el-button>
              </el-tooltip>

              <el-tooltip
                class="item"
                size="small"
                effect="dark"
                content="任务运行统计"
                placement="top-start"
              >
                <el-button
                  type="warning"
                  size="small"
                  icon="el-icon-s-data"
                ></el-button>
              </el-tooltip>

              <el-tooltip
                class="item"
                size="small"
                effect="dark"
                content="删除"
                placement="top-start"
              >
                <el-button
                  type="danger"
                  size="small"
                  icon="el-icon-delete"
                  @click="deleteTask(scope.row.taskId)"
                ></el-button>
              </el-tooltip>
            </div>
          </template>
        </el-table-column>
      </el-table>
      <div class="pagination-footer">
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="currentPage"
          :page-sizes="[15, 20, 40]"
          :page-size="pagesize"
          layout="total, sizes, prev, pager, next"
          :total="tableData.length"
        ></el-pagination>
      </div>
    </div>
  </div>
</template>

<style>
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
  startTask,
  hostList,
  taskList,
  deleteTask,
} from "../../api/index";
export default {
  inject: ["reload"],

  data() {
    return {
      tableData: [],
      hostList: [],
      ddd: [],
      nowTaskId: "",
      platId: "",
      currentPage: 1, //初始页
      pagesize: 15, //    每页的数据
    };
  },

  watch: {
    $route() {
      this.platId = this.$route.params.projectId;
      this.projectId = this.$route.params.projectId;
      // this.loadTaskList();
    },
  },

  created() {
    this.projectId = this.$route.params.projectId;
    this.loadTaskList();
    this.loadHostList();
  },

  methods: {
    tableRowClassName({ row, rowIndex }) {
      // if (rowIndex === 1) {
      //   console.log("---------");
      //   return "warning-row";
      // } else if (rowIndex === 3) {
      //   return "success-row";
      // }
      // return "";
    },

    // 初始页currentPage、初始每页数据数pagesize和数据data
    handleSizeChange(size) {
      this.pagesize = size;
      // console.log(this.pagesize); //每页下拉显示数据
    },
    handleCurrentChange(currentPage) {
      this.currentPage = currentPage;
      // console.log(this.currentPage); //点击第几页
    },

    loadTaskList() {
      taskList({
        projectId: this.projectId,
      }).then((res) => {
        console.log(res);
        this.tableData = res.data.data;
      });
    },

    onTaskSubmit(taskId, taskName, taskPath, selectHosts) {
      const self = this;
      self.nowTaskId = taskId; // 设置当前 taskId
      var data = {
        taskId: taskId,
        taskHosts: selectHosts,
      };
      console.log("提交数据 ==> ", data);
      self.$message.success({
        dangerouslyUseHTMLString: true,
        message: "<strong>成功派发一个爬虫任务</strong>",
      });
      self.$api
        .startTask(taskPath, data)
        .then((res) => {
          self.nowTaskId = ""; // 回值
          if (res.data.code === 200) {
            self.$notify({
              title: taskName + " 更新成功",
              message: "更新成功 " + new Date().toLocaleTimeString(),
              type: "success",
              duration: 0,
            });
          } else if (res.data.code === 422) {
            self.$notify({
              title: taskName + " 正在更新中",
              message:
                taskName +
                " 正在更新中,请勿重复调度 " +
                new Date().toLocaleTimeString(),
              type: "warning",
              duration: 0,
            });
          } else {
            self.$notify({
              title: taskName + " 更新失败",
              message:
                "登陆失效,请3分钟后重试 " + new Date().toLocaleTimeString(),
              type: "error",
              duration: 0,
            });
            // self.$message.error(res.data.msg);
          }
          self.reload();
        })
        .catch((err) => {
          console.log(err);
        });
    },

    onTaskLog(taskId) {
      const self = this;
      self.$router.push(`/taskLog/${taskId}`);
    },

    loadHostList() {
      hostList().then((res) => {
        this.hostList = res.data.data;
      });
    },

    getData(selectHosts) {
      console.log(selectHosts);
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

    taskDetail(taskId) {
      const self = this;
      self.$router.push(`/taskDetail/${taskId}`);
    },
  },
};
</script>
 
 
 