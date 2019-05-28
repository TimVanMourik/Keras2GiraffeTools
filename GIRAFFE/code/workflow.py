#This is a Nipype generator. Warning, here be dragons.
#!/usr/bin/env python

import sys
import nipype
import nipype.pipeline as pe











#Create a workflow to connect all those nodes
analysisflow = nipype.Workflow('MyWorkflow')
analysisflow.connect(Conv2D, "OUTPUT", Conv2D_1, "INPUT")
analysisflow.connect(Conv2D_1, "OUTPUT", MaxPooling2D, "INPUT")
analysisflow.connect(MaxPooling2D, "OUTPUT", Dropout, "INPUT")
analysisflow.connect(Dropout, "OUTPUT", Flatten, "INPUT")
analysisflow.connect(Flatten, "OUTPUT", Dense, "INPUT")
analysisflow.connect(Dense, "OUTPUT", Dropout_1, "INPUT")
analysisflow.connect(Dropout_1, "OUTPUT", Dense_1, "INPUT")

#Run the workflow
plugin = 'MultiProc' #adjust your desired plugin here
plugin_args = {'n_procs': 1} #adjust to your number of cores
analysisflow.write_graph(graph2use='flat', format='png', simple_form=False)
analysisflow.run(plugin=plugin, plugin_args=plugin_args)
