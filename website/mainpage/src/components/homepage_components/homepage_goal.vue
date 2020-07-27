<template>
    <div class="goal mid" id="app_goal">
        <h3 class="title">{{ goal_title }}</h3>

        <div v-if="this.goalStatus===0">
            <div class="text_part">
                <p class="sub-title">Set a monthly goal</p>
            </div>
            <div class="input-group">
                <el-input
                        placeholder="input a number"
                        v-model="textGoal"
                        oninput="value=value.replace(/[^\d]/g,'')"
                        maxLength='3'
                        clearable>
                </el-input>
                <el-button type="warning" plain @click="setGoal()" class="set-goal">Set Goal</el-button>
            </div>
        </div>

        <div v-else>
            <div class="text_part">
                <p>{{ bookData[0].read }} books complete</p>
                <p>{{ Number(bookData[0].totalBook - bookData[0].read) }} books in the schedule</p>
            </div>

            <el-progress :text-inside="true"
                         :stroke-width="26"
                         :percentage="bookData[0].read/bookData[0].totalBook * 100"
                         class="process-bar">
            </el-progress>

            <!-- TODO: 弹窗，reset goal -->
            <el-button type="text" @click="open">Click to reset goal</el-button>
        </div>
    </div>
</template>

<script>
    import {getCurGoal, postCurGoal} from "../../network/requests";

    let now = new Date()
    let nowMonth = now.getMonth() + 1
    let nowYear = now.getFullYear()
    let curMonth = {year:nowYear, month:nowMonth}

    export default {
        name: 'homepage-goal',
        data() {
            return {
                bookData: [{read: '', totalBook: ''}],
                goal_title: nowYear + "-" + nowMonth + " Reading Challenge",
                response: {},
                target: null,
                already_done: null,
                goalStatus: 0,  // 0代表没设置，1代表设置了
                textGoal: '',
            }
        },

        methods: {
            open() {
                this.$prompt('Set a new goal', 'hint', {
                    confirmButtonText: 'Confirm',
                    cancelButtonText: 'Cancel',
                    inputPattern: /^\d{0,3}$/,
                    inputErrorMessage: 'Please input a digit (<1000)'
                }).then(({value}) => {
                    this.$message({
                        type: 'success',
                        message: 'Reset successfully: ' + value
                    });
                    this.setGoal(value)
                    this.$forceUpdate()
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: 'Stop reset'
                    });
                });
            },

            getGoal() {
                getCurGoal(curMonth).then(res=>{
                    console.log("get: ",res)
                    this.goalStatus = 1

                    if(res.status === 400) {
                        this.goalStatus = 0
                        // console.log("need set goal: " + this.goalStatus)
                    }

                    this.bookData[0].read = res.already_done
                    this.bookData[0].totalBook = res.target
                    // console.log("no need to set goal: " + this.goalStatus)
                    // console.log("read: " + res.already_done)
                    // console.log("totalBook: " + res.target)
                }).catch(error => {
                    console.log(error)
                });
            },

            setGoal(value = this.textGoal) {
                if(value === '') {
                    this.$message.error('Please input something.')
                    return
                }

                let data = {month_goal:{month:nowMonth,year:nowYear ,target:value}}
                postCurGoal(data).then(res=>{
                    // console.log("setgoal result: " + res.already_done)
                    // this.bookData[0].read = res.already_done
                    this.goalStatus = 1
                    // this.bookData[0].totalBook = res.target
                    // if(mode===2) {
                    //     // this.textGoal = ''
                    //     // this.$message.success("Reset successfully!")
                    // }
                    // console.log(this.totalBook, this.read, this.goalStatus)
                    this.$forceUpdate()
                    this.$set(this.bookData[0], "read", res.already_done)
                    this.$set(this.bookData[0], "totalBook", value)
                    // console.log(this.bookData[0].totalBook, this.bookData[0].read, this.goalStatus)
                }).catch(error => {
                    console.log(error)
                });
            }
        },

        created() {
            // console.log("curMonth:" + curMonth.month)
            this.getGoal()
        },
    }
</script>

<style lang="less" scoped>
    .goal {
        margin: auto;
        height: 280px;
        width: 270px;
        border-style: solid;
        border-radius: 2px;
        border-color: bisque;
        background-color: darkgrey;
        padding-top: 30px;
    }

    .mid {
        margin-top: 60px;
    }

    .title {

    }

    .sub-title {
        margin-top: 10px;
    }

    .input-group {
        margin-top: 25px;
        float: left;
        height: 40px;
    }

    .el-input {
        margin: 5px 2px 0 2px;;
        width: 60%;
        float: left;
    }

    .set-goal {
        margin: 5px 2px 0 2px;
        height: 100%;
    }

    .el-progress {
        width: 230px;
        margin: 0 auto;
    }
</style>




