<template>
    <v-container>
        <v-layout row wrap>
            <v-flex xs12>
                <v-card>
                    <v-card-title>
                        <h5 class="primary--text">Recognition</h5>
                    </v-card-title>
                    <v-img
                            src="https://pic4.zhimg.com/80/v2-3186cceadf7ac4bf46152160cb787704_720w.jpg"
                            height="400px"
                            style="border-radius: 5px"
                    >
                    </v-img>
                    <v-card-text>
                        <div>Date</div>
                        <div>Result</div>
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
        name: "Result",

    }
</script>

<style scoped>

</style>