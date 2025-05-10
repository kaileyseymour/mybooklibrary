import './assets/main.css'

import { createApp } from 'vue'
import router from './router'
import App from './App.vue'
import BookCard from './components/bookCard.vue'

const app = createApp(App)
app.use(router)
app.component('BookCard',BookCard)
app.mount('#app')
