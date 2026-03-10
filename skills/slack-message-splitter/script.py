import os
import json
import re

def split_text(text, limit=4000):
    if len(text) <= limit:
        return [text]

    chunks = []
    current_pos = 0
    
    while current_pos < len(text):
        if len(text) - current_pos <= limit:
            chunks.append(text[current_pos:])
            break
            
        # Define the end of the potential chunk
        chunk_end = current_pos + limit
        
        # Look for the last newline within the limit to avoid cutting lists or sentences
        last_newline = text.rfind('\n', current_pos, chunk_end)
        
        if last_newline != -1 and last_newline > current_pos:
            # Split at the newline
            split_at = last_newline
        else:
            # If no newline, look for the last space
            last_space = text.rfind(' ', current_pos, chunk_end)
            if last_space != -1 and last_space > current_pos:
                split_at = last_space
            else:
                # Force split at limit if no whitespace found
                split_at = chunk_end
        
        chunks.append(text[current_pos:split_at].strip())
        current_pos = split_at + 1 if text[split_at:split_at+1] == '\n' or text[split_at:split_at+1] == ' ' else split_at

    return chunks

def main():
    try:
        input_data = os.environ.get("INPUT_JSON")
        if not input_data:
            print(json.dumps({"error": "No input provided"}))
            return

        params = json.loads(input_data)
        text = params.get("text", "")

        if not text:
            print(json.dumps({"messages": []}))
            return

        # Slack character limit is technically 4000, but we use a safety margin
        messages = split_text(text, limit=3900)
        
        print(json.dumps({
            "messages": messages,
            "count": len(messages)
        }))

    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    main()