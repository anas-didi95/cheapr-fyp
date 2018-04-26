<template>
<div class="card">
  <div class="card-header">
    <strong class="card-title mb-3">Price Comparison</strong>
  </div>
  <div class="card-body">
    <canvas id="chartId"></canvas>
  </div>
</div>
</template>

<script>
export default {
  name: 'PriceChart',
  props: ['data', 'options'],
  mounted () {
    let ctx = document.getElementById('chartId')
    let chartPrice = new Chart(ctx, {
      type: 'line',
      data: {
        labels: this.data.labels,
        datasets: this.data.datasets
      }
    })
  }
}
</script>

<style>
</style>
