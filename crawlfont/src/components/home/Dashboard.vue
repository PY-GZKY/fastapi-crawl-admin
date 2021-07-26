<template>
  <div>
    <el-row :gutter="20">
      <el-col :span="24">
        <el-row :gutter="8" class="mgb20">
          <el-col :span="6">
            <el-card shadow="hover" :body-style="{ padding: '0px' }">
              <div class="grid-content1 grid-con-1">
                <i class="el-icon-s-promotion grid-con-icon"></i>

                <div class="grid-cont-right" to="projectIndex">
                  <div>
                    <router-link class="grid-cont-right" to="projectIndex">
                      <div>{{ projectCount }}</div>
                      爬虫项目
                    </router-link>
                  </div>
                </div>
              </div>
            </el-card>
          </el-col>
          <el-col :span="6">
            <el-card shadow="hover" :body-style="{ padding: '0px' }">
              <div class="grid-content2 grid-con-4">
                <i class="el-icon-s-promotion grid-con-icon"></i>
                <div class="grid-cont-right" to="taskIndex">
                  <div>
                    <router-link class="grid-cont-right" to="taskIndex">
                      <div>{{ taskCount }}</div>
                      爬虫任务
                    </router-link>
                  </div>
                </div>
              </div>
            </el-card>
          </el-col>
          <el-col :span="6">
            <el-card shadow="hover" :body-style="{ padding: '0px' }">
              <div class="grid-content3 grid-con-2">
                <i class="el-icon-s-data grid-con-icon"></i>
                <div class="grid-cont-right" to="hosts">
                  <div>
                    <router-link class="grid-cont-right" to="hosts">
                      <div>{{ hostCount }}</div>
                      主机数量
                    </router-link>
                  </div>
                </div>
              </div>
            </el-card>
          </el-col>
          <el-col :span="6">
            <el-card shadow="hover" :body-style="{ padding: '0px' }">
              <div class="grid-content4 grid-con-3">
                <i class="el-icon-notebook-2 grid-con-icon"></i>
                <div class="grid-cont-right">
                  <div>
                    <router-link class="grid-cont-right" to="taskIndex">
                      <div>5025664009</div>
                      数据总量
                    </router-link>
                  </div>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </el-col>
    </el-row>

    <el-row :gutter="12">
      <el-col :span="6" class="mgb20" :offset="0">
        <el-card shadow="hover">
          <div shadow="hover" style="padding-bottom: 12px; color: #000">
            <h4 class="title">系统信息</h4>
          </div>
          <div shadow="hover">
            <el-row class="buttonClass">
              <span>
                <el-button type="success" size="mini" 
                  >操作系统：{{systemParams.info.platform}}</el-button
                >

                <br /><br />
                <el-button type="warning" size="mini" plain
                  >已使用内存：{{systemParams.mem.mem_used}}</el-button
                >
                <el-button type="warning" size="mini" plain
                  >内存使用率：{{systemParams.mem.mem_percent}}</el-button
                >
                <br /><br />
                <el-button type="primary" size="mini" plain
                  >物理CPU：{{systemParams.cpu.cpu_cores}}</el-button
                >
                <el-button type="primary" size="mini" plain
                  >处理器位数：{{systemParams.info.bit_msg}}</el-button
                >
              </span>
            </el-row>
          </div>
        </el-card>
      </el-col>

      <el-col :span="6" class="mgb20" :offset="0">
        <el-card shadow="hover">
          <div shadow="hover" style="padding-bottom: 12px; color: #000">
            <h4 class="title">Redis</h4>
          </div>
          <div shadow="hover">
            <el-row class="buttonClass">
              <span>
                <el-button type="primary" size="mini" plain
                  >操作系统：{{ redisParams.os }}</el-button
                >
                <br /><br />
                <el-button type="primary" size="mini" plain
                  >redis 版本{{ redisParams.redis_version }}</el-button
                >
                <el-button type="primary" size="mini" plain
                  >开放端口：{{ redisParams.tcp_port }}</el-button
                >

                <br /><br />
                <el-button type="primary" size="mini" plain
                  >已用内存：{{ redisParams.used_memory_human }}</el-button
                >
                <el-button type="primary" size="mini" plain
                  >内存占用峰值：{{
                    redisParams.used_memory_peak_human
                  }}</el-button
                >
              </span>
            </el-row>
          </div>
        </el-card>
      </el-col>

      <el-col :span="6" class="mgb20" :offset="0">
        <el-card shadow="hover">
          <div shadow="hover" style="padding-bottom: 12px; color: #000">
            <h4 class="title">MongoDB</h4>
          </div>
          <div shadow="hover">
            <el-row class="buttonClass">
              <span>
                <el-button type="primary" size="mini" plain
                  >数据库版本：{{ mongoParams.version }}</el-button
                >
                <el-button type="primary" size="mini" plain
                  >运行时长: {{ mongoParams.uptime }}</el-button
                >
                <br />
                <br />
                <el-button type="primary" size="mini" plain
                  >活跃连接数: {{ mongoParams.connections.active }}</el-button
                >
                <el-button type="primary" size="mini" plain
                  >占用物理内存: {{ mongoParams.mem.resident }}</el-button
                >
                <br />
                <br />
    
                <el-button type="primary" size="mini" plain
                  >表数量: {{ mongoParams.collections }}</el-button
                >
                            <el-button type="primary" size="mini" plain
                  >总文档数：{{ mongoParams.objects }}</el-button
                >
              </span>
            </el-row>
          </div>
        </el-card>
      </el-col>

      <el-col :span="6" class="mgb20" :offset="0">
        <el-card shadow="hover">
          <div shadow="hover" style="padding-bottom: 12px; color: #000">
            <h4 class="title">运行情况</h4>
          </div>
          <div shadow="hover">
            <el-row class="buttonClass">
              <span>
                <el-button type="primary" size="mini" plain
                  >正在运行任务：{{taskParams.length}}</el-button
                >
                <el-button type="primary" size="mini" plain
                  >历史运行任务：16</el-button
                >
                <br />
                <br />

                <el-button type="primary" size="mini" plain
                  >总运行时长：02:09:12 </el-button
                >
     
                <br />
                <br />

                <el-button type="primary" size="mini" plain
                  >总运行时长：</el-button
                >
              </span>
            </el-row>
          </div>
        </el-card>
      </el-col>
    </el-row>

    <el-card shadow="hover" style="height: 470px">
      <div slot="header" class="clearfix">
        <span>待办事项</span>
        <el-button
          style="float: right; padding: 3px 0"
          type="text"
          @click="dialogAddVisible = true"
          >添加</el-button
        >
      </div>
      <el-table :show-header="false" :data="todoList" style="width: 100%">
        <el-table-column width="40">
          <template slot-scope="scope">
            <el-checkbox
              v-model="scope.row.status"
              @change="handleUpdate(scope.row.id)"
            ></el-checkbox>
          </template>
        </el-table-column>
        <el-table-column>
          <template slot-scope="scope">
            <div
              class="todo-item"
              :class="{ 'todo-item-del': scope.row.status }"
            >
              {{ scope.row.title }}
            </div>
          </template>
        </el-table-column>
        <el-table-column width="200" align="right">
          <template slot-scope="scope">
            <el-button
              type="text"
              icon="el-icon-edit"
              @click="
                dialogEditVisible = true;
                editForm.todoId = scope.row.id;
              "
              >编辑</el-button
            >
            <el-button
              type="text"
              icon="el-icon-delete"
              class="red"
              @click="handleDelete(scope.row.id)"
              >删除</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <el-dialog title="添加 TODO" :visible.sync="dialogAddVisible" width="30%">
      <el-form ref="form" label-width="90px">
        <el-form-item label="你要做什么" :model="addForm">
          <el-input v-model="addForm.title"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogAddVisible = false">取 消</el-button>
        <el-button type="primary" @click="handleCreate">确 定</el-button>
      </span>
    </el-dialog>

    <el-dialog title="编辑 TODO" :visible.sync="dialogEditVisible" width="30%">
      <el-form ref="form" label-width="90px">
        <el-form-item label="事项更改为" :model="editForm">
          <el-input v-model="editForm.todoTitle"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogEditVisible = false">取 消</el-button>
        <el-button type="primary" @click="handleEdit">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import Schart from "vue-schart";
import vChart from "../eCharts/BaseCharts";
import bus from "../common/bus";
import {
  taskIndex,
  systemParams,
  redisParams,
  mongoParams,
  projectCount,
  getTodoList,
  addTodo,
  delTodo,
  editTodo,
  updateTodo,
} from "../../api/index";

export default {
  name: "dashboard",
  inject: ["reload"],
  data() {
    return {
      name: localStorage.getItem("username"),
      projectCount: null,
      taskCount: null,
      hostCount: null,
      taskParams: [],
      systemParams: {},
      redisParams: {},
      mongoParams: {},
      todoList: [],
      data: [],
      dialogAddVisible: false,
      dialogEditVisible: false,
      addForm: {
        title: "",
      },
      editForm: {
        todoId: "",
        todoTitle: "",
      },
    };
  },
  components: {
    vChart,
  },
  computed: {},
  activated() {},
  deactivated() {},

  created() {
    this.loadSystemParams();
    this.loadProjectCount();
    this.loadTodoList();
  },

  methods: {
    format(percentage) {
      return percentage === 100 ? `${percentage}%` : `${percentage}%`;
    },

    customColorMethod(percentage) {
      if (percentage < 30) {
        return "#339900";
      } else if (percentage < 60) {
        return "#67c23a";
      } else if (percentage < 90) {
        return "#FF7E00";
      } else {
        return "#FF3333";
      }
    },

    // todo create
    handleCreate(title) {
      var self = this;
      self.$api
        .addTodo({
          title: this.addForm.title,
        })
        .then((res) => {
          console.log(res);
          self.$message.success({
            dangerouslyUseHTMLString: true,
            message: res.data.message,
          });
          self.reload();
        })
        .catch(function (error) {
          console.log("error");
        });
    },
    // todo del
    handleDelete(todoId) {
      var self = this;
      console.log("todoId:", todoId);
      // 二次确认删除
      self
        .$confirm("确定要删除吗？", "提示", {
          type: "warning",
        })
        .then(() => {
          self.$api
            .delTodo({
              todoId,
            })
            .then((res) => {
              self.$message.success({
                dangerouslyUseHTMLString: true,
                message: res.data.message,
              });
              self.reload();
            })
            .catch(function (error) {
              console.log("error");
            });
        })
        .catch(() => {});
    },

    // todo edit
    handleEdit() {
      var self = this;
      self.$api
        .editTodo({
          todoId: this.editForm.todoId,
          todoTitle: this.editForm.todoTitle,
        })
        .then((res) => {
          console.log(res);
          self.$message.success({
            dangerouslyUseHTMLString: true,
            message: res.data.message,
          });
          self.reload();
        })
        .catch(function (error) {
          console.log("error");
        });
    },

    // todo update
    handleUpdate(todoId) {
      var self = this;
      self.$api
        .updateTodo({
          todoId,
        })
        .then((res) => {
          // console.log(res);
          // self.$message.success({
          //   dangerouslyUseHTMLString: true,
          //   message: res.data.message,
          // });
        })
        .catch(function (error) {
          console.log("error");
        });
    },

    // todo list
    loadTodoList() {
      getTodoList().then((res) => {
        this.todoList = res.data.data;
      });
    },

    loadSystemParams() {
      systemParams().then((res) => {
        // console.log(res);
        this.systemParams = res.data.data;
      });

      redisParams().then((res) => {
        // console.log(res);
        this.redisParams = res.data.data;
      });

      mongoParams().then((res) => {
        // console.log(res);
        this.mongoParams = res.data.data;
      });

      taskIndex({status:0}).then((res) => {
        // console.log(res.data.data);
        this.taskParams = res.data.data;
      });
    },

    loadProjectCount() {
      projectCount().then((res) => {
        this.projectCount = res.data.data.projectCount;
        this.taskCount = res.data.data.taskCount;
        this.hostCount = res.data.data.hostCount;
      });
    },
  },
};
</script>


<style scoped>
.buttonClass {
  letter-spacing: 0.5px;
  font-size: 14px;
  white-space: pre-line;
}

.el-progress {
  width: 80%;
}

.el-row {
  margin-bottom: 10px;
}

.card {
  padding: 0px;
  background: #085a0f;
  color: #fff;
}

.card1 {
  padding: 0px;
  background: #857c03;
  color: #fff;
}

.card2 {
  padding: 0px;
  background: #0b5172;
  color: #fff;
}

.card3 {
  padding: 0px;
  background: #660b72;
  color: #fff;
}

.grid-content1 {
  display: flex;
  align-items: center;
  height: 60px;
  background: #409eff;
}

.grid-content2 {
  display: flex;
  align-items: center;
  height: 60px;
  background: #df7e20;
}

.grid-content3 {
  display: flex;
  align-items: center;
  height: 60px;
  background: #55c464;
}

.grid-content4 {
  display: flex;
  align-items: center;
  height: 60px;
  background: #e74f4f;
}

.grid-cont-right {
  flex: 1;
  text-align: center;
  font-size: 14px;
  font-weight: bold;
  color: rgb(255, 255, 255);
}

.grid-num {
  font-size: 16px;
  font-weight: bold;
}

.grid-con-icon {
  font-size: 30px;
  width: 70px;
  height: 100px;
  text-align: center;
  line-height: 100px;
  color: #fff;
}

.grid-con-1 .grid-con-icon {
  background: rgb(45, 140, 240);
}

.grid-con-2 .grid-con-icon {
  background: rgb(100, 213, 114);
}

.grid-con-3 .grid-con-icon {
  background: rgb(242, 94, 67);
}

.grid-con-4 .grid-con-icon {
  background: #e28a36;
}

.user-info {
  display: flex;
  align-items: center;
  padding-bottom: 10px;
  border-bottom: 2px solid #ccc;
  margin-bottom: 20px;
}

.user-avator {
  width: 120px;
  height: 120px;
  border-radius: 50%;
}

.user-info-cont {
  padding-left: 50px;
  flex: 1;
  font-size: 14px;
  color: #999;
}

.user-info-cont div:first-child {
  font-size: 30px;
  color: #222;
}

.user-info-list {
  font-size: 14px;
  color: #999;
  line-height: 25px;
}

.user-info-list span {
  margin-left: 70px;
}

.mgb20 {
  margin-bottom: 10px;
}

.todo-item {
  font-size: 14px;
}

.todo-item-del {
  text-decoration: line-through;
  color: #999;
}

.red {
  color: #ff0000;
}

.schart {
  width: 100%;
  height: 300px;
}
</style>
