<template>
    <div class="container">
        <!-- <video style="width: 100%;height: 100%;" id="video" webkit-playsinline="true" preload="auto" controls="controls" loop="loop">
            <source id="videoSource" type="video/mp4"> 您的浏览器不支持该视频格式。
        </video> -->
        <div style="margin-left:20.2%;margin-top:100px;">
            <textarea v-model="skill" placeholder="个人技能描述……" name="" id="" cols="105" rows="2" style="font-size:16px;color:#888;padding-left:6px;padding-top:2px;border:1px solid #E4E4E4;"></textarea>
        </div>
        <br>

        <div class="input">
            <Select v-model="edu" style="width:100px;margin-left:20%" placeholder="选择学历">
                <Option v-for="item in cityList1" :value="item.value" :key="item.value">{{ item.label }}</Option>
            </Select>
            <Input v-model="major" placeholder="输入专业" style="width: 150px"></Input>
            <Input v-model="value1" placeholder="输入学校" style="width: 150px"></Input>
            <Input v-model="workplace" placeholder="输入求职地" style="width: 150px"></Input>
            <Input v-model="keyword" placeholder="输入岗位名称" style="width: 150px" on-blur="bb" on-focus="get($event)" @input="get($event)" @keydown.down.prevent="selectDown" @keydown.up.prevent="selectUp"></Input>
            <ul style="width: 305px;margin-left:57%;font-size:14px;position:absolute;list-style:none; border:1px solid #E8E8E8;">
                <li style="padding-left:10px; padding:3px 8px;" class="text-center" v-for="(value,index) in myData">
                    <span @click="jump" class="text-success textprimary" :class="{gray:index==now}">{{value}}</span>
                </li>
            </ul>
            <Input v-model="exp" placeholder="输入工作年限" style="width: 150px"></Input>
            <Button style="margin-left:20px;margin-top:2px;" type="info" icon="ios-search" @click="btn">匹配查询</Button>
        </div>
        <br>
        <br>

        <div style="margin-left:100px;margin-top:40px;">
            <p style="font-size:22px;font-weight:bold;float:left;color:black">{{job}}待遇水平：</p>
            <p style="font-size:22px;;float:left">{{salary}}</p>
        </div>
        <br>
        <br>

        <div style="margin-left:100px;margin-top:30px;">
            <p style="font-size:22px;font-weight:bold;color:black">求职者画像</p>
            <div id="myChart1" :style="{margin:'0 auto',width: '600px', height: '500px'}"></div>
        </div>
        <br>

        <p style="margin-left:100px;font-size:22px;font-weight:bold;color:black">匹配企业</p>
        <br>
        <br>
        <br>
        <br>

        <div style="margin-left:50px;margin-top:-50px;">

            <div class="hover-hidden1">

                <div class=" box-item " v-for="item in classList" :key="item.company_name">
                    <br>
                    <p style="color: black;font-size:1.3rem;font-weight:bold;text-align:center;">{{item.company_name}}</p>
                    <div class="content">
                        <p>工资：{{item.payment}}</p>
                        <p>福利：{{item.welfare}}</p>
                        <p>公司规模：{{item.size}}</p>
                        <br>
                        <a v-bind:href="item.url" title="查看详情" target="_blank">匹配概率：{{Number(item.rate*100).toFixed(2)}}%</a>
                        <br>
                    </div>
                </div>
            </div>

        </div>
    </div>

</template>


<script src="echarts.min.js"></script>
<script src="echarts-wordcloud.min.js"></script>



<script src="http://cdn.bootcss.com/jquery/3.0.0-alpha1/jquery.min.js"></script>  
<script src="http://cdn.bootcss.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>  

<script>
import axios from "axios";
import Data from "../libs/test.js";
export default {
    data() {
        return {
            job: "",
            classList: [],
            skill: "",
            now: -1,
            newData: Data.customData(),
            myData: [],
            salary: "",
            edu: "",
            keyword: "",
            exp: "",
            workplace: "",
            major: "",
            value1: "",
            cityList1: [
                {
                    value: "0",
                    label: "不限"
                },
                {
                    value: "1",
                    label: "中技"
                },
                {
                    value: "2",
                    label: "中专"
                },
                {
                    value: "3",
                    label: "高中"
                },
                {
                    value: "4",
                    label: "大专"
                },
                {
                    value: "5",
                    label: "本科"
                },
                {
                    value: "6",
                    label: "硕士"
                },
                {
                    value: "7",
                    label: "博士"
                }
            ],
            leverl1: [],
            leverl2: [],
            exp1: "",
            exp2: "",
            edu1: "",
            edu2: "",
            payment1: "",
            payment2: ""
        };
    },
    mounted() {
        this.drawLine();
    },
    methods: {
        videoPlay(videoplayurl) {
            var _videoPlay = document.getElementById("video");
            var _videoSource = document.getElementById("video");
            _videoSource.src =
                "http://img.vip.kanimg.com/img/banner/201702241034284066.mp4";
            _videoPlay.play();
        },
        cli: function() {
            window.open("https://jobs.51job.com/beijing-cyq/98792553.html?s=01&t=0");
        },
        jump: function(e) {
            this.keyword = e.target.innerHTML;
            this.myData = [];
        },
        get: function(event) {
            this.myData = [];
            var st = this.newData;
            var word = this.keyword;
            word = word.replace(" ", "");
            if (word == "") return;
            var s = '"[^' + word + '",]*' + word + '[^"]*"';
            var pat = new RegExp(s, "ig");
            var ans = st.match(pat);
            if (!ans) {
                this.myData.push("无匹配结果,请重新输入");
                return;
            }
            var len = 0;
            len = ans.length;
            for (var i = 0; i < Math.min(6, len); ++i) {
                this.myData.push(ans[i].replace(/\"/gi, ""));
            }
        },
        selectDown: function() {
            this.now++;
            if (this.now == this.newData.length) this.now = -1;
            this.keyword = this.newData[this.now];
        },
        selectUp: function() {
            this.now--;
            if (this.now == -2) this.now = this.newData.length - 1;
            this.keyword = this.newData[this.now];
        },
        btn: function() {
            var that = this;
            console.log(that.keyword);
            that.job = that.keyword;
            that.classList=[];
            that.leverl1=[];
            that.leverl2=[];

            this.$http({
                method: "post",
                url: "http://127.0.0.1:8000/api/recommendation",
                data: {
                    job_show_name: that.keyword,
                    edu: that.edu,
                    exp: that.exp,
                    skill: that.skill,
                    major: that.major,
                    workplace: that.workplace
                }
            }).then(res => {
                console.log("res => ", res);
                that.salary = res.data.payment_range;

                that.edu1 = parseInt(res.data.average.edu);

                that.edu2 = parseInt(res.data.personal.edu);
                that.exp1 = parseInt(res.data.average.exp);
                that.exp2 = parseInt(res.data.personal.exp);
                that.payment1 = parseInt(res.data.average.payment);
                that.payment2 = parseInt(res.data.personal.payment);
                that.leverl1.push(that.edu2);
                that.leverl1.push(that.exp2);
                that.leverl1.push(that.payment2);
                that.leverl2.push(that.edu1);
                that.leverl2.push(that.exp1);
                that.leverl2.push(that.payment1);

                var len = res.data.jobs.length;
                for (var i = 0; i < len; ++i) {
                    var tmp = {
                        company_name: "",
                        payment: 0,
                        size: 0,
                        url: "",
                        welfare: "",
                        rate: 0
                    };
                    tmp.company_name = res.data.jobs[i].company_name;
                    tmp.payment = res.data.jobs[i].payment;
                    tmp.size = res.data.jobs[i].size;
                    tmp.url = res.data.jobs[i].url;
                    tmp.welfare = res.data.jobs[i].welfare;
                    tmp.rate = res.data.jobs[i].rate;

                    that.classList.push(tmp);
                }

                that.drawLine();
            });
        },
        drawLine() {
            var that = this;
            var LEVEL1 = that.leverl1;
            var LEVEL2 = that.leverl2;
            var echarts = require("echarts");
            require("echarts-wordcloud");
            // 基于准备好的dom，初始化echarts实例

            let myChart1 = this.$echarts.init(
                document.getElementById("myChart1")
            );
            myChart1.setOption({
                title: {
                    text: ""
                },
                tooltip: {},
                legend: {
                    data: ["个人水平", "平均水平"]
                },
                radar: {
                    // shape: 'circle',

                    indicator: [
                        { name: "学历", max: 7 },
                        { name: "工作经验", max: 15 },
                        { name: "工资", max: 30000 }
                    ]
                },
                series: [
                    {
                        name: "预算 vs 开销（Budget vs spending）",
                        type: "radar",
                        // areaStyle: {normal: {}},
                        data: [
                            {
                                value: LEVEL1,
                                name: "个人水平"
                            },
                            {
                                value: LEVEL2,
                                name: "平均水平"
                            }
                        ]
                    }
                ]
            });
        }
    }
};
</script>


<style scoped>
.container {
    display: flex;
    min-height: 100vh;
    flex-direction: column;
}

.layout {
    border: 1px solid #d7dde4;
    background: #f5f7f9;
    position: relative;
    border-radius: 4px;
    overflow: hidden;
}
.box-item {
    float: left;
    margin: 16px;
    width: 22%;
    height: 300px;
    position: relative;
    /* background-color: #fff0f5; */
    /* background-color: #c1ffc1; */
}
.content {
    cursor: pointer;
    border: 1px solid black;
    width: 80%;
    height: 230px;
    position: absolute;
    top: 80px;
    margin-left: 30px;
    -moz-transition: all 1s linear 0.1s;
    -webkit-transition: all 1s linear 0.1s;
    -o-transition: all 1s linear 0.1s;
    -ms-transition: all 1s linear 0.1s;
    transition: all 1s linear 0.1s;
}

.content:hover {
    background-color: #BCD2EE;
}

.content p {
    font-size: 16px;
    padding-top: 10px;
    padding-left: 30px;
    padding-right: 18px;
    color: #828282;

    line-height: 24px;
}

.content a {
    margin-left: 64px;
    color: #71C093;
    font-size: 16px;
    position: absolute;
    bottom: 20px;
}

.hover-show1 {
    position: absolute; /*注意这两个盒子要设置为绝对定位*/
    width: 200px;
    height: 240px;
    /* background: #fe4563; */
    background: #71c093;

    text-align: center;
    color: #fff;
    font-size: 20px;
    padding-top: 50px;
    opacity: 0;
    /*为鼠标移入时显示的那个盒子的显示绑定动画*/
    -moz-transition: all 1s linear 0.1s;
    -webkit-transition: all 1s linear 0.1s;
    -o-transition: all 1s linear 0.1s;
    -ms-transition: all 1s linear 0.1s;
    transition: all 1s linear 0.1s;
    /* -moz-transform: translateX(-100px);  
  -webkit-transform: translateX(-100px);
  -o-transform: translateX(-100px);
  transform: translateX(-100px); */
}
.hover-hidden1 {
    position: relative; /*注意这两个盒子要设置为绝对定位*/
    /* width: 400px;
  text-align: center; */
    /*为鼠标移入时隐藏的那个盒子的显示绑定动画*/
    width: 100%;
    height: auto;
    min-height: 600px;
    -moz-transition: all 1s ease-out 0.1s;
    -webkit-transition: all 1s ease-out 0.1s;
    -o-transition: all 1s ease-out 0.1s;
    -ms-transition: all 1s ease-out 0.1s;
    transition: all 1s ease-out 0.1s;
}
.container-detailed:hover .hover-hidden1 {
    /* -moz-transform: rotate(90deg) scale(0.5);
  -webkit-transform: rotate(90deg) scale(0.5);
  -o-transform: rotate(90deg) scale(0.5);
  transform: rotate(90deg) scale(0.5); */
    opacity: 0;
}
.container-detailed:hover .hover-show1 {
    -moz-transform: translateX(0px);
    -webkit-transform: translateX(0px);
    -o-transform: translateX(0px);
    transform: translateX(0px);
    opacity: 1;
}
.container ul :hover {
    background-color: #f0f0f0;
}
::-webkit-input-placeholder {
    /* WebKit browsers */
    color: #888;
}
</style>

