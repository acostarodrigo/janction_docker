# Start from an Ubuntu base image (no ARM here since Rosetta handles x86)
FROM linuxserver/blender

# Set working directory
WORKDIR /workspace

# Copy your .blend file into the container
COPY greasepencil-bike.blend /workspace/greasepencil-bike.blend

# Command to run Blender in background mode
CMD ["blender", "-b", "/workspace/greasepencil-bike.blend", "-o", "/workspace/output/frame_######", "-F", "PNG", "-E", "CYCLES", "-s", "16", "-e", "30", "-a"]