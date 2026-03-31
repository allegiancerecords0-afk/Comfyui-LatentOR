import torch

class LatentORGate:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "latent_a": ("LATENT", {"forceInput": True}),
                "latent_b": ("LATENT", {"forceInput": True}),
            },
            "optional": {
                "threshold": ("FLOAT", {
                    "default": 0.00001,
                    "min": 0.0,
                    "max": 10.0,
                    "step": 0.000001,
                    "description": "Anything above this = 'has information'"
                }),
                "priority": (["A", "B"], {"default": "A"}),
            }
        }

    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("latent",)
    FUNCTION = "or_gate"
    CATEGORY = "latent/utils"

    def or_gate(self, latent_a, latent_b, threshold=0.00001, priority="A"):
        def has_information(latent):
            samples = latent["samples"]
            if samples is None or samples.numel() == 0:
                return False
            mean_abs = torch.mean(torch.abs(samples)).item()
            return mean_abs > threshold

        info_a = has_information(latent_a)
        info_b = has_information(latent_b)

        if info_a and not info_b:
            return (latent_a,)
        elif info_b and not info_a:
            return (latent_b,)
        elif info_a and info_b:
            # Both have data → use priority
            return (latent_a if priority == "A" else latent_b,)
        else:
            # Neither has data → safe fallback
            return (latent_a,)

# Register the node
NODE_CLASS_MAPPINGS = {
    "LatentORGate": LatentORGate
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LatentORGate": "🔀 Latent OR Gate (Auto)"
}