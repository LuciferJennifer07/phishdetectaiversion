import imaplib
import email
from email.header import decode_header

def fetch_emails(imap_host, user, password, n=5):
    mail = imaplib.IMAP4_SSL(imap_host)
    mail.login(user, password)
    mail.select("inbox")

    _, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()[-n:]

    emails = []
    for eid in reversed(email_ids):
        _, msg = mail.fetch(eid, "(RFC822)")
        msg = email.message_from_bytes(msg[0][1])

        subject, enc = decode_header(msg["Subject"])[0]
        subject = subject.decode(enc or "utf-8", errors="ignore") if isinstance(subject, bytes) else subject

        sender = msg.get("From")
        body = ""

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode(errors="ignore")
                    break
        else:
            body = msg.get_payload(decode=True).decode(errors="ignore")

        emails.append({"from": sender, "subject": subject, "body": body})

    mail.logout()
    return emails
