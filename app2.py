# from flask import Flask, render_template, request
# import requests , math

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index2.html',result=None)

# @app.route('/result', methods=['POST'])
# def calculate_salary():
#     hourly_salary = int(request.form['hourlySalary'])
#     proposed_indian_salary = int(request.form['proposedIndianSalary'])

#     response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
#     exchange_rate = response.json()['rates']['INR']

#     daily_salary = hourly_salary * 8
#     monthly_salary = daily_salary * 20
#     yearly_salary = monthly_salary * 12

#     actual_indian_salary = yearly_salary * exchange_rate
#     daily_salaryy = daily_salary * exchange_rate
#     monthly_salaryy = monthly_salary * exchange_rate
    
#     data=[]
#     k=19
#     for i in range(1,22):
#         total=k*8*20*12*exchange_rate
#         temp=((total-proposed_indian_salary)*100/total)
#         data.append(temp)
#         k+=1
#     company_profit = ((actual_indian_salary - proposed_indian_salary) / actual_indian_salary) * 100
#     # predict_sal=datas
   
#     return render_template('result2.html', hourly_salary=hourly_salary,daily_salary=daily_salary, monthly_salary=monthly_salary,
#                             yearly_salary=yearly_salary, actual_indian_salary=math.floor(actual_indian_salary), daily_salaryy=daily_salaryy,monthly_salaryy=monthly_salaryy,
#                             company_profit=company_profit,data=data)
                        
    

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
import requests, math

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index2.html', result=None, hourly_salary=None, daily_salary=None, monthly_salary=None,
                           yearly_salary=None, actual_indian_salary=None, daily_salaryy=None, monthly_salaryy=None,
                           company_profit=None, data=None)

@app.route('/calculate', methods=['POST'])
def calculate_salary():
    hourly_salary = int(request.form['hourlySalary'])
    proposed_indian_salary = int(request.form['proposedIndianSalary'])

    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    exchange_rate = response.json()['rates']['INR']

    daily_salary = hourly_salary * 8
    monthly_salary = daily_salary * 20
    yearly_salary = monthly_salary * 12

    actual_indian_salary = yearly_salary * exchange_rate
    daily_salaryy = daily_salary * exchange_rate
    monthly_salaryy = monthly_salary * exchange_rate

    data = []
    k = 19
    for i in range(1, 22):
        total = k * 8 * 20 * 12 * exchange_rate
        temp = ((total - proposed_indian_salary) * 100 / total)
        data.append(temp)
        k += 1
    company_profit = ((actual_indian_salary - proposed_indian_salary) / actual_indian_salary) * 100

    return render_template('index2.html', result="success", hourly_salary=hourly_salary, proposed_indian_salary=proposed_indian_salary, daily_salary=daily_salary,
                           monthly_salary=monthly_salary, yearly_salary=yearly_salary,
                           actual_indian_salary=math.floor(actual_indian_salary), daily_salaryy=daily_salaryy,
                           monthly_salaryy=monthly_salaryy, company_profit=company_profit, data=data)


if __name__ == '__main__':
    app.run(debug=True)
