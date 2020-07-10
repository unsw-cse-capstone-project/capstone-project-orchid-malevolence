
<style lang="less" scoped>
  .block span{
    margin-left: 10px;
    font-size: 16px;
  }

  .score{
    position: absolute;
    float: right;
  }


</style>


<template>
  <div  class="block">
    <span class="demonstration"> my rating: {{info.value}}</span>
    <div v-if="info.exist===true" @click="disable()" style="width: 120px;">
      <el-rate
              v-model="info.value"
              text-color="#ff9900"
              score-template="{info.value}">
      </el-rate>
    </div>
    <div v-else>
      <el-rate
              v-model="info.value"
              disabled
              show-score
              text-color="#ff9900"
              score-template="{value}">
      </el-rate>
    </div>


  </div>

</template>

<script>
// import axios from 'axios'

export default {
  name: "rating",
  data() {
    return {
      info:{
        value: Number(""),
        exist:true
      }

    }
  },


  methods:{
    disable(){
      this.info.exist=false
      this.$axios({
        method:'post',
        url:'http://127.0.0.1:8000/api/rating/',
        data:this.info.value
      }).then(res=>
        console.log(res))
      .catch(error=>console.log(error))
    },


  }
}
</script>


