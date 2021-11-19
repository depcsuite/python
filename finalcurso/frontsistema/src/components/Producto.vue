<template>

    <h1 class="display-1 text-center">Lista de productos</h1>
    <ul>
        <li v-for="prod in datosProducto" :key="prod.id">{{prod.nombre}}</li>
    </ul>

</template>

<script>
import axios from "axios"
export default {
    //////
  name: 'Producto',
  data() {
      return {
          datosProducto: {}, 
      };
  },
  ///////
  methods: {
      getProductos() {
        axios({
              url: "http://127.0.0.1:8000/producto/",
              headers: {},
              method: "GET",
        }).then((response) => {
            this.datosProducto = response.data;
        });
      },
  },
  mounted() {
      this.getProductos();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
