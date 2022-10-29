
## What ’re the methods that you used ?

- figure

- subplots


## Explain each method ..

- figure()
    - ***Syntax*** : `plt.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None,frameon=True,  
                      FigureClass=<class 'matplotlib.figure.Figure'>, clear=False, **kwargs)[source]`.
    - ***Parameters*** : **num** , **figsize** , **dpi** , **facecolor** , **edgecolor** , **frameon** , **frameon**  ,
        -  **FigureClass** , **clearbool** , **tight_layout**
        - ***name *** : (int or str, optional) to identify the figure .
        - ***figsize*** : (float, float), (default:[6.4,4.8])Width, height in inches.
        - ***dpi*** : (float , optional )(default: 100.0) the resolutionof the figure
        - ***facecolor*** : (color , optional) (default : 'white')  the background color.
        - ***edgecolor*** : (color , optional) (default : 'white') The border color
        - ***frameon*** : (bool,optional)(default: True) if False , suppress drawing the figure frame.
        - **FigureClass** : To optionally use a custom Figure instance. subclass of the used figure.
        - **clearbool** : (bool , optional) default: False if True , then color the figure .
    - To Create a new figure, or activate an existing figure.


- subplots()
    - ***Syntax*** : `matplotlib.pyplot.subplots(nrows=1, ncols=1, sharex=False, sharey=False,squeeze=True, 
                      subplot_kw=None, gridspec_kw=None, **fig_kw)`.
    - ***Parameters*** : **nrows,ncols ** , **sharex** , **sharey** , **squeeze** , **subplot_kw** and **gridspec_kw** 
        - **nrows, ncols ** : (int, optional) default: 1, Number of rows/columns of the subplot grid.
        - ***sharex & sharey*** :   bool or {'none', 'all', 'row', 'col'}, default: False
        - ***squeeze*** : (bool, optional) default: True 
        - ***num*** :( int or string, optional), default: None.keyword that sets the figure number or label
        - ***subplot_kw*** : (dic ,optional)Dict with keywords passed to the add_subplot call used to create each subplot.
        - ***frameon*** :(dict, optional) Dict with keywords passed to the GridSpec constructor used to create the grid                     the subplots are placed on.
    - To Create a figure and a set of subplots.





## What’s new for you ?
- parameters of the whole content

## Resources ? 
- [seasorn documentation about lineplot](https://seaborn.pydata.org/generated/seaborn.lineplot.html)
- [seasorn documentation about subplots](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplots.html)
