import gradio as gr
from sorter import bubble_sort
from ui import BubbleSortVisualizer
import time

# Creates a visualizer object to hold the steps and draw frames
visualizer = BubbleSortVisualizer()

def start_sort(input_text):
    # Attempts to parse the input text into integers
    try:
        input_list = [x.strip() for x in input_text.split(",") if x.strip()]
        arr = [int(x) for x in input_list]
    except:
        # Prompts user to enter a valid input
        return None, "Error: Please enter integers separated by commas."

    # Limits size so bubbles don't overlap
    if len(arr) > 15:
        return None, "Error: Too many numbers. Please try 15 or fewer."

    # Generates all visualization steps using bubble sort
    steps = bubble_sort(arr)

    # Loads steps into visualizer
    visualizer.load_steps(steps)

    # Draws the initial frame 
    first_frame = visualizer.draw_frame(0)

    return first_frame, "Press play to start!" 

def toggle_play(current_label, speed_value):
    # If currently playing
    if current_label == "Play":

        # If animation previously ended resume 
        if visualizer.index >= len(visualizer.steps) - 1:
            pass

        # Allow autoplay to continue
        visualizer.pause_flag = False
        visualizer.last_step_time = time.time()

        # Converts speed value into timing interval
        visualizer.step_interval = 1.0 / float(speed_value)

        return "Pause", gr.Timer(active=True)

    else:
        # Pauses the animation
        visualizer.pause_flag = True
        return "Play", gr.Timer(active=False)

def advance(speed_value):
    # Stops if paused
    if visualizer.pause_flag:
        return gr.Timer(active=False), gr.skip(), gr.skip(), "Play", speed_value

    # Stops if already at the last frame
    if visualizer.index >= len(visualizer.steps) - 1:
        return gr.Timer(active=False), gr.skip(), "Finished!", "Play", speed_value

    # Checks if enough time has passed for the next frame (playback speed)
    current_time = time.time()
    required_delay = 1.0 / max(0.1, float(speed_value))

    # If not enough time has passed, skips updating
    if current_time - visualizer.last_step_time < required_delay:
        return gr.Timer(active=True), gr.skip(), gr.skip(), gr.skip(), speed_value

    # Moves to next frame
    visualizer.last_step_time = current_time
    img, status = visualizer.next_frame()

    # Resets play button when finished
    btn_update = gr.skip()
    if status == "Finished!":
        btn_update = "Play"

    return gr.Timer(active=True), img, status, btn_update, speed_value

def random_array():
    # Generates a random 8 element list
    import random
    arr = [random.randint(1, 99) for _ in range(8)]
    return ",".join(str(x) for x in arr)

def clear_input():
    # Clears the textbox
    return ""

# UI layout
with gr.Blocks(title="Bubble Sort Visualizer") as demo:

    gr.Markdown("<h1 style='text-align:center;'>Bubble Sort Visualizer</h1>")

    # Input area (textbox and buttons)
    with gr.Column(scale=1):
        input_box = gr.Textbox(
            label="Enter numbers (comma separated)",
            value="5, 1, 4, 2, 8"
        )

        # Row of input buttons
        with gr.Row():
            clear_btn = gr.Button("Clear Input")
            random_btn = gr.Button("Random")
            start_btn = gr.Button("Load / Reset", variant="primary")

    # Output image (where bubbles will be drawn)
    image_output = gr.Image(
        width=600,
        height=300,
        interactive=False,
        show_label=False
    )

    # Status message 
    status = gr.Textbox(
        label="Status",
        value="Waiting...",
        interactive=False
    )

    # Playback controls: Play/pause, playback speed slider
    with gr.Row():
        toggle_btn = gr.Button("Play", variant="secondary")
        speed_slider = gr.Slider(
            minimum=0.5,
            maximum=5.0,
            value=1.0,
            step=0.1,
            label="Playback Speed (x)"
        )

    # Timer drives the animation loop
    timer = gr.Timer(value=0.05, active=False)

    # Maps buttons to functions
    start_btn.click(start_sort, inputs=input_box, outputs=[image_output, status])
    clear_btn.click(clear_input, outputs=input_box)
    random_btn.click(random_array, outputs=input_box)

    # Play/pause button 
    toggle_btn.click(
        toggle_play,
        inputs=[toggle_btn, speed_slider],
        outputs=[toggle_btn, timer]
    )

    timer.tick(
        advance,
        inputs=[speed_slider],
        outputs=[timer, image_output, status, toggle_btn, speed_slider]
    )

demo.launch()
