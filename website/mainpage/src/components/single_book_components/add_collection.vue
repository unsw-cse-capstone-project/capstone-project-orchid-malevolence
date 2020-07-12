<style scoped>
	*{
		margin: 0;
		padding: 0;
		box-sizing: border-box;

	}
	.add_button{
		border: solid 1px black;
		position: absolute;
		font-size: 18px;
		width: 40px;
		height: 30px;
		border-radius: 3px;

		margin: 20px 50px;
	}
	.add_button:hover{
		background-color: lightblue;

	}

	.popBox{
		position: relative;
		width: 40vw;
		height: 50vh;
		border-radius: 4px;
		z-index: 100;
		background-color: white;
		border: solid 1px black;
		font-size: 20px;
		top:-200px;
		left:300px

	}
	.close{
		border: solid 1px ;
		float: right;

		margin: 4px 5px 0 0;


	}




</style>
<template>
	<div class="box">
		<button class="add_button" @click="clickshow">add</button>
		<div class="popBox" v-show="isShow">
				<span style="margin: 5px 0 0 10px; font-size: 18px">add to a collection</span>
				<el-button class="close" @click="closeshow" type="primary">x</el-button>
<!--			//遮罩层-->




		</div>



	</div>



</template>

<script>
export default {
	name: 'add_collection',
	data () {
		return {
			isShow: false

		}
	},
	methods: {
		clickshow () {
			this.isShow = true
			this.$emit('clickshow')


		},
		closeshow () {
			this.isShow = false
			this.$emit('closeshow')
		}
	}

	// methods: {
	// 	open() {
	// 		this.$alert('这是一段内容', 'add to a collection', {
	// 			confirmButtonText: 'confirm',
	// 			callback: action => {
	// 				this.$message({
	// 					type: 'info',
	// 					message: `action: ${ action }`
	// 				});
	// 			}
	// 		});
	// 	}
	// }

}
</script>

