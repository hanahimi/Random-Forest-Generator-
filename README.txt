Data Mining Project: Random Forest Generation

-Anthony Ittiyera Vazhappilly

-01596046



Goal: The aim of our project is to build a random forest based on Ensemble Classificstion. Each Decision tree in the random forest will work on set of randomly seleted attributes 
      from all the attributes.
A bootstrap sample is taken as a trainging set from the whole set provided to us and each tree is trained based on that sample.



Implementations: 
    
	RandomForest.py- In the init function we intialize the forest array to which we will be adding our decision trees.

                         In the train function we start creating our decision trees. For each tree i chose 10 attributes from the total attributes provided to us and also 
			 a bootstrap set of 300
 records to train the decision tree. We then create and add the Decision Tree object to the forest arrray, I also pass the 
			 selected attributesand bootstrap training set to the train function of the decision tree.
                   
                         The predict function is where i predict the label for the rows provided. The prediction from each decision tree in the forest array is taken and
			 the numbers for 'e' and 
'p' are counted. The one with the majority is given as the predicted value for the record.

                         The bootstrap function chooses 300 records with replacement from the trainging records provided to us.
  
    
        DecisionTree.py-  The init function intializes the root for the decison tree.
  
                          The train function recieves the training records and the attributes. This is assigned to the root of the tree. THis function then calls the tree_growth
                          function to begin branching out. 
                    
		          The tree_growth function is where the the records get split based on the best attribute and where the leaf node is created based on the stopping_cond().
                          This iterates through all attributes and for each value in the attribute it performs a split by calling the split_set. Once the split is completed the we 
                          calculate the entropy and gain
 of the split sets. For each set of records the best attribute and the best value in the attribute is selected as the 'splitPoint' 
                          and the sets which are split become the left and right branch of the current node. The splitPoint is chosen based the maximum gain from all possible splits. 
                          The max gain is also used by my stopping_cond(). If my max gain is zero it creates the leaf node.

                          The createLeaf() creates the leaf by giving the label a value of either 'p' or 'e'.
        
                          The predict function predicts the label for the leaf node. It iterates through the tree and based on the attribute value provided in the splitPoint as it 
                          reaches the leaf
 node it returns the label value of the leaf.
 
Execution:
          First we enter the folder "Random Forest"
                
          Then Run the command "python src/main.py -m 1 -t data/mushrooms_train.data -e data/mushrooms_test.data -n 20" 
          to compile and execute the random forest.



Summary: I have run and executed the random project without any errors. Using the test and training data provided in the project foders i am getting an accuracy of nearly 100%.

        
    

