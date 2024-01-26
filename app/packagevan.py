from phone_number_validator_van_ben_pham import validator
from lib_llm.gpt4 import QueryDocumentV3, default_schema_enbridge

my_validator = validator.PhoneNumberValidator(api_key="num_live_VWZV0PNfrIAQh0lBbgtNlDdmX3pstcwIuwzLkQyt")


is_valid1 = my_validator.validate("+154725")
is_valid2 = my_validator.validate("+127143847563452")
is_valid3 = my_validator.validate("543895732985734", country_code="US")
print(is_valid1)
print(is_valid2)
print(is_valid3)

MY_OPENAI_KEY = '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'
my_query = QueryDocumentV3(company="enbridge",openai_key=MY_OPENAI_KEY)
output = my_query.search_v3('pdf_enbridge/f6a50c4f-2d0b-4cb2-b1a7-6e1a0970d8c8.pdf', 'easy')

print(output)