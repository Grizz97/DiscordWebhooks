import requests        #requirement if you don't have this module just open cmd and type (pip install requests)




def main():     
    url = input("Enter Webhook Url : ")           #IMPORTANT!!!  For example = https://discord.com/api/webhooks/webhook_id/webhook_token
    username = input("Enter Webhook username : ")   #The name to display on current message (you can leave this blank if you want)
    picture = input("Enter Webhook Avatar Url : ")  #Update avatar on current webhook message(you can leave this blank as well)
    message = input("Enter the message you want to send : ") #INPORTANT!!!
    data = {"content":message,"username":username,"avatar_url":picture}   #main data to be stored 
    r = requests.post(url,data=data)
    if r.status_code == 204:     #Status Code shown when request was completed.
        print("Message Sent Successfully !")
    else :
        print("Message Not Sent")

main()   #calling the function
