import { createMemoryHistory, createRouter } from 'vue-router'

import HomeView from './components/home.vue'

const routes = [
  { path: '/books', component: HomeView },
]

const router = createRouter({
  history: createMemoryHistory(),
  headers: {"Access-Control-Allow-Origin": "*"},
  routes,
})

export default router