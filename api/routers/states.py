from fastapi import APIRouter

from ..utils.states import USStates

router = APIRouter()
states = USStates.state_names

@router.get("/state/{state}")
async def get_state(state: str):
    if str(state) in states:
        return {
            "country": "USA",
            "state": state,
            "returnCode": 200,
            "message": f"State {state} is a valid State in the USA"
        }
    else:
        return {
            "returnCode": 404,
            "message": f"Error state:{state} is not a valid USA state, Try Again with a valid state | valid states:{states}"
        }