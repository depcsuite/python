<template>
    <div>
    <h1 class="display-1 text-center">Lista de pedidos</h1>
    <ul>
        <li v-for="prod in datosPedido" :key="prod.id">{{prod.fecha}}</li>
    </ul>
    </div>
</template>

<script>
import axios from "axios"
export default {
    //////
  name: 'Product',
  data() {
      return {
          datosPedido: {}, 
      };
  },
  ///////
  methods: {
      getPedidos() {
        axios({
              url: "http://127.0.0.1:8000/pedido/",
              headers: {Authorization: "Token " + this.$store.getters.getToken},
              method: "GET",
        }).then((response) => {
            this.datosPedido = response.data;
    


        });
      },
  },
  mounted() {
      this.getPedidos();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
