import gradio as gr

def placeholder(x):
    return f"You entered: {x}"

demo = gr.Interface(fn=placeholder, inputs="text", outputs="text")

if __name__ == "__main__":
    demo.launch()
