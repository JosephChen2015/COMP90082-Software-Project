

module.exports = {
  // publicPath:'/dist',
  "transpileDependencies": [
    "vuetify"
  ],
  devServer:{
    proxy:{
      // '/api2':{
      //   target:'http://localhost:3000',
      //   changeOrigin:true,
      // },
      '/recog':{
        target:'http://115.146.95.169:5000',
        changeOrigin: true,//反向代理的时候是否要改变地址
        pathRewrite:{
          '^/recog':'/recog'
        }
      },
    }
  },

}