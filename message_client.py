class MessageClient:
    def send_post(url: str, data: dict) -> None:
        print(f"POST sent to {url}. Data: {data}")
