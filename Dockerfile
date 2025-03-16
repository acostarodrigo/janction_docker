# Use the Blender base image from linuxserver
FROM linuxserver/blender

# Set working directory
WORKDIR /script

# Copies the script that will fixed the seed for deterministics renders
COPY set_params.py /script/set_params.py

# Set executable permissions for the script 
RUN chmod +x /script/set_params.py