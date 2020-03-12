import pycountry
from functools import lru_cache
@lru_cache(maxsize=None)
def COUNTRY_ISO2(country):
    try:
        result = pycountry.countries.search_fuzzy(country)
        return result[0].alpha_2
    except:
        return np.nan



