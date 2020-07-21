<style scoped>
  span{
    margin-left: 10px;
    font-size: 16px;
  }

</style>

<template>
  <div class="block" >
    <span class="demonstration">My rating:</span>
    <div v-if="exist===true" @click="disable()">
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

    <!--    {{bookID}}-->
  </div>
</template>

<script>
import {postrating} from "../../network/single_book"
export default {
  name: 'rate',
  data() {
    return {
      exist: true,
      token_log: localStorage.getItem('token'),
      value: 0,
      colors: ['#99A9BF', '#F7BA2A', '#FF9900']  }
  },
  props: {
    bookID:String
  },
  created () {

  },
  methods:{
    disable(){
      console.log(this.bookID)
      let postvalue={
        "rating_info":{
          "book":this.bookID,
          "rating":this.value
        }
      }

      postrating(postvalue).then(res=>{
        console.log(res)
      })
      console.log(this.bookID)
      this.$nextTick(()=>{
        this.$emit('updateData',this.bookID)
      })
      this.exist=false


    },






  },

}
</script>

