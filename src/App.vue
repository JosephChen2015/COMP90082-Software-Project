<!--App.vue是主组件，所有页面在App.vue下进行切换-->

<template>
  <v-app>
    <v-app-bar color="#114155" elevate-on-scroll scroll-target="#scrolling-techniques" style="height: 64px">
      <v-app-bar-nav-icon class="white--text" @click="sideNav = !sideNav"></v-app-bar-nav-icon>
      <router-link tag="v-card" to="/" style="cursor:pointer; font-family: 'Bradley Hand'"><v-toolbar-title class="white--text">Celebrities Recognition</v-toolbar-title></router-link>
      <v-spacer></v-spacer>
      <v-toolbar-items id="items" style="height: 59px; font-family: 'Bradley Hand'">
        <v-btn color="#114155" @click="onLoadHome">
          <v-icon left class="mdi mdi-home white--text"></v-icon>
          <div class="white--text">Home</div>
        </v-btn>
        <v-btn v-if="menuItems.login.login" color="#114155" @click="onLoadLogin">
            <v-icon left class="mdi mdi-login white--text"></v-icon>
          <div class="white--text">Login</div>
        </v-btn>
        <v-btn v-if="menuItems.register.register" color="#114155" @click="onLoadSignUp">
            <v-icon left class="mdi mdi-account-plus white--text"></v-icon>
          <div class="white--text">Sign Up</div>
        </v-btn>
          <v-btn v-if="menuItems.history.history" color="#114155" @click="onLoadHistory">
            <v-icon left class="mdi mdi-history white--text"></v-icon>
            <div class="white--text">History</div>
          </v-btn>
        <v-btn v-if="menuItems.logout.logout" @click="onLogout" color="#114155">
            <v-icon left class="mdi mdi-logout white--text"></v-icon>
          <div class="white--text">Log Out</div>
        </v-btn>


      </v-toolbar-items>
    </v-app-bar>
    <div id="main">
    <v-sheet
            id="scrolling-techniques"
            class="overflow-y-auto"

    >
      <v-container style="height: 1500px">
        <div><router-view></router-view></div>
      </v-container>
    </v-sheet>
    <v-navigation-drawer width="160px" temporary absolute v-model="sideNav" color="#114155">
      <v-list class="list">
        <v-list-item>
          <v-icon class="mdi mdi-home white--text" @click="onLoadHome">  Home</v-icon>
        </v-list-item>
        <v-list-item v-if="menuItems.login.login">
          <v-icon class="mdi mdi-login white--text" @click="onLoadLogin">  Login</v-icon>
        </v-list-item>
        <v-list-item v-if="menuItems.register.register">
          <v-icon class="mdi mdi-account-plus white--text" @click="onLoadSignUp">  Sign Up</v-icon>
        </v-list-item>
        <v-list-item v-if="menuItems.history.history">
          <v-icon class="mdi mdi-history white--text" @click="onLoadHistory">  History</v-icon>
        </v-list-item>
        <v-list-item v-if="menuItems.logout.logout">
          <v-icon class="mdi mdi-logout white--text" @click="onLogout">  Log Out</v-icon>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    </div>


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


    data(){
      return{
        sideNav:false,

    }

    },
    computed:{
      // mini(){
      //   switch (this.$vuetify.breakpoint.name) {
      //     case 'xs': return true
      //     case 'sm': return true
      //     case 'md': return true
      //     case 'lg': return false
      //     case 'xl': return false
      //   }
      // },
      menuItems(){
        let menuItems = {
          home:{home:true, title: 'Home'},
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
        this.$router.push('/')
      },
      onLoadHome(){
        this.$router.push('/')
      },
      onLoadHistory(){
        this.$router.push('/History/')
      },
      onLoadLogin(){
        this.$router.push('/Login/')
      },
      onLoadSignUp(){
        this.$router.push('/Register/')
      },
    }
    // data: () => ({
    //   sideNav:false
    // }
  };
</script>
<style>
  .list{
    font-family: "Bradley Hand";
  }
  @media screen and (max-width: 600px) {
    #items{
      display: none;
    }
  }
  @media screen and (max-width: 600px){
    #drawer{

    }
  }
  #scrolling-techniques{
    /*opacity: 0.85;*/

    background: url('assets/poly-bg6.jpg') no-repeat center center fixed;
    background-size: 110% 110%;
  }

</style>

