# CS Lead

> Built with [Oya AI](https://oya.ai)

## About

You are the Jumper Media Customer Service Team Manager, an expert on all internal company processes, knowledge bases, and client management workflows. You provide clear, authoritative, and helpful guidance to team members by referencing official policies and Notion documentation. You answer any and all questions regarding specific clients from Retool Database. All client data is connected by client email. Your goal is to ensure consistency across the support team and help members navigate complex client scenarios efficiently.

Tone: Clear, concise, action-oriented. Use bullet points for updates.

Constraints: 
- Never make up data or links, always provide accurate information from the provided sources. If information done by web search, specify that it is coming from web search
- Data accuracy is at most important. never make up data, if you don't know where to find information - let user know 
- Never delete anything without confirming
- Before sending emails, always send preview and wait for user approval to send it 
- When creating documents make sure permissions are set so that anybod with the link can view it 
- When creating meetings always add video conferencing 
- When user ask to analyze transcript or/and data from transcripts/past client interactions make sure you analyze both metting transcipts and transcripts summary, call transcripts and call summaries, email exchnage, notes 



  To get information about  clients performance on  jumper local dashboard, you should always get that information from Xano database. The client unique identifier its gmbs_id or a name although some clients have multiple locations under same bussiness name, so gmbs_id is the only reliable identifier for such clients.  user can also ask you to generate gmb & website report. You can do that, but you need the user to provide you gmbs_id. To generate new report, all you need is to call this agent curl -X POST "https://oya.ai/api/triggers/3d0274e1-f8c3-4e45-a12a-6df67c03014a/webhook" \
  -H "Content-Type: application/json" \
  -H "x-trigger-secret: M94CcOmbu8LWJ39x-BpZmRjb-y8YPuYG" \
  -d '{"gmbs_id":"398"}' ; once gmbs Id is provided let user know that generating report might take 1-3 min and you will provide link to report when report is ready. Here is how you can check its status # Poll status (repeat until status is "done" or "failed")
curl -s "https://oya.ai/api/agent-run-jobs/{job_id}/status" \
  -H "x-trigger-secret: M94CcOmbu8LWJ39x-BpZmRjb-y8YPuYG"

# Get result (when status is done or failed)
curl -s "https://oya.ai/api/agent-run-jobs/{job_id}/result" \
  -H "x-trigger-secret: M94CcOmbu8LWJ39x-BpZmRjb-y8YPuYG"




## Configuration

- **Mode:** skills
- **Agent ID:** `fb4a33bb-0a0d-4ece-98ad-8cacb0965ab8`
- **Model:** `gemini/gemini-3-pro-preview`

## Usage

Every deployed agent exposes an **OpenAI-compatible API endpoint**. Use any SDK or HTTP client that supports the OpenAI chat completions format.

### Authentication

Pass your API key via either header:
- `Authorization: Bearer a2a_your_key_here`
- `X-API-Key: a2a_your_key_here`

Create API keys at [https://oya.ai/api-keys](https://oya.ai/api-keys).

### Endpoint

```
https://oya.ai/api/v1/chat/completions
```

### cURL

```bash
curl -X POST https://oya.ai/api/v1/chat/completions \
  -H "Authorization: Bearer a2a_your_key_here" \
  -H "Content-Type: application/json" \
  -d '{"model":"gemini/gemini-3-pro-preview","messages":[{"role":"user","content":"Hello"}]}'

# Continue a conversation using thread_id from the first response:
curl -X POST https://oya.ai/api/v1/chat/completions \
  -H "Authorization: Bearer a2a_your_key_here" \
  -H "Content-Type: application/json" \
  -d '{"model":"gemini/gemini-3-pro-preview","messages":[{"role":"user","content":"Follow up"}],"thread_id":"THREAD_ID"}'
```

### Python

```python
from openai import OpenAI

client = OpenAI(
    api_key="a2a_your_key_here",
    base_url="https://oya.ai/api/v1",
)

# First message — starts a new thread
response = client.chat.completions.create(
    model="gemini/gemini-3-pro-preview",
    messages=[{"role": "user", "content": "Hello"}],
)
print(response.choices[0].message.content)

# Continue the conversation using thread_id
thread_id = response.thread_id
response = client.chat.completions.create(
    model="gemini/gemini-3-pro-preview",
    messages=[{"role": "user", "content": "Follow up question"}],
    extra_body={"thread_id": thread_id},
)
print(response.choices[0].message.content)
```

### TypeScript

```typescript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "a2a_your_key_here",
  baseURL: "https://oya.ai/api/v1",
});

// First message — starts a new thread
const response = await client.chat.completions.create({
  model: "gemini/gemini-3-pro-preview",
  messages: [{ role: "user", content: "Hello" }],
});
console.log(response.choices[0].message.content);

// Continue the conversation using thread_id
const threadId = (response as any).thread_id;
const followUp = await client.chat.completions.create({
  model: "gemini/gemini-3-pro-preview",
  messages: [{ role: "user", content: "Follow up question" }],
  // @ts-ignore — custom field
  thread_id: threadId,
});
console.log(followUp.choices[0].message.content);
```

### Swift

```swift
// Package.swift:
// .package(url: "https://github.com/MacPaw/OpenAI.git", from: "0.4.0")
import Foundation
import OpenAI

@main
struct Main {
    static func main() async throws {
        let config = OpenAI.Configuration(
            token: "a2a_your_key_here",
            host: "oya.ai",
            scheme: "https"
        )
        let client = OpenAI(configuration: config)

        let query = ChatQuery(
            messages: [.user(.init(content: .string("Hello")))],
            model: "gemini/gemini-3-pro-preview"
        )
        let result = try await withCheckedThrowingContinuation { continuation in
            _ = client.chats(query: query) { continuation.resume(with: $0) }
        }
        print(result.choices.first?.message.content ?? "")
    }
}
```

### Kotlin

```kotlin
// build.gradle.kts dependencies:
// implementation("com.aallam.openai:openai-client:4.0.1")
// implementation("io.ktor:ktor-client-cio:3.0.0")
import com.aallam.openai.api.chat.ChatCompletionRequest
import com.aallam.openai.api.chat.ChatMessage
import com.aallam.openai.api.chat.ChatRole
import com.aallam.openai.api.model.ModelId
import com.aallam.openai.client.OpenAI
import com.aallam.openai.client.OpenAIHost
import kotlinx.coroutines.runBlocking

fun main() = runBlocking {
    val openai = OpenAI(
        token = "a2a_your_key_here",
        host = OpenAIHost(baseUrl = "https://oya.ai/api/v1/")
    )
    val completion = openai.chatCompletion(
        ChatCompletionRequest(
            model = ModelId("gemini/gemini-3-pro-preview"),
            messages = listOf(ChatMessage(role = ChatRole.User, content = "Hello"))
        )
    )
    println(completion.choices.first().message.messageContent)
}
```

### Streaming

```python
stream = client.chat.completions.create(
    model="gemini/gemini-3-pro-preview",
    messages=[{"role": "user", "content": "Tell me about AI agents"}],
    stream=True,
)
for chunk in stream:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
```

### Embeddable Widget

```html
<!-- Oya Chat Widget -->
<script
  src="https://oya.ai/widget.js"
  data-agent-id="fb4a33bb-0a0d-4ece-98ad-8cacb0965ab8"
  data-api-key="a2a_your_key_here"
  data-title="CS Lead"
></script>
```

### Supported Models

- `gemini/gemini-2.0-flash`
- `gemini/gemini-2.5-flash`
- `gemini/gemini-2.5-pro`
- `gemini/gemini-3-flash-preview`
- `gemini/gemini-3-pro-preview`

---

*Managed by [Oya AI](https://oya.ai). Do not edit manually — changes are overwritten on each sync.*