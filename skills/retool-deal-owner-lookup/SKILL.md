---
name: retool-deal-owner-lookup
display_name: "Retool Deal Owner Lookup"
description: Fetches deal owner information from Retool using custom owner fields mapping.
category: productivity
icon: user-check
skill_type: sandbox
catalog_type: addon
resource_requirements:
  - env_var: RETOOL_API_KEY
    name: Retool API Key
    description: API Key for authenticating with Retool
  - env_var: RETOOL_BASE_URL
    name: Retool Base URL
    description: The base URL for your Retool instance/resource API
tool_schema:
  name: get_deal_owner_custom
  description: Retrieves owner data for a specific deal including custom owner field mappings.
  parameters:
    type: object
    properties:
      deal_id:
        type: string
        description: The unique identifier for the deal.
      custom_field_key:
        type: string
        description: The specific custom owner field key to look up (e.g., 'technical_owner_id').
    required:
      - deal_id
---
# Retool Deal Owner Lookup
Fetches deal owner information from Retool using custom owner fields mapping.