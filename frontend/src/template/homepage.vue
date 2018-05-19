<template>
    <div class="container">
        <div class="bmg-cont">
            <h2>P O L E</h2>
            <h3>Scrapy-Redis分布式爬虫+</h3>
            <h3>Doc2Vec模型和K-means聚类算法+</h3>
            <h3>随机森林算法</h3>
        </div>
        <Carousel :autoplay="true" v-model="value2" :autoplay-speed="4000" loop style="width:100%;height:666px;margin-top:60px;">
            <CarouselItem>
                <img src="../images/5.jpg" class="bmg"></img>
            </CarouselItem>

            <CarouselItem>
                <img src="../images/1.jpg" class="bmg"></img>
            </CarouselItem>
            <CarouselItem>
                <img src="../images/2.jpg" class="bmg"></img>
            </CarouselItem>

        </Carousel>
    </div>
</template>


<script>
export default {
    data() {
        return {
            value2: 0
        };
    }
};
</script>

<style>
.bmg {
    width: 100%;
    height: 666px;
    position: relative;
}
.bmg-cont {
    position: absolute;
    top: 300px;
    left: 580px;
    height: 200px;
    width: auto;
    z-index: 500;
    text-align: center;
}

.bmg-cont h2 {
    color: white;
    font-size: 46px;
}

.bmg-cont h3 {
    color: white;
    font-size: 24px;
    font-weight: lighter;
}

/* .container p {
    position: absolute;
    top:200px;
    left: 200px;
    font-size: 20px;
} */
</style>

