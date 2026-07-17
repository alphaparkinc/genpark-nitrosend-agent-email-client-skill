from client import NitrosendAgentEmailClient
import time
client = NitrosendAgentEmailClient()
print(client.plan_delivery("Hello", "This is a **markdown** message.", "user@domain.com"))