<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/RaulMaya/Kepler-Telescope-Search">
    <img src="readme_resources/nasa.png" alt="Logo" width="195" height="150">
  </a>

  <h2 align="center">Kepler Telescope Search</h2>

  <p align="center">
    Developing classification machine learning models using <a href="https://scikit-learn.org/stable/">sklearn</a>, to discover hidden planets outside of our solar system, using data collected by the NASA Kepler space telescope.
    <br />
    <br />
    <a href="https://www.kaggle.com/nasa/kepler-exoplanet-search-results">Data Source</a>
    ·
    <a href="https://github.com/RaulMaya/Kepler-Telescope-Search/tree/master/models">Explore the docs</a>
    ·
    <a href="https://github.com/RaulMaya/Kepler-Telescope-Search/tree/master/data">CSV File</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
### About The Project

![exoplanets.jpg](readme_resources/kepler.jpg)

Over a period of nine years in deep space, the NASA Kepler space telescope has been out on a planet-hunting mission to discover hidden planets outside of our solar system.

To help process this data, you will create machine learning models capable of classifying candidate exoplanets from the raw dataset.


<p align="right">(<a href="#top">back to top</a>)</p>


### Selected Models

This section lists the selected machine learning models, for future evaluations between all the listed models, once evaluated, it can be selected which models are good enough to predict new exoplanets, and which model is the best to predict them.

* [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html?highlight=logistic#sklearn.linear_model.LogisticRegression)
* [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC)
* [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html?highlight=kneighbors#sklearn.neighbors.KNeighborsClassifier)
* [Decision Tree](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html?highlight=decision%20tree#sklearn.tree.DecisionTreeClassifier)
* [Random Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html?highlight=random%20forest#sklearn.ensemble.RandomForestClassifier)

<p align="right">(<a href="#top">back to top</a>)</p>

### Model Comparison

<div align="center">

| Model      | Scaling         | Best Parameters | Accuracy   | Features  |
| ------------- | ------------- | ----- | ---- | ---- |
| LogisticRegression | MinMaxScaler | C: 78.47599703514607, max_iter: 1000, multi_class: multinomial, penalty: l2, solver: lbfgs | 85.56 %  | 10 |
| SVC     | MinMaxScaler      | C: 10,  gamma: 0.0001| 86.51% | 15 |
| KNeighborsClassifier | MinMaxScaler | n_neighbors: 16   | 82.79 % | 40  |
| Decision Tree | MinMaxScaler | criterion: entropy, max_leaf_nodes: 19, min_sample_split: 2 | 88.32 % | 7  |
| Random Forest | MinMaxScaler | n_estimators: 500 | 87.31 % | 16 |

</div>

<p align="right">(<a href="#top">back to top</a>)</p>

### Contact :iphone:

* Name: Raul Maya Salazar
* Phone: +52 833 159 7006
* E-mail: raulmayas20@gmail.com
* GitHub: https://github.com/RaulMaya
* LinkedIn: https://www.linkedin.com/in/raul-maya/
