# Comfyui-LatentOR
Latent detection logic node

If you have two streams of latent but only one is ever live at a given time you can use this to have comfy automatically pick the enabled one. Everything else I found required a manual switch toggle so I explained the issue to grok and it gave me this, which I am now giving to anyone who is interested.

Create a folder in custom_nodes names whatever you want and put the --init--.py file in there. Restart comfy and it's in Latents > Utils in the custom node section of the gallery as "Latent OR Gate (Auto)"
