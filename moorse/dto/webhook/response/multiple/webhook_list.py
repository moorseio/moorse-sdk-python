from dto.webhook.response.multiple.webhook_list_data import WebhookListData
from dto.moorse_error import MoorseError

class WebhookList:

    data: WebhookListData = None
    errors: list[MoorseError] = []

    def __init__(self, data: dict[str, object]):

        if(data == None): return

        self.data = WebhookListData(data.get('data'))
        for error in data.get('errors'):
            self.errors.append(MoorseError(error))