import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Login from '@/views/LoginBar.vue'
import Register from '@/views/RegisterBar.vue'
import Home from '@/views/HomeBar.vue'
import Tournament from '@/views/TournamentBar.vue'
import Tournament1 from '@/views/TournamentList.vue'
import Tournament2 from '@/views/TournamentRegis.vue'
import Data from '@/views/PlayerData.vue'
import tournamentdata from "@/views/TournamentData.vue";

const routes: Array<RouteRecordRaw> = [
  { path: '/', redirect: '/login',},
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/index', component: Home },
  { path: '/tournament', component: Tournament},
  {path: '/tournamentlist', component: Tournament1},
  {path: '/tournamentregis', component: Tournament2},
  {path: '/playerdata', component: Data},
  {path: '/tournamentdata', component: tournamentdata}
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
