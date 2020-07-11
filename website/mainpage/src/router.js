import Vue from 'vue'
import Router from 'vue-router'
import login from './pages/login.vue'
import register from './pages/register.vue'
import homepage from './pages/homepage.vue'
import single_book from './pages/single_book'

Vue.use(Router)

const router = new Router({
    routes: [
        {
            path: '/',
            redirect: '/homepage',
            meta:{
                title:'homepage'
            }
        },
        {
            path: '/homepage',
            name: 'homepage',
            component: homepage,
            meta:{
                title:'homepage'
            }
        },
        {
            path: '/register',
            name: 'register',
            component: register,
            meta:{
                title:'register'
            }
        },
        {
            path: '/login',
            name: 'login',
            component: login,
            meta:{
                title:'login'
            }
        },
        {
            path: '/single_book',
            name: 'single_book',
            component: single_book,
            meta:{
                title:'single_book'
            }
        }
    ],

})


// 路由导航守卫
router.beforeEach((to, from, next) => {
    document.title=to.matched[0].meta.title
    // to 将要访问的路径
    // from 代表从那个路径跳转过来的
    // next 是一个函数，表示放行
    // next() 放行， next('/login') 强制跳转
    const tokenStr = window.sessionStorage.getItem('token')
    if (to.path === '/homepage' | to.path === '/login' | to.path === '/register'| to.path==='/single_book') { return next() }
    else if (tokenStr == null) {
        return next('/homepage')
    }
    else next()
})

export default router