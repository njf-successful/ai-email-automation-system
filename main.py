print("AI Email Automation System Prototype")

emails = [
    {
        "sender": "john@company.com",
        "subject": "Updated report request",
        "body": "Can you send the updated financial report by Thursday?"
    },
    {
        "sender": "sarah@client.com",
        "subject": "Meeting confirmation",
        "body": "Please confirm tomorrow's meeting time."
    }
]

for email in emails:

    print("\n--------------")
    print("Sender:", email["sender"])
    print("Subject:", email["subject"])

    print("Summary:")
    print("Email requires review and possible response.")

    print("Task Extracted:")
    print("Follow up on request.")
