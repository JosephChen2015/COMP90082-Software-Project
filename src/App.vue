<!--App.vue是主组件，所有页面在App.vue下进行切换-->

<template>
  <v-app>
    <v-app-bar class="blue lighten-4" elevate-on-scroll scroll-target="#scrolling-techniques" style="height: 64px">
      <v-app-bar-nav-icon @click="sideNav = !sideNav"></v-app-bar-nav-icon>
      <router-link tag="v-card" to="/" style="cursor:pointer"><v-toolbar-title>Celebrities Recognition</v-toolbar-title></router-link>
      <v-spacer></v-spacer>
      <v-toolbar-items style="height: 59px">
        <v-btn v-if="menuItems.login.login" class="blue lighten-4">
          <router-link tag="v-card" to="/Login">
            <v-icon left class="mdi mdi-login"></v-icon>
            Login
          </router-link>
        </v-btn>
        <v-btn v-if="menuItems.register.register" class="blue lighten-4">
          <router-link tag="v-card" to="/Register">
            <v-icon left class="mdi mdi-account-plus"></v-icon>
            Sign Up
          </router-link>
        </v-btn>
        <router-link tag="v-card" to="/History">
          <v-btn v-if="menuItems.history.history" class="blue lighten-4">
            <v-icon left class="mdi mdi-login"></v-icon>
            History
          </v-btn>
        </router-link>
        <v-btn v-if="menuItems.logout.logout" @click="onLogout" class="blue lighten-4">
            <v-icon left class="mdi mdi-logout"></v-icon>
            Log Out
        </v-btn>


      </v-toolbar-items>
    </v-app-bar>
    <v-sheet
            id="scrolling-techniques"
            class="overflow-y-auto"
            max-height="900"
    >
      <v-container style="height: 1500px">
        <div><router-view></router-view></div>
      </v-container>
    </v-sheet>

    <v-navigation-drawer temporary absolute v-model="sideNav">
      <v-list>
        <v-list-item>
          <v-icon class="mdi mdi-login">Login</v-icon>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>


  </v-app>
</template>

<script>
  import {Swiper, SwiperSlide, directive} from 'vue-awesome-swiper'
  import 'swiper/css/swiper.css'
  export default {
    name: 'App',

    components: {
      // eslint-disable-next-line vue/no-unused-components
      Swiper,
      // eslint-disable-next-line vue/no-unused-components
      SwiperSlide
    },
    directives: {
      swiper: directive
    },
    // computed:{
    //   swiper(){
    //     return this.$refs.mySwiper.swiper
    //   }
    // },
    // mounted() {
    //   console.log('mounted');
    // },

    data(){
      return{
        // swiperOption:{
        //   notNextTick:true,
        //   autoplay:3000,
        //   effect:"coverflow",
        //   grabCursor:true,
        //   setWrapperSize:true,
        //   pagination:'.swiper-pagination',
        //   paginationClickable:true,
        //   prevButton:".swiper-button-prev",
        //   nextButton:".swiper-button-next",
        //   observeParents:true,
        // },
        sideNav:false,

      }
    },
    computed:{
      menuItems(){
        let menuItems = {
        login:{login:true, title: 'Login'},
        register:{register:true, title: 'Register'},
        history:{history:false, title: 'History'},
        logout:{logout:false, title: 'Logout'}
      }
        if(this.userIsAuthenticated){
          menuItems = {
          login:{login:false, title:'Login'},
          register:{register:false, title:'Register'},
          history:{history:true, title:'History'},
          logout:{logout:true, title: 'Logout'}
          }
        }
        return menuItems
      },
      userIsAuthenticated(){
        return this.$store.getters.user !== null && this.$store.getters.user !== undefined
      }
    },
    methods:{
      onLogout(){
        this.$store.dispatch('logout')
      }
    }
    // data: () => ({
    //   sideNav:false
    // }),
  };
</script>
