<template>
    <v-container>
        <v-layout row>
            <v-flex xs12>
                <form @submit.prevent="onUpload" style="margin-top:10%; text-align: center">
                    <v-layout row>
                        <v-flex xs12 sm6 offset-sm3 style="margin-bottom: 5%">
                            <h1 style="font-family: Krungthep">Start a Recognition!</h1>
                        </v-flex>
                    </v-layout>
                    <v-layout row>
                        <v-flex xs12 sm6 offset-sm3>
                            <v-btn  x-large raised color="#47B5AA" style="margin-bottom: 5%; font-family: Chalkduster" @click="onPickFile">Upload Image
                                <v-icon right dark class="mdi mdi-cloud-upload"></v-icon>
                            </v-btn>
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
                            <v-btn x-large color="#47B5AA" style="margin-top: 5%; font-family: Chalkduster" :disabled="!formIsValid" type="submit">Recognize
                                <v-icon right class="mdi mdi-face-recognition"></v-icon>
                            </v-btn>
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
                // const imageData = {
                //     image:this.image,
                //     date:new Date(),
                // }
                // this.$store.dispatch('recognitionReq',imageData)
                this.imageBase64 = this.imageUrl.slice(this.imageUrl.lastIndexOf(',')+1)
                this.axios.post('/recog/recogUploadApi',{uid:this.uid,imageBase64:this.imageBase64,date:new Date()}).then((res)=> {
                    if(res.data.classified){
                        this.result=res.data
                        console.log(this.result)
                        this.$store.dispatch('result', this.result)
                        this.$router.push('/Result')
                    }else{
                        alert('Sorry, our system is failed to recognize the person in the uploaded picture.')
                    }
                }).catch((error)=>{
                    alert(error)
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
