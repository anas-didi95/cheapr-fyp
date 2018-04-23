<template>
<aside id="left-panel" class="left-panel">
  <nav class="navbar navbar-expand-sm navbar-default">
    <NavbarHeader/>
    <MainMenu/>
  </nav>
</aside>
</template>

<script>
import NavbarHeader from '@/components/NavbarHeader';
import MainMenu from '@/components/MainMenu';
export default {
  name: "LeftPanel",
  components: {
    NavbarHeader,
    MainMenu,
  },
};
</script>

<style scoped>

</style>

