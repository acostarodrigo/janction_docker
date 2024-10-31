#!/bin/sh
echo "**********************************************"
echo "Starting Blender with START_FRAME=$START_FRAME and END_FRAME=$END_FRAME"
echo "**********************************************"
blender -b /workspace/greasepencil-bike.blend -o /workspace/output/frame_###### -F PNG -E CYCLES -s $START_FRAME -e $END_FRAME -a
