
<template>
      <v-app id="carousel">
      <v-content>
<!--      <v-container class="fill-height ma-0 pa-0"-->
<!--                        fluid-->
<!--      >-->
            <v-row class="mb-12">
                  <v-col class="mx-auto my-0"  style="height: 600px" cols="10">
                        <div class="scroll">
                              <swiper :options="swiperOption" ref="mySwiper">
                                    <!-- slides -->
                                    <swiper-slide><v-img :src="results[0].imageUrl" style="border-radius: 5px; max-height:500px; max-width:500px"></v-img></swiper-slide>
                                    <swiper-slide><v-img :src="results[1].imageUrl" style="border-radius: 5px; max-height:500px; max-width:500px"></v-img></swiper-slide>
                                    <swiper-slide><v-img :src="results[2].imageUrl" style="border-radius: 5px; max-height:500px; max-width:500px"></v-img></swiper-slide>
                                    <swiper-slide><v-img :src="results[3].imageUrl" style="border-radius: 5px; max-height:500px; max-width:500px"></v-img></swiper-slide>
                                    <swiper-slide><v-img :src="results[4].imageUrl" style="border-radius: 5px; max-height:500px; max-width:500px"></v-img></swiper-slide>
<!--                                    <swiper-slide>1</swiper-slide>-->
<!--                                    <swiper-slide>2</swiper-slide>-->
<!--                                    <swiper-slide>3</swiper-slide>-->
<!--                                    <swiper-slide>4</swiper-slide>-->
<!--                                    <swiper-slide>5</swiper-slide>-->

                                    <!-- Optional controls -->
                                    <div class="swiper-pagination "  slot="pagination"></div>
                                    <div class="swiper-button-prev swiper-button-black" slot="button-prev"></div>
                                    <div class="swiper-button-next swiper-button-black" slot="button-next"></div>
                                    <!-- <div class="swiper-scrollbar"   slot="scrollbar"></div> -->
                              </swiper>
                        </div>

                  </v-col>
            </v-row>
            <v-row  justify="center" align="center">
                  <v-col align-self="center" md="2">
                        <v-btn x-large color="primary">Login</v-btn>
                  </v-col>
                  <v-col align-self="center" md="1">
                        <router-link tag="v-card" to="/Upload">
                              <v-btn x-large color="primary">Upload</v-btn>
                        </router-link>
                  </v-col>
            </v-row>
<!--            <v-row class="mx-auto">-->
<!--                  <v-col>-->
<!--                        <v-btn>Login</v-btn>-->
<!--                  </v-col>-->
<!--                  <v-col>-->
<!--                        <v-btn>Upload</v-btn>-->
<!--                  </v-col>-->
<!--            </v-row>-->
<!--            <v-row class="mx-auto">-->
<!--                  <v-col-->
<!--                        cols="2"-->
<!--                        style="height: 500px"-->
<!--                  >-->
<!--                        <v-btn>Login</v-btn>-->
<!--                  </v-col>-->
<!--                  <v-col-->
<!--                        cols="6"-->
<!--                        md="2"-->
<!--                  >-->
<!--                        <v-btn>Upload</v-btn>-->
<!--                  </v-col>-->
<!--            </v-row>-->

<!--      </v-container>-->
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
                              notNextTick: true,
                              loop:true,
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
<style scoped>
      h1, h2 {
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
            color: #42b983;
      }
      .swiper-slide{
            height:500px;
      }

</style>
