<style scoped>
	.body{
		width: 70%;
		margin: 80px auto;
		position: relative;
	}
	.title{
		margin: 20px 0;
	}

	.img-box{
		width: 20%;
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
		/*font-size: 18px;*/
	}
	.btn_add{
		display: inline-block;
		vertical-align: top;
		position: absolute;
		left:18%;
		top:70%;

	}
	.get_review_box{
		position: absolute;
		width: 95%;
		border-top: 2px solid gray;

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
				<div><p>ISBN: {{book.ISBN}}</p></div>
			</div>

			<div class="read_score">
				<read_score :res="result"></read_score>
			</div>
			<div>
				<add_your_collection class="btn_add" style="display: inline-block" :bookID="result.book_id" ></add_your_collection>
			</div>
			<div class="rating">
				<rating :bookID="result.book_id"></rating>
			</div>
			<div>
				<div class="get_review_box">
					<h3 style="margin:10px 0">Reviews:</h3>
					<div>

					</div>

				</div>
<!--				<get_reviews></get_reviews>-->
			</div>







		</div>


	</div>


</template>

<script>
import Header from '../components/homepage_components/header'
import {getSingleBookmultdata} from '../network/single_book'

import read_score from '../components/single_book_components/read_score'
import Rating from '../components/single_book_components/rating'
import add_your_collection from '../components/single_book_components/add_your_collection'
// import get_reviews from '../components/single_book_components/get_reviews'


export default {
	name: 'one_book',
	data () {
		return {
			token_log: localStorage.getItem('token'),
			id: null,
			review:[],
			book:{},
			book_id:null,
			result:{
				rate:Number,
				TotalCount:Number,
				averageScore:Number,
				book_id:"",
				publisher_data: ''

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

	created () {
		this.getData();
		this.getreview()
	},

	methods: {

		getData () {
			this.book=this.$route.query

			// let that=this.book.id
			console.log(this.book)
			// let post_value=(this.$route.params.item)

			let post_value={book_id:this.book.book_id}
			console.log(post_value)

			getSingleBookmultdata(post_value).then(result => {
				console.log(result)
				this.result.rate=result.rating_analyse.rating
				this.result.TotalCount=result.rating_analyse.how_many_user_scored
				this.result.averageScore=result.rating_analyse.average_rating
				this.result.book_id=result.id
				this.result.publication_date=result.pub

			}).catch(res=>{
				console.log(res)
			})
		},
		getreview(){

		}
	},

}
</script>

