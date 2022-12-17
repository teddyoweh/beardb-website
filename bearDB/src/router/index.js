import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SupportView from '../views/Support.vue'
import Credits from '../views/Credits.vue'
const router = createRouter({
    history: createWebHistory(
        import.meta.env.BASE_URL),
    routes: [{
            path: '/',
            name: 'home',
            component: HomeView
        },
        {
            path: '/support',
            name: 'support',
            component: SupportView
        },
        {
            path: '/credits',
            name: 'credits',
            component: Credits}



    ]
})

export default router