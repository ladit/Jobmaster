<template>
  <header>
    <Layout>
      <Menu mode="horizontal" active-name="1">

        <img  @click="$router.push({name:'homepage'})" class="logo" src="../../images/logo.png">
        <div @click="$router.push({name:'msignIn'})" class="layout-title">POLE 后台管理系统</div>

        <!-- <div class="nav">
          <a style="float: right;
                color:#FF4500;
  font-size: 17px;
  line-height: 48px;
  margin-top:6px;
  margin-right: 60px;" @click="$router.push({name:'signIn'})">注销</a>

        </div> -->
      </Menu>
    </Layout>
  </header>
</template>
<script>
export default {
  data() {
    return {
      ifPO: "",
      ifPE: ""
    };
  },
  methods: {
    POST() {
      this.ifPO = true;
      this.ifPE = false;
    },
    PERSONAL() {
      this.ifPO = false;
      this.ifPE = true;
    }
  }
};
</script>

<style scoped>
.layout {
  border: 1px solid #d7dde4;
  background: #f5f7f9;
  position: relative;
  border-radius: 4px;
  overflow: hidden;
}

.logo {
  width: 50px;
  height: 56px;
  float: left;
  margin-top: 4px;
  margin-left: 100px;
}

.layout-title {
  font-size: 20px;
  color: #47769c;
  float: left;
  position: relative;
  margin-left: 20px;
}
nav {
  float: right;
  font-size: 26px;
  line-height: 48px;
  margin-right: 30px;
}

.choosen {
  /* color: #71C093; */
}
</style>
