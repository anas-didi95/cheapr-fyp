<template>
<div class="navbar-header">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#main-menu" aria-controls="main-menu" aria-expanded="false"
    aria-label="Toggle navigation">
    <i class="fa fa-bars"></i>
  </button>
  <a class="navbar-brand" href="./">
    <img :src="imageBrand" alt="Logo">
  </a>
  <a class="navbar-brand hidden" href="./">
    <img :src="imageBrandHidden" alt="Logo">
  </a>
</div>
</template>

<script>
import ImageBrand from '@/assets/images/logo.png'
import ImageBrandHidden from '@/assets/images/logo2.png'
export default {
  name: 'NavbarHeader',
  data: function () {
    return {
      imageBrand: ImageBrand,
      imageBrandHidden: ImageBrandHidden
    }
  }
}
</script>

<style scoped>
</style>
