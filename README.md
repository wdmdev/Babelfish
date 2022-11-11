# Fork of StarGANv2-VC
This fork focuses on using StarGANv2-VC for Emotional Voice Conversion (EVC).


Below are the original authors and the description of StarGANv2-VC from the original repo: https://github.com/yl4579/StarGANv2-VC

### Yinghao Aaron Li, Ali Zare, Nima Mesgarani

> We present an unsupervised non-parallel many-to-many voice conversion (VC) method using a generative adversarial network (GAN) called StarGAN v2. Using a combination of adversarial source classifier loss and perceptual loss, our model significantly outperforms previous VC models. Although our model is trained only with 20 English speakers, it generalizes to a variety of voice conversion tasks, such as any-to-many, cross-lingual, and singing conversion. Using a style encoder, our framework can also convert plain reading speech into stylistic speech, such as emotional and falsetto speech. Subjective and objective evaluation experiments on a non-parallel many-to-many voice conversion task revealed that our model produces natural sounding voices, close to the sound quality of state-of-the-art text-tospeech (TTS) based voice conversion methods without the need for text labels. Moreover, our model is completely convolutional and with a faster-than-real-time vocoder such as Parallel WaveGAN can perform real-time voice conversion.

Paper: https://arxiv.org/abs/2107.10394

Audio samples: https://starganv2-vc.github.io/

## Base Setup
For setting up the project with the data and trainig configurations from the original paper use:
```bash
make base_setup
```

## Training
Use
```
make train
```

## Further Information
See the original repo: https://github.com/yl4579/StarGANv2-VC

## Acknowledgement
The authors of StarGANv2-VC: Yinghao Aaron Li, Ali Zare, Nima Mesgarani
