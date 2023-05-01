from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from inworld_python import inworld_chat

app = FastAPI()
security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    This function verifies that the Bearer token included in the HTTP Authorization 
    header of the request matches the expected API key.

    :param credentials: HTTPAuthorizationCredentials object with scheme and credentials
    :return: credentials if verification is successful
    :raises HTTPException: if verification fails
    """
    if credentials.scheme != "Bearer" or credentials.credentials != "YOUR_API_KEY":
        # Raise exception if scheme is not Bearer or credentials do not match expected API key
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return credentials

@app.post("/inworld_chat")
async def inworld_chat_api(query: str, user_name: str, channel_id: str, user_id: str, token: HTTPAuthorizationCredentials = Depends(verify_token)):
    """
    This function is an API endpoint that accepts POST requests to '/inworld_chat'.
    It verifies the Bearer token included in the Authorization header, then 
    initializes an InWorldChat object and uses it to chat.

    :param query: string, message to chat
    :param user_name: string, user name
    :param channel_id: string, channel id
    :param user_id: string, user id
    :param token: HTTPAuthorizationCredentials object, Bearer token for API authorization
    :return: dictionary with 'response' key and chat output as value
    """
    # Create an InWorldChat object with the given key, secret, and scene
    chat_app = inworld_chat.InWorldChat('inworld_key', 'inworld_secret','inworld_scene')
    # Set up the chat
    chat_app.setup()
    # Perform the chat and get the output
    out = chat_app.chat(query, user_name, channel_id, user_id)
    # Return the output
    return {"response": out}
