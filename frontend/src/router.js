import App from './app.vue'
import head from "./template/head.vue";

import index from "./views/index.vue";
import post from "./template/post.vue";
import personal from "./template/personal.vue";
import test from "./template/test.vue";
import homepage from "./template/homepage.vue";

const routers = [
  {
    path: "/",
    component: index,
    children: [
        {
            path: 'post',
            name: 'post',
            component: post,
        },
        {
            path: 'test',
            name: 'test',
            component: test,
        },
        {
            path: 'personal',
            name: 'personal',
            component: personal,
        },
        ,
        {
            path: '',
            name: 'homepage',
            component: homepage,
        }
    ]
  }
];
export default routers;
