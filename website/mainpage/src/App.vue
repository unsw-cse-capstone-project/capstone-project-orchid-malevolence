<template>
    <div id="app">

        <router-view v-if="isRouterAlive"/>
    </div>
</template>

<script>
    // import HelloWorld from './components/HelloWorld.vue'
    export default {



// 第二步: 映射组件标签
        components:{

        },
		provide(){
			return{
				reload: this.reload
			};
		},
		data(){
			return{
				style: '',
				isRouterAlive: true
			};
		},
		methods: {
			reload() {
				this.isRouterAlive = false;
				this.$nextTick(function() {
					this.isRouterAlive = true;
				});
			}
		}
    }
</script>

<!-- 引入stylus -->
<style lang="stylus" rel="stylesheet/stylus">
</style>


<!-- TODO: layout after login -->
<!-- TODO: token save style session->local -->
<!-- TODO: strict login after registered -->
