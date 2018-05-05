<template>
<div>
  <form action="" id="form-search" style="margin: 10px">
    <div class="form-group">
      <div class="input-group">
        <input type="text" class="form-control" v-model='search_value'>
        <span class="input-group-btn">
          <button class="btn btn-success" @click='clickSearch()'>
            <i class="fa fa-search"></i>
            <span> Search</span>
          </button>
        </span>
      </div>
    </div>
  </form>
</div>
</template>

<script>
export default {
  name: 'SearchForm',
  props: ['value'],
  data: function () {
    return {
      search_value: ''
    }
  },
  methods: {
    clickSearch: function () {
      console.log(this.search_value);
      this.$emit('onUpdateSearchValue', this.search_value)
    }
  }
}
</script>

<style>
#form-search >.form-group >.input-group > .form-control {
    height: 40px;
}
#form-search >.form-group >.input-group > .input-group-btn > .btn{
        height: 40px;
        font-size: 16px;
        font-weight: 300;
}
#form-search >.form-group >.input-group > .input-group-btn > .btn .glyphicon{
 margin-right:12px;
}
#form-search >.form-group >.input-group > .form-control {
    font-size: 16px;
    font-weight: 300;
}
#form-search >.form-group >.input-group > .form-control:focus {
  border-color: #33A444;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 1px rgba(0, 109, 0, 0.8);
          box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 1px rgba(0, 109, 0, 0.8);
}
</style>
