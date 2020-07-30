
<template>
  <div>
    <span class="demonstration">Rating and commit</span>
    <div @click="checkLogin()">
      <div v-if="exist===true" @click="disable() ">
        <el-rate
                v-model="value"
                show-score
                score-template="{value}"
                :colors="colors">
        </el-rate>

      </div>
      <div v-else>
        <el-rate
                v-model="value"
                disabled
                show-score
                text-color="#ff9900"
                score-template="{value}">
        </el-rate>

      </div>
    </div>



    <el-drawer

            title="I am title"
            @close="afterclose"

            :visible.sync="drawer"
            :with-header="false">
      <h3 class="margin_class" style="display: block">Rating and commit</h3>
      <div class="margin_class" v-if="exist===true"  @click="disable()">
        <el-rate
                v-model="value"
                show-score
                score-template="{value}"
                :colors="colors">
        </el-rate>

      </div>
      <div class="margin_class" v-else>
        <el-rate

                v-model="value"
                disabled
                show-score
                text-color="#ff9900"
                score-template="{value}">
        </el-rate>

      </div>
      <p class="line"></p>

      <el-input class="margin_class input_content"
              type="textarea"
              :autosize="{ minRows: 7, maxRows: 10}"
              placeholder="Commit this book"
              v-model="textarea2">
      </el-input>
      <el-button @click="submite_review" class="margin_class" style="float: right" type="primary" round>submit</el-button>
      <el-button @click="Close_drawer" class="margin_class" style="float: right" type="primary" round>cancle</el-button>

    </el-drawer>

  </div>

</template>

<script>
import {getSingleBookmultdata,postrating,postReview} from "../../network/requests"
export default {
  name: 'rate',
  data () {
    return {
      token_log: localStorage.getItem('token'),

      // wrapperClosable:true,
      drawer: false,
      exist: true,
      textarea1: '',
      textarea2: '',
      username: localStorage.getItem('username'),
      value: 0,
      colors: ['#99A9BF', '#F7BA2A', '#FF9900']
    }
  },
  props: {
    bookID: String //the arguments bookID received from father page one_book page
  },
  computed:{

  },


  methods: {
    checkLogin(){
      if(this.token_log){
      this.drawer = true

    }
    },

    submite_review () {
      if(this.token_log){
        let post_review = {
          "book_id": this.bookID,
          "review": {
            "content": this.textarea2
          }
        }
        postReview(post_review).then(res => {
          console.log(res)
        }).catch(res => {
          console.log(res)
        })
        let get_book_value = {
          "book_id": this.bookID,

        }
        getSingleBookmultdata(get_book_value).then(res => {
          console.log(res)

        }).catch(res => {
          console.log(res)
        })
        this.drawer=false
        location.reload()
      }


    },
    Close_drawer(){
      this.drawer=false
    },


    afterclose () {
      this.drawer = false

    },
    disable () {
      if(this.token_log){
        // console.log(this.bookID)
        let postvalue = {
          "rating_info": {
            "book": this.bookID,
            "rating": this.value
          }
        }

        postrating(postvalue).then(res => {
          console.log(res)
        })
        this.exist = false

      }else{
        this.$message({message: 'please login', showClose: true,})
        return false
      }

    },


  }
}
</script>
<style lang="less" scoped>
  span{
    /*margin-left: 10px;*/
    font-size: 16px;
  }
  .margin_class{
    margin: 10px 10px;
  }
  .line{
    border: 1px solid gray;
    width: 95%;
    margin: auto;
  }
  .input_content{
    width: 95%;

    margin-top: 20px;
  }
  .inner_usernamne{
    display: block;
  }



</style>

