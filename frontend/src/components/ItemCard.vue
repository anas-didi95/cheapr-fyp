<template>
<div class="card">
  <!-- <div class="card-header"> -->
    <!-- <strong class="card-title mb-3">Profile Card</strong> -->
  <!-- </div> -->
  <div class="card-body">
    <div class="mx-auto d-block">
      <img class="rounded-circle mx-auto d-block" src="" alt="Card image cap">
      <h5 class="text-sm-center mt-2 mb-1">{{ item.name }}</h5>
      <div class="location text-sm-center">
        <i class="fa fa-shopping-cart"></i> {{ item.category }}</div>
    </div>
    <hr>
    <div class="card-text text-sm-center">
      <a href="#">
        <small>Giant</small>
      </a>
      <a href="#">
        <small>Tesco</small>
      </a>
      <a href="#">
        <small>EconSave</small>
      </a>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'ItemCard',
  props: ['item'],
  data: function () {
    return {
    }
  }
}
</script>

<style>

</style>
