import { expect } from 'chai'
import { shallowMount } from '@vue/test-utils'
import ImageGridWhole from '../../src/components/ImageGridWhole.vue';

describe('ImageGridWhole', () => {
    it('renders the correct prompt', () => {
      const wrapper = shallowMount(ImageGridWhole, {
        propsData: { prompt: 'Select the group of images below that has the highest image quality' },
      });
      expect(wrapper.text()).contain('Select the group of images below that has the highest image quality');
    });
});

