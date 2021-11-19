import {createRouter, createWebHistory} from 'vue-router'
import Index from './components/Index.vue'
import Producto from './components/Producto.vue'
import Pedido from './components/Pedido.vue'
export const router = createRouter ({
    history: createWebHistory(),
    routes: [
        {path: '/', name: 'Index', component: Index},
        {path: '/producto', name: 'Producto', component: Producto},
        {path: '/pedido', name: 'Pedido', component: Pedido}





    ],





})