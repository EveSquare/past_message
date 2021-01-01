from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

line_bot_api = LineBotApi("PydKcB4ohoGs3rq3aCj53UYhHUA7Qam1UwnMnkRQdDXsqByYOokMIIXXkYAKJTji5pf7T2LFj+8299innh1yVgNo7uGwi8WnrwaMxUMVeuWoxhBjDvY9uNbeGfhoCwNa6bo8+L1fVSnT73e2nMA3gwdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("ec4b4f750316feb4d1984a52cb8d3f37")

line_bot_api.multicast(['Ud04d8ad9c4a2070d410d4b913422da5f'], TextSendMessage(text='Hello World!'))