import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Register from '../views/Register.vue'
import Login from '../views/Login.vue'
import Upload from '../views/Upload.vue'
import History from  '../views/History.vue'
import Recognition from '../components/Recognition.vue'
import Result from '../views/Result.vue'

Vue.use(VueRouter)

const routes = [
  // {
  //   path:'/*',
  //   redirect:'/'
  // },
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/Register',
    name: 'Register',
    component: Register
  },
  {
    path: '/Login',
    name: 'Login',
    component: Login
  },
  {
    path: '/Upload',
    name: 'Upload',
    component: Upload
  },
  {
    path:'/History',
    name:'History',
    component:History
  },
  {
    path:'/History/:id',
    name:'recognition',
    props:true,
    component:Recognition
  },
  {
    path:'/Result',
    name:'result',
    component:Result
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path:'/*',
    redirect:'/Login'
  },
]

const router = new VueRouter({
  mode:'history',
  base: process.env.BASE_URL,
  routes,
  // base:'dist'
})

export default router
