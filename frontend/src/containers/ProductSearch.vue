<template>
<div class="container">
  <div class="row">
    <div class="col-md-6 offset-md-3" style="margin-top: 10%;">
      <SearchLogo/>
      <SearchForm :value='search_value' @update='onSearchFormUpdate()'/>
    </div>
  </div>
</div>
</template>

<script>
import SearchLogo from '@/components/SearchLogo'
import SearchForm from '@/components/SearchForm'
export default {
  name: 'Search',
  components: {
    SearchLogo,
    SearchForm
  },
  props: ['value'],
  data: function () {
    return {
      search_value: this.props.search_value
    }
  },
  methods: {
    onSearchFormUpdate: function (search_value) {
      this.search_value = search_value
    }
  }
}
</script>

<style>
* {
  -webkit-border-radius: 1px !important;
     -moz-border-radius: 1px !important;
          border-radius: 1px !important;
}
</style>
