#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             

# PROGRAMMER: Ezra Mulaga
# DATE CREATED: 30/07/2024                                 
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the program run using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    

def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images.
    
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifier labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                    name (starting with 'pct' for percentage or 'n' for count)
                    and the value is the statistic's value.
    """        
    # Initialize counters
    n_images = len(results_dic)
    n_dogs_img = 0
    n_notdogs_img = 0
    n_match = 0
    n_correct_dogs = 0
    n_correct_notdogs = 0
    n_correct_breed = 0
    
    # Iterate through results_dic
    for key in results_dic:
        # Check if image is a dog
        if results_dic[key][3] == 1:
            n_dogs_img += 1
        else:
            n_notdogs_img += 1
        
        # Check if there's a match between pet label and classifier label
        if results_dic[key][2] == 1:
            n_match += 1
        
        # Check if it's a correct dog classification
        if results_dic[key][3] == 1 and results_dic[key][4] == 1:
            n_correct_dogs += 1
        
        # Check if it's a correct non-dog classification
        if results_dic[key][3] == 0 and results_dic[key][4] == 0:
            n_correct_notdogs += 1
        
        # Check if it's a correct breed classification
        if results_dic[key][3] == 1 and results_dic[key][4] == 1 and results_dic[key][2] == 1:
            n_correct_breed += 1
    
    # Calculate percentages
    pct_match = (n_match / n_images) * 100.0 if n_images > 0 else 0.0
    pct_correct_dogs = (n_correct_dogs / n_dogs_img) * 100.0 if n_dogs_img > 0 else 0.0
    pct_correct_breed = (n_correct_breed / n_dogs_img) * 100.0 if n_dogs_img > 0 else 0.0
    pct_correct_notdogs = (n_correct_notdogs / n_notdogs_img) * 100.0 if n_notdogs_img > 0 else 0.0
    
    # Create results_stats_dic
    results_stats_dic = {
        'n_images': n_images,
        'n_dogs_img': n_dogs_img,
        'n_notdogs_img': n_notdogs_img,
        'n_match': n_match,
        'n_correct_dogs': n_correct_dogs,
        'n_correct_notdogs': n_correct_notdogs,
        'n_correct_breed': n_correct_breed,
        'pct_match': pct_match,
        'pct_correct_dogs': pct_correct_dogs,
        'pct_correct_breed': pct_correct_breed,
        'pct_correct_notdogs': pct_correct_notdogs
    }
    
    return results_stats_dic

# This part is for testing the function
if __name__ == "__main__":
    # Dummy data for testing
    results_dict = {
        'image_1.jpg': ['golden retriever', 'golden retriever', 1, 1, 1],
        'image_2.jpg': ['pug', 'bulldog', 0, 1, 1],
        'image_3.jpg': ['cat', 'persian cat', 0, 0, 0],
        'image_4.jpg': ['beagle', 'beagle', 1, 1, 1]
    }
    
    results_stats = calculates_results_stats(results_dict)
    print("Results Statistics:")
    for key, value in results_stats.items():
        print(f"{key}: {value}")