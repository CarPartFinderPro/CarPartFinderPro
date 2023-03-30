// import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'

// const routes = [
//   {
//     path: '/',
//     name: 'home',
//     component: HomeView
//   },
//   {
//     path: '/about',
//     name: 'about',
//     // route level code-splitting
//     // this generates a separate chunk (about.[hash].js) for this route
//     // which is lazy-loaded when the route is visited.
//     component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
//   }
// ]

// const router = createRouter({
//   history: createWebHistory(process.env.BASE_URL),
//   routes
// })

// export default router

import { createRouter, createWebHistory } from 'vue-router'
import CarPartList from '../components/CarPartList.vue'
import CarPartDetails from '../components/CarPartDetails.vue'
import UserComponent from '../components/UserComponent.vue'

const routes = [
  {
    path: '/',
    name: 'CarPartList',
    component: CarPartList
  },
  {
    path: '/uzytkownik',
    name: 'UserComponent',
    component: UserComponent
  },
  {
    path: '/car_parts/:id',
    name: 'CarPartDetails',
    component: CarPartDetails,
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
