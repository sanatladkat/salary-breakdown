from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate',methods=['POST'])
def calculate():

    monthly = request.form.get ("monthly")
    monthly = int(monthly)
    ctc = monthly * 12

    basic = (50 * monthly)/100 #50% of ctc
    basic_mod = basic 
    if basic_mod >= 15000:
        basic_mod = 15000
    hra = (25 * monthly)/100
    conveyance = (9.62 * monthly)/100
    eps = (8.33 * basic_mod)/100 #8.33 %
    epf_employer = (3.67 * basic_mod)/100 #3.67 %
    pf_employer = eps + epf_employer
    pf_employee = (12 * basic_mod)/100 #12%
    esi_tot = basic_mod + conveyance + hra
    if esi_tot >= 21000:
        total = basic + hra + conveyance + eps + epf_employer + pf_employee
        diff = monthly-total
        hra = hra + (diff/2)
        conveyance = conveyance + (diff/2)
        total = basic + hra + conveyance + eps + epf_employer + pf_employee

        return render_template('index.html', 
        ctc ='CTC : {} ₹'.format(round(ctc)),
        monthly ='Monthly Salary : {} ₹'.format(round(monthly)),
        basic ='Basic : {} ₹'.format(round(basic)),
        hra ='HRA : {} ₹'.format(round(hra)),
        conveyance ='Conveyance/Travel : {} ₹'.format(round(conveyance)),
        pf_employer ='PF Employer : {} ₹ (EPS {} ₹ + PF {}₹)'.format(round(pf_employer),round(eps),round(epf_employer)),
        pf_employee ='PF Employee : {} ₹'.format(round(pf_employee)),
        total='Total : {}  ₹'.format(round(total))
        
        )
    
    else:
            esi_employer = (3.25 * (esi_tot))/100 #3.25%
            esi_employee = (0.75 * (esi_tot))/100 #0.75% 
            total = basic + hra + conveyance + eps + epf_employer + pf_employee + esi_employee + esi_employer
            print(f"ESI Employer [3.25%] : {round(esi_employer)}")
            print(f"ESI Employee [0.75] : {round(esi_employee)}\n")

            return render_template('index.html', 
            ctc ='CTC : {} ₹'.format(round(ctc)),
            monthly ='Monthly Salary : {} ₹'.format(round(monthly)),
            basic ='Basic : {}  ₹'.format(round(basic)),
            hra ='HRA : {}  ₹'.format(round(hra)),
            conveyance ='Conveyance/Travel : {}  ₹'.format(round(conveyance)),
            pf_employer ='PF Employer : {} ₹ (EPS {} ₹ + PF {} ₹)'.format(round(pf_employer), round(eps), round(epf_employer)),
            pf_employee ='PF Employee : {}  ₹'.format(round(pf_employee)),
            esi_employer ='ESI Employer : {}  ₹'.format(round(esi_employer)),
            esi_employee ='ESI Employee : {}  ₹'.format(round(esi_employee)),
            total='Total : {}  ₹'.format(round(total))
            )

    


if __name__ == "__main__":
    app.run(debug=True)