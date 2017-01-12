import functools
import math

from collections import Counter, defaultdict

def entropy(class_probs):
	"""
	Given a list of class probs, comput the entropy
	"""
	return sum(-p * math.log(p,2) for p in class_probs if p)

def class_probs(labels):
	total_count = len(labels)
	return [count / total_count for count in Counter(labels).values()]

def data_entropy(labeled_data):
	labels = [label for _, label in labeled_data]
	probs = class_probs(labels)
	return entropy(probs)

def partition_entropy(subsets):
	"""
	Find the entropy fromthis partition of data int o subsets
	subsets is a list of lists of labeled data
	"""

	total_count = sum(len(subset) for subset in subsets)

	return sum(data_entropy(subset) * len(subset) / total_count
				for subset in subsets )

inputs = [
		({'level':'Senior', 'lang':'Java', 'tweets':'no', 'phd':'no'}, False),
		({'level':'Senior', 'lang':'Java', 'tweets':'no', 'phd':'yes'},	False),
		({'level':'Mid', 'lang':'Python', 'tweets':'no', 'phd':'no'}, True),
		({'level':'Junior', 'lang':'Python', 'tweets':'no', 'phd':'no'}, True),
		({'level':'Junior', 'lang':'R', 'tweets':'yes', 'phd':'no'}, True),
		({'level':'Junior', 'lang':'R', 'tweets':'yes', 'phd':'yes'}, False),
		({'level':'Mid', 'lang':'R', 'tweets':'yes', 'phd':'yes'},	True),
		({'level':'Senior', 'lang':'Python', 'tweets':'no', 'phd':'no'}, False),
		({'level':'Senior', 'lang':'R', 'tweets':'yes', 'phd':'no'},True),
		({'level':'Junior', 'lang':'Python', 'tweets':'yes', 'phd':'no'}, True),
		({'level':'Senior', 'lang':'Python', 'tweets':'yes', 'phd':'yes'}, True),
		({'level':'Mid', 'lang':'Python', 'tweets':'no', 'phd':'yes'},	True),
		({'level':'Mid', 'lang':'Java', 'tweets':'yes', 'phd':'no'}, True),
		({'level':'Junior', 'lang':'Python', 'tweets':'no', 'phd':'yes'}, False)
]

def partition_by(inputs, attribute):
	"""
	Each input is a pair (attribute_dict, label)
	returns a dict : attribute_value -> inputs	
	"""
	groups = defaultdict(list)
	for input in inputs:
		key = input[0][attribute]	# Get the value of the specified attribute
		groups[key].append(input)	# Then add this input to the correct list
	return groups

def partition_entropy_by(inputs, attribute):
	"""
	Compute the entropy corresponding to the given partition
	"""

	partitions = partition_by(inputs, attribute)
	return partition_entropy(partitions.values())

for key in ['level', 'lang', 'tweets', 'phd']:
	print(key, partition_entropy_by(inputs, key))

print("_______________________________________________")
senior_inputs = [(input, label)
				for input, label in inputs if input["level"] == "Senior"]
for key in ['lang', 'tweets', 'phd']:
	print (key, partition_entropy_by(senior_inputs, key))

def classify(tree, input):
	# If this is a leaf node, return its value
	if tree in [True, False]:
		return tree

	# Otherwise, this tree consists of an attribute to split on 
	# and a dictionary whose keys are values of that attribute
	# and whose values of are subtrees to consider next
	attribute, subtree_dict = tree
	
	subtree_key = input.get(attribute) 	# None if input is missing attribute
	
	if subtree_key not in subtree_dict: # if no subtree for key, use None
		subtree_key = None

	subtree = subtree_dict[subtree_key] # Choose appropriate subtree
	return classify(subtree, input)

def build_tree_id3(inputs, split_candidates=None):
	# If first pass, all keys of first input are split candidates
	if split_candidates is None:
		split_candidates = inputs[0][0].keys()
	
	# Count Trues and False in the inputs
	num_inputs = len(inputs)
	num_trues = len([label for item, label in inputs if label])
	num_falses = num_inputs - num_trues

	if num_trues == 0: return False 	# No Trues, return False leaf
	if num_falses == 0: return True		# No Falses, return True laef

	if not split_candidates:			# If no split candidates, return majority
		return num_trues >= num_falses

	# Otherwise, split on best attribute
	best_attribute = min(split_candidates, key=functools.partial(partition_entropy_by, inputs))

	partitions = partition_by(inputs, best_attribute)
	new_candidates = [a for a in split_candidates
					  if a != best_attribute] 

	# Recursively build subtree
	subtrees = { attribute_value : build_tree_id3(subset, new_candidates)
				for attribute_value, subset in partitions.items() }
	
	subtrees[None] = num_trues > num_falses 	# default case

	return (best_attribute, subtrees)

print("_______________________________________________")
tree = build_tree_id3(inputs)

print (classify(tree, {"level" : "Junior",
					   "lang"  : "Java",
					   "tweets": "yes",
					   "phd"   : "no"} ))

print (classify(tree, {"level" : "Junior",
					   "lang"  : "Java",
					   "tweets": "yes",
					   "phd"   : "yes"} ))

print (classify(tree, {"level" : "Intern"} ) )
print (classify(tree, {"level" : "Senior"} ) )
