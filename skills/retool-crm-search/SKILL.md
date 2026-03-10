---
name: retool-crm-search
display_name: "Retool CRM Search"
description: Queries deal and contact data from Retool with priority on specific tables.
category: productivity
icon: database
skill_type: sandbox
catalog_type: addon
resource_requirements:
  - env_var: RETOOL_API_KEY
    name: Retool API Key
    description: API Key for Retool Database access
  - env_var: RETOOL_BASE_URL
    name: Retool Base URL
    description: The base URL for the Retool API (e.g., https://yourdomain.retool.com/api/v1)
tool_schema:
  name: retool_crm_search
  description: Searches for deal and client information prioritizing jm_fw_all_deals and jm_fw_contacts tables.
  parameters:
    type: object
    properties:
      query:
        type: string
        description: The search term or name to look for in the CRM tables.
      search_type:
        type: string
        enum: [deals, contacts, both]
        description: Filter to search specifically for deals, contacts, or both.
    required: [query]
---
# Retool CRM Search
Prioritize "jm_fw_all_deals" and "jm_fw_contacts" tables from Retool for deal and client data.