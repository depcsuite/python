<template>
  <div>
    <h3 class="display-3">Productos</h3>
  <div id="alerta" class="alert alert-success" role="alert">
    A simple success alert—check it out!
  </div>
    <ul>
      <div class="row">
        <li v-for="item in datosProducto" :key="item.id">
          <div class="col-12 col-sm-12">
            <div class="card" style="width: 50rem">
              <div class="card-body">
                <h5 class="card-title">{{ item.nombre }}</h5>
                <p class="card-text">{{ item.descripcion }}</p>
                <p class="card-text">Precio: {{ item.precio }}</p>
                <span v-if="isLogged">
                  <span v-if="pedidoAbierto">
                    <button v-on:click="agregarAPedido(item.id)" class="btn btn-primary m-1" type="button">
                    Agregar a pedido
                  </button>
                  </span>
                </span>
              </div>
            </div>
          </div>
        </li>
      </div>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
export default {
  //////
  name: "Producto",
  data() {
    return {
      datosProducto: {},
    };
  },
  ///////
  methods: {
    getProductos() {
    var alerta = document.getElementById("alerta"); 
    alerta.style.display = 'none';
      axios({
        url: "http://127.0.0.1:8000/producto/",
        headers: {},
        method: "GET",
      }).then((response) => {
        this.datosProducto = response.data;
      });
    },
    agregarAPedido(idProducto) {
      axios({
        url: "http://127.0.0.1:8000/productopedido/agregar/",
        headers: { Authorization: "Token " + this.$store.getters.getToken },
        method: "POST",
        data: {idProd: idProducto, idPed: this.$store.getters.getIdPedidoAbierto},
      });
      var alerta = document.getElementById("alerta"); 
      alerta.style.display = 'block';
    }
  },
  mounted() {
    var alerta = document.getElementById("alerta"); 
    alerta.style.display = 'none';
    this.getProductos();
  },
  computed: {
    isLogged() {
      return this.$store.getters.getIsLog;
    },
    pedidoAbierto() {
      return (this.$store.getters.getIdPedidoAbierto != 0);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
