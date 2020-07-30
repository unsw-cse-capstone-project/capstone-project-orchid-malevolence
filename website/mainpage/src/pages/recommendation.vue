<template>
	<div id="app1">
		<Header></Header>
		<el-row>
			<el-col :span="6">
				<div class="grid-content bg-purple">
					<div class="choose_collection">
						<p>Recommendation Style:</p>
						<el-select class="collections" v-model="value" placeholder="Choose style" @change="currentSel(value)">
							<el-option
									v-for="item in options"
									:key="item.value"
									:label="show_types(item.value)"
									:value="item.value"
							>
							</el-option>
						</el-select>
					</div>
				</div>
			</el-col>

			<el-col :span="18">
				<div class="collection-body">
					<!-- 分割线，显示当前collection名字 -->
					<el-divider content-position="center">{{show_types(value)}}</el-divider>

					<!-- collection主体，显示 图 & 书名 -->
					<div class="wrap">
						<div class="content" v-for="item in books" :key="item.imageLink">
							<el-popover
									placement="right"
									width="400"
									trigger="hover">
								<div>
									<b>{{item.title}}</b>
									<el-rate
											v-model="item.avg_rating"
											disabled
											show-score
											text-color="#ff9900"
											score-template="{value}">
									</el-rate>
									{{item.description}}
								</div>
								<!--                        <el-button slot="reference">hover 激活</el-button>-->
								<img :src="item.imageLink" class="img" alt slot="reference"/>
							</el-popover>
							<!--                    <img :src="item.imageLink" class="img" alt @click="jump_one_book(item)" />-->
							<!--                    <a>{{item.title}}</a>-->
							<el-button class="book-detail" @click="jump_one_book(item)">More Details</el-button>
						</div>
					</div>
				</div>
			</el-col>
		</el-row>
	</div>
</template>

<script>
import {getAccount, getRecommend} from "@/network/requests";
import Header from "@/components/homepage_components/header";

export default {
	name: "recommendation",
	data() {
		return {
			myID: '',
			recommendList: [],
			books: [],			// current collection's books
			options: [],		// collections' content
			value: '',       	// collection name
			item: '', 		 	// one book param
		};
	},

	components:{
		Header,
	},

	methods: {
		show_types(type) {
			const rec_type = {"rating_rec": "By Rating", "added_rec":"By Added Books"}
			return rec_type[type]
		},

		currentSel(selVal) {
			this.value = selVal;
			let obj = {}
			obj = this.options.find((item)=>{
				return item.value === selVal;
			});
			this.getCollectionBooks(obj.value)
		},

		getCollectionNames(res) {
			let option
			for(let item_ in res) {
				// 提取collections' name
				option = {}
				option["key"] = item_
				option["value"] = item_
				this.options.push(option)
			}
		},

		getCollectionBooks(value) {
			this.books = []  // refresh books' list

			let obj = this.recommendList[value]

			let book
			let len = obj.length
			for(let i = 0; i < len; i++) {
				// console.log(obj.books[i])
				book = {}
				book["id"] = obj[i].id
				book["authors"] = obj[i].authors
				book["title"] = obj[i].title
				book["imageLink"] = obj[i].imageLink
				book["ISBN"] = obj[i].ISBN
				book["publisher"] = obj[i].publisher
				book["publish_date"] = obj[i].publish_date
				book["categories"] = obj[i].categories
				book["join_date"] = obj[i].join_date
				book["description"] = obj[i].description
				if(book["description"].length > 200) {
					book["description"] = book["description"].slice(0, 200) + "..."
				}
				book["avg_rating"] = parseInt(obj[i].avg_rating)
				this.books.push(book)
			}
		},

		jump_one_book(value) {
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
		getRecommend({id:this.myID}).then(res => {
			this.recommendList = res
			for(let v in res){
				this.value = v
				break
			}
			// this.value = this.recommendList.keys(0)
			this.getCollectionNames(res)
			this.getCollectionBooks(this.value)
			console.log("recommendList: ", this.recommendList)
			console.log("value: ", this.value)
		})
	},

	created() {
		getAccount().then(res => {
			this.myID = parseInt(res.id)
			console.log("id: ", this.myID)
		})
	}
}
</script>

<style lang="less" scoped>
html, body {
	height: 100%;
	width: 100%;
	margin: 0;
	padding: 0;
	background: aliceblue;
}

#app1 {
	font-family: 'Avenir', Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #2c3e50;
	background: aliceblue;
	height: 100%;
	width: 100%;
	position:absolute;
}

.choose_collection{
	margin-top: 50px;
}

.content {
	margin: 10px 30px 30px 30px;
	width: 180px;
}

.el-divider {
	margin-top: 60px;
}

.el-divider__text {
	font-size: 30px;
	background-color: aliceblue;
}

.wrap {
	margin-top: 100px;
	display: grid;
	grid-template-columns: repeat(3, 1fr);
}

.grid-content {
	min-height: 36px;
}

.el-button {
	margin-top: 5px;
}

.img {
	width: 180px;
	height: 240px;
}
</style>