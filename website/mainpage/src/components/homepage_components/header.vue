<template>
    <el-menu :default-active="activeIndex2" class="el-menu-main" mode="horizontal" @select="handleSelect" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
        <!--    主页跳转    -->
        <el-menu-item index="1" @click="jump_homepage">
            Home
        </el-menu-item>

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

        <!--    TODO: LOGO    -->
    </el-menu>
</template>

<script >
    export default {
        data() {
            return {
                token_log: sessionStorage.getItem('token'),
                activeIndex: '1',
                activeIndex2: '1'
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
            }
        }
    }
</script>

