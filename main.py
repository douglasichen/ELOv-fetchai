import os
from uagents_core.utils.registration import (
    register_chat_agent,
    RegistrationRequestCredentials,
)
import dotenv
dotenv.load_dotenv()

register_chat_agent(
    "role-agent",
    "https://kqarhesayyvtbakgpaqr.supabase.co/functions/v1/role-agent",
    active=True,
    credentials=RegistrationRequestCredentials(
        agentverse_api_key=os.environ["AGENTVERSE_KEY"],
        agent_seed_phrase=os.environ["AGENT_SEED_PHRASE"],        
    ),
)