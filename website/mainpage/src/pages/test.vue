<template>
	<div></div>
</template>

<script>
import {getSingleBookmultdata} from '../network/requests'

export default {
	name: 'test',
	created () {
		let postvalue={book_id:"eeJOAQAAQBAJ"}
		console.log(postvalue)
		getSingleBookmultdata(postvalue).then(res=>{
			console.log(res)
		})

	}
}
</script>

<style scoped>


</style>