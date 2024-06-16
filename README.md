# BT_VITON - Bangladeshi-Traditional-Virtual-Try-on

### Application of Virtual Outfit Trial Shop with Deep Learning Technique and Computer Vision.->

### Reference Paper: https://arxiv.org/abs/2206.14180

**Abstract:** *We aim to build a project based on generating a full-body human pose with different clothes from a single image input from the user. This model will allow users to take pictures and choose the desired outfit which will be placed onto the picture of the user as a try-on virtually. The virtual item like dresses will be rendered onto the image and generate an output image by blending the virtual item with the real image. We will also introduce Bangladeshi dresses (e.g., Panjabi, Saree, Salwar-Kameez). It will basically create a virtual outfit try-on environmen*

## Installation

Clone this repository:

```
git clone https://github.com/KaziRamisaRifa/BT_VITON-Bangladeshi-Traditional-Virtual-Try-on
cd ./BT_VITON-Bangladeshi-Traditional-Virtual-Try-on/
```

Install PyTorch and other dependencies:

```
conda create -n {env_name} python=3.8
conda activate {env_name}
conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch-lts -c nvidia
pip install opencv-python torchgeometry Pillow tqdm tensorboardX scikit-image scipy
```
Install apex NVIDIA , dependecies for Try on Generator
```
!git clone https://github.com/NVIDIA/apex
%cd /content/HR-VITON/apex
!pip install -v --disable-pip-version-check --no-cache-dir ./
```

## Dataset
We train and evaluate our model using our own dataset. link is comming soon....

We assume that you have downloaded it into `./data`.

## Inference

Here are the download links for each required pre-train model checkpoint:

- Try-on condition generator: [link](https://drive.google.com/file/d/1XJTCdRBOPVgVTmqzhVGFAgMm2NLkw5uQ/view?usp=sharing)
- Try-on condition generator (discriminator): [link](https://drive.google.com/file/d/1Gi185XUAI3w4srReTbp3eIzkjFC51ym-/view?usp=sharing)
- Try-on image generator: [link](https://drive.google.com/file/d/1BkSA8UJo-6eOkKcXTFOHK80Esc4vBmVC/view?usp=sharing)
- AlexNet (LPIPS): [link](https://drive.google.com/file/d/1FF3BBSDIA3uavmAiuMH6YFCv09Lt8jUr/view?usp=sharing), we assume that you have downloaded it into `./eval_models/weights/v0.1`.

```python
python test_condition.py --gpu_ids 0 --tocg_checkpoint /checkpoints --D_checkpoint /content/HR-VITON/checkpoint/ --datasetting unpaired --dataroot /content/HR-VITON/data --data_list /content/HR-VITON/data/test_pairs.txt --norm_const 1.5 --Ddownx2 --Ddropout --occlusion --spectral
```

## Train try-on condition generator

```%cd /content/HR-VITON/
!python train_condition.py --name condition_gen --workers 2 --batch-size 4 --display_count 9 --save_count 99 --keep_step 99 --gpu_ids 0 --test_datasetting paired --Ddownx2 --Ddropout --lasttvonly --interflowloss --occlusion 
```

## Train try-on image generator

```python
%cd /content/HR-VITON
!python train_generator.py --name ramisa_train_gen -b 4 -j 4 --gpu_ids 0 --fp16 --tocg_checkpoint '/content/HR-VITON/checkpoints/condition_gen/tocg_final.pth' --display_count 99 --save_count 999 --keep_step 900 --decay_step 99 --occlusion 
```
