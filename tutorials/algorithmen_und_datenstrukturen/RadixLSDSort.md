# Radix LSD Sort

Radixsort benötigt zwischen allen Zeichen des Alphabets eine Total- bzw. Quasiordnung.

Laufzeit: O(n * l)  
Zusätzlicher Speicherbedarf: O(n)  
Stabil: ja

> Hinweis: l ist die Länge der Stellen des größten Elements zur entsprechenden Basis 

## implementation

> Hinweis: Die nachfolgenden Algorithmen ermöglichen es nur natürliche Zahlen zu sortieren 

### Mit Listen

Es gibt 2 Phasen, in der Partitionierung werden die Zahlen entsprechenden Partitionen zugeordnet entsprechend der Stelle, die betrachtet wird. In der Sammelphase werden dann die Partitionen in aufsteigender Ordnung in der wieder zu einer Liste zusammengefügt wobei die Reihenfolge in der Partition selbst nicht verändert wird. 

Beispiel mt einer zahl zur Basis 10:  
Runde 1: 012<ins>3</ins> => 4 Partition  
Runde 2: 01<ins>2</ins>3 => 3 Partition  
Runde 3: 0<ins>1</ins>23 => 2 Partition  
Runde 4: <ins>0</ins>123 => 1 Partition  

Im folgenden wird die Liste mit Zahlen zur Basis 10 sortiert sortiert:

Liste:
```python
[796, 504, 999, 200, 409, 53, 838, 81, 712, 174]
```

Runde 1: 
```python
[[200], [81], [712], [53], [504, 174],[], [796], [], [838], [999, 409]]  # Partitionierung

[200, 81, 712, 53, 504, 174, 796, 838, 999, 409]  # Sammelphase
```

Runde 2:
```python
[[200, 504, 409], [712], [], [838], [], [53], [], [174], [81], [796, 999]]  # Partitionierung

[200, 504, 409, 712, 838, 53, 174, 81, 796, 999]  # Sammelphase
```

Runde 3:
```python
[[53, 81], [174], [200], [], [409], [504], [], [712, 796], [838], [999]]  # Partitionierung

[53, 81, 174, 200, 409, 504, 712, 796, 838, 999]  # Sammelphase (Ergebnis)
```

Die implementierung ist in den Folgenden Dokumenten zu finden:
- [Binär](./radix_lsd_sort_binary.py)
- [Base10](./radix_lsd_sort_base.py)

### Mit Countingsort

Auch hier gibt es 2 Phasen, hierbei wird in der Zählphase ein Histogramm erstellt welche die Verteilung der Zahlen an der betrachteten Stelle darstellt. Dieses Histogramm wird dann in ein linksseitiges Integral umgewandelt in dem jede Stelle im Histogramm mit der vorherigen addiert wird. Im Anschluss wird in der Sammelphase jedes Element an die finale Position in der Runde mittels des Histogrammintegrals verschoben. Dabei muss nach jedem zugriff auf eine stelle des Histogrammintegral dekrementiert werden da diese Liste von rechts nach links durchlaufen wird. Der wert dient hierbei als Zeiger zum Schreiben des wertes in die jeweilige Position der neuen Liste.

Liste:
```python
[796, 504, 999, 200, 409, 53, 838, 81, 712, 174]
```

Runde 1:
```python
# Zählphase
[1, 1, 1, 1, 2, 0, 1, 0, 1, 2]  # Histogramm 
[1, 2, 3, 4, 6, 6, 7, 7, 8, 10]  # linksseitiges Integral

[200, 81, 712, 53, 504, 174, 796, 838, 999, 409]  # Sammelphase
```

Runde 2:
```python
# Zählphase
[3, 1, 0, 1, 0, 1, 0, 1, 1, 2]  # Histogramm 
[3, 4, 4, 5, 5, 6, 6, 7, 8, 10]  # linksseitiges Integral

[200, 504, 409, 712, 838, 53, 174, 81, 796, 999]  # Sammelphase
```

Runde 3:
```python
# Zählphase
[2, 1, 1, 0, 1, 1, 0, 2, 1, 1]  # Histogramm 
[2, 3, 4, 4, 5, 6, 6, 8, 9, 10]  # linksseitiges Integral

[53, 81, 174, 200, 409, 504, 712, 796, 838, 999]  # Sammelphase (Ergebnis)
```

Die implementierung ist in den Folgenden Dokument zu finden:
- [Countingsort](./radix_lsd_sort_count.py)
