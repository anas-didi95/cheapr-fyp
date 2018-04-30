<template>
<div>
  <div class="row">
    <div class="col-sm-6 offset-sm-3 col-12">
      <div class="card">
        <div class="card-header">
          <strong class="card-title mb-3 text-center">{{ title }}</strong>
        </div>
        <div class="card-body">
          <div class="input-group">
            <div class="input-group-addon">
              <i class="fa fa-search"></i>
            </div>
            <input type="text" class="form-control" placeholder="Search product here" v-model='search'>
          </div>
          <small class="form-text text-muted">ex. milo, bio zip</small>
        </div>
      </div>
    </div>
  </div>
  <div class="row">
    <div class="col-12 text-center" v-if="this.loadingAjax">
      <img :src="loadingImg" alt="Loading...">
    </div>
    <div class="col-sm-4 col-6" v-else v-for="item in searchItem" :key='item.id'>
      <router-link :to="{name: 'product-details', params: {id: item.id} }">
        <ItemCard :item='item'></ItemCard>
      </router-link>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import loadingImg from '@/assets/ajax-loader.gif'
import ItemCard from '@/components/ItemCard'
export default {
  name: 'ProductList',
  components: {
    ItemCard
  },
  data: function () {
    return {
      title: '',
      items: [],
      search: '',
      loadingAjax: false,
      loadingImg: loadingImg
    }
  },
  methods: {
    getProducts: function () {
      let api = process.env.API;
      this.loadingAjax = true
      axios.get(`${api}/product/`)
        .then((response) => {
          console.log(response.statusText)
          this.items = response.data
          this.loadingAjax = false
        })
    }
  },
  computed: {
    searchItem: function () {
      const search = this.search.toLowerCase();
      return this.items.filter(item => {
        return item.name.toLowerCase().indexOf(search) !== -1
      })
    }
  },
  created () {
    this.getProducts()
  },
  mounted () {
    this.title = this.$route.meta.breadcrumb.name
  }
}
</script>

<style>

</style>
