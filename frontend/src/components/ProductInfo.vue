<template>
<article class="card-body p-5">
  <h3 class="title mb-3">{{ item.name }}</h3>
  <p class="price-detail-wrap">
    <div class="price h3 text-warning" v-for='price in this.prices' :key='price.id' v-if='item'>
      <span class="currency">{{ price.supermarket }} | RM </span>
      <span class="num">{{ price.price_value }}</span>
      <span>/per {{ price.description }}</span>
    </div>
  </p>
  <dl class="item-property">
    <dt>Description</dt>
    <dd>
      <p>{{ item.name }} {{ item.prices[0].description }}</p>
    </dd>
  </dl>
  <dl class="param param-feature">
    <dt>Latest update</dt>
    <dd>{{ this.date_updated }}</dd>
  </dl>
</article>
</template>

<script>
export default {
  name: 'ProductInfo',
  props: ['item'],
  computed: {
    date_updated: function () {
      let datetime = this.item.prices[0].date_updated
      return new Date(datetime).toDateString()
    },
    prices: function () {
      let prices = []
      for (let i = 0; i < 3; i++) {
        prices.push(this.item.prices[i])
      }
      console.log(prices)
      return prices
    }
  }
}
</script>

<style>

</style>
