<template>
    <v-container>
        <v-layout row wrap>
            <v-flex xs12>
                <v-card id="res">
                    <v-card-title class="justify-center">
                        <h5 class="white--text">Here is your result</h5>
                    </v-card-title>
                    <v-img
                            :src="result.imageUrl"
                            width="50%"
                            height="50%"
                            style="border-radius:10%;margin: 0 auto"
                    >
                    </v-img>
                    <v-card-text style="text-align: center; font-family: Futura" id="result">

                        <div v-for="(detail,result) in result.results" :key="detail.name"><div id="name">This is {{detail.name}}</div><div class="detail"> Probability:{{detail.probability}}</div>
                            <div><a style="color: aquamarine;text-decoration:underline; margin-bottom: 2px" :href="'https://en.wikipedia.org/wiki/'+result.name" >Find more details about {{result.name}} on Wiki</a></div>
                        </div>
<!--                        <div v-for="result in result.results" :key="result.name"><a style="color: aquamarine;text-decoration:underline " :href="'https://en.wikipedia.org/wiki/'+result.name" >Find more details about {{result.name}} on Wiki</a></div>-->
                        <div style="text-align: center">
                            <router-link tag="v-card" to="/Upload">
                                <v-btn  large raised color="#47B5AA" style="margin-top:2%; font-family: Chalkduster">Start Another <br>Recognition
                                    <v-icon right dark class="mdi mdi-face-recognition"></v-icon>
                                </v-btn>
                            </router-link>
                        </div>

                    </v-card-text>
                    <v-card-actions>

                    </v-card-actions>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    export default {
        name: "Result",

        computed:{
            result(){
                console.log(this.$store.getters.result)
                return this.$store.getters.result
            },
            // wiki(){
            //     const url = 'https://en.wikipedia.org/wiki/' + this.$store.getters.result.results[0].name
            //     return url
            // }
        },
    }
</script>

<style scoped>
#res{
    background: url('../assets/poly-bg6.jpg') no-repeat center center fixed;
    background-size: 110% 110%;
}
#result{
    font-family: Futura;
    color: white;
}
    h5{
        text-align: center;
        font-family: Futura;
        font-size: 5vw;
    }
    #name{
        font-size:3vw;
        /*margin: 0 0;*/
    }
    .detail{
        font-size: 1vw;
    }

@media screen and (min-width: 800px){
    h5{
        margin-top: 5%;
        font-size: 40px;
    }
    #name{
        font-size: 24px;
        margin:0 0;
    }
}

</style>
