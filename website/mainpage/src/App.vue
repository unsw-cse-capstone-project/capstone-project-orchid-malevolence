<template>
    <div id="app">

        <router-view v-if="isRouterAlive"/>
    </div>
</template>

<script>
    // import HelloWorld from './components/HelloWorld.vue'
    export default {

// Step 2: Map component labels
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

<!-- The introduction of stylus -->
<style lang="stylus" rel="stylesheet/stylus">
</style>


<!-- TODO: strict login after registered -->
