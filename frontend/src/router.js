import App from './app.vue'
import head from "./template/head.vue";

import index from "./views/index.vue";
import mindex from "./views/mindex.vue";
import post from "./template/post.vue";
import personal from "./template/personal.vue";
import test from "./template/test.vue";
import homepage from "./template/homepage.vue";
import msignIn from "./template/Manager/msignIn.vue";
import mhead from "./template/Manager/mhead.vue";
import major from "./template/Manager/major.vue";

const routers = [{
        path: "/",
        component: index,
        children: [{
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
            {
                path: '',
                name: 'homepage',
                component: homepage,
            },
            {
                path: 'mindex',
                name: 'mindex',
                component: mindex
            }
        ]
    },
    {
        path: "mindex",
        component: mindex,
        children: [{

                path: '',
                name: 'msignIn',
                component: msignIn
            },
            {

                path: 'major',
                name: 'major',
                component: major
            }
        ]
    }
];
export default routers;