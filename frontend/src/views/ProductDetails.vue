<template>
 <div>
   <div class="row">
     <div class="col-sm-4 offset-sm-4">
       <ItemCard :item='item'></ItemCard>
     </div>
   </div>
 </div> 
</template>

<script>
import ItemCard from '@/components/ItemCard'
export default {
  name: 'ProductDetails',
  components: {
    ItemCard
  },
  data: function () {
    return {
      item: {
        "id": 1,
        "name": "100 Plus Isotonic Drink",
        "category": "Drink",
        "category_name": "Drink",
        "date_created": "2018-04-25T21:05:22.482223Z",
        "date_updated": "2018-04-25T21:05:22.482259Z"
      }
    }
  }
}
</script>

<style>

</style>
