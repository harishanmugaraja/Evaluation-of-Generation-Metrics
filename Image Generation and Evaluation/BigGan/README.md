# BigGan generation and evaluation

## Pretrained BigGan
We a pretrained BigGan model trained on ImageNet. Original implementation is found here: https://colab.research.google.com/drive/1D_UYVtPz3yEHkACzztwSZM9NLlZZxNjT?usp=sharing

### Our addition - Applying noise
Our changes and to the original implementation can be found here:
https://colab.research.google.com/drive/172LzGRTdYhyQQnxL6btBPlNqIG-lCSJu#scrollTo=NHddR0lzGO9G

The notebook calculates FID and IS scores on the pretrained BigGan with a Gaussain noise applied to the models parameters. The variance of the Gaussain noise is given by the ```--noise_variance``` parameter. 
