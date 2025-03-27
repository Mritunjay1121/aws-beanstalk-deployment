import gradio as gr

# Define a simple function
def say_hello():
    return "Hello from Gradio!"

# Create the Gradio interface
demo = gr.Interface(
    fn=say_hello,       # The function to execute
    inputs=None,        # No inputs required
    outputs="text",     # Output will be text
    title="Simple Hello App",
    description="A basic Gradio app that says Hello!dfsfs"
)

# Create the WSGI app for Gunicorn
app = demo.app  # Gradio's underlying Flask app

if __name__ == "__main__":
    # For local testing
    demo.launch(
        server_name="127.0.0.1",
        server_port=8080,
        debug=True
    )