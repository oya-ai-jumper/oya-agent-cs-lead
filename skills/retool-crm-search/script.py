import os
import json
import httpx

def run():
    try:
        # Load inputs
        input_data = json.loads(os.environ.get("INPUT_JSON", "{}"))
        query = input_data.get("query")
        search_type = input_data.get("search_type", "both")
        
        api_key = os.environ.get("RETOOL_API_KEY")
        base_url = os.environ.get("RETOOL_BASE_URL", "").rstrip("/")
        
        if not api_key or not base_url:
            print(json.dumps({"error": "Missing Retool credentials or URL"}))
            return

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        results = {
            "deals": [],
            "contacts": []
        }

        # Function to query specific tables
        def query_table(table_name):
            # Retool Database API usually uses REST endpoints for tables
            url = f"{base_url}/resources/db/tables/{table_name}/records"
            # Note: Specific filtering syntax depends on Retool setup; 
            # common approach is query params or body for search.
            params = {"search": query}
            response = httpx.get(url, headers=headers, params=params, timeout=10.0)
            if response.status_code == 200:
                return response.json().get("data", [])
            return []

        # Priority Search
        if search_type in ["deals", "both"]:
            results["deals"] = query_table("jm_fw_all_deals")
            
        if search_type in ["contacts", "both"]:
            results["contacts"] = query_table("jm_fw_contacts")

        # Combine results
        output = {
            "query": query,
            "source_priority": ["jm_fw_all_deals", "jm_fw_contacts"],
            "results": results
        }
        
        print(json.dumps(output))

    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    run()