<!-- This component acts as a wrapper for images. It displays images with a border box around them.
  The border box's color can change to indicate an image is selected (useful for certain tasks)
  The component also contains metadata about the image, like it's FID score, its url (provided by flask server), and its sequence number (if its part of an ImageGrid). 
-->
<template>
  <div class='square' v-bind:class="[selected ? 'selected' : '']">
    <img :src="this.imgurl"/> 
  </div>
  <br>
</template>

<style scoped>
img {
  width: 100px;
  height: 100px;
}

.square {
  max-width: 104px;
  max-height: 104px;
  padding: 0px;
  margin: 0px;
  border: 2px solid #000;
}

.square.selected {
  border: 2px solid #0A0;
}
</style>

<script>
export default {
  props: {
    imgurl: String,
    fidScore: Number,
    seqNum: Number, // Useful to know which image was selected in ImageGridSingle (kind of like a local ID number)
    selected: Boolean,
  },
  data(){
    return {
      isSelected : this.selected,
    }
  },
}
</script>