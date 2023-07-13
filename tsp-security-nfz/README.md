# TSP - Security Risk + NFZ

- [X] Points description
|Nr.|Points| Latitude  | Longitude |Description|NFZ|
|--|-|-----------|-----------|-|-|
|1|A| -27.59326 | -48.55176 |Metropolitan Area.|-|
|2|B| -27.60659 | -48.53559 |Neighborhood with less orderly urban planning.|-|
|3|C| -27.57891 | -48.50347 |Remote residential area.|-|
|4|D| -27.61561 | -48.52510 |Industrial zone.|-|
|5|E| -27.67142 | -48.54058 |Integration with the airport area.|X|
|6|F| -27.67593 | -48.56567 |Florianopolis Air Base.|X|
|7|G| -27.63648 | -48.45649 |Beach area with potential drone support|-|
|8|H| -27.61013 | -48.47585 |Conflict area in popular tourist routes frequented by helicopters|-|
|9|I| -27.67799 | -48.42475 |Maritime monitoring area and product delivery to offshore platforms|-|

- [X] Points in Map
```geojson
{"type":"FeatureCollection","features":[{"type":"Feature","properties":{"descrição":"Integração com área de aeroporto","letra":"e"},"geometry":{"coordinates":[-48.540577179137415,-27.671422137162196],"type":"Point"},"id":0},{"type":"Feature","properties":{"descrição":"Base Aérea de Florianópolis - 2º Esquadrão do 7º Grupo de Aviação","letra":"f"},"geometry":{"coordinates":[-48.56566790514921,-27.675930258082644],"type":"Point"},"id":1},{"type":"Feature","properties":{"descrição":"área industrial","letra":"d"},"geometry":{"coordinates":[-48.52509636671357,-27.615609439201847],"type":"Point"}},{"type":"Feature","properties":{"descrição":"bairro não tão perto da cidade","letra":"b"},"geometry":{"coordinates":[-48.53558784624806,-27.60659198856831],"type":"Point"}},{"type":"Feature","properties":{"descrição":"área metropolitana","letra":"a"},"geometry":{"coordinates":[-48.55176243236028,-27.593260258436075],"type":"Point"}},{"type":"Feature","properties":{"descrição":"bairro afastado","letra":"c"},"geometry":{"coordinates":[-48.50346749120868,-27.578913616488954],"type":"Point"}},{"type":"Feature","properties":{"descrição":"área de praia com possível apoio","letra":"g"},"geometry":{"coordinates":[-48.45649179749506,-27.636479362331634],"type":"Point"},"id":6},{"type":"Feature","properties":{"descrição":"Conflitos em rotas turísticas populadas por helicópteros","letra":"h"},"geometry":{"coordinates":[-48.4758534389978,-27.610134265333556],"type":"Point"}},{"type":"Feature","properties":{"descrição":"Monitoramento marítimo e entrega de produtos em plataforma de petróleo","letra":"i"},"geometry":{"coordinates":[-48.42475106534704,-27.677998240992387],"type":"Point"},"id":8}]}
```

- [X] Distance Matrix

|   |   1    |   2    |   3    |   4    |   5    |   6    |   7    |   8    |   9    |
|---|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 1 |   0    | 2.049  | 5.473  | 3.391  | 5.887  | 6.277  | 11.06  | 8.532  | 15.44  |
| 2 | 2.049  |   0    | 4.112  | 1.342  | 4.805  | 6.102  | 9.067  | 6.647  | 13.4   |
| 3 | 5.473  | 4.112  |   0    | 3.618  | 7.965  | 9.943  | 6.73   | 3.837  | 11.4   |
| 4 | 3.391  | 1.342  | 3.618  |   0    | 4.456  | 6.33   | 7.782  | 5.49   | 12.07  |
| 5 | 5.887  | 4.805  | 7.965  | 4.456  |   0    | 2.81   | 9.698  | 8.496  | 12.89  |
| 6 | 6.277  | 6.102  | 9.943  | 6.33   | 2.81   |   0    | 12.48  | 11.1   | 15.67  |
| 7 | 11.06  | 9.067  | 6.73   | 7.782  | 9.698  | 12.48  |   0    | 2.9    | 4.673  |
| 8 | 8.532  | 6.647  | 3.837  | 5.49   | 8.496  | 11.1   | 2.9    |   0    | 7.572  |
| 9 | 15.44  | 13.4   | 11.4   | 12.07  | 12.89  | 15.67  | 4.673  | 7.572  |   0    |

- [X] Security Risk Matrix 
Here's the table in Markdown format:

|    |   1 |   2 |   3 |   4 |   5 |   6 |   7 |   8 |   9 |
|----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|  1 |   . |   3 |   2 |   1 |   4 |   5 |   6 |   7 |   8 |
|  2 |   3 |   . |   2 |   1 |   3 |   4 |   5 |   6 |   7 |
|  3 |   2 |   2 |   . |   4 |   2 |   1 |   3 |   4 |   5 |
|  4 |   1 |   1 |   4 |   . |   1 |   2 |   3 |   4 |   5 |
|  5 |   4 |   3 |   2 |   1 |   . |   5 |   4 |   3 |   2 |
|  6 |   5 |   4 |   1 |   2 |   5 |   . |   2 |   1 |   4 |
|  7 |   6 |   5 |   3 |   4 |   4 |   2 |   . |   3 |   1 |
|  8 |   7 |   6 |   4 |   3 |   3 |   1 |   3 |   . |   2 |
|  9 |   8 |   7 |   5 |   5 |   2 |   4 |   1 |   2 |   . |


![image](https://github.com/avelin0/Operational-Research/assets/12461215/3c5f5616-a1dc-414a-97fe-324407eab168)

- [X] Solutions
Aleatory 1:
(1,4),(4,7),(7,9),(9,2),(2,3),(3,8),(8,1) 
dist = 45.727
risk = 25

Aleatory 2:
(1,3),(3,4),(4,9),(9,7),(7,2),(2,8),(8,1)
dist = 50.08
risk = 30

Minimizing only risk: 
(1,2),(2,3),(3,7),(7,9),(9,8),(8,4),(4,1)
dist = 34.407
risk = 15

Minimizing only distance:
dist = 33.344
risk = 19

Multi-objective Optimum value:
(1,3),(3,7),(7,9),(9,8),(8,4),(4,2),(2,1)
dist = 33.329
risk = 15

