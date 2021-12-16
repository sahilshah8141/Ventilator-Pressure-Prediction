import os
from pathlib import Path
import time
import joblib

start_time = time.time()
project_path = Path(__file__).parent.parent.parent
model_prediction_file = os.path.join(project_path, "models/random_forest_model_lower_data.joblib")
scaler_file = os.path.join(project_path, "models/ventilator-scaler-lower.pkl")

class PredictionServices:

    @staticmethod
    def get_current_timestep():
        global start_time
        end_time = time.time()
        time_step = end_time - start_time

        if time_step >= 3:
            start_time = time.time()
            time_step = 0

        return time_step

    @staticmethod
    def predict_pressure_service(prediction_details):

        try:
            r = prediction_details.R
            c = prediction_details.C
            time_step = PredictionServices.get_current_timestep()
            u_in = prediction_details.u_in
            u_out = prediction_details.u_out

            # Currrently taken aggregation values of first breath
            u_in_max = 4.987079
            u_in_mean = 3.152422
            u_in_std = 1.763825

            user_requested_data = [[r, c, time_step, u_in, u_out, u_in_max, u_in_mean, u_in_std]]
            scaler = joblib.load(scaler_file)
            scaled_user_requested_data = scaler.transform(user_requested_data)
            model = joblib.load(model_prediction_file)
            pressure_res = list(model.predict(scaled_user_requested_data))[0]

        except Exception as v_exc:
            pressure_res = v_exc.__str__()

        return pressure_res


class AppServices:

    @staticmethod
    def app_response(status_code: int, message: str, data: any = None) -> dict:
        response = {
            "status_code": status_code,
            "message": message,
            "data": data
        }

        return response



