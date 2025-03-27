import gradio as gr

# Define a simple function
def say_hello():
    return "Hello from Gradio!"

# Create the Gradio interface
# demo = gr.Interface(
#     fn=say_hello,       # The function to execute
#     inputs=None,        # No inputs required
#     outputs="text",     # Output will be text
#     title="Simple Hello App",
#     description="A basic Gradio app that says Hello!"
# )


gr.Interface(
    fn=say_hello,       # The function to execute
    inputs=None,        # No inputs required
    outputs="text",     # Output will be text
    title="Simple Hello App",
    description="A basic Gradio app that says Hello!",
    server_name="0.0.0.0"
).launch()
# Launch the app
# if __name__ == "__main__":
#     demo.launch(
#         server_name="0.0.0.0",  # Localhost
#         server_port=8000,        # Default Gradio port (changed from 8080 to avoid conflicts)
#         debug=True               # Enable debug mode for troubleshooting
#     )