<template>
  <div class="login">
    <div class="loginHeader">
        User Login
    </div>

    <div class="loginContainer">
        <table>
            <tr>
                <td>Username</td>
                <td>:</td>
                <td><input type="text" placeholder="Username" v-model="user.email"></td>
            </tr>

            <tr>
                <td>Password</td>
                <td>:</td>
                <td><input type="text" placeholder="Password" v-model="user.password"></td>
            </tr>

            <tr>
                <td></td>
                <td></td>
                <td><button class="addBtn" @click="loginNow()">Login</button></td>
            </tr>
        </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      user: {
          email: "",
          password: ""
      }
    }
  },
  methods: {
      loginNow(){
          // console.log(this.user)
          this.$eventBus.$emit("loadingStatus", true);
          this.$axios.post("http://localhost:8000/api/login", this.user)
          .then(res => {
              this.$eventBus.$emit("loadingStatus", false)
              // console.log(res.data);
              localStorage.setItem("token", res.data["jwt"])
              // this.$axios.defaults.headers.common['Authorization'] = 'Token' + localStorage.getItem("token");
              this.$router.push({name: "admin"});
          })
          .catch(err => {
            // alert(err.response.data["detail"])
            this.$eventBus.$emit("loadingStatus", false)
            this.$iziToast.error({
              title: 'Error',
              message: err.response.data["detail"] 
            })
          })
      }
  }
}
</script>
