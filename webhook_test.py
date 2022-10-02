import requests #dependency

url = "https://discord.com/api/webhooks/898946596086087733/sAM6GsAHDfASjqzB39PONOTwZZnxid2dHC4CkIhfA-G8g5xN6fmsrvMJzzr3MaawEYaf" #webhook url, from here: https://i.imgur.com/f9XnAew.png

#for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
data = {
    "content" : "This is a test.",
    "username" : "Webhook Test"
}

#leave this out if you dont want an embed
#for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
data["embeds"] = [
    {
        "description" : "embed test",
        "title" : "embed title",
        "type" : "video",
        "url" : "https://www.youtube.com/watch?v=R7vxXfy09EA",
        "height" : "100",
        "width" : "200"
    }
]

result = requests.post(url, json = data)

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("Payload delivered successfully, code {}.".format(result.status_code))

#result: https://i.imgur.com/DRqXQzA.png