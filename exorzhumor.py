import random

urlExorz=["https://media.discordapp.net/attachments/310547686896173056/666047680174358548/image0.jpg?width=702&height=702",
    "https://cdn.discordapp.com/attachments/310547686896173056/666047167424888891/image0.jpg",
    "https://cdn.discordapp.com/attachments/310547686896173056/666047112118796288/unknown.png",
    "https://cdn.discordapp.com/attachments/310547686896173056/666047067595997204/unknown.png",
    "https://cdn.discordapp.com/attachments/310547686896173056/666047013070307329/unknown.png",
    "https://cdn.discordapp.com/attachments/310547686896173056/666047009735704578/original-19982-1446133182-3.png",
    "https://cdn.discordapp.com/attachments/310547686896173056/666046965011841034/unknown.png",
    "https://cdn.discordapp.com/attachments/310547686896173056/666046891569578033/bc6.png",
    "https://cdn.discordapp.com/attachments/310547686896173056/666046876545712149/image0.jpg",
    "https://cdn.discordapp.com/attachments/310547686896173056/666046861676904461/unknown.png",
    "https://cdn.discordapp.com/attachments/310547686896173056/666046818446082065/unknown.png",
    "https://cdn.discordapp.com/attachments/310547686896173056/666046756772904992/unknown.png",
    "https://cdn.discordapp.com/attachments/310547686896173056/666046741920874516/thumb_eats-spicy-goodness-dranoverachild-oh-god-oh-frick-please-dont-55237914.png",
    "https://cdn.discordapp.com/attachments/310547686896173056/666046644416020510/unknown.png",
    "https://cdn.discordapp.com/attachments/310547686896173056/666046606810021910/800px-Sup_dawg.png",
    "https://i.imgur.com/fk71LEa.jpg",
    "https://preview.redd.it/5shus4tsvn941.jpg?width=640&crop=smart&auto=webp&s=65f805a86e49907a72fc6e9b5952cf2e5e2f9b3a",
    "https://preview.redd.it/ngrfbhgqog941.jpg?width=640&crop=smart&auto=webp&s=57f04cd2ef3df25656c63d66042919887af25ae9",
    "https://i.redd.it/6x8n5t6wnz231.jpg",
    "https://i.redd.it/4q9qyfru5lo31.jpg",
    "https://preview.redd.it/erjtxp3e82y31.jpg?width=640&crop=smart&auto=webp&s=3847f633285414a36c5c1474be61937cc2756a1c",
    "https://i.redd.it/gqywezrrxv831.jpg",
    "https://preview.redd.it/vi8v7osfmq241.jpg?width=640&crop=smart&auto=webp&s=256e91ea2806dab19b803ae89d93db2d9432f813",
    "https://i.redd.it/ldilw1qvd5841.png",
    "https://preview.redd.it/ggthq860s0h31.jpg?width=640&crop=smart&auto=webp&s=0001e1e1c6ce393179ac86e1d75cf94f5b69796c",
    "https://preview.redd.it/s396srxwou141.jpg?width=640&crop=smart&auto=webp&s=1f9711933ade9d4c44a7fb09f33e7e32fac79e43",
    "https://preview.redd.it/1qa0vr22nh141.jpg?width=640&crop=smart&auto=webp&s=5cd9313a143b2a1c5afcf0162fab8f0f561ef0e0",
    "https://preview.redd.it/eus8l2h0re541.jpg?width=640&crop=smart&auto=webp&s=4230ca3d7f0b5933b8a52111ae58d1d500a4bc4e",
    "https://i.redd.it/mw4kuokpqw041.jpg",
    "https://i.redd.it/fi8n0z96n0741.jpg",
    "https://i.redd.it/2jcllqs4vut21.jpg",
    "https://preview.redd.it/l2oh28727c341.jpg?width=640&crop=smart&auto=webp&s=983a635545c4372858669d6b1cdfeb53ff8eacbe"]

def randomExorz():
    link = ""
    link = urlExorz[random.randrange(0,len(urlExorz))]

    return link