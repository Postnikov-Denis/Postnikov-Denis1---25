from PIL import Image
def zad71(image1):
    image1 = Image.open(image1)

    print(f"Размер изображения: {image1.size}")
    print(f"Формат изображения: {image1.format}")
    print(f"Цветовая модель: {image1.mode}")

    image1.show()
#imagepath = "Logo_comp1.png"
#print(zad71(imagepath))
