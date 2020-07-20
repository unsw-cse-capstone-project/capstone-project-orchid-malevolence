import Vue from 'vue'
import App from './App'
import ElementUI from 'element-ui' //element-ui的全部组件
import 'element-ui/lib/theme-chalk/index.css'//element-ui的css
import router from './router'
import {Message} from 'element-ui'
import axios from 'axios' ;
import Vuex from 'vuex' //引入状态管理
import 'jquery'
import 'popper.js'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'
Vue.prototype.$axios= axios ;
Vue.use(Vuex) ;
Vue.prototype.$message = Message
Vue.use(ElementUI) //使用elementUI
Vue.config.productionTip = false

axios.defaults.baseURL = 'http://127.0.0.1:8000/'
//请求拦截器
axios.interceptors.request.use(config => {
  // 在发送请求前做些什么
  // console.log(config)
  if (window.localStorage.getItem('token')) {
    config.headers.Authorization = window.localStorage.getItem('token')
  }
  return config
},
error => {
  return Promise.reject(error);
});

// 响应拦截器
axios.interceptors.response.use(res => {
  // 在请求成功后的数据处理
  return res
}, err=>{
  // 在响应错误的时候的逻辑处理
  return Promise.reject(err.response)
})

new Vue({
  el: '#app',
  router,

  components: { App },
  template: '<App/>',
  render: h => h(App),
}).$mount('#app')
