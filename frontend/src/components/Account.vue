<template>
  <div v-if="loaded" class="information">
    <h1>Información de su cuenta</h1>
    <h2>
      Nombre: <span>{{ name }}</span>
    </h2>
    <h2>
      Saldo: <span>{{ balance }} COP </span>
    </h2>
    <h2>
      Correo electrónico: <span>{{ email }}</span>
    </h2>
  </div>
</template>
<script>
import jwt_decode from "jwt-decode";
import axios from "axios";
export default {
  name: "Account",
  data: function () {
    return {
      name: "",
      email: "",
      balance: 0,
      loaded: false,
    };
  },
  methods: {
    getData: async function () {
      debugger
      if (
        localStorage.getItem("token_access") === null ||
        localStorage.getItem("token_refresh") === null
      ) {
        this.$emit("logOut");
        return;
      }
      await this.verifyToken();

      let token = localStorage.getItem("token_access");
      let userId = jwt_decode(token).user_id.toString();

      axios
        .get(
          `http://127.0.0.1:8000/user/${userId}/`,
          { headers: { Authorization: `Bearer ${token}` } }
        )

        .then((result) => {
          debugger
          this.name = result.data.name;
          this.email = result.data.email;
          this.balance = result.data.account.balance;
          this.loaded = true;
        })
        .catch(() => {
          this.$emit("logOut");
        });
    },
    verifyToken: function () {
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
  created: async function () {
    this.getData();
  },
};
</script>
<style>
.information {
  margin: 0;
  padding: 0%;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.information h1 {
  font-size: 60px;
  color: #0f1316;
}
.information h2 {
  font-size: 40px;
  color: #283747;
}
.information span {
  color: crimson;
  font-weight: bold;
}
</style>