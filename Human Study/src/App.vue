<script>
import axios from 'axios'

export default {
  name: 'all-groups',
  data() {
    return {
      formData: {
        // form field values go here
        user_ranking: [],
        user_q2_bin1_elements: [],
        user_q2_bin2_elements: [],
        user_q3_group_selected: -1,
        user_q4_image_selected: null,
        user_q5_bin1_elements: [],
        user_q5_bin2_elements: []
      }
    }
  },
  methods: {
    async submitForm(e) {
      if (this.$refs['bin-groups-1'].bin1.length == 4 && this.$refs['bin-groups-1'].bin2.length == 4 && this.$refs['image-grid-whole'].selectNum > -1 && this.$refs['image-grid-single'].selectNum > -1 && this.$refs['bin-groups-2'].bin1.length == 4 && this.$refs['bin-groups-2'].bin2.length == 4) {
        this.formData.user_ranking = JSON.parse(JSON.stringify(this.$refs['rank-groups'].imagebars))
        this.formData.user_q2_bin1_elements = JSON.parse(JSON.stringify(this.$refs['bin-groups-1'].bin1))
        this.formData.user_q2_bin2_elements = JSON.parse(JSON.stringify(this.$refs['bin-groups-1'].bin2))
        this.formData.user_q3_group_selected = this.$refs['image-grid-whole'].selectNum
        this.formData.user_q4_image_selected = this.$refs['image-grid-single'].selectNum
        this.formData.user_q5_bin1_elements = JSON.parse(JSON.stringify(this.$refs['bin-groups-2'].bin1))
        this.formData.user_q5_bin2_elements = JSON.parse(JSON.stringify(this.$refs['bin-groups-2'].bin2))
        // this.formData = JSON.parse(JSON.stringify(this.formData))
        console.log(JSON.parse(JSON.stringify(this.formData)))
        console.log("true is the value")
        e.preventDefault()
        try {
          const response = await axios.post('http://localhost:3030/submit-form', JSON.parse(JSON.stringify(this.formData)))
          console.log(response)
          // handle successful form submission
        } catch (error) {
          console.log(error)
          // handle failed form submission
        }
        return true;
      }
      e.preventDefault()
      console.log("false is the value")
      return false;
    }
  }
}
</script>
<script setup>
import RankGroups from './components/RankGroups.vue'
import BinGroups from './components/BinGroups.vue'
import ImageGridSingle from './components/ImageGridSingle.vue';
import ImageGridWhole from './components/ImageGridWhole.vue';
</script>

<!-- This is the file where the components get mounted to as a final HTML file -->

<template>
  <form method="post" action="/submit-form" @submit="submitForm">
    <div class="app">
      <RankGroups ref="rank-groups" :prompt = "'Rank these groups of images from highest image quality to the lowest'"></RankGroups>
      <BinGroups ref="bin-groups-1" :prompt = "'These images belong to one of two different groups, seperate them into their respective groups'"></BinGroups>
      <ImageGridWhole ref="image-grid-whole" :prompt = "'Select the group of images below that has the highest image quality'"></ImageGridWhole>
      <ImageGridSingle ref="image-grid-single" :prompt = "'Select the image from the group of images below that does not belong'"></ImageGridSingle>
      <BinGroups ref="bin-groups-2" :prompt = "'These images belong to one of two different groups, seperate them into their respective groups'"></BinGroups>
      <button type="submit">Submit</button>
      <!-- <button>Emit Event</button> -->
    </div>
  </form>
</template>

<style scoped>
.app {
  position: relative;
  width: 80vw;
  height: auto;
  margin: 0px;
}
</style>