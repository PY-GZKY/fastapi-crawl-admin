<template>
  <div>
    <div class="elcol">
      <el-button
        type="success"
        icon="el-icon-plus"
        @click="createWorkVisible = true"
        >新建日志</el-button
      >

    </div>
    <el-row :gutter="12">
      <el-col
        class="elcol"
        :span="7"
        v-for="(o, i_index) in workList"
        :key="i_index"
        :offset="1"
      >
        <el-card :body-style="{ padding: '10px' }">
          <div style="padding: 2px 2px">
            <span style="font-weight: bold">{{ o.title }}</span>
            <div class="bottom clearfix">
              <span class="desc" v-for="(i, index) in o.content">
                <span class="desc" v-if="i">
                  {{ index + 1 }} {{ i }}<br />
                </span>
                <span class="desc" v-else> {{ i }}<br /> </span>
              </span>

              <br />
              <time class="time">{{ o.updateTime }}</time>
              <el-button
                type="text"
                icon="el-icon-delete"
                class="button-red"
                @click="deleteWork(o.id)"
                >删除</el-button
              >
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>

    <!-- 编辑弹出框 -->
    <el-dialog title="添加小朋友" :visible.sync="createWorkVisible" width="40%">
      <el-form ref="form" :model="createForm" label-width="80px">
        <el-form-item label="主题">
          <el-input
            v-model="createForm.title"
            placeholder="主题"
            maxlength="20"
            show-word-limit
          ></el-input>
        </el-form-item>
        <el-form-item label="内容1">
          <el-input
            placeholder="请输入内容"
            v-model="createForm.content1"
            maxlength="100"
            show-word-limit
          >
          </el-input>
        </el-form-item>
        <el-form-item label="内容2">
          <el-input
            placeholder="请输入内容"
            v-model="createForm.content2"
            maxlength="100"
            show-word-limit
          >
          </el-input>
        </el-form-item>
        <el-form-item label="内容3">
          <el-input
            placeholder="请输入内容"
            v-model="createForm.content3"
            maxlength="100"
            show-word-limit
          >
          </el-input>
        </el-form-item>
        <el-form-item label="内容4">
          <el-input
            placeholder="请输入内容"
            v-model="createForm.content4"
            maxlength="100"
            show-word-limit
          >
          </el-input>
        </el-form-item>
        <el-form-item label="内容5">
          <el-input
            placeholder="请输入内容"
            v-model="createForm.content5"
            maxlength="100"
            show-word-limit
          >
          </el-input>
        </el-form-item>
      </el-form>
      <span slot="footer">
        <el-button @click="createWorkVisible = false">取 消</el-button>
        <el-button type="primary" @click="createWork">确 定</el-button>
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
import { getWorkList, createWork, deleteWork } from "../../api/index";

export default {
  inject: ["reload"],
  data() {
    return {
      workList: [],
      workId: "",
      title: "",
      content: "",
      createWorkVisible: false,
      createForm: {
        title: "",
        content1: "",
        content2: "",
        content3: "",
        content4: "",
        content5: "",
      },
      currentDate: new Date(),
    };
  },

  created() {
    this.loadWorkList();
  },

  methods: {
    loadWorkList() {
      const self = this;
      getWorkList().then((res) => {
        console.log(res);
        self.workList = res.data.data;
      });
    },

    deleteWork(workId) {
      var self = this;
      var data = {
        workId,
      };

      // 二次确认删除
      self
        .$confirm("确定要删除吗？", "提示", {
          type: "warning",
        })
        .then(() => {
          deleteWork(data).then((res) => {
            if (res.data.code === 200) {
              self.$message.success("删除成功");
              self.reload();
            }
          });
        })
        .catch(() => {});
    },

    createWork() {
      var self = this;
      var data = this.createForm;
      createWork(data).then((res) => {
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