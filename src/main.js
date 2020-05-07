//入口文件，初始化VUE实例，并引入所需插件

import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import 'swiper/css/swiper.css'
import VueAwesomeSwiper from 'vue-awesome-swiper';
import 'roboto-fontface/css/roboto/roboto-fontface.css'
import '@mdi/font/css/materialdesignicons.css'
import * as firebase from 'firebase'
import store from './store'

Vue.use(VueAwesomeSwiper)
Vue.use(vuetify)
Vue.config.productionTip = false

new Vue({
  store,
  router,
  vuetify,
  render: h => h(App),
  created(){
    firebase.initializeApp({
      apiKey: "AIzaSyBZEUJ0unUXbOOFN9MaLcHMyGfL14hUAZk",
      authDomain: "aussie-celebrities-recog-72ab7.firebaseapp.com",
      databaseURL: "https://aussie-celebrities-recog-72ab7.firebaseio.com",
      projectId: "aussie-celebrities-recog-72ab7",
      storageBucket: "aussie-celebrities-recog-72ab7.appspot.com",
      messagingSenderId: "877617425337",
      appId: "1:877617425337:web:9d910dc5efbfb376aaa468",
      measurementId: "G-LY6LWF8B9Y"
    })
    firebase.auth().onAuthStateChanged((user)=>{
      if(user){
        this.$store.dispatch('autoLogin',user)
        this.$store.dispatch('recognitionAll')
      }
    })
    // this.$store.dispatch('recognitionAll')
  }
}).$mount('#app')
