<template>
    <div class="login">
        <my-head style="position:absolute;top:0;z=index:99999;height:20px;"></my-head>
        <h2 style="color:#47769C;margin-top:70px;">Login</h2>
        <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="60">
            <Form-item label="账号" prop="user">
                <Input type="text" v-model="formValidate.user" placeholder="">
                <Icon type="ios-person-outline" slot="prepend"></Icon>
                </Input>
            </Form-item>
            <Form-item label="密码" prop="password" class="password">
                <Input type="password" v-model="formValidate.password">
                <Icon type="ios-locked-outline" slot="prepend"></Icon>
                </Input>
            </Form-item>
            <Form-item>
                <a class="forget-password">忘记密码</a>
                <Button type="success" long @click="$router.push({name:'major'})">登录</Button>
                <!-- <Button type="success" long @click="handleSubmit('formValidate')">登录</Button> -->
            </Form-item>
        </Form>
    </div>
</template>

<script>
// import axios from "axios";
export default {
  name: "signUpPageOne",
  data() {
    return {
      current: 0,
      formValidate: {
        user: " ",
        password: ""
      },
      ruleValidate: {
        user: [{  message: "手机号不能为空", trigger: "blur" }],
        password: [
          {  message: "请填写密码", trigger: "blur" },
          {
            type: "string",
            min: 6,
            message: "密码长度不能小于6位",
            trigger: "blur"
          }
        ]
      }
    };
  },
  mounted() {
    var that = this;
  },
  methods: {},
  components: {
    myHead: require("./mhead")
  }
};
</script>

<style scoped>

.login {
  padding-top: 60px;
  margin: 0px auto;
  height: 686px;
}

h2 {
  font-size: 26px;
  text-align: center;
}

form {
  width: 360px;
  margin: 20px auto;
  padding-right: 50px;
}

.password {
  margin: 0;
  padding: 0;
}

.forget-password {
  float: right;
  margin: 0;
  padding: 0;
}

button {
  font-size: 14px;
}
</style>

