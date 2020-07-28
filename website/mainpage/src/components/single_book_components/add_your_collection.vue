<style lang="less" scoped>
	.all_margin{
		margin: 10px 10px;
	}

</style>
<template>
	<div class="add">
		<div>

		</div>
		<el-button @click="loginfirst()" type="primary" style="margin-left: 16px;">
			Add to collection
		</el-button>

		<el-drawer
						:wrapperClosable=this.wrapperClosable
						title="I am title"

						:visible.sync="drawer"
						:with-header="false">
			<h3 class="all_margin">Add to your collection</h3>

			<span class="all_margin">Add to: </span>
			<el-select  class="all_margin" v-model="value"  placeholder="please choose one"  >
				<el-option

								v-for="item in options"
								:key="item.id"
								:label="item.name"
								:value="item.id">
				</el-option>


			</el-select>

			<el-button  type="primary" @click="choose_collection(value)" >Confirm</el-button>


			<p style="border-bottom: solid 1px gray;width: 93%; margin: 15px auto" ></p>
			<div class="all_margin" >
				<span>Add a Shelf:</span>
				<el-button @click="isShow=!isShow" style="margin-left: 20px; font-size: 15px;" type="primary" icon="el-icon-circle-plus-outline"></el-button>

			</div>
			<div class="all_margin" v-show="isShow">
				<span>Name:</span>
				<el-input   style="width: 40%; margin: 0 15px"  v-model="input" placeholder="please add a shelf"></el-input>

				<el-button type="primary" :plain="true" @click="add_new_shelf" >Add</el-button>


			</div>




		</el-drawer>

	</div>

</template>

<script>
import {addCollection,getCollectionmultdata,Add2Collection} from "../../network/requests"
export default {
	name: 'add_your_collection',
	data () {
		return {
			token_log: localStorage.getItem('token'),

			wrapperClosable:true,
			drawer: false,
			img:[],
			isShow:false,
			input:'',
			options:[],

			value: '',

			// label:''
		}
	},
	props:{
		bookID: String
	},
	components:{

	},


	created () {
		if(this.token_log){
			getCollectionmultdata().then(res=>{
				console.log(res)

				for (let i=0;i<res.length;i++){
					let j=res[i].id
					let k=res[i].name
					this.options.push({id:j,name:k})
				}
				// console.log(this.options)

			}).catch(res=>{
				console.log(res)
			})

		}



	},

	methods: {
		Close_drawer(){
			this.drawer=false
		},
		loginfirst(){
			if(this.token_log){
				this.drawer = true;

			}else{
				this.$message({message: 'please login', showClose: true,})
				return false
			}
		},
		add_new_shelf () {
			let value = {name: this.input}
			let exist = false
			for (let i = 0; i < this.options.length; i++) {
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
				getCollectionmultdata().then(res => {
					this.list=[]
					for (let i=0;i<res.length;i++){
						let j=res[i].id
						let k=res[i].name
						// let val1={id:j}
						// let val2={name:k}
						// this.list.push({id:j,name:k})
						this.list.push(Object.assign([{}],this.options,{
							id:j,
							name:k
						}))
						this.$nextTick().then(() => {
							this.options = this.list;
						});
						// console.log(this.options)

					}

				})
				// this.$set(this.options,val1,val2)


			}
			// console.log(this.options)

			this.$message({
				message: 'Congratulations, You have added a shelf',
				type: 'success'
			});
			getCollectionmultdata().then(res=>{
				console.log(res)
				this.options=[]

				for (let i=0;i<res.length;i++){
					let j=res[i].id
					let k=res[i].name
					this.options.push({id:j,name:k})
				}

				// console.log(this.options)

			}).catch(res=>{
				console.log(res)
			})



		},

		choose_collection(value){

			// console.log("book_id"+this.bookID,"collection_id"+value)
			let postvalue={collection_id:value,book_id:this.bookID}
			// console.log(postvalue)

			Add2Collection(postvalue).then(res=>{
				console.log(res)
			}).catch(res=>{
				console.log(res)
			})
			this.drawer=false

		}
	},


}
</script>

