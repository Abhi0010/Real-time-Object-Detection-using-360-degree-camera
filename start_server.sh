#!/bin/bash

python app.py "$@"

#python fisheye_to_equi.py "--sourceProjection SideBySideFisheye --sourceImage images/sidebysidefisheye.png --sourceProjection SideBySideFisheye --outProjection Equirectangular --outImage foo1.png --outWidth 768 --outHeight 512"
#python equi_to_cube.py "--sourceProjection Equirectangular --sourceImage foo1.png --sourceProjection Equirectangular --outProjection CubeMap --outImage "front.png right.png back.png left.png top.png bottom.png" --outWidth 512 --outHeight 512"