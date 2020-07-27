<style lang="less" scoped>
	.body{
		width: 70%;
		margin: auto;
	}
	h2{
		height: 30px;
		margin: 10px 0 20px 0;
	}



</style>

<template>

	<div>
		<div>
			<Header></Header>
		</div>

		<div class="body">
			<h2>Search {{key_word}}</h2>
			<book_list :books="result_list" v-if="isShow"></book_list>

		</div>


	</div>


</template>

<script>
import book_list from '../components/search_result_components/book_list'
import {getSearchResult,filtersearchbook} from '../network/requests'
import Header from  '../components/homepage_components/header'


export default {
	name: 'search_result',

	data(){

		return{
			token_log: localStorage.getItem('token'),
			search_type:'',
			key_word:'',
			score:'',
			result_list:[],
			isShow:false,

		}
	},
	components:{
		// search_model,
		book_list,
		Header

	},
	methods:{

		//将请求的数据按每页10个显示，包含当前页，总数
		slite_pages:function(value){
			console.log(value)

			let list=[]
			let start=0
			let num=parseInt(value.length/10)
			let i
			for (i=0;i<=num;i++ ){
				list.push({total_book:value.length,page:i,book_li:value.slice(start,(i+1)*10)})

				start=(i+1)*10
			}
			let result=value.slice(start,i*10)
			if (result.length){
				list.push({total_book:value.length,page:i,book_li:value.slice(start,(i+1)*10)})
			}
			console.log(list)
			return list

		},




	},
	//在监听到搜索点击的时候触发，向后台请求数据，并分页

	watch: {
		'$route' (to, from) {
			console.log(to)
			console.log(from)

			// 路由传参获取title/author 和keyword
			this.key_word=this.$route.query.key_word
			this.search_type=this.$route.query.search_type
			this.score=this.$route.query.score
			if (this.score===''){
				if(this.search_type===""){
					this.search_type='Title'
				}
				let post_value={search_type:this.search_type,key_word:this.key_word }
				//发送axios get请求
				console.log(post_value)
				getSearchResult(post_value).then(res=>{
					if (res.status===400){
						this.$message({message:'No book about: '+this.key_word, showClose:true,} )

						this.isShow=false
						let temp=this.key_word
						this.key_word=this.search_type+temp+ '. There is no related book'

					}else{

						this.isShow=true

						//得到结果
						this.result_list=this.slite_pages(res)
					}
					console.log(this.result_list)
					console.log('from router')
				}).catch(err=>{

					console.log(err)
				})

			}
			else {
				if(this.search_type===""){
					this.search_type='Title'
				}
				let post_value={search_type:this.search_type,key_word:this.key_word,filter_rating:this.score }
				//发送axios get请求
				console.log(post_value)
				filtersearchbook(post_value).then(res=>{
					if (res.status===400){
						this.$message({message:'No book about: '+this.key_word, showClose:true,} )

						this.isShow=false
						let temp=this.key_word
						this.key_word=this.search_type+temp+ '. There is no related book'

					}else{

						this.isShow=true

						//得到结果
						this.result_list=this.slite_pages(res)
					}
					console.log(this.result_list)
					console.log('from router')
				}).catch(err=>{

					console.log(err)
				})
			}




		}
	},

	mounted () {

		//路由传参获取title/author 和keyword
		this.key_word=this.$route.query.key_word
		this.search_type=this.$route.query.search_type
		if(this.search_type===""){
			this.search_type='Title'
		}
		let post_value={search_type:this.search_type,key_word:this.key_word }
		//发送axios get请求
		console.log(post_value)
		getSearchResult(post_value).then(res=>{
			if (res.status===400){
				this.$message({message:'No book about: '+this.key_word, showClose:true,} )

					this.isShow=false
					let temp=this.key_word
					this.key_word=temp+ '. There is no related book'

			}else{

					this.isShow=true

				//得到结果
				this.result_list=this.slite_pages(res)
			}
			console.log(this.result_list)
		}).catch(err=>{

			console.log(err)
		})




	},

}
</script>

