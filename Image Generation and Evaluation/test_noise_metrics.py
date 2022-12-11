import unittest
import noise_metrics
import torch
from torchvision.models import inception_v3
import os, requests, json

class TestNoiseMetrics(unittest.TestCase):
    def __equals_parameters(self, model1, model2):
        '''Returns true if the parameters of model1 and model2 are the same.'''
        for param1, param2 in zip(model1.parameters(), model2.parameters()):
            if param1.data.ne(param2.data).sum() > 0:
                return False
        return True
    
    def __download_set(self, dir):
        '''Downloads a test image directory if it does not exist. Returns the directory name.'''
        if os.path.exists(dir): # Images are already downloaded
            desc = os.path.join(dir, 'desc.json') # Remove metrics file
            if os.path.exists(desc):
                os.remove(desc)

        else: # Download images
            if dir == 'test_images/set1':
                url = "https://www.googleapis.com/drive/v3/files/1I-TYXXHrfFciUNvMcgj4Qo8QiXNsI8Yq/view?usp=share_link"
            else:
                url = "https://www.googleapis.com/drive/v3/files/18B-xq4igb7kzVOZoEsWlPSUp281nueXX"
            print("Downloading: " + url)
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                print("Unzipping into: " + dir)
                with open(dir, 'wb') as f:
                    f.write(response.raw.read())
            else:
                print("File not found: Download from https://drive.google.com/drive/u/0/folders/1xQO4n0uBFYxBd-X0QT4w9JICtozZ7PzE")
        
        return dir

    def test_add_noise(self):
        '''Tests if noise_metrics.add_noise() works correctly.'''
        with torch.no_grad():
            inception = inception_v3(pretrained=True) # Load pretrained Inception-v3
            
            # Weights should be changed if Gaussian noise is added to the parameters
            inception2 = noise_metrics.add_noise(inception_v3(pretrained=True), noise_variance=0.2) # Add Gaussian noise to Inception-v3
            if self.__equals_parameters(inception, inception2):
                self.assertFalse("Weights should be changed if noise_variance != 0")
            
            self.assertTrue("noise_metrics works correctly!")

    def test_add_noise_none(self):
        '''Tests if noise_metrics.add_noise() works correctly when no noise is added.'''
        with torch.no_grad():
            inception = inception_v3(pretrained=True) # Load pretrained Inception-v3
            
            # Weights should not be changed if Gaussian noise is not added to the parameters
            inception2 = noise_metrics.add_noise(inception_v3(pretrained=True))
            if not self.__equals_parameters(inception, inception2):
                self.assertFalse("Weights should not be changed if noise_variance == 0")
            
            self.assertTrue("noise_metrics works correctly!")

    def test_calculate_metrics(self):
        '''Tests if noise_metrics.calculate_metrics() works correctly.'''

        set1 = self.__download_set('test_images/set1') # StyleGAN2 AFHQ-Wild, FID: 3.4703217644117217
        set2 = self.__download_set('test_images/set2') # Noised StyleGAN2 AFHQ-Wild, FID: 34.511662174966546

        if not noise_metrics.calculate_metrics(set1, set2, noise_variance=0.2): # Calculate and save metrics
            self.assertFalse("calculate_metrics did not save the metrics!")
        
        # Verify that metrics file was generated
        desc = os.path.join(set1, 'desc.json')
        if not os.path.exists(desc): # Metrics file not found
            self.assertFalse(desc + " was not generated!")

        # Verify that all values were saved
        with open(desc) as desc_file:
            metrics = json.load(desc_file) # Load saved metrics

            keys = ["inception_score_mean",
                    "inception_score_std",
                    "frechet_inception_distance",
                    "kernel_inception_distance_mean",
                    "kernel_inception_distance_std"]
            for key in keys:
                if key not in metrics:
                    self.assertFalse(key + " was not calculated!")
            
            if "noise_variance" not in metrics:
                self.assertFalse("noise_variance was not saved!")
            if metrics["noise_variance"] != 0.2:
                self.assertFalse("noise_variance is not the correct value!")

        self.assertTrue("calculate_metrics works correctly!")

    def test_calculate_metrics_small(self):
        '''Tests if noise_metrics.calculate_metrics() works correctly when image sets are too small.'''

        set1 = self.__download_set('test_images/set1') # StyleGAN2 AFHQ-Wild, FID: 3.4703217644117217
        # '.': No images

        if noise_metrics.calculate_metrics(set1, '.'):
            self.assertFalse("calculate_metrics should not calculate metrics if there are less than 2048 images in either distribution!")

        if noise_metrics.calculate_metrics('.', set1):
            self.assertFalse("calculate_metrics should not calculate metrics if there are less than 2048 images in either distribution!")

        if noise_metrics.calculate_metrics('.', '.'):
            self.assertFalse("calculate_metrics should not calculate metrics if there are less than 2048 images in either distribution!")

        self.assertTrue("calculate_metrics works correctly!")


if __name__ == '__main__':
    unittest.main()
    
    

