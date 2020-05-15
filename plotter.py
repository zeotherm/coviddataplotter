import matplotlib.pyplot as plt
import numpy as np

def make_plot(x_data, y_data, x_interp, y_interp, y_deriv, title, x_title, ly_title, ry_title, use_derive=True):
    fig, ax1 = plt.subplots()
    ax1.scatter(x_data, y_data, marker='X', color='b')
    ax1.set_xscale('log')
    ax1.set_xlim(left=10)
    ax1.set_yscale('log')
    ax1.set_ylim(bottom=10)
    ax2 = ax1.twinx()
    if(use_derive): ax2.plot(x_interp[1:-13], y_deriv[1:-13], color='red')
    ax1.plot(x_interp[1:], y_interp[1:], color='green')
    ax1.set_xlabel(x_title)
    ax1.set_ylabel(ly_title)
    ax2.set_ylabel(ry_title)
    plt.title(title)
    fig.tight_layout()
    plt.show()


def make_compare_plot(state_data, title, x_title, y_title):
	fig, ax = plt.subplots()
	for state_abbrv, data in state_data.items():
		ax.plot(data[0], data[1], label=state_abbrv)
	ax.set_xscale('log')
	ax.set_xlim(left=100)
	ax.set_yscale('log')
	ax.set_ylim(bottom=10)
	ax.set_xlabel(x_title)
	ax.set_ylabel(y_title)
	#ax.legend()
	plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")
	plt.title(title)
	plt.tight_layout()
	plt.show()
		
		