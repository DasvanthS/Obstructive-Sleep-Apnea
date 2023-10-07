from flask import Flask, render_template, request

app = Flask(__name__)

# Define the form page
@app.route('/')
def input_page():
    return render_template('form.html')

# Define the form submission handler
@app.route('/process_input', methods=['POST'])
def process_input():
    # Get the input data from the form
    input1 = request.form['input1']
    input2 = request.form['input2']
    input3 = request.form['input3']
    
    # Pass the input data to another function for processing
    output_data = process_inputs(input1, input2, input3)
    
    # Render an HTML template with the output data
    return render_template('output.html', output_data=output_data)

# Define the function that processes the input data
def process_inputs(input1, input2, input3):
    # Process the input data here
    output_data = [input1.upper(), input2.lower(), input3]
    return output_data

if __name__ == '__main__':
    app.run(debug=True)
