---
name: slack-message-splitter
display_name: "Slack Message Splitter"
description: Splits long text into chunks that fit within Slack's 4000 character limit without cutting mid-sentence or mid-item.
category: communication
icon: scissors
skill_type: sandbox
catalog_type: addon
resource_requirements: []
tool_schema:
  name: split_slack_message
  description: Takes a long string and splits it into an array of strings, each under the 4000 character Slack limit.
  parameters:
    type: object
    properties:
      text:
        type: string
        description: The full message text to be split.
    required:
      - text
---
# Slack Message Splitter
Splits long text into chunks that fit within Slack's 4000 character limit without cutting mid-sentence or mid-item.