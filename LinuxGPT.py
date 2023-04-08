import openai
import os
#Get it from https://platform.openai.com/account/api-keys
openai.api_key = "Your api key"
model_engine = "text-davinci-003"
max_tokens = 500

while True: 
    messageK=[]
    message=input(">")
    messageS=message.split()

    # for messageM in messageS:
    #     messageK.append(messageM)
    # if "flatpak" or "flathub" or "флатпак" in messageK:
    # #if message == "flatpak" or message ==  "flathub" or message == "флатпак":
    #     print(messageK)
    #     prompt=( "You are linuxGPT Your work help me with my pc  Write bash code for this prompt"+'" '+(message)+ '"' +"For system Linux Manjaro kde  prime  Write only  code do not explain how it work do not take any inoformation if  коментарі в коді пиши україньською  and update flutpak or install something from flathub, flatpak, kde ")
    #     print("flatpak mode active ")
    # else:
    slovo = "flatpak"
    code="N"
    slovo4="python"
    for stroka in message.split(' '):
        if stroka == slovo4:
            code="PY"
            break
    slovo1="parameters"
    for stroka in message.split(' '):
        if stroka == slovo1:
            code="P"
            break
    slovo2="sudo"
    for stroka in message.split(' '):
        if stroka == slovo2:
            code="SUDO"
            break
    slovo3="судо"
    for stroka in message.split(' '):
        if stroka == slovo3:
            code="SUDO"
            break
    for stroka in message.split(' '):
        if stroka == slovo:
            code="F"
            break
    slovo0 = "флатпак"

    for stroka in message.split(' '):
        if stroka == slovo0:
            code="F"
            break
    if code=="N":
        prompt=( "You are linuxGPT Your work help me with my pc  Write bash code for this prompt"+'" '+(message)+ '"' +"For system Linux Manjaro kde  prime  Write only  code do not explain how it work do not take any   inoformation if  коментарі в коді пиши україньською   ")
    elif code=="F":
        print("flatpak mode active")
        prompt=( "You are linuxGPT Your work help me with my pc  Write bash code for this prompt"+'" '+(message)+ '"' +"For system Linux Manjaro kde  prime  Write only  code do not explain how it work do not take any inoformation if  коментарі в коді пиши україньською  and update flutpak or install something from flathub, flatpak, kde and use command flatpak update ")
    elif code=="P":
        print("System param method active")
        prompt=( "You are linuxGPT Your work help me with my pc  Write bash code for this prompt"+'" '+(message)+ '"' +"For system Linux Manjaro kde  write parameters of my system like memory or CPU, GPU  Write only  code do not explain how it work do not take any   inoformation if  коментарі в коді пиши україньською prioritize methods from git hub redit and other forums   ")
    elif code=="SUDO":
        print("ATTENTION sudo mode active")
        prompt=( "Attantion sudo mode  is on You are linuxGPT Your work help me with my pc  Write bash code for this prompt"+'" '+(message)+ '"' +"For system Linux Manjaro kde be careful and run you script as sudo  Write only  code do not explain how it work do not take any      inoformation if  коментарі в коді пиши україньською")
    elif code=="PY":
        print("PY Mode")
        prompt=( " You are linuxGPT Your work help me with my pc  Write python  code for this prompt"+'" '+(message)+ '"' +"For system Linux Manjaro kde   Write only  python code code do not explain how it work do not take any   inoformation if  коментарі в коді пиши україньською save it in document using bash code ")
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        
        presence_penalty=0
        )
    print(completion.choices[0].text) 
    os.system(completion.choices[0].text)
    
