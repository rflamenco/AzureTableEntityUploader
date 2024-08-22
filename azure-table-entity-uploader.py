import os
from azure.data.tables import TableServiceClient

# Access the environment variable
connection_string = os.getenv('AZURE_TABLE_CONN_STR_DEV')

# Ensure the connection string is available
if connection_string is None:
    raise ValueError("The Azure Table Storage connection string is not set in environment variables")

# Connect to Azure Table Storage
table_service = TableServiceClient.from_connection_string(conn_str=connection_string)

# Table must already exist; replace with your table name
table_name = "yourtablename"
table_client = table_service.get_table_client(table_name=table_name)

# Example entities; add more as needed
entities = [
    {"PartitionKey": "pk_value", "RowKey": "rk_value", "PropertyName1": "PropertyName1_value", "PropertyName2": "PropertyName2_value"}]

# Convert all values to strings
for entity in entities:
    for key in entity:
        entity[key] = str(entity[key])

# Add each entity to the table
for entity in entities:
    table_client.create_entity(entity=entity)
