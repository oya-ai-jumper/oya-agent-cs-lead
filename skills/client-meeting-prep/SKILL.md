---
name: client-meeting-prep
display_name: "Client Meeting Prep"
description: Analyzes transcripts, emails, and notes from Retool and Xano to provide a comprehensive briefing for client calls.
category: productivity
icon: briefcase
skill_type: sandbox
catalog_type: addon
resource_requirements:
  - env_var: XANO_BASE_URL
    name: Xano Base URL
    description: The base URL for the Xano API.
  - env_var: XANO_API_KEY
    name: Xano API Key
    description: API Key to authenticate with Xano.
  - env_var: RETOOL_API_KEY
    name: Retool API Key
    description: API Key to fetch client data from Retool.
tool_schema:
  name: prepare_client_briefing
  description: Fetches and analyzes communication history, notes, and rankings for a specific client to prepare the user for a meeting.
  parameters:
    type: object
    properties:
      client_name:
        type: string
        description: The name of the client to prepare for.
      client_id:
        type: string
        description: The internal ID of the client if known.
    required:
      - client_name
---
# Client Meeting Prep
Prepares a detailed briefing including concerns, expectations, recommendations, talking points, and personal notes for upcoming client calls.