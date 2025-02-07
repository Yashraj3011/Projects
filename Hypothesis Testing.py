{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c93b6aee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         Theme  Click Through Rate  Conversion Rate  Bounce Rate  \\\n",
      "0  Light Theme            0.054920         0.282367     0.405085   \n",
      "1  Light Theme            0.113932         0.032973     0.732759   \n",
      "2   Dark Theme            0.323352         0.178763     0.296543   \n",
      "3  Light Theme            0.485836         0.325225     0.245001   \n",
      "4  Light Theme            0.034783         0.196766     0.765100   \n",
      "\n",
      "   Scroll_Depth  Age   Location  Session_Duration Purchases Added_to_Cart  \n",
      "0     72.489458   25    Chennai              1535        No           Yes  \n",
      "1     61.858568   19       Pune               303        No           Yes  \n",
      "2     45.737376   47    Chennai               563       Yes           Yes  \n",
      "3     76.305298   58       Pune               385       Yes            No  \n",
      "4     48.927407   25  New Delhi              1437        No            No  \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from scipy.stats import ttest_ind\n",
    "\n",
    "df = pd.read_csv(\"website_ab_test.csv\")\n",
    "\n",
    "print(df.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "13cd89da",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Number of Records': 1000,\n",
       " 'Number of Columns': 10,\n",
       " 'Missing Values': Theme                 0\n",
       " Click Through Rate    0\n",
       " Conversion Rate       0\n",
       " Bounce Rate           0\n",
       " Scroll_Depth          0\n",
       " Age                   0\n",
       " Location              0\n",
       " Session_Duration      0\n",
       " Purchases             0\n",
       " Added_to_Cart         0\n",
       " dtype: int64,\n",
       " 'Numerical Columns Summary':        Click Through Rate  Conversion Rate  Bounce Rate  Scroll_Depth  \\\n",
       " count         1000.000000      1000.000000  1000.000000   1000.000000   \n",
       " mean             0.256048         0.253312     0.505758     50.319494   \n",
       " std              0.139265         0.139092     0.172195     16.895269   \n",
       " min              0.010767         0.010881     0.200720     20.011738   \n",
       " 25%              0.140794         0.131564     0.353609     35.655167   \n",
       " 50%              0.253715         0.252823     0.514049     51.130712   \n",
       " 75%              0.370674         0.373040     0.648557     64.666258   \n",
       " max              0.499989         0.498916     0.799658     79.997108   \n",
       " \n",
       "                Age  Session_Duration  \n",
       " count  1000.000000       1000.000000  \n",
       " mean     41.528000        924.999000  \n",
       " std      14.114334        508.231723  \n",
       " min      18.000000         38.000000  \n",
       " 25%      29.000000        466.500000  \n",
       " 50%      42.000000        931.000000  \n",
       " 75%      54.000000       1375.250000  \n",
       " max      65.000000       1797.000000  }"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "summary = {\n",
    "    'Number of Records': df.shape[0],\n",
    "    'Number of Columns': df.shape[1],\n",
    "    'Missing Values': df.isnull().sum(),\n",
    "    'Numerical Columns Summary': df.describe()\n",
    "}\n",
    "\n",
    "summary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "49c93593",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "             Click Through Rate  Conversion Rate  Bounce Rate  Scroll_Depth  \\\n",
      "Theme                                                                         \n",
      "Light Theme            0.247109         0.255459     0.499035     50.735232   \n",
      "Dark Theme             0.264501         0.251282     0.512115     49.926404   \n",
      "\n",
      "                   Age  Session_Duration  \n",
      "Theme                                     \n",
      "Light Theme  41.734568        930.833333  \n",
      "Dark Theme   41.332685        919.482490  \n"
     ]
    }
   ],
   "source": [
    "theme_performance = df.groupby('Theme').mean()\n",
    "theme_performance_sorted = theme_performance.sort_values(by='Conversion Rate', ascending=False)\n",
    "print(theme_performance_sorted)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "2f1eb843",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(0.4748494462782632, 0.6349982678451778)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "conversion_rates_light = df[df['Theme'] == 'Light Theme']['Conversion Rate']\n",
    "conversion_rates_dark = df[df['Theme'] == 'Dark Theme']['Conversion Rate']\n",
    "t_stat, p_value = ttest_ind(conversion_rates_light, conversion_rates_dark, equal_var=False)\n",
    "t_stat, p_value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b011cb34",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(-1.9781708664172253, 0.04818435371010704)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ctr_light = df[df['Theme'] == 'Light Theme']['Click Through Rate']\n",
    "ctr_dark = df[df['Theme'] == 'Dark Theme']['Click Through Rate']\n",
    "t_stat_ctr, p_value_ctr = ttest_ind(ctr_light, ctr_dark, equal_var=False)\n",
    "t_stat_ctr, p_value_ctr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "5f40227d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Metric</th>\n",
       "      <th>T-Statistic</th>\n",
       "      <th>P-Value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Click Through Rate</td>\n",
       "      <td>-1.978171</td>\n",
       "      <td>0.048184</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Conversion Rate</td>\n",
       "      <td>0.474849</td>\n",
       "      <td>0.634998</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Bounce Rate</td>\n",
       "      <td>-1.201888</td>\n",
       "      <td>0.229692</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Scroll Depth</td>\n",
       "      <td>0.756228</td>\n",
       "      <td>0.449692</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Metric  T-Statistic   P-Value\n",
       "0  Click Through Rate    -1.978171  0.048184\n",
       "1     Conversion Rate     0.474849  0.634998\n",
       "2         Bounce Rate    -1.201888  0.229692\n",
       "3        Scroll Depth     0.756228  0.449692"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bounce_rates_light = df[df['Theme'] == 'Light Theme']['Bounce Rate']\n",
    "bounce_rates_dark = df[df['Theme'] == 'Dark Theme']['Bounce Rate']\n",
    "\n",
    "t_stat_bounce, p_value_bounce = ttest_ind(bounce_rates_light, bounce_rates_dark, equal_var=False)\n",
    "\n",
    "scroll_depth_light = df[df['Theme'] == 'Light Theme']['Scroll_Depth']\n",
    "scroll_depth_dark = df[df['Theme'] == 'Dark Theme']['Scroll_Depth']\n",
    "\n",
    "t_stat_scroll, p_value_scroll = ttest_ind(scroll_depth_light, scroll_depth_dark, equal_var=False)\n",
    "\n",
    "comparison_table = pd.DataFrame({\n",
    "    'Metric': ['Click Through Rate', 'Conversion Rate', 'Bounce Rate', 'Scroll Depth'],\n",
    "    'T-Statistic': [t_stat_ctr, t_stat, t_stat_bounce, t_stat_scroll],\n",
    "    'P-Value': [p_value_ctr, p_value, p_value_bounce, p_value_scroll]\n",
    "})\n",
    "\n",
    "comparison_table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ba9f16d9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
