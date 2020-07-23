<style scoped>

	.book_item{
		display: inline-block;
		margin: 20px 20px 20px 5px

	}
	.img-box{
		width: 15%;
		height: 180px;

	}
	.text-block{
		display: inline-block;
		vertical-align: top;
		/*padding-top: 10px;*/

		width: 65%;
		word-break: break-all
	}
	.info{
		font-size: 14px;
		opacity: 0.7;
	}






</style>
<template>
	<div>
		<div class="info" >Page:{{books[real_page-1].page+1}}   Totally related books: {{books[real_page-1].total_book}}</div>


		<div class="all_book" v-for="item in books[real_page-1].book_li" :key="item.ISBN">

			<div class="item_box">
				<div class="book_item img-box" >
					<img  :src="item.imageLink" style="width:90%;height: 100% " alt="" @click="jump_one_book(item)">
				</div>

				<div class="book_item text-block">
					<div><h5 style="word-break: break-all">{{item.title}}</h5></div>
					<div><p>Author: {{item.authors}}</p></div>
					<div><p>Publisher: {{item.publisher}}</p></div>
					<div><p>publish_date: {{item.publish_date}}</p></div>
					<div><p>category: {{item.categories}}</p></div>

				</div>
			</div>


		</div>
		<div style="display:flex; justify-content: center">

			<el-pagination
							background
							@current-change="getpage"
							:page-size="10"
							:pager-count="11"
							layout="prev, pager, next"
							:total=books[0].total_book>
			</el-pagination>
		</div>



	</div>
</template>

<script>
export default {
	data(){
		return{
			token_log: localStorage.getItem('token'),

			// isShow:false,

			real_page:1,

		}
	},

	name: 'book_list',
	props:{
		//books是从父组件search_result传递过来的参数
		books:{
			type:Array,
			default(){
				return []

			}

		}
	},

	methods:{
		getpage(value){
			this.real_page=value
			console.log("this.real_page "+ this.real_page)

		},
		jump_one_book (value) {
			console.log(value)

			this.$router.push({
				name: 'one_book',

				query: {

					// item:value
					book_id: value.id,
					authors:value.authors,
					title:value.title,
					ISBN:value.ISBN,
					publisher:value.publisher,
					publisher_data:value.publish_date,
					imageLink:value.imageLink,
					category:value.categories


				}

			})
		},



	},



}
</script>

