<template>
    <v-container id="login">
        <v-flex xs12 sm6 offset-sm3>
            <v-card id="loginCard" style="margin-top: 25%" name="LoginCard">
                <v-card-text>
                    <v-container>
                        <form  @submit.prevent="onLogin">
                            <v-layout row>
                                <v-flex xs12>
                                    <v-text-field
                                            background-color="rgba(193, 195, 196, 0.56)"
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
                                            background-color="rgba(193, 195, 196, 0.56)"
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
                            <v-layout style="text-align: center" row>
                                <v-flex xs12>
                                    <v-btn style="background-color: rgba(193, 195, 196, 0.56)" type="submit">Login</v-btn>
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
<style>
    #loginCard{
        background: rgba(193, 195, 196, 0.56);
    }


</style>
