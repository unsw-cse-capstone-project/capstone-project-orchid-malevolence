<template>
  <div class="wrap_login">
    <el-form ref="loginFormRef" :model="loginForm" :label-position="labelPosition" label-width="80px" class="register_form">
      <!-- 表头字体 -->
      <div class="register_title_wrap">
        <div class="register_title">Login</div>
      </div>
      <!-- 用户名 -->
      <el-form-item label="Username" prop="username">
        <el-input v-model="loginForm.username" placeholder="username" prefix-icon="iconfont icon-user"></el-input>
      </el-form-item>
      <!-- 密码 -->
      <el-form-item label="Password" prop="password">
        <el-input type="password" v-model="loginForm.password" placeholder="password" prefix-icon="iconfont icon-lock">
        </el-input>
      </el-form-item>
      <!-- 按钮 -->
      <el-form-item class="btns">
          <el-button type="primary" @click="login">Login</el-button>
      </el-form-item>
      <div class="other">
        No account number? <router-link to='/register'>register</router-link>
      </div>
    </el-form>

  </div>
</template>

<script>
//在vuex中mutations是专门用来修改state中属性状态的方法集合（对象）
// import { mapMutations } from 'vuex';
export default {
  data () {
    return {
      labelPosition: 'left',
      loginForm: {
        username: '',
        password: ''
      }
    };
  },
  methods: {
    // ...mapMutations(['changeLogin']),
    login () {
		this.$refs.loginFormRef.validate(async valid => {
			if(!valid){
				return
			}
        // let _this = this;
		if (this.loginForm.username === '' || this.loginForm.password === '') {
			this.$message.warning('The account or password cannot be empty')
		} else {
			this.$axios({
				method: 'post',
				url: 'http://127.0.0.1:8000/api/login/',
				data: this.loginForm
			}).then(res => {
            // console.log(res.data.msg);
				if(res.status === 400){
					this.$message.error('fail to login')
				}else if(res.status === 200){
					console.log(res.data.token);
					window.localStorage.setItem('token', res.data.token)
					this.$message.success('login successfully')
					this.$router.push('/')
				}
			})
		}
		})
	}
  }
}
</script>

<style lang="less" scoped>
body, html{
  height: 100%;
  overflow: hidden;
}
.wrap_login{
  position: absolute;
  // background-color: deeppink;
  background: url(../assets/background_login.jpg) no-repeat fixed;
  background-size: cover;
  background-origin: border-box;
  height: 100%;
  width: 100%;
}
// 注册列表的布局
.el-form{
  position: absolute;
  top: 50%;
  margin-top: -293px;
  right: 100px;
  // background: url("../img/frame.png") no-repeat;
  width: 590px;
  height: 586px;
  // border: 1px solid;
  // background-color: rgba(0,0,0,.3);
  background-image: repeating-linear-gradient(135deg,rgba(0,0,0,0.05),rgba(225,169,131,.5));
  border-radius: 30px;
}

// title 居中+字体
.register_title{
  text-align: center;
  font: 34px/168px bolder sans-serif;
}
// 每个单列表的处理
.el-form-item{
  height: 62.5px;
  margin-left: 30px;
}
// 修改输入框的长度
.el-input{
  width: 300px;
}
.other{
  text-align: center;
  font: bolder;
}
</style>
