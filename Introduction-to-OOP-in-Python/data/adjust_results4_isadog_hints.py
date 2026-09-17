#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog_hints.py
#                                                                             
# PROGRAMMER: Noluthando Buda
# DATE CREATED: 24 August 2026                              
# REVISED DATE: 30 August 2026
# PURPOSE: This is a *hints* file to help guide students in creating the 
#         function adjust_results4_isadog that adjusts the results dictionary
#         to indicate whether or not the pet image label is of-a-dog, 
#         and to indicate whether or not the classifier image label is of-a-dog.
#         All dog labels from both the pet images and the classifier function
#         will be found in the dognames.txt file. We recommend reading all the
#         dog names in dognames.txt into a dictionary where the 'key' is the 
#         dog name (from dognames.txt) and the 'value' is one. If a label is 
#         found to exist within this dictionary of dog names then the label 
#         is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#         could also read all the dog names into a list and then if the label
#         is found to exist within this list - the label is of-a-dog, otherwise
#         the label isn't of a dog. 
#         This function inputs:
#             -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#             -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#             This function uses the extend function to add items to the list 
#             that's the 'value' of the results dictionary. You will be adding the
#             whether or not the pet image label is of-a-dog as the item at index
#             3 of the list and whether or not the classifier label is of-a-dog as
#             the item at index 4 of the list. Note we recommend setting the values
#             at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#             label isn't a dog.
#
##
# TODO 4: EDIT and ADD code BELOW to do the following that's stated in the 
#       comments below that start with "TODO: 4" for the adjust_results4_isadog 
#       function. Specifically EDIT and ADD code to define the 
#       adjust_results4_isadog function. Notice that this function doesn't return
#       anything because the results_dic dictionary that is passed into the 
#       function is a mutable data type so no return is needed.
# 
def adjust_results4_isadog(results_dic, dogfile):
    """Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match)."""           
    # Creates dognames dictionary for quick matching to results_dic labels from
    # real answer & classifier's answer
    dognames_dic = dict()

    # Read dog names into dognames_dic
    with open(dogfile, 'r') as f:
        for line in f:
            dog_name = line.strip().lower()
            if dog_name not in dognames_dic:
                dognames_dic[dog_name] = 1

    # Check each image in results_dic and append [is_dog_pet_label, is_dog_classifier_label]
    for key in results_dic:
        pet_label = results_dic[key][0]
        classifier_label = results_dic[key][1]

        # Check if pet label is a dog
        is_pet_dog = 1 if pet_label in dognames_dic else 0

        # Check if classifier label contains any dog name from dognames_dic
        is_classifier_dog = 0
        for dog_name in dognames_dic:
            if dog_name in classifier_label:
                is_classifier_dog = 1
                break

        # Append index 3 and index 4
        results_dic[key].extend([is_pet_dog, is_classifier_dog])