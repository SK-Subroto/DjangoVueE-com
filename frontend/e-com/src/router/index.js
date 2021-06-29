import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/pages/Login'
import Admin from '@/components/pages/admin/Admin'
import Category from '@/components/pages/admin/Category'
import Supplier from '@/components/pages/admin/Supplier'
import Product from '@/components/pages/admin/Product'
import Shop from '@/components/pages/shop/Shop'
import ShopProducts from '@/components/pages/shop/ShopProducts'
import ShopProduct from '@/components/pages/shop/ShopProduct'
import CheckOut from '@/components/pages/shop/CheckOut'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      redirect: {path: "login"}
    },

    {
      path: '/login',
      name: 'login',
      component: Login
    },

    {
      path: '/admin',
      name: 'admin',
      component: Admin,
      redirect: {path: "/admin/category"},
      children: [
        {
          path: 'category',
          name: 'admin.category',
          component: Category
        },
        {
          path: 'supplier',
          name: 'admin.supplier',
          component: Supplier
        },
        {
          path: 'product',
          name: 'admin.product',
          component: Product
        }
      ]
    },
    {
      path: '/shop',
      name: 'shop',
      component: Shop,
      redirect: {path: "/shop/products"},
      children: [
        {
          path: 'products',
          name: 'shop.products',
          component: ShopProducts
        },
        {
          path: 'product/:pid',
          name: 'shop.product',
          component: ShopProduct
        },
        {
          path: 'checkout',
          name: 'shop.checkout',
          component: CheckOut
        },
      ]
    }
  ],

  mode: "history"
})
