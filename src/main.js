import { createApp } from 'vue'
import App from './App.vue'
import VueSidebarMenuAkahon from "vue-sidebar-menu-akahon";

const app = createApp(App)

app.component('vue-sidebar-menu-akahon', VueSidebarMenuAkahon)

app.mount('#app')