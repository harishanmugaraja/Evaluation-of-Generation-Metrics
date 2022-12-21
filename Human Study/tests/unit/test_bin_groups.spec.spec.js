import { expect } from 'chai'
import { shallowMount } from '@vue/test-utils'
import BinGroups from '../../src/components/BinGroups.vue';

describe('BinGroups', () => {
    it('renders the correct prompt', () => {
      const wrapper = shallowMount(BinGroups, {
        propsData: { prompt: 'These images belong to one of two different groups, seperate them into their respective groups' },
      });
      expect(wrapper.text()).contain('These images belong to one of two different groups, seperate them into their respective groups');
    });
});