import os
from dotenv import load_dotenv
from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    String,
    Date,
    Integer,
    Numeric,
)

# Load environment variables from .env
load_dotenv()

# Load connection string from environment variable
NEON_DB_URL = os.getenv("NEON_DB_CONNECTION_STRING")
engine = create_engine(NEON_DB_URL)

# Define metadata and table schema
metadata = MetaData()

usage_data = Table(
    "usage_data",
    metadata,
    Column("tenant_id", String, primary_key=True),
    Column("date", Date, primary_key=True),
    Column("api_calls", Integer),
    Column("storage_gb", Numeric),
)

# Create table
with engine.begin() as conn:
    metadata.create_all(conn)

    # Insert mock data
    conn.execute(
        usage_data.insert(),
        [
            {
                "tenant_id": "tenant_456",
                "date": "2025-03-27",
                "api_calls": 870,
                "storage_gb": 23.9,
            },
            {
                "tenant_id": "tenant_456",
                "date": "2025-03-28",
                "api_calls": 880,
                "storage_gb": 24.0,
            },
            {
                "tenant_id": "tenant_456",
                "date": "2025-03-29",
                "api_calls": 900,
                "storage_gb": 24.5,
            },
            {
                "tenant_id": "tenant_456",
                "date": "2025-03-30",
                "api_calls": 2200,
                "storage_gb": 26.0,
            },
            {
                "tenant_id": "tenant_456",
                "date": "2025-03-31",
                "api_calls": 950,
                "storage_gb": 24.8,
            },
            {
                "tenant_id": "tenant_456",
                "date": "2025-04-01",
                "api_calls": 1000,
                "storage_gb": 25.0,
            },
        ],
    )

print("✅ usage_data table created and mock data inserted.")
