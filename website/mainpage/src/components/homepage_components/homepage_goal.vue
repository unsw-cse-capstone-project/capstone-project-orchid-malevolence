<!-- Written by Yangyu GAO -->
<template>
    <div class="goal mid" id="app_goal">
        <h3 class="title">{{ goal_title }}</h3>

		<!-- if not set goal yet -->
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
	
		<!-- if set goal -->
        <div v-else>
			<!-- if read book less than monthly goal -->
            <div class="text_part" v-if="Number(bookData[0].totalBook - bookData[0].read) > 0">
                <p>{{ bookData[0].read }} books complete</p>
                <p>{{ Number(bookData[0].totalBook - bookData[0].read) }} books in the schedule</p>
            </div>

			<!-- if read book larger than monthly goal -->
			<div class="text_part" v-else>
				<p style="color: firebrick">Congratulate! You have complete your monthly goal.</p>
			</div>
			
			<!-- show goal progress by a progress bar -->
            <el-progress :text-inside="true" :show-text="false"
                         :stroke-width="26"
                         :percentage="bookData[0].read/bookData[0].totalBook * 100"
                         class="process-bar">
            </el-progress>

            <!-- Click to reset goal -->
<!--            <el-button @click="open" style="color: lightskyblue">Click to reset goal</el-button>-->

            <el-button @click="dialogFormVisible = true">Reset Goal</el-button>

            <el-dialog title="Reset Monthly Goal" :visible.sync="dialogFormVisible">
                <el-form :model="form">
                    <el-form-item label="Set a new goal" :label-width="formLabelWidth">
                        <el-input v-model="form.name" autocomplete="off"></el-input>
                    </el-form-item>
                </el-form>
                <div slot="footer" class="dialog-footer">
                    <el-button @click="dialogFormVisible = false">取 消</el-button>
                    <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
                </div>
            </el-dialog>
            
        </div>
    </div>
</template>

<script>
    import {getCurGoal, postCurGoal} from "../../network/requests";

    /* get date */
    let now = new Date()
    let nowMonth = now.getMonth() + 1
    let nowYear = now.getFullYear()

    export default {
        name: 'homepage-goal',
        data() {
            return {
                bookData: [{read: '', totalBook: ''}],
                goal_title: nowYear + "-" + nowMonth + " Reading Challenge",
                response: {},
                target: null,
                already_done: null,
                goalStatus: 0,  // 0: false, 1: true
                textGoal: '',
                dialogFormVisible: false,
                form: {
                    name: '',
                    region: '',
                    date1: '',
                    date2: '',
                    delivery: false,
                    type: [],
                    resource: '',
                    desc: ''
                },
                formLabelWidth: '120px'
            }
        },

        methods: {
			/* enforce user input format, number in range of [0, 1000) */
            open() {
                this.$prompt('Set a new goal', 'Reset Goal', {
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

			/* get current user's monthly goal, if not yet set, change goalStatus to 0, else to 1 */
            getGoal() {
				let params = {year:nowYear,month:nowMonth}
                getCurGoal(params).then(res=>{
                    console.log("get: ",res)
                    if(res.already_done === 0 & res.target === 0) {
                        this.goalStatus = 0
                    } else {
						this.goalStatus = 1
					}

                    this.bookData[0].read = res.already_done
                    this.bookData[0].totalBook = res.target
                }).catch(error => {
                    console.log(error)
                });
            },

			/* if no input, pop error window, end function */
            setGoal(value = this.textGoal) {
				if(value === '') {
                    this.$message.error('Please input a goal number.')
                    return
                }

                // if have input, send new data to server
                let data = {month_goal:{month:nowMonth,year:nowYear ,target:value}}
                postCurGoal(data).then(res=>{
                    this.goalStatus = 1
                    this.$forceUpdate()
                    this.$set(this.bookData[0], "read", res.already_done)
                    this.$set(this.bookData[0], "totalBook", value)
                }).catch(error => {
                    console.log(error)
                });
            }
        },

        created() {
            this.getGoal()
        },
    }
</script>

<style lang="less" scoped>
    .goal {
        margin: auto;
        height: 240px;
        width: 270px;
        border-style: solid;
        border-radius: 2px;
        border-color: bisque;
        background-color: ivory;
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
    
    .el-button {
		margin-top: 20px;
    }
</style>




