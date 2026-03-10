---
name: deal-owner-lookup
display_name: "Deal Owner Lookup"
description: Fetches deal owner information using specific tables based on the owner role (CSR vs SDR/AE).
category: productivity
icon: users
skill_type: sandbox
catalog_type: addon
resource_requirements:
  - env_var: API_BASE_URL
    name: API Base URL
    description: The base endpoint for the internal data service
  - env_var: API_KEY
    name: API Key
    description: Authorization token for the data service
tool_schema:
  name: get_deal_owner_info
  description: Retrieves deal owner details from jm_fw_contacts for CSRs or jm_fw_all_deals for SDR/AEs.
  parameters:
    type: object
    properties:
      deal_id:
        type: string
        description: "The unique identifier for the deal."
      role_type:
        type: string
        enum: [csr, sdr_ae]
        description: "The role of the owner to look up."
    required: [deal_id, role_type]
---
# Deal Owner Lookup
Fetches deal owner information using specific tables based on the owner role (CSR vs SDR/AE).