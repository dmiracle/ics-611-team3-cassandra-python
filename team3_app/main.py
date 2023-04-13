from fastapi import FastAPI
from pydantic import BaseModel
from team3_app.geolocate import get_census_tract
from team3_app.get_demographics import get_demographics
from team3_app.ad_engine import start_auction, retreive_ad

app = FastAPI()


class UpdateResponse(BaseModel):
    tract: str
    demographics: dict
    auction_id: str
    ad: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/update")
def update_location(address: str = "700 E 7th St, St Paul, MN 55106"):
    tract = get_census_tract(address)
    demographics = get_demographics(tract)
    auction_id = start_auction(demographics)
    ad = retreive_ad(auction_id)

    return UpdateResponse(
        tract=tract, demographics=demographics._asdict(), auction_id=auction_id, ad=ad
    )
