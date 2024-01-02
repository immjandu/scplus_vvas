# scplus_vvas
SCplus with VVAS(Vitis Video Analytics SDK)
- VVAS v.2.0
- Vitis-AI-Library v.2.5


## prepare VVAS

```shell
cd scplus_vvas/VVAS

# set cross-compile env
source ~/petalinux_sdk_2022.1/environment-setup-cortexa72-cortexa53-xilinx-linux

# cross-compile for Edge
./build_install_vvas.sh Edge 1 1

# send results(install/vvas_installer.tar.gz) to Edge
scp install/vvas_installer.tar.gz <board ip>:./

# (host in Edge) 
cd VVAS
mkdir install
tar -xvf vvas_installer.tar.gz -C ./install
# run docker (docker image : xilinx/smartcam)
docker exec -it test bash

# (docker in Edge) change old VVAS to new one
cp -Pra VVAS/install/usr/lib/* /usr/lib/aarch64-linux-gnu/
cp -Pra VVAS/install/usr/lib/gstreamer-1.0/* /usr/lib/aarch64-linux-gnu/gstreamer-1.0/
cp -Pra VVAS/install/usr/lib/pkgconfig/* /usr/lib/aarch64-linux-gnu/pkgconfig/
```

## run face-detection/recognition

- model
  - face detection : densebox_640_360
  - face recognition : InceptionResNetV1

```shell
INPUT_FILE="data/all5_720p.mp4"
```


### face detection
```shell
gst-launch-1.0 filesrc location=${INPUT_FILE} \
! qtdemux ! h264parse ! omxh264dec internal-entropy-buffers=2 \
! videorate max-rate=30 \
! queue ! vvas_xinfer preprocess-config="resource/fd_preprocess_cfg.json" infer-config="resource/fd_inference_cfg.json" \
! queue ! vvas_xmetaconvert config-location="resource/metaconvert_cfg.json" \
! vvas_xoverlay \
! omxh264enc target-bitrate=3000 ! video/x-h264, alignment=au \
! filesink location=./out_fd.h264
```

### face detection & recognition
```shell
gst-launch-1.0 filesrc location=${INPUT_FILE} \
! qtdemux ! h264parse ! omxh264dec internal-entropy-buffers=2 \
! videorate max-rate=30 \
! queue ! vvas_xinfer preprocess-config="resource/fd_preprocess_cfg.json" infer-config="resource/fd_inference_cfg.json" name=fd \
! queue ! vvas_xinfer preprocess-config="resource/fr_preprocess_cfg.json" infer-config="resource/fr_inference_cfg.json" name=fr \
! queue ! vvas_xmetaconvert config-location="resource/metaconvert_cfg.json" \
! vvas_xoverlay \
! omxh264enc target-bitrate=3000 ! video/x-h264, alignment=au \
! filesink location=./out_fr.h264
```

## TroubleShooting

- gdb: error while loading shared libraries: libbabeltrace.so.1: cannot open shared object file: No such file or directory
```shell
apt install -y libbabeltrace-ctf-dev libsource-highlight-dev libdebuginfod-dev
```

- opencv version : If you may need v.4.5, you can re-cross-compile opencv v.4.5.
```shell
# remove all old opencv
sudo apt purge libopencv* python-opencv
sudo apt -y autoremove
sudo find /usr/local/ -name "*opencv*" -exec rm -rfi {} \;

# install some packages
sudo apt install -y build-essential cmake pkg-config \
	libjpeg-dev libtiff5-dev libpng-dev ffmpeg libavcodec-dev libavformat-dev libswscale-dev libxvidcore-dev libx264-dev libxine2-dev \
	libv4l-dev v4l-utils libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgtk-3-dev \
	mesa-utils libgl1-mesa-dri libgtkgl2.0-dev libgtkglext1-dev \
	libatlas-base-dev gfortran libeigen3-dev python3-dev python3-numpy

# download the opencv file to install
mkdir opencv && cd opencv
wget -O opencv.zip "https://github.com/opencv/opencv/archive/4.5.2.zip" && unzip opencv.zip
wget -O opencv_contrib.zip "https://github.com/opencv/opencv_contrib/archive/4.5.2.zip" && unzip opencv_contrib.zip
ls
# you can get like...
# opencv-4.5.2  opencv.zip  opencv_contrib-4.5.2  opencv_contrib.zip

# cross-compile
CROSS_COMPILE_PARENT_DIR="/home/ubuntu/Vitis-AI/petalinux_sdk_2022.1" # need to change to yours
source "${CROSS_COMPILE_PARENT_DIR}/environment-setup-cortexa72-cortexa53-xilinx-linux"
cd opencv-4.5.2 && mkdir build && cd build
INSTALL_DIR="${CROSS_COMPILE_PARENT_DIR}/sysroots/cortexa72-cortexa53-xilinx-linux/usr"
cmake .. \
	-D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=${INSTALL_DIR} \
	-D WITH_TBB=OFF \
	-D WITH_IPP=OFF \
	-D WITH_1394=OFF \
	-D BUILD_WITH_DEBUG_INFO=OFF \
	-D BUILD_DOCS=OFF \
	-D INSTALL_C_EXAMPLES=ON \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D BUILD_EXAMPLES=OFF \
	-D BUILD_PACKAGE=OFF \
	-D BUILD_TESTS=OFF \
	-D BUILD_PERF_TESTS=OFF \
	-D WITH_QT=OFF \
	-D WITH_GTK=ON \
	-D WITH_OPENGL=ON \
	-D BUILD_opencv_python3=ON \
	-D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-4.5.2/modules \
	-D WITH_V4L=ON \
	-D WITH_FFMPEG=ON \
	-D WITH_GSTREAMER=ON \
	-D WITH_XINE=ON \
	-D OPENCV_ENABLE_NONFREE=ON \
	-D BUILD_NEW_PYTHON_SUPPORT=ON \
	-D OPENCV_SKIP_PYTHON_LOADER=ON \
	-D OPENCV_GENERATE_PKGCONFIG=ON ../ \
	-D PYTHON3_INCLUDE_DIR=${INSTALL_DIR}/include/python3.9 \
	-D PYTHON3_NUMPY_INCLUDE_DIRS=${INSTALL_DIR}/lib/python3.9/site-packages/numpy/core/include \
	-D PYTHON3_PACKAGES_PATH=${INSTALL_DIR}/lib/python3.9/site-packages \
	-D PYTHON3_LIBRARY=${INSTALL_DIR}/lib/libpython3.9.so

time make -j$(nproc)
make install

sudo sh -c "echo "${INSTALL_DIR}/lib" > /etc/ld.so.conf.d/opencv.conf"
sudo ldconfig

```