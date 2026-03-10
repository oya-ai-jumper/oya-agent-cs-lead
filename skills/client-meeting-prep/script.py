import os
import json
import httpx
from datetime import datetime

def run():
    try:
        # Load input parameters
        input_data = json.loads(os.environ.get("INPUT_JSON", "{}"))
        client_name = input_data.get("client_name")
        client_id = input_data.get("client_id")

        # Load credentials
        xano_url = os.environ.get("XANO_BASE_URL", "").rstrip('/')
        xano_key = os.environ.get("XANO_API_KEY")
        retool_key = os.environ.get("RETOOL_API_KEY")

        if not xano_url or not xano_key:
            print(json.dumps({"error": "Missing required API credentials for Xano."}))
            return

        headers = {
            "Authorization": f"Bearer {xano_key}",
            "Content-Type": "application/json"
        }

        # 1. Fetch Client Data and Communication History from Xano
        # Assuming endpoints for communication (transcripts/emails) and rankings
        search_params = {"client_name": client_name}
        if client_id:
            search_params["client_id"] = client_id

        # Fetch communications
        comm_resp = httpx.get(f"{xano_url}/communications", params=search_params, headers=headers, timeout=30.0)
        comm_data = comm_resp.json() if comm_resp.status_code == 200 else []

        # Fetch notes and rankings
        rank_resp = httpx.get(f"{xano_url}/client_stats", params=search_params, headers=headers, timeout=30.0)
        rank_data = rank_resp.json() if rank_resp.status_code == 200 else {}

        if not comm_data and not rank_data:
            print(json.dumps({"message": f"No data available for client '{client_name}' in the database. Cannot generate briefing."}))
            return

        # 2. Process Data (Aggregation logic)
        briefing = {
            "client_name": client_name,
            "concerns": [],
            "expectations": [],
            "recommendations_last_call": [],
            "talking_points": [],
            "things_to_remember": [],
            "current_rankings": rank_data.get("rankings", "No ranking data available"),
            "data_sources": ["Xano", "Retool Integrations"]
        }

        # Simple parsing of communication logs
        for entry in comm_data:
            content = entry.get("content", "").lower()
            entry_type = entry.get("type", "note") # transcript, email, text
            
            # Extract concerns/expectations
            if "concern" in content or "issue" in content or "worried" in content:
                briefing["concerns"].append(f"({entry_type}) {entry.get('content')}")
            
            if "expect" in content or "goal" in content or "want" in content:
                briefing["expectations"].append(entry.get("content"))

            # Extract personal details (Things to remember)
            personal_keywords = ["kid", "tournament", "travel", "vacation", "flight", "reschedule", "family"]
            if any(key in content for key in personal_keywords):
                briefing["things_to_remember"].append(entry.get("content"))

            # Extract recommendations
            if "recommend" in content or "suggest" in content or "next steps" in content:
                briefing["recommendations_last_call"].append(entry.get("content"))

        # 3. Generate Talking Points based on logic
        if briefing["concerns"]:
            briefing["talking_points"].append(f"Address previous concerns regarding: {briefing['concerns'][0][:50]}...")
        if briefing["recommendations_last_call"]:
            briefing["talking_points"].append("Follow up on recommendations provided in the last interaction.")
        
        # Deduplicate and clean up
        briefing["concerns"] = list(set(briefing["concerns"]))[:5]
        briefing["things_to_remember"] = list(set(briefing["things_to_remember"]))[:5]

        print(json.dumps(briefing))

    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    run()