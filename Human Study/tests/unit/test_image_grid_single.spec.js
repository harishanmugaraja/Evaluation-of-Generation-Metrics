import { expect } from 'chai'
import { shallowMount } from '@vue/test-utils'
import ImageGridSingle from '../../src/components/ImageGridWhole.vue';

describe('ImageGridSingle', () => {
    it('renders the correct prompt', () => {
      const wrapper = shallowMount(ImageGridSingle, {
        propsData: { prompt: 'Select the image from the group of images below that does not belong' },
      });
      expect(wrapper.text()).contain('Select the image from the group of images below that does not belong');
    });
});

describe('ImageGridSingle', () => {
    it('changes its CSS when clicked', () => {
      const wrapper = shallowMount(ImageGridSingle);
      console.log(wrapper.html())
    });
  });