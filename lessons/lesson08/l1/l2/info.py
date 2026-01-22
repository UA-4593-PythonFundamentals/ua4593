
def print_info():
    import os
    print(f"full path to module: {os.path.abspath(__file__)}")
    print(f"{__name__=}")

print_info()