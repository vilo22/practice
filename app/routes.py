from app import app 
#route decorator 
# @<flask object/bluprint name>. route('/url endpoint', mehtods>)
# followed by a regular pyhton function 
@app.route('/')
def home():
    #this is a regular python function, you can write python functions here 
    greeting = 'Hello world'
    print(greeting)

    return greeting