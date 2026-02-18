import os
from google.cloud import bigquery

project_id = os.environ["GCP_PROJECT_ID"]

client = bigquery.Client(project=project_id)

query = """
SELECT
  CURRENT_DATE() AS today,
  "hello from github" AS msg
"""

job = client.query(query)
rows = job.result()

for row in rows:
    print(dict(row))
