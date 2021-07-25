<template>
  <div>
    <div class="crumbs">
             <el-breadcrumb separator="/">
        <el-breadcrumb-item
          ><i class="el-icon-lx-calendar"></i> 表格</el-breadcrumb-item
        >
        <el-breadcrumb-item>基础表格</el-breadcrumb-item>
      </el-breadcrumb>

    </div>
    <div class="container">
      <div class="handle-box">
        <el-button
          type="danger"
          icon="el-icon-delete"
          class="handle-del mr10"
          @click="delAllSelection"
          >批量删除</el-button
        >
        <el-select
          v-model="query.address"
          placeholder="地址"
          class="handle-select mr10"
        >
          <el-option key="1" label="广东省" value="广东省"></el-option>
          <el-option key="2" label="湖南省" value="湖南省"></el-option>
        </el-select>
        <!-- <el-input
          v-model="query.name"
          placeholder="用户名"
          class="handle-input mr10"
        ></el-input> -->
        <el-button type="primary" icon="el-icon-search" 
          >搜索</el-button
        >

        <el-button type="primary" size="small" @click="dialogFormVisible = true"
          >上传表格</el-button
        >

        <el-button type="primary" @click="dialogDownVisible = true" size="small"
          >导出EXCEL</el-button
        >
      </div>

      <el-table
        :data="tableData"
        border
        class="table"
        ref="multipleTable"
        header-cell-class-name="table-header"
        @selection-change="handleSelectionChange"
      >
        <el-table-column
          type="selection"
          width="55"
          align="center"
        ></el-table-column>
        <el-table-column
          prop="统计日期"
          label="统计日期"
          align="center"
        ></el-table-column>
        <el-table-column prop="商品ID" label="商品ID"></el-table-column>
        <el-table-column
          prop="商品名称"
          label="商品名称"
          width="380"
          align="center"
        ></el-table-column>
        <el-table-column
          prop="商品浏览量"
          label="商品浏览量"
          align="center"
        ></el-table-column>
        <el-table-column
          prop="支付买家数"
          label="支付买家数"
          align="center"
        ></el-table-column>
        <el-table-column
          prop="支付金额"
          label="支付金额"
          align="center"
        ></el-table-column>
        <el-table-column
          prop="访客平均价值"
          label="访客平均价值"
          align="center"
        ></el-table-column>
        <!-- <el-table-column label="账户余额">
                    <template slot-scope="scope">￥{{scope.row.money}}</template>
                </el-table-column> -->
        <!-- <el-table-column label="头像(查看大图)" align="center">
                    <template slot-scope="scope">
                        <el-image
                            class="table-td-thumb"
                            :src="scope.row.thumb"
                            :preview-src-list="[scope.row.thumb]"
                        ></el-image>
                    </template>
                </el-table-column> -->
        <el-table-column
          prop="月累计支付金额"
          label="月累计支付金额"
          align="center"
        ></el-table-column>
        <!-- <el-table-column label="状态" align="center">
                    <template slot-scope="scope">
                        <el-tag
                            :type="scope.row.state==='成功'?'success':(scope.row.state==='失败'?'danger':'')"
                        >{{scope.row.state}}</el-tag>
                    </template>
                </el-table-column> -->

        <el-table-column
          prop="支付转化率"
          label="支付转化率"
          align="center"
        ></el-table-column>
        <el-table-column label="操作" width="180" align="center">
          <template slot-scope="scope">
            <el-button
              type="text"
              icon="el-icon-edit"
              @click="handleEdit(scope.$index, scope.row)"
              >编辑</el-button
            >
            <el-button
              type="text"
              icon="el-icon-delete"
              class="red"
              @click="handleDelete(scope.$index, scope.row)"
              >删除</el-button
            >
          </template>
        </el-table-column>
      </el-table>
      <div class="pagination">
        <el-pagination
          background
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="currentPage"
          :page-sizes="[10, 50, 100]"
          layout="total, sizes, prev, pager, next"
          :total="total"
        >
        </el-pagination>
        <div class="pagination-footer"></div>
      </div>
      <!-- 上传文件弹出框 -->

      <el-dialog title="上传文件" :visible.sync="dialogFormVisible" width="35%">
        <div
          class="upload-demo"
          v-if="loading"
          v-loading="loading"
          element-loading-text="数据上传中"
          element-loading-spinner="el-icon-loading"
          element-loading-background="white"
        ></div>

        <el-upload
          v-else
          class="upload-demo"
          drag
          :action="`${importApi}`"
          :http-request="upload"
          :limit="limit"
          :before-upload="beforeUpload"
          multiple
        >
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
          <div class="el-upload__tip" slot="tip">
            只能上传 {{ uploadType }} 文件，且不超过 {{ sizeLimit }} M
          </div>
        </el-upload>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="dialogFormVisible = false"
            >确 定</el-button
          >
        </div>
      </el-dialog>

      <!-- 下载文件弹出框 -->
      <el-dialog title="文件下载" :visible.sync="dialogDownVisible" width="30%">
   
        <div
          class="upload-demo"
          v-if="loading"
          v-loading="loading"
          element-loading-text="数据导出中"
          element-loading-spinner="el-icon-loading"
          element-loading-background="white"
        ></div>
        <div v-else>
          <el-date-picker
            v-model="timeRangeList"
            type="datetimerange"
            :picker-options="pickerOptions"
            range-separator="至"
            start-placeholder="开始日期"
            end-placeholder="结束日期"
            value-format="yyyy-MM-dd"
          >
          </el-date-picker>
          <el-button class="dialog-conent" type="primary" @click="download"
            >下载表格</el-button
          >
        </div>

        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogDownVisible = false">取 消</el-button>
          <el-button type="primary" @click="dialogDownVisible = false"
            >确 定</el-button
          >
        </div>
      </el-dialog>

      <!-- 编辑弹出框 -->
      <el-dialog title="编辑" :visible.sync="editVisible" width="30%">
        <el-form ref="form" :model="form" label-width="70px">
          <el-form-item label="用户名">
            <el-input v-model="form.name"></el-input>
          </el-form-item>
          <el-form-item label="地址">
            <el-input v-model="form.address"></el-input>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="editVisible = false">取 消</el-button>
          <el-button type="primary" @click="saveEdit">确 定</el-button>
        </span>
      </el-dialog>
    </div>
  </div>
</template>

<script>
import {
  downloadExcel,
  uploadExcel,
  apiBase,
  mongoData,
} from "../../api/index";
export default {
  name: "basetable",
  data() {
    return {
      exportApi: `${apiBase}/file/export`,
      importApi: `${apiBase}/file/import`,
      dialogFormVisible: false,
      dialogDownVisible: false,
      loading: false,
      limit: 1,
      sizeLimit: 100,
      uploadType: "Excel",

      query: {
        address: "广东",
        name: "",
      },
      tableData: [],
      total: 0,
      currentPage: 1, //初始页
      pagesize: 10, //    每页的数据
      multipleSelection: [],
      delList: [],
      editVisible: false,
      form: {},
      idx: -1,
      id: -1,
      pickerOptions: {
        shortcuts: [
          {
            text: "最近一周",
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit("pick", [start, end]);
            },
          },
          {
            text: "最近一个月",
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
              picker.$emit("pick", [start, end]);
            },
          },
          {
            text: "最近三个月",
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
              picker.$emit("pick", [start, end]);
            },
          },
        ],
      },
      timeRangeList: "",
    };
  },
  created() {
    this.getData();
  },

  methods: {
    getData() {
      mongoData({
        currentPage: this.currentPage,
        pageSize: this.pagesize,
      }).then((res) => {
        console.log(res);
        this.tableData = res.data.data.queryList;
        this.total = res.data.data.totalNum;
      });
    },

    // 初始页currentPage、初始每页数据数pagesize和数据data
    handleSizeChange(size) {
      this.pagesize = size;
      this.getData();

      // console.log(this.pagesize); //每页下拉显示数据
    },
    handleCurrentChange(currentPage) {
      this.currentPage = currentPage;
      this.getData();
      // console.log(this.currentPage); //点击第几页
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

    download() {
      var self = this;
      this.loading = true;
      console.log(this.timeRangeList);
      self.$api
        .downloadExcel({ timeRange: this.timeRangeList })
        .then((res) => {
          this.loading = false;
        //   console.log(res);
          const aLink = document.createElement("a");
          let blob = new Blob([res.data], {
            type: "application/vnd.ms-excel;charset=utf-8",
          });

          aLink.href = URL.createObjectURL(blob);
          let filename = res.headers["content-disposition"];
          aLink.download = filename;
          aLink.click();
          document.body.appendChild(aLink);
        })
        .catch(function (error) {
          console.log("error");
        });
    },

    upload(param) {
      var self = this;
      const formData = new FormData();
      formData.append("file", param.file);
      self.$api
        .uploadExcel(formData)
        .then((res) => {
          this.loading = false;
          console.log(res);
          self.$message.success({
            dangerouslyUseHTMLString: true,
            message: res.data.message,
          });
        })
        .catch(function (error) {
          console.log("error");
        });
    },

    handleDelete(index, row) {
      // 二次确认删除
      this.$confirm("确定要删除吗？", "提示", {
        type: "warning",
      })
        .then(() => {
          this.$message.success("删除成功");
          this.tableData.splice(index, 1);
        })
        .catch(() => {});
    },
    // 多选操作
    handleSelectionChange(val) {
      this.multipleSelection = val;
    },
    delAllSelection() {
      const length = this.multipleSelection.length;
      let str = "";
      this.delList = this.delList.concat(this.multipleSelection);
      for (let i = 0; i < length; i++) {
        str += this.multipleSelection[i].name + " ";
      }
      this.$message.error(`删除了${str}`);
      this.multipleSelection = [];
    },
    // 编辑操作
    handleEdit(index, row) {
      this.idx = index;
      this.form = row;
      this.editVisible = true;
    },
    // 保存编辑
    saveEdit() {
      this.editVisible = false;
      this.$message.success(`修改第 ${this.idx + 1} 行成功`);
      this.$set(this.tableData, this.idx, this.form);
    },
  },
};
</script>

<style scoped>
.upload-demo {
  margin-top: 0px;
  height: 150px;
}
.crumbs {
  margin-top: 0px;
}
.dialog-conent {
  margin-left: 15px;
}
.handle-box {
  margin-bottom: 15px;
}

.handle-select {
  width: 120px;
}

.handle-input {
  width: 300px;
  display: inline-block;
}
.table {
  width: 100%;
  font-size: 12px;
}
.red {
  color: #ff0000;
}
.mr10 {
  margin-right: 10px;
}
.table-td-thumb {
  display: block;
  margin: auto;
  width: 40px;
  height: 40px;
}
</style>
