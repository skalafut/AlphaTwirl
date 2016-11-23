
![AlphaTwirl](images/AlphaTwirl.png?raw=true)

---

A Python library for summarizing event data in ROOT Trees

#### Description
The library contains a set of Python classes which can be used to loop over event data, summarize them, and store the results for further analysis or visualization. Event data here are defined as any data with one row (or entry) for one event; for example, data in [ROOT](https://root.cern.ch/) [TTrees](https://root.cern.ch/doc/master/classTTree.html) are event data when they have one entry for one proton-proton collision event. Outputs of this library are typically not event data but multi-dimensional categorical data, which have one row for one category. Therefore, the outputs can be imported into [R](https://www.r-project.org/) or [pandas](http://pandas.pydata.org/) as data frames. Then, users can continue a multi-dimensional categorical analysis with R, pandas, and other modern data analysis tools.

#### AlphaTwirl Usage
One of AlphaTwirl's greatest strengths is that it works with any data stored in a TTree or EDM root file.  GEN particles, DIGI collections, HLTFilterObjects, PFRecHits, GsfElectrons, whatever you can find in a TTree or EDM root file will work with AlphaTwirl.  In addition, using Scribblers AlphaTwirl can take a large tree with many branches and condense the useful information from a select few branches into a single event object which facilitates faster calculations.

#### AlphaTwirl Count
All of AlphaTwirl can be reduced down to the dictionaries defined the configuration table (see twirl-example for a thorough introduction).  Three types of dictionaries can be defined in the configuration table, one of which is the Count style dictionary.  A Count style dictionary produces a txt file which is analogous to a 1 or multi dimensional histogram, showing the number of events as a function of different values of the input variables.

#### AlphaTwirl Sum
AlphaTwirl Sum is another type of dictionary which can be defined in the configuration table before run time.  Beginning with a Count dictionary, a Sum dictionary is created by adding 4 new elements to the dictionary.  valAttrNames (list), valIndices (list), valOutColumnNames (list), and summaryClass (string).  The val lists indicate the variable to sum over given different input key values.

#### AlphaTwirl Scan
AlphaTwirl Scan is another type of dictionary which can be defined in the configuration table before run time.  Beginning with a Sum dictionary, a Scan dictionary is created by changing summaryClass from AlphaTwirl.Summary.Sum to AlphaTwirl.Summary.Scan.  (describe usefulness of Scan).

