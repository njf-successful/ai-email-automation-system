import json


def summarize_email(sender, body):
    body_lower = body.lower()
    sender_name = sender.split("@")[0].replace(".", " ").title()

    if "financial report" in body_lower and "thursday" in body_lower:
        return f"{sender_name} is requesting the updated financial report by Thursday."

    if "confirm" in body_lower and "meeting" in body_lower:
        return f"{sender_name} is asking for confirmation of tomorrow's meeting time."

    if "send over" in body_lower or "need" in body_lower or "please" in body_lower:
        return f"{sender_name} sent a request that likely needs follow-up."

    return f"{sender_name} sent an email that should be reviewed."


def classify_email(body):
    body_lower = body.lower()

    if "financial report" in body_lower:
        return {
            "category": "Request",
            "priority": "Medium",
            "tone": "Neutral",
            "response_required": "Yes",
            "action_required": "Yes",
        }

    if "meeting" in body_lower and "confirm" in body_lower:
        return {
            "category": "Meeting Coordination",
            "priority": "Medium",
            "tone": "Neutral",
            "response_required": "Yes",
            "action_required": "Yes",
        }

    if "urgent" in body_lower or "asap" in body_lower:
        return {
            "category": "Urgent Request",
            "priority": "High",
            "tone": "Urgent",
            "response_required": "Yes",
            "action_required": "Yes",
        }

    return {
        "category": "General",
        "priority": "Low",
        "tone": "Neutral",
        "response_required": "No",
        "action_required": "No",
    }


def extract_tasks(body):
    body_lower = body.lower()
    tasks = []

    if "financial report" in body_lower:
        tasks.append("Send updated financial report")

    if "thursday" in body_lower:
        tasks.append("Complete by Thursday")

    if "confirm" in body_lower and "meeting" in body_lower:
        tasks.append("Confirm tomorrow's meeting time")

    if "review" in body_lower:
        tasks.append("Review requested material")

    return tasks


def draft_reply(sender, body):
    body_lower = body.lower()
    sender_name = sender.split("@")[0].replace(".", " ").title()

    if "financial report" in body_lower:
        return (
            f"Hi {sender_name},\n\n"
            "Thanks for your email. I will send the updated financial report by Thursday.\n\n"
            "Best,\n"
            "Nia"
        )

    if "confirm" in body_lower and "meeting" in body_lower:
        return (
            f"Hi {sender_name},\n\n"
            "Thanks for reaching out. Confirming tomorrow's meeting time as scheduled.\n\n"
            "Best,\n"
            "Nia"
        )

    if "urgent" in body_lower or "asap" in body_lower:
        return (
            f"Hi {sender_name},\n\n"
            "Thanks for flagging this. I’m reviewing it now and will follow up as soon as possible.\n\n"
            "Best,\n"
            "Nia"
        )

    return (
        f"Hi {sender_name},\n\n"
        "Thanks for your email. I’ll review this and follow up shortly.\n\n"
        "Best,\n"
        "Nia"
    )


def load_emails():
    with open("sample_data/emails.json", "r") as f:
        return json.load(f)


def process_emails():
    emails = load_emails()

    print("AI Email Automation System Prototype")

    for email in emails:
        sender = email["sender"]
        subject = email["subject"]
        body = email["body"]

        summary = summarize_email(sender, body)
        classification = classify_email(body)
        tasks = extract_tasks(body)
        reply = draft_reply(sender, body)

        print("\n--------------")
        print(f"Sender: {sender}")
        print(f"Subject: {subject}\n")

        print("Summary:")
        print(summary)

        print("\nClassification:")
        print(f"Category: {classification['category']}")
        print(f"Priority: {classification['priority']}")
        print(f"Tone: {classification['tone']}")
        print(f"Response Required: {classification['response_required']}")
        print(f"Action Required: {classification['action_required']}")

        print("\nExtracted Tasks:")
        if tasks:
            for task in tasks:
                print(f"- {task}")
        else:
            print("- No tasks found")

        print("\nDraft Reply:")
        print(reply)


if __name__ == "__main__":
    process_emails()
