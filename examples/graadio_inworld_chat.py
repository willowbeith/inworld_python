from inworld_python import inworld_chat
import gradio as gr

# Initialize the InWorldChat object
chat_app = inworld_chat.InWorldChat('inworld_key', 'inworld_secret', 'inworld_scene')

# installs the inworld command in the current directory as iw.js
chat_app.setup()

def chat(query: str, user_name: str = "blowhard", channel_id: str = "3232323", user_id: str = "23232323"):
    """
    Function to be used in the Gradio interface.
    It takes the input from the user and sends it to the chat.

    :param query: string, message to chat
    :param user_name: string, user name
    :param channel_id: string, channel id
    :param user_id: string, user id
    :return: string, chat output
    """
    # Send the message to the chat and get the response
    out = chat_app.chat(query, user_name, channel_id, user_id)
    return out

# Define Gradio interface
iface = gr.Interface(fn=chat, 
                     inputs="text", 
                     outputs="text")

# Launch the interface
iface.launch()
