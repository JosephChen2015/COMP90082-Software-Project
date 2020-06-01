
<template>
      <v-app id="carousel">
      <v-content id="body">
<!--      <v-container class="fill-height ma-0 pa-0"-->
<!--                        fluid-->
<!--      >-->
<!--            <div id="mainpage" style="text-align: center;width: 100%">-->
<!--                <img style="opacity: 0.5;width: 100%" src="../assets/12e8a6a547e317524121f7a5d6084036.gif">-->
<!--&lt;!&ndash;            <p id="title">Welcome to Australian celebrity facial recognition</p>&ndash;&gt;-->
<!--            </div>-->


<div id="mainpage">
            <div style="text-align: center;margin-top: 10%">
                <h1 style="font-family: Krungthep; margin-bottom: 10%" class="font-weight-bold">Welcome to our AU celebrity recognition website</h1>
                  <router-link tag="v-card" to="/Upload">
<!--                        <v-btn x-large class="blue lighten-4" >-->
<!--                              <v-icon left class="mdi mdi-face-recognition"></v-icon>-->
<!--                              Start Recognition now-->
<!--                        </v-btn>-->
                        <!--                        <v-btn x-large color="primary">Upload</v-btn>-->
                      <a id="upload" href="Upload.vue"><img src="../assets/facial_recognition.svg">
                      <div  class="text white--text font-weight-bold" >Click Here to Start a Recognition Now</div>
                      </a>
                  </router-link>
            </div>
</div>
            <v-row class="mb-12">
                  <v-col class="mx-auto my-0"  style="height: 400px" cols="10">
                        <div class="scroll">
                              <swiper :options="swiperOption" ref="mySwiper">
                                    <!-- slides -->
                                    <swiper-slide><v-img :src="results[0].imageUrl" style="border-radius: 15%; height: 50vw; width: 40vw"></v-img></swiper-slide>
                                    <swiper-slide><v-img :src="results[1].imageUrl" style="border-radius: 15%; height: 50vw; width: 40vw"></v-img></swiper-slide>
                                    <swiper-slide><v-img :src="results[2].imageUrl" style="border-radius: 15%; height: 50vw; width: 40vw"></v-img></swiper-slide>
                                    <swiper-slide><v-img :src="results[3].imageUrl" style="border-radius: 15%; height: 50vw; width: 40vw"></v-img></swiper-slide>
                                    <swiper-slide><v-img :src="results[4].imageUrl" style="border-radius: 15%; height: 50vw; width: 40vw"></v-img></swiper-slide>


                                    <!-- Optional controls -->
                                    <div class="swiper-pagination "  slot="pagination" style="font-size: 1vw"></div>
                                    <div class="swiper-button-prev swiper-button-black" slot="button-prev"></div>
                                    <div class="swiper-button-next swiper-button-black" slot="button-next"></div>
                                    <!-- <div class="swiper-scrollbar"   slot="scrollbar"></div> -->
                              </swiper>
                        </div>

                  </v-col>
            </v-row>
<!--            <v-row  justify="center" align="center">-->
<!--                  <v-col align-self="center" md="2">-->
<!--                        <v-btn x-large color="primary">Login</v-btn>-->
<!--                  </v-col>-->
<!--                  <v-col align-self="center" md="1">-->
<!--                        <router-link tag="v-card" to="/Upload">-->
<!--                              <v-btn x-large color="primary">Upload</v-btn>-->
<!--                        </router-link>-->
<!--                  </v-col>-->
<!--            </v-row>-->

<!--            <div><v-img src="@/assets/16pic_9321443_b.jpg"></v-img></div>-->
      </v-content>
      </v-app>
</template>

<script>
      import { swiper, swiperSlide } from 'vue-awesome-swiper'
      export default {
            name: 'HelloWorld',
            components: {
                  swiper,
                  swiperSlide
            },
            data () {
                  return {

                        //页面布局
                        alignment:'center',
                        //轮播图
                        swiperOption: {
                              autoHeight:true,
                              notNextTick: true,
                              loop:false,
                              //设定初始化时slide的索引
                              initialSlide:0,
                              //自动播放
                              // autoplay:true,
                              autoplay: {
                                  delay: 5000,
                                  stopOnLastSlide: false,
                                  disableOnInteraction: true,
                              },
                              // 设置轮播
                              effect : 'flip',
                              //滑动速度
                              speed:800,
                              //滑动方向
                              direction : 'horizontal',
                              centeredSlides: true,
                              //小手掌抓取滑动
                              // grabCursor : true,
                              //滑动之后回调函数
                              on: {
                                    slideChangeTransitionEnd: function(){
                                          // console.log(this.activeIndex);//切换结束时，告诉我现在是第几个slide
                                    },
                              },
                              //左右点击
                              navigation: {
                                    nextEl: '.swiper-button-next',
                                    prevEl: '.swiper-button-prev',
                              },
                              //分页器设置
                              pagination: {
                                    el: '.swiper-pagination',
                                    clickable :true
                              }
                        },
                        // swiperSlides: [1, 2, 3, 4, 5]
                  }
            },
            computed: {
                  swiper() {
                        return this.$refs.mySwiper.swiper;
                  },
                  results(){
                        return this.$store.getters.results;
                  }
            },
            mounted () {
                  //可以使用swiper这个对象去使用swiper官网中的那些方法
                  this.$nextTick(() => {
                        const swiperTop = this.$refs.swiperTop.swiper
                        const swiperThumbs = this.$refs.swiperThumbs.swiper
                        swiperTop.controller.control = swiperThumbs
                        swiperThumbs.controller.control = swiperTop
                  })
            }
      }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    *{
        margin:0;
        padding: 0;
    }
      #body{
         width: 100%;
            /*opacity: 0.85;*/
            background: url('../assets/poly-bg6.jpg') no-repeat center center fixed;
            background-size: 110% 110%;

      ;
      }
      .text{
          font-size:3vw;
          font-family: 'Times New Roman';
          text-decoration: underline;
          margin-bottom: 5%;
      }
      @media screen and (min-width: 600px){
          .text{
              font-size: 18px;
          }
      }
    .swiper-button-next,
    .swiper-button-prev{
        color: #112533;
        /*height: 10px;*/
        /*width: 5px;*/
    }

      /*#mainpage{*/
      /*    margin: 0;*/
      /*    padding: 0;*/
      /*    width: 100%;*/
      /*    background: url('../assets/12e8a6a547e317524121f7a5d6084036.gif') no-repeat center center fixed;*/
      /*    background-size: cover;*/
      /*}*/
      #upload{
          font-size:20px;
          font-family: Chalkboard;
          text-underline: white;
          margin-top: 20px;
      }
      #title{
          font-weight: bold;
          font-family: "Krungthep";
          color: aliceblue;
          font-size: 30px;
      }
      h1, h2 {
          /*font-family: Tahoma;*/
            color: aliceblue;
            font-weight: normal;
      }
      ul {
            list-style-type: none;
            padding: 0;
      }
      li {
            display: inline-block;
            margin: 0 10px;
      }
      a {
          text-decoration: white ;
      }
      .swiper-container{
            height: 50vw;
            width: 40vw;
      }

</style>
