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
    <div class="col-sm-4 col-6" v-for="item in items" :key='item.id'>
      <router-link :to="{name: 'product-details', params: {id: item.id} }">
        <ItemCard :item='item'></ItemCard>
      </router-link>
    </div>
  </div>
  <div class="col-12 text-center" v-if="this.loadingAjax">
    <img :src="loadingImg" alt="Loading...">
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
      next: `${process.env.API}/product/`,
      loadingAjax: false,
      loadingImg: loadingImg,
      bottom: false
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
    getProducts: function () {
      if (this.next && !this.loadingAjax) {
        this.loadingAjax = true
        axios.get(`${this.next}`)
          .then((response) => {
            console.log(response.statusText)
            let items = response.data.results
            items.forEach(item => {
              this.items.push(item)
            })
            this.next = response.data.next
            this.loadingAjax = false
          })
      }
    }
  },
  watch: {
    bottom: function (isBottom) {
      if (isBottom) {
        this.getProducts()
      }
    }
  },
  created () {
    window.addEventListener('scroll', () => {
      this.bottom = this.bottomVisible()
    })
    this.getProducts()
  },
  mounted () {
    this.title = this.$route.meta.breadcrumb.name
  }
}
</script>

<style>

</style>
