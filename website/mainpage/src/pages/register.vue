<template>
  <div class="wrap">
    <el-form ref="RegisterFormRef" :model="RegisterForm" :rules="RegisterFormRules" :label-position="labelPosition" label-width="80px" class="register_form">
      <!-- 表头字体 -->
      <div class="register_title_wrap">
        <div class="register_title">Register</div>
      </div>
      <!-- 用户名 -->
      <el-form-item label="Username" prop="username">
        <el-input v-model="RegisterForm.username" placeholder="username" prefix-icon="iconfont icon-user"></el-input>
      </el-form-item>
      <!-- 邮箱 -->
      <el-form-item label="Email" prop="email">
        <el-input type="email" v-model="RegisterForm.email" placeholder="e-mail" prefix-icon="iconfont icon-email"></el-input>
      </el-form-item>
      <!-- 密码 -->
      <el-form-item label="Password" prop="password">
        <el-input type="password" v-model="RegisterForm.password" placeholder="password" prefix-icon="iconfont icon-lock"></el-input>
      </el-form-item>
      <!-- 确认密码 -->
      <el-form-item label="CheckPass" prop="checkpass">
        <el-input type="password" v-model="RegisterForm.checkpass" placeholder="confirm password" prefix-icon="iconfont icon-lock"></el-input>
      </el-form-item>
      <!-- 按钮 -->
      <el-form-item class="btns">
          <el-button type="primary" @click="register('RegisterForm')">Register</el-button>
          <el-button type="info" @click="formreset">Reset</el-button>
      </el-form-item>
      <div class="other">
        An existing account? <router-link to='/login'>login</router-link>
      </div>
    </el-form>
  </div>
</template>


<script>
  export default {
    data () {
      // 验证邮箱格式是否正确
      var checkEmail = (rule, value, callback) => {
        const mailReg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/
        if (!value) {
          return callback(new Error('Please enter email address'))
        }
        setTimeout(() => {
          if (mailReg.test(value)) {
            callback()
          } else {
            callback(new Error('Incorrect email format'))
          }
        }, 100)
      }
      // 验证密码
      let validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('Please enter your password.'))
        } else {
          if (this.RegisterForm.checkpass !== '') {
            this.$refs.RegisterFormRef.validateField('checkpass')
          }
          callback()
        }
      }
      // 二次验证密码
      let validatePass2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('Please enter your password again'))
        } else if (value !== this.RegisterForm.password) {
          callback(new Error('The password is inconsistent!'))
        } else {
          callback()
        }
      }
      return {
        labelPosition: 'left',
        // v-model绑定对象
        RegisterForm: {
          username: '',
          password: '',
          checkpass: '',
          email: ''
        },
        // 注册表单验证规则
        RegisterFormRules: {
          // 用户名验证
          username: [
            { required: true, message: 'Please enter the username', trigger: 'blur' },
            { min: 3, max: 10, message: 'The length is between 3 and 10 characters', trigger: 'blur' }
          ],
          password: [
            { required: true, validator: validatePass, trigger: 'blur' },
            { min: 6, max: 10, message: 'The length is between 6 and 10 characters', trigger: 'blur' }
          ],
          checkpass: [
            { required: true, validator: validatePass2, trigger: 'blur' }
          ],
          email: [
            { required: true, validator: checkEmail, trigger: 'blur' }
          ]
        }
      }
    },
    methods: {
      formreset() {
              this.$refs.RegisterFormRef.resetFields()
      },
      register() {
        this.$refs.RegisterFormRef.validate(valid => {
          if(!valid){
            return
          }
          this.$axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/api/register/',
            data: this.RegisterForm
          }).then(res => {
            console.log(res);
            if(res.status !== 200){
              console.log(res.data.msg);
              this.$message.error('Registered failure');
            }else if(res.status == 200){
              // window.sessionStorage.setItem('token', res.data.token)
              // this.$router.push('/login');
              console.log(res.data.msg);
              // alert('注册成功');
              this.$message.success('Registered successfully');
              this.$router.push('/login');
            }
          })
        })
      }
    }
  }
</script>

<!-- Add "scoped" attribu
te to limit CSS to this component only -->
<style lang="less" scoped>
body, html{
  height: 100%;
  overflow: hidden;
}
.wrap{
  position: absolute;
  // background-color: deeppink;
  background: url(../assets/background_register.jpg) no-repeat fixed;
  background-size: cover;
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
  background-image: repeating-linear-gradient(135deg,rgba(0,0,0,0.1),rgba(167,178,222,.5));
  border-radius: 30px;
}

// title 居中+字体
.register_title{
  text-align: center;
  font: 34px/98px bolder sans-serif;
}
// 每个单列表的处理
.el-form-item{
  height: 53px;
  margin-left: 30px;
  margin-top: 10px;
}
// 修改输入框的长度
.el-input{
  width: 300px;
}
.other{
  text-align: center;
  font: bolder;
}
label{
  font: 16px bolder;
}
</style>
