<template>
    <!-- TODO: 2 type: before set goal, after set goal -->

    <div class="goal mid" id="app_goal">
        <h3>{{ goal_title }}</h3>

        <div v-if="this.goalStatus===0">
            <div class="text_part">
                <p>Set a monthly goal</p>
            </div>
            <div>
                <el-input
                        placeholder="input a number"
                        v-model="goalNum"
                        oninput="value=value.replace(/[^\d]/g,'')"
                        maxLength='3'
                        clearable>
                </el-input>
                <el-button type="warning" plain @click="setGoal">Set Goal</el-button>
            </div>
        </div>

        <div v-else>
            <div class="text_part">
                <p>{{ read }} books complete</p>
                <p>{{ Number(totalBook - read) }} books in the schedule</p>
            </div>

            <el-progress :text-inside="true" :stroke-width="26" :percentage="read/totalBook * 100"></el-progress>

            <!-- TODO: change goal -->
            <div>
                <el-input
                        placeholder="reset your goal"
                        v-model="goalNum"
                        oninput="value=value.replace(/[^\d]/g,'')"
                        maxLength='3'
                        clearable
                        class="input">
                </el-input>
                <el-button type="warning" plain @click="setGoal(2)" class="button2">Reset Goal</el-button>
            </div>

<!--            <el-divider class="divider"></el-divider>-->

        </div>
    </div>
</template>

<script>
    import {getCurGoal, postCurGoal} from "../../network/single_book";

    let now = new Date()
    let nowMonth = now.getMonth() + 1
    let nowYear = now.getFullYear()
    let curMonth = {month:nowMonth}

    export default {
        name: 'homepage-goal',
        data() {
            return {
                read: '',
                totalBook: '',
                goal_title: nowYear + "-" + nowMonth + " Reading Challenge",
                response: {},
                target: null,
                already_done: null,
                goalStatus: 0,  // 0代表没设置，1代表设置了
                goalNum: '',
            }
        },

        methods: {
            getGoal() {
                getCurGoal(curMonth).then(res=>{
                    // console.log(res)
                    this.goalStatus = 1
                    this.read = res.already_done
                    this.totalBook = res.target
                    // console.log("no need to set goal: " + this.goalStatus)
                    // console.log("read: " + res.already_done)
                    // console.log("totalBook: " + this.totalBook)

                    if(res.status === 400) {
                        // TODO: set goal
                        this.goalStatus = 0
                        // this.goalStatus = 0
                        console.log("need set goal: " + this.goalStatus)
                    }
                }).catch(error => {
                    console.log(error)
                });
            },

            setGoal(mode=1) {
                if(this.goalNum === '') {
                    this.$message.error('Please input something.')
                    return
                }

                let data = {month_goal:{month:nowMonth,target:this.goalNum}}
                postCurGoal(data).then(res=>{
                    // console.log("setgoal result: " + res)
                    this.read = res.already_done
                    this.goalStatus = 1
                    this.totalBook = this.goalNum
                    if(mode===2) {
                        this.goalNum = ''
                        this.$message.success("Reset successfully!")
                    }
                    // console.log(this.totalBook, this.read, this.goalStatus)
                    this.$forceUpdate()
                }).catch(error => {
                    console.log(error)
                });
            }
        },

        created() {
            // console.log("curMonth:" + curMonth.month)
            this.getGoal()
        },

        mounted() {
            // this.timer = setInterval(() => {
            //     this.getGoal()
            // })
        },

        // beforeDestroy() {
        //     if (this.timer) {
        //         clearInterval(this.timer);
        //     }
        // },
    }
</script>

<style lang="less" scoped>
    .goal {
        margin: auto;
        height: 330px;
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

    .input {
        margin-top: 20px;
    }

    .button2 {
        margin-top: 5px;
    }
</style>




