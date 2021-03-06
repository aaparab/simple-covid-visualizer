# Main 

import os, sys
from functions import *

datapath = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'data')

if __name__ == '__main__':
    
    casedf = fetch_data()    # cases dataset
    deathdf = fetch_data(cases_data=False)    # deaths dataset
    
    # Illinois state (default)
    state = 'Illinois'
    filename = 'illinois.png'
    illinois_cases = slice_fit(casedf)
    illinois_deaths = slice_fit(deathdf)
    plot(deathdf=illinois_deaths, casedf=illinois_cases, saveloc=os.path.join(datapath, filename))

    # Illinois cases (cumulative)
    state = 'Illinois'
    filename = 'illinois_cumu.png'
    plot(casedf=illinois_cases, fit=True, cumulative=True, saveloc=os.path.join(datapath, filename))
    
    # California state
    state = 'New York'
    filename = 'ny.png'
    ny_cases = slice_fit(casedf, state=state, polydeg=8)
    plot(casedf=ny_cases, state=state, saveloc=os.path.join(datapath, filename))

    print('Program completed successfully.')
