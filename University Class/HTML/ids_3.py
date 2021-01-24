 Procedure IdSearch(G,s,goal) 
2:           Inputs
3:                     G: graph with nodes N and arcs A 
4:                     s: set of start nodes 
5:                     goal: Boolean function on states 
6:           Output
7:                     path from s to a node for which goal is true 
8:                     or ⊥ if there is no such path 
9:           Local
10:                     natural_failure: Boolean 
11:                     bound: integer 
12:                     Procedure dbsearch(⟨n0,...,nk⟩,b) 
13:                               Inputs
14:                                         ⟨n0,...,nk⟩: path 
15:                                         b: integer, b ≥ 0 
16:                               Output
17:                                         path to goal of length k+b 
18:                               if (b>0) then 
19:                                         for each arc ⟨nk,n⟩∈A do 
20:                                                   dbsearch(⟨n0,...,nk,n⟩,b-1) 
21:                               else if (goal(nk)) then 
22:                                         return ⟨n0,...,nk⟩ 
23:                               else if (nk has any neighbors) then 
24:                                         natural_failure←false 
25:           bound ←0 
26:           repeat
27:                     natural_failure←true 
28:                     dbsearch({⟨s⟩:s∈S},bound) 
29:                     bound ←bound+1 
30:           until natural_failure 
31:           return ⊥