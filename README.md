# FactorGraph

This program has been made for recreational number threory purposes, however, with the visualizations set in the progrm right now, there are some interesting things you can ascertain from computing phi(n), but first, some tips on using this software successfully.

<strong>Tips</strong>
<ul>
  <li>Leave data.txt blank, the program will write the y-values of the third graph to this file</li>
  <li>Clear out data.txt before running the program if you care about the data that is in it, currently the program cannot clear it before running the program, hopefully I will ad this soon</li>
  <li>If you want to compute really large numbers, comment out where the third graph is, it has a complexity of something like O(n^4), so just keep that in mind</li>
</ul>

<strong>Interesting things</strong>
<ul>
  <li>There seems to be a large number of numbers that have a prime number of factors (excluding 1), for instance in the first 100 integers, 83 of them have some prime number of factors</li>
  <li>This program also graphs a histogram of the average number of factors that an arbitrary interval {1,n} has, as n increases, the line graphed seems to approach some sort of logarithmic function, I do not know the base of that log function, but I have a feeling it might be base pi due to some initial calculations and looking at the values of the file</li>
</ul>

Any help on this is greatly appreciated as this is very interesting since I could not find anything referencing this specific pattern.
