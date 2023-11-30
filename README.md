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

## Trouble Shooting

- gdb: error while loading shared libraries: libbabeltrace.so.1: cannot open shared object file: No such file or directory
```shell
apt install -y libbabeltrace-ctf-dev libsource-highlight-dev libdebuginfod-dev
```