import { createWebHistory, createRouter } from 'vue-router';

const load = (component) => {
    return () => import(`../views/${component}.vue`)
}

const routes = [
    {
        path: '/',
        redirect: '/posts/1'
    },

    {
        path: '/posts/:id',
        name: 'Post',
        component: load('PostsView'),
    },

    {
        path: '/:pathMatch(.*)',
        name: 'NotFound',
        component: load('NotFound'),
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
