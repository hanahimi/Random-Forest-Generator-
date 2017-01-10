import math
class TreeNode(object):
    def __init__(self, isLeaf=False):
        # Your code here
        """block"""

    def predict(self, sample):
        """
        This function predicts the label of given sample
        """
        # Your code here

     
    
class DecisionTree(object):
    """
    Class of the Decision Tree
    """
    def __init__(self):
        self.root = None

    def split_set(self,records,column,value):
        # splits the records in two sets based on
        # the value of the attribute
        set1=[]
        set2=[]
        for row in records:
            if row['attributes'][column]==value:
                set1.append(row)          
            else:
                set2.append(row)
       
        return (set1,set2)

    def infoGain(self,records,set1,set2):
        # based on the entropy for each set
        # we can calculate thee gain
        # greater the gain for for the records means the split is good
        eP=self.entropy(records)
        e1=self.entropy(set1)
        e2=self.entropy(set2)
        
        
        pC1=float(len(set1))/float(len(records))
        pC2=float(len(set2))/float(len(records))
        return eP-(pC1*(e1)+pC2*(e2))


    def entropy(self,record):
        # Entropy lets us know how pure a set is 
        # we calculate the entropy based on the label value
        # lower the entropy of a set means its more pure
        if(len(record))!=0:
            c1=0.0
            c2=0.0
            for row in record:
                if row['label'][0]=='p':
                    c1+=1          
                else:
                    c2+=1
            
            pC1=c1/(c1+c2)
            pC2=c2/(c1+c2)
            if (pC1==0 or pC2==0):
                e1=0
            else:
                e1=-1.0*((pC1)*math.log(pC1,2)+(pC2)*math.log(pC2,2))
            return e1
        return 0.0



    def createLeaf(self,recs):
        #  here we count the number of 'P' and 'e' in the records
        #  return the label with the majority count
        c1=0
        c2=0
        for row in recs:
            if row['label'][0]=='p':
                c1+=1          
            else:
                c2+=1
        if(c1<c2):
            return "e"
        else:
            return "p"
    def train(self, records, attributes):
        
        # This is where we intialize the root with all the records        
        self.root=self.tree_growth(records,attributes)

              
    def predict(self, sample):
        
        current = self.root
        
        flag = 0
        # this loop iterates through the tree till it finds the leaf node
        while flag==0:
            if(current.get("label") == None):
                # current["spliInfo"][0] gives the attribut number of the split
                # current["spliInfo"][1] gives the values based on which the split has occured
                if sample["attributes"][current["spliInfo"][0]] == current["spliInfo"][1]:
                    current = current["left"]
                else:
                    current = current["right"]
            else:
                # means this nodes is a leaf node
                flag = 1
        return current["label"]

    def stopping_cond(self, InfoGain):
        # check if the Info Gain is zero
        if(InfoGain==0):
            return True
        else:
            return False

    def tree_growth(self,records,attributes):
        # creates the node for the decision tree
        node={}
        maxIG=0.0
        split1=None
        spit2=None
        splitPoint=(0,'')
        # iterates through all the attributes and the values in the records
        for col in attributes:
            # store the values of the attributes in the dictionary so we use them once
            unique_val={}
            for row in records:
                unique_val[row['attributes'][col]]=1
            for val in unique_val:
                # splits the record
                (set1,set2)=self.split_set(records,col,val) 
                # calculates the information gain for the spilt
                iG=self.infoGain(records,set1,set2)
                # this condition makes sure that we save the best splits
                #  and the best attribute value the split occured
                if(iG>=maxIG):
                    
                    maxIG=iG
                    split1=set1
                    split2=set2
                    splitPoint=(col,val)
        # stores the points of the best split
        node["spliInfo"]=splitPoint
        # the stopping condition for the node of the decision tree
        if(self.stopping_cond(maxIG)):
            # creates the leaf by assigning a value to the label
            node["label"]=self.createLeaf(records)
        else:
            # creates new branches
            node["left"]=self.tree_growth(split1,attributes)
            node["right"]=self.tree_growth(split2,attributes)
        return node