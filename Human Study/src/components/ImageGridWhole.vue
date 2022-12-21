<!-- This code is very simlar to ImageGridSingle, but this task is meant to ask users to pick which group of images they prefer -->
<template>
    <h1>{{prompt}}</h1>
    <SquareGrid class = "multi" v-for="(imagearr, index) in imagearrs" :key=index @click="select(index)">    <!-- While this code looks almost identical, the v-for on this line generates multiple SquareGrids -->
        <div v-for="(element, index) in imagearr" :key="index">
            <ImageBox :imgurl="element.url" :fidScore = "element.fid" :seqNum="index" :selected="element.selected"></ImageBox>
        </div>
    </SquareGrid>
</template>

<style scoped lang="scss">

.multi {
    margin-top: 1cm;
    margin-bottom: 1cm;
}

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
    grid-row-gap: var(--gutter);

}

// This code overwrites the code in created(), but here are some things you can do with media queries if you put them in SquareGrid

//decide with media queries when to add another column 

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

const BASE_URL = 'http://127.0.0.1:5000/'

import axios from 'axios';

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
        .get(BASE_URL+'gridWhole')
        .then((response) => {
          this.imagearrs = response.data.imagearrs; 
          this.initData();
        });
        document.documentElement.style.setProperty("--content-width", this.size * 100);
        document.documentElement.style.setProperty("--columns", this.size);

    },
    methods: {
        select(num){ // This method is a bit more complicated than the select for ImageGridSingle, but the logic is the same.
            if (this.selectNum < 0) {// if selectNum is negative, it means no image has been selected yet, we change that fact in this method
                this.selectNum = 0
            }
            let imagearr = this.imagearrs[this.selectNum] // iterate through one grid and change border to black
            for (const image of imagearr) {
                image.selected = false;
            }
            this.selectNum = num
            imagearr = this.imagearrs[this.selectNum] // iterate through the other grid and change border to green
            for (const image of imagearr) {
                image.selected = true;
            }
            
        },
        initData() {
            for (const imagearr of this.imagearrs) {
                for (const image of imagearr) {
                    image.selected = false;
                }
            }
        },
    },
    data() {
        return {
            selectNum: -1, // shows which index of imagearr was selected by the user
            id: null, // assigned a Unique ID by loadash
            imagearrs: [],
        };
    },
    components: { ImageBox }
}
</script>