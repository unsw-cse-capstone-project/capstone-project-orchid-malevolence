
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
    <span> {{res.TotalCount }} people have read this book</span>

  </div>

</template>

<script>

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
      TotalCount:'',
      isShow:true



    }
  },
  props: {
    res: Object
  },
  watch:{
    average(newV,oldV) {
      this.average=newV
      console.log(oldV)


    }
  },
  // request method page initial and get average score of this book
  updated () {
    if(this.res.averageScore!==undefined){
      let average=this.res.averageScore
      let book_id=this.res.book_id
      this.average = average
      this.book_id = book_id
      // this.$forceUpdate()


        // this.$forceUpdate()

      // this.TotalCount=this.res.TotalCount
      console.log(this.book_id + " aaaa")
    }
    else{
      this.isShow=false
    }





  },



}


</script>


