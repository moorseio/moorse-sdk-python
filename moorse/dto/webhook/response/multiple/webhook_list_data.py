from dto.webhook.response.multiple.webhook_list_element import WebhookListElement

class WebhookListData:

    content: list[WebhookListElement] = []

    def __init__(self, data: list[dict[str, object]]):

        if(data == None): return

        for webhoookData in data.get('content'):
            self.content.append(
                WebhookListElement(webhoookData)
            )