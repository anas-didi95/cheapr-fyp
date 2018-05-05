<template>
<div class="container">
  <div class="row">
    <div style="margin: 10px; margin-bottom: 10px;">
      <router-link :to='{name: "product-search"}' class="btn btn-primary">
        <i class="fa fa-arrow-left"></i>
        <span> Return</span>
      </router-link>
    </div>
  </div>
  <hr>
  <div class="card" v-if='this.item'>
    <div class="row">
      <aside class="col-sm-5 border-right">
        <ProductImage/>
      </aside>
      <aside class="col-sm-7">
        <ProductInfo :item='item'/>
      </aside>
    </div>
  </div>
  <div class="row" v-else>
    <div class="col-12 text-center" v-if='this.loadingAjax'>
      <img :src='loadingImg' alt="Loading...">
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import ProductImage from '@/components/ProductImage'
import ProductInfo from '@/components/ProductInfo'
import loadingImg from '@/assets/ajax-loader.gif'
export default {
 name: 'ProductDetails',
 components: {
   ProductImage,
   ProductInfo
 },
 data: function () {
   return {
     item: null,
     loadingAjax: false,
     loadingImg: loadingImg,
     url: `${process.env.API}/product/${this.$route.params.id}`
   }
 },
 methods: {
   getProduct: function () {
     if (!this.loadingAjax) {
       this.loadingAjax = true
       axios.get(this.url)
        .then((response) => {
          console.log(response.statusText)
          this.item = response.data
          this.loadingAjax = false
        })
     }
   }
 },
 created () {
   this.getProduct()
 }
}
</script>

<style>

</style>
