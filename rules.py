# external counts
cant_convert_count = 0
blacklist_count = 0


# ["flagged", "date", "description", "from", "to", "cc", "subject", "content", "time (minutes)"]
def apply_rules(date, sent_from, sent_to, cc, subject, contents, name, email, phone, topic, message_subject, message):
    return [
        "",
        date,
        "",
        ", ".join(sent_from),
        ", ".join(sent_to),
        ", ".join(cc),
        subject,
        contents,
        name,
        email,
        phone,
        topic,
        message_subject,
        message
    ]
