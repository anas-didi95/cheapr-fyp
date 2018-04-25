<template>
<div>
  <div class="row">
    <div class="col-sm-6 offset-sm-3 col-12">
      <div class="card">
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
      <div class="card">
        <div class="card-body">
          {{ item.name }}
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'ProductList',
  data: function () {
    return {
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
  }
}
</script>

<style>

</style>
