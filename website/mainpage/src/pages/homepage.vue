<template>
    <div id="app">
        <el-row>
            <el-col :span="24">
                <div class="grid-content bg-purple-light">
<!--                    <router-view/>-->
                    <Header></Header>
                    <Carousel></Carousel>
                    <Search></Search>
                    <CardBook></CardBook>
                    <Footer></Footer>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import Header from '../components/header.vue'
    import Carousel from '../components/carousel.vue'
    import Search from '../components/search.vue'
    import CardBook from '../components/mainpagebooks.vue'
    import Footer from '../components/footer.vue'

    export default {
        components:{
            Header, Carousel, Search, CardBook, Footer
        },
        name: 'App'
    }
</script>

<style>
    html, body {
        height: 100%;
    }

    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        display: flex;
        flex-direction: column;
        min-height: 100%;
    }

    .el-row {
        margin-bottom: 20px;
    }

    .el-row:last-child {
        margin-bottom:  0;
    }

    .el-col {
        border-radius: 4px;
    }
    .bg-purple-dark {
        background: #99a9bf;
    }
    .bg-purple {
        background: #d3dce6;
    }
    .bg-purple-light {
        background: #e5e9f2;
    }
    .grid-content {
        border-radius: 4px;
        min-height: 36px;
    }
    .row-bg {
        padding: 10px 0;
        background-color: #f9fafc;
    }
</style>