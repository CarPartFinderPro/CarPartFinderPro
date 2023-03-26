axios.defaults.baseURL = 'http://localhost:8000';
import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueSidebarMenuAkahon from "vue-sidebar-menu-akahon";

const app = createApp(App)

app.component('vue-sidebar-menu-akahon', VueSidebarMenuAkahon)

app.mount('#app')