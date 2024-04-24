from PIL import Image
    def zad71(image):
        image = Image.open(image)

        print(f"Размер изображения: {image.size}")
        print(f"Формат изображения: {image.format}")
        print(f"Цветовая модель: {image.mode}")

        image.show()

print(zad71(Logo_comp1.png))