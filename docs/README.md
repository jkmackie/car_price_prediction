# car_price_prediction
**CraigsList vehicle price prediction with scikit-learn and tensorflow 2.0 libraries**

---

### <ins>Resources</ins>
* **[Notebooks](https://github.com/ageron/handson-ml2) for new <ins>[Hands-on Machine Learning with Scikit-Learn, Keras and TensorFlow 2](https://www.amazon.com/dp/1492032646/ref=cm_sw_r_tw_dp_U_x_HWDQDb0DEX69X)</ins>**
* **[TensorFlow Tutorials](https://www.tensorflow.org/tutorials/)**
* **[TensorFlow Serving with Docker](https://www.tensorflow.org/tfx/serving/docker)**

***
### <ins>Proposed learning</ins>
* **classify image**
* **extract name, address, payee, and amount from invoices**

***
### <ins>vehicle.json</ins>
* start_urls = [https://houston.craigslist.org/search/cta?auto_make_model=ford](https://houston.craigslist.org/search/cta?auto_make_model=ford)
* contains vehicle url, title, price, subLocation (Ex. Katy), attribute dictionary, and image dictionary
***
### start_url screenshot:
![ford_screenshot](cl_ford_query.PNG)


***
### Week 1 Notes
**Research notes October 24 - October 30**
***

Car Price Prediction using Machine  Learning Techniques (Feb19) - ensemble provides much better predictions
* http://www.temjournal.com/content/81/TEMJournalFebruary2019_113_118.pdf

Build, Develop and Deploy a Machine Learning Model to predict cars price using Gradient Boosting (Mar19)
* https://towardsdatascience.com/build-develop-and-deploy-a-machine-learning-model-to-predict-cars-price-using-gradient-boosting-2d4d78fddf09
* https://github.com/PaacMaan/cars-price-predictor/blob/master/cars_price_predictor.ipynb

How to Build, Develop and Deploy a Machine Learning Model to predict cars price using Neural Networks (May19)
* https://medium.com/thelaunchpad/how-to-build-develop-and-deploy-a-machine-learning-model-to-predict-cars-price-using-neural-7f7439a37300

Scrapy spider tutorials:
* https://youtu.be/gGnGnIPgR84


***
### Week 2 Notes - Draft1
**Notes October 31 - November 6**
***

**Scrape car price data from [Craigslist Houston cars+trucks](https://houston.craigslist.org/d/cars-trucks/search/cta)**
* Get 50+ observations per model trim
* Organize the raw features in a database
* Clean the features so they are ready for modeling

**Scrape Filter Details**
* Filtered for dealer ('ctd') or owner ('cto') and make_model='honda'
* start_urls = ['https://houston.craigslist.org/search/cta?auto_make_model=ford']



