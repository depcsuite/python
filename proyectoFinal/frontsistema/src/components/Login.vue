<template>
<div>
    <h1 class="display-1 text-center">Login</h1>
    <form class="form-group" @submit.prevent="loguear">
        <label>Nombre:</label>
        <input type="text" class="form-control" required v-model="username" placeholder="Username">
        <label>Password:</label>
        <input type="password" class="form-control" required v-model="password" placeholder="Password">
        <button class="form-control" type="submit">Login</button>
    </form>
</div>
</template>

<script>
import axios from "axios"
export default {
    //////
  name: 'Login',
  data() {
      return {
          username: "",
          password: "",
      }
  },
  ///////
  methods: {
      loguear() {
        axios({
              url: 'http://127.0.0.1:8000/auth/token/login/',
              data: {username: this.username, password: this.password},
              method: 'POST'
        }).then((response) => {
            //console.log(response.data);
            this.$store.commit(
                "logUser",
                response.data.auth_token,
                response.data.id
            );
            this.$router.push('/');
        });
      },
  },
  mounted() {
      //
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
