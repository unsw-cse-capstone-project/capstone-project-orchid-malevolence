<template>
    <div id="app">
        <div class="header">
            <Header></Header>
        </div>

        <div class="content">
            <!-- before login -->
            <Carousel v-show="token_log == null"></Carousel>
            <!--                    <Search></Search>-->
            <CardBook v-show="token_log == null"></CardBook>

            <div class="after-login">
                <el-row>
                    <el-col :span="6" v-show="token_log != null">
                        <div class="grid-content bg-purple">
                            <!-- left hand side: current goal -->
                            <Goal></Goal>
                        </div>
                    </el-col>

                    <el-col :span="18" v-show="token_log != null">
                        <div class="grid-content bg-purple">
                            <!-- right hand side: collections -->
                        </div>
                    </el-col>
                </el-row>
            </div>
        </div>

        <div class="footer">
            <Footer></Footer>
        </div>
    </div>
</template>

<script>
    import Header from '../components/homepage_components/header.vue'
    import Carousel from '../components/homepage_components/carousel.vue'
    import CardBook from '../components/homepage_components/mainpagebooks.vue'
    import Footer from '../components/homepage_components/footer.vue'
    import Goal from '../components/homepage_components/homepage_goal.vue'


    export default {
        data() {
          return {
              token_log: sessionStorage.getItem('token')
          }
        },
        components:{
            Header,
            Carousel,
            CardBook,
            Footer,
            Goal
        },
        name: 'App'
    }
</script>

<style scoped>
    html, body {
        height: 100%;
        margin: 0;
        padding: 0;
    }

    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        min-height: 100%;
        /*position: relative;*/
        display: flex;
        flex-direction: column;
    }

    .header {
        /*box-sizing: border-box;*/
        height: 60px;
    }

    .content {
        /*padding-bottom: 40px;*/
        /*padding-top: 40px;*/
        flex: 1;
        height: 100%;
    }

    .footer {
        width: 100%;
        height: 60px;
        bottom: 0;
        box-sizing: border-box;
        /*position: absolute;*/
    }

    .bg-purple {
        background: #d3dce6;
    }
    .grid-content {
        /*border-radius: 4px;*/
        min-height: 36px;
        height: 1310px;
    }
</style>