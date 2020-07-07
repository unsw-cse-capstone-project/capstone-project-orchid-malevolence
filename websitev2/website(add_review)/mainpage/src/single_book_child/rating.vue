
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
  <div class="block">
    <span class="demonstration"> my rating: {{change_soce}}</span>

    <el-rate style="width: 120px;" v-model.number="value1"></el-rate>
    <div class="score"></div>
  </div>
</template>

<script>
  export default {
    name: "rating",
    data() {
      return {
        value1: Number(""),
        value2: "",
        colors: ['#99A9BF', '#F7BA2A', '#FF9900']
      }
    },
    computed:{
      change_soce:function () {
        return this.value1

      }
    }
  }
</script>


