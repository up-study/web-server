from model_bakery import baker


baker.generators.add(
    "phonenumber_field.modelfields.PhoneNumberField", lambda: "+18443721141"
)
