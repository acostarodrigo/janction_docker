import random
import bpy

# Set a fixed seed value for deterministic renders
SEED_VALUE = 123455

# Ensure Blender is using Cycles
bpy.context.scene.render.engine = 'CYCLES'

# Set the seed for Cycles rendering
bpy.context.scene.cycles.seed = SEED_VALUE
