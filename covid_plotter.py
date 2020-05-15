import json
import numpy as np

def get_state_data(data, state):
	return list(filter(lambda l: l['state'] == state, data))[::-1]

def get_xy_from_state(state_data):
	ds = [(i.get('positive',-1), i.get('positiveIncrease',-1)) for i in state_data[1:]]
	return ([v[0] for v in ds], [v[1] for v in ds])

def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

def make_combined_data(data, state_list):
	d = {}
	n = 5
	for abbrv in state_list:
		s_x, s_y = get_xy_from_state(get_state_data(data, abbrv))
		d[abbrv] = (s_x[n-1:], moving_average(s_y, n=n))
	return d

	
#>>> import covid_data as cd
#>>> import covid_plotter as cp
#>>> import plotter as p
#>>> plot_data = cp.make_combined_data(cd.load_data(), ['ME', 'NH', 'MA', 'RI', 'CT', 'NY', 'NJ', 'PA', 'MD', 'VA', 'NC', 'SC', 'GA', 'FL'])
#>>> p.make_compare_plot(plot_data, 'New cases v. Total Cases', 'Total Cases', 'New Cases (5-day moving average)')