from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BFHLAPIView(APIView):

    def post(self, request):
        data = request.data.get("data", [])
        numbers = [x for x in data if x.isdigit()]
        alphabets = [x for x in data if x.isalpha()]
        lowercase_alphabets = [x for x in alphabets if x.islower()]

        highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else None

        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",  # Replace with dynamic user info
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
        }
        return Response(response, status=status.HTTP_200_OK)

    def get(self, request):
        return Response({"operation_code": 1}, status=status.HTTP_200_OK)
