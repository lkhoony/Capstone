import Vue from 'vue'
import VueRouter from "vue-router";
import routes from "./routes";
import Elec_compare from "@/pages/Elec_compare.vue";
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);

//Vue.use(VueRouter)

/*const routes =[
  {
    path: '/electric',
    name: "elec_compare",
    component: Elec_compare
  },
  /*{
    path: '/elec_pattern',
    name: "Electric_pattern",
    component: Elec_pattern
  }
]*/

// configure router
const router = new VueRouter({
  mode:'history',
  routes, // short for routes: routes
  linkExactActiveClass: "active",
  scrollBehavior: (to) => {
    if (to.hash) {
      return {selector: to.hash}
    } else {
      return { x: 0, y: 0 }
    }
  }
})


export default router;
