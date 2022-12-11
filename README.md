# Evaluation-of-Generation-Metrics
## Pipeline for Generating and Evaluating Image Distributions by Noising Pretrained Weights
Modifying a model’s generation script requires only three lines of code: the first to import the module, the second to add noise to the loaded pretrained weights, and the third to calculate the metrics after the images are generated. Thus, we created a pipeline for generating and evaluating image distributions with any PyTorch image generation model.
1. Put ```noise_metrics.py``` in the main directory.
2. ```pip install torch_fidelity```.
3. Add ```import noise_metrics``` to the top of the generation script.
4. Initialize the image generation model and load the pretrained weights.
5. Add Gaussian noise to the weights using ```noise_metrics.add_noise(model, noise_variance=0)```.
6. Generate the same number of images as the training data.
7. Calculate the metrics using ```noise_metrics.calculate_metrics(dir, traindir, noise_variance=None)```. The scores will be saved in ```[dir]/desc.json```.