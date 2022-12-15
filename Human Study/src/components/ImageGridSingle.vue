<!-- This component is meant to be an odd-one-out task. The user is picking an image that does not look like the others-->
<template>
    <h1>{{prompt}}</h1>
    <SquareGrid>    
        <div v-for="(element, index) in imagearr" :key="index" @click="select(index)">
            <ImageBox :imgurl="element.url" :fidScore = "element.fid" :seqNum="index" :selected="element.selected"></ImageBox>
        </div>
    </SquareGrid>
</template>

<style scoped lang="scss">

SquareGrid { // This Square Grid component is actually made with SASS and not HTML.
             // The SASS code is very succcinct and performant
    // The content width you use on your website
    --content-width: 320px;

    // The size of the gutter  
    --gutter: 10px;

    // The amount of columns
    --columns: 3;


    // This is the calculation for the row height.   
    --row-size: calc((var(--content-width) - (var(--gutter) * (var(--columns) - 1))) / var(--columns));

    display: grid;

    width: 100%;
    max-width: var(--content-width);

    grid-template-columns: repeat(var(--columns), 1fr);
    grid-auto-rows: var(--row-size);

    grid-column-gap: var(--gutter);
    grid-row-gap: var(--gutter); // gap between columns

}

// This code overwrites the code in created(), but here are some things you can do with media queries if you put them in SquareGrid

// @media (min-width: 450px) {
//     SquareGrid {
//         --columns: 2;
//     }
// }

// @media (min-width: 750px) {
//     SquareGrid {
//         --columns: 3;
//     }
// }

// @media (min-width: 1200px) {
//     SquareGrid {
//         --columns: 4;
//     }
// }
</style>

<script>
import ImageBox from './ImageBox.vue';
import uniqueId from 'lodash.uniqueid';
import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:5000/'

export default {
    props: {
        size: Number, //This is the length of one side of the grid (i.e grid can have at max size*size ImageBoxes)
        prompt: String,
    },
    computed: {
        finished() {
            if (this.selectNum > 0){
                return true;
            } else {
                return false;
            }
        }
    },
    created() { //API call made here to set a unique ID, populate and initialize imagearr, and set styling for ImageGrid
        this.id = uniqueId();
        axios
        .get(BASE_URL+'gridSingle')
        .then((response) => {
          this.imagearr = response.data.groups; 
          this.initData();
        });
        document.documentElement.style.setProperty("--content-width", this.size * 100);
        document.documentElement.style.setProperty("--columns", this.size);
    },
    methods: {
        select(num){
            if (this.selectNum < 0) { // if selectNum is negative, it means no image has been selected yet, we change that fact in this method
                this.selectNum = 0
            }
            this.imagearr[this.selectNum].selected = false; // changes data to which component is selected. Changing the "selected" field makes the ImageBox border turn green!
            this.selectNum = num;
            this.imagearr[this.selectNum].selected = true;
        },
        initData() {
            for (const image of this.imagearr) { // Wasn't part of the API call, so we add it here. Wasn't added to the API call to make back-end code cleaner
                image.selected = false;
            }
        },
    },
    data() {
        return {
            selectNum: -1, // shows which index of imagearr was selected by the user
            id: null, // assigned a Unique ID by loadash
            imagearr: [],
            // After the API call is made in created, iamgearr should look like this:
            // imagearr: [
            //     {
            //         "id": 5,
            //         "fid": 2,
            //         "url": "../assets/images/group1/p2.png"
            //         //selected: false
            //     },
            //     {
            //         "id": 4,
            //         "fid": 2,
            //         "url": "../assets/images/group1/p1.png"
            //     },
            //     {
            //         "id": 6,
            //         "fid": 2,
            //         "url": "../assets/images/group1/p3.png"
            //     },
            //     {
            //         "id": 7,
            //         "fid": 2,
            //         "url": "../assets/images/group1/p4.png"
            //     },
            //     {
            //         "id": 0,
            //         "fid": 1,
            //         "url": "../assets/images/group3/p1.png"
            //     },
            //     {
            //         "id": 2,
            //         "fid": 1,
            //         "url": "../assets/images/group3/p3.png"
            //     },
            //     {
            //         "id": 1,
            //         "fid": 1,
            //         "url": "../assets/images/group3/p2.png"
            //     },
            //     {
            //         "id": 3,
            //         "fid": 1,
            //         "url": "../assets/images/group3/p4.png"
            //     },
            //     {
            //         "id": 8,
            //         "fid": 2,
            //         "url": "../assets/images/group1/p3.png"
            //     },
            // ],
        };
    },
    components: { ImageBox }
}
</script>