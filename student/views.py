from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from student.serializers import StudentSerializer
from utils.dynamodb import DynamoDBClient

dynamo_client = DynamoDBClient(table_name="Student")


class StudentListCreateView(ListCreateAPIView):
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        limit = int(request.GET.get("limit", 10))
        start_key = request.GET.get("start_key")
        start_key_dict = {"roll_no": start_key} if start_key else None

        response = dynamo_client.table.scan(Limit=limit, ExclusiveStartKey=start_key_dict) \
            if start_key_dict else dynamo_client.table.scan(Limit=limit)

        return Response({
            "students": response.get("Items", []),
            "last_evaluated_key": response.get("LastEvaluatedKey")
        })

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        student_data = serializer.validated_data
        dynamo_client.put_item(student_data)

        return Response(student_data, status=status.HTTP_201_CREATED)
