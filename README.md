# AI Agent for Postgres using Azure AI Agent Service

This project demonstrates how to build an AI agent that can analyze SaaS usage data stored in a Neon Serverless Postgres database and explain billing anomalies in natural language using Azure AI Agent Service.

## ✨ Why this project?
- No need for complex frameworks like LangChain, Semantic Kernel, or AutoGen
- Leverages Azure AI Foundry's built-in agent orchestration
- Connects to a real Postgres backend (Neon) to fetch and analyze data
- Beginner-friendly setup with clear steps

## 🧠 Use Case
Imagine you run a SaaS platform and want to:
- Spot billing spikes (e.g., sudden API call increases)
- Ask natural questions like: *"Why did my bill go up this week?"*
- Get AI-powered insights directly from your usage database

## 📦 Project Structure
```
.
├── billing_anomaly_agent.py         # Main script to run the agent
├── billing_agent_tools.py           # Tool functions used by the agent
├── init_usage_data.py               # Optional: Populate sample data in Neon
├── requirements.txt                 # Python dependencies
├── .env                             # Environment variables (not committed)
└── README.md                        # This file
```

## ✅ Prerequisites

- An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services).
- Make sure you have the **Azure AI Developer** [RBAC role](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/rbac-azure-ai-foundry) assigned
- Install [Python 3.11.x](https://www.python.org/downloads/).

## ⚙️ Setup Instructions

### 1. Clone the repo and install dependencies
```bash
git clone https://github.com/your-org/billing-anomaly-agent.git
cd billing-anomaly-agent
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate for Windows
pip install -r requirements.txt
```

### 2. Create the .env file

```env
PROJECT_CONNECTION_STRING="<Your AI Foundry connection string>"
AZURE_OPENAI_DEPLOYMENT_NAME=""
NEON_DB_CONNECTION_STRING="<Your Neon connection string>"
```

### 3. Load sample data into Neon
```bash
python init_usage_data.py
```

### 4. Run the agent
```bash
python billing_anomaly_agent.py
```

## 🧪 Test Your Agent in the Playground
1. Go to [Azure AI Foundry](https://ai.azure.com/) → **Agents**
2. Select your billing agent
3. Use the playground to ask:
   - "Why did tenant_456 have a spike in API usage?"
   - "What happened with storage for tenant_789 last week?"

## 🧼 Cleanup (Optional)
Delete the agent from your script or the Azure portal after testing:
```python
project_client.agents.delete_agent(agent.id)
```

## 📚 Resources
- [Azure AI Agents Documentation](https://learn.microsoft.com/en-us/azure/ai-services/agents/overview)
- [Neon Serverless Postgres](https://neon.tech)

---

Made with ❤️ using Python, Azure AI, and Neon.

