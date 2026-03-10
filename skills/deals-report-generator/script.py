import os
import json
import httpx

def run():
    try:
        # Load input parameters
        input_data = json.loads(os.environ.get("INPUT_JSON", "{}"))
        limit = input_data.get("limit", 100)
        
        # Load credentials
        api_key = os.environ.get("RETOOL_API_KEY")
        base_url = os.environ.get("RETOOL_BASE_URL", "").rstrip("/")
        
        if not api_key or not base_url:
            print(json.dumps({"error": "Missing required credentials (RETOOL_API_KEY or RETOOL_BASE_URL)"}))
            return

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        # In a real Retool environment, we would typically query a specific resource or use a workflow.
        # Since these are described as Retool tables, we simulate fetching the datasets to perform the LEFT JOIN locally.
        
        # 1. Fetch Deals (Primary Table)
        deals_resp = httpx.get(f"{base_url}/tables/jm_fw_all_deals", headers=headers, timeout=30.0)
        deals_resp.raise_for_status()
        deals = deals_resp.json()[:limit]

        # 2. Fetch Contacts
        contacts_resp = httpx.get(f"{base_url}/tables/jm_fw_contacts", headers=headers, timeout=30.0)
        contacts_resp.raise_for_status()
        contacts = {str(c['id']): c for c in contacts_resp.json()}

        # 3. Fetch Meeting Summaries
        summaries_resp = httpx.get(f"{base_url}/tables/z2fw_meeting_summaries", headers=headers, timeout=30.0)
        summaries_resp.raise_for_status()
        # Mapping by deal_id for the join
        summaries = {}
        for s in summaries_resp.json():
            summaries[str(s.get('deal_id'))] = s

        # Perform Left Join
        report = []
        for deal in deals:
            deal_id = str(deal.get('id'))
            contact_id = str(deal.get('contact_id'))
            
            # Merge Contact Data
            contact_info = contacts.get(contact_id, {})
            deal['phone'] = contact_info.get('phone', 'N/A')
            deal['address'] = contact_info.get('address', 'N/A')
            
            # Merge Summary/Transcript Data
            summary_info = summaries.get(deal_id, {})
            deal['transcript'] = summary_info.get('transcript', 'No transcript available')
            deal['meeting_notes'] = summary_info.get('notes', 'N/A')
            
            report.append(deal)

        print(json.dumps({"success": True, "data": report}))

    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    run()