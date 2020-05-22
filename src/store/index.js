import Vue from 'vue'
import Vuex from 'vuex'
import * as firebase from 'firebase'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        user:null,
        recognitions:[],
        resultsAll:[],
        result:{}
    },
    mutations: {
        setUser(state,payload){
            state.user = payload
        },
        recognitionReq(state,payload){
            state.recognitions.push(payload)
        },
        recognitionHis(state,payload){
            state.recognitions = payload
        },
        resultsAll(state,payload){
            state.resultsAll = payload
        },
        setResult(state,payload){
            state.result = payload
        }
    },

    actions: {
        register({commit},payload){
            var newUser = {
                id:'',
            }
            firebase.auth().createUserWithEmailAndPassword(payload.email,payload.password).then(
                (data) => {
                    newUser.id = data.user.uid
                    console.log(newUser)
                    commit('setUser',newUser)
                    }
                ).then(()=>{
                    var username = payload.username
                    var email = payload.email
                    firebase.database().ref('/users/'+newUser.id).set(
                        {
                            uid:newUser.id,
                            username: username,
                            email: email,
                            recognitions:{}
                        }
                    )
                }).catch(
                    error => {
                        alert(error)
                    }
                )

        },
        login({commit},payload){
            firebase.auth().signInWithEmailAndPassword(payload.email,payload.password).then(
                (data) => {
                    const newUser = {
                        id:data.user.uid,

                    }
                    commit('setUser',newUser)


                }).catch(
                    error => {
                        alert(error)
                    }
                )
        },
        recognitionReq({commit, getters},payload){
            const recognition = {
                results:'',
                userId:'',
                date:payload.date.toISOString()
            }
            let imageUrl
            let key
            let extension
            if(getters.user===null){
                recognition.userId = 'undefined'
            }else{
                recognition.userId = getters.user.id
            }
            firebase.database().ref('users/'+recognition.userId+'/recognitions').push(recognition).then((data)=> {
                key = data.key
                return key
            }).then(key=> {
                const filename = payload.image.name
                extension = filename.slice(filename.lastIndexOf('.'))
                return firebase.storage().ref('recognitions/' + key + '.' + extension).put(payload.image)
            }).then(fileData => {
                console.log(key)
                console.log(fileData)
                return firebase.storage().ref('recognitions/' + key + '.' + extension).getDownloadURL()
            }).then((URL)=>{
                imageUrl = URL
                console.log(imageUrl)
                return firebase.database().ref('users/' + recognition.userId + '/recognitions').child(key).update({imageUrl: imageUrl})
            }).then(()=>{
                commit('recognitionReq',{
                    ...recognition,
                    imageUrl:imageUrl,
                    id:key
                })

            }).catch((error)=>{
                console.log(error)
            })

        },
        recognitionAll({commit,getters}){
            firebase.database().ref('users/'+getters.user.id+'/recognitions').once('value').then((data)=>{
                const recognitions = []
                const obj = data.val()
                for(let key in obj){
                    recognitions.push({
                        id:key,
                        imageUrl:obj[key].imageUrl,
                        date:obj[key].date,
                        results:obj[key].results,
                        description:obj[key].description,
                        userId:obj[key].userId
                    })
                }
                commit('recognitionHis',recognitions)
            }).catch((error)=>{
                alert(error)
            })
        },
        results({commit}){
            firebase.database().ref('recognitions').once('value').then((data)=>{
                const resultsAll = []
                const obj = data.val()
                for(let key in obj){
                    if(obj[key].results){
                        resultsAll.push({
                            id:key,
                            imageUrl:obj[key].imageUrl,
                            results:obj[key].results,
                        })
                    }
                }
                const sorted = resultsAll.sort((resultA,resultB)=>{
                    return resultB.results[0].probability - resultA.results[0].probability
                })
                console.log(sorted)
                commit('resultsAll',sorted)
            }).catch((error)=>{
                alert(error)
            })
        },
        autoLogin({commit},payload){
            commit('setUser',{id:payload.uid, recognitions:[]})
        },
        logout({commit}){
            firebase.auth().signOut()
            commit('setUser',null)
        },
        result({commit},payload){
            commit('setResult',payload)
        }
    },
    getters:{
        user(state){
            return state.user
        },
        recognitions(state){
            return state.recognitions.sort((recognitionA,recognitionB)=>{
                return recognitionA.date < recognitionB.date
            })
        },
        recognition(state){
            return (recognitionId)=>{
                return state.recognitions.find((recognition)=>{
                    return recognition.id === recognitionId
                })
            }
        },
        results(state){
            return state.resultsAll
        },
        result(state){
            return state.result
        }
    },
    modules: {

    }
})
