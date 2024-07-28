import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'LogIn',
    component:  ()=>import('../views/LogIn')
  },
  {
    path: '/PersonalProject',
    name: 'PersonalProject',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/PersonalProject.vue')
  },
  // {
  //   path: '/LogIn',
  //   name: 'LogIn',
  //   component: ()=>import('../views/back/LogIn')
  // }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
