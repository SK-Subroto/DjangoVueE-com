import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

import createPersistedState from 'vuex-persistedstate';

const store = new Vuex.Store({
    state: {
        appName: "Sk Shop",
        cart: []
    },
    getters: {
        getAppName: state => {
            return state.appName;
        },

        getCart: state => {
            return state.cart;
        },

        getTotal: state => {
            var total = 0;
            for(var i = 0; i<state.cart.length; i++){
                var item = state.cart[i];
                total += item.quantity * item.product.price
            }

            return total;
        }
    },
    mutations: {
        addToCart(state, payload) {
            setTimeout(function() {
                state.cart.push(payload)
            }, 3333);
        },

        removeFromCart(state, payload) {
            state.cart.splice(payload, 1);
        }
    },
    actions: {
        addToCartByActions (context, payload) {
            context.commit('addToCart', payload)
        }
    },
    plugins: [createPersistedState()]
})

export default store;