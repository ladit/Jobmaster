<template>
  <div class="container">

    <div style="margin-left:20.4%;margin-top:40px;">
      <textarea placeholder="自我描述……" name="" id="" cols="111" rows="4" style="font-size:16px;border:4px bolid black"></textarea>
    </div>
    <br>

    <div class="input" style="">
      <Select v-model="model2" style="width:100px;margin-left:20%" placeholder="选择学历">
        <Option v-for="item in cityList" :value="item.value" :key="item.value">{{ item.label }}</Option>
      </Select>
      <Select v-model="model3" style="width:150px" placeholder="选择专业">
        <Option v-for="item in cityList" :value="item.value" :key="item.value">{{ item.label }}</Option>
      </Select>
      <Select v-model="model4" style="width:150px" placeholder="选择学校">
        <Option v-for="item in cityList" :value="item.value" :key="item.value">{{ item.label }}</Option>
      </Select>
      <Select v-model="model4" style="width:150px" placeholder="选择求职地">
        <Option v-for="item in cityList" :value="item.value" :key="item.value">{{ item.label }}</Option>
      </Select>
      <Select v-model="model4" style="width:200px" placeholder="选择岗位名称">
        <Option v-for="item in cityList" :value="item.value" :key="item.value">{{ item.label }}</Option>
      </Select>
      <Select v-model="model4" style="width:150px" placeholder="选择工作年限">
        <Option v-for="item in cityList" :value="item.value" :key="item.value">{{ item.label }}</Option>
      </Select>
      <Button style="margin-left:20px" type="info" icon="ios-search">匹配查询</Button>
    </div>

    <div style="margin-left:100px;margin-top:40px;">
      <p style="font-size:20px;font-weight:bold;float:left">XXX岗位待遇水平：</p>
      <p style="font-size:20px;;float:left">5000-12000</p>
    </div>

    <br>

    <div style="margin-left:100px;margin-top:30px;">
      <p style="font-size:20px;font-weight:bold">求职者画像</p>
      <div id="myChart1" :style="{margin:'0 auto',width: '600px', height: '500px'}"></div>
    </div>

    <div style="margin-left:100px;margin-top:-50px;">
      <p style="font-size:20px;font-weight:bold">匹配企业</p>
      <br>

      <div class="container-detailed">
        <div class="hover-hidden1">

          <div class="box-item">
            <br>
            <p style="font-size:22px;font-weight:bold;text-align:center;">ALIBABA</p>
            <div class="content">
              <p>工资：7000-15500</p>
              <p>福利：无限是假的回</p>
              <p>公司规模：7000-15500</p>
              <br>
              <span>匹配概率：50%</span>
              <br>
            </div>
          </div>

        </div>

        <div class="hover-show1">
          点击查看详情
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
export default {
    data() {
        return {
            value13: "",
            cityList: [
                {
                    value: "New York",
                    label: "New York"
                },
                {
                    value: "London",
                    label: "London"
                },
                {
                    value: "Sydney",
                    label: "Sydney"
                },
                {
                    value: "Ottawa",
                    label: "Ottawa"
                },
                {
                    value: "Paris",
                    label: "Paris"
                },
                {
                    value: "Canberra",
                    label: "Canberra"
                }
            ],
            model2: "",
            model3: "",
            model4: ""
        };
    },
    mounted() {
        this.drawLine();
    },
    methods: {
        drawLine() {
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
                        { name: "工资", max: 6500 },
                        { name: "学历", max: 16000 },
                        { name: "工作经验", max: 30000 }
                    ]
                },
                series: [
                    {
                        name: "预算 vs 开销（Budget vs spending）",
                        type: "radar",
                        // areaStyle: {normal: {}},
                        data: [
                            {
                                value: [4300, 10000, 28000],
                                name: "个人水平"
                            },
                            {
                                value: [5000, 14000, 28000],
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
    height: 1500px;
    /* border: 5px solid red; */
}

.layout {
    border: 1px solid #d7dde4;
    background: #f5f7f9;
    position: relative;
    border-radius: 4px;
    overflow: hidden;
}
.box-item {
    width: 200px;
    height: 240px;
    /* background-color: #fff0f5; */
    background-color: #c1ffc1;
}

.content p {
    font-size: 14px;
    padding-top: 6px;
    padding-left: 18px;
    padding-right: 18px;
    color: #828282;
    line-height: 20px;
}

.content span {
    margin-left: 44px;
    color: #b5b5b5;
    font-size: 16px;
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
    position: absolute; /*注意这两个盒子要设置为绝对定位*/
    /* width: 400px;
  text-align: center; */
    /*为鼠标移入时隐藏的那个盒子的显示绑定动画*/

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
</style>

