from django.http import JsonResponse
from django.views import View

class MissionSearchView(View):
    def get(self, request):
        query = request.GET.get('query', '')
        missions = 'missions.Mission'.objects.filter(name__icontains=query)

        response_data = {
            "data": []
        }

        for mission in missions:
            crew_members = mission.crew.all()
            crew_data = [{"name": member.name, "role": member.role} for member in crew_members]

            response_data["data"].append({
                "type": "Миссия",
                "name": mission.name,
                "launch_date": mission.launch_date,
                "landing_date": mission.landing_date,
                "crew": crew_data,
                "landing_site": mission.landing_site
            })

        return JsonResponse(response_data, status=200)
