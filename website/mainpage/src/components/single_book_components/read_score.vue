
<template>
	<div class="read_score">
		<span style="font-size: 14px">Website average rating</span>
		<span class="score">{{average}}</span>
		<el-rate
						class="rate"
						v-model="average"
						disabled
						text-color="#ff9900"
						score-template="{value}">
		</el-rate>

		<ul>
			<li>5 star<el-progress class="percentage"  :percentage="this.rating_list.five"></el-progress></li>
			<li>4 star<el-progress class="percentage"  :percentage="this.rating_list.four"></el-progress></li>
			<li>3 star<el-progress class="percentage"  :percentage="this.rating_list.three"></el-progress></li>
			<li>2 star<el-progress class="percentage"  :percentage="this.rating_list.two"></el-progress></li>
			<li>1 star<el-progress class="percentage"  :percentage="this.rating_list.one"></el-progress></li>
		</ul>



		<span> {{res.TotalCount}} people have read this book</span>

	</div>

</template>

<script>


export default {
	name: 'read_score',
	data () {
		return {
			token_log: localStorage.getItem('token'),
			average: 0,
			number: Number(0),
			book_id: String,
			value: 0,
			TotalCount: '',
			isShow: true,
			rating_list:{},
			count:100,


		}
	},
	props: {
		res: Object,
		default: {}
	},


	// request method page initial and get average score of this book
	updated () {
		console.log(this.res)
		this.average = this.res.averageScore
		this.book_id = this.res.book_id
		this.TotalCount = this.res.TotalCount
		this.rating_list.five=this.res.rating_analyse.five*100
		this.rating_list.four=this.res.rating_analyse.four*100
		this.rating_list.three=this.res.rating_analyse.three*100
		this.rating_list.two=this.res.rating_analyse.two*100
		this.rating_list.one=this.res.rating_analyse.one*100
		console.log(this.rating_list)

	},


}


</script>
<style lang="less" scoped>

	.read_score {
		position: absolute;
		float: right;
		width: 220px;


	}

	span {
		display: block;
		font-size: 12px;
		margin: 5px 0;
	}
	li{
		list-style: none;
		color: gray;
	}
	ul{
		padding: 0;
		color: gray;
	}
	.percentage{
		width: 70%;
		display: inline-block;
		margin-left: 10px;
	}
	/deep/ .el-rate__text{
		font-size: 20px;
	}
	.score{
		display: inline-block;
		margin: 0 5px 0 0;
		/*margin-right: 10px;*/
		font-size: 18px;
		color: #F7BA2A;
		vertical-align: top;

	}
	.rate{
		display: inline-block;
		/*vertical-align: top;*/

	}
</style>

