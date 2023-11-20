import os


name = os.getenv("env_prod", "prod")
if name != "prod":
    DATA_BASE = "postgresql://myuser:mypassword@localhost/genesiswarehouse"
else:
    DATA_BASE = "postgresql://myuser:mypassword@postgres/genesiswarehouse"
