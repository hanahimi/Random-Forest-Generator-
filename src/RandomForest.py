import random
from DecisionTree import DecisionTree
class RandomForest(object):
    """
    Class of the Random Forest
    """
    def __init__(self, tree_num):
        self.tree_num = tree_num
        # intialize the forest array
        self.forest = []

    def train(self, records, attributes):
        # we start creating decision trees for our random forest
               
        for treeId in range(0,self.tree_num):
            # select 10 attributes from the entire attribute list provided to us
            selectedAttri=random.sample(attributes,10)
            # create the training set for each tree using bootstrap
            sampleSet=self.bootstrap(records)
            # add the tree object to the forest
            self.forest.append(DecisionTree())
            # start the train to train  
            self.forest[treeId].train(sampleSet, selectedAttri)

              


        


    def predict(self, sample):
        # this is where we get the classifications of all the decision trees in the random forest
        # the majority is taken as the predicted label for the record
        c1=c2=0
        for treeId in range (0, self.tree_num):
            classification = self.forest[treeId].predict(sample)
            if(classification == "e"):
                c1+=1
            else:
                c2+=1
        if c1 > c2:
            return "e"
        return "p"

    def bootstrap(self, records):
        # this createsa sample set, with replacement, of 400 for each decision tree
        sample=[]
        for recNum in range(0,400):
            sample.append(records[random.randint(0,len(records)-1)])
        return sample
