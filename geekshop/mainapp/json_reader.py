import json


def read(file='products.JSON'):
    with open(file, 'r', encoding='utf8') as f:
        product_lst = json.load(f)["products"]
        return product_lst


if __name__ == "__main__":
    [print(a) for a in read()]