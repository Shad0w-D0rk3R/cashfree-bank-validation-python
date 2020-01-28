from cashfree_sdk.payouts import Payouts
from cashfree_sdk.payouts.validations import Validations

clientId = "clientId"
clientSecret = "clientSecret"

try:
    Payouts.init(clientId, clientSecret, "TEST")
    bank_validation_result = Validations.bank_details_validation(**{
        "name": "sameera",
        "phone": "9000000000",
        "bankAccount": "026291800001191",
        "ifsc": "YESB0000262"
    })
    print("bank validation")
    print(bank_validation_result.content)
except Exception as err:
    print("err caught in bank validation")
    print(err)
