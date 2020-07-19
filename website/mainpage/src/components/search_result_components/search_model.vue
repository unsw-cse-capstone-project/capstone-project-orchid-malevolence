<template>
	<el-menu :default-active="activeIndex2" class="el-menu-main" mode="horizontal" @select="handleSelect" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
		<!--    主页跳转    -->
		<el-menu-item index="1" @click="jump_homepage">
			Home
		</el-menu-item>

		<!--        <Search></Search>-->

		<div class="search">
			<el-input placeholder="input contents" v-model="input3" class="input-with-select">
				<el-select v-model="select" slot="prepend" placeholder="please select">
					<el-option  label="Title" value="Title" ></el-option>
					<el-option label="Authors" value="Authors" ></el-option>
					<!--                    <el-option label="My Book" value="3"></el-option>-->
				</el-select>
				<el-button slot="append" icon="el-icon-search" @click="jump_search_result"></el-button>
			</el-input>
		</div>

		<!--    注册跳转    -->
		<el-menu-item index="2" style="float:right" @click="jump_reg" v-if="token_log == null">
			Register
		</el-menu-item>

		<!--    登录跳转    -->
		<el-menu-item index="3" style="float:right" @click="jump_login" v-if="token_log == null">
			Login
		</el-menu-item>

		<el-menu-item index="4" style="float:right" @click="jump_logout" v-if="token_log != null">
			Logout
		</el-menu-item>

		<!-- TODO: complete jump to the profile page ||@click="jump_profile"|| -->
		<el-menu-item index="5" style="float:right" v-if="token_log != null">
			My Profile
		</el-menu-item>

		<!--    TODO: LOGO Search    -->
	</el-menu>
</template>

<script>
export default {
	name: 'search_model',
	data() {
		return {
			token_log: sessionStorage.getItem('token'),
			activeIndex: '1',
			activeIndex2: '1',
			input1: '',
			input2: '',
			input3: '',
			select: '',

		};
	},

	methods: {
		handleSelect(key, keyPath) {
			console.log(key, keyPath);
		},

		jump_homepage() {
			this.$router.push('home')
		},

		jump_reg() {
			this.$router.push('register')
		},

		jump_login() {
			this.$router.push('login')
		},

		jump_logout() {
			window.sessionStorage.clear()
			this.$router.go(0)
		},

		jump_search_result(){

			this.$emit('childfromheader',this.input3,this.select)

		}
	}
}
</script>


<style lang="less" scoped>
	.el-menu-main {
		position: relative;

	}

	.search {
		position: absolute;
		width: 300px;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
	}

	.el-select .el-input {
		width: 130px;
	}
	.input-with-select .el-input-group__prepend {
		background-color: #fff;
	}
</style>