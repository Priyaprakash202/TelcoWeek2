import json


class U:
    def __init__(self, data):
        self.a = data.get("A")
        self.b = data.get("B")

        if not isinstance(self.a, int):
            raise Exception("A must be an integer")

        if not isinstance(self.b, str):
            raise Exception("B must be a string")


def main():
    
    with open("data22.json") as f:
        D = json.load(f)

    
    valid = 0
    invalid = 0

 
    for item in D:
        try:
            obj = U(item)
            print("Valid:", obj.a, obj.b)
            valid += 1
        except Exception as e:
            print("Invalid:", item, "-", e)
            invalid += 1


main()