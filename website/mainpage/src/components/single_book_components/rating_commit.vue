
<template>
	<div>
		<el-button type="primary" @click="isShowDialog" icon="el-icon-edit">rating and commit</el-button>

		<el-dialog
						title="rating and commit"
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

				<el-input class="commit" type="textarea" :autosize="{ minRows: 7, maxRows: 10}" placeholder="Commit this book" v-model="textarea1">
				</el-input>

			<span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">cancel</el-button>
        <el-button type="primary" @click="submite_ratingandreview()">submit</el-button>
      </span>
		</el-dialog>

	</div>
</template>

<script>
import {getSingleBookmultdata, postrating, postReview} from '../../network/requests'

export default {
	name: 'rating_commit',
	data () {
		return {
			token_log: localStorage.getItem('token'),
			username: localStorage.getItem('username'),
			dialogVisible: false,
			// wrapperClosable:true,
			textarea1: '',
			value: 0,
			colors: ['#99A9BF', '#F7BA2A', '#FF9900']
		}
	},
	props: {
		bookID: String //the arguments bookID received from father page one_book page
	},
	methods: {
		isShowDialog(){
			if (this.token_log){
				this.dialogVisible=true

			}else{
				this.$message({message: 'please login: ', type: 'warning',showClose: true,})

			}

		},
		submite_ratingandreview () {

			if (this.token_log) {

				let postvalue = {
					'rating_info': {
						'book': this.bookID,
						'rating': this.value
					}
				}

				postrating(postvalue).then(res => {
					console.log(res)
				})
				let post_review = {
					'book_id': this.bookID,
					'review': {
						'content': this.textarea1
					}
				}
				postReview(post_review).then(res => {
					console.log(res)
				}).catch(res => {
					console.log(res)
				})
				let get_book_value = {
					'book_id': this.bookID,

				}
				getSingleBookmultdata(get_book_value).then(res => {
					console.log(res)
					location.reload()

				}).catch(res => {
					console.log(res)
				})

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
	.commit {
		margin-top: 20px;
	}





</style>