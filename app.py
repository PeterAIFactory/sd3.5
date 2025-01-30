from sd3_infer import main


# Or specify more parameters
generated_image = main(
    prompt="A cat with a hat, flying in the sky",
    model="models/sd3.5_large_turbo.safetensors",
    seed=42,
    width=1024,
    height=1024,
    steps=30,
    cfg=4.5,
    # lora_file="loras/LoRA_Llama3.3_70b_natural-regenerate-rank64-13440.safetensors",
    # lora_alpha=0.6
)