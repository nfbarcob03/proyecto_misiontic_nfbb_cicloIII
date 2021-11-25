import { createRouter, createWebHistory } from "vue-router";
import App from "./App.vue";
import LogIn from "./components/LogIn.vue";
import SignUp from "./components/SignUp.vue";
import Home from "./components/Home.vue";
import Account from "./components/Account.vue";
import CrearInmueble from "./components/CrearInmueble";
import VerInmuebles  from "./components/VerInmuebles";
import EditarInmueble from "./components/EditarInmueble";
const routes = [
  {
    path: "/",
    name: "root",
    component: App,
  },
  {
    path: "/user/logIn",
    name: "logIn",
    component: LogIn,
  },
  {
    path: "/user/signUp",
    name: "signUp",
    component: SignUp,
  },
  {
    path: "/user/home",
    name: "home",
    component: Home,
  },
  {
    path: "/user/account",
    name: "account",
    component: Account,
  },
  {
    path: "/inmueble/createInmueble",
    name: "CrearInmueble",
    component: CrearInmueble,
  },
  {
    path: "/inmueble/VerInmuebles",
    name: "VerInmuebles",
    component: VerInmuebles,
  },
  {
    path: "/inmueble/EditarInmueble",
    name: "EditarInmueble",
    component: EditarInmueble,
  },

  
];
const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;
