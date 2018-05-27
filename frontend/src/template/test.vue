<template>
        <p>{{ newData }}</p>
</template>

<script>
import Data from "../libs/test.js";
export default {
    data: function() {
        return {
            newData: Data.customData()
        };
    },
    mounted() {
        alert("test   ");
        var st = this.newData;
        console.log("answer", st);
        var word = "工程师"
        var s = "\"[^"+word+"\",]*"+word+"[^\"]*\""
        var pat = new RegExp(s,"ig")
        var ans = st.match(pat)
        var len = ans.length
        for(var i=0; i<len; ++i) {
                console.log(ans[i].replace(/\"/ig, ""))
        }       
    }
};
</script>

<style scoped>

</style>