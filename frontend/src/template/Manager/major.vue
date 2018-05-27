<template>

    <div class="container">
        <div class="input" style="margin-top:80px;margin-left:41%">
            <Select v-model="model1" style="width:160px" placeholder="选择更新频率">
                <Option v-for="item in cityList" :value="item.value" :key="item.value">{{ item.label }}</Option>
            </Select>
            <TimePicker v-model="model2" format="HH:mm" placeholder="选择更新时间" style="width: 130px"></TimePicker>

        </div>
        <CheckboxGroup v-model="social" size="large" style="margin-top:30px;margin-left:26%">
            <Checkbox label="boss">
                <span>boss</span>
            </Checkbox>
            <Checkbox label="51job">
                <span>51job</span>
            </Checkbox>
            <Checkbox label="内推网">
                <span>内推网</span>
            </Checkbox>
            <Checkbox label="智联招聘">
                <span>智联招聘</span>
            </Checkbox>
            <Checkbox label="猎聘网">
                <span>猎聘网</span>
            </Checkbox>
            <Checkbox label="拉钩网">
                <span>拉钩网</span>
            </Checkbox>
            <Checkbox label="中国人才热线">
                <span>中国人才热线</span>
            </Checkbox>
            <Checkbox label="应届生求职网">
                <span>应届生求职网</span>
            </Checkbox>
            <Checkbox label="58同城">
                <span>58同城</span>
            </Checkbox>
            <Checkbox label="大街网">
                <span>大街网</span>
            </Checkbox>
        </CheckboxGroup>
        <div style="margin-top:30px;margin-left:45%">
            <Button disabled type="warning" icon="refresh" @click="chushi">初始化</Button>
            <Button class="bttn" type="success" style="margin-left:14px;" icon="arrow-right-b" @click="btn">启动</Button>
        </div>
        <div style="margin-top:30px;margin-left:60px;">
            <Table :loading="loading" highlight-row border ref="currentRowTable" :columns="columns3" :data="data1" style="width:1400px"></Table>
        </div>

    </div>

</template> 

<script>
export default {
    data() {
        return {
            loading: false,
            cnt: 4,
            cityList: [
                {
                    value: "每隔2天",
                    label: "每隔2天"
                },
                {
                    value: "每隔3天",
                    label: "每隔3天"
                },
                {
                    value: "每隔5天",
                    label: "每隔5天"
                },
                {
                    value: "每隔7天",
                    label: "每隔7天"
                },
                {
                    value: "永不自动更新",
                    label: "永不自动更新"
                }
            ],
            model1: "",
            model2: "",
            social: [],
            fruit: ["苹果"],
            columns3: [
                {
                    type: "index",
                    width: 60,
                    align: "center"
                },
                {
                    title: "开始时间",
                    key: "name",
                    width: 300,
                    align: "center"
                },
                {
                    title: "结束时间",
                    key: "age",
                    width: 300,
                    align: "center"
                },
                {
                    title: "爬取频率",
                    key: "rate",
                    align: "center"
                },
                {
                    title: "爬取时间",
                    key: "time",
                    align: "center"
                },
                {
                    title: "爬取网站",
                    key: "address",
                    align: "center"
                },
                {
                    title: "更新次数",
                    key: "count",
                    align: "center"
                }
            ],
            data1: [
                {
                    name: "2018/3/14 10:00",
                    age: "2018/3/16 21:06:03",
                    rate: "初始化",
                    time: "初始化",
                    count: "1",
                    address: "ALL"
                },
                {
                    name: "2018/3/17 13:00",
                    age: "2018/3/28 20:40:22",
                    rate: "每隔5天",
                    time: "13:00",
                    count: "2",
                    address: ["boss", "猎聘网", "拉钩网", "58同城", "大街网"]
                },
                {
                    name: "2018/3/28 15:00",
                    age: "2018/4/02 09:02:12",
                    rate: "每隔2天",
                    time: "15:00",
                    count: "3",
                    address: ["boss", "51job", "智联招聘", "拉钩网", "大街网"]
                },
                {
                    name: "2018/4/02 20:00",
                    age: "2018/4/18 15:42:47",
                    rate: "每隔3天",
                    time: "20:00",
                    count: "5",
                    address: [
                        "内推网",
                        "智联招聘",
                        "猎聘网",
                        "拉钩网",
                        "中国人才热线"
                    ]
                },
                {
                    name: "2018/4/19 08:00",
                    age: "2018/5/22 21:15:14",
                    rate: "每隔5天",
                    time: "08:00",
                    count: "6",
                    address: [
                        "51job",
                        "智联招聘",
                        "猎聘网",
                        "拉钩网",
                        "58同城",
                        "大街网"
                    ]
                }
            ]
        };
    },
    mounted() {
        //   console.log("tid = >" + this.$store.getters.getTid);
    },
    methods: {
        btn: function() {
            var that = this;
            // if(that.data1[that.cnt].name=="未开始")
            // {
            //     this.data1.splice(index,that.cnt);
            // }
            this.cnt++;
            var myDate = new Date();
            var date = myDate.toLocaleDateString(); //获取日期
            var mytime = myDate.toLocaleTimeString(); //获取时间
            var tmp = {
                name: "",
                age: "",
                rate: "",
                time: "",
                count: "",
                address: ""
            };
            if (myDate.getHours() > parseInt(this.model2.slice(0,2))) {
                var nextDate = new Date(myDate.getTime() + 24*60*60*1000)
                tmp.name = nextDate.toLocaleDateString() + " " + this.model2;
            } else {
                tmp.name = myDate.toLocaleDateString() + " " + this.model2;
            }
            tmp.age = "未完成";
            tmp.rate = this.model1;
            tmp.time = this.model2;
            tmp.address = this.social;
            tmp.count = 0;
            this.data1.push(tmp);

            var BTN = document.getElementById("bttn");
            BTN.type = "warning";
        }
    }
};
</script>

<style scoped>
.main {
    height: 600px;
    width: 100%;
    padding: 0;
    margin: 0;
    background: #fdfdfc;
}

.layout {
    border: 1px solid #d7dde4;
    background: #f2f2f3;
    height: 686px;
}

.layout-content {
    min-height: 200px;
    margin: 15px;
    overflow: hidden;
    background: #fff;
    border-radius: 4px;
}

.layout-content-main {
    padding: 25px 0;
}

.layout-copy {
    text-align: center;
    padding: 10px 0 20px;
    color: #9ea7b4;
}
</style>