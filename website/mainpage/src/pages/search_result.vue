<style lang="less" scoped>
	.body {
		width: 70%;
		margin: auto;
	}

	h2 {
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
			<h2 v-show="isShow">Search {{key_word}}</h2>
			<book_list v-if="isShow" :books="result_list"></book_list>

		</div>


	</div>


</template>

<script>
import book_list from '../components/search_result_components/book_list'
import {getSearchResult, filtersearchbook,getCollectionmultdata} from '../network/requests'
import Header from '../components/homepage_components/header'


export default {
	name: 'search_result',

	data () {

		return {
			token_log: localStorage.getItem('token'),
			search_type: 'Title',
			key_word: '',
			score: 0,
			result_list: [],
			isShow: false,
			user: '',
			post_value: {}

		}
	},
	components: {
		// search_model,
		book_list,
		Header

	},
	methods: {

		//divided the books into pages, every page contains 10 books
		slite_pages(value) {
			console.log(value)
			let len = value.length
			for (let j = 0; j < len; j++) {
				value[j].avg_rating = parseFloat(value[j].avg_rating)
			}
			let list = []
			let start = 0
			let num = parseInt(value.length / 10)
			let i
			for (i = 0; i <= num; i++) {
				list.push({total_book: value.length, page: i, book_li: value.slice(start, (i + 1) * 10)})
				start = (i + 1) * 10
			}
			let result = value.slice(start, i * 10)
			if (result.length) {
				list.push({total_book: value.length, page: i, book_li: value.slice(start, (i + 1) * 10)})
			}
			console.log(list)
			return list
		},


		//search result based on title/author/user
		getResult: function (val) {

			this.key_word = val.key_word
			if (val.search_type !== '') {
				this.search_type = val.search_type

			}
			this.score = parseFloat(val.score)

			// if search not based on rating, which means not choose rating range
			if (isNaN(this.score)) {
				// case0 search based on user
				if (this.search_type === 'User') {
					this.isShow = false
					getCollectionmultdata().then(res=>{
						console.log(res)})


				}
				//search based on Title or authors
				else {
					this.post_value = {search_type: this.search_type, key_word: this.key_word}
					getSearchResult(this.post_value).then(res => {
						if (res.status === 400) {
							this.$message({message: 'No book about: ' + this.key_word, showClose: true,})
							this.isShow = false
							let temp = this.key_word
							this.key_word = this.search_type + temp + '. There is no related book'
						} else {
							console.log(res)
							//if get the response, the show the result


							//get the resut
							this.result_list = this.slite_pages(res)
							this.isShow = true
						}
						console.log(this.result_list)
						console.log('from router')
					}).catch(err => {

						console.log(err)
					})
				}
			}
			// if search based on rating range
			else {
				this.post_value = {search_type: this.search_type, key_word: this.key_word, filter_rating: this.score}
				filtersearchbook(this.post_value).then(res => {
					if (res.status === 400) {
						this.$message({message: 'No book about: ' + this.key_word, showClose: true,})

						this.isShow = false
						let temp = this.key_word
						this.key_word = this.search_type + temp + '. There is no related book'

					} else {


						console.log(res)

						//get the result
						this.result_list = this.slite_pages(res)
						this.isShow = true
					}
					console.log(this.result_list)
					console.log('from router')
				}).catch(err => {

					console.log(err)
				})

			}
		}


	},
	//listen to the route, and to check whether it changed
	watch: {
		'$route' () {
			this.getResult(this.$route.query)
			this.search_type = 'Title'
		}
	},

	mounted () {
		this.getResult(this.$route.query)
		this.search_type = 'Title'
	},

}
</script>

