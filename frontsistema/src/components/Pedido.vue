<template>
  <div>
    <h3 class="display-3">Mis pedidos</h3>
    
    <ul>
      
        <li v-for="item in datosPedido" :key="item.id">    
          <div class="row">
            <div class="col-12 col-sm-12">    
            
            <b>Código:</b> {{ item.id }} | <b>Fecha:</b> {{item.fecha}} | <b>Total:</b> {{item.total}} 
            <span v-if="item.estado === 'A'">
                <button v-on:click="detalle" class="btn btn-danger m-1" type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
                Cerrar pedido
                </button> 
            </span>
            <span v-else-if="item.estado === 'P'">
                <button class="btn btn-warning m-1" type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample" disabled>
                Pendiente
                </button>
            </span>
            <span v-else-if="item.estado === 'V'">
                <button class="btn btn-outline-success m-1" type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample" disabled>
                En viaje
                </button>
            </span>
            <span v-else-if="item.estado === 'E'">
                <button class="btn btn-success m-1" type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample" disabled>
                Entregado
                </button>
            </span>
            <router-link class="nav-link active" to="/detallepedido/">
            <button class="btn btn-primary m-1" type="button" data-bs-toggle="collapse" data-bs-target="#detPedido">
            Ver detalle
            </button></router-link>
            <div class="collapse m-2" id="detPedido">
            <div class="card card-body">
             <ul>
               <li v-for="p in arrDetalles" :key="p.id">Producto: {{p.producto.nombre}} | Cantidad: {{p.cantidad}}</li>
             </ul>
            
            </div>
            </div>
            </div>
            
          </div>
      </li>
    
    </ul>
    
  </div>
</template>


<script>
import axios from "axios"
export default {
    //////
  name: 'Pedido',
  data() {
      return {
          datosPedido: {}, 
      };
  },
  ///////
  methods: {
      getPedidos() {
        axios({
              url: "http://127.0.0.1:8000/pedido/c/",
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
