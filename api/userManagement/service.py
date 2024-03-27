import json

from django.http import HttpResponse

from rest_framework import status
from rest_framework.response import Response

def invalid_input(input_name):
    """
    this function return an invalid input
    :return :
    HttpResponse : a message containing the name of the invalid input
    """
    response = json.dumps({"Error": f"Invalid {input_name}"})
    status_code = status.HTTP_403_FORBIDDEN
    return HttpResponse(
        response, content_type="application/json", status=status_code
    )


def check_parameters(
    first_name: str,
    last_name: str,
    username: str,
    password: str,
    email: str,
    telephone: str,
) -> bool:
    """
    This function returns check the validity of the user
    (username,password...)

    parameters:
    first_name (str) : first name of the user
    last_name (str) : last name of the user
    username (str) : username
    password (str) : password
    email (str) : email of the user
    telephone (integer) : telephone

    returns:
    bool ==> True if all conditions True else HttpResponse
    """
    conditions_first_name = [not first_name, not isinstance(first_name, str)]
    conditions_last_name = [not last_name, not isinstance(last_name, str)]
    conditions_username = [not username, not isinstance(username, str)]
    conditions_password = [not password, not isinstance(password, str)]
    conditions_email = [not email, not isinstance(email, str)]
    conditions_telephone = [not telephone, not isinstance(telephone, str)]
    if any(conditions_first_name):
        return invalid_input("first_name")
    elif any(conditions_last_name):
        return invalid_input("last_name")
    elif any(conditions_username):
        return invalid_input("username")
    elif any(conditions_password):
        return invalid_input("password")
    elif any(conditions_email):
        return invalid_input("email")
    elif any(conditions_telephone):
        return invalid_input("telephone")
    elif any(conditions_profession):
        return invalid_input("profession")
    elif bool(plan) is True and any(conditions_plan):
        return invalid_input("plan")
    else:
        return True