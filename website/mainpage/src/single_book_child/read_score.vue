
<style lang="less" scoped>
  .read_score span{
    /*float: right;*/
    margin-left: 10px;
    font-size: 16px;
  }

  .read_score{
    position: absolute;
    float: right;
  }
</style>
<template>
  <div class="read_score">
    <el-rate
      v-model="value"
      disabled
      show-score
      text-color="#ff9900"
      score-template="{value}">
    </el-rate>
  </div>

</template>

<script>
    import {getSingleBook_multdata} from '../network/single_book'

    export default {
        name: "read_score",
      data() {
        return {
          value: 3.7
        }
      },
      // request method page initial and get average score of this book

      created(){
        getSingleBook_multdata().then(result =>{
          //右侧输入获取的average_score
          this.value=result.data.xxx
        })
      },
    }
</script>


