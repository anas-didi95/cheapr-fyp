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
  <div class="card" v-if='this.product'>
    <div class="row">
      <aside class="col-sm-5 border-right">
        <ProductImage :product='product'/>
      </aside>
      <aside class="col-sm-7">
        <ProductInfo :product='product' :supermarkets='supermarkets' :prices='prices' :loadingAjax='loadingAjax'/>
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
import axios from "axios";
import ProductImage from "@/components/ProductImage";
import ProductInfo from "@/components/ProductInfo";
import loadingImg from "@/assets/ajax-loader.gif";
export default {
  name: "ProductDetails",
  components: {
    ProductImage,
    ProductInfo
  },
  data: function() {
    return {
      loadingAjax: false,
      loadingImg: loadingImg,
      product: null,
      supermarkets: null,
      prices: []
    };
  },
  methods: {
    getProduct: function() {
      if (!this.loadingAjax) {
        this.loadingAjax = true;
        axios.get(`${process.env.API}/product/${this.$route.params.id}`).then(response => {
          console.log(response.statusText);
          this.product = response.data;
          this.getSupermarkets();
        })
      }
    },
    getSupermarkets: function() {
      axios.get(`${process.env.API}/supermarket`).then(response => {
        console.log(`getsupermarket=${response.statusText}`);
        this.supermarkets = response.data.results;
        this.getPrices()
      })
    },
    getPrices: function() {
      axios.get(`${process.env.API}/price/filter?product=${this.product.id}`).then(response => {
        console.log(`getprices=${response.statusText}`)
        let datas = response.data.results
        this.supermarkets.forEach(supermarket => {
          let price = datas.filter(data => {
            return supermarket.id == data.supermarket
          })
          let obj = {}
          obj['name'] = supermarket.name
          obj['value'] = price[0]
          this.prices.push(obj)
        })
        this.loadingAjax = false
      })
    }
  },
  async created() {
    await this.getProduct()
  }
}
</script>

<style>

</style>
