<template>
    <!-- <draggable v-model="imagebars">
        <ImageBar v-for="imagebar in imagebars" :key="imagebar.id" :imgarr="imagebar"></ImageBar>
        <div :id="element.id" v-for="element in imagebars" :key="element.id">
          <strong>{{element.name}}</strong>
          <span>{{element.images[0]}}</span>
        </div>
    </draggable> -->
 <ImageBar v-for="images in imagebars" :imgarr="images.images"></ImageBar>
 <!-- <ImageBar :imgarr="['../assets/images/group2/p1.png','../assets/images/group2/p2.png','../assets/images/group2/p3.png','../assets/images/group2/p4.png']"></ImageBar> -->
</template>

<style scoped>
</style>

<script>
import ImageBar from './ImageBar.vue';
import draggable from 'vuedraggable';

export default {
    name: 'sort-groups',

    components: {
        'ImageBar': ImageBar,
        'draggable': draggable
    },

    data() {
        return {
            imagebars: [
                {id: 0, images: ['../assets/images/group1/p1.png','../assets/images/group1/p2.png','../assets/images/group1/p3.png','../assets/images/group1/p4.png']},
                {id: 1, images: ['../assets/images/group2/p1.png','../assets/images/group2/p2.png','../assets/images/group2/p3.png','../assets/images/group2/p4.png']}
            ],
        };
    },

}

</script>
