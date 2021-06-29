<template>
  <div id="app">
    <div id="loading" v-if="loading">
      <img src="/static/img/loading.gif" alt="" height="80">
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data(){
    return {
      loading: false
    }
  },
  created() {
    this.$eventBus.$on("loadingStatus", (payload) => {
      this.loading = payload
    })
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  margin-top: 60px;
}
</style>
