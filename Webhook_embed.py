import requests




def main():     
    url = input("Enter Webhook Url : ")                         #For example = https://discord.com/api/webhooks/webhook_id/webhook_token
    username = input("Enter Webhook username : ")               #can leave this empty    
    picture = input("Enter Webhook Avatar Url : ")              #can leave this empty      
    message = input("Enter the message you want to send : ")     
    data = {"content":message,
            "username":username,
            "avatar_url":picture,
            "embeds":[
                {
                    "author":{"name":"Sensei.Qt",
                    "url":"https://media.tenor.com/images/4fd49de4149a6d348e04f2465a3970af/tenor.gif",
                    "icon_url":"https://cdn.discordapp.com/attachments/798172513799634975/846278305019592794/Screenshot_20210524-014736.jpg"
                    },
                    "title":"This is a test Title",
                    "url":"https://github.com/SenseiQt07/DiscordWebhooks/edit/main/Webhook_embed.py",
                    "description":"**This is a Test Description**",
                    "color":0x00fefe,
                    "thumbnail":{"url":"https://cdn.discordapp.com/attachments/798172513799634975/846278241778139146/Screenshot_20210524-014627.jpg"},
                    "image":{"url":"https://cdn.discordapp.com/attachments/798172513799634975/845576908769984522/Screenshot_20210522-005526.jpg"},
                    "footer":{"text":"Nice Footer","icon_url":"https://cdn.discordapp.com/attachments/798172513799634975/845576908988743680/Screenshot_20210522-005358.jpg"}
                }
            ]}
    r = requests.post(url,json=data)
    if r.status_code == 204:                                
        print("Message Sent Successfully !")
    else :
        print("Message Not Sent")

        
        
        
main()   #calling the function
#also please see the Embed_Readme.md file as it explains the concept in detail. 
