<style scoped>
	.body{
		width: 70%;
		margin: 80px auto;
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
				<div><p>publish_date: {{book.publish_date}}</p></div>
				<div><p>ISBN: {{book.ISBN}}</p></div>
			</div>

			<div class="read_score">
				<read_score :res="result"></read_score>
			</div>
			<div class="rating">
				<rating :bookID="book.id"></rating>


			</div>




		</div>


	</div>


</template>

<script>
import Header from '../components/homepage_components/header'
import {getSingleBookmultdata} from '../network/single_book'
import read_score from '../components/single_book_components/read_score'
import Rating from '../components/single_book_components/rating'

export default {
	name: 'one_book',
	data () {
		return {
			token_log: localStorage.getItem('token'),
			id: null,
			review:[],
			book:[],
			book_id:null,
			result:{
				rate:Number,
				TotalCount:Number,
				averageScore:Number,
				book_id:""

			},
			update_cont:0


		}

	},
	components: {
		Header,
		read_score,
		Rating
	},

	created () {
		this.getData();
	},

	methods: {
		getData () {
			this.book=(this.$route.params.item)
			// let that=this.book.id
			console.log(this.book)
			// let post_value=(this.$route.params.item)

			let post_value={book_id:this.book.id}
			console.log(post_value)

			getSingleBookmultdata(post_value).then(result => {
				console.log(result)
				this.result.rate=result.rating.rating
				this.result.TotalCount=result.rating.how_many_user_scored
				this.result.averageScore=result.rating.average_rating
				this.result.book_id=result.id

				//

			}).catch(res=>{
				console.log(res)
			})
		},



	},

}
</script>

