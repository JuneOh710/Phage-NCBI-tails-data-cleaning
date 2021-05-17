# Phage-NCBI-tails-data-cleaning
This little python script made my life easier when I had to clean up and extract data from the NCBI protein database for a biochemistry research project. 

## What it does
For each file in the raw_data directory, the script will:
1. Filter the HMM (Name) by each protein family.
2. Count the number of Prot RefSeqs for that family. Record this number as "Total #hits".
3. Filter for E values less than 0.001 and count the Prot RefSeqs that satisfy this condition.
4. Filter for unique Prot RefSeqs and record this number as "Unique hits".
5. Generate a new file containing the totals hits, number of E values less than 0.001 and unique hits.
6. Generate a new file containing the unique Prot RefSeqs and their smallest E values and protein family identity.
7. Move on to the next file in the raw_data directory to repeat steps 1-6.
