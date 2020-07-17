<!-- TODO: Books位置调整 -->
<template>
    <el-row class="book_cards">
        <el-col :span="4" v-for="(o, index) in 5" :key="o" :offset="index > 0 ? 1 : 0">
            <el-card :body-style="{ padding: '0px' }">
                <img src="https://m.media-amazon.com/images/M/MV5BMjIyZGU4YzUtNDkzYi00ZDRhLTljYzctYTMxMDQ4M2E0Y2YxXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_SX667_CR0,0,667,999_AL_.jpg" class="image" alt/>
                <div style="padding: 14px;">
                    <span>Harry Porter</span>
                    <div class="bottom clearfix">
<!--                        <time class="time">{{ currentDate }}</time>-->
                      <router-link :to="{name:'single_book',query:{id:'23'}}">
                        <el-button type="text" class="button">More Details</el-button>
                      </router-link>
                    </div>
                </div>
            </el-card>
        </el-col>
    </el-row>
</template>

<script>
    export default {
        name: "mainpagebooks",
        data() {
            return {
                currentDate: new Date()
            };
        },
      methods:{



      }
    }
</script>

<style  lang="less" scoped>
    .book_cards {
        margin: 40px 20px 40px 20px;
    }

    .time {
        font-size: 13px;
        color: #999;
    }

    .bottom {
        margin-top: 13px;
        line-height: 12px;
    }

    .button {
        padding: 0;
        /*float: center;*/
    }

    .image {
        width: 100%;
        display: block;
    }

    /*.clearfix:before,*/
    /*.clearfix:after {*/
    /*    display: table;*/
    /*    content: "";*/
    /*}*/

    /*.clearfix:after {*/
    /*    clear: both*/
    /*}*/
</style>