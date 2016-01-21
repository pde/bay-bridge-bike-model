This repository contains a quickly put-togther [iPython
Notebook](http://ipython.org/notebook.html) model of the commute time across a
proposed Bay Bridge bike path, as a function most particularly of wind speed.
It includes evaluations of two types of wind shielding: a tube enclosing the
path in both directions, and a tube enclosing the path just in the westbound
direction.

For a windy day (15 knot winds from the WSW,
more or less along the bridge), the results are:

Open air:
  Eastbound 10.2919700996 minutes
  Westbound 27.8813418402 minutes
Half Tube:
  Eastbound 10.2919700996 minutes
  Westbound 15.3037753663 minutes
Full Tube:
  Eastbound 15.2994915657 minutes
  Westbound 15.3037753663 minutes
Tube Saves 7.57004500779 minutes
Half tube saves 12.5775664739 minutes
(25.6 minutes vs 38.2 minutes)

Current omissions and questions include:

* Use real wind direction and speed distributions from
  http://www.met.sjsu.edu/cgi-bin/wind/windbin.cgi (will need assistance from
  their team) or elsewhere

* Account for slight difference in orientation of the two spans

* Include ramps and Yerba Buena island in the model

* If fully enclosed tubing is prohibitively expensive, attempt to model
  partial shielding of various sorts?  For instance, is there a way to build a
  cheap / simple shield on one side of the path, which approximates a half
  tube?  Presuming that such a shield should also double as a traffic noise
  barrier, would this argue for placing bike lanes on the south side of the
  bridge, or for staying on the north side but marking the path as "bike on
  the left" rather than on the right, as is typical in the US?
