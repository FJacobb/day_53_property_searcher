from zila import Place
from formGoogle import Form

data = Place()

in_data = Form()

for value in data.list_data:
    in_data.adds(value)