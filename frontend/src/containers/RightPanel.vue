<template>
<div id="right-panel" class="right-panel">
  <Header :title='title'></Header>
  <Breadcrumb></Breadcrumb>
  <div class="content mt-3">
    <router-view></router-view>
  </div>
</div>

</template>

<script>
import Header from '@/components/Header'
import Breadcrumb from '@/components/Breadcrumb'
export default {
  name: 'RightPanel',
  components: {
    Header,
    Breadcrumb
  },
  data: function () {
    return {
      title: ''
    }
  },
  watch: {
    '$route' () {
      this.title = this.$route.meta.breadcrumb.title
    }
  },
  mounted () {
    this.title = this.$route.meta.breadcrumb.title
  }
}
</script>

<style>

</style>
