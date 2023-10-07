from flask import Flask, render_template, request, make_response
import pickle
import pdfkit
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('OSAmodel.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('valid.html')

@app.route('/symptoms')
def symptoms():
    return render_template('symptoms.html', msg="success")

@app.route('/treatments')
def treatments():
    return render_template('treatments.html',msg="success")

@app.route('/valid')
def valid():
    return render_template('valid.html',msg="success")

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        name = request.form['name']
        BQ= int(request.form['BQ'])
        ESS=int(request.form['ESS'])
        BMI=float(request.form['BMI'])
        Weight=int(request.form['Weight'])
        Height=int(request.form['Height'])
        Head=float(request.form['Head'])
        Neck=int(request.form['Neck'])
        Waist=int(request.form['Waist'])
        Buttock=int(request.form['Buttock'])
        Age=int(request.form['Age'])
        M=int(request.form['M'])
        prediction=model.predict([[BQ,ESS,BMI,Weight,Height,Head,Neck,Waist,Buttock,Age,M
]])
        prediction=round(prediction[0],4)

        output_data = process_inputs(name,BQ,ESS,BMI,Weight,Height,Head,Neck,Waist,Buttock,Age,M)

        if prediction<0:
            return render_template('valid.html',output_data=output_data, prediction_texts="No{}") 
        elif prediction==0:
            return render_template('Rnormal.html',output_data=output_data, prediction_text= "OBSTRUCTIVE SLEEP APNEA CONDITION : NORMAL") 
        elif prediction==1:
            return render_template('Rmild.html',output_data=output_data, prediction_text= "OBSTRUCTIVE SLEEP APNEA CONDITION : MILD ")   
        elif prediction==2:
            return render_template('Rmoderate.html',output_data=output_data, prediction_text= "OBSTRUCTIVE SLEEP APNEA CONDITION : MODERATE ")
        elif prediction ==3:
            return render_template('Rsevere.html',output_data=output_data, prediction_text= "OBSTRUCTIVE SLEEP APNEA CONDITION : SEVERE")  
    else:
        return render_template('valid.html')

def process_inputs(name,BQ,ESS,BMI,Weight,Height,Head,Neck,Waist,Buttock,Age,M):
    # Process the input data here
    output_data = [name,BQ,ESS,BMI,Weight,Height,Head,Neck,Waist,Buttock,Age,M]
    return output_data

if __name__=="__main__":
    app.run(debug=True)