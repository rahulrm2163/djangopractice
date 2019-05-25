from rest_framework.response import Response
from rest_framework.views import status


def validate_request_data(fn):
    def decorated(*args, **kwargs):
        # args[0] == GenericView Object
        first_name = args[0].request.data.get("first_name", "")
        last_name = args[0].request.data.get("last_name", "")
        last_update = args[0].request.data.get("last_update", "")

        if not first_name and not last_name and not last_update:

            return Response(
                data={
                    "message": "Both title and artist are required to add a song"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)

    return decorated
