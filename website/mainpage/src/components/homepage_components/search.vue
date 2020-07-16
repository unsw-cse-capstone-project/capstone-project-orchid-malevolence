<!-- TODO: 搜索框居中，大小固定 -->
<template>
    <div class="search" style="margin-top: 0;">
        <el-input placeholder="input contents" v-model="input3" class="input-with-select">
            <el-select v-model="select" slot="prepend" placeholder="please select">
                <el-option label="New Book" value="1"></el-option>
                <el-option label="Other Users' Book" value="2"></el-option>
                <el-option label="My Book" value="3"></el-option>
            </el-select>
            <el-button slot="append" icon="el-icon-search" ></el-button>
        </el-input>
    </div>
</template>

<script>
    export default {
        name: "search",
        data() {
            return {
                input1: '',
                input2: '',
                input3: '',
                select: ''
            }
        }
    }
</script>

<style lang="less" scoped>
    .search {
        width: 300px;
        margin: 0 auto;
    }

    .el-select .el-input {
        width: 130px;
    }
    .input-with-select .el-input-group__prepend {
        background-color: #fff;
    }
</style>