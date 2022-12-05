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
  /* padding: 1px; */
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
    seqNum: Number,
    selected: Boolean,
  },
  data(){
    return {
      isSelected : this.selected,
    }
  },
  created() {
    // console.log(this.imgurl);
  },

}
</script>