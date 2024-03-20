# pkraken

# Setup

Goto https://octopus.energy/dashboard/new/accounts/personal-details/api-access and get an API key.

Add a `.env` file with the following content:

```bash
# To test the API
API_KEY=your api key
GAS_MPRN=your mprn
GAS_SERIAL=your serial
ELEC_MPAN=your mpan
ELEC_SERIAL=your serial
# DJANGO
DB_ENGINE=django.db.backends.postgresql
DB_NAME=xxxxxxxx
DB_USER=xxxxxxxx
DB_PASSWORD=xxxxxxxx
DB_HOST=xxxxxxxx
DB_PORT=xxxxxxxx

```
# Tests

```bash
python -m unittest -v tests.all
```