import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
    history: createWebHistory(
        import.meta.env.BASE_URL),
    routes: [{
            path: '/',
            name: 'home',
            component: HomeView
        },
        {
            path: '/about',
            name: 'about',

            component: () =>
                import ('../views/AboutView.vue')
        },
        {
            path: '/app',
            name: 'app',

            component: () =>
                import ('../views/DashboardView.vue')
        },
        {
            path: '/auth',
            name: 'auth',

            component: () =>
                import ('../views/AuthView.vue')
        }, {
            path: '/app/:project',
            name: 'project',
            props: { project: ':project' },

            component: () =>
                import ('../views/AppView.vue')
        }



    ]
})

export default router