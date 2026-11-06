from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

Space_Stations = [
    {
        "id": 1,
        "name": "ISS",
        "orbit": "Earth",
        "crew": 40
    },
    {
        "id": 2,
        "name": "LEO",
        "orbit": "Low Earth Orbit",
        "crew": 50
    },
]

class SpaceStations(BaseModel):
    id: int
    name: str
    orbit: str
    crew: int

class SpaceStationCreate(BaseModel):
    name: str
    orbit: str
    crew: int

@app.get("/Space_Stations", response_model=list[SpaceStations])
def get_space_stations():
    return Space_Stations

@app.post("/Space_Stations", response_model=SpaceStations, status_code=201)
def create_space_station(space_station: SpaceStationCreate):
    new_space_station = space_station.model_dump()
    new_space_station["id"] = len(Space_Stations) + 1
    Space_Stations.append(new_space_station)
    return new_space_station
