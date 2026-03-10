import os
import json
import httpx

try:
    token = os.environ["NOTION_API_KEY"]
    inp = json.loads(os.environ.get("INPUT_JSON", "{}"))
    query = inp.get("query", "")
    limit = inp.get("limit", 10)

    headers = {"Authorization": f"Bearer {token}", "Notion-Version": "2022-06-28", "Content-Type": "application/json"}

    with httpx.Client(timeout=15) as c:
        r = c.post("https://api.notion.com/v1/search", headers=headers, json={"query": query, "page_size": limit})
        r.raise_for_status()
        data = r.json()

    results = [{"id": p.get("id"), "type": p.get("object"), "title": next((t.get("plain_text", "") for prop in p.get("properties", {}).values() if prop.get("type") == "title" for t in prop.get("title", [])), "")} for p in data.get("results", [])]

    print(json.dumps({"results": results}, indent=2))
except Exception as e:
    print(json.dumps({"error": str(e)}))