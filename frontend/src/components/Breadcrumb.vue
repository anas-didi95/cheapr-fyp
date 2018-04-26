<template>
<div class="breadcrumbs">
  <div class="col-sm-4">
    <div class="page-header float-left">
      <div class="page-title">
        <h1>
          <router-link v-if="this.$route.meta.breadcrumb.hasPrevious" :to="{name: this.$route.meta.breadcrumb.previous.name}">
            <i class="fa fa-arrow-left"></i> Go back
          </router-link>
        </h1>
      </div>
    </div>
  </div>
  <div class="col-sm-4">
    <div class="page-header float-right">
      <div class="page-title">
        <h1>
          <router-link v-if="this.$route.meta.breadcrumb.hasNext" :to="{name: this.$route.meta.breadcrumb.previous.name}">
            <i class="fa fa-arrow-right"></i> Next
          </router-link>
        </h1>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'Breadcrumb',
  props: ['text'],
  data: function () {
    return {
      breadcrumb: this.text
    }
  }
}
</script>

<style>

</style>
