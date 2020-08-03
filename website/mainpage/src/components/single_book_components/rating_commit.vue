
<template>
	<div>
		<span style="display: inline-block; margin-right: 10px">Rating</span>
		<el-rate v-show="isShow"
						@change="submit_rating(value)"
						v-model="value"
						:colors="colors">
		</el-rate>
		<el-rate v-show="!isShow"
						v-model="value1"
						disabled
						show-score
						text-color="#ff9900"
						score-template="{value}">
		</el-rate>
		<span v-show="isShow" style="display: inline-block; margin-right: 10px">{{value1}}</span>
		<el-button type="primary" @click="isShowDialog" icon="el-icon-edit">comment</el-button>

		<el-dialog
						title="comment"
						:visible.sync="dialogVisible"
						width="30%">

			<!--			Pop up a dialog-->

					<p>rating this book:</p>

					<el-rate
									v-model="value"
									show-score
									score-template="{value}"
									:colors="colors">
					</el-rate>

				<el-input class="comment" type="textarea"  @keyup.enter.native="submite_ratingandreview" :autosize="{ minRows: 7, maxRows: 10}" placeholder="Comment this book" v-model="textarea1">
				</el-input>

			<span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">cancel</el-button>
        <el-button type="primary" @click="submite_ratingandreview">submit</el-button>
      </span>
		</el-dialog>

	</div>
</template>

<script>
import {postrating, postReview} from '../../network/requests'
export default {
	name: 'rating_commit',
	data () {
		return {
			token_log: localStorage.getItem('token'),
			username: localStorage.getItem('username'),
			dialogVisible: false,
			// wrapperClosable:true,
			textarea1: "",
			isShow:true,
			value: 0,
			value1:0,
			colors: ['#99A9BF', '#F7BA2A', '#FF9900']
		}
	},
	props: {
		bookID: String, //the arguments bookID received from father page one_book page
		book_name:String
	},

	// this.dialogVisible = false
	methods: {
		isShowDialog(){
			if (this.token_log){
				this.dialogVisible=true

			}else{
				this.$message({message: 'please login: ', type: 'warning',showClose: true,})

			}

		},
		submit_rating(value){
			this.isShow=false

			let postvalue = {
				'rating_info': {
					'book': this.bookID,
					'rating': value
				}
			}

			postrating(postvalue).then(res => {
				console.log(res)
			})
			this.$emit('val',value)
			this.value1=value

			// location.reload()

		},
		submite_ratingandreview () {

			if (this.token_log) {
				// if (this.textarea1===""){
				// 	this.$message({message: 'please write your commit: ', type: 'warning',showClose: true,})
				// 	return
				// }

				let post_review = {
					'book_id': this.bookID,
					'review': {
						'content': this.textarea1
					}
				}
				if (this.textarea1!==""){
					postReview(post_review).then(res => {
						console.log(res)
					}).catch(res => {
						console.log(res)
					})
				}
			}


			this.dialogVisible = false



		},

	}
}
</script>

<style scoped>
	/deep/ .el-dialog__body{
		padding: 0 20px;
		color: #606266;
		font-size: 14px;
		word-break: break-all;
	}
	.comment {
		margin-top: 20px;
	}
	.el-rate{
		display: inline-block;
	}





</style>