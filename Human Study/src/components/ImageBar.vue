<!-- Very similar to ImageBox, except that this is a rectangle that houses groups of images in a row -->
<template>
    <h1>{{prompt}}</h1>
    <div class = 'rectangle'>
        <img v-for="image in this.imgarr" :src="image" />
    </div>
    <br>
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
    prompt: String,
  },
}
</script>

