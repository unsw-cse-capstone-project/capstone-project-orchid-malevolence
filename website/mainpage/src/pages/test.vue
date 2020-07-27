<template>
	<div></div>
</template>

<script>
import {filtersearchbook} from '../network/requests'

export default {
	name: 'test',
	data(){
		return{
			postval:{
				search_type:'',
				key_word:'',
				filter_rating:''
			},
		}
	},
	created () {
		this.postval.search_type='Title'
		this.postval.key_word='python'
		this.postval.filter_rating=3
		console.log(this.postval)

		filtersearchbook(this.postval).then(res=>{
			console.log(res)
		})
	}

}
</script>

<style scoped>

</style>