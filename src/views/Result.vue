<template>
    <div class="result">
        <ResultPage msg="Welcome to Your Vue.js App"/>
    </div>
</template>

<script>
    // @ is an alias to /src
    import ResultPage from '@/components/Result.vue'

    export default {
        name: 'Result',
        components: {
            ResultPage
        }
    }
</script>