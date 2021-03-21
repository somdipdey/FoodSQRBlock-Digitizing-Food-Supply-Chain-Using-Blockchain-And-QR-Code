import hashlib
import qrcode
from PIL import Image
import time

#FoodBlock is the blockchain class for food items' block
class FoodSCBlock:
    def __init__(self, info, previous_hash, transaction):
        self.info = info
        self.transaction = transaction
        self.previous_hash = previous_hash
        string_to_hash = "".join(transaction) + previous_hash
        self.block_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()

#Food class for each food item
class Food:
    def __init__(self, name, variety, farm, size, production_date, expiry_date):
        self.name = name
        self.variety = variety
        self.farm = farm
        self.size = size
        self.production_date = production_date
        self.expiry_date = expiry_date
        self.info = name + ";" + variety + ";" + farm + ";" + size + ";" + production_date + ";" + expiry_date

#get time before starting to process
then_time = time.time()

#create unique hash if for the farmer
farm_id = hashlib.sha256("BOYDELLS DAIRY FARM".encode()).hexdigest()
first_item = Food("milk", "whole milk 3.5% fat", str(farm_id), "1 lt", "2020-07-13", "2020-08-3")

print("Item info: ")
print(first_item.info + "\n")

next_supply_chain_point1 = hashlib.sha256("distribution house 1".encode()).hexdigest()
#first block in the blockchain
genesis_block = FoodSCBlock(first_item.info, first_item.info, [str(next_supply_chain_point1)])
print("Item info: " + genesis_block.info + "\n")
print("First block hash: ")
print(genesis_block.block_hash + "\n\n")

#second block in the blockchain
next_supply_chain_point2 = hashlib.sha256("shop 1".encode()).hexdigest()
second_block = FoodSCBlock(first_item.info, genesis_block.block_hash, [str(next_supply_chain_point2)])
print("Item info: " + second_block.info + "\n")
print("Second block hash: ")
print(second_block.block_hash + "\n\n")

#ftech nosh logo
logo_image = Image.open('purple-logo.png')
new_logo = logo_image.resize((120, 30))

#generate qr code to hold the food items data
#qr version 1-40. Larger the version number then larger the qr code.
qr_code = qrcode.QRCode(
            version = 30,
            error_correction = qrcode.constants.ERROR_CORRECT_H,
            box_size = 4
            )
qr_code.add_data(second_block.info + ";" + second_block.block_hash)
embedded_data = second_block.info + ";" + second_block.block_hash
print("[!] Embedded data in QR code: \n" + embedded_data + "\n")
qr_code.make(fit=True)
img = qr_code.make_image(fill_color="#451bfe", back_color="white").convert('RGB')

pos = ((img.size[0] - new_logo.size[0]) // 2, (img.size[1] - new_logo.size[1]) // 2)
img.paste(new_logo, pos)
img.save("qrcode_milk.png")

#execution time
time_def = time.time() - then_time
print("[!] Execution time: " + str(time_def))
