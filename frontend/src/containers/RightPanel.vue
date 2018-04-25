<template>
<div id="right-panel" class="right-panel">
  <Header></Header>
  <Breadcrumb :text='breadcrumb'></Breadcrumb>
  <div class="content mt-3">
    <ProductDetails></ProductDetails>
  </div>
</div>

</template>

<script>
import Header from '@/components/Header'
import Breadcrumb from '@/components/Breadcrumb'
import ProductList  from '@/views/ProductList'
import ProductDetails from '@/views/ProductDetails'
export default {
  name: 'RightPanel',
  components: {
    Header,
    Breadcrumb,
    ProductList,
    ProductDetails
  },
  data: function () {
    return {
      breadcrumb: 'Product Details'
    }
  }
}
</script>

<style>

</style>
