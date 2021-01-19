def generate_affiliation_link(url):
    parts = url.split("/")
    prod = parts[parts.index('dp')+1]
    return f"http://www.amazon.com/dp/{prod}/?tag=pyb0f-20"
