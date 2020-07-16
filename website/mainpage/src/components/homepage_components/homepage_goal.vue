<template>
    <!-- TODO: 2 type: before set goal, after set goal -->

    <div class="goal mid" id="app_goal">
        <h3>{{ goal_title }}</h3>

        <div class="text_part">
            <p>{{ alComplete }} books complete</p>
            <p>{{ notComplete }} books in the schedule</p>
        </div>

        <el-progress :text-inside="true" :stroke-width="26" :percentage="percent"></el-progress>

        <el-divider class="divider"></el-divider>
    </div>
</template>

<script>

    const now = new Date()
    const nowMonth = now.getMonth() + 1
    const nowYear = now.getFullYear()
    let read = 5
    let totalBook = 10

    export default {
        name: 'homepage-goal',
        data() {
            return {
                percent: read/totalBook * 100,
                goal_title: nowYear + "-" + nowMonth + " Reading Challenge",
                alComplete: read,
                notComplete: Number(totalBook - read),
            }
        }
    }
</script>

<style lang="less" scoped>
    .goal {
        margin: auto;
        height: 250px;
        width: 270px;
        border-radius: 2px;
        background: crimson;
        padding-top: 30px;
    }

    .mid {
        margin-top: 60px;
    }

    .divider {
        background-color: black;
        height: 2px;
    }
</style>




