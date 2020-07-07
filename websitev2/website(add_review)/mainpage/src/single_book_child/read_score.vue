
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

    export default {
        name: "read_score",
      data() {
        return {
          value: 3.7
        }
      }
    }
</script>


