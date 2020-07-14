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

    <textarea class='text_area' :disabled="isAble" v-model.lazy="content" placeholder="want do u want to say"></textarea>
    <el-row >
      <el-button class='button' :disabled="isAble" @click="add" size="small"><span style="width:70px; height: 30px; display: inline-block; font-size: 15px; text-align: center">commit</span></el-button>
    </el-row>



      <ul class='list-group'>
        <li class='list-group-item' style="position: relative" v-for="item in items" :key="item.id">

          <span class="badge" style="margin-left: -15px;  font-size: 15px; border: 1px solid" >{{item.username}}:</span>
          <span class="more" style="display:block;overflow-wrap:break-word;">{{item.content}}</span>
          <img @click="changeNumber" style="display:inline-block ; position: absolute; right: 30px; top: 10px; width: 20px;height: 20px; text-align: center" :src="imgUrl" alt="">
          <span class="number" style="display:inline-block; position:absolute; right:10px; top:10px">{{number}}</span>


        </li>
      </ul>


  </div>
</template>

<script>
import {getSingleBookmultdata} from '../../network/single_book'

export default {
  name:"review1",
  data () {
    return {
      items:[],
      username:'',
      number:Number(""),
      content:'',
      flag:true,
      imgUrl:require('../../img/single_book_child/agree.png'),
      isAble:false,
      title:this.ctitle


    }
  },
  props:{
    ctitle:{
      type:String
    }
  },
  // 获取该书所有的评论
  created(){

    getSingleBookmultdata().then(result =>{
      this.items.push({

        // content:result.xxxx,//从后端获取该书的所有评论
        username:result.xxx,//从后端获取该书每条评论对应的用户名
      })


    })

  },
  methods: {

    changeNumber(){
      if(this.flag===true){
        this.number++
        this.flag=false
        this.imgUrl=require('../../img/single_book_child/agree_true.png')

      }else{
        this.number--
        this.flag=true
        this.imgUrl=require('../../img/single_book_child/agree.png')
      }

    },
//点击评论屏幕上会出现一条评论，并同时向后端传送评论数据，包括username，review，点赞的number number只传1 或0
    add(){
      var temp=window.sessionStorage.token
      this.items.push({
        content:this.content,
        username:temp,//need to change to the username

      })


      this.isAble=true
      this.content=''
      if (this.flag===false){
        this.$axios({

          method:'post',
          url:'http://127.0.0.1:8000/api/review/',
          data:{
            'username':this.username,
            'content':this.content,
            'number':1,
            'title':this.title

          }

        }).then(res=>{
          console.log(res)
        })
                .catch(error=>{
                  console.log(error)
                })


      }else{
        this.$axios({

          method:'post',
          url:'http://127.0.0.1:8000/api/review/',
          data:{
            'username':this.username,
            'content':this.content,
            'number':0,
            'title':this.title

          }

        }).then(res=>{
          console.log(res)
        })
                .catch(error=>{
                  console.log(error)
                })
      }


    },

  },
  computed:{

  }


}
</script>


