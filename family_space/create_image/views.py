from tkinter import Image

from django.http import JsonResponse, HttpResponse
from django.views import View
from django.core.exceptions import ValidationError
from django.core.files.storage import default_storage
import os


class ImageDraw:
    pass


class ImageFont:
    pass


class LunarWatermarkView(View):
    """
    Создание ватермарки.
    """
    def post(self, request):
        fileimage = request.FILES.get('fileimage')
        message = request.POST.get('message', '')

        # Проверка обязательных полей
        if not fileimage:
            return JsonResponse({"error": "fileimage is required"}, status=400)

        if not message or not (10 <= len(message) <= 20):
            return JsonResponse({"error": "message must be between 10 and 20 characters"}, status=400)

        # Сохранение исходного изображения
        image_path = default_storage.save('original_' + fileimage.name, fileimage)

        # Создание водяного знака
        final_image = self.add_watermark(image_path, message)

        # Возвращаем итоговое изображение
        response = HttpResponse(final_image, content_type="image/jpeg")
        response['Content-Disposition'] = 'attachment; filename="watermarked_image.jpg"'
        return response

    def add_watermark(self, image_path, message):
        with Image.open(image_path) as img:
            draw = ImageDraw.Draw(img)

            # Настройка шрифта — установить шрифт
            font = ImageFont.load_default()

            # Позиция для водяного знака
            text_size = draw.textsize(message, font=font)
            position = (img.width - text_size[0] - 10, img.height - text_size[1] - 10)

            draw.text(position, message, fill=(255, 255, 255, 128), font=font)

            # Сохранение изображения с водяным знаком во временный файл
            image_with_watermark_path = 'watermarked_' + os.path.basename(image_path)
            img.save(image_with_watermark_path)

            return open(image_with_watermark_path, 'rb').read()
