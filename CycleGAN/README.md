# CycleGAN

## Dataset

You can download datasets manually: https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/

Downloadable datasets: apple2orange, summer2winter_yosemite, horse2zebra, monet2photo, cezanne2photo, ukiyoe2photo, vangogh2photo, maps, cityscapes, facades, iphone2dslr_flower, ae_photos

Or you can run shell script to download dataset automatically via below command:

`./download_dataset <dataset_name>`

The dataset before using CycleGAN should be organized as following structure:

```
.
├── data                   
|   ├── <dataset_name>         # Like facades
|   |   ├── trainA             # Trainset A
|   |   ├── trainB             # Trainset B
|   |   ├── testA              # Testset A
|   |   ├── testB              # Testset B
```

## Results

The corresponding result is saved in <dataset\_name>\_results.

The result directory is organized as following structure:

```
.
├── <dataset_name>_results   # Dataset name like facades              
|   ├── test_results         # test_results
|   |   ├── AtoB             # A transfers to B
|   |   ├── BtoA             # B transfers to A
|   ├── train_results        # train_results
|   |   ├── AtoB             # A transfers to B
|   |   ├── BtoA             # B transfers to A
```

## Demo

Please visit the demo website to see more results!

**[Demo Website](https://sites.google.com/view/ece285-styletransfer/%E9%A6%96%E9%A1%B5?authuser=1)**


## Reference

[1] Zhu, Jun-Yan, et al. "Unpaired image-to-image translation using cycle-consistent adversarial networks." arXiv preprint arXiv:1703.10593 (2017).

(Full paper: https://arxiv.org/pdf/1703.10593.pdf)
