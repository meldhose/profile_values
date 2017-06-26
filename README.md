# profile_values

This package provides some basic tools to do data profiling on a pandas DataFrame of values

### Installing
To install this package:

1. First install PyQt5, e.g. using one of the following methods:

  1. If you have Anaconda installed on your machine, then use the following command:

     ```$ conda install pyqt```

  2. Otherwise follow the instructions at http://pyqt.sourceforge.net/Docs/PyQt5/installation.html

2. Then install the package using one of the following methods:

  1. Run the following command:

     ```pip install git+https://github.com/meldhose/profile_values```
	 
  2. First clone the package source code using the following command:

     ```$ git clone https://github.com/meldhose/profile_values```

     Then enter the source code root folder (```profile_values```) and install the package using the following command:

     ```$ python setup.py install```

     You can use ```--prefix``` to change the destination folder for installing the package (see the help using ```$ python setup.py --help```).


## Usage Guide ##

To use this package, import it by running the following python command:

   ```>>> import profile_values as pv```

We are profiling data values on the below four aspects, namely:

1. Detect any potential encoding issues with the data values
2. Analysis on numerical values
  a. Detect if all values are of numerical data type or a hybrid of numerical and other types
  b. Data profiling on the list of numerical values
3. Analysis on the lengths of the data values using histogram
4. Analysis on the string values
  a. Find the unique values in the list
  b. Cluster the list of values

### Detect any potential encoding issues ###

1. First load your data values into a pandas DataFrame with one column using the following command:

   ```>>> data_frame = pd.read_csv('PATH-TO-TEXT-FILE', names=['Attributes'])```
  
   where the file at ```PATH-TO-TEXT-FILE``` contains the data values to be analyzed, one data value per line.

2. Now run the command:

   ```>>> encoding_analysis = encoding_analysis(data_frame)```
  
   This will contain results of the encoding analysis done on the data values.
 
3. The below command lets us know whether there are any unusual characters in the data values
 
    ```>>> encoding_analysis['contains_unusual_chars']```
    
    This returns true if unusual characters are found in the data values that may mean that there is an encoding issue.
  
4. The below command returns DataFrame of values that contain unusual characters.
 
     ```>>> encoding_analysis['unusual_strings']```
     
5. The below command returns DataFrame of values that contain unusual characters along with the unusual characters in them.
 
     ```>>> encoding_analysis['strings_with_unusual_chars']```



###  Analysis on numerical values ###

#### Detect type of the data values ####

1. First load your data values into a pandas DataFrame with one column using the following command:

   ```>>> data_frame = pd.read_csv('PATH-TO-TEXT-FILE', names=['Attributes'])```
  
   where the file at ```PATH-TO-TEXT-FILE``` contains the data values to be analyzed, one data value per line

2. Now run the command:

   ```>>> na = numerical_analysis(data_frame)```

3. The below command lets us know whether the values are of data type numerical or not
 
    ```>>> na['is_numeric']```
    
    This returns true if all values are of data type numeric.
  
4. The below command lets us know whether the values are a combination of numerical and other data types
 
     ```>>> na['is_hybrid']```
     
#### Data profiling on the list of numerical values ####
     
5. The below command returns analysis report of the numerical values like min, max, mean.
 
     ```>>> na['analysis_report']```

### Analysis on the lengths of the data values using histogram ###

1. First load your data values into a pandas DataFrame with one column using the following command:

   ```>>> data_frame = pd.read_csv('PATH-TO-TEXT-FILE', names=['Attributes'])```
  
   where the file at ```PATH-TO-TEXT-FILE``` contains the data values to be analyzed, one data value per line.
   
2. Now run the command:

   ```>>> histogram = histogram_value_lengths(data_frame)```
   
   This returns histogram on length of data values.
   
### Analysis on the string values ###

#### Find the unique values in the data frame ####

1. First load your data values into a pandas DataFrame with one column using the following command:

   ```>>> data_frame = pd.read_csv('PATH-TO-TEXT-FILE', names=['Attributes'])```
  
   where the file at ```PATH-TO-TEXT-FILE``` contains the data values to be analyzed, one data value per line.
   
2. Now run the command:

   ```>>> sa = analyse_strings(data_frame)```
   
   sa will contain results of the string analysis done on the data values.
   
3. The below command gives us the unique data values.
 
    ```>>> sa['unique_values']```
    
    This returns DataFrame of unique data values.
  
4. The below command returns clusters of the data values
 
     ```>>> sa['cluster_values']```


