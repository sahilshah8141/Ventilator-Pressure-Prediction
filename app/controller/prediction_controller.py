from fastapi import APIRouter
from app.request_models.prediction_model import PredictionModel
from app.services.prediction_services import AppServices, PredictionServices
prediction_router = APIRouter()


@prediction_router.post('/')
def pressure_prediction(prediction_details: PredictionModel):
    """
    This API is used to predict the ventilator pressure based on the user input.
    ...
    Author
    --------------
    Name: Sahil Shah
    """
    if prediction_details:
        pressure_res = PredictionServices.predict_pressure_service(prediction_details)
        response = AppServices.app_response(200, "Ventilator pressure procedure completed"
                                            " successfully!!", pressure_res)
    else:
        response = AppServices.app_response(500, "Proper feature details haven't found",
                                            "Internal Server Error")

    return response

