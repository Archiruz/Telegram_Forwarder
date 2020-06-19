from auto_forwarder.sample_config import Config


class Development(Config):
    API_KEY = "1155370524:AAEFB-Ntg33e8KNbz40cKQZjvzIeTt3rQFo"  # Your bot API key
    OWNER_ID = 888449576  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    FROM_CHATS = [-1001234567890]  # List of chat id's to forward messages from.
    TO_CHATS = [-1001453770633]  # List of chat id's to forward messages to.
    
    WORKERS = 4
