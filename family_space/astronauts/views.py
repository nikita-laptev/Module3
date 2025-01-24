from django.http import JsonResponse
from django.views import View

class GagarinFlightView(View):
    """
    Функция получения полетов Гагарина.
    """
    def get(self, request):
        response_data = {
            "data": [
                {
                    "mission": {
                        "name": "Восток 1",
                        "launch_details": {
                            "launch_date": "1961-04-12",
                            "launch_site": {
                                "name": "Космодром Байконур",
                                "location": {
                                    "latitude": "45.9650000",
                                    "longitude": "63.3050000"
                                }
                            }
                        },
                        "flight_duration": {
                            "hours": 1,
                            "minutes": 48
                        },
                        "spacecraft": {
                            "name": "Восток 3KA",
                            "manufacturer": "OKB-1",
                            "crew_capacity": 1
                        }
                    },
                    "landing": {
                        "date": "1961-04-12",
                        "site": {
                            "name": "Смеловка",
                            "country": "СССР",
                            "coordinates": {
                                "latitude": "51.2700000",
                                "longitude": "45.9970000"
                            }
                        },
                        "details": {
                            "parachute_landing": True,
                            "impact_velocity_mps": 7
                        }
                    },
                    "cosmonaut": {
                        "name": "Юрий Гагарин",
                        "birthdate": "1934-03-09",
                        "rank": "Старший лейтенант",
                        "bio": {
                            "early_life": "Родился в Клушино, Россия.",
                            "career": "Отобран в отряд космонавтов в 1960 году...",
                            "post_flight": "Стал международным героем."
                        }
                    }
                }
            ]
        }

        return JsonResponse(response_data)
