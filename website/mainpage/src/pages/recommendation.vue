<template>
	<div>
		<Header></Header>
		<el-button @click="getRecommend">test</el-button>
	</div>
</template>

<script>
import {getAccount, getRecommend} from "@/network/requests";
import Header from "@/components/homepage_components/header";

export default {
	name: "recommendation",
	data() {
		return {
			myID: '',
			recommendList: [],
		};
	},

	components:{
		Header,
	},

	methods: {
		getRecommend() {
			let idRes = {id:this.myID}
			getRecommend(idRes).then(res => {
				this.recommendList = res
				console.log("list: ", this.recommendList)
			})
		}
	},

	created() {
		getAccount().then(res => {
			// let id_ = parseInt(res.id)
			this.myID = parseInt(res.id)
			console.log("id: ", this.myID)
		})


	}
}
</script>

<style scoped>

</style>