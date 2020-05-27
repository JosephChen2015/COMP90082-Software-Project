<template>
    <v-container>
        <v-layout row wrap v-for="recognition in recognitions" :key="recognition.id" class="mb-2">
            <v-flex xs12 sm10 md8 offset-sm1 offset-md2>
                <v-card class="info">
                    <v-container fluid style="padding:0">
                        <v-layout style="background-color: gray; margin-bottom: 5%" row>
                            <v-flex xs5 sm4 md3>
                                <v-img
                                    :src="recognition.imageUrl"
                                    height="150px"
                                    style="border-radius: 5px"
                                    >
                                </v-img>
                            </v-flex>
                            <v-flex xs7 sm8 md9>
                                <v-card-title primary-title>
                                    <div>
                                        <h4 class="white--text mb-0">Recognition</h4>
                                        <div>{{recognition.date}}</div>
                                    </div>
                                </v-card-title>
                                <v-card-actions>
                                    <v-btn text class="white--text" @click="onLoadRecognition(recognition.id)">
                                        <v-icon left light class="mdi mdi-arrow-left-thick"></v-icon>
                                        View Results
                                    </v-btn>
                                </v-card-actions>

                            </v-flex>
                        </v-layout>
                    </v-container>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    export default {
        name: "History",
        computed:{
            recognitions(){
                return this.$store.getters.recognitions
            },
        },
        methods:{
            onLoadRecognition(id){
                this.$router.push('/History/'+id)
            }
        }
    }
</script>

<style scoped>

</style>
