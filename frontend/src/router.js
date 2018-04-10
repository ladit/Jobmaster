import App from './app.vue'
import head from "./template/head.vue";

import index from "./views/index.vue";
import post from "./template/post.vue";
import personal from "./template/personal.vue";

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
            path: 'personal',
            name: 'personal',
            component: personal,
        }
    ]
  }
];
export default routers;
