from pydantic import BaseModel


class PredictionModel(BaseModel):
    R: int
    C: int
    u_in: float
    u_out: int
