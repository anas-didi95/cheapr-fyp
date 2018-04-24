<template>
<div id="right-panel" class="right-panel">
  <Header></Header>
  <Breadcrumb></Breadcrumb>
  <div class="content mt-3"></div>
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
  }
}
</script>

<style>

</style>
