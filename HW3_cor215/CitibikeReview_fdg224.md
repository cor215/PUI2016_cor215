# City bike review - By Felipe (fdg224)

## Null and alternative hypotheses 

Both hypotheses are formulated correctly. There is no confidence level established at the beginning, although at this point there is no hypothesis test designed.

## Data 

Data was processed in a proper manner. The same dataset is loaded into memory twice as *df* and *data*:

~~~~

df = pd.read_csv("PUIDATA/" + datestring + '-citibike-tripdata.csv')

data = pd.read_csv('PUIDATA/201502-citibike-tripdata.csv')

~~~~


Beyond this, the variables needed are kept in the data set and both are the correct type. Age is derived from the year of birth (as the original dataset doesn't provide information for the date of birth, as a proxy of the age of the costumer this is as good  as it can be).

## Hypothesis test

With one continous dependent variable and one dichotomical independent variable (although, an originally continous one) and considering the Null Hypothesis takes tha mean as the main statistic, the best test would be the * Independent Samples t-Test*.

$$ t = \frac{ (\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)}{\sqrt{(s_p^2) (\frac{1}{n_1} \frac{1}{n_2} ) } } $$


