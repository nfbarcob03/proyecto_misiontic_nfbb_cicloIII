<template>
  <div id="crear_producto">
    <h2>Crear Inmueble</h2>
    <label for="text"> Arrendatario</label>
    <select class="form-control" id="id_arrendatario" v-model="id_arrendatario">
      <option v-for="usuario in allUsuarios" :value="usuario.id">{{
        usuario.name
      }}</option>
    </select>
    <label for="precio">Precio</label>
    <input
      type="number"
      id="precio"
      name="precio"
      v-model="precio"
      placeholder="$$$$$"
    />
    <label for="precio_unitario"> Numero de habitaciones</label>
    <input
      type="number"
      id="habitaciones"
      name="habitaciones"
      v-model="habitaciones"
      placeholder="Numero de habitaciones"
    />
    <label for="habitaciones">Tipo de inmueble</label>
    <select class="form-control" id="tipo" v-model="tipo">
      <option v-for="tipo in allTipos" :value="tipo.id">{{
        tipo.nombre
      }}</option>
    </select>
    <label for="unit_messu">Estado inmueble</label>
    <select class="form-control" id="disponible" v-model="disponible">
      <option value="true">Disponible</option>
      <option value="false">No Disponible</option>
    </select>
    <button v-on:click="createInmueble">createProducto</button>
    <button v-on:click="resetProduct">borrar campos</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "CrearInmueble",
  data: function() {
    return {
      id: "",
      id_arrendatario: "",
      precio: "",
      habitaciones: "",
      tipo: "",
      disponible: false,
      allUsuarios: [],
      allTipos: [],
    };
  },
  created: function() {
    debugger;
    this.id_arrendatario = localStorage.getItem("userId");
    this.username = this.$route.params.username;
    let self = this;
    this.allCategories = this.$route.params.allCategories;
    (this.units_mesusre = ["Units", "Liters", "Grams"]), this.getAllUsuarios();
    this.getAllTipos();
  },
  methods: {
    getAllUsuarios: async function() {
      axios
        .get(`http://127.0.0.1:8000/users/`, { headers: {} })

        .then((result) => {
          debugger;
          this.allUsuarios = result.data;
        })
        .catch(() => {
          this.$emit("logOut");
        });
    },
    verifyToken: function() {
      return axios
        .post(
          "http://127.0.0.1:8000/refresh/",
          { refresh: localStorage.getItem("token_refresh") },
          { headers: {} }
        )
        .then((result) => {
          localStorage.setItem("token_access", result.data.access);
        })
        .catch(() => {
          this.$emit("logOut");
        });
    },
    getAllTipos: async function() {
      axios
        .get(`http://127.0.0.1:8000/tipoInmuebles/`, { headers: {} })

        .then((result) => {
          this.allTipos = result.data;
        })
        .catch(() => {
          this.$emit("logOut");
        });
    },
    resetProduct: function() {
      debugger
      this.username = this.$route.params.username;
      this.id_arrendatario = ""
      this.precio = ""
      this.habitaciones = ""
      this.tipo = ""
      this.disponible = false
    },
    createInmueble: function() {
      debugger;
      let inmueble = {
        id_arrendatario: parseInt(this.id_arrendatario),
        precio: this.precio,
        habitaciones: this.habitaciones,
        tipo: this.tipo,
        disponible: this.disponible,
      };
      this.verifyToken();
      axios
        .post("http://127.0.0.1:8000/inmueble/", inmueble, {
          headers: { Authorization: `Bearer ${ localStorage.getItem("token_access")}` },
        })
        .then((result) => {
          debugger;
          if (result.status == 201) {
            alert("se ha creado correctamente el inmueble");
            this.resetProduct();
          } else {
            console.log(result);
            alert("hubo un error al crear el iunmueble");
          }
        })
        .catch((error) => {
          if (error.response.status == "401")
            alert("ERROR 401: Credenciales Incorrectas.");
        });
    },
    verifyToken: function() {
      return axios
        .post(
          "http://127.0.0.1:8000/refresh/",
          { refresh: localStorage.getItem("token_refresh") },
          { headers: {} }
        )
        .then((result) => {
          localStorage.setItem("token_access", result.data.access);
        })
        .catch(() => {
          this.$emit("logOut");
        });
    },
  },
};
</script>

<style>
*{box-sizing:border-box;}

form{
	width:300px;
	padding:16px;
	border-radius:10px;
	margin:auto;
	background-color:#ccc;
}

form label{
	width:72px;
	font-weight:bold;
	display:inline-block;
}

form input[type="text"],
form input[type="email"]{
	width:180px;
	padding:3px 10px;
	border:1px solid #f6f6f6;
	border-radius:3px;
	background-color:#f6f6f6;
	margin:8px 0;
	display:inline-block;
}

form input[type="submit"]{
	width:100%;
	padding:8px 16px;
	margin-top:32px;
	border:1px solid #000;
	border-radius:5px;
	display:block;
	color:#fff;
	background-color:#000;
} 

form input[type="submit"]:hover{
	cursor:pointer;
}

textarea{
	width:100%;
	height:100px;
	border:1px solid #f6f6f6;
	border-radius:3px;
	background-color:#f6f6f6;			
	margin:8px 0;
	/*resize: vertical | horizontal | none | both*/
	resize:none;
	display:block;
}
</style>
