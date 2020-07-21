<style scoped>
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
			<search_model @childfromheader="childfromheader(arguments)"></search_model>
		</div>

		<div class="body">
			<h2>Search {{key_word}}</h2>
			<book_list :books="result_list" v-if="isShow"></book_list>

		</div>
	</div>
</template>

<script>
import search_model from '../components/search_result_components/search_model'
import book_list from '../components/search_result_components/book_list'
import {getSearchResult} from '../network/single_book'


export default {
	name: 'search_result',
	data(){

		return{
			token_log: localStorage.getItem('token'),
			search_type:'',
			key_word:'',
			result_list:[],
			isShow:false

		}
	},
	components:{
		search_model,
		book_list,

	},
	methods:{
		//在监听到子组件搜索点击的时候触发，向后台请求数据，并分页

		childfromheader(value){
			console.log(value)
			this.key_word=value[0]
				this.search_type=value[1]
				if(this.search_type===""){
					this.search_type='Title'

				}
				// post的参数（后端要求传输的内容）
				let that=this
				let post_value={search_type:that.search_type,key_word:that.key_word }

			// console.log(typeof post_value)
			getSearchResult(post_value).then(res=>{
				// console.log(res)
				if (res.status===400){
					// console.log('ss')
					this.$message({message:'No related book: '+this.key_word, showClose:true,} )
					this.$nextTick(()=>{
						this.isShow=false
						let temp=this.key_word
						this.key_word=temp+ '. There is no related book'
					})


				}else{
					this.$nextTick(()=>{
						this.isShow=true

					})

					this.result_list=this.slite_pages(res)
				}
				// console.log(this.result_list)
				// console.log(this.result_list)
			}).catch(err=>{

				console.log(err)
			})



		},
		//将请求的数据按每页10个显示，包含当前页，总数
		slite_pages:function(value){
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
			// console.log(list)



			return list

		},




	},

	created () {
		this.key_word=this.$route.params.key_word
		// console.log(this.key_word)
		this.search_type=this.$route.params.search_type
		// console.log(this.search_type)
		if(this.search_type===""){
			this.search_type='Title'
		}


		let post_value={search_type:this.search_type,key_word:this.key_word }
		// console.log( post_value)
		getSearchResult(post_value).then(res=>{
			// console.log(res)
			if (res.status===400){
				// console.log('ss')
				this.$message({message:'No related book: '+this.key_word, showClose:true,} )
				this.$nextTick(()=>{
					this.isShow=false
					let temp=this.key_word
					this.key_word=temp+ '. There is no related book'
				})


			}else{
				this.$nextTick(()=>{
					this.isShow=true

				})

				this.result_list=this.slite_pages(res)
			}
			// console.log(this.result_list)
			// console.log(this.result_list)
		}).catch(err=>{

			console.log(err)
		})




	}

}
</script>

