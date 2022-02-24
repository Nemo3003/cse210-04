from PIL import Image
icon_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (255, 255)]
image = Image.open('game/directing/gems.png')
fileoutpath = 'game/directing' 
for size in icon_sizes:
    print(size[0])
    fileoutname = fileoutpath + str(size[0]) + ".png"
    new_image = image.resize(size)
    new_image.save(fileoutname)

new_logo_ico_filename = fileoutpath + "Icon.ico"
new_logo_ico = image.resize((128, 128))
new_logo_ico.save(new_logo_ico_filename, format="ICO",quality=90)