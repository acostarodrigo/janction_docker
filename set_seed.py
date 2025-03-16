import random
import bpy

# Set the seed (use the same value for consistent results)
seed_value = 123455
random.seed(seed_value)
bpy.context.scene.render.seed = seed_value  # Set the seed for rendering