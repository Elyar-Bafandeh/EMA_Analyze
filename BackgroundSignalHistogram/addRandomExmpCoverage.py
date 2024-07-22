import random
def addRandomCoverage(input_bed_dir ,output_bed_dir):
    with open(input_bed_dir , "r") as inp_file, open(output_bed_dir , "w") as out_file:
        for line in inp_file:
            new_line = line.strip()
            new_line = new_line + f"\t{random.randint(10,100)}\n"
            out_file.write(new_line)

def main():
    addRandomCoverage("BackgroundSignalHistogram\exmpBed.bed" , "BackgroundSignalHistogram\exmpBedCov.bed")

main()
