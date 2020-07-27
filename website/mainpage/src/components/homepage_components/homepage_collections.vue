<template>
    <div class="collection">
        <div class="collection-head">
            <el-select v-model="value" placeholder="please select a collection"
                       @change="currentSel(value)">
                <el-option
                        v-for="item in options"
                        :key="item.label"
                        :value="item.value"
                >
                </el-option>
            </el-select>
        </div>

        <!-- get collections base on selection -->
        <div class="collection-body">
            <!-- 分割线，显示当前collection名字 -->
            <el-divider content-position="center" class="divider">{{value}}</el-divider>

            <!-- collection主体，显示 图 & 书名 -->
            <div class="wrap">
                <div class="content" v-for="item in books" :key="item.imageLink">
                    <img :src="item.imageLink" class="img" alt @click="jump_one_book(item)" />
                    <a>{{item.title}}</a>
                </div>
            </div>

            <!-- TODO: 更多书籍button，跳转到 my profile -->
        </div>
    </div>
</template>

<script>
    import {getCollectionmultdata} from '../../network/requests'

    export default {
        data() {
            return {
                books: [],       // current collection's books
                options: [],     // collections' content
                value: '',       // collection name
                // cur_key: 0,      // collection id
                collections: [], // result from api package
                item: '', // one book param

                // TODO: connect with backend, get all book images in this collections
                img_list: [
                    {
                        imageLink: require("../../img/test book image/harry.jpg"),
                        title: 'Harry Porter',
                        url: ''  // TODO: fill the url
                    },
                ],
            }
        },

        methods: {
            // check which collection is now selecting
            currentSel(selVal) {
                this.value = selVal;
                let obj = {}
                obj = this.options.find((item)=>{
                    return item.value === selVal;
                });
                this.getCollectionBooks(obj.key)
            },

            getCollectionNames(res) {
                const len = res.length
                let option
                for(let i = 0; i < len; i++) {
                    // 提取collections' name
                    option = {}
                    option["key"] = res[i].id
                    option["value"] = res[i].name
                    this.options.push(option)
                }
            },

            // get books from specific collection through collection id
            getCollectionBooks(col_id) {
                this.books = []  // refresh books' list
                // console.log("now select: " + col_id)

                let obj = {}
                obj = this.collections.find((item) => {
                    return item.id === col_id;
                });



                let book
                let len = obj.books.length
                for(let i = 0; i < len; i++) {
                    book = {}
                    book["id"] = obj.books[i].id
                    book["authors"] = obj.books[i].authors
                    book["title"] = obj.books[i].title
                    book["imageLink"] = obj.books[i].imageLink
                    book["ISBN"] = obj.books[i].ISBN
                    book["publisher"] = obj.books[i].publisher
                    book["publish_date"] = obj.books[i].publish_date
                    book["categories"] = obj.books[i].categories
                    // book["url"] = ''   // TODO: 跳转url
                    this.books.push(book)
                }
                console.log(book)
            },

            jump_one_book(value) {
                console.log(value)
                this.$router.push({
                    name: 'one_book',
                    query: {
                        // item:value
                        book_id: value.id,
                        authors: value.authors,
                        title: value.title,
                        ISBN: value.ISBN,
                        publisher: value.publisher,
                        imageLink: value.imageLink,
                        publisher_data:value.publish_date,
                        category:value.categories
                    }

                })
            },
        },

        mounted() {
            getCollectionmultdata().then(res=>{
                console.log(res)
                this.collections = res
                this.value = this.collections[0].name
                this.getCollectionNames(res)   // 把api返回的collection名字整理出来
                this.getCollectionBooks(this.collections[0].id) // default select first collection
            })
            .catch(error => {
                console.log(error)
            });
        }
    }


</script>

<style lang="less" scoped>
    .collection {
        background-color: aliceblue;
        border-left-style: solid;
        border-radius: 2px;
        border-color: bisque;
        margin: 0 auto;
        width: 100%;
        height: 1310px;
    }

    .collection-head {
        padding-top: 60px;
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
        height: 240px;
    }
</style>