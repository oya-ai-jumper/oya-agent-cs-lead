---
name: notion-search
display_name: "Notion Search"
description: "Search across Notion workspace by query"
category: productivity
icon: search
skill_type: sandbox
catalog_type: addon
resource_requirements:
  - env_var: NOTION_API_KEY
    name: "Notion API Key"
    description: "Notion integration token"
config_schema:
  properties:
    default_database:
      type: string
      label: "Default Database ID"
      description: "Limit search to a specific database"
      placeholder: "abc123def456..."
      group: defaults
tool_schema:
  name: notion_search
  description: "Search across Notion workspace"
  parameters:
    type: object
    properties:
      query:
        type: "string"
        description: "Search query"
      limit:
        type: "integer"
        description: "Max results"
        default: 10
    required: [query]
---
# Notion Search
Search across Notion workspace by query
