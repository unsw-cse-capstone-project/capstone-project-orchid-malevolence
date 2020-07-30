import Vue from 'vue'
import Router from 'vue-router'
import login from './pages/login.vue'
import register from './pages/register.vue'
import homepage from './pages/homepage.vue'
import search_result from './pages/search_result'
import person from './pages/person.vue'
import one_book from './pages/one_book'
import my_bookspage from './pages/my_bookspage'
import recommendation from './pages/recommendation'
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
			path: '/person',
			name: 'person',
			component: person,
			meta:{
				title:'personal information'
			}
		},
        {
            path: '/one_book',
            name: 'one_book',
            component: one_book,
            meta:{
                title:'one_book'
		}
        },
        {
            path: '/search_result',
            name: 'search_result',
            component: search_result,
            meta:{
                title:'search_result'
            }
        },
        {
            path: '/my_bookspage',
            name: 'my_bookspage',
            component: my_bookspage,
            meta:{
                title:'my_bookspage'
            }
        },
        {
            path: '/recommendation',
            name: 'recommendation',
            component: recommendation,
            meta:{
                title:'recommendation'
            }
        },

    ],

})


// 路由导航守卫
router.beforeEach((to, from, next) => {
    document.title=to.matched[0].meta.title
    // to 将要访问的路径
    // from 代表从那个路径跳转过来的
    // next 是一个函数，表示放行
    // next() 放行， next('/login') 强制跳转
    const tokenStr = window.localStorage.getItem('token')
    if (to.path === '/homepage' | to.path === '/login' |
        to.path === '/register'| to.path==='/one_book' | to.path==='/search_result' |
        to.path==='/my_bookspage' | to.path === '/recommendation') { return next() }
    else if (tokenStr == null) {
        return next('/homepage')
    }
    else next()
})

export default router