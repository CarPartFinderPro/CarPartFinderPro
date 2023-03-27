import Vue from 'vue' // import the Vue library
import VueRouter from 'vue-router' // import the Vue Router library
import CarPartList from '../components/CarPartList.vue' // import the CarPartList component
import CarPartDetails from '../components/CarPartDetails.vue'

Vue.use(VueRouter) // tell Vue to use the Vue Router library

const routes = [ // define the routes
  {
    path: '/car_parts', // the URL path
    name: 'CarPartList', // the name of the route
    component: CarPartList // the component to render when the route is accessed
  },
  {
    path: '/car_parts/:id',
    name: 'CarPartDetails',
    component: CarPartDetails,
    props: true
  }
]

const router = new VueRouter({ // create a new instance of Vue Router
  mode: 'history', // enable history mode (no hash in URL)
  base: process.env.BASE_URL, // set the base URL
  routes // pass in the routes we defined earlier
})

export default router // export the router so we can use it elsewhere in our application
