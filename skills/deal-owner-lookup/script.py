import os
import json
import httpx
import sys

def main():
    try:
        # Load inputs
        input_json = os.environ.get("INPUT_JSON")
        if not input_json:
            print(json.dumps({"error": "No INPUT_JSON provided"}))
            return

        args = json.loads(input_json)
        deal_id = args.get("deal_id")
        role_type = args.get("role_type")
        
        # Credentials
        api_url = os.environ.get("API_BASE_URL", "").rstrip("/")
        api_key = os.environ.get("API_KEY")

        if not api_url or not api_key:
            print(json.dumps({"error": "Missing API credentials"}))
            return

        # Map role to table
        # CSR -> jm_fw_contacts
        # SDR/AE -> jm_fw_all_deals
        table_name = "jm_fw_contacts" if role_type == "csr" else "jm_fw_all_deals"

        # Construct request
        endpoint = f"{api_url}/query"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        # Payload assuming a standard query interface for the specific tables
        payload = {
            "table": table_name,
            "filters": {
                "deal_id": deal_id
            }
        }

        with httpx.Client(timeout=30.0) as client:
            response = client.post(endpoint, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()

        result = {
            "deal_id": deal_id,
            "role_type": role_type,
            "source_table": table_name,
            "owner_data": data
        }
        
        print(json.dumps(result))

    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    main()