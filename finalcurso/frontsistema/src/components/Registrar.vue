<template>
<div>
    <h1 class="display-1 text-center">Registro de nuevo usuario</h1>
    <form class="form-group" @submit.prevent="registrar">
        <label>Nombre:</label>
        <input type="text" class="form-control" required v-model="username" placeholder="Username">
        <label>Password:</label>
        <input type="password" class="form-control" required v-model="password" placeholder="Password">
        <label>Email:</label>
        <input type="text" class="form-control" required v-model="email" placeholder="Email">
        <button class="form-control" type="submit">Registrarme</button>
    </form>
</div>
</template>

<script>
import axios from "axios"
export default {
    //////
  name: 'Registrar',
  data() {
      return {
          username: "",
          password: "",
          email: "" 
      }
  },
  ///////
  methods: {
      registrar() {
        axios({
              url: 'http://127.0.0.1:8000/auth/users/',
              data: {username: this.username, email: this.email, password: this.password},
              method: 'POST'
        }).then((response) => {
            console.log(response.data);
            this.$router.push('/')
        });
      },
  },
  mounted() {
      //
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
