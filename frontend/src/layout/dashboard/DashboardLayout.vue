
<!--<template>
  <div class="wrapper">
    <side-bar>
      <template slot-scope= "props" slot="links">
        <sidebar-link to="/cchp" :name="$t('CCHP 소개')" icon="tim-icons icon-single-copy-04"/>
        <sidebar-link to="/electric" :name="$t('전력 사용량 패턴 분석')" icon="tim-icons icon-chart-bar-32"/>
        <sidebar-link to="/scheduling" :name="$t('CCHP 스케줄링')" icon="tim-icons icon-chart-pie-36"/>
        <sidebar-link to="/economics" :name="$t('경제성 분석')" icon="tim-icons icon-coins"/>
        <sidebar-link to="/profile" :name="$t('sidebar.userProfile')" icon="tim-icons icon-single-02"/>
        <sidebar-link to="/table-list" :name="$t('sidebar.tableList')" icon="tim-icons icon-puzzle-10"/>
      </template>
    </side-bar>-->
    <!--<div class="sidebar-wrapper">
      <side-bar title="HOME" short-title="S" background-color="vue">
         <template slot="links">
         <sidebar-item :link="{ name: 'CCHP 소개', icon: 'tim-icons icon-image-02' }">

         <sidebar-item
           :link="{
             name: 'CCHP 소개',
             path: '/cchp',
             isRoute: false,
           }"/>

           <sidebar-item
              :link="{
                name: 'CCHP 적용사례',
                path: '/cchp_ex',
                isRoute: false,
              }"/>

        </sidebar-item>
        </template>
    </side-bar>
    <div class="main-panel">
      <top-navbar></top-navbar>
      <dashboard-content @click.native="toggleSidebar">
      </dashboard-content>
      <content-footer></content-footer>
    </div>
  </div>
</template>
<style lang="scss">
</style>
<script>
import Vue from 'vue'
import BootstrapSidebar from 'vue-bootstrap-sidebar'
import TopNavbar from "./TopNavbar.vue";
import ContentFooter from "./ContentFooter.vue";
import DashboardContent from "./Content.vue";
import MobileMenu from "./MobileMenu";
import VueSidebarMenu from 'vue-sidebar-menu'
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'
import { SidebarMenu } from 'vue-sidebar-menu'
export default {
//export default Vue.extend({
  //props: ['name','path'],
  name: 'sidebar-wrapper',
  components: {
    BootstrapSidebar,
    TopNavbar,
    ContentFooter,
    DashboardContent,
    MobileMenu
  },

  methods: {
    /*toggleSidebar() {
      if (this.$sidebar.showSidebar) {
        this.$sidebar.displaySidebar(false);
      }
    }*/
  }
};
</script>
<!--
<script>
import Vue from 'vue'
import BootstrapSidebar from 'vue-bootstrap-sidebar'
import TopNavbar from "./TopNavbar.vue";
import ContentFooter from "./ContentFooter.vue";
import DashboardContent from "./Content.vue";
import MobileMenu from "./MobileMenu";

export default Vue.extend({
  name: 'App',
  components: {
    BootstrapSidebar,
    TopNavbar,
    ContentFooter,
    DashboardContent,
    MobileMenu
  },
  data () {
    return {
      initialShow: true,
      header: '<h3>Sidebar</h3>',
      links: [
        { name: 'Home', href: { name: 'home' }, faIcon: ['fas', 'home'] },
        {
          name: 'Dropdown',
          faIcon: ['fas', 'tint'],
          children: [
            {
              name: 'Child Item 1',
              href: {
                name: 'child-item-1'
              },
              faIcon: ['fas', 'child']
            },
            {
              name: 'Child Item 2',
              href: {
                name: 'child-item-2'
              },
              faIcon: ['fas', 'child']
            }
          ]
        },
        { name: 'About', href: { name: 'about' }, faIcon: 'users' },
        { name: 'Contact', href: { name: 'contact' }, faIcon: 'phone' }
      ]
    }
  },
  methods: {
    onSidebarChanged () {
    },
    toggleSidebar() {
      if (this.$sidebar.showSidebar) {
        this.$sidebar.displaySidebar(false);
      }
    }
  }
})
</script>

<template>
  <div id="App">
    <BootstrapSidebar
      :initial-show="initialShow"
      :links="links"
      :header="header"
      :fa="true"
      @sidebarChanged="onSidebarChanged"
    >
      <template v-slot:navbar>
        <b-navbar
          id="mainNavbar"
          toggleable="lg"
          type="light"
          variant="light"
          fixed="top"
        >
          <b-navbar-nav>
            <b-nav-item>
              Navbar
            </b-nav-item>
          </b-navbar-nav>
        </b-navbar>
      </template>
    <template v-slot:content>
        <b-container style="margin-top: 30px">
          <router-view />
        </b-container>
    </template>
    <div class="main-panel">
      <top-navbar></top-navbar>
      <dashboard-content @click.native="toggleSidebar">
      </dashboard-content>
      <content-footer></content-footer>
    </div>
  </div>
</template>

<style lang="scss">
@import 'node_modules/bootstrap/scss/bootstrap';
@import 'node_modules/bootstrap-vue/src/index.scss';
@import 'node_modules/vue-bootstrap-sidebar/src/scss/default-theme';
@import 'node_modules/vue-bootstrap-sidebar/src/scss/default-theme.scss';
</style>


<!--<template>
  <sidebar-menu :menu="menu" />

</template>
<script>
import Vue from 'vue'
import BootstrapSidebar from 'vue-bootstrap-sidebar'
import TopNavbar from "./TopNavbar.vue";
import ContentFooter from "./ContentFooter.vue";
import DashboardContent from "./Content.vue";
import MobileMenu from "./MobileMenu";
import VueSidebarMenu from 'vue-sidebar-menu'
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'
import { SidebarMenu } from 'vue-sidebar-menu'
export default {
  components: {
    SidebarMenu,
    BootstrapSidebar,
    TopNavbar,
    ContentFooter,
    DashboardContent,
    MobileMenu
  },
  data() {
          return {
              menu: [
                  {
                      header: true,
                      title: 'Main Navigation',
                      hiddenOnCollapse: true
                  },
                  {
                      href: '/cchp',
                      title: 'Menu 1',
                      icon: 'ICON CLASS HERE'
                  },
                  {
                      href: '/2',
                      title: 'Menu 2',
                      icon: 'ICON CLASS HERE',
                      child: [
                          {
                              href: '/2-1',
                              title: 'Menu 2-1'
                          }
                      ]
                  }
              ]
          }
      }
  }
</script>-->



<!-- 기능 작동 /
<script>
import Vue from 'vue'
import BootstrapSidebar from 'vue-bootstrap-sidebar'
import TopNavbar from "./TopNavbar.vue";
import ContentFooter from "./ContentFooter.vue";
import DashboardContent from "./Content.vue";
import MobileMenu from "./MobileMenu";
import VueSidebarMenu from 'vue-sidebar-menu'
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'
import { SidebarMenu } from 'vue-sidebar-menu'

export default Vue.extend({
  name: 'App',
  components: {
    SidebarMenu,
    BootstrapSidebar,
    TopNavbar,
    ContentFooter,
    DashboardContent,
    MobileMenu
  },
  data () {
    return {
      initialShow: true,
      header: '<h3>Sidebar</h3>',
      links: [
        { name: 'Home', href:  '/home', faIcon: ['fas', 'home'] },
        {
          name: 'CCHP',
          faIcon: ['fas', 'tint'],
          children: [
            {
              name: 'CCHP 소개',
              href:  '/cchp',
              faIcon: ['fas', 'child']
            },
            {
              name: 'CCHP 적용사례',
              href:  '/cchp_ex',
              faIcon: ['fas', 'child']
            },
             {
              name: 'CCHP 뉴스',
              href:  '/cchp_news',
              faIcon: ['fas', 'child']
            }
          ]
        },
        { name: 'About', href: { name: 'about' }, faIcon: 'users' },
        { name: 'Contact', href: { name: 'contact' }, faIcon: 'phone' }
      ]
    }
  },
  methods: {
   onSidebarChanged () {
    }
     /*onToggleCollapse(collapsed) {},
    onItemClick(event, item, node) {}*/
  }
})
</script>

<template>
  <div id="App">
    <BootstrapSidebar
      :initial-show="initialShow"
      :links="links"
      :header="header"
      :fa="true"
      @sidebarChanged="onSidebarChanged"
    >
      <template v-slot:navbar>
        <b-navbar
          id="mainNavbar"
          toggleable="lg"
          type="light"
          variant="light"
          fixed="top"
        >
          <b-navbar-nav>
            <b-nav-item>
              Navbar
            </b-nav-item>
          </b-navbar-nav>
        </b-navbar>
      </template>
      <!--/*<template v-slot:content>
        <b-container style="margin-top: 56px">
          <router-view />
        </b-container>
      </template>*/-->
 <!--   </BootstrapSidebar>
    <div class="main-panel">
      <top-navbar></top-navbar>
      <dashboard-content @click.native="toggleSidebar">
      </dashboard-content>
      <content-footer></content-footer>
    </div>
  </div>
</template>

<style lang="scss">
@import 'node_modules/bootstrap/scss/bootstrap';
@import 'node_modules/bootstrap-vue/src/index.scss';
@import 'node_modules/vue-bootstrap-sidebar/src/scss/default-theme';
</style>






<!--
<template>
 <div class="wrapper">
  <sidebar-menu :menu="menu" />
   <div class="main-panel">
      <top-navbar></top-navbar>
      <dashboard-content @click.native="toggleSidebar">
      </dashboard-content>
      <content-footer></content-footer>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import VueSidebarMenu from 'vue-sidebar-menu'
import BootstrapSidebar from 'vue-bootstrap-sidebar'
import TopNavbar from "./TopNavbar.vue";
import ContentFooter from "./ContentFooter.vue";
import DashboardContent from "./Content.vue";
import MobileMenu from "./MobileMenu";
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'
import { SidebarMenu } from 'vue-sidebar-menu'

//Vue.use(VueSidebarMenu)
    export default {
      /*components: {
       SidebarMenu,
       BootstrapSidebar,
       TopNavbar,
       ContentFooter,
       DashboardContent,
       MobileMenu
      },*/
      data() {
            menu: [
                {
                    href: '/',
                    title: 'Dashboard',
                    icon: 'fa fa-user'
                },
                {
                    href: '#',
                    title: 'Charts',
                    icon: 'fa fa-chart-area'
                },
            ]
        }
    }
</script>
-->

<!--
<template>
  <div>
  <sidebar-menu :menu="menu">
    <div slot="header"></div>
    <span slot="dropdown-icon"></span>
  </sidebar-menu>
  <div class="main-panel">
      <top-navbar></top-navbar>
      <dashboard-content @click.native="toggleSidebar">
      </dashboard-content>
      <content-footer></content-footer>
    </div>
  </div>
</template>

<script>
import { SidebarMenu } from 'vue-sidebar-menu'
import VueSidebarMenu from 'vue-sidebar-menu'
import BootstrapSidebar from 'vue-bootstrap-sidebar'
import TopNavbar from "./TopNavbar.vue";
import ContentFooter from "./ContentFooter.vue";
import DashboardContent from "./Content.vue";
import MobileMenu from "./MobileMenu";
export default {
  props: {
      menu: {
      type: Array,
      required: true
    },
    // Sidebar Collapse state
      collapsed: {
      type: Boolean,
      default: false
    },
    // Sidebar width (expanded)
    width: {
    type: String,
    default: '50px'
    },
    // Sidebar width (collapsed)
    widthCollapsed: {
    type: String,
    default: '40px'
    },
    // Keep only one child opened at a time (first level only)
    showOneChild: {
    type: Boolean,
    default: false
    },
    // Keep all child open
    showChild: {
    type: Boolean,
    default: false
    },
    // Sidebar right to left
    rtl: {
    type: Boolean,
    default: false
    },
    // Make sidebar relative to the parent (by default the sidebar is relative to the viewport)
    relative: {
    type: Boolean,
    default: false
    },
    // Hide toggle collapse btn
    hideToggle: {
    type: Boolean,
    default: false
    },
    // Sidebar theme (available themes: 'white-theme')
    theme: {
     type: String,
     default: ''
    },
  // Disable hover on collapse mode
    disableHover: {
    type: Boolean,
    default: false
    }
  },
  components: {
    SidebarMenu,
    TopNavbar,
    ContentFooter,
    DashboardContent,
    MobileMenu
  },
  methods: {
    onToggleCollapse(collapsed) {},
    onItemClick(event, item, node) {}
  },
  data() {
          return {
              menu: [
                  {
                      header: true,
                      title: 'Main Navigation',
                      hiddenOnCollapse: true
                  },
                  {
                      path: '/cchp',
                      name: 'CCHP 소개',
                      icon: 'tim-icons icon-single-copy-04'
                  },
                  {
                      path: '/electric',
                      name: 'CCHP 소개',
                      icon: 'tim-icons icon-single-copy-04',
                      child: [
                          {
                              href: '#',
                              name: 'Menu 2-1'
                          }
                      ]
                  }
              ]
          }
      }
}
</script>
-->








<template>
  <div id="app2">
    <side-bar title="HOME" short-title="S" background-color="vue">
     <!-- <template slot="links" :items="items" >
       <vue-tree-navigation :items="items" />   :defaultOpenLevel="1"    드롭다운 처음부터 실행-->
       <template slot="links">
         <sidebar-link to="/cchp" :name="$t('CCHP')"  icon="tim-icons icon-single-copy-04" />
         <span><vue-tree-navigation :items="menu1" /></span>
         <sidebar-link to="/electric"  :name="$t('ELECTRIC')"  icon="tim-icons icon-chart-bar-32"/>
         <span><vue-tree-navigation :items="menu2" /></span>
         <sidebar-link to="/scheduling" :name="$t('SCHEDULING')" icon="tim-icons icon-chart-pie-36"/>
         <span><vue-tree-navigation :items="menu3" /></span>
         <sidebar-link to="/economics"  :name="$t('ECONOMICS')" icon="tim-icons icon-coins"/>
         <span><vue-tree-navigation :items="menu4" /></span>
         <sidebar-link to="/profile" :name="$t('sidebar.userProfile')" icon="tim-icons icon-single-02"/>
         <!-- <sidebar-link to="/table-list" :name="$t('sidebar.tableList')" icon="tim-icons icon-puzzle-10"/> -->
       </template>
    </side-bar>

  <div class="main-panel">
    <top-navbar></top-navbar>
    <dashboard-content @click.native="toggleSidebar">
    </dashboard-content>
    <content-footer></content-footer>
  </div>
  </div>
</template>
<script src="https://unpkg.com/vue-tree-navigation@4.0.0/dist/vue-tree-navigation.js"></script>
<script>
import Vue from 'vue'
import BootstrapSidebar from 'vue-bootstrap-sidebar'
import TopNavbar from "./TopNavbar.vue";
import ContentFooter from "./ContentFooter.vue";
import DashboardContent from "./Content.vue";
import MobileMenu from "./MobileMenu";
import VueSidebarMenu from 'vue-sidebar-menu'
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'
import { SidebarMenu } from 'vue-sidebar-menu'
import VueTreeNavigation from 'vue-tree-navigation';
import SidebarLink from '../../components/SidebarPlugin/SidebarLink.vue';
Vue.use(VueTreeNavigation)
export default {
  components: {
    BootstrapSidebar,
    TopNavbar,
    ContentFooter,
    DashboardContent,
    MobileMenu,
    SidebarLink
  },
  data() {
     return {
        menu1: [
              {
                path: '/cchp',
                children: [
                  { name: "CCHP 소개", path: 'cchp_info' },
                  { name: "CCHP 적용사례", path: 'cchp_ex' },
                  { name: "CCHP 관련뉴스", path: 'cchp_news' }
                ]
              }
            ],
        menu2:[
              {
                path: 'electric',
                children: [
                  { name: "전력 사용량 패턴 분석", path: 'elec_pattern' },
                  { name: "예측 전력 사용량 비교", path: 'elec_compare' },
                  { name: "입력 변수 데이터 통계", path: 'elec_inputdata' },
                  { name: "교육용 요금제", path: 'elec_payment' }
                ]
              }
            ],
        menu3:[
               {
                path: "scheduling",
                children: [
                  { name: "전력 사용량 예측", path: "sch_prediction" },
                  { name: "CCHP 스케줄링", path: "sch_cchp" },
                  // { name: "CCHP 운영 시간표", path: "sch_time" },
                  { name: "입력 변수 데이터 통계", path: "sch_inputdata" }
                ]
              },
          ],
        menu4: [
                {
                path: "economics",
                children: [
                  { name: "경제성 분석", path: 'eco_analysis' },
                  // { name: "다른 요금제와 비교", path: "eco_compare" },
                  // { name: "입력 변수 데이터 통계", path: "eco_inputdata" }
                ]
              },
           ],
        };
    },
    methods: {
     toggleSidebar() {
      if (this.$sidebar.showSidebar) {
        this.$sidebar.displaySidebar(false);
      }
    }
  },
    disableHover: {
      type: Boolean,
      default: false
  }
 };
</script>
<style lang="scss">

  .NavigationToggle {
  position: relative;
  top:  -37px;
  left: 165px;
  padding:  5px 5px 5px 3px;
  cursor:   pointer;

  &__icon {
    display:      inline-block;
    padding:      3px;
    border:       solid #000;
    border-width: 0 2px 2px 0;
    transform:    rotate(45deg);
  }

   &__icon--closed {
    transform: rotate(-45deg);
    }
  }
  .NavigationLevel {
   top:  -100px;
   padding-top: -100px;
   &--closed {
      ul {
        display: none;
      }
    }
  }
  .NavigationLevel__children {
    padding-top:  -100px;
    padding-left: 10px;

    //font-family: 'Helvetica Neue', Arial, sans-serif;
  }

  .NavigationLevel__parent {
    line-height:100%;
    padding-top:    -100px;
    font-weight:    600;
    padding-bottom: 0px;
  }

  .NavigationItem {
   //line-height:100%;
   display: inline-block;
   padding-left: 11px;
   padding-bottom: 5px;
    span {
     cursor: pointer;
    }
    a {
        font-family:  'Courier, monospace';
        /*'Helvetica Neue', Arial, sans-serif;*/
        //padding-top:    -100px;
        font-size: 11.5px;
        font-weight: 600;
        color: #fff;
        text-decoration: none;
    }
    a:hover{
        color:#12f771;
    }

  }
  .TreeNavigation {
   // line-height:100%;
     top: -100px;
     display: inline-block;
     padding: -100px;
     margin:  0;

   ul {
     padding:         -100px;
     margin:          0px;
     list-style-type: none;
     color: #fff;
   }

   li {
    color: #fff;
    padding-left: 20px;
   }
 }
  .NavigationItem--active {
    top: -100px;
     color: #000508;
     //color: #fff;
  }

  .NavigationToggle__icon {
    border-color: #12f771;
  }
  .NavigationToggle__icon--closed {
   //border-color: #155dc9;
    border-color:#fff;
  }
</style>
