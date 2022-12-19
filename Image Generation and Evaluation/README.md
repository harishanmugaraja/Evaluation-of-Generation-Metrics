# Image Generation and Evaluation

## [StyleGAN2-ADA-PyTorch](https://github.com/tuallen/noise_metrics-stylegan2-ada-pytorch) 
We implemented our image generation and evaluation pipeline in [NVlabs/stylegan2-ada-pytorch](https://github.com/NVlabs/stylegan2-ada-pytorch). See our [fork](https://github.com/tuallen/noise_metrics-stylegan2-ada-pytorch) for more details.

## ```BigGAN```
BigGAN with our image generation and evaluation pipeline.

## Pipeline for Generating and Evaluating Image Distributions by Noising Pretrained Weights
Modifying a model’s generation script requires only three lines of code: the first to import the module, the second to add noise to the loaded pretrained weights, and the third to calculate the metrics after the images are generated. Thus, we created a pipeline for generating and evaluating image distributions with any PyTorch image generation model.
1. Put ```noise_metrics.py``` in the main directory.
2. ```pip install torch_fidelity```.
3. Add ```import noise_metrics``` to the top of the generation script.
4. Initialize the image generation model and load the pretrained weights.
5. Add Gaussian noise to the weights using ```noise_metrics.add_noise(model, noise_variance=0)```.
6. Generate the same number of images as the training data.
7. Calculate the metrics using ```noise_metrics.calculate_metrics(dir, traindir, noise_variance=None)```. The scores will be saved in ```[dir]/desc.json```.

## ```noise_metrics.py```
### Setup
1. Install PyTorch following the directions on their [website](https://pytorch.org/).
2. ```pip install torch_fidelity```

### ```add_noise(model, noise_variance)```
Adds Gaussian noise to the model parameters.

* Arguments
  * ```model```: PyTorch model
  * ```noise_variance```: Variance of the Gaussian noise; adds no noise by default
* Returns: ```model``` with Gaussian noise added to the parameters

### ```calculate_metrics(dir, traindir, noise_variance=None)```
Calculate Inception Score (ISC), Frechet Inception Distance (FID), and Kernel Inception Distance (KID) for generated images. Saves metrics as ```[dir]/desc.json```. Optionally,The variance of the Gaussian noise that was added to the model can be added to the file. Requires [```toshas/torch-fidelity```](https://github.com/toshas/torch-fidelity)
    
* Arguments:
  * dir: Directory of the generated images
  * traindir: Directory of the training images
  * noise_variance: Variance of the Gaussian noise added to the weights; not saved by default
* Outputs:
  * ```[dir]/desc.json```: Dictionary of ISC, FID, KID, and (optionally) noise_variance
* Returns: ```True``` if metrics are saved 

## ``test_noise_metrics.py``
Collection of tests for verifying ``noise_metrics.py``. 
* ```__download_set(dir)``` downloads a test image directory if it does not exist. Alternatively, you can download and unzip the sets into ```./test_images/``` from [Google Drive](https://drive.google.com/drive/u/0/folders/1xQO4n0uBFYxBd-X0QT4w9JICtozZ7PzE).
  * ```test_images/set1```: StyleGAN2 AFHQ-Wild, FID: 3.4703217644117217
    * 1,000 `.png` images, 480MB
  * ```test_images/set2```: Noised StyleGAN2 AFHQ-Wild, FID: 34.511662174966546
    * 1,000 `.png` images, 641MB
