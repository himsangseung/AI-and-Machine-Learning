#!/usr/bin/env python
# coding: utf-8

# In[1]:
#SangSeung (Jay) Lee
#Credit to Sari Sadiya

import numpy as np
import sklearn
from sklearn import datasets
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import random
# Get the sklearn digit recognition toy dataset, it contains 569 cases.
# We then take the first 500 to be our training set and the last 69 for testing

# In[2]:

# load the data set
img, label = sklearn.datasets.load_breast_cancer(return_X_y=True)
# split the data set
TRAIN_SIZE = 500
label = 2 * label - 1
train_img, test_img = img[:TRAIN_SIZE], img[TRAIN_SIZE:]
train_label, test_label = label[:TRAIN_SIZE], label[TRAIN_SIZE:]

# In[3]:

# Perceptron Class
class Perceptron(object):
    # Initialize the perceptron
    def __init__(self, dim_input=30, dim_out=2, learning_rate=1):
        self.w = np.zeros(dim_input)
        self.dim_input = dim_input  # dimension of the input (30 for our medical cases)
        self.learning_rate = learning_rate
        self.dim_out = dim_out
        self.dim_weight = dim_out*dim_input
        self.w_multi = np.zeros(shape=(dim_out,dim_input))

    def predict(self, input_array):
        z = np.dot(self.w , input_array)
        if self.dim_out == 2:# binary
            return np.sign(z)  # y
        else: # multi-class
            z = np.argmax(self.w_multi*input_array, axis =None)//self.dim_input
            return z

    def one_update(self, input_array, label):
        y =  self.predict(input_array)
        if y != label and self.dim_out == 2: # binary
            self.w = self.w + self.learning_rate * label * input_array
        elif self.dim_out != 2: #multi-class
            for n in range(self.dim_out):
                if np.max(self.w_multi[label]*input_array) <= np.max(self.w_multi[n]*input_array):
                    self.w_multi[n] -= self.learning_rate* input_array # demote y'
                self.w_multi[label] += self.learning_rate* input_array # promote y



    def train(self, training_inputs, labels):
        print()
        la = labels
        for ii in range(len(training_inputs)):
            self.one_update(training_inputs[ii], labels[ii])

    def test(self, testing_inputs, labels):
        # number of correct predictions
        count_correct = 0
        # a list of the predicted labels the same order as the input
        pred_list = []
        for test_array, label in zip(testing_inputs, labels):
            prediction = perceptron.predict(test_array)
            if prediction == label:
                count_correct += 1
            pred_list.append(prediction)
        accuracy = float(count_correct) / len(test_label)
        print('Accuracy is ' + str(accuracy))
        return np.asarray(pred_list)


# In[4]:


# Number of epochs (iterations over the training set)
NUM_EPOCH = 6

# In[5]:

# Try the perceptron with sigmoid activation
perceptron = Perceptron()
for ii in range(NUM_EPOCH):
    perceptron.train(train_img, train_label)  # Complete!
print('For sigmoid activation and ' + str(NUM_EPOCH) + ' epochs')
pred_array = perceptron.test(test_img, test_label)  # Complete!



# In[6]:


# Confusion matrix shows what we predicted vs what was the real (True) label.
# A perfect classifier will have has non zero elements only in the diagonal (why??)
# Look at the results outside the diagonal, does it make sense that these mistakes happened?
confusion_mat = confusion_matrix((test_label+1)/2, (pred_array+1)/2, labels=range(0,2))
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
cax = ax.matshow(confusion_mat)
plt.title('Confusion Matrix\n')
fig.colorbar(cax)
labels = ['malignant', 'benign']
ax.set_xticklabels(['']+labels)
ax.set_yticklabels(['']+labels)
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

# In[7]:


confusion_mat


# # Extra Credit!!!
# The same simple rule can be applied to multiple classes, update your code to work with any number of classe!

# In[11]:

# load the data set
# This is handwritten digit recognition
img,label=sklearn.datasets.load_digits(return_X_y=True)
TRAIN_SIZE = 1700
# split the data set
train_img,test_img = img[:TRAIN_SIZE], img[TRAIN_SIZE:]
train_label,test_label = label[:TRAIN_SIZE], label[TRAIN_SIZE:]
print()

# As can be observed, each of these train img is an 8x8 pixel grayscale image of a handwritten digit, 
# for instance training image number 47 is of the handwritten digit '1'. 
# We can also verify that the label in the dataset is indeed 1.

# In[12]:


IMG_DIM = (8,8)


# In[13]:


# Try it yourself with any index!
img_idx = 1
plt.matshow(np.reshape(train_img[img_idx],IMG_DIM),cmap='gray')
print('label in the dataset is '+str(train_label[img_idx]))
# In[19]:


perceptron = Perceptron(dim_input=8*8, dim_out=10)
for ii in range(NUM_EPOCH):
    perceptron.train(train_img,train_label)
print('For linear activation and '+str(NUM_EPOCH)+' epochs')
pred_array = perceptron.test(test_img,test_label)

# In[20]:


#########################################################################################
# Confusion matrix shows what we predicted vs what was the real (True) label.
# A perfect classifier will have has non zero elements only in the diagonal (why??)
# Look at the results outside the diagonal, does it make sense that these mistakes happened?
confusion_mat = confusion_matrix(test_label, pred_array, labels=range(0,10))
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
cax = ax.matshow(confusion_mat)
plt.title('Confusion Matrix\n')
fig.colorbar(cax)
labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ax.set_xticklabels(['']+labels)
ax.set_yticklabels(['']+labels)
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()


# In[21]:


# Note the perceptron seems to have misclassified some 3s as 8s, these digits do look similar  
# so this is to be expected.. what else did we misclassify?


# In[ ]:


# In[ ]:
