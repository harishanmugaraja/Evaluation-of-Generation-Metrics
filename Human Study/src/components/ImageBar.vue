<template>
    <div class = 'rectangle'>
        <img v-for="image in this.imgarr" :src="image" />
    </div>
</template>

<style scoped>
img {
    width: 100px;
    height: 100px;
    padding: 1px;
}
.rectangle {
width:520px;
height:105px;
border:1px solid #000;
}
</style>

<script>
export default {
    props: {
    imgarr: Array,
  },

  created() {
    console.log(this.imgarr);
  },

}
</script>

