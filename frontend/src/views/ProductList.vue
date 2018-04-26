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
    <div class="col-sm-4 col-6" v-for="item in searchItem" :key='item.id'>
      <router-link :to="{name: 'product-details', params: {id: item.id} }">
        <ItemCard :item='item'></ItemCard>
      </router-link>
    </div>
  </div>
</div>
</template>

<script>
import ItemCard from '@/components/ItemCard'
export default {
  name: 'ProductList',
  components: {
    ItemCard
  },
  data: function () {
    return {
      title: '',
      items: [
        {
          "id": 1,
          "name": "100 Plus Isotonic Drink",
          "category": "Drink",
          "category_name": "Drink",
          "date_created": "2018-04-25T21:05:22.482223Z",
          "date_updated": "2018-04-25T21:05:22.482259Z"
        },
        {
          "id": 2,
          "name": "A&W Cream Soda",
          "category": "Drink",
          "category_name": "Drink",
          "date_created": "2018-04-25T21:05:22.500922Z",
          "date_updated": "2018-04-25T21:05:22.500959Z"
        },
        {
          "id": 3,
          "name": "A1 Sardine In Tomato Sauce",
          "category": "Ingredient",
          "category_name": "Ingredient",
          "date_created": "2018-04-25T21:05:22.521063Z",
          "date_updated": "2018-04-25T21:05:22.521089Z"
        }
      ],
      displayItems: [],
      search: ''
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
  mounted () {
    this.title = this.$route.meta.breadcrumb.name
  }
}
</script>

<style>

</style>
