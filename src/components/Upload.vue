<template>
    <v-container>
        <v-layout row>
            <v-flex xs12>
                <form @submit.prevent="onUpload">
                    <v-layout row>
                        <v-flex xs12 sm6 offset-sm3>
                            <h1>Start a Recognition!</h1>
                        </v-flex>
                    </v-layout>
                    <v-layout row>
                        <v-flex xs12 sm6 offset-sm3>
                            <v-btn raised class="primary" @click="onPickFile">Upload Image</v-btn>
                            <input type="file"
                                   style="display:none"
                                   ref="fileInput"
                                   accept="image/*"
                                   @change="onFilePicked">
                        </v-flex>
                    </v-layout>
                    <v-layout row>
                        <v-flex xs12 sm6 offset-sm3>
                            <img :src="imageUrl" height="150">
                        </v-flex>
                    </v-layout>
                    <v-layout row>
                        <v-flex xs12 sm6 offset-sm3>
                            <v-btn class="primary" :disabled="!formIsValid" type="submit">Recognize</v-btn>
                        </v-flex>
                    </v-layout>
                </form>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    export default {
        data(){
            return {
                imageUrl:'',
                image:null,
                imageBase64:'',
                uid:'',
                result:{}
            }
        },
        computed:{
            formIsValid(){
                return this.imageUrl !== ''
            }
        },
        methods:{
            onUpload(){
                if(!this.formIsValid){
                    return
                }
                if(!this.image){
                    return
                }
                if(this.$store.getters.user===null){
                    this.uid = 'undefined'
                }else{
                    this.uid = this.$store.getters.user.id
                }
                const imageData = {
                    image:this.image,
                    date:new Date(),
                }
                this.$store.dispatch('recognitionReq',imageData)
                this.imageBase64 = this.imageUrl.slice(this.imageUrl.lastIndexOf(',')+1)
                this.axios.post('/recog/recogUploadApi',{uid:this.uid,imageBase64:this.imageBase64,date:new Date()}).then((res)=> {
                    this.result=res.data
                    console.log(this.result)
                    this.$store.dispatch('result', this.result)
                    this.$router.push('/Result')
                })
            },
            onPickFile(){
                this.$refs.fileInput.click()
            },
            onFilePicked(event){
                const files = event.target.files

                let filename = files[0].name
                if(filename.lastIndexOf('.')<=0){
                    return alert('Please choose a valid file!')
                }
                const fileReader = new FileReader()
                fileReader.addEventListener('load',()=>{
                    this.imageUrl = fileReader.result

                })
                fileReader.readAsDataURL(files[0])
                this.image = files[0]

                console.log(this.uid)
            }
        }
    }
</script>