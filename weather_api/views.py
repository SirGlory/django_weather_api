import requests
from rest_framework.views import APIView
from rest_framework.response import Response

from statistics import mean, median

api_key = 'a6bdb8db6b644cf9b9293312212407'

class Temperatures(APIView):

    def get(self, request, city):

        # Extracts second parameter from query string within url
        try:
            number_of_days = request.GET['days']
        # Handles exception where no days are provided or url incomplete, sets days = default of 1
        except :
             number_of_days = 1

        # Get request to www.weatherapi.com, data capture
        url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days={number_of_days}&aqi=no&alerts=no"
        response = requests.get(url)
        data = response.json()

        # Iterate through data to extract hourly temperatures into list
        temp_lst = []
        for days in range(len(data['forecast']['forecastday'])):
            for hours in range(len(data['forecast']['forecastday'][days]['hour'])):
                temp_lst.append(data['forecast']['forecastday'][days]['hour'][hours]['temp_c'])

        # Compute and Set outputs into dictionary form
        data_response = {
            "maximum":max(temp_lst).__round__(1),
            "minimum":min(temp_lst).__round__(1),
            "average":mean(temp_lst).__round__(1),
            "median":median(temp_lst).__round__(1),
        }

        # Return view as rest_framework response
        return Response(data_response)
