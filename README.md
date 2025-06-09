# jetson-nano
Fun projects with Jetson Nano


# Docker run command
sudo docker run -it --rm \
  --runtime nvidia \
  --network host \
  --volume /tmp/.X11-unix:/tmp/.X11-unix \
  -e DISPLAY=$DISPLAY \
  yolov3-csi-nano
