import bpy

# Set a fixed seed for repeatability
SEED_VALUE = 123455

# Ensure Cycles is the renderer
bpy.context.scene.render.engine = 'CYCLES'

# Set sampling settings (important for determinism)
bpy.context.scene.cycles.seed = SEED_VALUE  # This should control random sampling
bpy.context.scene.cycles.use_animated_seed = False  # Ensure the seed stays fixed across frames

# Disable denoising (denoising can introduce randomness)
bpy.context.scene.cycles.use_denoising = False

# Ensure sampling settings are consistent
bpy.context.scene.cycles.samples = 128  # Make sure all nodes use the same sample count
bpy.context.scene.cycles.adaptive_threshold = 0  # Avoid dynamic changes in sample count
bpy.context.scene.cycles.use_adaptive_sampling = False  # Disable adaptive sampling
bpy.context.scene.cycles.max_bounces = 12  # Set maximum bounces
bpy.context.scene.cycles.diffuse_bounces = 4  # Set diffuse bounces
bpy.context.scene.cycles.glossy_bounces = 4  # Set glossy bounces
bpy.context.scene.cycles.transmission_bounces = 12  # Set transmission bounces
bpy.context.scene.cycles.volume_bounces = 0  # Set volume bounces

# Force CPU-only rendering (for full determinism)
bpy.context.preferences.addons['cycles'].preferences.compute_device_type = 'NONE'
bpy.context.scene.cycles.device = 'CPU'

# Ensure threads are consistent
bpy.context.scene.render.threads = 1  # Lock number of threads for determinism
