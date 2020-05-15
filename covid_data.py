import json
import urllib.request

def load_data():
	url = 'https://covidtracking.com/api/v1/states/daily.json'
	file_name = 'covid_tmp.json'
	urllib.request.urlretrieve(url, file_name)
	#open(file_name, 'w').write(r.content)
	
	#file_name = "C:\\Users\\Matt\\Desktop\\covid.json"
	raw_data = open(file_name, 'r')
	return json.load(raw_data)


#md_data = get_state_data(data, 'MD')
#md_data_rev = md_data[::-1] # puts it in chronological order
#md_data[0].keys()
#dict_keys(['date', 'state', 'positive', 'negative', 'pending', 'hospitalizedCurrently', 'hospitalizedCumulative', 'inIcuCurrently', 'inIcuCumulative', 'onVentilatorCurrently', 'onVentilatorCumulative', 'recovered', 'dataQualityGrade', 'lastUpdateEt', 'hash', 'dateChecked', 'death', 'hospitalized', 'total', 'totalTestResults', 'posNeg', 'fips', 'deathIncrease', 'hospitalizedIncrease', 'negativeIncrease', 'positiveIncrease', 'totalTestResultsIncrease'])


#ds = [(i.get('positive',-1), i.get('positiveIncrease',-1)) for i in md_data_rev[1:]]
#x = [v[0] for v in ds]
#y = [v[1] for v in ds]
"""
>>> ds_hosp = [(i.get('positive',-1), i.get('hospitalizedIncrease',-1)) for i in md_data[1:]]
>>> x_hosp = [v[0] for v in ds_hosp]
>>> y_hosp = [v[1] for v in ds_hosp]
>>> x_inp = [300*i for i in range(116)]
>>> y_inp = np.interp(x_inp, x, y)
>>> y_filtered = savitzky_golay(y_inp, 9, 2)
>>> y_deriv = savitzky_golay(y_inp, 13, 2, deriv=1)
>>> y_inp_hosp = np.interp(x_inp, x_hosp, y_hosp)
>>> y_filtered_hosp = savitzky_golay(y_inp_hosp, 9, 2)
>>> y_deriv_hosp = savitzky_golay(y_inp_hosp, 13, 2, deriv=1)
>>> plotter.make_plot(x_hosp, y_hosp, x_inp, y_filtered_hosp, y_deriv_hosp, 'daily new hospitalizations v. total cases', 'total cases', 'new hospitalizations', 'd(new hosp)/d(total cases)')
>>>  y_filtered_hosp = savitzky_golay(y_inp_hosp, 9, 3)
  File "<stdin>", line 1
    y_filtered_hosp = savitzky_golay(y_inp_hosp, 9, 3)
    ^
IndentationError: unexpected indent
>>> y_filtered_hosp = savitzky_golay(y_inp_hosp, 9, 3)
>>> y_deriv_hosp = savitzky_golay(y_inp_hosp, 13, 3, deriv=1)
>>> plotter.make_plot(x_hosp, y_hosp, x_inp, y_filtered_hosp, y_deriv_hosp, 'daily new hospitalizations v. total cases', 'total cases', 'new hospitalizations', 'd(new hosp)/d(total cases)')
>>> plotter = reload(plotter)
>>> plotter.make_plot(x_hosp, y_hosp, x_inp, y_filtered_hosp, y_deriv_hosp, 'daily new hospitalizations v. total cases', 'total cases', 'new hospitalizations', 'd(new hosp)/d(total cases)')
>>> plotter.make_plot(x, y, x_inp, y_filtered, y_deriv, 'daily new cases v. total cases', 'total cases', 'new cases', 'd(new cases)/d(total cases)')
>>> plotter.make_plot(x, y, x_inp, y_filtered, y_deriv, 'daily new cases v. total cases', 'total cases', 'new cases', 'd(new cases)/d(total cases)')
>>> plotter.make_plot(x_hosp, y_hosp, x_inp, y_filtered_hosp, y_deriv_hosp, 'daily new hospitalizations v. total cases', 'total cases', 'new hospitalizations', 'd(new hosp)/d(total cases)')
>>> plotter = reload(plotter)
>>> plotter.make_plot(x, y, x_inp, y_filtered, y_deriv, 'daily new cases v. total cases', 'total cases', 'new cases', 'd(new cases)/d(total cases)')
>>> plotter.make_plot(x_hosp, y_hosp, x_inp, y_filtered_hosp, y_deriv_hosp, 'daily new hospitalizations v. total cases', 'total cases', 'new hospitalizations', 'd(new hosp)/d(total cases)')
>>>
"""