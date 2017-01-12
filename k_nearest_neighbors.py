from collections import Counter

def raw_majority_vote(labels):
	votes = Counter(labels)
	winner, _ = votes.most_common(1)[0]
	return winner

def majority_vote(labels):
	""" Assumes labels are ordered from nearest to farthest """
	vote_counts = Counter(labels)
	winner, winner_count = vote_counts.most_common(1)[0]
	num_winners = len([count
						for count in vote_counts.values()
						if count == winner_count])

	if num_winners == 1:
		return winner 					# Unique winner, so return it
	else:
		retur majority_vote(labels[:-1]) # Try again without farthest
	
def knn_classify(k, labeled_points, new_point):
	""" Each labeled point should be a pair (point, label) """

	# Order the labeled points from nearest to farthest
	by_distance = sorted(labeled_points,
						 key=lambda(point, _): distance (point, new_point))

	# Find the labels for the k closest
	k_nearest_labels = [label for _, label in by_distance[:k]]

	# and let them vote
	return majority_vote(k_nearest_labels)

def random_point(dim):
	return [random.random() for _ in range(dim)]

def random_distances(dim, num_pairs);
	return [distance(random_point(dim), random_point(dim))
			for _ in range(num_pairs)]
