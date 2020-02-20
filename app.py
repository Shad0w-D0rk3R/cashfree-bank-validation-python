'''
Below is an integration flow on how to use Cashfree's payouts SDK. The SDK can be found at: https://github.com/cashfree/cashfree-sdk-python
Please go through the payout docs here: https://dev.cashfree.com/payouts
The following script contains the following functionalities :
    1. Validations.bank_details_validation -> validate bank account
'''

from cashfree_sdk.payouts import Payouts
from cashfree_sdk.payouts.validations import Validations

clientId = "clientId"
clientSecret = "clientSecret"
env = "TEST"

try:
    Payouts.init(clientId, clientSecret, env)
    bank_validation_result = Validations.bank_details_validation(
        name= "sameera",
        phone= "9000000000",
        bankAccount= "026291800001191",
        ifsc= "YESB0000262"
    )
    print("bank validation")
    print(bank_validation_result.content)
except Exception as err:
    print("err caught in bank validation")
    print(err)
