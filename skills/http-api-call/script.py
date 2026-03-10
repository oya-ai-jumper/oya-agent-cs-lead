import os
import json
import httpx

try:
    inp = json.loads(os.environ.get("INPUT_JSON", "{}"))
    url = inp.get("url", "")
    method = inp.get("method", "GET").upper()
    body = inp.get("body_json", "")
    extra_headers = json.loads(inp.get("headers_json", "{}"))

    headers = {"Content-Type": "application/json"}
    headers.update(extra_headers)

    kwargs = {"headers": headers, "timeout": 15}
    if body and method in ("POST", "PUT", "PATCH"):
        kwargs["json"] = json.loads(body)

    with httpx.Client(follow_redirects=True) as c:
        r = c.request(method, url, **kwargs)

    try:
        resp_json = r.json()
    except Exception:
        resp_json = None

    print(json.dumps({"status": r.status_code, "body": resp_json if resp_json else r.text[:2000]}))
except Exception as e:
    print(json.dumps({"error": str(e)}))