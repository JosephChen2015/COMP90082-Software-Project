<template>
    <v-container>
        <v-layout row wrap>
            <v-flex xs12>
                <v-card>
                    <v-card-title>
                        <h5 class="primary--text">Recognition</h5>
                    </v-card-title>
                    <v-img
                            :src="recognition.imageUrl"
                            height="400px"
                            style="border-radius: 5px"
                    >
                    </v-img>
                    <v-card-text>
                        <div>Date:{{recognition.date}}</div>
                        <div v-for="result in recognition.results" :key="result.name">Result:{{result.name}}  Probability:{{result.probability}}</div>
                        <div v-for="result in recognition.results" :key="result.name">Description:<a :href="'https://en.wikipedia.org/wiki/'+result.name" >Find more details about {{result.name}} on Wiki</a></div>
                        <div ></div>
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

</style>