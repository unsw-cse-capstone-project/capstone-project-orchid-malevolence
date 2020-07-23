
<style lang="less" scoped>

  .read_score{
    position: absolute;
    float: right;


  }
  span{
    display: block;
    font-size: 12px;
    margin: 10px 0;
  }
</style>
<template>
  <div class="read_score">
    <span style="font-size: 18px">Website average rating</span>
    <el-rate
            v-model="average"
            disabled
            show-score
            text-color="#ff9900"
            score-template="{value}">
    </el-rate>
    <span>{{res.TotalCount}} people have read this book</span>
    <!--    <span>{{res}}{{value}}</span>-->
  </div>

</template>

<script>
import brothers_talk from '../../network/brothers_talk'

// import {getSingleBookmultdata} from '../../network/single_book'

export default {
  name: "read_score",
  data () {
    return {
      token_log: localStorage.getItem('token'),
      average: 0,
      number: Number(0),
      book_id: String,
      value: 0,
      TotalCount:''


    }
  },
  props: {
    res: Object
  },
  // request method page initial and get average score of this book
  updated () {

    this.average = this.res.averageScore
    this.book_id = this.res.book_id
    console.log(this.book_id + " aaaa")
    brothers_talk.$on('score',function (val) {
      this.value=val

    })


  },



}


</script>


