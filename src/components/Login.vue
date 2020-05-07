<template>
    <v-container>
        <v-flex xs12 sm6 offset-sm3>
            <v-card name="LoginCard">
                <v-card-text>
                    <v-container>
                        <form @submit.prevent="onLogin">
                            <v-layout row>
                                <v-flex xs12>
                                    <v-text-field
                                            solo
                                            name="email"
                                            lable="Mail"
                                            id="email"
                                            v-model="email"
                                            type="email"
                                            required
                                            placeholder="Email">

                                    </v-text-field>
                                </v-flex>
                            </v-layout>
                            <v-layout row>
                                <v-flex xs12>
                                    <v-text-field
                                            solo
                                            required
                                            name="password"
                                            lable="Password"
                                            id="password"
                                            v-model="password"
                                            type="password"
                                            placeholder="Password">

                                    </v-text-field>
                                </v-flex>
                            </v-layout>
                            <v-layout row>
                                <v-flex xs12>
                                    <v-btn type="submit">Login</v-btn>
                                </v-flex>
                            </v-layout>
                        </form>
                    </v-container>
                </v-card-text>
            </v-card>
        </v-flex>
    </v-container>
</template>

<script>
    export default{
        data(){
            return{
                email:'',
                password:'',

            }
        },
        computed:{
            user(){
                return this.$store.getters.user
            }
        },
        watch:{
            user(value){
                if(value !== null&&value !==undefined){
                    this.$router.push('/')
                }
            }
        },
        methods:{
            onLogin(){
                this.$store.dispatch('login',{email:this.email,password:this.password})
            }
        }
    }
</script>