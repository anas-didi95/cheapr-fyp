<template>
<div id="container">
  <LeftPanel></LeftPanel>
  <RightPanel></RightPanel>
</div>
</template>

<script>
import LeftPanel from '@/containers/LeftPanel';
import RightPanel from '@/containers/RightPanel';
export default {
  name: 'App',
  components: {
    LeftPanel,
    RightPanel,
  }
}
</script>

<style>
#container {
  display: table;
  width: 100%;
} 
</style>
