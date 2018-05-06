<template>
<article class="card-body p-5">
  <h3 class="title mb-3">{{ product.name }}</h3>
  <p class="price-detail-wrap">
    <table class="table">
      <tr v-for='price in this.display_prices' :key='price.id'>
        <td>{{ price.name }}</td>
        <td>RM {{ price.value.price_value }}</td>
      </tr>
    </table>
  </p>
  <dl class="item-property">
    <dt>Description</dt>
    <dd>
      <p>{{ product.name }} {{ this.description }}</p>
    </dd>
  </dl>
  <dl class="param param-feature">
    <dt>Latest update</dt>
    <dd>{{ this.latest_update }}</dd>
  </dl>
</article>
</template>

<script>
export default {
  name: "ProductInfo",
  props: ["product", "supermarkets", "prices", "loadingAjax"],
  data: function() {
    return {
      description: "",
      latest_update: "",
      display_prices: null
    }
  },
  watch: {
    loadingAjax: function(ajax) {
      if (!ajax) {
        this.getLatestDate();
        this.getDisplayPrices();
      }
    }
  },
  methods: {
    getLatestDate: function() {
      let v = this.prices[0]
      this.description = v.value.description
      this.latest_update = `${v.value.year_start}/${v.value.month_start}/${v.value.day_start}`
    },
    getDisplayPrices: function () {
      this.display_prices = this.prices
      this.display_prices.sort((a,b) => {
        return parseFloat(a.value.price_value) - parseFloat(b.value.price_value)
      })
    }
  }
}
</script>

<style>

</style>
