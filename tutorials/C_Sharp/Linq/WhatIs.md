# Was ist Linq?
Linq steht für **L**anguage **In**tegrated **Q**uery und ist dafür da um Daten aus verschiedenen Quellen zu verarbeiten.

Die möglichen Datenquellen sind:
+ Arrays
+ Listen
+ Relationale Datenbanken
+ XML Dokumente
+ Excel Dokumente (ja sogar Excel)

## Warum Linq?
Linq bietet den Vorteil, dass mit einer Technologie viele verschiedene (und auch verbreitete) Datenquellen gleich genutzt werden können. Zusätzlich ist es durch die Query Syntax sehr leicht für Personen mit SQL Kenntnissen sich hineinzuarbeiten.

### Arten von Linq:
+ Query Syntax
+ Method Syntax

## Linq Beispiele
Array mit den Daten für die Beispiele: 
```cs
int[] example = new int[10] { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
```

## Basic Abfrage
+ ### Query Syntax
```cs
[Datentyp] [Variable] = from [Daten] in [Datenquelle]
                        where [Bedingung]
                        select [Daten];
```
```cs
//Selected alle Werte aus dem Array example welche kleiner 5 sind
var query = from ex in example
            where ex < 5
            select ex;
```
+ ### Method Syntax
```cs
[Datentyp] [Variable] = [Datenquelle].Where([Daten] => [Daten] < 5);
```
```cs
//Selected alle Werte aus dem Array example welche kleiner 5 sind
var method = example.Where(ex => ex < 5);
```
