from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate',methods=['POST'])
def calculate():

    ctc = request.form.get ("ctc")
    ctc = int(ctc)

    basic = (50 * ctc)/100
    basic_mod = basic 
    if basic_mod >= 15000:
        basic_mod = 15000
    hra = (25 * ctc)/100
    conveyance = (9.62 * ctc)/100
    eps = (8.33 * basic_mod)/100 #8.33 %
    epf_employer = (3.67 * basic_mod)/100 #3.67 %
    pf_employee = (12 * basic_mod)/100 #12%
    esi_tot = basic_mod + conveyance + hra
    if esi_tot >= 21000:
        total = basic + hra + conveyance + eps + epf_employer + pf_employee
        diff = ctc-total
        hra = hra + (diff/2)
        conveyance = conveyance + (diff/2)
        total = basic + hra + conveyance + eps + epf_employer + pf_employee

        return render_template('index.html', 
        ctc ='CTC : {}'.format(round(ctc)),
        basic ='Basic [50 %] : {}  ₹'.format(round(basic)),
        hra ='HRA [25 %] : {}  ₹'.format(round(hra)),
        conveyance ='Conveyance/Travel [9.62 %] : {}  ₹'.format(round(conveyance)),
        eps ='EPS [8.33 %] : {}'.format(round(eps)),
        epf_employer ='EPF Employer [8.33 %] : {}  ₹'.format(round(epf_employer)),
        pf_employee ='PF Employee [12 %] : {}  ₹'.format(round(pf_employee)),
        total='Total : {}  ₹'.format(round(total))
        
        )
    
    else:
            esi_employer = (3.25 * (esi_tot))/100 #3.25%
            esi_employee = (0.75 * (esi_tot))/100 #0.75% 
            total = basic + hra + conveyance + eps + epf_employer + pf_employee + esi_employee + esi_employer
            print(f"ESI Employer [3.25%] : {round(esi_employer)}")
            print(f"ESI Employee [0.75] : {round(esi_employee)}\n")

            return render_template('index.html', 
            ctc ='CTC : {}'.format(round(ctc)),
            basic ='Basic [50 %] : {}  ₹'.format(round(basic)),
            hra ='HRA [25 %] : {}  ₹'.format(round(hra)),
            conveyance ='Conveyance/Travel [9.62 %] : {}  ₹'.format(round(conveyance)),
            eps ='EPS [8.33 %] : {}'.format(round(eps)),
            epf_employer ='EPF Employer [8.33 %] : {}  ₹'.format(round(epf_employer)),
            pf_employee ='PF Employee [12 %] : {}  ₹'.format(round(pf_employee)),
            esi_employer ='ESI Employer [3.25%] : {}  ₹'.format(round(esi_employer)),
            esi_employee ='ESI Employee [0.75 %] : {}  ₹'.format(round(esi_employee)),
            total='Total : {}  ₹'.format(round(total))
            )

    


if __name__ == "__main__":
    app.run(debug=True)