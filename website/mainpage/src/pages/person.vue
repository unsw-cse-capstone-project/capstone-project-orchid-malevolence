<template>
<div class="wrap">
	<div class="header">
		<Header></Header>
	</div>
	
	<div class="content">
		<el-tabs :tab-position="tabPosition" style="height: 100%;">
			<!-- Personal information -->
			<el-tab-pane label="Personal information">
				<div class="Per_info_title">
					Personal information
				</div>
				
				<div class="Per_info">
					
					<el-form ref="PerinfoFormRef" :model="PerinfoForm" label-width="80px" class="register_form">
						<!-- username -->
						<el-form-item label="Username" prop="username">
							<el-input v-model="PerinfoForm.username" placeholder="username" prefix-icon="el-icon-user" :disabled="true"></el-input>
						</el-form-item>
						<!-- email -->
						<el-form-item label="Email" prop="email">
							<el-input type="email" v-model="PerinfoForm.email" placeholder="email" prefix-icon="el-icon-message" :disabled="true"></el-input>
						</el-form-item>
						<!-- join date -->
						<el-form-item label="join date" prop="join date">
							<el-input v-model="PerinfoForm.regisdate" placeholder="join date" prefix-icon="el-icon-date" :disabled="true"></el-input>
						</el-form-item>
						<!-- birthday -->
						<el-form-item label="birthday" prop="birthday">
							<el-date-picker v-model="PerinfoForm.date_of_birth" type="date" placeholder="birthday" :picker-options="pickerOptions0"></el-date-picker>
						</el-form-item>
						<!-- gender -->
						<el-form-item label="Gender" prop="gender">
							<el-radio-group v-model="PerinfoForm.gender">
								<el-radio label="Male"></el-radio>
								<el-radio label="Female"></el-radio>
							</el-radio-group>
						</el-form-item>
						<!-- confirm -->
						<el-form-item class="btns">
							<el-button type="primary" @click="confirm">confirm</el-button>
						</el-form-item>
					</el-form>
				</div>
			</el-tab-pane>
			
			<!-- Collection -->
			<el-tab-pane label="collection">collection</el-tab-pane>
			
			<el-tab-pane label="set goal">
				<div class="Per_info_title">
					set goal
				</div>
				<el-divider content-position="left">How many books do I want to read this year</el-divider>
				<div class="year">
					<div class="left">
					
					</div>
					<div class="right">
					
					</div>
				</div>
				<el-divider content-position="left">How many books have I read this year</el-divider>
				<div class="month">
					<div class="left">
					
					</div>
					<div class="right">
					
					</div>
				</div>
			</el-tab-pane>
		</el-tabs>
	</div>
</div>
</template>

<script>
import Header from '../components/homepage_components/header.vue'
import {getperinfodata} from '../network/single_book'
import {postperinfo} from '../network/single_book'
// import axios from 'axios'
export default {
	components:{
		Header
	},
	data() {
		return {
			tabPosition: 'left',
			pickerOptions0: {
				disabledDate(time) {
					return time.getTime() > Date.now() - 8.64e6//如果没有后面的-8.64e6就是不可以选择今天的
				}
			},
			PerinfoForm: {
				id:'',
				username: '',
				email: '',
				regisdate: '',
				date_of_birth:'',
				gender: ''
			}
		}
	},
	methods: {
		confirm() {
			this.$refs.PerinfoFormRef.validate(async valid => {
				if (!valid) { return }
				postperinfo(this.PerinfoForm).then(res=>{
					console.log(res);
					this.$message.success('Modify successfully');
				}).catch(err=>{
					console.log(err)
					this.$message.error('Modify failure');
				})
			})
		}
	},
	mounted: function () {
		this.$refs.PerinfoFormRef.validate(async valid => {
			if (!valid) { return }
			getperinfodata().then(result =>{
				// console.log(result)
				this.PerinfoForm.username = result.username
				this.PerinfoForm.email = result.email
				this.PerinfoForm.regisdate = result.join_date
				this.PerinfoForm.date_of_birth = result.date_of_birth
				this.PerinfoForm.gender = result.gender
				this.PerinfoForm.id = result.id
			}).catch((error)=>{
				console.log(error);
			})
		})
		
	}
}
</script>

<style lang="less" scoped>
	body, html{
		height: 100%;
		overflow: hidden;
	}
	.header{
		margin-bottom: 10px;
	}
	.wrap{
		position: absolute;
		height: 100%;
		width: 100%;
		background: url(../assets/person2.png) no-repeat fixed;
		background-size: cover;
		background-origin: border-box;
		opacity:0.85;
	}
	.content{
		height: 91%;
		width: 70%;		
		border: 1px solid;
		margin: auto;
	}
	// 个人资料
	.Per_info_title{
		margin-top: 30px;
		font: 34px bolder;
	}
	.el-input{
		width: 300px;
	}
	.Per_info{
		margin-top: 50px;
	}
	// 目标
	.year, .month{
		height: 250px;
		border: 1px solid;
		width: 70%;
		margin: auto;
		margin-top: 15px;
	}
	.left{
		float: left;
		width: 20%;
		height: 230px;
		border: 1px solid;
		background-color: deeppink;
	}
	.right{
		// float: left;
		border: 1px solid;
		width: 100%;
		height: 230px;
		background-color: skyblue;
	}
</style>
