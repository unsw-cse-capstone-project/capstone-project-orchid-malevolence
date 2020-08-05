<!-- Written by Yangyu GAO -->
<template>
    <div class="footer" id="app2">
		<div class="text">
			<span>UNSW COMP9900 Group Project</span>
			<span class="footer-divider"> | </span>
			<span>©2020-2021 Group: capstone project orchid malevolence</span>
		</div>
    </div>
</template>

<script>
    export default {
        name: "homepage_footer"
    }
</script>

<style lang="less" scoped>
    .footer {
        background: #99a9bf;
		//justify-content: center;
		display: table;
    }

	.text {
		display: table-cell;
		vertical-align: middle;
	}

    .span {
        margin: 0 auto;
        font-size: 22px;
    }
</style>