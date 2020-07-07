<style lang="less" scoped>

  *{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  .page{
    position: relative;
    width: 1400px;
    background-color: pink;
    margin: 0 auto;
  }

.header{
  position: absolute;
  width: 1400px;
  height: 200px;
  /*background-color: red;*/
  border: 1px solid red;




}
  .body{
    position: absolute;
    width: 960px;
    height: 1000px;
    /*background-color: green;*/
    border: 1px solid red;
    margin: 220px 220px;

  }
  .footer{
    margin-top: 1240px;
    position: absolute;
    width: 1400px;
    height: 200px;
    /*background-color: gray;*/
    border: 1px solid red;


  }
  .left_side{
    position: absolute;
    margin-top: 220px;
    height: 1000px;
    width: 200px;
    /*background-color: black;*/
    border: 1px solid red;

  }
  .right_side{
    position: absolute;
    margin-top: 220px;
    margin-left: 1200px;
    height: 1000px;
    width: 200px;
    /*background-color: purple;*/
    border: 1px solid red;


  }
  .body #detail{
    position: relative;
    padding-left: 20px;
    width: 100%;
    height: 370px;


    display: inline-block;
  }
  .body #detail span{
    padding: 4px 0 0 10px;

  }
  .body #book_image{

    position: absolute;
  margin-left: 10px;
    width: 230px;
    height: 300px;
    border-right: 1px solid;

  }
  .body #book_image img{
    width: 90%;
    height: 100%;
  }
  .body #detail #book_detail{
    position: absolute;
    padding-left: 260px;
    /*border-left: 1px solid gray;*/

  }
  .rating{
    position: relative;
  }
   .rating1{
    position: absolute;
     margin-left: 50px;

    width: 350px;

  }
  .read_rating{
    position: relative;


  }
  .read_score{
    height: 100px;

    position: absolute;
    margin: 10px 0 0 600px;
    border-left: 1px solid gray;

  }



</style>



<template>
  <div class="page">
    <div class="header">

    </div>


    <div class="body">

<!--      Book_detail-->
      <div id="detail">
        <h1>
          <span> Harry Potter</span>
        </h1>
        <div id="book_image"><img src="../img/single_book_child/ImageHandler.jpeg" alt="">
        </div>


          <div id="book_detail">
            <span>author:xxxxx</span><br>
            <span>publisher:xxxx</span><br>
            <span>publication date:xxxx</span><br>
            <span>category:xxxx</span><br>
          </div>
        <div class="read_rating">

          <read_score class="read_score"></read_score>

        </div>

    </div>
      <div class="rating">
        <rating class="rating1"></rating>
      </div>


    <div class="review1">
      <review1></review1>
    </div>






    </div>



    <div class="right_side"></div>
    <div class="left_side"></div>
    <div class="footer"></div>

  </div>
</template>

<script>
  import rating from '../single_book_child/rating'
  import review1 from '../single_book_child/review1'
  import read_score from '../single_book_child/read_score'
  export default {
    name: "single_book",
    components:{
      rating,
      review1,
      read_score,

    }
  }
</script>
