from PIL import Image, ImageDraw

class BubbleSortVisualizer:
    def __init__(self):
        # All recorded steps for one sort run
        self.steps = []
        # Current step index
        self.index = 0
        # Whether animation is paused
        self.pause_flag = False
        # Time spacing between frames (Playback speed slider)
        self.step_interval = 1.0
        # Time when last frame was shown
        self.last_step_time = 0.0

    def load_steps(self, steps):
        # Resets everything and load new steps
        self.steps = steps
        self.index = 0
        self.pause_flag = False

    def draw_frame(self, idx):
        # If no steps loaded, returns blank image
        if not self.steps:
            return Image.new("RGB", (600, 300), (200, 200, 200))

        # Clamp index
        if idx >= len(self.steps):
            idx = len(self.steps) - 1

        step = self.steps[idx]
        arr = step["array"]

        # Creates the image canvas
        W, H = 600, 300
        img = Image.new("RGB", (W, H), (120, 160, 240))  # blue background
        draw = ImageDraw.Draw(img)

        # Layout calculations for bubble spacing
        count = len(arr)
        if count == 0:
            return img

        spacing = W // (count + 1)
        r = min(28, (spacing // 2) - 2)
        y = H // 2

        # Draws each bubble
        for k, value in enumerate(arr):
            x = spacing * (k + 1)

            # Default bubble appearance
            fill_color = (80, 140, 255)
            outline_color = (255, 255, 255)

            # Comparison bubble appearance (orange highlight)
            if step["type"] == "compare" and (k == step.get("i") or k == step.get("j")):
                fill_color = (255, 150, 80)

            # Swap bubble appearance (green highlight)
            if step["type"] == "swap" and (k == step.get("i") or k == step.get("j")):
                fill_color = (120, 255, 120)

            # Final sorted state bubble appearance (green highlight)
            if step["type"] == "done":
                fill_color = (100, 200, 100)

            # Draws main bubble circle
            draw.ellipse((x - r, y - r, x + r, y + r), fill=fill_color, outline=outline_color)

            # Shadow for 3d effect 
            shadow = (max(fill_color[0]-50,0), max(fill_color[1]-50,0), max(fill_color[2]-50,0))
            draw.arc((x - r + 2, y - r + 2, x + r - 2, y + r - 2),
                     start=0, end=90, fill=shadow, width=2)

            # Glare highlight 
            glare_size = r // 2.5
            glare_offset = r // 2
            gx = x - glare_offset
            gy = y - glare_offset
            draw.ellipse((gx, gy, gx + glare_size, gy + glare_size), fill=(255, 255, 255, 180))

            # Draws centered number inside bubble
            draw.text((x, y), str(value), fill="black", anchor="mm")

        return img

    def next_frame(self):
        # Displays nothing if no steps loaded
        if not self.steps:
            return None, "No data."

        # End of animation
        if self.index >= len(self.steps) - 1:
            img = self.draw_frame(self.index)
            return img, "Finished!"

        # Move forward
        self.index += 1

        # Draw next frame
        img = self.draw_frame(self.index)
        step_type = self.steps[self.index]["type"]

        # Status text
        if step_type == "compare":
            status = "Comparing..."
        elif step_type == "swap":
            status = "Swapping..."
        elif step_type == "init":
            status = "Ready."
        elif step_type == "done":
            status = "Finished!"
        else:
            status = "Running..."

        return img, status
