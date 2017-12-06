

|							|								|
|:----------------------------:|:----------------------------------:|
|		Student				|			Appari Lalith			|
| 		Student roll number	| 20161038						|
| 		Code review of 		| Bomberman/1					|
| 		Bugs identified		| 6		 						|


|		Bug Number			|	Description		 	|
|:--------------------------:|:--------------------:|
|		  1    				| Enemy can't identify the bomb 	|
|		  2					| Board array is not private		|
|		  3					| Bricks array is not private		|
|		  4					| Del method of an Enemy is not private |
|		  5					| Del method of an Bomb is not private	|
|		  6					| When enemy overlaps with the bomb and the bomb explodes the bomb is not removed from  that position|

|		Code smell			|	Description		 	|
|:--------------------------:|:--------------------:|
|		  Missing-docstring    			| Missing module docstring			|
|		  Unused-import				| Unnnecessary import of a module		|
|		  Superfluous-parens			| Unnecessary parens after 'if' keyword		|
|		  Invalid-name				| Invalid constant or attribute or argument name|
|		  Attribute-defined-outside-init	| Attribute  defined outside __init__ ()	|
|		  Too-few-public-methods)		| Too few public methods 			|
|		Unneeded-not				| Changing "not type() is int" to "type() is not int"	|	
|		Unidiomatic-typecheck			|  Using type() instead of isinstance() for a typecheck. |
|		No-self-use				| Method could be a function 			|
|		Unused-variable				| Unused variable |
|		Wrong-import-order			| Standard import order not followed |
|		Wildcard-import				| Wildcard import not advised|
|		Too-many-instance-attributes		| Too many instance attributes|
|		Protected-access			| Access to a protected member _del_ of a client class |
|		Too-many-nested-blocks			| Too many nested blocks	|
|		Too-many-branches			| Too many nested blocks	|	
|		Too-many-statements			| Too many statements |
|		Redefined-outer-name			| Redefining name 'sys' from outer scope |
|		Reimported				| Module reimported|
|		No-member				| Instance of 'Person' has no 'populate' member |

Report
======
```bash
396 statements analysed.
```

Statistics by type
------------------
```bash
+---------+-------+
|type     |number |
+=========+=======+
|module   |7      |
+---------+-------+
|class    |9      |
+---------+-------+
|method   |32     |
+---------+-------+
|function |2      |
+---------+-------+
```



Messages
--------
```bash
+-------------------------------+------------+
|Code smell                     |occurrences |
+===============================+============+
|invalid-name                   |65          |
+-------------------------------+------------+
|superfluous-parens             |58          |
+-------------------------------+------------+
|unused-wildcard-import         |43          |
+-------------------------------+------------+
|missing-docstring              |35          |
+-------------------------------+------------+
|unused-import                  |12          |
+-------------------------------+------------+
|wildcard-import                |9           |
+-------------------------------+------------+
|wrong-import-order             |7           |
+-------------------------------+------------+
|no-self-use                    |4           |
+-------------------------------+------------+
|unused-argument                |3           |
+-------------------------------+------------+
|too-few-public-methods         |3           |
+-------------------------------+------------+
|too-many-nested-blocks         |2           |
+-------------------------------+------------+
|duplicate-code                 |2           |
+-------------------------------+------------+
|attribute-defined-outside-init |2           |
+-------------------------------+------------+
|unused-variable                |1           |
+-------------------------------+------------+
|unneeded-not                   |1           |
+-------------------------------+------------+
|unidiomatic-typecheck          |1           |
+-------------------------------+------------+
|undefined-variable             |1           |
+-------------------------------+------------+
|too-many-statements            |1           |
+-------------------------------+------------+
|too-many-instance-attributes   |1           |
+-------------------------------+------------+
|too-many-branches              |1           |
+-------------------------------+------------+
|reimported                     |1           |
+-------------------------------+------------+
|redefined-outer-name           |1           |
+-------------------------------+------------+
|protected-access               |1           |
+-------------------------------+------------+
|pointless-string-statement     |1           |
+-------------------------------+------------+
|no-member                      |1           |
+-------------------------------+------------+
|function-redefined             |1           |
+-------------------------------+------------+
```


