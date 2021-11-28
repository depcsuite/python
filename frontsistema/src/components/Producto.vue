<template>
  <div>
    <h3 class="display-3">Productos</h3>

    <ul>
    <div class="row">
      <li v-for="item in datosProducto" :key="item.id">
        
        <div class="col-12 col-sm-4">

            <div class="card" style="width: 18rem;">

              
              <div class="card-body">
                <h5 class="card-title">{{ item.nombre}}</h5>
                <p class="card-text">{{ item.descripcion }}</p>
                <p class="card-text">Precio: {{ item.precio }}</p>
                <span v-if="isLoggedIn"><router-link
                :to="{ name: 'detallepedidos', params: { id: item.id } }"
                ><a href="#" class="btn btn-success">Agregar a pedido</a></router-link></span>
              </div>
            </div>
        </div>
          
        
      </li>
      </div>
    </ul>
  </div>
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
