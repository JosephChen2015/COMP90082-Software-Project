<template>
    <v-container>
        <v-layout row wrap>
            <v-flex xs12>
                <v-card id="rec">
                    <v-card-title style="text-align: center" class="justify-center">
                        <h5 class="white--text">Here is your result</h5>
                    </v-card-title>
                    <v-img
                            :src="recognition.imageUrl"
                            width="50%"
                            height="50%"
                            style="border-radius:10%;margin: 0 auto"
                    >
                    </v-img>
                    <v-card-text id="recognition">
                        <div>Date:{{recognition.date}}</div>
                        <div v-for="result in recognition.results" :key="result.name">Result:{{result.name}}<br>  Probability:{{result.probability}}</div>
                        <div v-for="result in recognition.results" :key="result.name">Description:<a style="color: aquamarine;text-decoration:underline " :href="'https://en.wikipedia.org/wiki/'+result.name" >Find more details about {{result.name}} on Wiki</a></div>
                    </v-card-text>
                           <router-link tag="v-card" to="/Upload">
                           <v-btn  large raised color="#47B5AA" style="font-family: Chalkduster">Start Another <br>Recognition
                               <v-icon right dark class="mdi mdi-face-recognition"></v-icon>
                           </v-btn>
                           </router-link>
                    <v-card-actions>

                    </v-card-actions>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    export default {
        name: "Recognition",
        props:['id'],
        computed:{
            recognition(){
                console.log(this.id)
                console.log(this.$store.getters.recognition(this.id))
                return this.$store.getters.recognition(this.id)
            },
            // wiki(){
            //     const url = 'https://en.wikipedia.org/wiki/' + this.$store.getters.recognition(this.id).results[0].name
            //     return url
            // }
        },
    }
</script>

<style scoped>
#rec{
    background: url('../assets/poly-bg6.jpg') no-repeat center center fixed;
    background-size: 110% 110%;
    text-align: center;
}
#recognition{
    font-family: Futura;
    color: white;
}

h5{
    text-align: center;
    font-family: Futura;
    font-size: 5vw;
}
@media screen and (min-width: 800px){
    h5{
        margin-top: 5%;
        font-size: 40px;
    }
}
</style>
