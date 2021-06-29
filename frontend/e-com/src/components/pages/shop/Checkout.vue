<template>
  <div>
    <h1 class="fleft">Delivery Information</h1>
    <router-link to="/shop/products" class="fright">All Product</router-link>
    <div class="clear"></div>
    <hr>
    <table>
        <tr>
            <td>
                Full Name
            </td>
            <td>
                <input type="text" placeholder="Full Name">
            </td>
        </tr>

        <tr>
            <td>
                City
            </td>
            <td>
                <select name="" id="">
                    <option value="">
                        --Select One--
                    </option>
                    <option value="">Dhaka</option>
                    <option value="">Rajshahi</option>
                    <option value="">Chittagon</option>
                    <option value="">Jessore</option>
                </select>
            </td>
        </tr>

        <tr>
            <td>
                Address
            </td>
            <td>
                <textarea name="" id="" cols="30" rows="10" placeholder="Write delivery description"></textarea>
            </td>
        </tr>

        <tr>
            <td>
                Mobile
            </td>
            <td>
                <input type="text" placeholder="Mobile">
            </td>
        </tr>

        <tr>
            <td>
                Payment Method
            </td>
            <td>
                <select name="" id="">
                    <option value="">
                        --Select one--
                    </option>
                    <option value="">Cash on delivery</option>
                    <option value="">Bkash</option>
                    <option value="">Master Card</option>
                </select>
            </td>
        </tr>

        <tr>
            <td>

            </td>
            <td>
                <button class="btnSave" @click="orderNow()">Order Now</button>
            </td>
        </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'Checkout',
  data () {
    return {
      mgs: 'Shop'
    }
  },
  mounted(){
      
  },
  methods: {
      orderNow(){
          this.$eventBus.$emit("loadingStatus", true);
        this.$axios.post("", {})
          .then(res => {
              this.$eventBus.$emit("loadingStatus", false)
              this.showingAddModal = false
                this.$iziToast.success({
                  title: 'Success',
                  message: "res.data.message"
                })
                this.$eventBus.$emit("clearCart")
                this.$router.push({path: '/shop/products'});
          })
          .catch(err => {
            this.$eventBus.$emit("loadingStatus", false)
            this.showingAddModal = false
            this.$iziToast.error({
              title: 'Error',
              message: "err.response.data.error "
            })
            this.$eventBus.$emit("clearCart")
            this.$router.push({path: '/shop/products'});
          })
      }
  }
}
</script>
