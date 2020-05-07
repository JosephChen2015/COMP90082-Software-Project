<template>
    <div class="upload">
        <UploadPage msg="Welcome to Your Vue.js App"/>
    </div>
</template>

<script>
    // @ is an alias to /src
    import UploadPage from '@/components/Upload.vue'

    export default {
        name: 'Upload',
        components: {
            UploadPage
        }
    }
</script>