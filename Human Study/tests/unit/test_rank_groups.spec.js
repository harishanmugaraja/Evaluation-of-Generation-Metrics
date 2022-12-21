import { expect } from 'chai'
import { shallowMount } from '@vue/test-utils'
import RankGroups from '../../src/components/RankGroups.vue';

describe('RankGroups', () => {
  it('renders the correct prompt', () => {
    const wrapper = shallowMount(RankGroups, {
      propsData: { prompt: 'Rank these groups of images from highest image quality to the lowest' },
    });
    expect(wrapper.text()).contain('Rank these groups of images from highest image quality to the lowest');
  });
});

describe('RankGroups', () => {
  it('can be dragged and dropped', () => {
    const wrapper = shallowMount(RankGroups, {
      propsData: { prompt: 'Rank these groups of images from highest image quality to the lowest' },
    });
    // const draggableElement = wrapper.find('draggable-stub').element;
    // console.log(wrapper.html())
    // console.log(wrapper.find('draggable-stub').element)
    // const dropzoneElement = wrapper.find('.dropzone').element;

    wrapper.vm.$nextTick(() => {
      wrapper.trigger('mousedown', { button: 0, clientX: 0, clientY: 0 });
      wrapper.trigger('mousemove', { clientX: 100, clientY: 100 });
      wrapper.trigger('mouseup');

    //   expect(dropzoneElement.textContent).to.include('Draggable element dropped');
    });
  });
});
