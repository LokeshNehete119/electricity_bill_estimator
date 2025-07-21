import joblib
import gradio as gr
import numpy as np

model = joblib.load('best_model_gb_grid.pkl')

# Define prediction function with all 7 inputs
def predict_bill(fan, refrigerator, ac, tv, monitor, month, tariff_rate):
    if month == 0:
        return "⚠️ Please select the month."
    total = fan + refrigerator + ac + tv + monitor
    if fan == 0 and refrigerator == 0 and ac == 0 and tv == 0 and monitor == 0:
        return "⚠️ Please turn on at least one appliance."

# Using a numpy array to store input values and total
    input_array = np.array([[fan, refrigerator, ac, tv, monitor, month, tariff_rate,total]])
    prediction = model.predict(input_array)
    return f"Predicted Electricity Bill: ₹{prediction[0]:.2f}"

# Build the Gradio interface
interface = gr.Interface(
    fn=predict_bill,
    inputs=[
        gr.Number(label="Fan (Hours/Day)"),
        gr.Number(label="Refrigerator (Hours/Day)"),
        gr.Number(label="Air Conditioner (Hours/Day)"),
        gr.Number(label="Television (Hours/Day)"),
        gr.Number(label="Monitor (Hours/Day)"),
        gr.Number(label="Month (1 to 12)"),
        gr.Number(label="Tariff Rate (₹ per Unit)"),
    ],
    outputs=gr.Textbox(label="Estimated Monthly Electricity Bill"),
    title="Electricity Bill Estimator",
    description="Enter appliance usage, month, and tariff rate to estimate your electricity bill"
)

# Launch the app
interface.launch()
