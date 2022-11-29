<script setup>
import RankGroups from './components/RankGroups.vue'
import BinGroups from './components/BinGroups.vue'
import ImageGridSingle from './components/ImageGridSingle.vue';
import ImageGridWhole from './components/ImageGridWhole.vue';
</script>

<template>
  <div class="app">
    <!-- <RankGroups></RankGroups> -->
    <!-- <BinGroups></BinGroups> -->
    <!-- <ImageGridWhole :size="4"></ImageGridWhole> -->
    <ImageGridSingle :size="4"></ImageGridSingle>
  </div>
</template>

<style scoped>
.app {
  position: relative;
  width: 80vw;
  height: auto;
  margin: 0px;
}
</style>
