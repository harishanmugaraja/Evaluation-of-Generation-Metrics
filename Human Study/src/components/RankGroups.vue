<template>
    <div class="rank-container">
        <draggable :list="imagebars" item-key="name">
            <template #item = "{ element }">
                <div>
                    <ImageBar :imgarr="element.images"></ImageBar>
                </div>
            </template>
        </draggable>
    </div>
</template>

<style scoped>
.rank-container {
    position: relative;
    width: 100%;
}
</style>

<script>
import ImageBar from './ImageBar.vue';
import draggable from 'vuedraggable';

export default {
    name: 'rank-groups',

    components: {
        'ImageBar': ImageBar,
        'draggable': draggable
    },

    data() {
        return {
            imagebars: [
                {id: 0, fid: 1, images: ['../assets/images/group1/p1.png','../assets/images/group1/p2.png','../assets/images/group1/p3.png','../assets/images/group1/p4.png']},
                {id: 1, fid: 2, images: ['../assets/images/group2/p1.png','../assets/images/group2/p2.png','../assets/images/group2/p3.png','../assets/images/group2/p4.png']},
                {id: 2, fid: 3, images: ['../assets/images/group3/p1.png','../assets/images/group3/p2.png','../assets/images/group3/p3.png','../assets/images/group3/p4.png']}
            ],
        };
    },

}

</script>
