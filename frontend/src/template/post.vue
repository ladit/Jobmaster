<template>
    <div class="container" >
        <div style="margin-top:280px;" v-if="isShow1" >
            <Input placeholder="输入相关岗位，如大数据、分析师等" size="large" style="width: 400px;margin-left:40%;font-size:20px" v-model="keyword" on-blur="bb" on-focus="get($event)" @input="get($event)" @keydown.down.prevent="selectDown" @keydown.up.prevent="selectUp">
            <Button slot="append" icon="ios-search" @click="btn"></Button>
            </Input>
            <ul style="width: 358.5px;margin-left:40%;font-size:14px;position:absolute;list-style:none; border:1px solid #E8E8E8;">
                <li style="padding-left:10px; padding:3px 8px;" class="text-center" v-for="(value,index) in myData">
                    <span @click="jump" class="text-success textprimary" :class="{gray:index==now}">{{value}}</span>
                </li>
            </ul>
        </div>
        <div style="margin-top:100px;" v-if="isShow" >
            <Input placeholder="输入相关岗位，如大数据、分析师等" size="large" style="width: 400px;margin-left:40%;font-size:20px" v-model="keyword" on-blur="bb" on-focus="get($event)" @input="get($event)" @keydown.down.prevent="selectDown" @keydown.up.prevent="selectUp">
            <Button slot="append" icon="ios-search" @click="btn"></Button>
            </Input>
            <ul style="width: 358.5px;margin-left:40%;font-size:14px;position:absolute;list-style:none; border:1px solid #E8E8E8;">
                <li style="padding-left:10px; padding:3px 8px;" class="text-center" v-for="(value,index) in myData">
                    <span @click="jump" class="text-success textprimary" :class="{gray:index==now}">{{value}}</span>
                </li>
            </ul>
        </div>

        <div style="margin-left:100px;margin-top:30px;"  v-if="isShow">
            <p style="font-size:22px;font-weight:bold;float:left;color:black">岗位名称：</p>
            <p style="font-size:22px;;float:left">{{name}}</p>
        </div>
        <br>

        <div style="margin-left:100px;margin-top:30px;"  v-if="isShow">
            <p style="font-size:22px;font-weight:bold;float:left;color:black">最低工作经历要求：</p>
            <p style="font-size:22px;;float:left">{{year}}</p>
        </div>
        <br>

        <div style="margin-left:100px;margin-top:30px;"  v-if="isShow">
            <p style="font-size:22px;font-weight:bold;color:black">岗位描述</p>
            <div id="myChart5" :style="{margin:'0 auto',width: '600px', height: '400px'}"></div>
        </div>

        <div style="margin-left:100px;float:left"  v-if="isShow">
            <p style="font-size:22px;font-weight:bold;color:black">岗位画像</p>
            <div id="myChart1" :style="{float: 'left',width: '460px', height: '460px'}"></div>
            <div id="myChart2" :style="{float: 'left',width: '460px', height: '460px'}"></div>
            <div id="myChart3" :style="{float: 'left',width: '460px', height: '460px'}"></div>
        </div>

        <div style="margin-left:100px;margin-top:50px;float:left"  v-if="isShow">
            <p style="font-size:22px;font-weight:bold;color:black">工作地分布</p>
            <div id="myChart4" :style="{width: '1000px', height: '800px'}"></div>
        </div>

    </div>

</template>




<script src="echarts.min.js"></script>
<script type="text/javascript" src="echarts.min.js"></script>  
<script type="text/javascript" src="china.js"></script> 
<script src="echarts-wordcloud.min.js"></script>


<script charset="utf-8" src="http://map.qq.com/api/js?v=2.exp"></script>


<script>
import axios from "axios";
import Data from "../libs/test.js";
import func from "../libs/canvas.js";
export default {
    data() {
        return {
            isShow1:true,
            isShow:false,
            value1: "",
            newData: Data.customData(),
            keyword: "",
            now: -1,
            myData: [],
            name: "大数据研发工程师",
            year: "无年限要求",
            WCNAME: [
                { name: "hive", value: 92 },
                { name: "大数据", value: 108 },
                { name: "算法", value: 67 },
                { name: "linux", value: 79 },
                { name: "hadoop", value: 141 },
                { name: "团队", value: 72 },
                { name: "经验", value: 148 },
                { name: "java", value: 134 },
                { name: "hbase", value: 83 },
                { name: "spark", value: 130 },
                { name: "python", value: 94 }
            ],
            STUList1: [
                { name: "不限", value: 18 },
                { name: "中技", value: 1 },
                { name: "中专", value: 3 },
                { name: "高中", value: 0 },
                { name: "大专", value: 44 },
                { name: "本科", value: 88 },
                { name: "硕士", value: 11 },
                { name: "博士", value: 0 }
            ],
            STUList2: [
                { name: "0-5000", value: 25 },
                { name: "0-面议", value: 13 },
                { name: "10000-25000", value: 74 },
                { name: "5000-10000", value: 36 },
                { name: "80000+", value: 1 },
                { name: "80000+", value: 1 },
                { name: "25000-50000", value: 15 },
                { name: "50000-80000", value: 1 }
            ],
            STUList3: [
                { name: "8000-20000", value: 12 },
                { name: "20000+", value: 0 },
                { name: "800-2000", value: 4 },
                { name: "0-100", value: 50 },
                { name: "2000-8000", value: 32 },
                { name: "100-800", value: 26 }
            ],
            map1: [
                {
                    name: "北京",
                    value: 38
                },
                {
                    name: "南京",
                    value: 147
                },
                {
                    name: "吉林",
                    value: 74
                },
                {
                    name: "上海",
                    value: 33
                },
                {
                    name: "成都",
                    value: 192
                },
                {
                    name: "哈尔滨",
                    value: 35
                },
                {
                    name: "沈阳",
                    value: 0
                },
                {
                    name: "武汉",
                    value: 36
                },
                {
                    name: "石家庄",
                    value: 32
                },
                {
                    name: "天津",
                    value: 7
                },
                {
                    name: "太原",
                    value: 1
                },
                {
                    name: "西安",
                    value: 63
                },
                {
                    name: "南宁",
                    value: 29
                },
                {
                    name: "南昌",
                    value: 48
                },
                {
                    name: "济南",
                    value: 61
                }
            ]
        };
    },
    mounted() {
        // function location(data) {
        //     console.log(data);
        // }
        // this.$http({
        //     methods: "get",
        //     url:
        //         "http://api.map.baidu.com/geocoder/v2/?address=北京&ak=7anorUrPABCFBPahSQl0tpi8SW1XMq5v&output=json&callback=showLocation"
        // });
        this.drawLine();
    },
    methods: {
        showLocation: function(data) {
            console.log(data);
        },

        btn: function() {
            this.isShow = true;
            this.isShow1 = false;
            this.name = this.keyword;
            const that = this;
            this.$http({
                method: "post",
                url: "http://127.0.0.1:8000/api/job_portrait",
                data: {
                    job_show_name: that.name
                }
            }).then(res => {
                var that = this;
                // console.log(res);
                if (res.data.least_exp == 0) {
                    that.year = "无年限要求";
                } else {
                    that.year = res.data.least_exp;
                }

                //wordcloud

                var wcdata = [
                    {
                        name: "",
                        value: 100,
                        textStyle: {
                            normal: {
                                color: "black"
                            },
                            emphasis: {
                                color: "red"
                            }
                        }
                    }
                ];

                var dec = res.data.dec;
                for (let key in dec) {
                    var tmp = { name: "", value: 0 };
                    tmp.name = key;
                    tmp.value = dec[key];
                    wcdata.push(tmp);
                }

                that.WCNAME = wcdata;

                //xueliyaoqiu

                var stuList1 = [];
                var edu = [
                    "不限",
                    "中技",
                    "中专",
                    "高中",
                    "大专",
                    "本科",
                    "硕士",
                    "博士"
                ];
                var dec = res.data.edu_demand_distribution;
                for (let key in dec) {
                    var tmp = { name: "", value: 0 };
                    tmp.name = edu[key];
                    tmp.value = dec[key];
                    stuList1.push(tmp);
                }

                that.STUList1 = stuList1;

                //gongzifenbu

                var stuList2 = [];

                var dec = res.data.payment_distribution;
                for (let key in dec) {
                    var tmp = { name: "", value: 0 };
                    tmp.name = key;
                    tmp.value = dec[key];
                    stuList2.push(tmp);
                }

                that.STUList2 = stuList2;

                //gongsiguimo

                var stuList3 = [];

                var dec = res.data.company_size_distribution;
                for (let key in dec) {
                    var tmp = { name: "", value: 0 };
                    tmp.name = key;
                    tmp.value = dec[key];
                    stuList3.push(tmp);
                }

                that.STUList3 = stuList3;

                //map
                var map2 = [];
                var dec = res.data.workplace_distribution;
                for (let key in dec) {
                    var tmp = { name: "", value: 0 };
                    tmp.name = key;
                    tmp.value = dec[key];
                    map2.push(tmp);
                }
                that.map1 = map2;

                that.drawLine();
            });
        },
        jump: function(e) {
            this.keyword = e.target.innerHTML;
            this.myData = [];
        },
        bb: function() {
            alert("dd");
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
        drawLine() {
            // 基于准备好的dom，初始化echarts实例
            var that = this;
            let myChart1 = this.$echarts.init(
                document.getElementById("myChart1")
            );
            // 绘制图表
            var data1 = that.STUList1;
            myChart1.setOption({
                backgroundColor: "#fff",
                title: {
                    text: "学历分布",
                    x: "center",
                    y: "center",
                    textStyle: {
                        fontWeight: "normal",
                        fontSize: 16
                    }
                },
                tooltip: {
                    show: true,
                    trigger: "item",
                    formatter: "{b}: {c} ({d}%)"
                },
                legend: {
                    orient: "horizontal",
                    bottom: "0%",
                    data: data1
                },
                series: [
                    {
                        type: "pie",
                        selectedMode: "single",
                        radius: ["25%", "58%"],
                        color: [
                            "#86D560",
                            "#AF89D6",
                            "#59ADF3",
                            "#FF999A",
                            "#FFCC67"
                        ],

                        label: {
                            normal: {
                                position: "inner",
                                formatter: "{d}%",

                                textStyle: {
                                    color: "#fff",
                                    fontWeight: "bold",
                                    fontSize: 14
                                }
                            }
                        },
                        labelLine: {
                            normal: {
                                show: false
                            }
                        },
                        data: data1
                    },
                    {
                        type: "pie",
                        radius: ["58%", "83%"],
                        itemStyle: {
                            normal: {
                                color: "#F2F2F2"
                            },
                            emphasis: {
                                color: "#ADADAD"
                            }
                        },
                        label: {
                            normal: {
                                position: "inner",
                                formatter: "{c}人",
                                textStyle: {
                                    color: "#777777",
                                    fontWeight: "bold",
                                    fontSize: 14
                                }
                            }
                        },
                        data: data1
                    }
                ]
            });
            var data2 = that.STUList2;
            let myChart2 = this.$echarts.init(
                document.getElementById("myChart2")
            );
            // 绘制图表
            myChart2.setOption({
                backgroundColor: "#fff",
                title: {
                    text: "工资分布",
                    x: "center",
                    y: "center",
                    textStyle: {
                        fontWeight: "normal",
                        fontSize: 16
                    }
                },
                tooltip: {
                    show: true,
                    trigger: "item",
                    formatter: "{b}: {c} ({d}%)"
                },
                legend: {
                    orient: "horizontal",
                    bottom: "0%",
                    data: data2
                },
                series: [
                    {
                        type: "pie",
                        selectedMode: "single",
                        radius: ["25%", "58%"],
                        color: [
                            "#86D560",
                            "#AF89D6",
                            "#59ADF3",
                            "#FF999A",
                            "#FFCC67"
                        ],

                        label: {
                            normal: {
                                position: "inner",
                                formatter: "{d}%",

                                textStyle: {
                                    color: "#fff",
                                    fontWeight: "bold",
                                    fontSize: 14
                                }
                            }
                        },
                        labelLine: {
                            normal: {
                                show: false
                            }
                        },
                        data: data2
                    },
                    {
                        type: "pie",
                        radius: ["58%", "83%"],
                        itemStyle: {
                            normal: {
                                color: "#F2F2F2"
                            },
                            emphasis: {
                                color: "#ADADAD"
                            }
                        },
                        label: {
                            normal: {
                                position: "inner",
                                formatter: "{c}人",
                                textStyle: {
                                    color: "#777777",
                                    fontWeight: "bold",
                                    fontSize: 14
                                }
                            }
                        },
                        data: data2
                    }
                ]
            });
            var data3 = that.STUList3;
            let myChart3 = this.$echarts.init(
                document.getElementById("myChart3")
            );
            // 绘制图表
            myChart3.setOption({
                backgroundColor: "#fff",
                title: {
                    text: "公司规模",
                    subtext: "2018年",
                    x: "center",
                    y: "center",
                    textStyle: {
                        fontWeight: "normal",
                        fontSize: 16
                    }
                },
                tooltip: {
                    show: true,
                    trigger: "item",
                    formatter: "{b}: {c} ({d}%)"
                },
                legend: {
                    orient: "horizontal",
                    bottom: "0%",
                    data: data3
                },
                series: [
                    {
                        type: "pie",
                        selectedMode: "single",
                        radius: ["25%", "58%"],
                        color: [
                            "#86D560",
                            "#AF89D6",
                            "#59ADF3",
                            "#FF999A",
                            "#FFCC67"
                        ],

                        label: {
                            normal: {
                                position: "inner",
                                formatter: "{d}%",

                                textStyle: {
                                    color: "#fff",
                                    fontWeight: "bold",
                                    fontSize: 14
                                }
                            }
                        },
                        labelLine: {
                            normal: {
                                show: false
                            }
                        },
                        data: data3
                    },
                    {
                        type: "pie",
                        radius: ["58%", "83%"],
                        itemStyle: {
                            normal: {
                                color: "#F2F2F2"
                            },
                            emphasis: {
                                color: "#ADADAD"
                            }
                        },
                        label: {
                            normal: {
                                position: "inner",
                                formatter: "{c}家",
                                textStyle: {
                                    color: "#777777",
                                    fontWeight: "bold",
                                    fontSize: 14
                                }
                            }
                        },
                        data: data3
                    }
                ]
            });
            var geoCoordMap = {
                海门: [121.15, 31.89],
                鄂尔多斯: [109.781327, 39.608266],
                招远: [120.38, 37.35],
                舟山: [122.207216, 29.985295],
                齐齐哈尔: [123.97, 47.33],
                盐城: [120.13, 33.38],
                赤峰: [118.87, 42.28],
                青岛: [120.33, 36.07],
                乳山: [121.52, 36.89],
                金昌: [102.188043, 38.520089],
                泉州: [118.58, 24.93],
                莱西: [120.53, 36.86],
                日照: [119.46, 35.42],
                胶南: [119.97, 35.88],
                南通: [121.05, 32.08],
                拉萨: [91.11, 29.97],
                云浮: [112.02, 22.93],
                梅州: [116.1, 24.55],
                文登: [122.05, 37.2],
                上海: [121.48, 31.22],
                攀枝花: [101.718637, 26.582347],
                威海: [122.1, 37.5],
                承德: [117.93, 40.97],
                厦门: [118.1, 24.46],
                汕尾: [115.375279, 22.786211],
                潮州: [116.63, 23.68],
                丹东: [124.37, 40.13],
                太仓: [121.1, 31.45],
                曲靖: [103.79, 25.51],
                烟台: [121.39, 37.52],
                福州: [119.3, 26.08],
                瓦房店: [121.979603, 39.627114],
                即墨: [120.45, 36.38],
                抚顺: [123.97, 41.97],
                玉溪: [102.52, 24.35],
                张家口: [114.87, 40.82],
                阳泉: [113.57, 37.85],
                莱州: [119.942327, 37.177017],
                湖州: [120.1, 30.86],
                汕头: [116.69, 23.39],
                昆山: [120.95, 31.39],
                宁波: [121.56, 29.86],
                湛江: [110.359377, 21.270708],
                揭阳: [116.35, 23.55],
                荣成: [122.41, 37.16],
                连云港: [119.16, 34.59],
                葫芦岛: [120.836932, 40.711052],
                常熟: [120.74, 31.64],
                东莞: [113.75, 23.04],
                河源: [114.68, 23.73],
                淮安: [119.15, 33.5],
                泰州: [119.9, 32.49],
                南宁: [108.33, 22.84],
                营口: [122.18, 40.65],
                惠州: [114.4, 23.09],
                江阴: [120.26, 31.91],
                蓬莱: [120.75, 37.8],
                韶关: [113.62, 24.84],
                嘉峪关: [98.289152, 39.77313],
                广州: [113.23, 23.16],
                延安: [109.47, 36.6],
                太原: [112.53, 37.87],
                清远: [113.01, 23.7],
                中山: [113.38, 22.52],
                昆明: [102.73, 25.04],
                寿光: [118.73, 36.86],
                盘锦: [122.070714, 41.119997],
                长治: [113.08, 36.18],
                深圳: [114.07, 22.62],
                珠海: [113.52, 22.3],
                宿迁: [118.3, 33.96],
                咸阳: [108.72, 34.36],
                铜川: [109.11, 35.09],
                平度: [119.97, 36.77],
                佛山: [113.11, 23.05],
                海口: [110.35, 20.02],
                江门: [113.06, 22.61],
                章丘: [117.53, 36.72],
                肇庆: [112.44, 23.05],
                大连: [121.62, 38.92],
                临汾: [111.5, 36.08],
                吴江: [120.63, 31.16],
                石嘴山: [106.39, 39.04],
                沈阳: [123.38, 41.8],
                苏州: [120.62, 31.32],
                茂名: [110.88, 21.68],
                嘉兴: [120.76, 30.77],
                长春: [125.35, 43.88],
                胶州: [120.03336, 36.264622],
                银川: [106.27, 38.47],
                张家港: [120.555821, 31.875428],
                三门峡: [111.19, 34.76],
                锦州: [121.15, 41.13],
                南昌: [115.89, 28.68],
                柳州: [109.4, 24.33],
                三亚: [109.511909, 18.252847],
                自贡: [104.778442, 29.33903],
                吉林: [126.57, 43.87],
                阳江: [111.95, 21.85],
                泸州: [105.39, 28.91],
                西宁: [101.74, 36.56],
                宜宾: [104.56, 29.77],
                呼和浩特: [111.65, 40.82],
                成都: [104.06, 30.67],
                大同: [113.3, 40.12],
                镇江: [119.44, 32.2],
                桂林: [110.28, 25.29],
                张家界: [110.479191, 29.117096],
                宜兴: [119.82, 31.36],
                北海: [109.12, 21.49],
                西安: [108.95, 34.27],
                金坛: [119.56, 31.74],
                东营: [118.49, 37.46],
                牡丹江: [129.58, 44.6],
                遵义: [106.9, 27.7],
                绍兴: [120.58, 30.01],
                扬州: [119.42, 32.39],
                常州: [119.95, 31.79],
                潍坊: [119.1, 36.62],
                重庆: [106.54, 29.59],
                台州: [121.420757, 28.656386],
                南京: [118.78, 32.04],
                滨州: [118.03, 37.36],
                贵阳: [106.71, 26.57],
                无锡: [120.29, 31.59],
                本溪: [123.73, 41.3],
                克拉玛依: [84.77, 45.59],
                渭南: [109.5, 34.52],
                马鞍山: [118.48, 31.56],
                宝鸡: [107.15, 34.38],
                焦作: [113.21, 35.24],
                句容: [119.16, 31.95],
                北京: [116.46, 39.92],
                徐州: [117.2, 34.26],
                衡水: [115.72, 37.72],
                包头: [110, 40.58],
                绵阳: [104.73, 31.48],
                乌鲁木齐: [87.68, 43.77],
                枣庄: [117.57, 34.86],
                杭州: [120.19, 30.26],
                淄博: [118.05, 36.78],
                鞍山: [122.85, 41.12],
                溧阳: [119.48, 31.43],
                库尔勒: [86.06, 41.68],
                安阳: [114.35, 36.1],
                开封: [114.35, 34.79],
                济南: [117, 36.65],
                德阳: [104.37, 31.13],
                温州: [120.65, 28.01],
                九江: [115.97, 29.71],
                邯郸: [114.47, 36.6],
                临安: [119.72, 30.23],
                兰州: [103.73, 36.03],
                沧州: [116.83, 38.33],
                临沂: [118.35, 35.05],
                南充: [106.110698, 30.837793],
                天津: [117.2, 39.13],
                富阳: [119.95, 30.07],
                泰安: [117.13, 36.18],
                诸暨: [120.23, 29.71],
                郑州: [113.65, 34.76],
                哈尔滨: [126.63, 45.75],
                聊城: [115.97, 36.45],
                芜湖: [118.38, 31.33],
                唐山: [118.02, 39.63],
                平顶山: [113.29, 33.75],
                邢台: [114.48, 37.05],
                德州: [116.29, 37.45],
                济宁: [116.59, 35.38],
                荆州: [112.239741, 30.335165],
                宜昌: [111.3, 30.7],
                义乌: [120.06, 29.32],
                丽水: [119.92, 28.45],
                洛阳: [112.44, 34.7],
                秦皇岛: [119.57, 39.95],
                株洲: [113.16, 27.83],
                石家庄: [114.48, 38.03],
                莱芜: [117.67, 36.19],
                常德: [111.69, 29.05],
                保定: [115.48, 38.85],
                湘潭: [112.91, 27.87],
                金华: [119.64, 29.12],
                岳阳: [113.09, 29.37],
                长沙: [113, 28.21],
                衢州: [118.88, 28.97],
                廊坊: [116.7, 39.53],
                菏泽: [115.480656, 35.23375],
                合肥: [117.27, 31.86],
                武汉: [114.31, 30.52],
                大庆: [125.03, 46.58]
            };
            var data = that.map1;

            var convertData = function(data) {
                var res = [];
                for (var i = 0; i < data.length; i++) {
                    var geoCoord = geoCoordMap[data[i].name];
                    if (geoCoord) {
                        res.push({
                            name: data[i].name,
                            value: geoCoord.concat(data[i].value)
                        });
                    }
                }
                return res;
            };

            var convertedData = [
                convertData(data),
                convertData(
                    data
                        .sort(function(a, b) {
                            return b.value - a.value;
                        })
                        .slice(0, 6)
                )
            ];
            data.sort(function(a, b) {
                return a.value - b.value;
            });

            var selectedItems = [];
            var categoryData = [];
            var barData = [];
            //   var maxBar = 30;
            var sum = 0;
            var count = data.length;
            for (var i = 0; i < data.length; i++) {
                categoryData.push(data[i].name);
                barData.push(data[i].value);
                sum += data[i].value;
            }
            console.log(categoryData);
            console.log(sum + "   " + count);
            let myChart4 = this.$echarts.init(
                document.getElementById("myChart4")
            );
            // 绘制图表
            myChart4.setOption({
                backgroundColor: "#fff",
                animation: true,
                animationDuration: 1000,
                animationEasing: "cubicInOut",
                animationDurationUpdate: 1000,
                animationEasingUpdate: "cubicInOut",
                title: [
                    {
                        text: "全国主要城市 工作岗位分布",
                        subtext: "统计数据，仅供参考",
                        left: "center",
                        textStyle: {
                            color: "#000"
                        }
                    },
                    {
                        id: "statistic",
                        text: count
                            ? "平均: " + parseInt((sum / count).toFixed(4))+"（个）"
                            : "",
                        right: 120,
                        top: 40,
                        width: 100,
                        textStyle: {
                            color: "#000",
                            fontSize: 16
                        }
                    }
                ],
                geo: {
                    map: "china",
                    left: "10",
                    right: "35%",
                    center: [117.98561551896913, 31.205000490896193],
                    zoom: 1.0,
                    label: {
                        emphasis: {
                            show: false
                        }
                    },
                    roam: true,
                    itemStyle: {
                        normal: {
                            areaColor: "#47769C",
                            borderColor: "#111"
                        },
                        emphasis: {
                            areaColor: "#77A9CC"
                        }
                    }
                },
                tooltip: {
                    show: true,
                    trigger: "item",
                    formatter: function(params) {
                        console.log(JSON.stringify(params));
                        if (typeof params.value[2] == "undefined") {
                            return params.data.value;
                        } else {
                            return params.data.value[2];
                        }
                    }
                },
                grid: {
                    right: 40,
                    top: 100,
                    bottom: 40,
                    width: "30%"
                },
                xAxis: {
                    type: "value",
                    scale: true,
                    position: "top",
                    boundaryGap: false,
                    splitLine: {
                        show: false
                    },
                    axisLine: {
                        show: false
                    },
                    axisTick: {
                        show: false
                    },
                    axisLabel: {
                        margin: 2,
                        textStyle: {
                            color: "#000"
                        }
                    }
                },
                yAxis: {
                    type: "category",
                    //  name: 'TOP 20',
                    nameGap: 16,
                    axisLine: {
                        show: true,
                        lineStyle: {
                            color: "#000"
                        }
                    },
                    axisTick: {
                        show: false,
                        lineStyle: {
                            color: "#000"
                        }
                    },
                    axisLabel: {
                        interval: 0,
                        textStyle: {
                            color: "#000"
                        }
                    },
                    data: categoryData
                },
                series: [
                    {
                        // name: 'pm2.5',
                        type: "scatter",
                        coordinateSystem: "geo",
                        data: convertedData[0],
                        symbolSize: function(val) {
                            return Math.max(val[2] / 10, 8);
                        },
                        label: {
                            normal: {
                                formatter: "{b}",
                                position: "right",
                                show: false
                            },
                            emphasis: {
                                show: true
                            }
                        },
                        itemStyle: {
                            normal: {
                                color: "#ddb926",
                                position: "right",
                                show: true
                            }
                        }
                    },
                    {
                        //  name: 'Top 5',
                        type: "effectScatter",
                        coordinateSystem: "geo",
                        data: convertedData[0],
                        symbolSize: function(val) {
                            return Math.max(val[2] / 10, 8);
                        },
                        showEffectOn: "emphasis",
                        rippleEffect: {
                            brushType: "stroke"
                        },
                        hoverAnimation: true,
                        label: {
                            normal: {
                                formatter: "{b}",
                                position: "right",
                                show: true
                            }
                        },
                        itemStyle: {
                            normal: {
                                color: "#FFE071",
                                shadowBlur: 10,
                                shadowColor: "#333"
                            }
                        },
                        zlevel: 1
                    },
                    {
                        id: "bar",
                        zlevel: 2,
                        type: "bar",
                        symbol: "none",
                        itemStyle: {
                            normal: {
                                color: "#FFE071"
                            }
                        },

                        data: data
                    }
                ]
            });
            function renderBrushed(params) {
                var mainSeries = params.batch[0].selected[0];

                var selectedItems = [];
                var categoryData = [];
                var barData = [];
                var maxBar = 30;
                var sum = 0;
                var count = 0;

                for (var i = 0; i < mainSeries.dataIndex.length; i++) {
                    var rawIndex = mainSeries.dataIndex[i];
                    var dataItem = convertedData[0][rawIndex];
                    var pmValue = dataItem.value[2];

                    sum += pmValue;
                    count++;

                    selectedItems.push(dataItem);
                }

                selectedItems.sort(function(a, b) {
                    //   return b.value[2] - a.value[2];
                    return a.value - b.value;
                });

                for (
                    var i = 0;
                    i < Math.min(selectedItems.length, maxBar);
                    i++
                ) {
                    categoryData.push(selectedItems[i].name);
                    barData.push(selectedItems[i].value[2]);
                }

                this.setOption({
                    yAxis: {
                        data: categoryData
                    },
                    xAxis: {
                        axisLabel: {
                            show: !!count
                        }
                    },
                    title: {
                        id: "statistic",
                        text: count ? "平均: " + (sum / count).toFixed(4) : ""
                    },
                    series: {
                        id: "bar",
                        //        sort:'descending',
                        data: barData
                    }
                });
            }
            var echarts = require("echarts");
            require("echarts-wordcloud");
            // 基于准备好的dom，初始化echarts实例
            let myChart5 = this.$echarts.init(
                document.getElementById("myChart5")
            );

            var NWCNAME = that.WCNAME;
            console.log("wordcloud'sname= ", that.name);
            myChart5.setOption({
                title: {},
                tooltip: {},
                series: [
                    {
                        type: "wordCloud",
                        gridSize: 30,
                        sizeRange: [12, 50],
                        rotationRange: [0, 0],
                        shape: "circle",
                        textStyle: {
                            normal: {
                                color: function() {
                                    return (
                                        "rgb(" +
                                        [
                                            Math.round(Math.random() * 160),
                                            Math.round(Math.random() * 160),
                                            Math.round(Math.random() * 160)
                                        ].join(",") +
                                        ")"
                                    );
                                }
                            },
                            emphasis: {
                                shadowBlur: 10,
                                shadowColor: "#333"
                            }
                        },
                        data: NWCNAME
                    }
                ]
            });
        }
    }
};
</script>



<style scoped>
.container {
    height: 2000px;
    /* border: 5px solid red; */
}

.container ul :hover {
    background-color: #f0f0f0;
}

#myChart4 {
    margin-left: 18%;
    margin-top: 20px;
}
</style>

