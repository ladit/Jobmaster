<template>

  <div class="main">
    <my-head style="position:fixed; left:0;width:100%;top:0;z-index:988;"></my-head>

    <div class="layout">
      <keep-alive>
        <router-view v-if="$route.meta.keepAlive"></router-view>
      </keep-alive>
      <router-view v-if="!$route.meta.keepAlive"></router-view>
    </div>
    <Footer class="layout-footer-center">Copyright © 2018 我全都要队 All Rights Reserved</Footer>

  </div>
</template>

<script>
export default {
    data() {
        return {};
    },
    components: {
        myHead: require("../template/Manager/mhead.vue")
    }
};
</script>

<style scoped>
.main {
    /* min-height: 800px; */
    height: auto;
    width: 100%;
    padding: 0;
    margin: 0;
    /* background-image: url('../images/bd.jpg'); */
    background-repeat: no-repeat;
    /* background-attachment: fixed; */
}

.layout {
    position: relative;
    border: 1px solid #d7dde4;
    min-height: 728px;
    /* background-image: url('../images/bmg.jpg'); */
    background-repeat: no-repeat;
}

.layout-footer-center {
    display: block;
    text-align: center;
    background: whitesmoke;
}
</style>