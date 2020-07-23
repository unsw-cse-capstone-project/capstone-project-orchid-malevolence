<template>
<div class="wrap">
	<div class="header">
		<Header></Header>
	</div>
	
	<div class="content">
		<el-tabs :tab-position="tabPosition" style="height: 100%;">
			<!-- Personal information -->
			<el-tab-pane label="Personal information">
				<div class="person_information">
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
				</div>
			</el-tab-pane>
			
			<!-- Collection -->
			<el-tab-pane label="collection">
				<div class="collection" >
					<div class="clearfix">
					<!-- select -->
					<div class="collection_head">
						<el-select v-model="value" placeholder="please select a collection"
									@change="currentSel(value)">
							<el-option
									v-for="item in options"
									:key="item.label"
									:value="item.value"
									
							>
							</el-option>
						</el-select>
					</div>
					<!-- create an new collection -->
					<div class="collection_add">
						<el-button type="text" @click="dialogFormVisible = true" class="collection_add_button">create an new collection</el-button>
						<el-dialog title="create an new collection" :visible.sync="dialogFormVisible">
							<el-form ref="collectionformRef" :model="collectionform">
								<el-form-item label="collection name" :label-width="formLabelWidth">
									<el-input v-model="collectionform.name" autocomplete="off"></el-input>
								</el-form-item>
							</el-form>
							<div slot="footer" class="dialog-footer">
								<el-button @click="dialogFormVisible = false">cancel</el-button>
								<el-button type="primary" @click="submit">confirm</el-button>
							</div>
						</el-dialog>
					</div>
					
					<!-- reset collection name -->
					<div class="collection_reset">
						<el-button type="text" @click="dialogFormVisible2 = true" class="collection_change_button">reset collection</el-button>
						<el-dialog title="reset collection" :visible.sync="dialogFormVisible2">
							<el-form ref="recollectionFormRef" :model="recollectionForm">
								<el-form-item label="reset collection" :label-width="formLabelWidth">
									<el-input v-model="recollectionForm.new_name" autocomplete="off"></el-input>
								</el-form-item>
							</el-form>
							<div slot="footer" class="dialog-footer">
								<el-button @click="dialogFormVisible2 = false">cancel</el-button>
								<el-button type="primary" @click="change">confirm</el-button>
							</div>
						</el-dialog>
					</div>
					
					<!-- delete collection -->
					<!-- <div class="collection_dele">
						<el-button type="text" @click="open" class="collection_dele_button">delete collection</el-button>
					</div> -->
					</div>
					<!-- 分割线，显示当前collection名字 -->
					<el-divider content-position="center" class="divider">{{value}}</el-divider>
					
					<!-- collection主体，显示 图 & 书名 -->
					<div class="coll_wrap">
						<div class="coll_content" v-for="item in books" :key="item.imageLink">
							<img :src="item.imageLink" class="img" alt/>
							<a href="item.url">{{item.title}}</a>
						</div>
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
import {getCollectionmultdata} from '../network/single_book'
import {postnewcollection} from '../network/single_book'
import {changecollectioname} from '../network/single_book'
//import {delecollection} from '../network/single_book'
// import axios from 'axios'
export default {
	components:{
		Header
	},
	inject: ["reload"],
	data() {
		return {
			// personal information
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
			},
			recollectionForm: {
				new_name: '',
				collection_id: ''
			},
			collection_id: '',
			// collection
			books: [],       // current collection's books
			options: [],     // collections' content
			value: '',       // collection name
			collections: [], // result from api package\
			// create an new collection
			collectionform: {
				name: ''
			},
			
			// delecollectionform: {
			// 	collection_id: ''
			// },
			dialogFormVisible: false,
			dialogFormVisible2: false,
			
			formLabelWidth: '120px',
			// TODO: connect with backend, get all book images in this collections
			img_list: [
				{
					imageLink: require("../img/test book image/harry.jpg"),
					title: 'Harry Porter',
					url: ''  // TODO: fill the url
				},
			]
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
		},
		
		// check which collection is now selecting
		currentSel(selVal) {
			this.value = selVal;
			let obj = {}
			obj = this.options.find((item)=>{
				return item.value === selVal;
			});
			this.getCollectionBooks(obj.key)
			this.collection_id = obj.key
			this.recollectionForm.new_name = obj.value
			this.recollectionForm.collection_id = obj.key
		},
		getCollectionNames(res) {
			const len = res.length
			let option
			for(let i = 0; i < len; i++) {
				// 提取collections' name
				option = {}
				option["key"] = res[i].id
				option["value"] = res[i].name
				this.options.push(option)
			}
		},
		// get books from specific collection through collection id
		getCollectionBooks(col_id) {
			this.books = []  // refresh books' list
			console.log("now select: " + col_id)
		
			let obj = {}
			obj = this.collections.find((item) => {
				return item.id === col_id;
			});
		
			let book
			let len = obj.books.length
			for(let i = 0; i < len; i++) {
				book = {}
				book["id"] = obj.books[i].id
				book["title"] = obj.books[i].title
				book["imageLink"] = obj.books[i].imageLink
				book["url"] = ''   // TODO: 跳转url
				this.books.push(book)
			}
		},
		// create an new collection
		submit() {
			this.$refs.collectionformRef.validate(async valid => {
				if (!valid) { return }
				postnewcollection(this.collectionform).then(res=>{
					console.log(res);
					this.$message.success('Successfully created');
					this.dialogFormVisible = false;
					this.reload();
				}).catch(err=>{
					console.log(err);
					this.$message.error('Create failure');
				})
			})
		},
		// reset collection name
		change() {
			this.$refs.recollectionFormRef.validate(async valid => {
				if (!valid) { return }
				changecollectioname(this.recollectionForm).then(res=>{
					console.log(res);
					this.$message.success('Modify successfully');
					this.dialogFormVisible2 = false;
					this.reload();
				}).catch(err=>{
					console.log(err)
					this.$message.error('Modify failure');
				})
			})
		},
		
		//delete collection
		// open() {
		// 	delecollection(this.collection_id).then(res=>{
		// 		console.log(res);
		// 		this.$message.success('delete successfully');
		// 		//this.reload();
		// 	}).catch(err=>{
		// 		console.log(err)
		// 		this.$message.error('delete failure');
		// 	})
		// }
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
		}),
		getCollectionmultdata().then(res=>{
			//console.log(res)
			this.collections = res
			this.value = this.collections[0].name
			this.getCollectionNames(res)   // 把api返回的collection名字整理出来
			this.getCollectionBooks(this.collections[0].id) // default select first collection
			this.recollectionForm.new_name = this.collections[0].name
			this.recollectionForm.collection_id = this.collections[0].id
			this.collection_id = this.collections[0].id
		})
		.catch(error => {
			console.log(error)
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
		overflow: scroll;
	}
	.content{
		// height: 10000px;
		width: 90%;		
		border: 1px solid;
		margin: auto;
		// overflow: scroll;
	}
	// 个人资料
	.person_information{
		margin-left: 60px;
	}
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

	// collection	
	.clearfix{
		*zoom: 1;    /* 开启haslayout *只有在ie6,7下认识这个hack*/
	}
	.clearfix:after{
		content: "";
		display: block;
		clear: both;
	}
	.collection_head, .collection_add,.collection_reset, .collection_dele {
		margin-top: 10px;
		float: left;
	}
	.collection_add{
		margin-top: 10px;
	}
	.coll_wrap {
		margin-top: 30px;
		display: grid;
		grid-template-columns: repeat(5, 1fr);
	}
	.coll_content {
		margin: 10px 10px 10px 10px;
	}
	
	.img {
		width: 180px;
		height: 300px;
	}
	// add
	.collection_add_button{
		margin-top: 10px;
		margin-left: 80px;
	}
	// reset
	.collection_change_button{
		margin-top: 10px;
		margin-left: 90px;
	}
	.collection_dele_button{
		margin-top: 10px;
		margin-left: 100px;
	}
</style>
