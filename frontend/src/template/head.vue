<template>
    <header>
        <Layout>
            <Menu mode="horizontal" theme="dark" active-name="1">
                <div class="layout-title">基于大数据的智能岗位分析系统</div>
                <div class="layout-nav">
                    <MenuItem name="1">
                    <Icon type="ios-search"></Icon>
                    <a @click="$router.push({name:'post'}), POST()" :class="{choosen:ifPO}" >岗位查询</a>
                    </MenuItem>
                    <MenuItem name="2">
                    <Icon type="ios-person-outline"></Icon>
                    <a @click="$router.push({name:'personal'}), PERSONAL()" :class="{choosen:ifPE}" >个人定向查询</a>
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
      ifPO:'' ,
      ifPE:''
    };  
  },
  methods: {
    POST() {
      this.ifPO = true;
      this.ifPE =false;
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
.layout-logo {
  width: 100px;
  height: 30px;
  background: #5b6270;
  border-radius: 3px;
  float: left;
  position: relative;
  top: 15px;
  left: 20px;
}

.layout-title {
  font-size: 20px;
  color: #f5f7f9;
  float: left;
  position: relative;
  left: 100px;
}
.layout-nav {
  width: 420px;
  margin: 0 auto;
  margin-right: 10px;
}


.choosen {
  color: white;
}


.a {
  color: white
}

</style>
