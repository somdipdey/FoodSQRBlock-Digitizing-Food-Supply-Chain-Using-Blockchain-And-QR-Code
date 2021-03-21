# pip install pyzbar
from pyzbar.pyzbar import decode
from PIL import Image
import hashlib

# function to return key for any value
def get_key(val, dict):
    for key, value in dict.items():
         if val == value:
             return key

    return "key doesn't exist"

#create the Food class
class Food:
    def __init__(self, name, variety, farm, size, production_date, expiry_date):
        self.name = name
        self.variety = variety
        self.farm = farm
        self.size = size
        self.production_date = production_date
        self.expiry_date = expiry_date
        self.info = name + ";" + variety + ";" + farm + ";" + size + ";" + production_date + ";" + expiry_date

#create a dictionary of framers with their unique has code
farmers_dict = {
  "BOYDELLS DAIRY FARM": str(hashlib.sha256("BOYDELLS DAIRY FARM".encode()).hexdigest()),
  "Foxes Farm Produce": str(hashlib.sha256("Foxes Farm Produce".encode()).hexdigest()),
  "Spinningdale Farm (Essex) Ltd": str(hashlib.sha256("Spinningdale Farm (Essex) Ltd".encode()).hexdigest())
}

#qr = qrtools.QR()
#qr.decode("qrcode_apple.png")
qr = decode(Image.open('qrcode_milk.png'))

print(qr[0].data)
#data = "apple;gala apple;640bf572c70d06fd1d92137c5b6f69bf6f098842993032f0ca7585323407387a;2020-07-11;2020-08-10;f23f6da1e096620df2db706f55e5d9f4a59ec30f8eb3580b23a68ca15157930e"
decoded_item = str(qr[0].data).split(";")

farm = get_key(decoded_item[2], farmers_dict)
food_item = Food(decoded_item[0], decoded_item[1], farm, decoded_item[3], decoded_item[4], decoded_item[5])

#print info of the food items
print("Item name: " + food_item.name + "\n")
print("Variety: " + food_item.variety + "\n")
print("Farm: " + food_item.farm + "\n")
print("Size: " + food_item.size + "\n")
print("Production date: " + food_item.production_date + "\n")
print("Expiry date: " + food_item.expiry_date + "\n")
