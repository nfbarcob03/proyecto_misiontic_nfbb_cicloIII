<template>
  <div>
    <h1>Contacts ()</h1>

    <table class="table table-bordered table-hover">
      <thead>
        <tr>
          <th>id</th>
          <th>nombre arrendatario</th>
          <th>precio</th>
          <th>numero de habitaciones</th>
          <th>tipo</th>
          <th>disponible</th>
          <th>Fecha creacion</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="inmueble in inmuebles">
          <th>{{ inmueble.id}}</th>

          <th>{{inmueble.nombre_arrenatario}}</th>

          <td>{{inmueble.precio}}</td>

          <td>{{inmueble.habitaciones}}</td>

          <td>{{inmueble.tipo}}</td>

          <td>{{inmueble.disponible}}</td>
        
          <td>{{inmueble.fechaCreacion}}</td>

          <td>
            <button class="btn btn-danger" @click="deleteContact(inmueble)"><i class="fa fa-trash"></i></button>
            <button class="btn" @click="editInmueble(inmueble)"><i class="fa fa-pencil"></i></button>
          </td>
        </tr>
      </tbody>
    </table>
    <div></div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "VerInmuebles",

  data() {
    return {
      inmuebles: [],
      numberOfContacts: 0,
    };
  },

  methods: {
    getAllInmuebles: async function() {
      axios
        .get(`http://127.0.0.1:8000/inmuebles/`, { headers: {} })

        .then((result) => {
          debugger;
          this.inmuebles = result.data;
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
    deleteContact: function(inmueble){
        axios
        .delete(`http://127.0.0.1:8000/inmueble/${inmueble.id}/`, { headers: {} })

        .then((result) => {
          debugger;
          console.log(result)
          this.getAllInmuebles();
        })
        .catch(() => {
          this.$emit("logOut");
        });
    },
    editInmueble: function(inmueble){
        debugger
      let inmuebleSend ={
          id: inmueble.id,
          id_arrendatario: inmueble.id_arrendatario,
          nombre_arrenatario:inmueble.nombre_arrenatario,
          precio: inmueble.precio,
          habitaciones: inmueble.habitaciones,
          id_tipo: inmueble.id_tipo,
          tipo: inmueble.tipo,
          disponible: inmueble.disponible,
      }
      localStorage.setItem("InmuebleEdit",JSON.stringify(inmuebleSend))
      this.$router.push({ name: "EditarInmueble" });
     },
  },
  
  created: function() {
    this.getAllInmuebles();
  },
};
</script>
