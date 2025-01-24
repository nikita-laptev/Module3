import json

from django.views import View
from django.http import JsonResponse, HttpResponseNotFound

class LunarMissionsView(View):
    """
    Функция получения миссий.
    """
    def get(self, request):
        """
        Метод получения миссий.
        :param request:
        :return:
        """
        response_data = [
            {
                "mission": {
                    "name": "Аполлон-11",
                    "launch_details": {
                        "launch_date": "1969-07-16",
                        "launch_site": {
                            "name": "Космический центр имени Кеннеди",
                            "location": {
                                "latitude": "28.5721000",
                                "longitude": "-80.6480000"
                            }
                        }
                    },
                    "landing_details": {
                        "landing_date": "1969-07-20",
                        "landing_site": {
                            "name": "Море спокойствия",
                            "coordinates": {
                                "latitude": "0.6740000",
                                "longitude": "23.4720000"
                            }
                        }
                    },
                    "spacecraft": {
                        "command_module": "Колумбия",
                        "lunar_module": "Орел",
                        "crew": [
                            {
                                "name": "Нил Армстронг",
                                "role": "Командир"
                            },
                            {
                                "name": "Базз Олдрин",
                                "role": "Пилот лунного модуля"
                            },
                            {
                                "name": "Майкл Коллинз",
                                "role": "Пилот командного модуля"
                            }
                        ]
                    }
                }
            },
            {
                "mission": {
                    "name": "Аполлон-17",
                    "launch_details": {
                        "launch_date": "1972-12-07",
                        "launch_site": {
                            "name": "Космический центр имени Кеннеди",
                            "location": {
                                "latitude": "28.5721000",
                                "longitude": "-80.6480000"
                            }
                        }
                    },
                    "landing_details": {
                        "landing_date": "1972-12-19",
                        "landing_site": {
                            "name": "Телец-Литтров",
                            "coordinates": {
                                "latitude": "20.1908000",
                                "longitude": "30.7717000"
                            }
                        }
                    },
                    "spacecraft": {
                        "command_module": "Америка",
                        "lunar_module": "Челленджер",
                        "crew": [
                            {
                                "name": "Евгений Сернан",
                                "role": "Командир"
                            },
                            {
                                "name": "Харрисон Шмитт",
                                "role": "Пилот лунного модуля"
                            },
                            {
                                "name": "Рональд Эванс",
                                "role": "Пилот командного модуля"
                            }
                        ]
                    }
                }
            }
        ]

        return JsonResponse(response_data, safe=False)

    def delete(self, request, mission_id):
        """
        Метод удаления миссий.
        """
        mission = self.get_mission_by_id(mission_id)

        if mission is None:
            return HttpResponseNotFound({"error": "Mission not found"}, content_type="application/json")

        # Логика для удаления миссии
        self.delete_mission(mission_id)

        return JsonResponse({}, status=204)

    def patch(self, request, mission_id):
        """
        Обновление миссии.
        """
        mission = self.get_mission_by_id(mission_id)
        if mission is None:
            return HttpResponseNotFound({"error": "Mission not found"}, content_type="application/json")

        # Обработка тела запроса
        try:
            data = json.loads(request.body)
            mission_data = data.get("mission", {})
            # Логика для обновления миссии
            self.update_mission(mission_id, mission_data)
            return JsonResponse({"data": {"code": 200, "message": "Mission updated"}}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    def get_mission_by_id(self, mission_id):
        return None

    def update_mission(self, mission_id, mission_data):
        pass