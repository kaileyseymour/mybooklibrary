import { createWebHistory, createRouter } from 'vue-router'

import HomeView from './components/home.vue'
import BookView from './components/book.vue'

const routes = [
  { path: '/', component: HomeView},
  { path: '/books', component: HomeView}, 
  { path: '/books/:isbn', component: BookView, props: true}
]

const router = createRouter({
  history: createWebHistory(),
  headers: {"Access-Control-Allow-Origin": "*"},
  routes,
})

export default router