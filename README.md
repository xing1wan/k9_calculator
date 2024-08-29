# Introduction:

The python tool takes csv formated file and generates `Michaelis-Menten` kinetics curves as well as `Vmax` and `Km`.

`Km` is equal to the concentration of the substrate when the rate is half of the maximum velocity. If enzyme A has a lower `Km` than enzyme B, enzyme A has a higher affinity for the substrate under similar conditions.

`Vmax` is the maximum rate of the reaction when the enzyme is fully saturated with substrate. Higher `Vmax` indicates higher maximum catalytic capacities under saturating substrate conditions.

Catalytic Efficiency = `Vmax/Km`, this ratio provides a measure of how efficiently an enzyme converts substrate to product. It combines both the affinity and the catalytic capacity. Higher `Vmax/Km` values suggest better overall catalytic efficiency.

# Usage:

Simply save the input data file `<data.csv>` and the script `k9_calculator.py` in one folder and run the script as:

```python
python3 k9_calculator.py data.csv michaelis_menten_plot.png
```

where `data.csv` is the input file name and `michaelis_menten_plot.png` is the output file name.

# Example plot:

If you run the script with example data file, you should be able to generate the plot below.
![example plot](https://github.com/xing1wan/k9_calculator/blob/cf9f8b8cc4e4c7ab9c60596783bc37782845b7e9/michaelis_menten_plot.png)
