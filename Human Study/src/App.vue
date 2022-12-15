<script setup>
import RankGroups from './components/RankGroups.vue'
import BinGroups from './components/BinGroups.vue'
import ImageGridSingle from './components/ImageGridSingle.vue';
import ImageGridWhole from './components/ImageGridWhole.vue';
</script>

<!-- This is the file where the components get mounted to as a final HTML file -->

<template>
  <div class="app">
    <RankGroups :prompt = "'Rank these groups of images from highest image quality to the lowest'"></RankGroups>
    <BinGroups :prompt = "'These images belong to one of two different groups, seperate them into their respective groups'"></BinGroups>
    <ImageGridWhole :prompt = "'Select the group of images below that has the highest image quality'"></ImageGridWhole>
    <ImageGridSingle :prompt = "'Select the image from the group of images below that does not belong'"></ImageGridSingle>
    <BinGroups :prompt = "'These images belong to one of two different groups, seperate them into their respective groups'"></BinGroups>
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
