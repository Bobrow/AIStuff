from google.cloud import bigquery
client = bigquery.Client(project='bigquery-public-data')
ethereum_classic_dataset_ref = client.dataset('crypto_ethereum_classic', project='bigquery-public-data')
query = """
WITH mined_block AS (
  SELECT miner, DATE(timestamp)
  FROM `bigquery-public-data.crypto_ethereum_classic.blocks` 
  WHERE DATE(timestamp) > DATE_SUB(CURRENT_DATE(), INTERVAL 1 MONTH)
  ORDER BY miner ASC)
SELECT miner, COUNT(miner) AS total_block_reward 
FROM mined_block 
GROUP BY miner 
ORDER BY total_block_reward DESC
LIMIT 10
"""

query_job = client.query(query)
iterator = query_job.result()

