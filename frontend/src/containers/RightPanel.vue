<template>
<div id="right-panel" class="right-panel">
  <Header></Header>
  <Breadcrumb :text='breadcrumb'></Breadcrumb>
  <div class="content mt-3">
    <ProductList></ProductList>
  </div>
</div>

</template>

<script>
import Header from '@/components/Header'
import Breadcrumb from '@/components/Breadcrumb'
import ProductList  from '@/views/ProductList'
export default {
  name: 'RightPanel',
  components: {
    Header,
    Breadcrumb,
    ProductList
  },
  data: function () {
    return {
      breadcrumb: 'Product List'
    }
  }
}
</script>

<style>

</style>
