#for use: this is password list test
#passwordsTest = ["tra","tra","trb","osu","guy","sug", "mos","mou","mosj"]


#class that contain flat function to be used by manager
class Markov:
    #generate and return the frequency matrix
    def generateFrequencyMatrix(self,passwordslist,N):
        frequencyList=[] #contain all the N-grams
        #take each n-gram from the passwordlist  
        for word in passwordslist:
            frequencyList+=[word[x:x+N] for x in xrange(len(word)-N+1)] 
        #build a dictonary instead of matrix
        frequencyMat = {} 
        #fill the dictonary
        for n in frequencyList:
            if n in frequencyMat:
                frequencyMat[n] += 1
            else:
                frequencyMat[n] = 1 #start with 1
        return frequencyMat
    
    
    #return a dictonary with n-1 grams word and the probaility of them   
    def calculateInfinityMatrix(self,FrequncyMatrix,N):
        infinitylist =  []
        for word in FrequncyMatrix:
            infinitylist.append(word[0:-1])
    
        #remove the duplicate of the (n-1)grams by converting to set and then to list
        infinitylist= list(set(infinitylist))
        
        #initialize the InfinityMatrix
        infinityMat = {}
        #sum the (n-1)gram suffix for all the ngrams
        for word in infinitylist:
            frequncyword = [(key, value) for key, value in FrequncyMatrix.items() if word in key[0:-1]]
            infinityMat[word]= sum(int(frequncyword[i][1]) for i in xrange(len(frequncyword)))    
        return infinityMat
     
    #compute the probability of all ngram
    def generateTransitionMatrix(self,FrequncyMatrix,InfinityMatrix,N):
        transitionMat ={}
        #compute the probability of the N-gram divide by total N-1 grams
        for word in FrequncyMatrix:
            transitionMat[word] = float(FrequncyMatrix[word])/InfinityMatrix[word[0:-1]]
        return transitionMat
    
    #compute the probability to generate the password who was given
    def computePobability(self,TransitionMatrix,N,password):
            #take each N-gram of the password
            #    if it isn't exist the probability is :0
            #multiply each other
            
            #check for error
            if (len(password)<N):
                return -1 #means error
            prob= 1.0
            for i in xrange(len(password)-N+1):
                if password[i:i+N] in TransitionMatrix:
    
                    prob=float(prob) * TransitionMatrix[password[i:i+N]]
                else:
                    return 0
            return prob
    
    #disable feature   
    #def addNoise(self,TransitionMatrix,quant):
    #    print "alive"




