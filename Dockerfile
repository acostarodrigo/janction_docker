# Use the Blender base image from linuxserver
FROM linuxserver/blender

# Set working directory
WORKDIR /workspace

# Copy your .blend file into the container
# COPY greasepencil-bike.blend /workspace/greasepencil-bike.blend
COPY run_blender.sh /workspace/run_blender.sh

# Set executable permissions for the script
RUN chmod +x /workspace/run_blender.sh

# Command to run the Blender script
CMD ["/workspace/run_blender.sh"]
