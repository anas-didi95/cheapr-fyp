<template>
 <div>
   <div class="row">
     <div class="col-sm-4 offset-sm-4" v-if='loadingAjax'>
       <img :src="loadingImg" alt="Loading...">
     </div>
     <div class="col-sm-4 offset-sm-4" v-else>
       <ItemCard :item='item'></ItemCard>
     </div>
   </div>
   <div class="row">
     <div class="col-sm-8">
       <div class="card">
         <div class="card-header">
           Price Comparison
         </div>
         <div class="card-body">
          <price-chart v-if='item' :chartData='chartdata'></price-chart>
         </div>
       </div>
     </div>
   </div>
 </div> 
</template>

<script>
import axios from 'axios'
import loadingImg from '@/assets/ajax-loader.gif'
import ItemCard from '@/components/ItemCard'
import PriceChart from '@/components/PriceChart'
export default {
  name: 'ProductDetails',
  components: {
    ItemCard,
    PriceChart
  },
  data: function () {
    return {
      title: '',
      item: null,
      loadingAjax: false,
      loadingImg: loadingImg,
      chartdata: {
        labels: [],
        datasets: [
          {
            data: [],
            label: 'EconSave',
            borderColor: 'rgba(0,103,255,0.5)',
            borderWidth: 3.5,
            pointStyle: 'circle',
            pointRadius: 5,
            pointBorderColor: 'transparent',
            pointBackgroundColor: 'rgba(0,0,255,0.5)',
          },
          {
            data: [],
            label: 'Tesco',
            borderColor: 'rgba(0,255,0,0.5)',
            borderWidth: 3.5,
            pointStyle: 'circle',
            pointRadius: 5,
            pointBorderColor: 'transparent',
            pointBackgroundColor: 'rgba(0,255,0,0.5)',
          },
          {
            data: [],
            label: 'Giant',
            pointBackgroundColor: 'rgba(255,0,0,0.5)',
            backgroundColor: 'rgba(255,0,0,0.5)'
          }
        ]
      }
    }
  },
  methods: {
    getProduct: function() {
      let api = process.env.API;
      this.loadingAjax = true
      axios.get(`${api}/product/${this.$route.params.id}`)
        .then((response) => {
          console.log(response)
          this.prepareChart(response.data.prices)
          this.item = response.data
          this.loadingAjax = false
        })  
    },
    prepareChart: function(prices) {
      console.log(prices)
      for (let i = 0; i < prices.length && i < 15; i++) {
        let day = prices[i].day_start
        let month = prices[i].month_start
        let year = prices[i].year_start
        let dataset_id = prices[i].supermarket
        let dataset_price = parseFloat(prices[i].price_value)
        let date = `${day}/${month}/${year}`
        if (!this.chartdata.labels.includes(date))
          this.chartdata.labels.push(`${day}/${month}/${year}`)
        this.chartdata.datasets[dataset_id-1].data.push(dataset_price)
      }
    }
  },
  created () {
    this.getProduct()
  }
}
</script>

<style>

</style>
