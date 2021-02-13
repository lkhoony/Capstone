import DashboardLayout from "@/layout/dashboard/DashboardLayout.vue";
// GeneralViews
import NotFound from "@/pages/NotFoundPage.vue";
/*import CCHP_info from "@/pages/CCHP/CCHP_info.vue";
import CCHP_ex from "@/pages/CCHP/CCHP_ex.vue";
import CCHP_news from "@/pages/CCHP/CCHP_.vue";*/
// Admin pages
const CCHP_info = () => import(/* webpackChunkName: "dashboard" */"@/pages/CCHP/CCHP_info.vue");
const CCHP_ex = () => import(/* webpackChunkName: "dashboard" */"@/pages/CCHP/CCHP_ex.vue");
const CCHP_news = () => import(/* webpackChunkName: "dashboard" */"@/pages/CCHP/CCHP_news.vue");
const Home = () => import(/* webpackChunkName: "dashboard" */"@/pages/Home.vue");
const Profile = () => import(/* webpackChunkName: "common" */ "@/pages/Profile.vue");
const scheduling = () => import(/* webpackChunkName: "common" */"@/pages/scheduling.vue");
const economics = () => import(/* webpackChunkName: "common" */ "@/pages/economics.vue");
const TableList = () => import(/* webpackChunkName: "common" */ "@/pages/TableList.vue");
const Elec_pattern = () => import(/* webpackChunkName: "common" */ "@/pages/Elec_pattern.vue");
const Elec_inputdata = () => import(/* webpackChunkName: "common" */ "@/pages/Elec_inputdata.vue");
const Elec_compare = () => import(/* webpackChunkName: "common" */ "@/pages/Elec_compare.vue");
const Elec_payment = () => import(/* webpackChunkName: "common" */ "@/pages/Elec_payment.vue");
const Sch_prediction = () => import(/* webpackChunkName: "common" */ "@/pages/Sch_prediction.vue");
const Sch_cchp = () => import(/* webpackChunkName: "common" */ "@/pages/Sch_cchp.vue");
const Sch_inputdata = () => import(/* webpackChunkName: "common" */ "@/pages/Sch_inputdata.vue");
const Sch_time = () => import(/* webpackChunkName: "common" */ "@/pages/Sch_time.vue");
const Eco_inputdata = () => import(/* webpackChunkName: "common" */ "@/pages/Eco_inputdata.vue");
const Eco_compare = () => import(/* webpackChunkName: "common" */ "@/pages/Eco_compare.vue");
const Eco_analysis = () => import(/* webpackChunkName: "common" */ "@/pages/Eco_analysis.vue");

const routes = [
  {
    path: "/",
    component: DashboardLayout,
    // redirect: "/home",
    children: [
      {
        path: '/',
        name: "Home",
        component: Home
      },
      {
        path: "CCHP",
        name: 'CCHP',
        component: CCHP_info
      },
      {
        path: 'electric',
        name: 'electric',
        component: Elec_pattern
      },
      {
        path: 'scheduling',
        name: 'scheduling',
        component: Sch_prediction
      },
      {
        path: 'economics',
        name: 'economics',
        component: Eco_analysis
      },
      {
        path: '/electric/elec_pattern',
        name: "/electric/elec_pattern",
        component: Elec_pattern
      },
      {
        path: '/electric/elec_compare',
        name: "/electric/elec_compare",
        component: Elec_compare
      },
      {
        path: '/electric/elec_inputdata',
        name: "/electric/elec_inputdata",
        component: Elec_inputdata
      },
      {
        path: '/electric/elec_payment',
        name: "/electric/elec_payment",
        component: Elec_payment
      },
      {
        path: "/CCHP/CCHP_info",
        name: "/CCHP/CCHP_info",
        component: CCHP_info
      },
      {
        path: "/CCHP/CCHP_ex",
        name: "/CCHP/CCHP_ex",
        component: CCHP_ex
      },
      {
        path: "/CCHP/CCHP_news",
        name: "/CCHP/CCHP_news",
        component: CCHP_news
      },
      {
        path: '/scheduling/sch_prediction',
        name: '/scheduling/sch_prediction',
        component: Sch_prediction
      },
      {
        path: '/scheduling/sch_cchp',
        name: '/scheduling/sch_cchp',
        component: Sch_cchp
      },
      {
        path: '/scheduling/sch_inputdata',
        name: '/scheduling/sch_inputdata',
        component: Sch_inputdata
      },
      {
        path: '/scheduling/sch_time',
        name: '/scheduling/sch_time',
        component: Sch_time
      },
      {
        path: '/economics/eco_analysis',
        name: '/economics/eco_analysis',
        component: Eco_analysis
      },
      {
        path: '/economics/eco_compare',
        name: '/economics/eco_compare',
        component: Eco_compare
      },
      {
        path: '/economics/eco_inputdata',
        name: '/economics/eco_inputdata',
        component: Eco_inputdata
      },
      {
        path: "profile",
        name: "profile",
        component: Profile
      },
      {
        path: "table-list",
        name: "table-list",
        component: TableList
      },
    ]
  },
 { path: "*", component: NotFound },
];

// const routes = {
//   "/": DashboardLayout
// }

/**
 * Asynchronously load view (Webpack Lazy loading compatible)
 * The specified component must be inside the Views folder
 * @param  {string} name  the filename (basename) of the view to load.
function view(name) {
   var res= require('../components/Dashboard/Views/' + name + '.vue');
   return res;
};**/

export default routes;
