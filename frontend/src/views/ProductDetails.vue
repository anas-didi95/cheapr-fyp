<template>
 <div>
   <div class="row">
     <div class="col-sm-4 offset-sm-4">
       <ItemCard :item='item'></ItemCard>
     </div>
   </div>
   <div class="row">
     <div class="col-sm-8">
       <price-chart :data='chartdata'></price-chart>
     </div>
   </div>
 </div> 
</template>

<script>
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
      item: {
        "id": 1,
        "name": "100 Plus Isotonic Drink",
        "category": "Drink",
        "category_name": "Drink",
        "date_created": "2018-04-25T21:05:22.482223Z",
        "date_updated": "2018-04-25T21:05:22.482259Z"
      },
      chartdata: {
        labels: ['', '', '', ''],
        datasets: [
          {
            data: [10, 20, 30],
            label: 'EconSave',
            borderColor: 'rgba(0,103,255,0.5)',
            borderWidth: 3.5,
            pointStyle: 'circle',
            pointRadius: 5,
            pointBorderColor: 'transparent',
            pointBackgroundColor: 'rgba(0,0,255,0.5)',
          },
          {
            data: [30, 20, 10],
            label: 'Giant',
            borderColor: 'rgba(0,255,0,0.5)',
            borderWidth: 3.5,
            pointStyle: 'circle',
            pointRadius: 5,
            pointBorderColor: 'transparent',
            pointBackgroundColor: 'rgba(0,255,0,0.5)',
          },
          {
            data: [20, 10, 30],
            label: 'Tesco',
            pointBackgroundColor: 'rgba(255,0,0,0.5)',
            backgroundColor: 'rgba(255,0,0,0.5)'
          }
        ]
      }
    }
  },
  mounted () {
    this.generateChart()
  },
  methods: {
    generateChart: function () {
      var ctx = document.getElementById('price-chart')
      console.log()
      var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [ "2010", "2011", "2012", "2013", "2014", "2015", "2016" ],
            type: 'line',
            defaultFontFamily: 'Montserrat',
            datasets: [ {
                data: [ 0, 7, 3, 5, 2, 10, 7 ],
                label: "Expense",
                backgroundColor: 'rgba(0,103,255,.15)',
                borderColor: 'rgba(0,103,255,0.5)',
                borderWidth: 3.5,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(0,103,255,0.5)',
                }, 
             ]
        },
      })
    }
  }
}
</script>

<style>

</style>
