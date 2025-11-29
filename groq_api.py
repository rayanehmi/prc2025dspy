# Above doesn't work with groq so let's use groq sdk instead
import requests
from groq import Groq
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
file_path = os.path.join(OUTPUT_DIR, "batches", "1.jsonl")
file_handler = client.files.create(file=open(file_path, "rb"), purpose="batch")
file_handler

response = client.batches.create(
    completion_window="24h",
    endpoint="/v1/chat/completions",
    input_file_id=file_handler.id,
)
print(response.to_json())
check = client.batches.retrieve(response.id)
print(check.to_json())
path = os.path.join(OUTPUT_DIR, "batches_responses")
os.makedirs(path, exist_ok=True)
response = client.files.content(check.output_file_id)
response.write_to_file(os.path.join(path, "1.jsonl"))
print("Batch file saved to batch_results.jsonl")

response[0]