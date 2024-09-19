# Drag Gan API

Method: Post
URL: http://127.0.0.1:5000/upload
Body String (raw):
{
  "image_data": (Base 64 string data),
  "point_start": [[point_start_1, point_start_2]],
  "point_target": [[point_target_1, point_target_2]]
}
Return:
{
  "image_data": (Base 64 string data)
}

## Acknowledgement

This code is based on [DragGAN](https://github.com/XingangPan/DragGAN). 
I have simplified it by building an API for easier use.

## License

The code related to the DragGAN algorithm is licensed under [CC-BY-NC](https://creativecommons.org/licenses/by-nc/4.0/).
However, most of this project are available under a separate license terms: all codes used or modified from [StyleGAN3](https://github.com/NVlabs/stylegan3) is under the [Nvidia Source Code License](https://github.com/NVlabs/stylegan3/blob/main/LICENSE.txt).

Any form of use and derivative of this code must preserve the watermarking functionality showing "AI Generated".

## BibTeX

```bibtex
@inproceedings{pan2023draggan,
    title={Drag Your GAN: Interactive Point-based Manipulation on the Generative Image Manifold},
    author={Pan, Xingang and Tewari, Ayush, and Leimk{\"u}hler, Thomas and Liu, Lingjie and Meka, Abhimitra and Theobalt, Christian},
    booktitle = {ACM SIGGRAPH 2023 Conference Proceedings},
    year={2023}
}
```
