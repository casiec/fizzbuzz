from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

callers = {
    "+18323776562": "Casie",
    }
 
@app.route("/", methods=['GET', 'POST'])
def hello_fizzbuzz():
    from_number = request.values.get("From", None)
    resp = twilio.twiml.Response()
    resp.say("Hello, and welcome to FizzBuzz!")

    with resp.gather(finishOnKey="*", action="/handle_number", method="POST") as g:
        g.say("Please enter a number followed by star to play")

    return str(resp)
@app.route("/handle_number", methods=['GET','POST'])
def handle_number():
    resp = twilio.twiml.Response()
    number_entered = request.values.get("Digits", None)
    number_list = ""
    for i in range(1, int(number_entered)+1):
        i_string = ""
        if i % 3 == 0:
            i_string += "Fizz"
        if i % 5 == 0:
            i_string += "Buzz"
        if not i_string:
            number_list = number_list + str(i) + " "
        else:
            number_list = number_list + i_string + " "
    resp.say("You entered {}. FizzBuzz says {}" .format(str(number_entered), number_list))
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)
