<template>
    <v-container>
        <v-layout row wrap>
            <v-flex xs12>
                <v-card>
                    <v-card-title>
                        <h5 class="primary--text">Recognition</h5>
                    </v-card-title>
                    <v-img
                            :src="result.imageUrl"
                            style="border-radius: 5px"
                    >
                    </v-img>
                    <v-card-text>
                        <div v-for="detail in result.results" :key="detail.name">Result:{{detail.name}}  Probability:{{detail.probability}}</div>
                        <div v-for="detail in result.results" :key="detail.name">Description:<a :href="'https://en.wikipedia.org/wiki/'+detail.name" >Find more details about {{detail.name}} on Wiki</a></div>
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

</style>