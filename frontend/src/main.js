import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:8000'
const app = createApp(App)
app.use(router)
app.config.globalProperties.$http = axios
app.mount('#app')
// createApp(App).use(router).mount('#app')

// import { createApp } from 'vue'
// import App from './App.vue'
// import router from './router'



