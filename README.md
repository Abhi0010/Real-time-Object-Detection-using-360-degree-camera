
<h1 align="center">:desktop_computer: 360° Machine Vision For Blind LiDAR Based Hat :desktop_computer:</h1>
<h3 align="center">An Machine Vision System with Object Detection and Depth Estimation with Text to Speech for assisting a blind person</h3>
![Python](https://img.shields.io/badge/python-v3.7-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)
![NumPy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)


## Directory
```graphql
./src/* 
  ├─ src/images - # Processor modules and driver simulation results
  ├─ src/ALU.txt - # ALU Module of the processor
  ├─ src/DATAMEM.txt - # 16 Kilo Byte Data Memory
  ├─ src/GROUP00TEST-Driver.txt - # Testing Driver Code for Group 00 Instruction set
  ├─ src/GRP01&11TEST-Driver.txt - # Testing Driver Code for Group 01 && 11 Instruction set
  ├─ src/INSMEM.txt - # Instruction memory with 256 x 24 Bit instruction capability
  ├─ src/PROCESSOR.txt - # Processor module which assembles all sub-modules of the processor
  └─ src/PROCESSOR-STIMULUS.txt - # Processor Driver Code example
./Instruction-Set.pdf - # Driver instructions for the processor
./Doc.pdf - # Architecture and instruction formats
```

## Implementation

TBD...


### User Guide

<details>
<summary>Test Commands</summary>

Currently commands are set to Image show. 


Can be modified to Image save.


Example command for Fisheye to Cubemap: 

`python app.py --approach Cubemap --input Image --image_path  test.png --output_path "front.png right.png back.png left.png top.png bottom.png" --output_width 512 --output_height 512`

Example command for Fisheye to Equi:

`python app.py --approach Equirectangular --input Image --image_path  test.png --output_path "equi.png" --output_width 512 --output_height 512`
 
</details>

## Authors

👤 **Meet Doshi**

- GitHub: [@meetdoshi90](https://github.com/meetdoshi90)
- LinkedIn: [@meetdoshi90](https://linkedin.com/in/meetdoshi90)

👤 **Abhishek Potdar**


👤 **Aniket Kulkarni**


👤 **Shafina Charania**


👤 **Param Shah**


👤 **Omkar Gavandi**




## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

## Show your support

Give a ⭐️ if you like this project!

## 📝 License

This project is licensed with [GNU General Public License](./LICENSE).


<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://linkedin.com/in/meetdoshi90" target="blank"><img align="center" src="https://cdn.worldvectorlogo.com/logos/linkedin-icon-2.svg" alt="meetdoshi90" height="30" width="40" /></a>
</p>
