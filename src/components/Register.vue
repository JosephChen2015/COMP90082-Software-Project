<template>
    <v-container>
        <v-flex xs12 sm6 offset-sm3>
            <v-card id="RegisterCard" style="margin-top: 20%" name="registerCard">
                <v-card-text>
                    <v-container>
                        <form @submit.prevent="onRegister">
                            <v-layout row>
                                <v-flex xs12>
                                    <v-text-field
                                            background-color="rgba(193, 195, 196, 0.56)"
                                            solo
                                            name="username"
                                            lable="Username"
                                            id="username"
                                            v-model="username"
                                            type="username"
                                            required
                                            placeholder="Username">

                                    </v-text-field>
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
                            <v-layout row>
                                <v-flex xs12>
                                    <v-text-field
                                            background-color="rgba(193, 195, 196, 0.56)"
                                            solo
                                            required
                                            placeholder="Confirm Password"
                                            name="confirmPassword"
                                            lable="Confirm Password"
                                            id="confirmPassword"
                                            v-model="confirmPassword"
                                            type="password"
                                            :rules="[comparePasswords]">

                                    </v-text-field>
                                </v-flex>
                            </v-layout>
                            <v-layout style="text-align: center" row>
                                <v-flex xs12>
                                    <v-btn style="background-color: rgba(193, 195, 196, 0.56)" type="submit">Register</v-btn>
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
                username:'',
                email:'',
                password:'',
                confirmPassword:'',
            }
        },
        computed:{
            comparePasswords(){
                return this.password !== this.confirmPassword ? 'Password does not match!':''
            },
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
            onRegister(){
                this.$store.dispatch('register',{username:this.username,email:this.email,password:this.password})
            }
        }
    }
</script>
<style>
    #RegisterCard{
        background: rgba(193, 195, 196, 0.56);
    }
</style>
