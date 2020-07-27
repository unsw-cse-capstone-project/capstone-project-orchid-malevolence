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
  height: 65px;
  /*background-color: red;*/
  border: 1px solid red;




}
  .body{
    position: absolute;
    width: 960px;
    height: 1000px;
    /*background-color: green;*/
    border: 1px solid red;
    margin: 100px 220px;

  }
  .footer{
    margin-top: 1150px;
    position: absolute;
    width: 1400px;
    height: 200px;
    /*background-color: gray;*/
    border: 1px solid red;


  }
  .left_side{
    position: absolute;
    margin-top: 100px;
    height: 1000px;
    width: 200px;
    /*background-color: black;*/
    border: 1px solid red;

  }
  .right_side{
    position: absolute;
    margin-top: 100px;
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
     margin-left:  100px;
     /*display: inline-block;*/

    width: 350px;

  }
  .read_rating{
    position: relative;


  }
  .read_score{
    height: 100px;

    position: absolute;
    margin: 10px 0 0 700px;

    border-left: 1px solid gray;

  }
  .add_collection{
    position: absolute;


    /*display: inline-block;*/


  }
  div.popContainer{
    position: fixed;
    z-index: 33;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0,0,0,0.3);
  }



</style>



<template>
  <div class="page">
    <div class="header">
      <Header>
        1
      </Header>


    </div>


    <div class="body">

<!--      Book_detail-->
      <div id="detail">
        <h1>
          <span>{{result.title}}</span>
        </h1>
        <div id="book_image"><img src="../img/single_book_child/ImageHandler.jpeg" alt="">
        </div>


          <div id="book_detail">
            <span>author:{{result.author}}</span><br>
            <span>publisher:{{result.publisher}}</span><br>
            <span>publication date:{{result.publication_date}}</span><br>
            <span>category:{{result.category}}</span><br>
            <span>summary:{{result.summary}}</span><br>

          </div>
        <div class="read_rating">
          <read_score class="read_score"></read_score>
        </div>
    </div>

      <div class="rating">
        <rating :ctitle="result.title" class="rating1"></rating>
        <add_collection @clickshow="child_add_click" @closeshow="child_close_click" class="add_collection"></add_collection>

      </div>
      <div class='popContainer' v-show="isShow"></div>
<!--      <div class="add_collection">-->
<!--      </div>-->



      <div class="review1">
        <review1 :ctitle="result.title"></review1>
      </div>






      <div>
        <p>{{this.$route.params.id}}</p>
      </div>



    </div>
    <div class="right_side"></div>
    <div class="left_side"></div>
    <div class="footer"></div>

  </div>

</template>

<script>
  import Header from '../components/homepage_components/header'
  import rating from '../components/single_book_components/rating'
  import review1 from '../components/single_book_components/review1'
  import read_score from '../components/single_book_components/read_score'
  import add_collection from '../components/single_book_components/add_collection'
  import {getSingleBookmultdata} from '../network/requests'

  export default {

    name: "single_book",
    data(){
      return{
        isShow:false,
        result:{
          title:'Harry Potter',
          author:'xx',
          publisher:'xx',
          publication_date:'xx',
          category:'xx',
          summary:'xxxxxxxxx'

        }

      }
    },
    components:{
      rating,
      review1,
      read_score,
      Header,
      add_collection

    },
    created(){
      getSingleBookmultdata().then(result =>{
        console.log(result)
        //右侧请输入你对应的的参数
        // this.result.author=result.data.xxx
        // this.result.publisher=result.data.xxx
        // this.result.publication_date=result.data.xxx
        // this.result.cate gory=result.data.xxx

      })
    },
    methods:{
      child_add_click(){
        this.isShow=true

      },
      child_close_click(){
        this.isShow=false
      }

    }
  }
</script>
