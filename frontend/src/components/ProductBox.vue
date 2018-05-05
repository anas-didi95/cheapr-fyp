<template>
<div class="productbox">
  <img src="http://placehold.it/460x250/e67e22/ffffff&text=HTML5" class="img-fluid">
  <div class="producttitle">{{ item.name }}</div>
  <div class="productprice">
    <div class="pull-right">
      <router-link :to='{name: "product-details", params: {id: item.id} }' class="btn btn-danger">
        <span>View</span>
      </router-link>
    </div>
    <div class="pricetext">{{ item.category }}</div>
  </div>
</div>
</template>

<script>
export default {
  name: 'ProductBox',
  props: ['item']
}
</script>

<style>
.productbox {
  background-color:#ffffff;
	padding: 20px;
	margin-bottom:10px;
  /* margin: 5px; */
	-webkit-box-shadow: 0 8px 6px -6px  #999;
	   -moz-box-shadow: 0 8px 6px -6px  #999;
	        box-shadow: 0 8px 6px -6px #999;
}
.producttitle {
    font-weight:bold;
	padding:5px 0 5px 0;
}
.productprice {
	border-top:1px solid #dadada;
	padding-top:5px;
}
.pricetext {
	font-weight:bold;
	font-size:0.8em;
}
</style>
