<template>
    <div id="cartContainer">
            <h1>{{ myAppName }}</h1>
            <h2>Your Cart</h2>
            <hr>
            <table class="cart">
                <tr>
                    <th>Product</th>
                    <th>Quantity</th>
                    <th>Price</th>
                    <th> - </th>
                </tr>

                <tr v-for="(item,i) in cart" :key="i">
                    <td>{{item.product.name}}</td>
                    <td><input type="number" class="input-number" v-model="item.quantity"></td>
                    <td> &#2547; {{ item.product.price * item.quantity }}</td>
                    <td> <button @click="removeItem(i)"> - </button> </td>
                </tr>
                <tr>
                    <td colspan="4">
                        <hr>
                    </td>
                </tr>

                <tr>
                    <td></td>
                    <td>Total = </td>
                    <td colspan="2"> &#2547; {{total}}</td>
                </tr>
            </table>

            <br><br>

            <p class="txt-center">
                <router-link to="/shop/checkout" class="addBtn">Checkout</router-link>
            </p>
        </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    data() {
        return {
            
        }
    },
    computed: {
        // myAppName() {
        //     return this.$store.getters.getAppName
        // },
        // cart() {
        //     return this.$store.getters.getCart;
        // },
        // total() {
        //     return this.$store.getters.getTotal;
        // }
        ...mapGetters({
            'myAppName': 'getAppName',
            'cart': 'getCart',
            'total': 'getTotal'
        })
    },
    methods: {
        removeItem(i){
            this.$store.commit("removeFromCart", i)
        }
    }
}
</script>