from flask import Flask, abort, request

app = Flask(__name__)


class Validity():
    num: int
    validity: bool
    eveness: bool

    items = {3, 5, 7, 11, 13, 17, 23}

    def dictonary(self):
        return {
            "even": True,
            "valid": True
        }

    def valid_id(self, number):
        if number not in Validity.items:
            temp = Validity
            temp.set_validity(self, False)
        if (number % 2) != 0:
            temp.set_eveness(self, False)
        return temp

    def set_validity(self, val):
        self.validity = val

    def set_eveness(self, val):
        self.eveness = val


@app.route('/api/valid_id/<id>', methods=["GET"])
def valid(id):
    if id not in Validity.items:
        temp = Validity
        temp.set_validity(False)
    if (id % 2) != 0:
        temp.set_eveness(False)
    return {"even": True, "valid": False}


