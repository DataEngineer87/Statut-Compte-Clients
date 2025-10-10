#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

def target_encode_smooth(df, col, target, alpha=40):
    df_copy = df[[col, target]].copy()
    classes = df[target].unique()
    global_probas = df[target].value_counts(normalize=True)
    stats = df_copy.groupby(col)[target].value_counts().unstack().fillna(0)
    totals = stats.sum(axis=1)
    encoded = pd.DataFrame(index=df.index)

    for cls in classes:
        n_cy = stats[cls] if cls in stats.columns else 0
        p_y = global_probas[cls]
        smooth = (n_cy + alpha * p_y) / (totals + alpha)
        encoded[f"{col}_enc_{cls}"] = df[col].map(smooth)

    return encoded

def encode_features(df, target_col='account_status', alpha=10):
    df = df.copy()
    dummy_cols = ['gender', 'marital_status', 'employment_status', 
                  'education_level', 'subscription_type', 'age_group']

    df_dummies = pd.get_dummies(df[dummy_cols], prefix=dummy_cols)
    country_enc = target_encode_smooth(df, col='country', target=target_col, alpha=alpha)

    numeric_cols = df.drop(columns=dummy_cols + ['country', target_col]).copy()
    numeric_cols = numeric_cols.astype({col: 'float64' for col in numeric_cols.select_dtypes('int').columns})

    final_df = pd.concat([df_dummies, country_enc, numeric_cols], axis=1)
    final_df[target_col] = df[target_col]
    return final_df


# In[ ]:




