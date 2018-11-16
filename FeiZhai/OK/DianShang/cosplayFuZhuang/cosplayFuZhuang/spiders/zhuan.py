def creacosRead():
    cos = open('cosplay.text')
    for co in cos.readline():
        c = co.replace("\r\n"," ")
        with open('ok.text','a') as ha:
            ha.write(c)

creacosRead()