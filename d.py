import pickle

db = [
    {
        "number": "50678543",
        "IMEI": "497114507705331",
        "state": True
    },
    {
        "number": "50774419",
        "IMEI": "447017241294071",
        "state": True
    },
    {
        "number": "50123654",
        "IMEI": "512015199488921",
        "state": False
    },
    {
        "number": "50098765",
        "IMEI": "981134182406861",
        "state": True
    },
    {
        "number": "50123456",
        "IMEI": "547236255848701",
        "state": True
    },
]

bfile = open("./data.dat", 'wb')

pickle.dump(db, bfile)

bfile.close()
dbfile = open("./data.dat", 'rb')
db = pickle.load(dbfile)
print(db)
dbfile.close()
