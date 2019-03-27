#!/bin/bash
pwd
for i in {1..20}
do
	cd r8s1.81/src/
	./r8s -f dar_example -b | tail -1 | cut -d " " -f 4 > dar_initial.txt
	cp dar_initial.txt ../../dar1.txt
	cd ../../
	cp dar1.txt Seq-Gen-1.3.4/Seq-Gen-1.3.4/source/dar1.txt
	cp dar1.txt standard-RAxML/dar_initial.txt
	cd Seq-Gen-1.3.4/Seq-Gen-1.3.4/source/
	# If branch length factoring is needed, uncomment line below
        # python3 multiply_branch_length.py dar1.txt 10 
	seq-gen -mHKY -l40 -n1 < dar1.txt > dar_output.txt
	cd ../../../
	cp Seq-Gen-1.3.4/Seq-Gen-1.3.4/source/dar_output.txt standard-RAxML/dar_output.txt
	cd standard-RAxML/
	./raxmlHPC -m GTRGAMMA -p 12345 -s dar_output.txt -n T1
	python3 dar_rf.py >> ../march_research/dar_bf_10.txt
	rm *.T1
	rm dar*.txt
	cd ../
done
