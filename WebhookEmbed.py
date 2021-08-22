import requests



def Webhook():
    url = input("Enter Webhook Url : ")
    username = input("Enter Webhook username : ")                  
    picture = input("Enter Webhook Avatar Url : ")                   
    message = input("Enter the message you want to send : ")   
    data = {
        "username":username,
        "avatar_url": picture,
        "content":message,
        "allowed_mentions":{
            "parse": ["users","roles"]
        },
        "embeds":[{
            "author" : {
                "name" : "Sensei.exe#7309",
                "url" : "https://media.tenor.com/images/4fd49de4149a6d348e04f2465a3970af/tenor.gif",
                "icon_url" : "https://media.tenor.com/images/4fd49de4149a6d348e04f2465a3970af/tenor.gif"},
            "fields" : [
                {
                "name" : "1st Field name",
                "value" : "1st Field value",
                "inline" : True
                },
                {
                 "name" : "2nd Field name",
                 "value" : "2nd Field value",
                 "inline" : True   
                }],
            "title" : "This is a test Title",
            "url" : "https://media.tenor.com/images/4fd49de4149a6d348e04f2465a3970af/tenor.gif",
            "description" : "This is the description of embed",
            "timestamp": "2021-08-21T12:00:00.000Z",
            "color" : 0x00fefe,
            "thumbnail" : {"url" : "https://media.tenor.com/images/4fd49de4149a6d348e04f2465a3970af/tenor.gif"},
            "image" : {"url":"https://media.tenor.com/images/4fd49de4149a6d348e04f2465a3970af/tenor.gif"},
            "footer" : {
                "text":"Nice Footer",
                "icon_url":"https://media.tenor.com/images/4fd49de4149a6d348e04f2465a3970af/tenor.gif"
                }}]}
    r = requests.post(url,json=data)
    if r.status_code == 204:                                
        print("Message Sent Successfully 👌")
    else :
        print("Message Not Sent")


        

    
Webhook()
