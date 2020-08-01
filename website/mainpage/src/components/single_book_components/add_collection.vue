<template>
	<div>
		<el-button type="primary" @click="dialogVisible = true" icon="el-icon-circle-plus-outline">Add to collection</el-button>
		<!--		pop up a dialog-->
		<el-dialog
						title="Add this book to your collection"
						:visible.sync="dialogVisible"
						width="30%">

			<!--choose one of your collections-->
			<el-select  class="all_margin" v-model="value"  placeholder="please choose one"  >
				<el-option

								v-for="item in options"
								:key="item.id"
								:label="item.name"
								:value="item.id"
								:disabled="item.disabled">
				</el-option>


			</el-select>
			<!--	add a new collection Button-add -->
			<div class="all_margin" >
				<span>want to add a new collection:</span>
				<el-button @click="isShow=!isShow" style="margin-left: 20px; font-size: 10px;" type="primary" icon="el-icon-circle-plus-outline"></el-button>
			</div>
			<!--	add a new collection click button-add and show below -->
			<div class="all_margin" v-show="isShow">
				<span>Name:</span>
				<el-input   style="width: 40%; margin: 0 15px"  v-model="input" placeholder="please add a shelf"></el-input>
				<el-button type="primary" :plain="true" @click="add_new_shelf" >Add</el-button>

			</div>

			<!-- close the dialog-->
			<span slot="footer">
        <el-button @click="dialogVisible = false">cancel</el-button>
				<!--	submit the action if click submit-->
        <el-button type="primary" @click="add_to_collection(value)">submit</el-button>
      </span>
		</el-dialog>

	</div>
</template>

<script>
// import {addCollection,getCollectionmultdata,Add2Collection} from "../../network/requests"

import {Add2Collection, addCollection, getCollectionmultdata} from '../../network/requests'

export default {
	name: 'add_collection',
	data () {
		return {
			token_log: localStorage.getItem('token'),
			dialogVisible:false,
			isShow:false,
			flag:false,

			img:[],
			input:'',
			options:[],
			value: '',
		}
	},
	props:{
		bookID: String,
		book_name:String
	},
	components:{

	},
	created () {
		if(this.token_log){
			getCollectionmultdata().then(res=>{
				console.log(res)
				console.log(this.book_name)

				for (let i=0;i<res.length;i++){
					let j=res[i].id
					let k=res[i].name
					let books=res[i].books
					let len=res[i].books.length
					// check the book in collection or not
					for(let j=0;j<len;j++){
						console.log(books[j].id)
						if (this.book_name===books[j].id){
							this.flag=true
							break
						}
					}
					console.log(k)
					//if that book already in collection u cannot choose it
					if (this.flag===true){
						this.options.push({id:j,name:k, disabled: true}) //get all name of collections
					}
					//otherwise u can choose it
					else{
						this.options.push({id:j,name:k, disabled: false}) //get all name of collections
					}
					//reset the flag
					this.flag=false
				}
			}).catch(res=>{
				console.log(res)
			})

		}
	},
	methods:{
		//add a new collection
		add_new_shelf () {
			let value = {name: this.input}
			let exist = false
			for (let i = 0; i < this.options.length; i++) {
				//check the added name whether exist the collection list, if exist === false then add the name
				if (value.name === this.options[i].name) {
					exist = true
				}
			}
			if (exist === false) {
				addCollection(value).then(res => {
					console.log(res)
				}).catch(res => {
					console.log(res)
				})
				// refresh the options
				getCollectionmultdata().then(res => {
					this.list=[]
					for (let i=0;i<res.length;i++){
						let j=res[i].id
						let k=res[i].name
						this.list.push(Object.assign([{}],this.options,{
							id:j,
							name:k
						}))
						this.$nextTick().then(() => {
							this.options = this.list;
						});

					}


				})
				this.$message({
					message: 'Congratulations, You have added a shelf',
					type: 'success'
				});

			}
			// if collection name already exist in collections ,send message
			else {
				this.$message({
					message: 'collection name already exist',
					type: 'success'
				});
			}


			// get all collection names in your account
			getCollectionmultdata().then(res=>{
				this.options=[]
				for (let i=0;i<res.length;i++){
					let j=res[i].id
					let k=res[i].name
					this.options.push({id:j,name:k})
				}
			}).catch(res=>{
				console.log(res)
			})
		},

		// add a book into the currently choosing collection
		add_to_collection(value){
			console.log(value)
			let postvalue={collection_id:value,book_id:this.bookID}
			console.log(postvalue)
			Add2Collection(postvalue).then(res=>{
				console.log(res)
				this.dialogVisible=false
			}).catch(res=>{
				console.log(res)
			})
		}
	}
}
</script>

<style scoped>
	.all_margin{
		padding: 10px 10px;
	}
	/deep/ .el-dialog__body{
		padding: 0 10px;
		color: #606266;
		font-size: 14px;
		word-break: break-all;
	}
	/deep/ .el-dialog__footer{
		margin-top: 40px;

	}
</style>