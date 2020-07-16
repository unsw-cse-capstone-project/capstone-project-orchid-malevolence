<template>
    <div class="collection">
        <div class="collection-head">
            <el-select v-model="name" placeholder="please select a collection" @change="currentSel">
                <el-option
                        v-for="item in options"
                        :key="item.label"
                        :label="item.label"
                        :value="item.value"
                >
                </el-option>
            </el-select>
        </div>

        <div class="collection-body">
            <el-divider content-position="center" class="divider">{{cur_collection}}</el-divider>

            <div class="wrap">
                <div class="content" v-for="item in img_list" :key="item.img_name">
                    <img :src="item.img_name" class="img" alt/>
                    <a href="item.url">{{item.title}}</a>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                // TODO: connect with backend, get all collections
                options: [{
                   value: 'Collection 1',
                   label: 'collection1'
                }, {
                   value: 'Collection 2',
                   label: 'collection2'
                }],
                value: '',
                cur_collection: '',

                // TODO: connect with backend, get all book images in this collections
                img_list: [
                    {
                        img_name: require("../../img/test book image/harry.jpg"),
                        title: 'Harry Porter',
                        url: ''  // TODO: fill the url
                    },
                    {
                        img_name: require("../../img/test book image/harry.jpg"),
                        title: 'Harry Porter',
                        url: ''  // TODO: fill the url
                    },
                    {
                        img_name: require("../../img/test book image/harry.jpg"),
                        title: 'Harry Porter',
                        url: ''  // TODO: fill the url
                    },
                    {
                        img_name: require("../../img/test book image/harry.jpg"),
                        title: 'Harry Porter',
                        url: ''  // TODO: fill the url
                    },
                ]
            }
        },

        methods: {
            currentSel(selVal) {
                this.cur_collection = selVal;
                // this.dialogVisible = true;
                console.log(selVal);
                // console.log(this.options[0].label);
            }
        }
    }


</script>

<style lang="less" scoped>
    .collection {
        background-color: salmon;
        margin: 0 auto;
        width: 100%;
        height: 1000px;
    }

    .collection-head {
        margin-top: 60px;
        margin-right: 50px;
        text-align: right;
    }

    .collection-body {
        /*padding-left: 10px;*/
    }

    .wrap {
        margin-top: 30px;
        display: grid;
        grid-template-columns: repeat(4, 1fr);
    }

    .divider {

    }

    .content {
        margin: 10px 30px 30px 30px;
        width: 180px;
    }

    .img {
        width: 180px;
    }
</style>