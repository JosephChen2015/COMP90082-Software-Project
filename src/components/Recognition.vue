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
                        <div>Result:{{recognition.result}}</div>
                        <div>Description</div>
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
            }
        }
    }
</script>

<style scoped>

</style>