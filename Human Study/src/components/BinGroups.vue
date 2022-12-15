<!-- This component is the binning task. Participants are asked to seperate images into two groups -->

<template>
  <h1>{{prompt}}</h1>
  <div class="BinGroups">
    <!-- This is the left bin -->
    <div class="edge left">
      <p>drag here &gt;</p>
      <draggable style="min-height:250px" :list="bin1" item-key="id" :animation="200" ghost-class="ghost-box"
      :group="this.id">
        <template #item="{ element }">
          <ImageBox :imgurl="element.url" :fidScore="element.fid"></ImageBox>
        </template>
      </draggable>
    </div>
    <!-- This is the left column of images -->
    <draggable class="center-left" style="min-height:250px" :list="shuffle_list_c1" item-key="id" :animation="200"
      ghost-class="ghost-box" :group="this.id">
      <template #item="{ element }">
        <div>
          <ImageBox :imgurl="element.url" :fidScore="element.fid"></ImageBox>
        </div>
      </template>
    </draggable>
    <!-- This is the right column of images -->
    <draggable class="center-right" style="min-height:250px" :list="shuffle_list_c2" item-key="id" :animation="200"
      ghost-class="ghost-box" :group="this.id">
      <template #item="{ element }">
        <div>
          <ImageBox :imgurl="element.url" :fidScore="element.fid"></ImageBox>
        </div>
      </template>
    </draggable>
    <!-- This is the right bin -->
    <div class="edge right">
      <p>&lt; drag here</p>
      <draggable style="min-height:250px" :list="bin2" item-key="id" :animation="200" ghost-class="ghost-box"
        :group="this.id">
        <template #item="{ element }">
          <ImageBox :imgurl="element.url" :fidScore="element.fid"></ImageBox>
        </template>
      </draggable>
    </div>
    <!-- This is the reset/submit buttons that are in the middle of all of it -->
    <div class="button"><button @click="init_state()">Reset</button><br><button v-show="readyToSubmit"
        @click="submit()">Submit</button></div>
  </div>

</template>

<style scoped>
/*CSS styling for each element*/
.BinGroups {
  position: relative;
  height: 60vh;
  margin-top: 1cm;
  margin-bottom: 2cm; 
}

.center-left {
  position: absolute;
  left: 35%;
}

.center-right {
  position: absolute;
  left: 65%;
}

.edge { 
  background-color: khaki;
  min-width: 100px;
  min-height: 250px;
  height: auto;
  width: auto;
  position: absolute;
  top: 0;
  border: 1px solid #000;
  padding: 10px;
}

.button {
  position: absolute;
  top: 0;
  left: 50%;
  border: 1px solid #000;
  padding: 10px;
}

.ghost-box {
  opacity: 0.5;
}

.left {
  left: 0;
}

.right {
  right: 0;
}
</style>

<script>
import ImageBox from './ImageBox.vue';
import draggable from 'vuedraggable';
import uniqueId from 'lodash.uniqueid';
import axios from "axios";

// This URL will be swapped with UMIACS FID server when we are satisfied with development results
const BASE_URL = 'http://127.0.0.1:5000/'

export default {
  name: 'sort-groups',

  components: {
    'ImageBox': ImageBox,
    'draggable': draggable
  },
  computed: {
    readyToSubmit() { // The submit checking code here sees if both of the columns of images are empty (meaning the user binned them)
      return this.shuffle_list_c1.length == 0 && this.shuffle_list_c2.length == 0;
    }
  },
  props: {
    prompt: String,
  },
  methods: {
    init_state() { // method that is called on component creation to initialize data
      let shuffle_list = this.create_shuffle(this.groups)
      this.shuffle_list_c1 = shuffle_list.slice(0, shuffle_list.length / 2)
      this.shuffle_list_c2 = shuffle_list.slice(shuffle_list.length / 2, shuffle_list.length)
      this.bin1 = []
      this.bin2 = []
    },
    submit() { // Will replace this code with an API call to a database later
      console.log("fids for bin1", this.bin1)
      console.log("fids for bin2", this.bin2)
    },

    shuffleArray(array) { //Done so that the columns of the images are not the same
      for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        const temp = array[i];
        array[i] = array[j];
        array[j] = temp;
      }
      return array;
    },

    create_shuffle(grouparr) { /* Appends and shuffles images sampled from two different FID distributions
                                  this could have been implemented in the backend, but was done here to simplify
                                  backend code*/
      let ret = [];
      for (let x = 0; x < this.groups[0].imagelist.length; x++) {
        ret.push({ id: x, fid: this.groups[0].fid, url: this.groups[0].imagelist[x] })
      }
      for (let x = 0; x < this.groups[1].imagelist.length; x++) {
        ret.push({ id: x + this.groups[0].imagelist.length, fid: this.groups[1].fid, url: this.groups[1].imagelist[x] })
      }
      return this.shuffleArray(ret);
    },
  },
  created() { /* When this component is created, give this component a unique ID using loadash.
               A unique ID is important as it prevents a user from dragging an image into another BinGroups task
               We then use Axios to perform an API call to populate our groups array in our data field below.*/
    this.id = uniqueId();
    axios
      .get(BASE_URL+'binGroups')
      .then((response) => {
          this.groups = response.data.imagearrs; 
          this.init_state();
        });
  },
  data() {
    return {
      id: null,
      shuffle_list_c1: [], // Images belonging to the left column
      shuffle_list_c2: [], // Images belonging to the right column
      bin1: [], // An array to be populated by the user (left bin)
      bin2: [], // Right bin
      groups: [], 
      // After the API call in created(), the groups array is populated with information in the format below:  
      // [{
      //     fid: 1,
      //     imagelist: ['../assets/images/group3/p1.png', '../assets/images/group3/p2.png', '../assets/images/group3/p3.png', '../assets/images/group3/p4.png'],
      //   },
      //   {
      //     fid: 2,
      //     imagelist: ['../assets/images/group1/p1.png', '../assets/images/group1/p2.png', '../assets/images/group1/p3.png', '../assets/images/group1/p4.png'],
      //   }
      // ],
    };
  }

}

</script>
