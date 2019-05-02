###########################################################
# CSE 491 HW 6 -- To Catch A Serial Killer
# Daria Tarasova
###########################################################


def find_min_distance(tree):
	shortest_dist_val = 10000000
	shortest_dist_key = 0
	for k,v in tree.items():
		if v < shortest_dist_val and v != 0:
			shortest_dist_val = v
			shortest_dist_key = k

	return shortest_dist_key



def restructure_upgma_tree(new_dict, tree, count): 	
# tree -> key = (person1,person2) value = distance (24)
# tup -> (person1, person2)
# count -> int

new = new_dict[:]
tup = tree[count]
new.remove(tup)
person1 = tup[0]
person2 = tup[1]
for k,v in tree.items():
	if person1 in k:
		# get weight for each person 
		weight_person1 = person1.count('>')
		weight_person2 = person2.count('>')


		other_person = k[0] if k.index(person1) == 1 else k[1]

		person2_dist = tree.get((other_person,person2))
		if person2_dist == None:
			person2_dist = tree.get((person2,other_person))
			new.remove((person2,other_person))
		else:
			new.remove((other_person,person2))

		new_distance = ((weight_person1*v)+(weight_person2*person2_dist))/(weight_person1+weight_person2)

		new[((person1,person2), other_person)] = new_distance

		new.remove(k)

return new


def parse_sequence_data(file1):

	seq_dict = {}
	while True:
	    line1 = file1.readline()
	    line2 = file1.readline()
	    if len(line1) == 0:
	    	break
	    seq_id = line1.strip()[1:]
	    seq_dict[seq_id] = line2.strip()

	return seq_dict


def compute_distance_matrix(db_dict, query_dict):

	hamming_distance_dict = {}
	for k,v in query_dict.items():
		db_dict[k] = v

	for k,v in db_dict.items():
		for kk, vv in db_dict.items():
			hamming_distance = 0
			for i in range(len(vv)):
				if v[i] != vv[i]:
					hamming_dist += 1
			hamming_distance_dict[(k,kk)] = hamming_dist

	return hamming_distance_dict


def infer_phylogeny(hd_dict):      # key = (person1,person2) value = distance (24)
	# Create n clusters, each containing a single taxon
	tree = {}     # key = random count (1)   value = (person1,person2)
	count = 0
	new_dict = hd_dict
 	while len(new_dict) != 0: # iterate until one cluster remains
 		tree[count] = find_min_distance(new_dict)
 		new_dict = restructure_upgma_tree(new_dict, tree, count)
 		count += 1

 return tree[count]

def output_phylogeny(tree):
	return str(tree)+';'

def main():
	# Step 3
	database_seq_file = open('database-sequences.fasta')
	query_seq_file = open('query-sequence.fasta')

	# Step 4
	database_dict = parse_sequence_data(database_seq_file)
	query_dict = parse_sequence_data(query_seq_file)

	# Step 5
	hamming_distance_dict = compute_distance_matrix(database_dict,query_dict)

	# Step 6
	tree = infer_phylogeny(hamming_distance_dict)

	# Step 7
	newick_string = output_phylogeny(tree)

main()