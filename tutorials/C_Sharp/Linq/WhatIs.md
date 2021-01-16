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

## Basic Where Abfrage
Array mit den Daten für die Beispiele: 
```cs
int[] example = new int[10] { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
```
### Query Syntax
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
### Method Syntax
```cs
[Datentyp] [Variable] = [Datenquelle].Where([Daten] => [Daten] < 5);
```
```cs
//Selected alle Werte aus dem Array example welche kleiner 5 sind
var method = example.Where(ex => ex < 5);
```

## Mehrere Where Abfragen
### Query Syntax
```cs
[Datentyp] [Variable] = from [Daten] in [Datenquelle]
                        where [Bedingung 1]
                        where [Bedingung 2]
                        select [Daten];
```
```cs
//Selected alle Werte aus dem Array example welche kleiner 5 und größer als 8 sind
var query = from ex in example
            where ex < 5
            where ex > 8
            select ex;
```
### Method Syntax
```cs
[Datentyp] [Variable] = [Datenquelle].Where([Daten] => [Daten] < 5).Where([Daten] => [Daten] > 5);
```
```cs
//Selected alle Werte aus dem Array example welche kleiner 5 und größer als 8 sind
var method = example.Where(ex => ex < 5).Where(ex => ex > 8);
```

## Über Abfragen Sortieren
Um mit Linq Daten zu sortieren gibt es mehrere Funktionen.
+ OrderBy
    + Sortiert über einen bestimmten Wert (aufsteigend)
+ OrderByDescending
    + Sortiert über einen bestimmten Wert (absteigend)
+ ThenBy
    + Sortiert über einen zweiten Wert (aufsteigend)
+ ThenByDescending
    + Sortiert über einen zweiten Wert (absteigend)
+ Reverse
    + Sortiert in umgekehrter Reihenfolge

Hierbei ist jedoch zu bedenken, dass über die Query Syntax nur "OrderBy" verfügbar ist.

Liste für die Abfragen
```cs
IList<User> userList = new List<User> {
    new User() { UserID = 1, UserName = "Paul", Age=22 },
    new User() { UserID = 2, UserName = "Moritz", Age=26 },
    new User() { UserID = 3, UserName = "Florian", Age=23 },
    new User() { UserID = 4, UserName = "Nico", Age=21 },
    new User() { UserID = 5, UserName = "Lisa", Age=19 },
    new User() { UserID = 6, UserName = "Davis", Age=23 }
}
```
## OrderBy
### Query Syntax
```cs
//Sortiert die Werte nach dem Namen
var query = from ex in userList
            orderby ex.UserName
            select ex;
```
### Method Syntax
