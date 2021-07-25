<template>
  <div>
    <div class="elcol">
      <el-button
        type="success"
        icon="el-icon-plus"
        @click="createProVisible = true"
        >新建项目</el-button
      >
    </div>
    <el-row :gutter="12">
      <el-col
        class="elcol"
        :span="6"
        v-for="(o, i_index) in projectList"
        :key="i_index"
        :offset="1"
      >
        <el-card :body-style="{ padding: '10px' }">
          <div style="padding: 2px 2px">
            <span style="font-weight: bold">{{ o.projectName }}</span>
            <div class="bottom clearfix">
              <time class="desc">{{ o.projectDesc }}</time
              ><br />
              <time class="time">{{ o.updateTime }}</time>
              <el-button
                type="text"
                icon="el-icon-delete"
                class="button-red"
                @click="deleteProject(o.projectId)"
                >删除</el-button
              >
              <el-button
                type="text"
                icon="el-icon-edit"
                class="button"
                @click="goTaskList(o.projectId)"
                >查看</el-button
              >
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>

    <!-- 编辑弹出框 -->
    <el-dialog title="添加项目" :visible.sync="createProVisible" width="40%">
      <el-form ref="form" :model="createForm" label-width="80px">
        <el-form-item label="项目名称">
          <el-input
            v-model="createForm.projectName"
            placeholder="项目名称"
          ></el-input>
        </el-form-item>
        <el-form-item label="项目简介">
          <el-input v-model="createForm.projectDesc" placeholder="项目简介"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer">
        <el-button @click="createProVisible = false">取 消</el-button>
        <el-button type="primary" @click="createProject">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>
<style>
.elcol {
  margin-top: 8px;
  margin-left: 12px;
}

.update-time {
  font-size: 14px;
  font-weight: bold;
  margin-top: 8px;
  margin-left: 12px;
}

.desc {
  font-size: 13px;
  color: rgb(97, 96, 96);
  font-weight: bold;
}

.time {
  font-size: 13px;
  color: #999;
  font-weight: bold;
}

.bottom {
  margin-top: 13px;
  line-height: 19px;
}

.button {
  padding: 5px;
  float: right;
  font-weight: bold;
}

.button-red {
  padding: 5px;
  float: right;
  color: #ff0000;
  font-weight: bold;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both;
}
</style>

<script>
import { projectIndex, createProject, deleteProject } from "../../api/index";

export default {
  inject: ["reload"],
  data() {
    return {
      projectList: [],
      projectId: "",
      title: "",
      createProVisible: false,
      createForm: {
        projectName: "",
        porjectDesc: "",
      },
      currentDate: new Date(),
    };
  },

  watch: {
    $route() {
      this.projectId = this.$route.params.projectId;
    },
  },
  created() {
    this.loadProjectIndex();
  },

  methods: {
    loadProjectIndex() {
      const self = this;
      projectIndex().then((res) => {
        console.log(res);
        self.projectList = res.data.data;
      });
    },
    // 跳转到爬虫列表详情
    goTaskList(projectId) {
      const self = this;
      self.$router.push(`/project/${projectId}`);

      // self.$router.push({
      //   path: "spiderPro",
      //   query: {
      //     projectId: projectId,
      //   },
      // });
    },

    deleteProject(projectId) {
      var self = this;
      var data = {
        projectId,
      };

      // 二次确认删除
      self.$confirm("确定要删除吗？", "提示", {
          type: "warning",
        })
        .then(() => {
          deleteProject(data).then((res) => {
            if (res.data.code === 200) {
              self.$message.success("删除成功");
              self.reload();
            }
          });
        }).catch(() => {});
    },

    createProject() {
      var self = this;
      var data = this.createForm;
      createProject(data).then((res) => {
        self.$message.success({
          dangerouslyUseHTMLString: true,
          message: "创建成功",
        });
        self.reload();
      });
    },
  },
};
</script>