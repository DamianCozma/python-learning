## School Catalogue

This project creates a digital school catalog for the New York City Department of Education. It includes classes for primary and high schools, all inheriting from a parent `School` class.

### Classes

**School**
- **Properties**: `name` (string), `level` ('primary', 'middle', or 'high'), `numberOfStudents` (integer)
- **Getters**: `get_name()`, `get_level()`, `get_numberOfStudents()`
- **Setters**: `set_numberOfStudents(new_number)`
- **Methods**: `__repr__()` displays `A {level} school named {name} with {numberOfStudents} students`

**PrimarySchool (inherits from School)**
- **Additional Property**: `pickupPolicy` (string, e.g., "Pickup after 3pm")
- **Getters**: `get_pickupPolicy()`
- **Methods**: `__repr__()` displays the school info and pickup policy

**HighSchool (inherits from School)**
- **Additional Property**: `sportsTeams` (list of strings, e.g., ['basketball', 'tennis'])
- **Getters**: `get_sportsTeams()`
- **Methods**: `__repr__()` displays the school info and sports teams

**Usage Example:**

```
ps = PrimarySchool("ABC Primary", "Parent pickup only", 300)
print(ps)

hs = HighSchool("XYZ High", 1500, ["basketball", "tennis"])
print(hs)
```
