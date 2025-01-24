from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from .models import SpaceFlight

@csrf_exempt  # временное отключение CSRF
class SpaceFlightView(View):
    """
    Создание космических рейсов.
    """
    def post(self, request):
        try:
            data = json.loads(request.body)

            flights = SpaceFlight.objects.create(
                flight_number=data['flight_number'],
                destination=data['destination'],
                launch_date=data['launch_date'],
                seats_available=data['seats_available']
            )
            return JsonResponse({
                "data": {
                    "code": 201,
                    "message": "Космический полет создан"
                }
            }, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt  # временное отключение CSRF
class BookFlightView(View):
    """
    Бронирование рейсов.
    """
    def post(self, request):
        try:
            data = json.loads(request.body)
            flight_number = data['flight_number']

            flight = SpaceFlight.objects.get(flight_number=flight_number)

            if flight.seats_available > 0:
                flight.seats_available -= 1
                flight.save()
                return JsonResponse({
                    "data": {
                        "code": 201,
                        "message": "Рейс забронирован"
                    }
                }, status=201)
            else:
                return JsonResponse({"error": "Нет доступных мест"}, status=400)

        except SpaceFlight.DoesNotExist:
            return JsonResponse({"error": "Рейс не найден"}, status=404)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
