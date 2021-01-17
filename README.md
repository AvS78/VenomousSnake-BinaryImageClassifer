# VenomousSnake-BinaryImageClassifer
Venemous-Non-Venemous Image Classifier
Identify snakes into venomous/nonvenomous categories. Problem type is classification. Such a classifier can be helpful in:
a)	Reptile interaction and preservation
b)	Trauma Mgmt. (our research suggests that 10-15% of snake bite deaths are related to fear psychosis of being bitten)
c)	Fear free trail runs!

# Database: 
1. Bing API vs Web Scraping
2. Manual expert based data labelling
3. Total images after manual cleaning:
  Total images venomous snakes: 1858
  Total images non venomous snakes: 1745
4. Curated database is available upon request. Else, the code repo provides database creation (requires Bing API access keys)
5. Database was augmented with image transformations - left/right shifts, zoom, color fading, rotations, flip,  etc
6. Every Database image normalized to: 96x96x3 

# Classifier Performance Metrics:
Confusion matrix based F1 score

# Classifiers:
Convolution Neural Networks (CNN) based feature extraction.
Finalized model uses ReLU (Rectified Linear Unit), Learning rate decay of 5%, Batch Normalization, L2 regularization
Finalized Deep Neural Network Model architecture: please see the repo


