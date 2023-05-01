from inworld_python import inworld_chat
import gradio as gr

# Initialize the InWorldChat object
chat_app = inworld_chat.InWorldChat('inworld_key', 'inworld_secret', 'inworld_scene')

def chat(query, user_name, channel_id, user_id):
    # Set up the app
    chat_app.setup()
    
    # Perform the chat
    out = chat_app.chat(query, user_name, channel_id, user_id)
    
    return out

iface = gr.Interface(fn=chat, 
                     inputs=[gr.inputs.Textbox(lines=2, placeholder="Enter query here..."), 
                             gr.inputs.Textbox(lines=1, placeholder="Enter user name here..."), 
                             gr.inputs.Textbox(lines=1, placeholder="Enter channel ID here..."), 
                             gr.inputs.Textbox(lines=1, placeholder="Enter user ID here...")], 
                     outputs=gr.outputs.Textbox())

# Launch the interface on your local network
iface.launch(share=True)
