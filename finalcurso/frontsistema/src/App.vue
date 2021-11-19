<template>
  <div id="app">
    <div class="container-fluid">
      <router-link to="/producto">Ver productos</router-link> |
      <router-link to="/pedido">Ver pedidos</router-link> |
      <router-link to="/">Home</router-link>
      <router-view />
      
      
      </div>
  </div>
</template>

<script>
export default {
  name: 'App',

}
</script>

