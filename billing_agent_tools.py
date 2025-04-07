# billing_agent_tools.py

import os
import json
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up the database engine
NEON_DB_URL = os.getenv("NEON_DB_CONNECTION_STRING")
db_engine = create_engine(NEON_DB_URL)


# Define the billing anomaly detection function
def billing_anomaly_summary(
    tenant_id: str,
    start_date: str = "2025-03-27",
    end_date: str = "2025-04-01",
    limit: int = 10,
) -> str:
    """
    Fetches recent usage data for a SaaS tenant and detects potential billing anomalies.

    :param tenant_id: The tenant ID to analyze.
    :type tenant_id: str
    :param start_date: Start date for the usage window.
    :type start_date: str
    :param end_date: End date for the usage window.
    :type end_date: str
    :param limit: Maximum number of records to return.
    :type limit: int
    :return: A JSON string with usage records and anomaly flags.
    :rtype: str
    """
    query = """
        SELECT date, api_calls, storage_gb
        FROM usage_data
        WHERE tenant_id = %s AND date BETWEEN %s AND %s
        ORDER BY date DESC
        LIMIT %s;
    """

    df = pd.read_sql(query, db_engine, params=(tenant_id, start_date, end_date, limit))

    if df.empty:
        return json.dumps(
            {"message": "No usage data found for this tenant in the specified range."}
        )

    df.sort_values("date", inplace=True)
    df["pct_change_api"] = df["api_calls"].pct_change()
    df["anomaly"] = df["pct_change_api"].abs() > 1.5

    return df.to_json(orient="records")


# Register this in a list to be used by FunctionTool
user_functions = [billing_anomaly_summary]
