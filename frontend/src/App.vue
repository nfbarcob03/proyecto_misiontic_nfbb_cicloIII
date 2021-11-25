<template>
  <div id="app" class="app">

    <div class="header">

      <h1> Banco Mision TIC </h1>
      <nav>
        <button v-if="is_auth" v-on:click="loadHome"> Inicio </button>
        <button v-if="is_auth" v-on:click="loadAccount"> Cuenta </button>
        <button v-if="is_auth" v-on:click="logOut"> Cerrar Sesión </button>
        <button v-if="!is_auth" v-on:click="loadLogIn" > Iniciar Sesión </button>
        <button v-if="!is_auth" v-on:click="loadSignUp" > Registrarse </button>
        <button v-if="is_auth" v-on:click="loadCrearInmueble"> Crear Inmueble </button>
        <button v-if="is_auth" v-on:click="verInmuebles"> Ver inmuebles </button>
      </nav>
    </div>
    

    <div class="main-component">
      <router-view
      v-on:completedLogIn="completedLogIn"
      v-on:completedSignUp="completedSignUp"
      v-on:logOut="logOut"
      >
      </router-view>
    </div>
    

    <div class="footer">
      <h2>Misión TIC 2022</h2>
    </div>

  </div>
</template>




<script>
import jwt_decode from "jwt-decode";
import axios from "axios"
export default {
  name: 'App',

  data: function(){
      return{
        is_auth: false
      }
  },

  components: {
  },

  methods:{
    verifyAuth: function() {
this.is_auth = localStorage.getItem("isAuth") || false;
if (this.is_auth == false)
this.$router.push({ name: "logIn" });
else
this.$router.push({ name: "home" });
},

    loadLogIn: function(){
      this.$router.push({name: "logIn"})
    },

    loadSignUp: function(){
      this.$router.push({name: "signUp"})
    },

   completedLogIn: function(data) {
     debugger
localStorage.setItem("isAuth", true);
localStorage.setItem("username", data.username);
localStorage.setItem("token_access", data.token_access);
localStorage.setItem("token_refresh", data.token_refresh);

if (
  localStorage.getItem("token_access") === null ||
  localStorage.getItem("token_refresh") === null
) {
  this.$emit("logOut");
  return;
}

let token = localStorage.getItem("token_access");
let userId = jwt_decode(token).user_id.toString();
localStorage.setItem("userId", userId);

alert("Autenticación Exitosa");
this.verifyAuth();
},

   completedSignUp: function(data) {
alert("Registro Exitoso");
this.completedLogIn(data);
},

loadHome: function() {
this.$router.push({ name: "home" });
},

loadCrearInmueble: function(){
  this.$router.push({ name: "CrearInmueble" });
},

verInmuebles:function(){
  this.$router.push({ name: "VerInmuebles" });
},

logOut: function () {
localStorage.clear();
alert("Sesión Cerrada");
this.verifyAuth();
},

loadAccount: function () {
this.$router.push({ name: "account" });
},

  },

  created: function(){
    this.verifyAuth()
  }

}
</script>






<style>

  body{
    margin: 0 0 0 0;
  }

  .header{
    margin: 0%;
    padding: 0;
    width: 100%;
    height: 10vh; 
    min-height: 100px;

    background-color: #283747 ;
    color:#E5E7E9  ;

    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .header h1{
    width: 20%;
    text-align: center;
  }

  .header nav {
    height: 100%;
    width: 20%;

    display: flex;
    justify-content: space-around;
    align-items: center;

    font-size: 20px;
  }

  .header nav button{
    color: #E5E7E9;
    background: #283747;
    border: 1px solid #E5E7E9;

    border-radius: 5px;
    padding: 10px 20px;
  }

  .header nav button:hover{
    color: #283747;
    background: #E5E7E9;
    border: 1px solid #E5E7E9;
  }

  
  .main-component{
    height: 75vh;
    margin: 0%;
    padding: 0%;

    background: #FDFEFE ;
  }

 
  .footer{
    margin: 0;
    padding: 0;
    width: 100%;
    height: 10vh;
    min-height: 100px; 

    background-color: #283747;
    color: #E5E7E9;

  }

  .footer h2{
    width: 100%;
    height: 100%;
    
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>
