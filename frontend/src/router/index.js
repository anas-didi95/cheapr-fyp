import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

// const ProductList = () => import('@/views/ProductList')
// const ProductDetails = () => import('@/views/ProductDetails')
const ProductSearch = () => import('@/containers/ProductSearch')
const ProductDetails = () => import('@/containers/ProductDetails')

export default new Router({
  routes: [
    {
      path: '/',
      name: 'product-search',
      component: ProductSearch
    },
    {
      path: '/product/:id',
      name: 'product-details',
      component: ProductDetails
    }
    // {
      // path: '/product',
      // name: 'product-list',
      // component: ProductList,
      // meta: {
        // breadcrumb: {
          // title: 'Application',
          // id: 'product-list',
          // name: 'Product List'
        // }
      // }
    // },
    // {
      // path: '/product/:id',
      // name: 'product-details',
      // component: ProductDetails,
      // meta: {
        // breadcrumb: {
          // title: 'Application',
          // id: 'product-details',
          // name: 'Product Details',
          // hasPrevious: true,
          // previous: {name: 'product-list'}
        // }
      // }
    // }
  ]
})
