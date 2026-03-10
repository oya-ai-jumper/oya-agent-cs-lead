---
name: deals-report-generator
display_name: "Deals Report Generator"
description: "Generates a comprehensive report by performing a left join on deals, contacts, and meeting summaries."
category: productivity
icon: table-properties
skill_type: sandbox
catalog_type: addon
resource_requirements:
  - env_var: RETOOL_API_KEY
    name: Retool API Key
    description: "API Key to access Retool database tables"
  - env_var: RETOOL_BASE_URL
    name: Retool Base URL
    description: "The base URL for the Retool API endpoint"
tool_schema:
  name: generate_deals_report
  description: "Fetches and joins data from jm_fw_all_deals, jm_fw_contacts, and z2fw_meeting_summaries."
  parameters:
    type: object
    properties:
      limit:
        type: integer
        description: "Maximum number of records to return"
        default: 100
    required: []
---
# Deals Report Generator
Performs a left join between deals, contacts, and meeting summaries to provide a complete view of leads and transcripts.