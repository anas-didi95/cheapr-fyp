<template>
<div id="main-menu" class="main-menu collapse navbar-collapse">
      <ul class="nav navbar-nav">
        <h3 class="menu-title">Introduction</h3>
        <li></li>
        <h3 class="menu-title">Application</h3>
        <li>
          <router-link :to="{name: 'product-list'}">
            <i class="menu-icon fa fa-search"></i> Search
          </router-link>
        </li>
      </ul>
    </div>
</template>

<script>
export default {
  name: 'MainMenu'
}
</script>

<style scoped>

</style>
