import os
import json
import httpx
import sys

def main():
    try:
        # Load input parameters
        input_json = os.environ.get("INPUT_JSON")
        if not input_json:
            print(json.dumps({"error": "No input parameters provided"}))
            return

        params = json.loads(input_json)
        meeting_id = params.get("meeting_id")
        participant_email = params.get("participant_email")
        
        # Load environment variables
        api_base = os.environ.get("INTERNAL_API_BASE_URL", "").rstrip('/')
        api_token = os.environ.get("INTERNAL_API_TOKEN")

        if not api_base or not api_token:
            print(json.dumps({"error": "Missing required API credentials"}))
            return

        headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }

        # Endpoints to check for comprehensive view
        endpoints = ["z2fw_meeting", "z2fw_zoom_call"]
        combined_results = {}

        with httpx.Client(timeout=30.0) as client:
            for endpoint in endpoints:
                url = f"{api_base}/{endpoint}/transcripts/{meeting_id}"
                query_params = {}
                if participant_email:
                    query_params["email"] = participant_email

                try:
                    response = client.get(url, headers=headers, params=query_params)
                    if response.status_code == 200:
                        combined_results[endpoint] = response.json()
                    elif response.status_code == 404:
                        combined_results[endpoint] = "No transcript found in this source."
                    else:
                        combined_results[endpoint] = f"Error: {response.status_code}"
                except Exception as e:
                    combined_results[endpoint] = f"Request failed: {str(e)}"

        # Print final JSON output
        print(json.dumps({
            "status": "success",
            "meeting_id": meeting_id,
            "sources_checked": endpoints,
            "transcripts": combined_results
        }))

    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    main()