import requests

def test_app():
    resp1 = requests.get('http://localhost:8080/1')
    resp2 = requests.get('http://localhost:8080/10')
    resp3 = requests.get('http://localhost:8080/100')
    x = "{" + '"' + "num" + '"' + ": 0}"
    y = "{" + '"' + "num" + '"' + ": 34}"
    z = "{" + '"' + "num" + '"' + ": 218922995834555169026}"
    if resp1.text == x:
        x = "test 1: first values passed"
    else:
        x = "test 1: first values failed"
    if resp2.text == y:
        y = " test 2: low values passed"
    else:
        y = " test 2: low values failed"
    if resp3.text == z:
        z = " test 3: high values passed"
    else:
        z = " test 3: high values failed"
    return(x + y + z)
print(test_app())