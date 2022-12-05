<template>
    <div class="rank-container">
        <h1>{{prompt}}</h1>
        <draggable :list="imagebars" item-key="name" :group="this.id">
            <template #item = "{ element }">
                <div>
                    <ImageBar :imgarr="element.imagelist"></ImageBar>
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
import axios from 'axios';
import uniqueId from 'lodash.uniqueid';

const BASE_URL = 'http://127.0.0.1:5000/'


export default {
    name: 'rank-groups',

    components: {
        'ImageBar': ImageBar,
        'draggable': draggable
    },

    props: {
        prompt: String,
    },

    created(){
        this.id = uniqueId();
        axios
        .get(BASE_URL+'rankGroups')
        .then((response) => {
          this.imagebars = response.data.imagearrs; 
        //   console.log(response.data.imagearrs);
        });
    },

    data() {
        return {
            id: null,
            imagebars: [],
            // imagebars: [
            //     {id: 0, fid: 1, imagelist: ['../assets/images/group1/p1.png','../assets/images/group1/p2.png','../assets/images/group1/p3.png','../assets/images/group1/p4.png']},
            //     {id: 1, fid: 2, imagelist: ['../assets/images/group2/p1.png','../assets/images/group2/p2.png','../assets/images/group2/p3.png','../assets/images/group2/p4.png']},
            //     {id: 2, fid: 3, imagelist: ['../assets/images/group3/p1.png','../assets/images/group3/p2.png','../assets/images/group3/p3.png','../assets/images/group3/p4.png']}
            // ],
        };
    },

}

</script>
