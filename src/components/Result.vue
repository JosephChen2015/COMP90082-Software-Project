<template>
    <v-container>
        <v-layout row wrap>
            <v-flex xs12>
                <v-card id="res">
                    <v-card-title>
                        <h5 class="white--text">Here is your result</h5>
                    </v-card-title>
                    <v-img
                            :src="result.imageUrl"
                            style="border-radius: 5px"
                    >
                    </v-img>
                    <v-card-text style="text-align: center" id="result">

                        <div v-for="detail in result.results" :key="detail.name">Result:{{detail.name}}<br>  Probability:{{detail.probability}}</div>
                        <div v-for="detail in result.results" :key="detail.name">Description:<a style="color: aquamarine;text-decoration:underline " :href="wiki" >Find more details about {{detail.name}} on Wiki</a></div>

                        <div style="text-align: center">
                            <router-link tag="v-card" to="/Upload">
                                <v-btn  large raised color="#47B5AA" style="margin-top: 2%; font-family: Chalkduster">Upload Another Image
                                    <v-icon right dark class="mdi mdi-cloud-upload"></v-icon>
                                </v-btn>
                            </router-link>
                        </div>

                        <v-col></v-col>
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
            wiki(){
                const url = 'https://en.wikipedia.org/wiki/' + this.$store.getters.result.results[0].name
                return url
            }
        },
    }
</script>

<style scoped>
#res{
    background: url('../assets/poly-bg6.jpg') no-repeat center center fixed;
    background-size: 110%;
}
#result{
    font-family: Futura;
    color: white;
}
    h5{
        text-align: center;
        font-family: Futura;
        font-size: 20px;
    }
</style>
