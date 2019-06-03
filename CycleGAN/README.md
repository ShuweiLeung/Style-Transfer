# pytorch-CycleGAN
Pytorch implementation of CycleGAN [1].

* you can download datasets: https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/
* you can see more information for network architecture and training details in https://arxiv.org/pdf/1703.10593.pdf

## Dataset

You can download datasets manually: https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/

Downloadable datasets: apple2orange, summer2winter_yosemite, horse2zebra, monet2photo, cezanne2photo, ukiyoe2photo, vangogh2photo, maps, cityscapes, facades, iphone2dslr_flower, ae_photos

Or you can run script to download dataset automatically via below the command:

`./download_dataset <dataset_name>`

The dataset before using CycleGAN should be organized as following structure:

```
.
├── datasets                   
|   ├── <dataset_name>         # i.e. brucewayne2batman
|   |   ├── trainA             # Trainset A
|   |   ├── trainB             # Trainset B
|   |   ├── testA              # Testset A
|   |   ├── testB              # Testset B
```

## Results

Please visit the demo website to see more results!

**[Demo Website](https://sites.google.com/view/ece285-styletransfer/%E9%A6%96%E9%A1%B5?authuser=1)**

## Development Environment

* Ubuntu 14.04 LTS
* NVIDIA GTX 1080 ti
* cuda 8.0
* Python 2.7.6
* pytorch 0.1.12
* matplotlib 1.3.1
* scipy 0.19.1

## Reference

[1] Zhu, Jun-Yan, et al. "Unpaired image-to-image translation using cycle-consistent adversarial networks." arXiv preprint arXiv:1703.10593 (2017).

(Full paper: https://arxiv.org/pdf/1703.10593.pdf)
