# Cheer Up System based on EEG
![Cheer Up System](./images/introduction.png)

## Introduction

Cheer Up System based on EEG is a real-time brain-computer interface (BCI) project designed to spark new energy in Taiwan’s sports culture. Our mission is to build a bridge between athletes and fans—emotionally and visually.


## Vedio Demo
影片

## System Pipline
By decoding EEG signals from athletes using a deep learning model, we estimate athlete's mental state in terms of Valence, Arousal, and Dominance (VAD). These emotional signals are sent live to a custom-built cloud server, where they’re transformed into lighting parameters.
Here’s where the magic happens: we created a visual application that turns those parameters into dynamic light displays—fans literally see what the athlete feels. It’s a brand-new way to cheer, connect, and celebrate team spirit through synchronized emotion and immersive atmosphere.
![Cheer Up System](./images/system-pipeline.png)

## Data description
### Gameemo
This study uses an EEG dataset collected from 28 participants. Each participant played four computer games designed to evoke different emotional states: boring, calm, horror, and funny. Each game lasted 5 minutes, resulting in a total of 20 minutes of EEG recordings for each subject.Subjects rated on participants emotional responses using the Self-Assessment Manikin (SAM) scale, which measures two dimensions: valence (pleasantness) and arousal (intensity).The dataset detail can be found via the following DOI: https://doi.org/10.1016/j.bspc.2020.101951

### Data Preprocessing
this study applied ICA along with the ICLabel tool to automatically classify the ICs extracted from the EEG signals. The following table shows the number of ICs in each category after different preprocessing steps (raw, bandpass filtering, and ASR):
![Cheer Up System](./images/data_preprocessing.png)

The results show that ASR effectively improves signal quality and enhances the reliability of subsequent emotion recognition analysis.

## AI Model framework
Our system brings together signal processing and deep learning to turn raw brainwaves into real-time ambient experiences. Here’s what’s under the hood:
架構圖
## Evaluation
### Experiment Setup
### Results

# Installation & Setup Guide

This document provides step-by-step instructions for setting up the dataset, training, and inference environment for this project.

---

## 1. Dataset Download

Download the dataset from the following link:

[**Dataset Download**](https://www.kaggle.com/datasets/sigfest/database-for-emotion-recognition-system-gameemo)

After downloading, upload the dataset to your Google Drive under the following path:
- `/content/drive/My Drive/Colab Notebooks/YOUR_PROJECT_NAME/`

## 2. Model Training Notebook

The model training code is located in the `model` directory:

- `train_model.ipynb`

To use it:

1. Download `train_model.ipynb` and upload it to your Google Drive under the path
- `/content/drive/My Drive/Colab Notebooks/YOUR_PROJECT_NAME/`
2. Open the notebook in **Google Colab**.
3. Modify all dataset and save path references in the notebook to match your Drive directory structure.
4. Run the notebook to train your model.

## 3. Inference Notebook and Pretrained Weight

The inference notebook and pretrained model are also located in the `model` directory:

- `1DCNN_2ch_4class_push_vad.ipynb`
- `1DCNNmodel_4class_2ch.pt`

To use them:

1. Download both files and place them in your Google Drive under:
- `/content/drive/My Drive/Colab Notebooks/YOUR_PROJECT_NAME/`
2. Open `1DCNN_2ch_4class_push_vad.ipynb` in **Google Colab**.
3. Update file paths in the notebook to correctly reference the `1DCNNmodel_4class_2ch.pt` model and test data.
4. Run the notebook to perform inference.

