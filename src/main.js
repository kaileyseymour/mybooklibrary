import './assets/main.css'

import { createApp } from 'vue'
import router from './router.js'
import App from './App.vue'

import '@fortawesome/fontawesome-free/css/all.css'
import '@fortawesome/fontawesome-free/js/all.js'

const app = createApp(App)
app.use(router)
app.mount('#app')
