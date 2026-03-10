---
name: fetch-comprehensive-transcripts
display_name: "Comprehensive Transcript Fetcher"
description: Retrieves and merges transcripts from both z2fw_meeting and z2fw_zoom_call for a complete communication history.
category: communication
icon: message-square
skill_type: sandbox
catalog_type: addon
resource_requirements:
  - env_var: RETOOL_Internal_URL
    name: API Base URL
    description: The base URL for the internal communication services
  - env_var: RETOOL_API_TOKEN
    name: API Token
    description: Bearer token for authentication
tool_schema:
  name: get_comprehensive_transcripts
  description: Fetches communication logs from both z2fw_meeting and z2fw_zoom_call endpoints to provide a full transcript view.
  parameters:
    type: object
    properties:
      meeting_id:
        type: string
        description: The unique identifier for the meeting or call session.
      participant_email:
        type: string
        description: Optional email to filter transcripts for a specific person.
    required:
      - meeting_id
---
# Comprehensive Transcript Fetcher
Retrieves and merges transcripts from both z2fw_meeting and z2fw_zoom_call for a complete communication history.