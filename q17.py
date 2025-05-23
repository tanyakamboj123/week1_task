import openai
import os
##openai.api_key="eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIxZjMwMDA3NDVAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.IZP6rAsgD2Bo9ClgiWVrrgFxPfe2FQpo9TB9FlkwpTA"


openai.api_key = os.getenv("OPENAI_API_KEY")

OPENAI_BASE_URL =" https://aipipe.org/openai/v1"

##openai.api_base = OPENAI_BASE_URL