import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Layout from './views/layouts/Layout.vue'
import Register from './views/Register.vue'
import Login from './views/Login.vue'

import store from './store'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'layout',
      component: Layout,
      children: [
        {
          path: '/',
          name: 'home',
          component: Home,
          beforeEnter(to, from, next){
            if (store.getters.isAuthenticated){
              next()
            } else {
              next("/login")
            }
          }
        }
      ]
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue'),
      beforeEnter(to, from, next){
        if (store.getters.isAuthenticated){
          next()
        } else {
          next("/login")
        }
      }
    }
  ]
})
