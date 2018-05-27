<template>
  <header>
    <Layout>
      <Menu mode="horizontal" active-name="1">

        <img @click="$router.push({name:'homepage'})" class="logo" src="../images/logo.png">
        <p @click="$router.push({name:'msignIn'})" class="layout-title">基于大数据的智能求职分析系统</p>

        <div class="layout-nav">
          <MenuItem name="1">
          <Icon type="ios-search"></Icon>
          <a @click="$router.push({name:'post'}), POST()" :class="{choosen:ifPO}">岗位查询</a>
          </MenuItem>
          <MenuItem name="2">
          <Icon type="ios-person-outline"></Icon>
          <a @click="$router.push({name:'personal'}), PERSONAL()" :class="{choosen:ifPE}">个人定向查询</a>
          </MenuItem>
        </div>
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
  color: #47769C;
  float: left;
  position: relative;
  margin-left: 20px;
}
.layout-nav {

  margin-left: 720px;
  float: left;
}

.choosen {
  color: #71C093;
}
</style>
