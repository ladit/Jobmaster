<template>
    <div class="container" click="click2">
        <div style="margin-top:40px;">
            <Input placeholder="输入相关岗位，如大数据、分析师等" style="width: 400px;margin-left:41%;font-size:18px" v-model="keyword" on-blur="bb" on-focus="get($event)" @input="get($event)" @keydown.down.prevent="selectDown" @keydown.up.prevent="selectUp">
            <Button slot="append" icon="ios-search" @click="btn"></Button>
            </Input>
            <ul style="width: 358.5px;margin-left:41%;font-size:14px;position:absolute;list-style:none; border:1px solid #E8E8E8;">
                <li style="padding-left:10px; padding:3px 8px;" class="text-center" v-for="(value,index) in myData">
                    <span @click="jump" class="text-success textprimary" :class="{gray:index==now}">{{value}}</span>
                </li>
            </ul>
        </div>

        <div style="margin-left:100px;margin-top:30px;">
            <p style="font-size:20px;font-weight:bold;float:left">岗位名称：</p>
            <p style="font-size:20px;;float:left">{{name}}</p>
        </div>
        <br>

        <div style="margin-left:100px;margin-top:30px;">
            <p style="font-size:20px;font-weight:bold;float:left">最低工作经历要求：</p>
            <p style="font-size:20px;;float:left">{{year}}</p>
        </div>
        <br>

        <div style="margin-left:100px;margin-top:30px;">
            <p style="font-size:20px;font-weight:bold">岗位描述</p>
            <div id="myChart5" :style="{margin:'0 auto',width: '600px', height: '400px'}"></div>
        </div>

        <div style="margin-left:100px;float:left">
            <p style="font-size:20px;font-weight:bold">岗位画像</p>
            <div id="myChart1" :style="{float: 'left',width: '460px', height: '460px'}"></div>
            <div id="myChart2" :style="{float: 'left',width: '460px', height: '460px'}"></div>
            <div id="myChart3" :style="{float: 'left',width: '460px', height: '460px'}"></div>
        </div>

        <div style="margin-left:100px;margin-top:50px;float:left">
            <p style="font-size:20px;font-weight:bold">工作地分布</p>
            <div id="myChart4" :style="{width: '1000px', height: '800px'}"></div>
        </div>

    </div>

</template>



<script src="echarts.min.js"></script>
<script type="text/javascript" src="echarts.min.js"></script>  
<script type="text/javascript" src="china.js"></script> 
<script src="echarts-wordcloud.min.js"></script>


<script>
import axios from "axios";
import Data from "../libs/test.js";
export default {
    data() {
        return {
            value1: "",
            newData: Data.customData(),
            keyword: "",
            now: -1,
            myData: [],
            name: "",
            year: ""
        };
    },
    mounted() {
        this.drawLine();
    },
    methods: {
        btn: function() {
            this.name = this.keyword;
            const that = this;
            axios
                .get(
                    "http://119.29.189.122/api/job_portrait?job_show_name="+that.name
                )   
                .then(function(res) {
                    console.log(res);
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
            console.log(ans.length);
            var len = 0;
            len = ans.length;

            for (var i = 0; i < Math.min(6, len); ++i) {
                console.log(ans[i].replace(/\"/gi, ""));
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
            let myChart1 = this.$echarts.init(
                document.getElementById("myChart1")
            );
            // 绘制图表
            var data = [
                {
                    value: 3661,
                    name: "<10w"
                },
                {
                    value: 5713,
                    name: "10w-50w"
                },
                {
                    value: 9938,
                    name: "50w-100w"
                },
                {
                    value: 17623,
                    name: "100w-500w"
                },
                {
                    value: 3299,
                    name: ">500w"
                }
            ];
            myChart1.setOption({
                backgroundColor: "#fff",
                title: {
                    text: "学历要求",
                    subtext: "2016年",
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
                    data: ["<10w", "10w-50w", "50w-100w", "100w-500w", ">500w"]
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
                        data: data
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
                        data: data
                    }
                ]
            });
            let myChart2 = this.$echarts.init(
                document.getElementById("myChart2")
            );
            // 绘制图表
            myChart2.setOption({
                backgroundColor: "#fff",
                title: {
                    text: "工资分布",
                    subtext: "2016年",
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
                    data: ["<10w", "10w-50w", "50w-100w", "100w-500w", ">500w"]
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
                        data: data
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
                        data: data
                    }
                ]
            });
            let myChart3 = this.$echarts.init(
                document.getElementById("myChart3")
            );
            // 绘制图表
            myChart3.setOption({
                backgroundColor: "#fff",
                title: {
                    text: "公司规模",
                    subtext: "2016年",
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
                    data: ["<10w", "10w-50w", "50w-100w", "100w-500w", ">500w"]
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
                        data: data
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
                        data: data
                    }
                ]
            });
            var geoCoordMap = {
                北京: [116.46, 39.92],
                南京: [118.78, 32.04],
                吉林: [126.57, 43.87],
                上海: [121.48, 31.22],
                成都: [104.06, 30.67],
                哈尔滨: [126.63, 45.75],
                沈阳: [123.38, 41.8],
                // "合肥":[117.27,31.86],
                武汉: [114.31, 30.52],
                石家庄: [114.48, 38.03],
                天津: [117.2, 39.13],
                太原: [112.53, 37.87],
                西安: [108.95, 34.27],
                南宁: [108.33, 22.84],
                南昌: [115.89, 28.68],
                济南: [117, 36.65]
            };

            var data = [
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
            ];
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
                        text: "全国主要城市 业务量",
                        subtext: "内部数据请勿外传",
                        left: "center",
                        textStyle: {
                            color: "#000"
                        }
                    },
                    {
                        id: "statistic",
                        text: count
                            ? "平均: " + parseInt((sum / count).toFixed(4))
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
                    trigger: "item"
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
            myChart5.setOption({
                title: {},
                tooltip: {},
                series: [
                    {
                        type: "wordCloud",
                        gridSize: 20,
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
                        data: [
                            {
                                name: "Sam S Club",
                                value: 10000,
                                textStyle: {
                                    normal: {
                                        color: "black"
                                    },
                                    emphasis: {
                                        color: "red"
                                    }
                                }
                            },
                            {
                                name: "Macys",
                                value: 6181
                            },
                            {
                                name: "Amy Schumer",
                                value: 4386
                            },
                            {
                                name: "Jurassic World",
                                value: 4055
                            },
                            {
                                name: "Charter Communications",
                                value: 2467
                            },
                            {
                                name: "Chick Fil A",
                                value: 2244
                            },
                            {
                                name: "Planet Fitness",
                                value: 1898
                            },
                            {
                                name: "Pitch Perfect",
                                value: 1484
                            },
                            {
                                name: "Express",
                                value: 1112
                            },
                            {
                                name: "Home",
                                value: 965
                            },
                            {
                                name: "Johnny Depp",
                                value: 847
                            },
                            {
                                name: "Lena Dunham",
                                value: 582
                            },
                            {
                                name: "Lewis Hamilton",
                                value: 555
                            },
                            {
                                name: "KXAN",
                                value: 550
                            },
                            {
                                name: "Mary Ellen Mark",
                                value: 462
                            },
                            {
                                name: "Farrah Abraham",
                                value: 366
                            },
                            {
                                name: "Rita Ora",
                                value: 360
                            },
                            {
                                name: "Serena Williams",
                                value: 282
                            },
                            {
                                name: "NCAA baseball tournament",
                                value: 273
                            },
                            {
                                name: "Point Break",
                                value: 265
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

