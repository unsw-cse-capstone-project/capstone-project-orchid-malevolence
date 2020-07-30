<style lang="less" scoped>
	.body{
		width: 70%;
		margin: 80px auto;
		position: relative;
	}
	.title{
		margin: 20px 0;
	}

	.img-box{
		width: 200px;
		height: 250px;
		display: inline-block;

	}
	.text-block{
		display: inline-block;
		vertical-align: top;

		width: 50%;
		word-break: break-all
	}
	.read_score{
		padding-left: 10px;
		display: inline-block;
		vertical-align: top;
		border-left: solid 1px gray;

	}
	.rating{
		margin: 20px;
		display: inline-block;
		vertical-align: top;

		/*font-size: 18px;*/
	}
	.btn_add{
		width: 25%;
		display: inline-block;
		/*vertical-align: top;*/
	}
	
	.get_review_box{
		width: 95%;
		border-top: 2px solid gray;
		height: 10%;
	}

	.username{
		color: #3377aa;
		margin-right: 20px;
		display: inline-block;
	}
	.inner_socre{
		margin-right: 10px;
		display: inline-block;

	}
	.inner_data{
		color: #666666;

		margin-right: 10px;

		display: inline-block;

	}
	.inner_content{
		display: block;
		margin: 10px 0;
	}



</style>

<template>
	<div>
		<Header></Header>

		<div class="body">
			<div class="title"><h3 style="word-break: break-all">{{book.title}}</h3></div>

			<div class="img-box" >
				<img  :src="book.imageLink" style="width:90%;height: 100% " alt="">
			</div>

			<div class="book_item text-block">
				<div><p>Author: {{book.authors}}</p></div>
				<div><p>Publisher: {{book.publisher}}</p></div>
				<div><p>publish_date: {{book.publisher_data}}</p></div>
				<div><p>ISBN: {{book.ISBN}}</p></div>
				<div><p>categories: {{book.category}}</p></div>

			</div>

			<div class="read_score">
				<read_score :res="result"></read_score>
			</div>
			<div class="btn_add">
				<add_your_collection :bookID="result.book_id" ></add_your_collection>
			</div>

			<div class="rating">
				<rating :bookID="result.book_id"></rating>
			</div>

			<h3 style="margin:10px 0">Reviews:</h3>
			<div v-for="item in this.result.review_book" class="get_review_box" v-bind:key="item.id">
				<span class="username">{{item.user}}</span>
					<el-rate class="inner_socre"
							v-model="item.rating"
							disabled
							text-color="#ff9900"
							score-template="{value}">
			</el-rate>
				<span class="inner_data">{{item.create_time}}</span>
				<div class="inner_content">
					<span style="overflow-wrap:break-word;">{{item.content  }}</span>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import Header from '../components/homepage_components/header'
import {getSingleBookmultdata} from '../network/requests'
import {getSingleBookmultdata1} from '../network/requestsWithoutLogin'

import read_score from '../components/single_book_components/read_score'
import Rating from '../components/single_book_components/rating'
import add_your_collection from '../components/single_book_components/add_your_collection'

export default {
	name: 'one_book',
	data () {
		return {
			token_log: localStorage.getItem('token'),
			id: null,
			count: 0,
			review: [],
			value: '',
			book: {},

			book_id:null,
			result:{
				rate:Number,
				TotalCount:Number,
				averageScore:Number,
				book_id:"",

				review_book:[]

			},
			update_cont:0
		}

	},
	components: {
		Header,
		read_score,
		Rating,
		add_your_collection,
		// get_reviews
	},

	mounted () {
		this.getData();
	},


	methods: {
		// get all info about this book
		getData () {
			this.book=this.$route.query
			let post_value={book_id:this.book.book_id}

			if(this.token_log){
				getSingleBookmultdata(post_value).then(result => {
					this.result=result
					this.result.rate=result.rating_analyse.rating
					this.result.TotalCount=result.rating_analyse.how_many_user_scored
					this.result.averageScore=result.rating_analyse.average_rating
					this.result.book_id=result.id
					this.result.review_book=result.review_book

				}).catch(res=>{
					console.log(res)
				})
			}
			else{
				//request book info like average score, reviews, totalcount of how many people have read
				getSingleBookmultdata1(post_value).then(result=>{
					this.result=result
					this.result.rate=result.rating_analyse.rating
					this.result.TotalCount=result.rating_analyse.how_many_user_scored
					this.result.averageScore=result.rating_analyse.average_rating
					this.result.book_id=result.id
					this.result.review_book=result.review_book

				}).catch(res=>{
					console.log(res)
				})
			}
		},
	},
}
</script>

