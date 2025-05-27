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
This study uses an EEG dataset collected from 28 participants. Each participant played four computer games designed to evoke different emotional states: boring, calm, horror, and funny. Each game lasted 5 minutes, resulting in a total of 20 minutes of EEG recordings for each subject.Subjects rated on participants emotional responses using the Self-Assessment Manikin (SAM) scale, which measures two dimensions: valence (pleasantness) and arousal (intensity).The dataset download link can be found on Kaggle or referenced via the following DOI: https://doi.org/10.1016/j.bspc.2020.101951

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
