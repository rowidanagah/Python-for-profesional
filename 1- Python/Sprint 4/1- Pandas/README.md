## What ’re the methods that you used ?

- DataFrame()

- Series()

- value_counts()

- idxmax()

- set_index()

- set_option () 

## Explain each method ..

- DataFrame()
    - 2D size, mutable and labeld tabular data with 3 principal components, the ***data***, ***rows***, and ***columns*** 
    - ***Syntax*** : `pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False) `.
    - ***Parameters*** : **data** or *****index***** ,  *****columns***** , *****dtype***** and *****copy***** .
        - data : could be list , dic ,list of dics or loading an existing storage data as a csv , sql or excel file.
        - index : (optional)if no index is passed, then by default, index will be range(n) where n is the array length.
        - columns : Column labels to use for resulting frame. Will default to RangeIndex (0, 1, 2, …, n) if no column  l          labels are provided.
        - dtype : Data type to force. Only a single dtype is allowed. If None, infer.
        - copy : Copy data from inputs. Only affects DataFrame / 2d ndarray input.
    - ***Returns*** :  dataframe object
    - data takes various forms like ndarray, series, map, lists, dict, constants and also another DataFrame.

- Series()
    - 1D size, mutable and labeld array capable of holding data of any type
    - ***Syntax*** :`pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)`.
    - ***Parameters*** : **data** or *****index***** ,  *****columns***** , *****dtype***** and *****copy***** .
        - data : array-like, Iterable, dict, or scalar value .
        - index : array-like or Index 
        - dtype : Data type to force. Only a single dtype is allowed. If None, infer.
        - name : (str, optional) The name to give to the Series.
        - copy :( bool, default False ) Copy input data.
    - ***Returns*** : pandas.core.series.Series
    - data takes various forms like ndarray, series, map, lists, dict, constants and also another DataFrame.

The name to give to the Series.

- value_counts() -> Series
    - ***Syntax*** : `Series.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)`.
    - ***Parameters*** : **normalize** or *****sort***** ,  *****ascending***** , *****bins***** and *****dropna***** .
        - normalize :(bool) If True then the object returned will contain the relative frequencies of the unique values .
        - sort : (bool ,optional) Sort by values.
        - ascending : (bool ,optional) Sort in ascending order.
        - dropna : Don’t include counts of NaN.
        - bins : (int, optional) Rather than count values, group them into half-open bins
    - ***Returns*** :  Return a Series containing counts of unique values.


- idxmax () -> int
    - ***Syntax*** : `DataFrame.idxmax(axis=0, skipna=True)`.
    - ***Parameters*** : **axis** and *****skipna***** .
        - normalize : (optional) The axis to use. 0 or ‘index’ for row-wise, 1 or ‘columns’ for column-wise.
        - skipna :(skipnabool, default True) Exclude NA/null values. If an entire row/column is NA, the result will be NA.
    - ***Returns*** : Return index of first occurrence of maximum over requested axis.
    - ****Raise ValueError**** : If the row/column is empty .


- set_index () -> int
    - It is a method to set a List, Series or Data frame as index of a Data Frame. 
    - ***Syntax*** : `DataFrame.set_index(keys, drop=True, append=False, inplace=False, verify_integrity=False)`.
    - ***Parameters*** : **axis** and *****skipna***** .
        - keys: Column name or list of column name.
        - drop: ( boolen, optional) value which drops the column used for index if True.
        - verify_integrity: Checks the new index column for duplicates if True.
        - append:(bool , optional) Appends the column to existing index column if True.
        - ***inplace***: (bool , optional) Makes the changes in the dataframe if True.

- set_option () -> int
    - It is a method to set a List, Series or Data frame as index of a Data Frame. 
    - ***Syntax*** : `pandas.set_option(pat, value) `.
    - ***Parameters*** : **pat** and *****value***** .
        - pat: (str) Regexp which should match a single option
        - drop: ( object) New value of option.
    - ***Returns*** : None
    - ****Raise ValueError**** : Raises OptionError if no such option exists

## What’s new for you ?
- to_csv()
- set_index()
- set_option()


## Resources ? 

- [pandas documentation about DataFrame](https://docs.python.org/3.7/library/re.html)
- [pandas documentation about Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html)
- [pandas documentation about read_scv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_scv.html)
- [pandas documentation about te_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_csv.html)
- [pandas documentation about valeu_counts](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html)
- [pandas documentation about idxmax](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.idxmax.html)
- [Geek for Geeks tutorial about set_index](https://www.geeksforgeeks.org/python-pandas-dataframe-set_index/)

