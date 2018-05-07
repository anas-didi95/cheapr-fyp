<template>
<div class="container">
  <div class="row">
    <div class="col-md-6 offset-md-3" style="margin-top: 10%;">
      <SearchLogo/>
      <form action="" style="margin: 10px">
        <div class="form-group">
          <label for="">Search By:</label><br>
          <input type="radio" name="search_by" value="name" v-model='search_by'> Name
          <input type="radio" name="search_by" value="category" v-model='search_by'> Category
        </div>
      </form>
      <form action="" style="margin: 10px" v-if='search_by==="category"'>
        <div class="form-group">
          <select class="form-control" v-model='search_category' @click='getProductsByCategory()'>
            <option disabled value="">.. Please select one ..</option>
            <option>Snack</option>
            <option>Drink</option>
            <option>Ingredient</option>
            <option>Fresh food</option>
            <option>Household</option>
            <option>Toiletries</option>
          </select>
        </div>
      </form>
      <form action="" id="form-search" style="margin: 10px" v-if='search_by==="name"'>
        <div class="form-group">
          <div class="input-group">
            <input type="text" class="form-control" v-model='search_name'>
            <span class="input-group-btn">
              <button class="btn btn-success" @click='getProductsByName()'>
                <i class="fa fa-search"></i>
                <span> Search</span>
              </button>
            </span>
          </div>
        </div>
      </form>
    </div>
  </div>
  <hr>
  <div class="row">
    <div class="col-md-4 col-xs-6" v-for='product in products' :key='product.id'>
      <ProductBox :product='product'/>
    </div>
    <div class="col-12 text-center" v-if='this.loadingAjax'>
      <img :src='loadingImg' alt="Loading..."/>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import SearchLogo from '@/components/SearchLogo'
import SearchForm from '@/components/SearchForm'
import ProductBox from '@/components/ProductBox'
import loadingImg from '@/assets/ajax-loader.gif'
export default {
  name: 'ProductSearch',
  components: {
    SearchLogo,
    SearchForm,
    ProductBox
  },
  data: function () {
    return {
      bottom: false,
      products: [],
      loadingAjax: false,
      loadingImg: loadingImg,
      next: null,
      search_by: 'name',
      search_category: '',
      search_name: ''
    }
  },
  methods: {
    bottomVisible: function () {
      const scrollY = window.scrollY
      const visible = document.documentElement.clientHeight
      const pageHeight = document.documentElement.scrollHeight
      const bottomOfPage = visible + scrollY >= pageHeight
      return bottomOfPage || pageHeight < visible
    },
    getProducts: function (url) {
      if (url && !this.loadingAjax) {
        this.loadingAjax = true
        axios.get(url)
          .then((response) => {
            console.log(response.statusText)
            let products = response.data.results
            products.forEach(product => {
              this.products.push(product)
            })
            this.next = response.data.next
            this.loadingAjax = false
          })
      }
    },
    getProductsByName: function () {
      let url = `${process.env.API}/product/search?name=${this.search_name}`
      this.products = []
      this.getProducts(url)
    },
    getProductsByCategory: function () {
      let url = `${process.env.API}/product/search?category=${this.search_category}`
      this.products = []
      this.getProducts(url)
    }
  },
  watch: {
    bottom: function (isBottom) {
      if (isBottom) {
        this.getProducts(this.next)
      }
    }
  },
  created () {
    window.addEventListener('scroll', () => {
      this.bottom = this.bottomVisible()
    })
    this.getProducts(`${process.env.API}/product`)
  }
}
</script>

<style>
* {
  -webkit-border-radius: 1px !important;
     -moz-border-radius: 1px !important;
          border-radius: 1px !important;
}
#form-search >.form-group >.input-group > .form-control {
    height: 40px;
}
#form-search >.form-group >.input-group > .input-group-btn > .btn{
        height: 40px;
        font-size: 16px;
        font-weight: 300;
}
#form-search >.form-group >.input-group > .input-group-btn > .btn .glyphicon{
 margin-right:12px;
}
#form-search >.form-group >.input-group > .form-control {
    font-size: 16px;
    font-weight: 300;
}
#form-search >.form-group >.input-group > .form-control:focus {
  border-color: #33A444;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 1px rgba(0, 109, 0, 0.8);
          box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 1px rgba(0, 109, 0, 0.8);
}
</style>
