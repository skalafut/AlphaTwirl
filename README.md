
![AlphaTwirl](images/AlphaTwirl.png?raw=true)

---

A Python library for summarizing event data in ROOT Trees

#### Description
The library contains a set of Python classes which can be used to loop over event data, summarize them, and store the results for further analysis or visualization. Event data here are defined as any data with one row (or entry) for one event; for example, data in [ROOT](https://root.cern.ch/) [TTrees](https://root.cern.ch/doc/master/classTTree.html) are event data when they have one entry for one proton-proton collision event. Outputs of this library are typically not event data but multi-dimensional categorical data, which have one row for one category. Therefore, the outputs can be imported into [R](https://www.r-project.org/) or [pandas](http://pandas.pydata.org/) as data frames. Then, users can continue a multi-dimensional categorical analysis with R, pandas, and other modern data analysis tools.

#### Example Instructions
checkout CMSSW_8_0_20_patch1, cd to the src directory, execute cmsenv, then checkout the branch v0.9.x.exmplAndInstrcts. Make a grid certificate proxy, cd to the AlphaTwirl directory, and update your PYTHONPATH variable to include the current directory:

	export PYTHONPATH=$PWD:$PYTHONPATH

Now you can run an example. Inside the completeExample directory are Framework.py, Scribbler.py (empty by default), and twirl.py. Framework.py builds the structure needed to run AlphaTwirl in a generic way, and twirl.py defines the particular attributes of an AlphaTwirl job - what variables to analyze and the binning used for each variable, references to the input .root files and output file directory name, and other job specific parameters which are specified on the command line at execution. By default twirl.py is configured to study the number of jets, HT, MHT, and jet pt by parsing a tree which contains branches named mht40_pt, ht40, nJet40, and jet_pt. Run the example by executing this command one directory above completeExample:

	./completeExample/twirl.py --input-files /afs/cern.ch/work/s/sakuma/public/cms/c150130_RA1_data/80X/MC/20160811_B01/ROC_MC_SM/TTJets_HT600to800_madgraphMLM/roctree/tree.root --dataset-names TTJets_HT600to800 -o testTbl -n 50000



