# Slack connection

## Supported actions

Currently, we support the following functionalities from Slack API inside SlackConnection/AsyncSlackConnection classes
1. [channel_conversation_history](slack_connection.py) - Get channel conversion history for given channel
2. [get_channel_latest_message](slack_connection.py) - Fetch latest message from specific channel
3. [send_text_message](slack_connection.py) - Send text type message to specific channel
4. [send_scheduled_text_message](slack_connection.py) - Schedule text message send for specific time
5. [send_file_message](slack_connection.py) - Send file to channel


> [!IMPORTANT]
> All the above functionalities are available for sync as well async flows under [AsyncSlackConnection](slack_connection.py) class.

## Example
```python
# Initialize Slack connection
slack_connection = SlackConnection(access_token="your_slack_access_token", channel_id="your_channel_id")

# Get conversation history
status, messages = slack_connection.channel_conversation_history()
print(status, messages)

# Get the latest message
status, latest_message = slack_connection.get_channel_latest_message()
print(status, latest_message)

# Send a text message
send_status = slack_connection.send_text_message(msg="Hello, Slack!")
print(send_status)

# Schedule a text message
schedule_status = slack_connection.send_scheduled_text_message(msg="Scheduled message", timestamp=future_timestamp)
print(schedule_status)

# Send a file
file_upload_status = slack_connection.send_file_message(file_path="path/to/file.txt", title="File Title", msg="File Message")
print(file_upload_status)

```
## Requirements
```shell
"slack_sdk==3.22.0"
"aiohttp==3.8.5"
```