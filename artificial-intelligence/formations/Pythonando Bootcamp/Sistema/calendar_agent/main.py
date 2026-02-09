"""
Agente Google Calendar (tutorial Notion - Agente Google Calendar).
Expõe API FastAPI para assistente de agendamento usando Agno + Google Calendar.
"""

import datetime
from pathlib import Path

from dotenv import load_dotenv

# .env na pasta pai (Bloco 2)
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.os import AgentOS
from agno.tools.googlecalendar import GoogleCalendarTools
from tzlocal import get_localzone_name

from credentials_google import get_credentials_path

credentials_path = get_credentials_path()

agent = Agent(
    model=OpenAIChat(id="gpt-4.1-mini"),
    tools=[
        GoogleCalendarTools(
            credentials_path=str(credentials_path),
            allow_update=True,
        )
    ],
    instructions=[
        f"""
You are a scheduling assistant. Today is {datetime.datetime.now()} and the user's timezone is {get_localzone_name()}.
You should help users to perform these actions in their Google calendar:
- get their scheduled events from a certain date and time
- create events based on provided details
"""
    ],
    add_datetime_to_context=True,
)

agent_os = AgentOS(agents=[agent])
app = agent_os.get_app()
