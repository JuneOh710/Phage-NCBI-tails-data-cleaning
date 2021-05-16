import pandas as pd

with open("file_names.txt") as file_name:
    file_name_list = file_name.readlines()

for long_file_name in file_name_list:
    long_file_name = long_file_name.rstrip()
    # long_file_name = input("File name: ")
    df = pd.read_csv("raw_data/" + long_file_name)
    file_name = long_file_name.split(" - ")[1].split(".")[0]

    # with open("Name.txt") as name_column:
    #     name_list = name_column.readlines()

    with open(f"processed_data/{file_name}.csv", "w") as f:
        f.write("Name, Total #hits, <0.001, Unique hits\n")

    family_list = set(df["Name "].to_list())
    for protein_name in family_list:
        family = protein_name.rstrip()
        seq_list = df[df["Name "] == family]["Prot RefSeq"].to_list()
        seq_set = set(seq_list)  # unique hits

        e_value_list = df[df["Name "] == family]["E value "].to_list()
        processed_evl = []
        for e_val in e_value_list:
            if float(e_val) < 0.001:
                processed_evl.append(e_val)

        msg = f"{protein_name}, {len(seq_list)}, {len(processed_evl)}, {len(seq_set)}\n"

        with open(f"processed_data/{file_name}.csv", "a") as outfile:
            outfile.write(msg)

    clean_df = df[["Prot RefSeq", "Name ", "E value "]]
    seq_map = {}  # will map RefSeq to [Name, min(E value)]
    for (i, row) in clean_df.iterrows():
        if row["Prot RefSeq"] not in seq_map:
            seq_map[row["Prot RefSeq"]] = [row["Name "], row["E value "]]
        else:
            e_val = min(row["E value "], seq_map[row["Prot RefSeq"]][1])
            seq_map[row["Prot RefSeq"]] = [row["Name "], e_val]

    csv_msg = "Prot RefSeq, Name, E Value\n"  # header of the csv
    for ref in seq_map:
        csv_msg += f"{ref}, {seq_map[ref][0]}, {seq_map[ref][1]}\n"

    with open(f"processed_data/{file_name}_uniques.csv", "w") as csv_out:
        csv_out.write(csv_msg)
