
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
    <p>{{info.title}}</p>


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
        exist:true,
        // title:this.props.ctitle
        title:this.ctitle
      }

    }
  },
  props:{
    ctitle:{
      type:String,
      // require:true
    }

  },


  methods:{
    disable(){
      var temp=window.sessionStorage.token

      this.info.exist=false
      this.$axios({ //评分 把username,评分value,书名title传递到后端
        method:'post',
        url:'http://127.0.0.1:8000/api/rating/',
        data:{
          'value':this.info.value,
          'username':temp,
          'title':this.info.title

        }

      }).then(res=>
        console.log(res))
      .catch(error=>console.log(error))
    },


  }
}
</script>


