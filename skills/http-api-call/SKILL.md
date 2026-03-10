---
name: http-api-call
display_name: "HTTP API Call"
description: "Make an HTTP request (GET/POST/PUT/DELETE) with headers and body"
category: communication
icon: terminal
skill_type: sandbox
catalog_type: addon
config_schema:
  properties:
    default_url:
      type: string
      label: "Default Base URL"
      description: "Base URL to prepend to relative paths"
      placeholder: "https://api.example.com/v1"
      group: defaults
    default_headers:
      type: text
      label: "Default Headers"
      description: "JSON headers to include in all requests"
      placeholder: '{"Authorization": "Bearer xxx", "Content-Type": "application/json"}'
      group: defaults
    default_method:
      type: select
      label: "Default Method"
      description: "HTTP method when not specified"
      options: ["GET", "POST", "PUT", "PATCH", "DELETE"]
      default: "GET"
      group: defaults
tool_schema:
  name: http_api_call
  description: "Make an HTTP request with custom method, headers, and body"
  parameters:
    type: object
    properties:
      url:
        type: "string"
        description: "Request URL"
      method:
        type: "string"
        description: "HTTP method"
        default: "GET"
        enum: ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'HEAD']
      body_json:
        type: "string"
        description: "JSON body"
        default: ""
      headers_json:
        type: "string"
        description: "Headers as JSON"
        default: "{}"
    required: [url]
---
# HTTP API Call
Make an HTTP request (GET/POST/PUT/DELETE) with headers and body
