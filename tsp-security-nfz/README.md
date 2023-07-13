# TSP - Security Risk + NFZ

Here's the coordinates table in Markdown format:

|Points|-| Latitude  | Longitude |
|--|-|-----------|-----------|
|1|E| -27.67142 | -48.54058 |
|2|F| -27.67593 | -48.56567 |
|3|D| -27.61561 | -48.52510 |
|4|B| -27.60659 | -48.53559 |
|5|-| -27.59326 | -48.55176 |
|6|-| -27.57891 | -48.50347 |
|7|-| -27.63648 | -48.45649 |
|8|-| -27.61013 | -48.47585 |
|9|-| -27.67799 | -48.42475 |


```geojson
{"type":"FeatureCollection","features":[{"type":"Feature","properties":{"descrição":"Integração com área de aeroporto","letra":"e"},"geometry":{"coordinates":[-48.540577179137415,-27.671422137162196],"type":"Point"},"id":0},{"type":"Feature","properties":{"descrição":"Base Aérea de Florianópolis - 2º Esquadrão do 7º Grupo de Aviação","letra":"f"},"geometry":{"coordinates":[-48.56566790514921,-27.675930258082644],"type":"Point"},"id":1},{"type":"Feature","properties":{"descrição":"área industrial","letra":"d"},"geometry":{"coordinates":[-48.52509636671357,-27.615609439201847],"type":"Point"}},{"type":"Feature","properties":{"descrição":"bairro não tão perto da cidade","letra":"b"},"geometry":{"coordinates":[-48.53558784624806,-27.60659198856831],"type":"Point"}},{"type":"Feature","properties":{"descrição":"área metropolitana","letra":"a"},"geometry":{"coordinates":[-48.55176243236028,-27.593260258436075],"type":"Point"}},{"type":"Feature","properties":{"descrição":"bairro afastado","letra":"c"},"geometry":{"coordinates":[-48.50346749120868,-27.578913616488954],"type":"Point"}},{"type":"Feature","properties":{"descrição":"área de praia com possível apoio","letra":"g"},"geometry":{"coordinates":[-48.45649179749506,-27.636479362331634],"type":"Point"},"id":6},{"type":"Feature","properties":{"descrição":"Conflitos em rotas turísticas populadas por helicópteros","letra":"h"},"geometry":{"coordinates":[-48.4758534389978,-27.610134265333556],"type":"Point"}},{"type":"Feature","properties":{"descrição":"Monitoramento marítimo e entrega de produtos em plataforma de petróleo","letra":"i"},"geometry":{"coordinates":[-48.42475106534704,-27.677998240992387],"type":"Point"},"id":8}]}
```

Distance Matrix
|    |   1 |      2 |      3 |      4 |      5 |      6 |      7 |      8 |      9 |
|----|-----|--------|--------|--------|--------|--------|--------|--------|--------|
|  1 |   0 | 2.8099 | 4.467  | 4.8195 | 5.9035 | 7.9829 | 9.7004 | 8.5035 | 12.889 |
|  2 | 2.8099 |      0 | 6.3396 | 6.115  | 6.2952 | 9.9587 | 12.485 | 11.107 | 15.671 |
|  3 | 4.467  | 6.3396 |      0 | 1.3434 | 3.3936 |  3.624 | 7.7832 | 5.4907 | 12.074 |
|  4 | 4.8195 |  6.115 | 1.3434 |      0 | 2.0504 | 4.1156 | 9.0686 | 6.6476 | 13.408 |
|  5 | 5.9035 | 6.2952 | 3.3936 | 2.0504 |      0 | 5.474  | 11.065 | 8.5327 | 15.450 |
|  6 | 7.9829 | 9.9587 |  3.624 | 4.1156 | 5.4739 |      0 | 6.7379 | 3.8412 | 11.416 |
|  7 | 9.7004 | 12.485 | 7.7832 | 9.0686 |  11.065 | 6.7379 |      0 | 2.9036 | 4.6791 |
|  8 | 8.5035 | 11.107 | 5.4907 | 6.6476 | 8.5327 | 3.8412 | 2.9036 |      0 | 7.5824 |
|  9 | 12.889 | 15.671 | 12.074 | 13.408 |  15.450 | 11.416 | 4.6791 | 7.5824 |      0 |


Security Risk Matrix 
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

