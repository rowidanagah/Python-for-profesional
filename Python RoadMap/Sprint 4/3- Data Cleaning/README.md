## What ’re the methods that you used ?

- dropna()

- fillna() 

- MinMaxScaler()

- where()

- to_datetime()

- decode()

## Explain each method ..


- dropna() -> DataFrame
    - ***Syntax*** : `DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)`.
    - ***Parameters*** : **axis** or *****how***** ,  *****thresh***** , *****subset***** and *****inplace***** .
        - axis : {0 or ‘index’, 1 or ‘columns’}, default 0
        - how : {‘any’, ‘all’}, default ‘any’ Drop the rows where all | any elements are missing.
        - thresh : (int (N), optional) Keep only the rows with at least N non-NA values.
        - subset : (array-like, optional) to Define in which columns to look for missing values.
        - inplace : (int, optional) Keep the DataFrame with valid entries in the same variable.
    - ***Returns*** : DataFrame with NA entries dropped from it.


- fillna() -> DataFrame or None
    - ***Syntax*** : ` DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)`.
    - ***Parameters*** : **value** or *****method*****,*****axis***** , *****limit*****, ***downcast*** and **inplace** .
        - value : valuescalar, dict, Series, or DataFrame
        - method : {‘backfill’, ‘bfill’, ‘pad’, ‘ffill’, None}, default None
        - axis : axis{0 or ‘index’, 1 or ‘columns’}
        - limit :( int, default None).
        - inplace : inplacebool, default False.
        - downcast : (dict, default is None)
    - ***Returns*** : Object with missing values filled or None if inplace=True.


- MinMaxScaler() -> DataFrame or None
    - ***Syntax*** : `sklearn.preprocessing.MinMaxScaler(feature_range=(0, 1), *, copy=True)`.
    - ***Parameters*** : **feature_range** and ****copy**** .
        - feature_range : (tuple (min, max), default=(0, 1))  Desired range of transformed data.
        - copy : (bool default=True , optional) Set to False to perform inplace row normalization and avoid a copy 
    - X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
    - X_scaled = X_std * (max - min) + min
    - ***Returns*** : Object with missing values filled or None if inplace=True.


- where() -> DataFrame or None
    - ***Syntax*** : `numpy.where(condition[, x, y])`.
    - ***Parameters*** : **condition** and ****x, y**** .
        - ***condition*** : When True, yield x, otherwise yield y.
        - ***x, y*** : Values from which to choose. x, y and condition need to be broadcastable to some shape.
    - ***Returns*** : the indices of elements in an input array where the given condition is satisfied.

- to_datetime() -> Date time object series .
    - ***Syntax*** : `.to_datetime(arg, errors=’raise’, dayfirst=False, yearfirst=False, utc=None, box=True, format=None, 		     exact=True, unit=None, infer_datetime_format=False, origin=’unix’, cache=False) `.
    - ***Parameters*** : ***arg*** , ***dayfirst*** , ***yearfirst*** , ***utc*** and ***format*** .
        - ***arg*** :An integer, string, float, list or dict object to convert in to Date time object.
        - ***dayfirst*** : Boolean value, places day first if True.
        - ***yearfirst*** : Boolean value, places year first if True.
        - ***utc*** :Boolean value, Returns time in UTC if True.
        - ***format*** : String input to tell position of day, month and year.
    - convert string Date time into Python Date time object.
    - ***Returns*** : Date time object series .


- decode() -> str
    - ***Syntax*** : `decode(encoding, error)`.
    - ***Parameters*** : **encoding** and ****error**** .
        - ***encoding*** : Specifies the encoding on the basis of which decoding has to be performed..
        - ***error*** : Decides how to handle the errors if they occur, e.g ‘strict’ raises Unicode error in case 
                    exception and ‘ignore’ ignores the errors occurred
    - ***Returns*** : the original string from the encoded string.


## What’s new for you ?
- FuzzyWuzzy Python library
- Parameters of the whole content


## Resources ? 
- [pandas documentation about dropna ](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html)
- [pandas documentation about MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html)
- [Geek for Geek tutorial about todatatime](https://www.geeksforgeeks.org/python-pandas-to_datetime/)

