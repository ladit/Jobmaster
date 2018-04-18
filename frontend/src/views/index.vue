<template>
  <div class="main">
    <my-head></my-head>
    <div class="layout">
      <keep-alive>
        <router-view v-if="$route.meta.keepAlive"></router-view>
      </keep-alive>
      <router-view v-if="!$route.meta.keepAlive"></router-view>
    </div>
    <Footer class="layout-footer-center">2018 &copy; 我全都要队</Footer>

  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  components: {
    myHead: require("../template/head.vue")
  }
};
</script>

<style scoped>
.main {
  height: 770px;
  width: 100%;
  padding: 0;
  margin: 0;
  /* background-image: url('../images/bd.jpg'); */
  background-repeat: no-repeat;
  background-attachment: fixed;
}

.layout {
  border: 1px solid #d7dde4;
  /* height: 2000px; */
}

.layout-content {
  min-height: 200px;
  margin: 15px;
  overflow: hidden;
  border-radius: 4px;
}
.layout-footer-center {
  text-align: center;
  background: whitesmoke;
}
</style>