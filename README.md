# pkraken

# Setup

Goto https://octopus.energy/dashboard/new/accounts/personal-details/api-access and get an API key.

Add a `.env` file with the following content:

```bash
API_KEY=your api key
GAS_MPRN=your mprn
ELEC_MPAN=your mpan
ELEC_SERIAL=your serial
```
# Tests

```bash
python -m unittest -v tests.all
```