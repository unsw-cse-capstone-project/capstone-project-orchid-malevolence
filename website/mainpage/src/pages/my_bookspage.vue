<style scoped>
	.body{
		width: 80%;
		margin: auto;

	}
	.choose_collection{
		margin-top: 50px;
		width: 15%;

		vertical-align: top;
		display: inline-block;

	}
	.collection_book{
		width: 70%;
		height: 90%;
		margin-left: 5%;



		vertical-align: top;
		display: inline-block;



	}
	.book_item{
		display: inline-block;
		margin: 20px 20px 20px 5px

	}
	.img-box{
		width: 20%;
		height: 180px;

	}
	.text-block{
		display: inline-block;
		vertical-align: top;

		width: 65%;
		word-break: break-all
	}
	.search_model{
		width: 25%;
		margin: 10px 25%;

	}
	.collections{
		margin-top: 10px;
	}



</style>
<template>
	<div>
		<div>
			<Header></Header>
		</div>
		<div class="search_model">
			<el-input v-model="input" placeholder="Search a book inside your collections">
				<el-button  style="display: inline-block" slot="append" icon="el-icon-search" @click="jump_this_book"></el-button>
			</el-input>

		</div>

		<div class="body">

			<div class="choose_collection">
				<el-button style="width: 100%" @click="isShow=true;show2=false;show=false" size="small">All books</el-button>
				<p style="margin-top:20px; border-bottom: 1px solid gray"></p>
				<el-select class="collections" v-model="value" placeholder="please select a collection" @change="currentSel(value)">
					<el-option
									v-for="item in options"
									:key="item.label"
									:value="item.value"
					>
					</el-option>
				</el-select>
			</div>

			<div class="collection_book" >
<!--				show all books in all collections-->
				<div v-show="isShow" >
					<el-divider content-position="center" class="divider">All books</el-divider>


					<div class="item_box" v-for="item in all_books" :key="item.ISBN">
						<div class="book_item img-box" >
							<img  :src="item.imageLink" style="width:90%;height: 100% " alt="" >
						</div>

						<div class="book_item text-block">
							<div><h5 style="word-break: break-all">{{item.title}}</h5></div>
							<el-rate
											v-model="item.avg_rating"
											disabled
											show-score
											text-color="#ff9900"
											score-template="{value}">
							</el-rate>

							<div><p>Author: {{item.authors}}</p></div>
							<div><p>Publisher: {{item.publisher}}</p></div>
							<div><p>publish_date: {{item.publish_date}}</p></div>

						</div>
					</div>
				</div>


				<!--			显示搜索到的书-->
				<div v-show="show">
					<el-divider content-position="center" class="divider">search result in your collections</el-divider>
					<div   class="item_box" v-for="(item,index) in search_book" :key="index">
						<div class="book_item img-box" >
							<img  :src="item.imageLink" style="width:90%;height: 100% " alt="" >
						</div>
						<div class="book_item text-block">
							<div><h5 style="word-break: break-all">{{item.title}}</h5></div>
							<el-rate
											v-model="item.avg_rating"
											disabled
											show-score
											text-color="#ff9900"
											score-template="{value}">
							</el-rate>

							<div><p>Author: {{item.authors}}</p></div>
							<div><p>Publisher: {{item.publisher}}</p></div>
							<div><p>publish_date: {{item.publish_date}}</p></div>

						</div>
					</div>
				</div>


						<!-- 分割线，显示当前collection名字 -->
<!--						主体，显示 图 & 书名-->
				<div v-show="show2">
					<el-divider content-position="center" class="divider">{{value}}</el-divider>

					<div  v-for="item in books2" :key="item.imageLink" class="item_box">

						<div class="book_item img-box">
							<img :src="item.imageLink" class="img" style="width:90%;height: 100% " @click="jump_one_book(item)" />
						</div>
						<div class="book_item text-block">
							<div><h5 style="word-break: break-all">{{item.title}}</h5></div>
							<el-rate
											v-model="item.avg_rating"
											disabled
											show-score
											text-color="#ff9900"
											score-template="{value}">
							</el-rate>

							<div><p>Author: {{item.authors}}</p></div>
							<div><p>Publisher: {{item.publisher}}</p></div>
							<div><p>publish_date: {{item.publish_date}}</p></div>
						</div>
					</div>
				</div>


<!--					</div>-->
				</div>


			</div>


	</div>
<!--	</div>-->





</template>

<script>

import {getCollectionmultdata} from '../network/single_book'
import Header from '../components/homepage_components/header'
// import search_inner_collections from '../components/search_result_components/search_inner_collections'
export default {
	name: 'my_bookspage',
	data () {
		return {
			books:[],
			all_books:[],
			name:'',
			input:'',
			isShow:true,
			search_book:[],
			show:false,
			// 所有的collections
			show2:false,
			books2: [],       // current collection's books
			options: [],     // collections' content
			value: '',       // collection name
			// cur_key: 0,      // collection id
			collections: [], // result from api package
			item: '', // one book param

			// TODO: connect with backend, get all book images in this collections



		}
	},
	components: {
		Header,
		// search_inner_collections


		// homepage_collections
	},
	mounted () {
		getCollectionmultdata().then(res=>{
			this.books=res
			this.getAllBooks(res)
			console.log(this.books)
			console.log(this.isShow)
// 所有的collections
			this.collections = res
			this.value = this.collections[0].name
			this.getCollectionNames(res)   // 把api返回的collection名字整理出来
			// this.getCollectionBooks(this.collections[0].id) // default select first collection
			console.log(this.options)
			console.log(this.value)
			console.log(this.books2)
		}).catch(res=>{
			console.log(res)})
		// 所有的collections

	},
	methods: {
		getAllBooks(val){
			let len=val.length
			for (let i=0;i<len;i++){
				let new_len=val[i].books.length
				let books=val[i].books
				for(let j=0;j<new_len;j++){
					this.all_books.push(books[j])
				}
			}
			console.log(this.all_books)
		},
		jump_this_book(){
			this.search_book=[]
			this.isShow=false
			this.show2=false
			this.show=true


			let len=this.all_books.length
			for(let i=0;i<len;i++){
				let title=this.all_books[i].title.toLowerCase()
				let input=this.input.toLowerCase()
					if ( title.indexOf(input)!==-1){
					this.search_book.push(this.all_books[i])

				}

			}
			console.log(this.search_book)
			console.log(this.isShow)


		},
		// 所有的collections
		currentSel(selVal) {
			this.value = selVal;
			let obj = {}
			obj = this.options.find((item)=>{
				return item.value === selVal;
			});
			this.getCollectionBooks(obj.key)
			this.isShow=false
			this.show=false
			this.show2=true
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
			this.books2 = []  // refresh books' list
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
				this.books2 .push(book)
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
	}
}
</script>

