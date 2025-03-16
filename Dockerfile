# Use the Blender base image from linuxserver
FROM linuxserver/blender

# Set working directory
WORKDIR /seed

# Copies the script that will fixed the seed for deterministics renders
COPY set_seed.py /seed/set_seed.py

# Set executable permissions for the script 
RUN chmod +x /seed/set_seed.py