<template>
  <div class="admin">
    <div id="header">
        <h1 class="fleft"> Simple Ecomerce </h1>
        <a href="#" class="fright" @click="logoutNow()">
            Logout
        </a>
    </div>

    <LeftSidebar />

    <div id="main">
        <router-view />
    </div>
  </div>
</template>

<script>
import LeftSidebar from "../../others/LeftSidebar.vue"

export default {
  name: 'Admin',
  data () {
    return {
      
    }
  },
  mounted(){
      var token = localStorage.getItem("token");
      if(!token){
        //   this.$router.push({name: "login"});
      }
  },
  methods: {
      logoutNow(){
          localStorage.setItem("token", "");
          this.$router.push({name: "login"});
      }
  },
  components: {
      LeftSidebar
  }
}
</script>
