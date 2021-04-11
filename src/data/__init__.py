def data_first_look(df, perc_missing = 0.3):
    ''' print out the shape of a dataframe
        , the percentage of features without missing values,
        and the columns with high missing rates
        INPUT:
        df: Pandas Dataframe
        perc_missing: float only features missing values than this limit are displayed in the plot 
        OUTPUT: 
        Barplot of columns with more than perc_missing*100 values
    '''
    import pandas as pd

    print(f"The dataframe has in total {df.shape[0]} rows and {df.shape[1]} features.\n")

    print("There are the following number of features per type:\n")
    print(df.dtypes.value_counts())
    
    missing_rates = pd.DataFrame(df.isna().mean())\
                    .rename({0:'perc_missing'}, axis=1)\
                    .sort_values('perc_missing', ascending=False)
    print("\n{}% of the features have missing values"\
          .format(round(sum(missing_rates['perc_missing']!=0)*100/len(missing_rates), 2)))

    missing_rates[missing_rates['perc_missing']>perc_missing].plot.bar(title="Missing rates")
