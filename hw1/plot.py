import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("feigin2014_table1_mortality.csv", sep=",", header=0)

age_groups = ["<75", ">=75", "all"]
titles = ["Age <75", "Age >= 75", "All ages"]
years = [1990, 2005, 2010]
income_groups = ["high", "low_and_middle", "all"]
labels = ["High", "Low & Middle", "Global"]
colors = ["blue", "orange", "gray"]
shifts = [-0.5, 0, 0.5] # small x-shift (in years) so error bars don't completely overlap
ticks = [20, 25, 30, 40, 50, 60, 80, 100, 120, 150, 1000, 1200, 1500, 2000, 2500, 3000] # used for the log scale (got from looking a the scales in 10^x form)

fig, axes = plt.subplots(1, 3, figsize=(12, 5))

for ax, age, title in zip(axes, age_groups, titles):
    for inc, label, color, shift in zip(income_groups, labels, colors, shifts):
        d = df[(df["age_group"] == age) & (df["income_group"] == inc)]
        x = d["year"] + shift
        y = d["mortality_rate"]
        lower = y - d["interval_low"] # distance from mortality_rate down to interval_low
        upper = d["interval_high"] - y  # distance from mortality_rate up to interval_high
        ax.plot(x, y, color=color)
        ax.errorbar(x, y, yerr=[lower, upper], fmt="o", color=color,
                    markerfacecolor=color, capsize=4, label=label)
        
    # log y-axis with plain-number tick labels (instead of 10^x)
    ax.set_yscale("log")
    ax.set_yticks(ticks, labels=ticks) # ticks outside a panel's range are skipped
    ax.minorticks_off()            
    ax.autoscale(axis="y") # shrink the axis back to this panel's data

    ax.set_title(title)
    ax.set_xticks(years)
    ax.set_xlabel("Year")
    ax.grid(axis="y", alpha=0.3)

axes[0].set_ylabel("Age-adjusted mortality rate\n(per 100,000 person-years in log scale)")
axes[-1].legend(title="Income group")
fig.tight_layout()
plt.savefig("figure.png")