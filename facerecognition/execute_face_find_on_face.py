from face_find import Face

# samples:
# https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Donald_Trump_official_portrait.jpg/1200px-Donald_Trump_official_portrait.jpg
# https://cryptobeat.co/pay/musk.png


predictions = Face("https://cryptobeat.co/pay/musk.png").predict()
print(predictions)
