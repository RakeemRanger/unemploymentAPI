import os

import us

class USStates:
    '''
    return all US states
    '''
    state_names = [state.name.replace(' ', '').lower() for state in us.states.STATES_AND_TERRITORIES]