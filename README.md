# DiscordWebhooks
A simple Discord Webhook message/embed maker using python
</br>
</br>
* If you've got a knack for JSON application-building or HTTP POST requests and want to customize your own webhooks, you can dig up some more information in discord's [`developer docs`](https://discord.com/developers/docs/resources/webhook).
* 
* Please use this with care as webhooks are capable of doing the @everyone,@here and all role ping even **ON LOOP** until you control it with 
  * `allowed_mentions` <br/>
  *  `users`, `roles` , `everyone`
  *  Do not share the webhook url with anyone
* Adding a for/while loop in the main function will result in spamming.  <br/>
* You can enter custom emotes by their id for example : [**`<:vSuccess:845197262309425192>`**](https://discord.com/developers/docs/resources/emoji)
* Beautify your messages with [**`discord markdowns`**](https://support.discord.com/hc/en-us/articles/210298617-Markdown-Text-101-Chat-Formatting-Bold-Italic-Underline-).
* We can also use embeds in webhooks , check the [**`WebhookEmbed.py`**](https://github.com/SenseiQt07/DiscordWebhooks/blob/main/WebhookEmbed.py) file in this repository.
* Webhooks can use animated emotes from the same server as the webhook itself but they can't have an animated profile picture.
* All of them have 0000 discriminator.
* Thats all i guess...
* A simple webhook message can be send like this as shown below : 
```py
import requests

url = "Your Webhook url here"
message = "Your message here"
data = {"content":message}
r = requests.post(url,data=data)
```


[Click here to know More](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)<br/>
[Click to see all resources](https://discord.com/developers/docs/resources/webhook)

![alt text](https://hackaday.com/wp-content/uploads/2018/02/discord-python-webhooks-featured.jpg?w=800)
