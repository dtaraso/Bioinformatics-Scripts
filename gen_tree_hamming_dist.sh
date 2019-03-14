#!/bin/bash
cd r8s1.81/src/
./r8s
begin rates;
simulate diversemodel=bdback seed=5 nreps=20 ntaxa=5 T=0;
describe tree=0 plot=chrono_description;
end;

cd ../../Seq-Gen-1.3.4/Seq-Gen-1.3.4/source/
seq-gen -mHKY -t3.0 -f0.3,0.2,0.2,0.3 -l40 -n3 < dar1.txt > dar_output.txt


cd ../../../standard-RAxML/ 
./raxmlHPC -m GTRGAMMA -p 12345 -s dar_output.txt -n T1
