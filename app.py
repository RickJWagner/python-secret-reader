import os
import subprocess
import json
from hydra import HydraApi
from hydra.auth import RedHatSSOAuth
from hydra.sso import get_token, throw_if_no_token

print ("starting!")


hydra_user = os.environ["HYDRA_USERNAME"]
hydra_pwd = os.environ["HYDRA_PASSWORD"]


print (hydra_user)
print ("ending")
