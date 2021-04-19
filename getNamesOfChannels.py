import requests as req
channels = [
    'https://www.youtube.com/channel/UCuwTHYdMavwEPsZ6OAkXfig',
    'https://www.youtube.com/channel/UCzve9ZBBT6_Nt_3j-qHyheQ',
    'https://www.youtube.com/channel/UCisfYJLiVP11BT-JY36sYAQ',
    'https://www.youtube.com/channel/UCVBG0RjyjzPKSXalwKNVFLQ',
    'https://www.youtube.com/channel/UCSNkfKl4cU-55Nm-ovsvOHQ',
    'https://www.youtube.com/channel/UCvZ0AZ0hUI_-xJalc3CXa6Q',
    'https://www.youtube.com/channel/UCoGokpe1nmjavku9voRvTmQ',
    'https://www.youtube.com/channel/UCKc3ji2XrPk6cOi97qdT3Jg',
    'https://www.youtube.com/channel/UCJaNoxBopnEOli2mI7PTlgg',
    'https://www.youtube.com/channel/UC4Y8dVfo_-aydzENDmE7wTw',
    'https://www.youtube.com/channel/UC4dhc6pe4Xb9Ww8TvBl9asg',
    'https://www.youtube.com/channel/UC4Yf0L-AWUIMnf1Kp3TqwSw',
    'https://www.youtube.com/channel/UCEGxeopnf36A-G8KPiZ2YFg',
    'https://www.youtube.com/channel/UCtYna3IBYYuB_tiCI7ZnFXw',
    'https://www.youtube.com/channel/UCJ_Y4Zl1w5jv5okzL2O3CyQ',
    'https://www.youtube.com/channel/UCveX_0uBOHVHbpV838OGXVA',
    'https://www.youtube.com/channel/UC_1FLItzEctoZGFkyVUY2YA',
    'https://www.youtube.com/channel/UCdsl5KATIPh9dThQM09PAdg',
    'https://www.youtube.com/c/UniqueCoderzAcademy?app=desktop',
    'https://www.youtube.com/channel/UChCMIwQrelEqLZT7Lt1L5Og',
    'https://www.youtube.com/channel/UChjh0djRQtOfzS9fWGXTt9g',
    'https://www.youtube.com/channel/UCFBuqAGEoQep87-oz27yjfQ',
    'https://www.youtube.com/channel/UCZtMEPGln_sbgd9_ioDDC9g',
    'https://www.youtube.com/channel/UCg554MAfjzG0jOp5vuAgdKg',
    'https://www.youtube.com/channel/UCi9DV7ai7a8-XgRt5iH9d7Q',
    'https://www.youtube.com/channel/UC8OxKsmAyrGAfBiluhpLkbA',
    'https://www.youtube.com/channel/UCPqlXXn7rfa6ZqsIIaF6bQw',
    'https://www.youtube.com/channel/UC24ELGatjbtDGivcd1pyeoA',
    'https://www.youtube.com/channel/UCjf3LbqewN1eVP6ybCMGOCQ',
    'https://www.youtube.com/channel/UCOpR7Tg8CVUdgZCUbQlKY-g',
    'https://www.youtube.com/channel/UCmgpWswPRFzIEEcZncyQLYw',
    'https://www.youtube.com/channel/UCLcFW31aAxyqsDxtALNnVTw',
    'https://www.youtube.com/channel/UC7OGxluGpaD5NHMNoKj33pw',
    'https://www.youtube.com/channel/UC06FVVN-__PTi8XHTx13ekA',
    'https://www.youtube.com/channel/UCCRdEITKZuY5A_WJiUZji8g',
    'https://www.youtube.com/channel/UCrKr6aiLvFxj1csAUfekiuw',
]
file = open("Arabic Youtube Tech.md", "a")
file.truncate(0)
for channel in channels:
    resp = req.get(channel)
    allText = resp.text
    title = allText[allText.find('<title>') +
                    len('<title>'): allText.find('</title>')].encode('utf-8').strip()
    file.write("["+title.replace(' - YouTube', '')+"]("+channel+")  ")
    file.write("\n")

file.close()
