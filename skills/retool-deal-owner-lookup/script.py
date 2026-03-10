import os
import json
import httpx
import sys

def main():
    try:
        # Load input parameters
        input_data = json.loads(os.environ.get("INPUT_JSON", "{}"))
        deal_id = input_data.get("deal_id")
        custom_field_key = input_data.get("custom_field_key", "owner_id")

        # Credentials
        api_key = os.environ.get("RETOOL_API_KEY")
        base_url = os.environ.get("RETOOL_BASE_URL", "").rstrip("/")

        if not api_key or not base_url:
            print(json.dumps({"error": "Missing Retool credentials (RETOOL_API_KEY or RETOOL_BASE_URL)"}))
            return

        if not deal_id:
            print(json.dumps({"error": "deal_id is required"}))
            return

        # Prepare headers
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        # Step 1: Fetch Deal Data
        # Assuming Retool REST API patterns where deal data contains custom owner field references
        deal_url = f"{base_url}/deals/{deal_id}"
        
        with httpx.Client(timeout=30.0) as client:
            response = client.get(deal_url, headers=headers)
            
            if response.status_code != 200:
                print(json.dumps({"error": f"Retool API error: {response.status_code} - {response.text}"}))
                return
            
            deal_data = response.json()
            
            # Identify the owner ID from the custom field
            owner_id = deal_data.get(custom_field_key)
            
            if not owner_id:
                print(json.dumps({
                    "success": False,
                    "message": f"Custom field '{custom_field_key}' not found or empty for deal {deal_id}",
                    "deal_data": deal_data
                }))
                return

            # Step 2: Fetch Owner Details (User data)
            user_url = f"{base_url}/users/{owner_id}"
            user_response = client.get(user_url, headers=headers)
            
            owner_info = user_response.json() if user_response.status_code == 200 else {"id": owner_id, "status": "details_not_found"}

            # Return consolidated result
            result = {
                "success": True,
                "deal_id": deal_id,
                "custom_field_used": custom_field_key,
                "owner_data": owner_info,
                "raw_deal_reference": deal_data
            }
            print(json.dumps(result))

    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    main()