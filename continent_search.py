@lru_cache(maxsize=None)
def do_continent_search(alpha2):
    try:
        result = pc.country_alpha2_to_continent_code(alpha2)
        return result
    except Exception:
        return np.nan
