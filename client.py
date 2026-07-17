class NitrosendAgentEmailClient:
    def plan_delivery(self, subject: str, body_markdown: str, recipient: str) -> dict:
        payload = {
            "message_id": f"nitro_{int(time.time())}",
            "to": recipient,
            "subject": subject,
            "body_html": f"<p>{body_markdown}</p>"
        }
        return {"delivered_payload": payload}