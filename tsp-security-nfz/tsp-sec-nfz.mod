'''
set Locations;
set NoFlyZone;
param N = card{Locations};
param coord_x{Locations};
param coord_y{Locations};
param R := 6371;  # Earth's radius in kilometers
param dist{Locations,Locations} >=0;
param SecurityRisk {Locations, Locations} >= 0;

var x{i in Locations, j in Locations} binary;
var u{i in Locations} integer >= 0; # MTZ constraints to eliminate sub tours

minimize FO: sum {i in Locations, j in Locations: i<>j} dist[i, j] * x[i, j] +
             sum {i in Locations, j in Locations:i<>j} SecurityRisk[i, j] * x[i, j];
subject to 
       arrive_once {i in Locations diff NoFlyZone}: sum {j in Locations: i <> j}  x[i, j] = 1;
       leave_once  {j in Locations diff NoFlyZone}: sum {i in Locations: i <> j}  x[i, j] = 1;
       departfrom: sum{j in Locations} x[1,j] = 1;
       returnto:   sum{j in Locations} x[j,1] = 1;
       NoFlyConstraint {i in NoFlyZone, j in Locations: i != j}: x[i, j] = 0;
       NoFlyConstraint2 {i in Locations, j in NoFlyZone: i != j}: x[i, j] = 0;
       subtour_elimination{i in 2..N, j in 2..N: i!=j}: u[i] - u[j] + N*x[i,j] <= N-1;
data;

set Locations := 1 2 3 4 5 6 7 8 9;
set NoFlyZone := 3;

param dist:
       1   2       3       4       5       6       7       8       9 :=
1      0   2.80989 4.46701 4.81949 5.90354 7.98288 9.70035 8.50345 12.889
2      2.80989 0 6.33963 6.11504 6.29523 9.95868 12.4854 11.1073 15.6707
3      4.46701 6.33963 0 1.34337 3.39363 3.6242 7.78322 5.49074 12.0743
4      4.81949 6.11504 1.34337 0 2.05039 4.11564 9.06861 6.64763 13.408
5      5.90354 6.29523 3.39363 2.05039 0 5.47397 11.065 8.53267 15.4503
6      7.98288 9.95868 3.6242 4.11564 5.47397 0 6.73789 3.84118 11.4155
7      9.70035 12.4854 7.78322 9.06861 11.065 6.73789 0 2.90363 4.67911
8      8.50345 11.1073 5.49074 6.64763 8.53267 3.84118 2.90363 0 7.58242
9      12.889 15.6707 12.0743 13.408 15.4503 11.4155 4.67911 7.58242 0;


param coord_x :=
    1 -27.671422137162196
    2 -27.675930258082644
    3 -27.615609439201847
    4 -27.60659198856831
    5 -27.593260258436075
    6 -27.578913616488954
    7 -27.636479362331634
    8 -27.610134265333556
    9 -27.677998240992387
    ;
    
    # ;
    # [-48.540577179137415, -27.671422137162196],
    # [-48.56566790514921, -27.675930258082644],
    # [-48.52509636671357, -27.615609439201847],
    # [-48.53558784624806, -27.60659198856831],
    # [-48.55176243236028, -27.593260258436075],
    # [-48.50346749120868, -27.578913616488954],
    # [-48.45649179749506, -27.636479362331634],
    # [-48.4758534389978, -27.610134265333556],
    # [-48.42475106534704, -27.677998240992387]

param coord_y :=
    1 -48.540577179137415
    2 -48.56566790514921
    3 -48.52509636671357
    4 -48.53558784624806
    5 -48.55176243236028
    6 -48.50346749120868
    7 -48.45649179749506
    8 -48.4758534389978
    9 -48.42475106534704
;

param SecurityRisk:
   1   2   3   4   5   6   7   8   9 :=
1  .   3   2   1   4   5   6   7   8
2  3   .   2   1   3   4   5   6   7
3  2   2   .   4   2   1   3   4   5
4  1   1   4   .   1   2   3   4   5
5  4   3   2   1   .   5   4   3   2
6  5   4   1   2   5   .   2   1   4
7  6   5   3   4   4   2   .   3   1
8  7   6   4   3   3   1   3   .   2
9  8   7   5   5   2   4   1   2   .
;
'''
