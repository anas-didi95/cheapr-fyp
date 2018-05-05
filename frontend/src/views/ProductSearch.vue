<template>
<div>
  <search :value='value'/>
  <hr>
  <product-list/>
</div>
</template>

<script>
import Search from '@/containers/Search'
import ProductList from '@/containers/ProductList'
export default {
  name: 'ProductSearch',
  components: {
    Search,
    ProductList
  },
  data: function () {
    return {
      value: 'hello world'
    }
  }
}
</script>

<style>

</style>
