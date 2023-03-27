// Set the default base URL for all axios requests
axios.defaults.baseURL = 'http://localhost:8000';

// Import necessary modules
import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueSidebarMenuAkahon from "vue-sidebar-menu-akahon";

// Create a new Vue app
const app = createApp(App)

// Register the Vue sidebar menu component globally
app.component('vue-sidebar-menu-akahon', VueSidebarMenuAkahon)

// Mount the Vue app to the HTML element with the ID 'app'
app.mount('#app')