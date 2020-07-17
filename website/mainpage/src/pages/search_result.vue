<style scoped>
	.body{
		width: 70%;
		margin: auto;
	}
	h2{
		height: 30px;
		margin: 10px 0 0 20px;
	}
	.result{

	}


</style>

<template>
	<div>
		<div>
			<Header @childfromheader="childfromheader(arguments)"></Header>
		</div>

		<div class="body">
			<h2>Search {{key_word}}</h2>
			<div class="result">

			</div>
		</div>
	</div>
</template>

<script>
import Header from '../components/homepage_components/header'
import {getSearchResult} from '../network/single_book'

export default {
	name: 'search_result',
	data(){
		return{

			search_type:'',
			key_word:''

		}
	},
	components:{
		Header

	},
	methods:{
		childfromheader(value){
			console.log(value)
			this.key_word=value[0]
			this.search_type=value[1]
			var that=this
			let post_value={search_type:that.search_type,key_word:that.key_word }
			getSearchResult(post_value).then(res=>{
				console.log(res)
			}).catch(err=>{
				console.log(err)
			})
		}


	},
	// mounted () {
	// 	var that=this
	// 	let post_value={search_type:that.search_type,key_word:that.key_word }
	// 	getSearchResult(post_value).then(res=>{
	// 		console.log(res)
	// 	}).catch(err=>{
	// 		console.log(err)
	// 	})
	//
	// }
}
</script>

