# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "The rules don't operate entirely independently. For example, Rule 7 and Rule 2 present conflicting outcomes for individuals who are single and don't own homes"
    answers["(b) explain"] = "The rule set is not exhaustive. Let's say we have a new entry where the individual is a homeowner, divorced, with low annual income, and currently unemployed. None of the existing rules can generate this scenario."
    answers["(c) explain"] = "Ordering might be crucialfor this rule set to prioritize more specific rules over general ones. For instance, applying Rule 7 before Rule 2 helps accurately classify single individuals who are not homeowners."
    answers["(d) explain"] = "Having a default class could be necessary for cases where none of the rules apply. This default class acts as a fallback classification when the specified conditions are not met, providing a safety net."

    return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "yes"
    answers["(b)"] = "no"
    answers["(c)"] = "no"

    # explain-string: explanation in english prose
    answers["(a) example"] = "In order to ensure that the rules are mutually exclusive, it's important to have no overlap between the conditions. They seem mutually exclusive as they classify distinct groups such as birds, fishes, mammals, and reptiles, each based on unique combinations of attributes."
    answers["(b) example"] = "The absence of a rule covering amphibians means that under the provided rules, a salamander wouldn't be classified. This highlights that the rules aren't exhaustive since they fail to classify every vertebrate in the dataset."
    answers["(c) example"] = "Since each rule assigns a distinct group without any overlap, the order in which they're applied won't change the classification outcome. As a result, there's no need to concern oneself with the sequence of these rules."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = True
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = False

    # explain_string: explanation in english prose
    answers["(a) explain"] = "The back-propagation algorithm efficiently computes gradients by recursively applying the chain rule of calculus. It propagates the gradient of the loss from the output layer backward through the network, utilizing each subsequent layer's gradient to compute the gradient of the preceding layer."
    answers["(b) explain"] = "Each layer's output is derived from the activations of the previous layer through weighted sums and activation functions. This creates a direct computational chain from the input layer to the output layer."
    answers["(c) explain"] = "The vanishing gradient problem arises when gradients diminish significantly as they traverse through the layers of a deep neural network during training. This can lead to slow or halted learning in the initial layers. It's characterized by training errors diminishing to zero while test errors remain substantial. However, it's important to note that this phenomenon is indicative of overfitting, not the vanishing gradient problem."
    answers["(d) explain"] = "The statement is largely inaccurate because achieving perfect classification doesn't guarantee zero gradients for all weights in a neural network. Gradients are influenced by various factors such as loss and activation functions, and even minor deviations or numerical precision issues can result in non-zero gradients. These non-zero gradients are essential for continued learning and refinement of the network."

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.41
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "yes"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.5
    answers["(c) P(X_2=1 | -)"] = 0.32
    answers["(c) P(X_3=1 | +)"] = 0.4
    answers["(c) P(X_3=1 | -)"] = 0.16

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = ""
    answers["(d) Row 2"] = ""
    answers["(d) Row 3"] = ""
    answers["(d) Row 4"] = ""

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.0

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 5
    answers["(b) K"] = 50

    # explain_string
    answers["(a) explain"] = "The choice of k=5 strikes a balance between generalization and sensitivity to local data structure by considering multiple neighbors. This approach helps to reduce the impact of noise and outliers while being less susceptible to random fluctuations compared to k=1. Moreover, k=5 avoids oversmoothing the local class information, a pitfall that can occur with larger values such as k=50"
    answers["(b) explain"] = "In cases where there is significant overlap between classes, opting for a larger value of k could be advantageous. This choice would lessen the reliance on immediate neighbors, which might be misleading due to the overlap. By considering a larger number of neighbors, a more stable decision boundary could be achieved in regions where classes blend together."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.6
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.8
    answers["(a) P(A=1|-)"] = 0.4
    answers["(a) P(B=1|-)"] = 0.4
    answers["(a) P(C=1|-)"] = 0.2

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = ""
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 0.0 
    answers["(b) P(R|+)"] = 0.0
    answers["(b) P(R|-)"] = 0.0

    # string, '+' or '-'
    answers["(b) class label"] = "+"

    # explain_string
    answers["(b) Explain your reasoning"] = ""
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.4
    answers["(c) P(A=1,B=1)"] = 0.2

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = "yes"
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.6
    answers["(d) P(A=1,B=0)"] = 0.3

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = "yes"
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.2
    answers["(e) P(A=1|+)"] = 0.6
    answers["(e) P(B=1|+)"] = 0.4

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = "no"

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  ""
  
    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    #answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    #answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
