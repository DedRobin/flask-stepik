from flask import Flask, render_template, request


class Order:
    def __init__(self, id, desc, items):
        self.id = id
        self.description = desc
        self.items = items

    def __repr__(self):
        return f'<Order {self.id}: {self.items} - {self.description}>'


orders = {43: Order(43, 'Оплата картой, через почту', ['Кружка', 'Майка', 'Стикеры']),
          69: Order(69, 'Оплата наличными, через почту', ['Медные диски'])}

app = Flask(__name__)


@app.route("/", methods=["POST"])
def render_send():
    try:
        order_id = int(request.form.get("id"))
    except ValueError:
        order = "Ошибка"
    else:
        order = orders.get(order_id, "Ошибка")
    return repr(order)


if __name__ == '__main__':
    app.run()
