from flask import Blueprint, jsonify, request
from flask_cors import CORS, cross_origin
from pydantic import BaseModel
from validate_email import validate_email
from typing import Union
from utils.encrypter import loadKeys, decrypt
import os

class EmailCheckerModel(BaseModel):
   email: str

class MainModel(BaseModel):
   data: str

class ResponseModel(BaseModel):
   success: bool
   email: str
   existingEmail: Union[bool, None]

checker = Blueprint("checker", __name__, url_prefix="/checker")
CORS(checker)

@checker.route("/email", methods=["POST"])
@cross_origin(origins="*", allow_headers=["Content-Type"])
def emal_checker_func() -> ResponseModel:
   if request.method == "POST":
      print("Data received")
      is_valid = validate_email(request.json['email'])
      return jsonify(dict(ResponseModel(
         success=True, 
         email=request.json['email'], 
         existingEmail=is_valid))
      )