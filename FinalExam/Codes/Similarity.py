from sematch.semantic.similarity import WordNetSimilarity
L1=[]
L2=[]
L3=[]
wns = WordNetSimilarity()

# Computing English word similarity using Li method
x=wns.word_similarity('programmer', 'coder', 'software engineer')
if(x>0.7):
    L1.append('programmer')
    L1.append('coder')
    L1.append('software engineer')
else:continue
    
    
# Computing english word similarity using Li method
wns.word_similarity('softwrae program', 'computer software', 'software system')
if(x>0.7):
    L1.append('software program')
    L1.append('computer software')
    L1.append('software system')
else:continue
