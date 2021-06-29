<template>
  <div>
    <h1>Latest Products</h1>
    <hr>
    <div class="product" v-for="(p, i) in allProducts" :key="i">
        <router-link :to="'/shop/product/'+ p.id">
            <div class="productContainer">
                <img :src="'http://localhost:8000/static'+p.img" alt="">
                <br><br>
                <strong>{{ p.name }}</strong>
                <p class="price"> &#2547; {{ p.price }}</p>
            </div>
        </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ShopProducts',
  data () {
    return {
      allProducts: []
    }
  },
  mounted(){
    this.init();
  },
  methods: {
      async init(){
          await this.$eventBus.$emit("loadingStatus", true);
          await this.$axios.get("http://localhost:8000/api/product")
          .then(res=> {
            console.log(res.data)
            this.allProducts = res.data
          })
          this.$eventBus.$emit("loadingStatus", false);
      }
  }
}
</script>
