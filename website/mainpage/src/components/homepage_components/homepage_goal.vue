<template>
    <div class="goal" id="app_goal">
        {{ goal_title }}
    </div>

</template>

<script>

    const now = new Date()
    const nowMonth = now.getMonth() + 1
    const nowYear = now.getFullYear()

    export default {
        name: 'homepage-goal',

        data() {
            return {
                goal_title: nowYear + "-" + nowMonth + " Reading Challenge"
            }
        }
    }



</script>

<style lang="less" scoped>
    .goal {
        margin: auto;
        height: 200px;
        width: 200px;
        border-radius: 2px;
        background: crimson;
        padding-top: 30px;
    }
</style>




