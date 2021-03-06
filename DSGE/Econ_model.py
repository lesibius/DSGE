from os.path import isfile
import json

from DSGE.Equation_parser import Econ_model_parser
from DSGE.Computation import make_equations


########################################################################
# MODULE DESCRIPTION
#
# This module contains the main class to run economic models.
# It defines the Econ_model class which is used to read and parse
# parameter and variable descriptions and use them for simulation
#

########################################################################
# TO DO LIST
#
# Allow different types of inputs for model, parameters
#    Should allow to add string directly or split between multiple files
# Remove storage of parameter and variable descriptions from
#    instanciation. Should be done later if needed so the user can
#    add or modify parameters/equations on the fly
# Create a separate class to store results?
# Add flexibility as to what is stored

class Econ_model:
    """
    Generic economic model class
    """

    def __init__(self,model_name,model_path,param_path):
        """
        Econ_model instanciation

        Arguments
        ---------
        * model_name: str name of the model
        * model_path: str path to variable descriptions
        * param_path: str path to parameter descriptions
        """
        self.model_name = model_name
        self.model_path = model_path
        self.param_path = param_path
        self.model_parameters = {}

    def __call__(self,n_simulation,n_iteration):
        """
        Run the simulation

        Arguments
        ---------
        * n_simulation: int  Number of simulations
        * n_iteration: int  Number of iterations (typically number of periods)
        """
        self._load_simulation_parameters()
        self._load_equations()
        self._assign_parameter_value()
        for i in range(n_simulation):
            for v,d in self.results.items():
                d[i] = []
            for j in range(n_iteration):
                self._compute_variables()
                self._store_iteration_results(i)
            self._store_simulation_results()
            

    def _load_simulation_parameters(self):
        with open(self.param_path) as f:
            self.model_parameters = json.load(f)

    def _load_equations(self):
        parser = Econ_model_parser()
        with open(self.model_path,'r') as f:
            for line in f:
                parser.run(line)

        all_vars,eoc,param = make_equations(
            parser.variables,
            parser.get_end_of_chain_variables(),
            parser.get_parameters()
            )

        self.parameter_objects = param
        self.end_of_chain_variables = eoc
        self.all_variables = all_vars
        self.results = {name:{} for name in self.all_variables.keys()}
        

    def _assign_parameter_value(self):
        for p,v in self.model_parameters.items():
            self.all_variables[p].value = v

    def _compute_variables(self):
        for v in self.end_of_chain_variables.values():
            v()

    def _store_iteration_results(self,simulation):
        for name,v in self.all_variables.items():
            self.results[name][simulation].append(v.value)

    def _store_simulation_results(self):
        pass


    @property
    def model_name(self):
        return self._model_name

    @model_name.setter
    def model_name(self,n):
        self._model_name = n

    @property
    def param_path(self):
        return self._param_path

    @param_path.setter
    def param_path(self,p):
        self._param_path = p
        
    @property
    def model_parameters(self):
        return self._model_parameters
    
    @model_parameters.setter
    def model_parameters(self,param):
        self._model_parameters = param    

    
        
    
