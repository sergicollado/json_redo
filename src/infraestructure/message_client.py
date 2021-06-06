from domain.message_client_abstract import MessageClientAbstract


class MessageClient(MessageClientAbstract):
    def send_post(url: str, data: dict) -> None:
        print(f"SMS sent to {url}. Data: {data}")
    
    def send_sms(phone: str, data: dict) -> None:
        print(f"SMS sent to {phone}. Data: {data}")

    def send_email(email: str, data: dict) -> None:
        print(f"SMS sent to {email}. Data: {data}")