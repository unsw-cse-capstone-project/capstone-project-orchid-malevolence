<style lang="less" scoped>
  *{
    margin: 0;
    padding: 0;

  }
  .box{
    margin: 150px 40px 0 40px;
    position: relative;
    height: 500px;
    /*background-color: pink;*/
  }
  .button{
    position: absolute;
    margin-left: 40px;

    /*float: right;*/
  }
  .text_area{
    width: 85%;

    margin: 0 40px 0 40px;
  }

  ul{
    margin: 50px 0 0 40px;
    width: 85%;
  }
  ul span{

  }

</style>

<template>
  <div class="box">

    <textarea class='text_area' v-model.lazy="content" placeholder="want do u want to say"></textarea>
    <el-row >
      <el-button class='button' @click="add" size="small"><span style="width:70px; height: 30px; display: inline-block; font-size: 15px; text-align: center">commit</span></el-button>
    </el-row>



      <ul class='list-group'>
        <li class='list-group-item' v-for="item in items" :key="item.id">

          <span class="badge" style="margin-left: -15px;  font-size: 15px; border: 1px solid" >{{item.username}}</span>
          : {{item.title}}
          <img @click="number+=1" style="display:inline-block ; position: relative; right: 40px;float: right; width: 20px;height: 20px; text-align: center" src="../img/single_book_child/agree.png" alt="">
          <span class="number" style="display:inline-block; position:relative; float: right">{{number}}</span>


        </li>
      </ul>





  </div>
</template>

<script>
export default {
  name:"review1",
  data () {
    return {
      items:[],
      username:'',
      number:0,
      content:'',

    }
  },
  methods: {

    add(){
      this.items.push({
        title:this.content,
        username:'Jack',

      })
      this.content='';
      this.username='';
    }
  }

}
</script>


