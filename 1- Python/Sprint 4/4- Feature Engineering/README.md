## What ’re the methods that you used ?

- query

- assign

- add_suffix

## Explain each method ..


-

- query() -> DataFrame 
    - ***Syntax*** : `DataFrame.query(expr, inplace=False, **kwargs)`.
    - ***Parameters*** : **expr** or *****inplace***** and **kwargs** .
        - str : The query string to evaluate.
        - innplace : (bool , optional) if the query should modify the data in place or return a modified copy.        
    - ***Returns*** : DataFrame after modification

- assign() -> DataFrame
	- ***Syntax***: `DataFrame.assign(**kwargs)`
	- ***Parameters*** : **kwargs** 
    - ***Returns*** : new DataFrame with the new columns in addition to all the existing columns.


- add_suffix() -> DataFrame or Series
	- ***Syntax***: `Series.add_suffix(suffix)`
	- ***Parameters*** : **suffix**
	    - suffix (str) : The string to add after each label.
    - ***Returns*** : New Series or DataFrame with updated labels.



## What’s new for you ?
- 

## Resources ? 
- [pandas documentation about Query](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html)

- [pandas documentation about Query](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.assign.html)

- [scikit-learn documentation about LabelEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html)

- [scikit-learn documentation about LabelEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html)

- [pandas  documentation about rolling](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.rolling.html)