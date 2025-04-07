# billing_anomaly_agent.py

import os
from datetime import datetime
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import FunctionTool, ToolSet
from dotenv import load_dotenv
from pprint import pprint
from billing_agent_tools import user_functions  # Custom tool function module

# Load environment variables from .env file
load_dotenv()

# Create an Azure AI Project Client
project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize toolset with our user-defined functions
functions = FunctionTool(user_functions)
toolset = ToolSet()
toolset.add(functions)

# Create the agent
agent = project_client.agents.create_agent(
    model=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    name=f"billing-anomaly-agent-{datetime.now().strftime('%Y%m%d%H%M')}",
    description="Billing Anomaly Detection Agent",
    instructions=f"""
    You are a helpful SaaS financial assistant that retrieves and explains billing anomalies using usage data.
    The current date is {datetime.now().strftime("%Y-%m-%d")}.
    """,
    toolset=toolset,
)
print(f"Created agent, ID: {agent.id}")

# Create a communication thread
thread = project_client.agents.create_thread()
print(f"Created thread, ID: {thread.id}")

# Post a message to the agent thread
message = project_client.agents.create_message(
    thread_id=thread.id,
    role="user",
    content="Why did my billing spike for tenant_456 this week?",
)
print(f"Created message, ID: {message.id}")

# Run the agent and process the query
run = project_client.agents.create_and_process_run(
    thread_id=thread.id, agent_id=agent.id
)
print(f"Run finished with status: {run.status}")

if run.status == "failed":
    print(f"Run failed: {run.last_error}")

# Fetch and display the messages
messages = project_client.agents.list_messages(thread_id=thread.id)
print("Messages:")
pprint(messages["data"][0]["content"][0]["text"]["value"])

# Optional cleanup:
# project_client.agents.delete_agent(agent.id)
# print("Deleted agent")
