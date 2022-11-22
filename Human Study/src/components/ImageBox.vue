<template>
  <div class='square'>
    <img :src="this.imgurl" />
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
  width: 102px;
  height: 102px;
  border: 2px solid #000;
}
</style>

<script>
export default {
  props: {
    imgurl: String,
    fidScore: Number,
  },

  created() {
    console.log(this.imgurl);
  },

}
</script>