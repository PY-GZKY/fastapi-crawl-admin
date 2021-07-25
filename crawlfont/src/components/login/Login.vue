<template>
  <div class="login-wrap">
    <div class="ms-login">
      <div class="ms-title">Fastapi-Crawl</div>
      <el-form :model="ruleForm" :rules="rules" ref="login" label-width="0px" class="ms-content">
        <el-form-item prop="username">
          <el-input v-model="ruleForm.username" placeholder="username">
            <el-button slot="prepend" icon="el-icon-lx-people"></el-button>
          </el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input
            type="password"
            placeholder="password"
            v-model="ruleForm.password"
            @keyup.enter.native="submitForm()"
          >
            <el-button slot="prepend" icon="el-icon-lx-lock"></el-button>
          </el-input>
        </el-form-item>
        <div class="login-btn">
          <el-button type="primary" @click="submitForm(ruleForm)">登录</el-button>
        </div>
        <p class="login-tips">Tips: 爬虫调度后台</p>
      </el-form>
    </div>
  </div>
</template>

<script>
import { login } from "../../api/index";
export default {
  data: function () {
    return {
      ruleForm: {
        username: "",
        password: "",
      },
      rules: {
        username: [{ required: true, trigger: "blur" }],
        password: [{ required: true, trigger: "blur" }],
      },
    };
  },
  methods: {
    submitForm(ruleForm) {
      const self = this;
      self.$refs.login.validate((valid) => {
        if (valid) {
          var login_data = {
            username: self.ruleForm.username,
            password: self.ruleForm.password,
          };
          console.log(login_data);
          self.$api.login(login_data)
            .then((result) => {
              console.log(result);
              if (result.data.code === 200) {
                localStorage.setItem('username',self.ruleForm.username);
                sessionStorage.setItem('username',self.ruleForm.username);
                localStorage.setItem('token',result.data.data.token);
                self.$message.success("登录成功");
                self.$router.push("/");
              } else {
                self.$message.error("完犊子了???");
              }
            })
            .catch(function (error) {
              console.log(error);
              self.$message.error("完犊子了???");
            });
        } else {
          self.$message.error("请输入账号和密码");
          console.log("error submit!!");
          return false;
        }
      });
    },
  },
};
</script>

<style scoped>
.login-wrap {
  position: relative;
  width: 100%;
  height: 100%;
  background-image: url(../../assets/img/login-bg.jpg);
  background-size: 100%;
}
.ms-title {
  width: 100%;
  line-height: 50px;
  text-align: center;
  font-size: 17px;
  color: rgb(0, 0, 0);
  border-bottom: 1px solid rgb(96, 134, 139);
}
.ms-login {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 350px;
  margin: -190px 0 0 -175px;
  border-radius: 5px;
  background: rgba(255, 255, 255, 0.3);
  overflow: hidden;
}
.ms-content {
  padding: 30px 30px;
  /* width: 300px;
  height: 300px; */
}
.login-btn {
  text-align: center;
}
.login-btn button {
  width: 100%;
  height: 36px;
  margin-bottom: 10px;
}
.login-tips {
  font-size: 12px;
  line-height: 30px;
  color: #fff;
}
</style>