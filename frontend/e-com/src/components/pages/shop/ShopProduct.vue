<template>
  <div>
    <h1 class="fleft">{{product.name}}</h1>
    <router-link to="/shop/products" class="fright">All products</router-link>
    <div class="clear"></div>
    <hr>
    
    <div class="product-left">
        <img :src="'http://localhost:8000/static'+product.img" alt="">
        <br>
    </div>

    <div class="product-right">
        <div class="product-description">
            <p>
                <strong>Category : </strong> {{product.category}} <br><br>
                <strong>Supplier : </strong> {{product.supplier}} <br><br>
                <strong>Price : </strong> {{product.price}} <br><br>
                <strong>Description : </strong> {{product.description}} <br><br>
            </p>
            <strong>Quantity: </strong>

            <input type="number" class="input-number" v-model="qty">
            <button class="addBtn" @click="addToCart()">Add to cart</button>
        </div>
    </div>

    <div class="clear"></div>
    <hr><br><br><br>
    <p class="txt-center">
        <router-link to="/shop/products" class="addBtn">Continue Shopping</router-link>
    </p>
  </div>
</template>

<script>
export default {
  name: 'ShopProduct',
  data () {
    return {
      productId: 0,
      product:{
        name: "",
        description: "",
        supplier: "",
        category: "",
        price: 0,
        img: "/images/default.jpg"
      },
      qty: 1
    }
  },
  mounted(){
      this.productId = this.$route.params.pid;
      console.log(this.product)
      this.init();
  },
  methods: {
      async init(){
          await this.$eventBus.$emit("loadingStatus", true);
          await this.$axios.get("http://localhost:8000/api/product/view/" + this.productId)
          .then(res=> {
            this.product = res.data
          })
          await this.$eventBus.$emit("loadingStatus", false);
      },

      addToCart() {
          // this.$store.commit("addToCart", {product: this.product, quantity: this.qty})
          this.$store.dispatch("addToCartByActions", {product: this.product, quantity: this.qty})
      }
  }
}
</script>
