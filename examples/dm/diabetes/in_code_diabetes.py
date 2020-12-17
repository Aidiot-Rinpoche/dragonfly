from dragonfly import minimise_multifidelity_function
from dragonfly.exd.cp_domain_utils import load_config_file
import os
# problem imports
from rfr_mf import objective as rfr_mf_obj
from rfr_mf import cost as rfr_mf_cost

MAX_CAPITAL = 10

LOG_FILE = 'rfr_mf_obj_mf'

def main():
    """ Main Function"""
    # Choose configuration file
    wp = os.getcwd()
    config_file = wp+'\\examples\\dm\\diabetes'+'\\config_skrfr_mf.json'
    config = load_config_file(config_file)
    log_stream = open(LOG_FILE,'w')
    # Call the optimiser
    opt_val, opt_pt, history = minimise_multifidelity_function(rfr_mf_obj, 
    config.fidel_space, config.domain, config.fidel_to_opt, rfr_mf_cost,
    MAX_CAPITAL,capital_type='realtime', config=config, reporter=log_stream)
    log_stream.close()
    print('Optimum Value found in %02.f time (%d evals): %0.4f'%(
        MAX_CAPITAL, len(history.curr_opt_points), opt_val))
    print('Optimum Point: %s.'%(str(opt_pt)))

if __name__ == '__main__':
    main()