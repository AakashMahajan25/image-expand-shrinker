from PIL import Image

# Load your image
img = Image.open("timeline-mobile-new.png")\

expand_shrink_factor = 1.5

# Define new size (e.g., 1.5x larger)
new_width = int(img.width * expand_shrink_factor)
new_height = int(img.height * expand_shrink_factor)

# Create a transparent background
new_img = Image.new("RGBA", (new_width, new_height), (0, 0, 0, 0))

# Paste the original image in the center
x = (new_width - img.width) // 2
y = (new_height - img.height) // 2
new_img.paste(img, (x, y))

# Save result
new_img.save("expanded_image.png")
