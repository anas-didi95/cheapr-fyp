<script>
import { Line, mixins } from 'vue-chartjs'
export default {
  extends: Line,
  name: 'PriceChart',
  mixins: [mixins.reactiveProp],
  props: ['chartData', 'options'],
  mounted () {
    this.renderChart(this.chartData)
  }
}
</script>
